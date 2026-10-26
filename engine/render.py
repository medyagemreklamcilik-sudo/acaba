"""acaba.nolurdu dikey (1080x1920) belgesel renderer.

Kullanım: VIDEO_DIR=videolar/<klasör> python3 engine/render.py <outdir> [workers] [still_t1,still_t2]
Video klasöründe scenes.py, img/ ve build/aligned.json bulunur.

Clean editorial look: punchy keyframed camera moves, varied transitions
(push, bars, iris, diagonal wipe, zoom-blur, spin, glitch), black/yellow
caption pills, kinetic type, animated arrow/circle callouts, split screens,
picture-in-picture cards. Everything is laid out inside the platform safe
zone (top ~230 px, bottom ~420 px and right ~130 px are kept clear).
"""
import json, math, os, subprocess, sys
from functools import lru_cache
from multiprocessing import Process

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

VID = os.path.abspath(os.environ["VIDEO_DIR"])
sys.path.insert(0, VID)
import scenes as S

W, H, FPS = 1080, 1920, 30
ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(VID, "img")
FONTS = os.path.join(ROOT, "fonts")
BUILD = os.path.join(VID, "build")
ASSETS = os.path.join(ROOT, "assets")
YEL = (255, 214, 10)
RED = (255, 45, 45)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SAFE_L, SAFE_R = 64, 950          # usable x range (right side keeps clear of buttons)
CX = (SAFE_L + SAFE_R) / 2


# ---------------------------------------------------------------- helpers
def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def ease(p):
    p = clamp(p)
    return p * p * (3 - 2 * p)


def eout(p, k=3):
    p = clamp(p)
    return 1 - (1 - p) ** k


def ein(p, k=3):
    p = clamp(p)
    return p ** k


def back_out(p, s=1.7):
    p = clamp(p) - 1
    return p * p * ((s + 1) * p + s) + 1


def tr_upper(s):
    return s.replace("i", "İ").replace("ı", "I").upper()


@lru_cache(None)
def font(name, size, weight=None):
    path = {"mont": "Montserrat[wght].ttf", "anton": "Anton-Regular.ttf",
            "play": "PlayfairDisplay-Italic[wght].ttf", "caveat": "Caveat[wght].ttf",
            "amiri": "Amiri-Bold.ttf", "mono": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"}[name]
    f = ImageFont.truetype(path if path.startswith("/") else os.path.join(FONTS, path), size)
    if weight is not None:
        try:
            f.set_variation_by_axes([weight])
        except OSError:
            pass
    return f


def grade(im, kind):
    a = np.asarray(im.convert("RGB")).astype(np.float32) / 255.0
    lum = a @ np.array([0.299, 0.587, 0.114], np.float32)
    sat = {"bw": 0.0, "dark": 0.55, "cold": 0.5}.get(kind, 1.05)
    a = lum[..., None] + (a - lum[..., None]) * sat
    # modern teal/orange split-tone
    sh = np.clip(1 - lum * 1.6, 0, 1)[..., None]
    hi = np.clip(lum * 1.6 - 0.6, 0, 1)[..., None]
    if kind not in ("bw",):
        a = a + sh * np.array([-0.02, 0.01, 0.035]) + hi * np.array([0.035, 0.012, -0.03])
    if kind == "cold":
        a = a * np.array([0.92, 0.98, 1.06])
    a = np.clip(a, 0, 1)
    a = np.clip((a - 0.5) * 1.12 + 0.5, 0, 1)          # contrast
    if kind in ("dark", "bw", "cold"):
        a = a * 0.7
    return Image.fromarray((a * 255).astype(np.uint8))


@lru_cache(80)
def load(key, kind="std"):
    spec = S.IMAGES[key]
    fn, crop = spec if isinstance(spec, tuple) else (spec, None)
    im = Image.open(os.path.join(IMG, fn)).convert("RGB")
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
    # cap working size for speed
    m = max(im.size)
    if m > 2600:
        s = 2600 / m
        im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    return grade(im, kind)


@lru_cache(40)
def blur_bg(key, kind):
    im = load(key, kind)
    s = max(W / im.width, H / im.height) * 1.1
    small = im.resize((max(1, int(im.width * s / 10)), max(1, int(im.height * s / 10))), Image.BILINEAR)
    small = small.filter(ImageFilter.GaussianBlur(5))
    big = small.resize((int(im.width * s), int(im.height * s)), Image.BILINEAR)
    l, t = (big.width - W) // 2, (big.height - H) // 2
    big = big.crop((l, t, l + W, t + H))
    return Image.blend(big, Image.new("RGB", (W, H), (8, 8, 10)), 0.45)


def view(im, cx, cy, scale, out=(W, H), rot=0.0):
    """Render so that source point (cx,cy) is at output centre, scaled, optionally rotated."""
    ow, oh = out
    a = 1.0 / scale
    if rot:
        c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        m = (a * c, a * s, 0, -a * s, a * c, 0)
        m = (m[0], m[1], cx - (m[0] * ow / 2 + m[1] * oh / 2), m[3], m[4], cy - (m[3] * ow / 2 + m[4] * oh / 2))
        return im.transform(out, Image.AFFINE, m, resample=Image.BILINEAR)
    return im.transform(out, Image.AFFINE, (a, 0, cx - ow / 2 * a, 0, a, cy - oh / 2 * a), resample=Image.BILINEAR)


def kf_interp(kfs, t):
    """Keyframes: list of (time, zoom, fx, fy). Eased between keys."""
    if t <= kfs[0][0]:
        return kfs[0][1:]
    for a, b in zip(kfs, kfs[1:]):
        if a[0] <= t <= b[0]:
            p = ease((t - a[0]) / max(1e-6, b[0] - a[0]))
            return tuple(x + (y - x) * p for x, y in zip(a[1:], b[1:]))
    return kfs[-1][1:]


def punch(t):
    z = 1.0
    for pt in S.PUNCH:
        d = t - pt
        if 0 <= d < 0.6:
            z += 0.06 * math.exp(-d * 8) * (1 - math.exp(-d * 60))
    return z


# ---------------------------------------------------------------- scene renderers
def cover_params(sc, t):
    if "kf" in sc:
        z, fx, fy = kf_interp(sc["kf"], t)
        return z, fx, fy
    start, end = sc["t"], sc["_end"]
    p = (t - start + 0.2) / (end - start + 0.4)
    z0, z1 = sc.get("zoom", (1.0, 1.12))
    f0 = sc.get("from", sc.get("focus", (0.5, 0.4)))
    f1 = sc.get("to", sc.get("focus", (0.5, 0.4)))
    q = ease(p) if sc.get("ease", False) else clamp(p)
    return z0 + (z1 - z0) * q, f0[0] + (f1[0] - f0[0]) * q, f0[1] + (f1[1] - f0[1]) * q


def r_cover(sc, t):
    im = load(sc["img"], sc.get("grade", "std"))
    z, fx, fy = cover_params(sc, t)
    z *= punch(t)
    s0 = max(W / im.width, H / im.height)
    sc_ = s0 * z
    vw, vh = W / sc_, H / sc_
    cx = clamp(fx * im.width, vw / 2, im.width - vw / 2)
    cy = clamp(fy * im.height, vh / 2, im.height - vh / 2)
    rot = sc.get("rot", 0.0) * math.sin((t - sc["t"]) * 0.6)
    return view(im, cx, cy, sc_, rot=rot)


@lru_cache(40)
def card_image(key, kind, maxw, maxh, radius=26):
    im = load(key, kind)
    s = min(maxw / im.width, maxh / im.height)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.width - 1, im.height - 1), radius, fill=255)
    rgba = im.convert("RGBA")
    rgba.putalpha(mask)
    pad = 60
    shadow = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((pad, pad + 18, pad + im.width, pad + im.height + 18), radius,
                                             fill=(0, 0, 0, 170))
    shadow = shadow.filter(ImageFilter.GaussianBlur(24))
    shadow.alpha_composite(rgba, (pad, pad))
    return shadow


def r_card(sc, t):
    kind = sc.get("grade", "std")
    bg = blur_bg(sc["img"], kind).copy()
    card = card_image(sc["img"], kind, sc.get("maxw", 900), sc.get("maxh", 1150))
    p = (t - sc["t"]) / max(0.5, sc["_end"] - sc["t"])
    z = (sc.get("zoom", (1.0, 1.08))[0] + (sc.get("zoom", (1.0, 1.08))[1] - sc.get("zoom", (1.0, 1.08))[0]) * clamp(p)) * punch(t)
    rot = sc.get("tilt", 2.0) * (1 - 2 * clamp(p))
    cw, ch = card.size
    c = card.resize((int(cw * z), int(ch * z)), Image.BILINEAR).rotate(rot, Image.BILINEAR, expand=True)
    cx, cy = CX, H * sc.get("y", 0.43)
    bg.paste(c, (int(cx - c.width / 2), int(cy - c.height / 2)), c)
    return bg


def r_split(sc, t):
    out = Image.new("RGB", (W, H), (6, 6, 8))
    hh = H // 2
    for i, sp in enumerate(sc["imgs"]):
        im = load(sp["img"], sp.get("grade", "std"))
        s0 = max(W / im.width, hh / im.height)
        z = 1.04 + 0.08 * clamp((t - sc["t"]) / 4)
        fx, fy = sp.get("focus", (0.5, 0.35))
        sc_ = s0 * z
        vw, vh = W / sc_, hh / sc_
        cx = clamp(fx * im.width, vw / 2, im.width - vw / 2)
        cy = clamp(fy * im.height, vh / 2, im.height - vh / 2)
        part = view(im, cx, cy, sc_, (W, hh))
        q = eout((t - sc["t"] - 0.1 * i) / 0.45, 4)
        off = int((1 - q) * (W if i == 0 else -W))
        out.paste(part, (off, i * hh))
    d = ImageDraw.Draw(out)
    lw = int(W * eout((t - sc["t"] - 0.2) / 0.4))
    d.rectangle(((W - lw) // 2, hh - 5, (W + lw) // 2, hh + 5), fill=YEL)
    return out


def r_grid(sc, t):
    bg = blur_bg(sc["bg"], "dark").copy()
    tiles = sc["tiles"]
    tw, th = 420, sc.get("th", 410)
    gy = sc.get("gy", 250)
    pos = [(80, gy), (520, gy), (80, gy + th + 20), (520, gy + th + 20)]
    for i, tl in enumerate(tiles):
        q = (t - tl["at"]) / 0.35
        if q <= 0:
            continue
        im = load(tl["img"], "std")
        s0 = max(tw / im.width, th / im.height)
        fx, fy = tl.get("focus", (0.5, 0.45))
        vw, vh = tw / s0, th / s0
        cx = clamp(fx * im.width, vw / 2, im.width - vw / 2)
        cy = clamp(fy * im.height, vh / 2, im.height - vh / 2)
        zt = 1.0 + 0.06 * clamp((t - tl["at"]) / 3)
        tile = view(im, cx, cy, s0 * zt, (tw, th)).convert("RGBA")
        mask = Image.new("L", (tw, th), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, tw - 1, th - 1), 22, fill=255)
        tile.putalpha(mask)
        td = ImageDraw.Draw(tile)
        f = font("anton", 46)
        txt = tr_upper(tl["name"])
        bw = td.textlength(txt, font=f) + 36
        td.rounded_rectangle((18, th - 82, 18 + bw, th - 22), 10, fill=(0, 0, 0, 235))
        td.text((36, th - 52), txt, font=f, fill=YEL, anchor="lm")
        s = 0.7 + 0.3 * back_out(q)
        tile = tile.resize((max(1, int(tw * s)), max(1, int(th * s))), Image.BILINEAR)
        x, y = pos[i]
        bg.paste(tile, (int(x + (tw - tile.width) / 2), int(y + (th - tile.height) / 2)), tile)
    return bg


def r_number(sc, t):
    """Kinetic year/number scene over a dark blurred plate."""
    bg = blur_bg(sc["bg"], "dark").copy()
    return bg


RENDER = {"cover": r_cover, "card": r_card, "split": r_split, "grid": r_grid, "plate": r_number}


def scene_frame(i, t):
    sc = S.SCENES[i]
    return RENDER[sc.get("mode", "cover")](sc, t)


# ---------------------------------------------------------------- transitions
def mblur_h(img, amount):
    if amount < 2:
        return img
    small = img.resize((W // 6, H // 6), Image.BILINEAR)
    arr = np.asarray(small).astype(np.float32)
    k = max(1, int(amount / 6))
    acc = sum(np.roll(arr, s, axis=1) for s in range(-k, k + 1)) / (2 * k + 1)
    return Image.blend(img, Image.fromarray(acc.astype(np.uint8)).resize((W, H), Image.BILINEAR), clamp(amount / 40))


def mblur_v(img, amount):
    if amount < 2:
        return img
    small = img.resize((W // 6, H // 6), Image.BILINEAR)
    arr = np.asarray(small).astype(np.float32)
    k = max(1, int(amount / 6))
    acc = sum(np.roll(arr, s, axis=0) for s in range(-k, k + 1)) / (2 * k + 1)
    return Image.blend(img, Image.fromarray(acc.astype(np.uint8)).resize((W, H), Image.BILINEAR), clamp(amount / 40))


def tr_push(a, b, p, axis="y", sign=1):
    q = ease(p)
    out = Image.new("RGB", (W, H))
    if axis == "y":
        off = int(q * H) * sign
        out.paste(a, (0, -off)); out.paste(b, (0, H * sign - off))
        return mblur_v(out, 60 * math.sin(math.pi * p))
    off = int(q * W) * sign
    out.paste(a, (-off, 0)); out.paste(b, (W * sign - off, 0))
    return mblur_h(out, 60 * math.sin(math.pi * p))


def tr_bars(a, b, p, n=6):
    out = a.copy()
    bh = H // n + 1
    for i in range(n):
        q = eout((p - i * 0.06) / 0.6, 3)
        if q <= 0:
            continue
        w = int(W * q)
        y = i * bh
        if i % 2 == 0:
            out.paste(b.crop((0, y, w, y + bh)), (0, y))
        else:
            out.paste(b.crop((W - w, y, W, y + bh)), (W - w, y))
    return out


def tr_iris(a, b, p, c=(0.5, 0.45)):
    r = eout(p, 3) * math.hypot(W, H)
    mask = Image.new("L", (W, H), 0)
    x, y = c[0] * W, c[1] * H
    ImageDraw.Draw(mask).ellipse((x - r, y - r, x + r, y + r), fill=255)
    out = Image.composite(b, a, mask)
    d = ImageDraw.Draw(out)
    if p < 0.95:
        d.ellipse((x - r, y - r, x + r, y + r), outline=YEL, width=10)
    return out


def tr_diag(a, b, p):
    q = ease(p)
    off = -700 + q * (W + 1400)
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon([(-10, -10), (off + 500, -10), (off - 500, H + 10), (-10, H + 10)], fill=255)
    out = Image.composite(b, a, mask)
    ImageDraw.Draw(out).line([(off + 500, -10), (off - 500, H + 10)], fill=YEL, width=14)
    return out


def tr_zoomblur(a, b, p):
    if p < 0.5:
        q = ein(p / 0.5, 2)
        img = view(a, W / 2, H / 2, 1 + 0.5 * q)
        blur = img.filter(ImageFilter.GaussianBlur(14 * q))
        return Image.blend(img, blur, q)
    q = (p - 0.5) / 0.5
    img = view(b, W / 2, H / 2, 1.35 - 0.35 * eout(q))
    return Image.blend(img.filter(ImageFilter.GaussianBlur(14 * (1 - q))), img, eout(q))


def tr_spin(a, b, p):
    if p < 0.5:
        q = ein(p / 0.5, 2)
        return view(a, W / 2, H / 2, 1 + 0.4 * q, rot=-12 * q).filter(ImageFilter.GaussianBlur(10 * q))
    q = (p - 0.5) / 0.5
    return view(b, W / 2, H / 2, 1.4 - 0.4 * eout(q), rot=12 * (1 - eout(q))).filter(ImageFilter.GaussianBlur(10 * (1 - q)))


def tr_glitch(a, b, p):
    base = a if p < 0.5 else b
    arr = np.asarray(base).copy()
    rng = np.random.default_rng(int(p * 997) + 3)
    sh = int(40 * math.sin(math.pi * p))
    arr[..., 0] = np.roll(arr[..., 0], sh, axis=1)
    arr[..., 2] = np.roll(arr[..., 2], -sh, axis=1)
    for _ in range(8):
        y = rng.integers(0, H - 80); hh = rng.integers(10, 90)
        arr[y:y + hh] = np.roll(arr[y:y + hh], rng.integers(-120, 120), axis=1)
    return Image.fromarray(arr)


def tr_flash(a, b, p):
    w = Image.new("RGB", (W, H), WHITE)
    return Image.blend(a, w, ease(p / 0.5)) if p < 0.5 else Image.blend(w, b, ease((p - 0.5) / 0.5))


def tr_dip(a, b, p):
    k = Image.new("RGB", (W, H), BLACK)
    return Image.blend(a, k, ease(p / 0.5)) if p < 0.5 else Image.blend(k, b, ease((p - 0.5) / 0.5))


TRANS = {
    "pushup": (0.32, lambda a, b, p: tr_push(a, b, p, "y", 1)),
    "pushdown": (0.32, lambda a, b, p: tr_push(a, b, p, "y", -1)),
    "pushleft": (0.32, lambda a, b, p: tr_push(a, b, p, "x", 1)),
    "pushright": (0.32, lambda a, b, p: tr_push(a, b, p, "x", -1)),
    "bars": (0.45, tr_bars), "iris": (0.5, tr_iris), "diag": (0.4, tr_diag),
    "zoomblur": (0.4, tr_zoomblur), "spin": (0.45, tr_spin), "glitch": (0.22, tr_glitch),
    "flash": (0.28, tr_flash), "dip": (0.5, tr_dip),
}


def base_frame(t):
    idx = max(i for i, sc in enumerate(S.SCENES) if sc["t"] <= t)
    for j in (idx + 1, idx):
        if 0 < j < len(S.SCENES):
            sc = S.SCENES[j]
            tr = sc.get("tr", "cut")
            if tr in TRANS:
                d, fn = TRANS[tr]
                t0 = sc["t"] - d / 2
                if t0 <= t < t0 + d:
                    return fn(scene_frame(j - 1, t), scene_frame(j, t), (t - t0) / d)
    return scene_frame(idx, t)


# ---------------------------------------------------------------- overlays
def pill_text(d, x, y, txt, f, fg, bg=(0, 0, 0, 235), padx=26, pady=14, anchor="mm", radius=16):
    tw = d.textlength(txt, font=f)
    asc, desc = f.getmetrics()
    th = asc * 0.78
    if anchor == "mm":
        x0 = x - tw / 2 - padx
    else:
        x0 = x - padx
    y0 = y - th / 2 - pady
    d.rounded_rectangle((x0, y0, x0 + tw + 2 * padx, y0 + th + 2 * pady), radius, fill=bg)
    d.text((x0 + padx, y), txt, font=f, fill=fg, anchor="lm")
    return x0 + tw + 2 * padx


def ov_title(L, ov, t):
    """Hook title: stacked black pills with yellow text, slam-in."""
    q = (t - ov["t0"]) / 0.22
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.25) / 0.25)
    tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    y = ov.get("y", 330)
    for i, line in enumerate(ov["lines"]):
        qi = (t - ov["t0"] - i * 0.12) / 0.22
        if qi <= 0:
            continue
        size = ov.get("size", 108)
        f = font("anton", size)
        sc = 1 + 0.35 * (1 - back_out(qi))
        fz = font("anton", max(10, int(size * sc)))
        pill_text(d, CX, y + i * (size + 34), line, fz, YEL, padx=30, pady=18)
    tmp.putalpha(ImageChops.multiply(tmp.split()[3], Image.new("L", (W, H), int(255 * clamp(out)))))
    L.alpha_composite(tmp)


def ov_label(L, ov, t):
    q = eout((t - ov["t0"]) / 0.35, 4)
    out = 1 - ease((t - ov["t1"] + 0.25) / 0.25)
    a = min(q, out)
    if a <= 0:
        return
    d = ImageDraw.Draw(L)
    x0 = SAFE_L - int((1 - q) * 500)
    y0 = ov.get("y", 250)
    fs = font("mont", 34, 700)
    fn = font("anton", ov.get("size", 74))
    name = tr_upper(ov["title"])
    sub = tr_upper(ov.get("sub", ""))
    nw = d.textlength(name, font=fn)
    sw = d.textlength(sub, font=fs) if sub else 0
    al = int(255 * a)
    # small yellow tag on top, big black block with white name
    if sub:
        d.rectangle((x0, y0, x0 + sw + 28, y0 + 50), fill=YEL + (al,))
        d.text((x0 + 14, y0 + 25), sub, font=fs, fill=(0, 0, 0, al), anchor="lm")
    y1 = y0 + (50 if sub else 0)
    d.rectangle((x0, y1, x0 + nw + 40, y1 + 104), fill=(0, 0, 0, int(225 * a)))
    d.text((x0 + 20, y1 + 53), name, font=fn, fill=WHITE + (al,), anchor="lm")


def ov_kinetic(L, ov, t):
    """Big word with a yellow highlighter box that wipes in behind it."""
    q = (t - ov["t0"]) / 0.3
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    size = ov.get("size", 150)
    f = font("anton", size)
    lines = ov["text"].split("\n")
    y = ov.get("y", 700)
    style = ov.get("style", "yellow")
    for i, ln in enumerate(lines):
        qi = (t - ov["t0"] - i * 0.1) / 0.3
        if qi <= 0:
            continue
        tw = d.textlength(ln, font=f)
        yy = y + i * (size * 1.05)
        bw = (tw + 50) * eout(qi, 4)
        x0 = CX - (tw + 50) / 2
        al = int(255 * out)
        if style == "red":
            box, fg = RED, WHITE
        elif style == "black":
            box, fg = BLACK, YEL
        else:
            box, fg = YEL, BLACK
        d.rectangle((x0, yy - size * 0.55, x0 + bw, yy + size * 0.55), fill=box + (al,))
        if qi > 0.35:
            ta = int(al * clamp((qi - 0.35) / 0.3))
            d.text((CX, yy + size * 0.02), ln, font=f, fill=fg + (ta,), anchor="mm")


def ov_counter(L, ov, t):
    q = (t - ov["t0"]) / ov.get("dur", 0.8)
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    v0, v1 = ov["from"], ov["to"]
    val = int(round(v0 + (v1 - v0) * eout(q, 3)))
    txt = ov.get("fmt", "{}").format(val)
    d = ImageDraw.Draw(L)
    size = ov.get("size", 230)
    sc = 1 + 0.08 * (1 - eout((t - ov["t0"] - ov.get("dur", 0.8)) / 0.3)) if q >= 1 else 1
    f = font("anton", int(size * sc))
    y = ov.get("y", 760)
    al = int(255 * out)
    d.text((CX + 6, y + 8), txt, font=f, fill=(0, 0, 0, int(al * 0.6)), anchor="mm")
    d.text((CX, y), txt, font=f, fill=YEL + (al,), anchor="mm")
    if ov.get("sub"):
        pill_text(d, CX, y + size * 0.62, tr_upper(ov["sub"]), font("anton", 52), WHITE, bg=(0, 0, 0, int(220 * out)))


def ov_arrow(L, ov, t):
    """Animated hand-drawn red arrow + ring around a point given in IMAGE coords of the current scene."""
    q = (t - ov["t0"]) / 0.25
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    sc = S.SCENES[[i for i, s in enumerate(S.SCENES) if s["t"] <= t][-1]]
    im = load(sc["img"], sc.get("grade", "std"))
    z, fx, fy = cover_params(sc, t)
    z *= punch(t)
    s0 = max(W / im.width, H / im.height) * z
    vw, vh = W / s0, H / s0
    cx = clamp(fx * im.width, vw / 2, im.width - vw / 2)
    cy = clamp(fy * im.height, vh / 2, im.height - vh / 2)
    px = (ov["pt"][0] * im.width - cx) * s0 + W / 2
    py = (ov["pt"][1] * im.height - cy) * s0 + H / 2
    r = ov.get("r", 0.05) * im.width * s0
    tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    col = tuple(ov.get("color", RED))
    al = int(255 * out)
    # ring drawn progressively
    ang = 360 * eout(q, 3)
    for k in range(3):
        rr = r + k * 2
        d.arc((px - rr, py - rr * 1.15, px + rr, py + rr * 1.15), -90, -90 + ang, fill=col + (al,), width=10)
    # arrow from upper-right, bobbing
    if q > 0.4:
        qa = eout((q - 0.4) / 0.6, 3)
        bob = 14 * math.sin((t - ov["t0"]) * 9)
        dx, dy = ov.get("dir", (1, -1))
        nrm = math.hypot(dx, dy)
        ux, uy = dx / nrm, dy / nrm
        tipx = px + ux * (r * 1.25 + bob)
        tipy = py + uy * (r * 1.4 + bob)
        length = 300 * qa
        tailx, taily = tipx + ux * length, tipy + uy * length
        d.line([(tailx, taily), (tipx + ux * 30, tipy + uy * 30)], fill=col + (al,), width=22)
        # head
        hx, hy = -ux, -uy
        px1 = tipx + ux * 70 + (-uy) * 45
        py1 = tipy + uy * 70 + (ux) * 45
        px2 = tipx + ux * 70 - (-uy) * 45
        py2 = tipy + uy * 70 - (ux) * 45
        d.polygon([(tipx, tipy), (px1, py1), (px2, py2)], fill=col + (al,))
        if ov.get("tag"):
            f = font("anton", 54)
            tx, ty = tailx + ux * 10, taily + uy * 40
            tx = clamp(tx, SAFE_L + 160, SAFE_R - 160)
            pill_text(d, tx, ty, ov["tag"], f, WHITE, bg=col + (al,))
    sh = tmp.filter(ImageFilter.GaussianBlur(6))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow.putalpha(sh.split()[3].point(lambda v: int(v * 0.6)))
    L.alpha_composite(shadow, (4, 6))
    L.alpha_composite(tmp)


def ov_pip(L, ov, t):
    q = (t - ov["t0"]) / 0.4
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.25) / 0.25)
    if out <= 0:
        return
    card = card_image(ov["img"], "std", ov.get("w", 380), ov.get("h", 470), 22)
    s = (0.6 + 0.4 * back_out(q)) * (0.9 + 0.1 * out)
    c = card.resize((int(card.width * s), int(card.height * s)), Image.BILINEAR).rotate(ov.get("rot", -4), Image.BILINEAR, expand=True)
    if out < 1:
        a = c.split()[3].point(lambda v: int(v * out))
        c.putalpha(a)
    x, y = ov.get("xy", (SAFE_R - 230, 520))
    L.alpha_composite(c, (int(x - c.width / 2), int(y - c.height / 2)))
    if ov.get("tag") and q > 0.6:
        d = ImageDraw.Draw(L)
        pill_text(d, x, y + c.height / 2 - 40, tr_upper(ov["tag"]), font("anton", 40), BLACK, bg=YEL + (int(255 * out),))


def ov_stamp(L, ov, t):
    q = (t - ov["t0"]) / 0.18
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    size = ov.get("size", 140)
    f = font("anton", size)
    txt = ov["text"]
    tmp = Image.new("RGBA", (900, 400), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    tw = d.textlength(txt, font=f)
    col = tuple(ov.get("color", RED))
    al = int(255 * out)
    box = (450 - tw / 2 - 34, 200 - size * 0.62, 450 + tw / 2 + 34, 200 + size * 0.62)
    if ov.get("fill"):
        d.rectangle(box, fill=(0, 0, 0, int(190 * out)))
    d.rectangle(box, outline=col + (al,), width=12)
    d.text((450, 205), txt, font=f, fill=col + (al,), anchor="mm")
    s = 1 + 1.2 * (1 - eout(q, 3))
    tmp = tmp.resize((int(900 * s), int(400 * s)), Image.BILINEAR).rotate(ov.get("rot", -8), Image.BILINEAR, expand=True)
    x, y = CX, ov.get("y", 800)
    L.alpha_composite(tmp, (int(x - tmp.width / 2), int(y - tmp.height / 2)))


def ov_tagpair(L, ov, t):
    """OSMANLI / AVRUPA tags on split screens."""
    d = ImageDraw.Draw(L)
    for (txt, y, at) in ov["tags"]:
        q = eout((t - at) / 0.3)
        if q <= 0:
            continue
        out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
        x = SAFE_L + 10 - int((1 - q) * 400)
        pill_text(d, x + 10, y, txt, font("anton", 70), BLACK, bg=YEL + (int(255 * out),), anchor="lm", padx=24)


def ov_cta(L, ov, t):
    q = (t - ov["t0"]) / 0.35
    if q <= 0:
        return
    d = ImageDraw.Draw(L)
    bob = 12 * math.sin(t * 8)
    y = ov.get("y", 1080)
    s = back_out(q)
    f = font("anton", int(84 * clamp(s, 0.3, 1.2)))
    pill_text(d, CX, y, "YORUMLARA YAZ", f, BLACK, bg=YEL + (255,), padx=34, pady=20)
    ax, ay = CX, y + 90 + bob
    d.polygon([(ax - 40, ay), (ax + 40, ay), (ax, ay + 48)], fill=YEL + (255,))


def ov_item(L, ov, t):
    """Persistent numbered item header: yellow number tile + black title block."""
    q = eout((t - ov["t0"]) / 0.4, 4)
    out = 1 - ease((t - ov["t1"] + 0.25) / 0.25)
    a = min(q, out)
    if a <= 0:
        return
    d = ImageDraw.Draw(L)
    al = int(255 * a)
    x0 = SAFE_L - int((1 - q) * 700)
    y0 = ov.get("y", 236)
    f = font("anton", 58)
    lines = ov["title"].split("\n")
    lh = 72
    bh = max(118, 26 + lh * len(lines))
    d.rectangle((x0, y0, x0 + 118, y0 + bh), fill=YEL + (al,))
    d.text((x0 + 59, y0 + bh / 2 + 4), str(ov["n"]), font=font("anton", 96), fill=(0, 0, 0, al), anchor="mm")
    tw = max(d.textlength(ln, font=f) for ln in lines)
    d.rectangle((x0 + 118, y0, x0 + 118 + tw + 44, y0 + bh), fill=(0, 0, 0, int(232 * a)))
    for i, ln in enumerate(lines):
        d.text((x0 + 140, y0 + bh / 2 + (i - (len(lines) - 1) / 2) * lh + 3), ln, font=f, fill=WHITE + (al,), anchor="lm")


def ov_source(L, ov, t):
    """Source line under the captions (inside the safe zone)."""
    q = ease((t - ov["t0"]) / 0.4)
    out = 1 - ease((t - ov["t1"] + 0.25) / 0.25)
    a = min(q, out)
    if a <= 0:
        return
    d = ImageDraw.Draw(L)
    f = font("mont", 27, 600)
    ft = font("anton", 30)
    maxw = SAFE_R - SAFE_L - 40
    words = ov["text"].split()
    lines, cur = [], ""
    tagw = d.textlength("KAYNAK", font=ft) + 30
    for w in words:
        trial = (cur + " " + w).strip()
        lim = maxw - (tagw if not lines else 0)
        if d.textlength(trial, font=f) <= lim:
            cur = trial
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    y = ov.get("y", 1385)
    lh = 40
    widths = [d.textlength(ln, font=f) + (tagw if i == 0 else 0) for i, ln in enumerate(lines)]
    bw = max(widths) + 40
    x0 = CX - bw / 2
    d.rounded_rectangle((x0, y - 28, x0 + bw, y - 28 + lh * len(lines) + 16), 12, fill=(0, 0, 0, int(200 * a)))
    al = int(255 * a)
    d.rounded_rectangle((x0 + 12, y - 19, x0 + 12 + tagw - 12, y + 19), 6, fill=YEL + (al,))
    d.text((x0 + 12 + (tagw - 12) / 2, y + 1), "KAYNAK", font=ft, fill=(0, 0, 0, al), anchor="mm")
    for i, ln in enumerate(lines):
        d.text((x0 + 20 + (tagw if i == 0 else 0), y + i * lh), ln, font=f, fill=(235, 235, 235, al), anchor="lm")


def ov_quote(L, ov, t):
    q = eout((t - ov["t0"]) / 0.35)
    out = 1 - ease((t - ov["t1"] + 0.3) / 0.3)
    a = min(q, out)
    if a <= 0:
        return
    d = ImageDraw.Draw(L)
    f = font("play", 74, 700)
    words = ov["words"]
    lines, cur = [], []
    for w, wt in words:
        trial = " ".join(x[0] for x in cur + [(w, wt)])
        if d.textlength(trial, font=f) > 780 and cur:
            lines.append(cur); cur = []
        cur.append((w, wt))
    lines.append(cur)
    lh = 98
    y0 = ov.get("y", 700) - (len(lines) - 1) * lh / 2
    bx0, bx1 = SAFE_L, SAFE_R
    by0, by1 = y0 - 190, y0 + (len(lines) - 1) * lh + 140
    d.rounded_rectangle((bx0, by0, bx1, by1), 28, fill=(0, 0, 0, int(225 * a)))
    d.rectangle((bx0, by0 + 30, bx0 + 10, by1 - 30), fill=YEL + (int(255 * a),))
    d.text((CX, by0 + 70), "\u201C", font=font("play", 170, 800), fill=YEL + (int(255 * a),), anchor="mm")
    for li, line in enumerate(lines):
        tw = d.textlength(" ".join(x[0] for x in line), font=f)
        x = CX - tw / 2
        y = y0 + li * lh
        for w, wt in line:
            wa = eout((t - wt + 0.05) / 0.3) * a
            col = YEL if t >= wt - 0.05 else WHITE
            if wa > 0:
                d.text((x, y + int((1 - wa) * 14)), w, font=f, fill=col + (int(255 * wa),), anchor="lm")
            x += d.textlength(w + " ", font=f)
    if ov.get("by"):
        d.text((CX, by1 - 48), ov["by"], font=font("mont", 30, 700), fill=(220, 220, 220, int(255 * a)), anchor="mm")


def ov_vs(L, ov, t):
    q = (t - ov["t0"]) / 0.3
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    r = 92 * back_out(q) * (1 + 0.05 * math.sin(t * 6))
    cx, cy = W / 2, H / 2
    al = int(255 * out)
    d.ellipse((cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8), fill=(0, 0, 0, al))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=YEL + (al,))
    d.text((cx, cy + 4), "VS", font=font("anton", max(10, int(r * 1.05))), fill=(0, 0, 0, al), anchor="mm")


@lru_cache(20)
def round_portrait(key, size):
    im = load(key, "std")
    s0 = max(size / im.width, size / im.height) * 1.25
    fx, fy = S.FACES.get(key, (0.5, 0.3))
    vw = size / s0
    cx = clamp(fx * im.width, vw / 2, im.width - vw / 2)
    cy = clamp(fy * im.height, vw / 2, im.height - vw / 2)
    tile = view(im, cx, cy, s0, (size, size)).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    tile.putalpha(mask)
    ring = Image.new("RGBA", (size + 16, size + 16), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, size + 15, size + 15), fill=YEL + (255,))
    ring.alpha_composite(tile, (8, 8))
    return ring


def ov_roster(L, ov, t):
    out = 1 - ease((t - ov["t1"] + 0.25) / 0.25)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    for i, (key, name, at, (x, y)) in enumerate(ov["items"]):
        q = (t - at) / 0.25
        if q <= 0:
            continue
        size = ov.get("size", 190)
        rp = round_portrait(key, size)
        s = back_out(q)
        rp2 = rp.resize((max(1, int(rp.width * s)), max(1, int(rp.height * s))), Image.BILINEAR)
        if out < 1:
            rp2.putalpha(rp2.split()[3].point(lambda v: int(v * out)))
        L.alpha_composite(rp2, (int(x - rp2.width / 2), int(y - rp2.height / 2)))
        if q > 0.6:
            pill_text(d, x, y + size / 2 + 34, name, font("anton", 34), WHITE, bg=(0, 0, 0, int(230 * out)), padx=14, pady=8)
        d.text((x - size / 2 + 6, y - size / 2 + 6), str(i + 1), font=font("anton", 44), fill=YEL + (int(255 * out),), anchor="lt",
               stroke_width=4, stroke_fill=(0, 0, 0, int(255 * out)))


# ---------------------------------------------------------------- pen / hand-drawn effects
def _wobble(seed, k):
    return math.sin(seed * 12.9898 + k * 1.7) * 0.5 + math.sin(seed * 4.1 + k * 3.3) * 0.5


def pen_poly(d, pts, col, width, al):
    if len(pts) < 2:
        return
    d.line(pts, fill=col + (al,), width=width, joint="curve")
    r = width / 2
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=col + (al,))


def ov_pencircle(L, ov, t):
    dur = ov.get("dur", 0.45)
    q = (t - ov["t0"]) / dur
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    cx, cy, rx, ry = ov["cx"], ov["cy"], ov["rx"], ov["ry"]
    seed = ov.get("seed", 1.0)
    a0 = ov.get("a0", -100)
    span = 395 * eout(q, 2)
    pts = []
    n = max(2, int(span / 4))
    for i in range(n + 1):
        a = math.radians(a0 + span * i / n)
        grow = 1 + 0.06 * (i / max(1, n)) * (span / 395)
        wob = 1 + 0.035 * _wobble(seed, i * 0.15)
        pts.append((cx + rx * grow * wob * math.cos(a), cy + ry * grow * wob * math.sin(a)))
    col = tuple(ov.get("color", RED))
    al = int(255 * out)
    pen_poly(d, pts, col, ov.get("width", 11), al)
    pen_poly(d, [(x + 2, y + 1) for x, y in pts], col, max(2, ov.get("width", 11) // 3), int(al * 0.6))


def _bez(p0, p1, p2, u):
    return ((1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0],
            (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1])


def ov_penarrow(L, ov, t):
    dur = ov.get("dur", 0.4)
    q = (t - ov["t0"]) / dur
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    p0, p2 = ov["src"], ov["dst"]
    bend = ov.get("bend", 0.25)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    nx, ny = -(p2[1] - p0[1]), (p2[0] - p0[0])
    p1 = (mx + nx * bend, my + ny * bend)
    u1 = eout(min(1, q), 2)
    pts = [_bez(p0, p1, p2, u1 * i / 40) for i in range(41)]
    col = tuple(ov.get("color", RED))
    al = int(255 * out)
    w = ov.get("width", 12)
    pen_poly(d, pts, col, w, al)
    if q > 1:
        qh = eout((q - 1) / 0.5, 2)
        ex, ey = pts[-1]
        bx, by = pts[-4]
        ang = math.atan2(ey - by, ex - bx)
        L_ = 60 * qh
        for da in (2.55, -2.55):
            pen_poly(d, [(ex, ey), (ex + L_ * math.cos(ang + da), ey + L_ * math.sin(ang + da))], col, w, al)


def ov_penline(L, ov, t):
    dur = ov.get("dur", 0.35)
    q = (t - ov["t0"]) / dur
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    x0, y0, x1 = ov["x0"], ov["y"], ov["x1"]
    u = eout(q, 2)
    pts = [(x0 + (x1 - x0) * u * i / 30, y0 + 6 * math.sin(i * 0.9) * (1 if ov.get("wavy") else 0.25)) for i in range(31)]
    pen_poly(d, pts, tuple(ov.get("color", RED)), ov.get("width", 10), int(255 * out))


def ov_pencross(L, ov, t):
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    cx, cy, r = ov["cx"], ov["cy"], ov.get("r", 120)
    col = tuple(ov.get("color", RED))
    for k, (a, b) in enumerate((((-1, -1), (1, 1)), ((1, -1), (-1, 1)))):
        q = (t - ov["t0"] - 0.22 * k) / 0.22
        if q <= 0:
            continue
        u = eout(q, 2)
        p0 = (cx + a[0] * r, cy + a[1] * r)
        p1 = (cx + a[0] * r + (b[0] - a[0]) * r * u, cy + a[1] * r + (b[1] - a[1]) * r * u)
        pen_poly(d, [p0, p1], col, 16, int(255 * out))


@lru_cache(40)
def _hand_layer(text, fname, size, weight, col, stroke):
    f = font(fname, size, weight)
    dd = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    bb = dd.textbbox((0, 0), text, font=f, stroke_width=stroke)
    w, h = bb[2] - bb[0] + 40, bb[3] - bb[1] + 40
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if stroke:
        d.text((20 - bb[0], 20 - bb[1]), text, font=f, fill=col + (255,), stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    else:
        d.text((20 - bb[0], 20 - bb[1]), text, font=f, fill=col + (255,))
    return im


def ov_handwrite(L, ov, t):
    dur = ov.get("dur", 0.8)
    q = (t - ov["t0"]) / dur
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    im = _hand_layer(ov["text"], ov.get("font", "caveat"), ov.get("size", 120), ov.get("weight", 700),
                     tuple(ov.get("color", YEL)), ov.get("stroke", 5))
    w, h = im.size
    u = clamp(q)
    rtl = ov.get("rtl", False)
    m = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(m)
    edge = w * u
    if rtl:
        md.rectangle((w - edge, 0, w, h), fill=255)
    else:
        md.rectangle((0, 0, edge, h), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(6))
    a = ImageChops.multiply(im.split()[3], m)
    if out < 1:
        a = a.point(lambda v: int(v * out))
    im2 = im.copy()
    im2.putalpha(a)
    x = int(ov.get("x", CX) - w / 2)
    y = int(ov["y"] - h / 2)
    L.alpha_composite(im2, (x, y))
    if u < 1:
        d = ImageDraw.Draw(L)
        px = x + (w - edge if rtl else edge)
        py = y + h / 2 + 22 * math.sin(t * 40)
        d.ellipse((px - 9, py - 9, px + 9, py + 9), fill=WHITE + (230,))


def ov_finger(L, ov, t):
    q = (t - ov["t0"]) / 0.28
    if q <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    im = _finger()
    s = ov.get("size", 760) / im.width
    s *= 0.25 + 0.75 * back_out(q, 2.2)
    for tp in ov.get("taps", []):
        dt = t - tp
        if 0 <= dt < 0.3:
            s *= 1 + 0.16 * math.sin(math.pi * dt / 0.3)
    s *= 1 + 0.015 * math.sin(t * 5)
    f2 = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
    if out < 1:
        f2.putalpha(f2.split()[3].point(lambda v: int(v * out)))
    sh = Image.new("RGBA", f2.size, (0, 0, 0, 0))
    sh.putalpha(f2.split()[3].point(lambda v: int(v * 0.45)))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    x, y = ov.get("x", CX), ov.get("y", 860)
    L.alpha_composite(sh, (int(x - f2.width / 2 + 14), int(y - f2.height / 2 + 26)))
    L.alpha_composite(f2, (int(x - f2.width / 2), int(y - f2.height / 2)))


@lru_cache(1)
def _finger():
    im = Image.open(os.path.join(IMG if os.path.exists(os.path.join(IMG, "finger.png")) else ASSETS, "finger.png")).convert("RGBA")
    return im.crop(im.getbbox())


def ov_people(L, ov, t):
    q0 = (t - ov["t0"]) / 0.3
    if q0 <= 0:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    al = int(255 * out)
    n = 10
    sp = 86
    x0 = CX - sp * (n - 1) / 2
    y = ov.get("y", 980)
    d.rounded_rectangle((x0 - 70, y - 120, x0 + sp * (n - 1) + 70, y + 110), 26, fill=(0, 0, 0, int(200 * out)))
    for i in range(n):
        qi = (t - ov["t0"] - i * 0.06) / 0.25
        if qi <= 0:
            continue
        gray = i != ov.get("keep", 4) and t >= ov["gray_t"] + 0.05 * i
        col = (110, 110, 110) if gray else YEL
        x = x0 + i * sp
        sc = back_out(qi)
        r = 20 * sc
        d.ellipse((x - r, y - 62 - r, x + r, y - 62 + r), fill=col + (al,))
        d.rounded_rectangle((x - 30 * sc, y - 34 * sc, x + 30 * sc, y + 60 * sc), int(18 * sc), fill=col + (al,))


def ov_typewriter(L, ov, t):
    if t < ov["t0"]:
        return
    out = 1 - ease((t - ov["t1"] + 0.2) / 0.2)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    txt = ov["text"]
    nchar = int(clamp((t - ov["t0"]) / ov.get("dur", 1.0)) * len(txt))
    f = font("mono", ov.get("size", 54))
    full_w = d.textlength(txt, font=f)
    y = ov.get("y", 760)
    x0 = CX - full_w / 2
    al = int(255 * out)
    d.rectangle((x0 - 30, y - 60, x0 + full_w + 30, y + 60), fill=(245, 235, 210, int(240 * out)))
    d.rectangle((x0 - 30, y - 60, x0 + full_w + 30, y + 60), outline=(60, 40, 20, al), width=3)
    shown = txt[:nchar]
    d.text((x0, y), shown, font=f, fill=(30, 20, 10, al), anchor="lm")
    if nchar < len(txt) or int(t * 3) % 2 == 0:
        cx = x0 + d.textlength(shown, font=f) + 4
        d.rectangle((cx, y - 30, cx + 6, y + 30), fill=(30, 20, 10, al))


def ov_papers(L, ov, t):
    if t < ov["t0"]:
        return
    out = 1 - ease((t - ov["t1"] + 0.3) / 0.3)
    if out <= 0:
        return
    d = ImageDraw.Draw(L)
    rng = np.random.default_rng(42)
    n = ov.get("n", 26)
    for i in range(n):
        st = ov["t0"] + rng.uniform(0, ov.get("spread", 2.5))
        x0 = rng.uniform(ov.get("x0", 300), ov.get("x1", 800))
        y0 = ov.get("y0", 520) + rng.uniform(-40, 40)
        vy = rng.uniform(260, 420)
        sway = rng.uniform(30, 90)
        ph = rng.uniform(0, 6.28)
        dt = t - st
        if dt < 0:
            continue
        x = x0 + sway * math.sin(dt * 2.2 + ph) + rng.uniform(-1, 1) * dt * 60
        y = y0 + vy * dt
        if y > H - 380:
            continue
        ang = 35 * math.sin(dt * 3 + ph)
        w, h = 46, 60 * abs(math.cos(dt * 2.5 + ph)) + 8
        c, s_ = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pts = [(x + px * c - py * s_, y + px * s_ + py * c) for px, py in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2))]
        d.polygon(pts, fill=(245, 238, 220, int(240 * out)), outline=(90, 80, 60, int(200 * out)))
        d.line([pts[0], pts[1]], fill=(120, 110, 90, int(160 * out)), width=2)


OV = {"title": ov_title, "label": ov_label, "kinetic": ov_kinetic, "counter": ov_counter, "arrow": ov_arrow,
      "pip": ov_pip, "stamp": ov_stamp, "tagpair": ov_tagpair, "cta": ov_cta,
      "item": ov_item, "source": ov_source, "quote": ov_quote,
      "vs": ov_vs, "roster": ov_roster, "pencircle": ov_pencircle, "penarrow": ov_penarrow,
      "penline": ov_penline, "pencross": ov_pencross, "handwrite": ov_handwrite, "finger": ov_finger,
      "people": ov_people, "typewriter": ov_typewriter, "papers": ov_papers}


# ---------------------------------------------------------------- captions
@lru_cache(1)
def chunks():
    words = json.load(open(os.path.join(BUILD, "aligned.json")))
    out, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        txt = " ".join(x["w"] for x in cur)
        nxt = words[i + 1] if i + 1 < len(words) else None
        if w["w"][-1] in ".,?!:" or len(cur) >= 3 or len(txt) > 15 or (nxt and nxt["s"] - w["e"] > 0.3):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    res = []
    for i, c in enumerate(out):
        s = c[0]["s"]
        e = out[i + 1][0]["s"] if i + 1 < len(out) else c[-1]["e"] + 0.8
        res.append((s, min(e, c[-1]["e"] + 0.5), c))
    return res


def captions(L, t):
    blur = 0.0
    for lo, hi, mx in getattr(S, "BLUR_CAPS", []):
        if lo <= t < hi:
            blur = mx * ease((t - lo) / 0.5)
    if blur > 0.3:
        tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        _captions(tmp, t)
        L.alpha_composite(tmp.filter(ImageFilter.GaussianBlur(blur)))
        return
    _captions(L, t)


def _captions(L, t):
    for lo, hi in S.NO_CAPTIONS:
        if lo <= t < hi:
            return
    cur = None
    for s, e, c in chunks():
        if s <= t < e:
            cur = (s, e, c)
            break
    if not cur:
        return
    s, e, c = cur
    d = ImageDraw.Draw(L)
    q = (t - s) / 0.12
    sc = 0.85 + 0.15 * back_out(q, 2.2)
    size = int(72 * sc)
    f = font("mont", size, 900)
    words = [tr_upper(x["w"].replace('"', "")) for x in c]
    act = [x["s"] - 0.02 <= t for x in c]
    space = d.textlength(" ", font=f)
    widths = [d.textlength(w, font=f) for w in words]
    tw = sum(widths) + space * (len(words) - 1)
    lines = [list(range(len(words)))]
    if tw > SAFE_R - SAFE_L - 60 and len(words) > 1:
        k = (len(words) + 1) // 2
        lines = [list(range(k)), list(range(k, len(words)))]
    y0 = S.CAPTION_Y(t)
    lh = size * 1.28
    for li, idx in enumerate(lines):
        lw = sum(widths[i] for i in idx) + space * (len(idx) - 1)
        yy = y0 + (li - (len(lines) - 1) / 2) * lh
        x = CX - lw / 2
        d.rounded_rectangle((x - 26, yy - size * 0.62, x + lw + 26, yy + size * 0.62), 18, fill=(0, 0, 0, 238))
        for i in idx:
            # spoken words full yellow, upcoming words dimmer yellow
            col = YEL + (255,) if act[i] else (255, 214, 10, 150)
            d.text((x, yy + size * 0.04), words[i], font=f, fill=col, anchor="lm")
            x += widths[i] + space


# ---------------------------------------------------------------- frame
@lru_cache(1)
def vignette():
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((x - W / 2) / (W / 2)) ** 2 + ((y - H / 2) / (H / 2)) ** 2 * 0.85)
    v = np.clip((r - 0.7) / 0.6, 0, 1) ** 1.8
    return (1 - 0.55 * v)[..., None].astype(np.float32)


@lru_cache(1)
def grain():
    rng = np.random.default_rng(5)
    return [rng.normal(0, 3.5, (H, W, 1)).astype(np.float32) for _ in range(4)]


@lru_cache(1)
def cover_frame():
    """Kapak (thumbnail): videonun ilk 2 karesi ve kapak.jpg. scenes.COVER ile tanımlanır."""
    c = S.COVER
    z = c.get("zoom", 1.05)
    sc = dict(t=-9.0, _end=-8.0, img=c["img"], zoom=(z, z), focus=c.get("focus", (0.5, 0.35)), grade=c.get("grade", "std"))
    img = r_cover(sc, -9.0)
    # üst ve alt koyu geçiş: yazılar her görselde okunur
    y = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
    shade = 1 - 0.55 * np.clip((0.32 - y) / 0.32, 0, 1) - 0.6 * np.clip((y - 0.62) / 0.38, 0, 1)
    arr = np.asarray(img).astype(np.float32) * shade * vignette()
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for m in c.get("marks", []):
        OV[m["type"]](L, dict(m, t0=-9.0, t1=99.0), 0.0)
    ov_title(L, dict(t0=-9.0, t1=99.0, lines=c["lines"], y=c.get("y", 300), size=c.get("size", 116)), 0.0)
    if c.get("stamp"):
        ov_stamp(L, dict(t0=-9.0, t1=99.0, text=c["stamp"], y=c.get("stamp_y", 1000), size=c.get("stamp_size", 130),
                         rot=c.get("stamp_rot", -7), color=c.get("stamp_color", RED), fill=True), 0.0)
    if c.get("bottom"):
        d = ImageDraw.Draw(L)
        pill_text(d, CX, c.get("bottom_y", 1300), tr_upper(c["bottom"]), font("mont", 62, 900), YEL, padx=28, pady=16)
    img.alpha_composite(L)
    return img.convert("RGB")


def frame(t):
    if hasattr(S, "COVER") and t < 2 / FPS:
        return cover_frame()
    img = base_frame(t)
    for ft, dur in S.FLASH:
        d = t - ft
        if 0 <= d < dur:
            img = Image.blend(img, Image.new("RGB", (W, H), WHITE), 0.75 * (1 - d / dur) ** 2)
    for st in S.SHAKE:
        d = t - st
        if 0 <= d < 0.35:
            amp = 16 * math.exp(-d * 9)
            img = view(img, W / 2 - amp * math.sin(d * 90), H / 2 - amp * math.cos(d * 77), 1.03)
    arr = np.asarray(img).astype(np.float32) * vignette() + grain()[int(t * FPS) % 4]
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for ov in S.OVERLAYS:
        if ov["t0"] - 0.01 <= t < ov["t1"]:
            OV[ov["type"]](L, ov, t)
    captions(L, t)
    img.alpha_composite(L)
    if t > S.DURATION - 0.35:
        img = Image.blend(img, Image.new("RGBA", (W, H), (0, 0, 0, 255)), clamp((t - S.DURATION + 0.35) / 0.35))
    return img.convert("RGB")


def render_range(f0, f1, out):
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-g", "60", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fi in range(f0, f1):
        p.stdin.write(frame(fi / FPS).tobytes())
        if (fi - f0) % 150 == 0:
            print(f"[{os.path.basename(out)}] {fi - f0}/{f1 - f0}", flush=True)
    p.stdin.close(); p.wait()


def main():
    outdir = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "cover":
        cover_frame().save(os.path.join(outdir, "kapak.jpg"), quality=92)
        return
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    if len(sys.argv) > 3:
        for ts in sys.argv[3].split(","):
            frame(float(ts)).save(os.path.join(outdir, f"s_{float(ts):06.2f}.jpg"), quality=88)
        return
    total = int(S.DURATION * FPS)
    b = [total * k // workers for k in range(workers + 1)]
    ps = [Process(target=render_range, args=(b[k], b[k + 1], os.path.join(outdir, f"seg{k}.mp4"))) for k in range(workers)]
    [p.start() for p in ps]; [p.join() for p in ps]
    with open(os.path.join(outdir, "segs.txt"), "w") as fh:
        fh.writelines(f"file 'seg{k}.mp4'\n" for k in range(workers))


if __name__ == "__main__":
    main()
