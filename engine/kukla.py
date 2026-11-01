"""Kukla (cut-out) animasyonu: engine/assets/kukla/<karakter>/ parçalarından iskelet, yürüme, ağız senkronu, göz kırpma.

scenes.py kullanımı:
  sahne : dict(t=..., mode="anim", bg="taht"|"avlu"|"sokak"|"kamp"|"koridor", pan=(0.2, 0.6), zoom=(1.0, 1.08))
  overlay: dict(type="kukla", char="anlatici"|"padisah"|"sehzade"|"vezir", t0, t1,
                path=[(t, x), ...]  # ayak ortası x; aralarda yürür
                y=1500, h=900,      # ayak çizgisi ve toplam boy (px)
                face="r"|"l",       # bakış yönü (anlatıcıda yan kafa yürürken)
                talk=[(t0, t1), ...] | True,   # bu aralıkta ağız sese göre açılır
                arm=[(t, "rest"|"up"|"point"|"wave"|"fist"), ...],
                fall=t,             # bu anda yere düşer (bayılma/ölüm)
                mood="angry"|"neutral")
"""
import json, math, os, subprocess
from functools import lru_cache

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
KDIR = os.path.join(HERE, "assets", "kukla")

# Eklem noktaları (parça içi kesir koordinatları). torso: boyun, omuzlar, kalçalar; parçalar: bağlanma noktası.
RIG = {
    "anlatici": dict(neck=(0.5, 0.03), sh_l=(0.13, 0.08), sh_r=(0.87, 0.08), hip_l=(0.33, 0.83), hip_r=(0.67, 0.83),
                     head_pin=(0.5, 0.93), arm_pin=(0.5, 0.04), leg_pin=(0.5, 0.03),
                     mouth=(0.5, 0.83), eyes=((0.33, 0.6), (0.67, 0.6)), eye_r=0.05, leg_over=False,
                     side_head="head_side"),
    "sehzade": dict(neck=(0.5, 0.06), sh_l=(0.2, 0.2), sh_r=(0.8, 0.2), hip_l=(0.4, 0.82), hip_r=(0.6, 0.82),
                    head_pin=(0.5, 0.97), arm_pin=(0.5, 0.05), leg_pin=(0.5, 0.05),
                    mouth=(0.6, 0.9), eyes=((0.36, 0.7), (0.62, 0.7)), eye_r=0.045, leg_over=False),
    "vezir": dict(neck=(0.5, 0.06), sh_l=(0.2, 0.2), sh_r=(0.8, 0.2), hip_l=(0.4, 0.82), hip_r=(0.6, 0.82),
                  head_pin=(0.5, 0.97), arm_pin=(0.5, 0.05), leg_pin=(0.5, 0.05),
                  mouth=(0.5, 0.9), eyes=((0.36, 0.7), (0.62, 0.7)), eye_r=0.04, leg_over=False),
    "padisah": dict(neck=(0.5, 0.06), sh_l=(0.2, 0.2), sh_r=(0.8, 0.2), hip_l=(0.4, 0.82), hip_r=(0.6, 0.82),
                    head_pin=(0.5, 0.97), arm_pin=(0.5, 0.05), leg_pin=(0.5, 0.05),
                    mouth=(0.5, 0.89), eyes=((0.37, 0.72), (0.63, 0.72)), eye_r=0.04, leg_over=False),
}

ARM_POSES = {  # (sol kol açısı, sağ kol açısı) derece; 0 = aşağı, + = dışa/yukarı kaldır
    "rest": (6, 6), "up": (8, 150), "point": (8, 95), "wave": (8, 140), "fist": (8, 120), "both": (140, 140),
    "shrug": (32, 32), "cross": (-20, -20),
}


@lru_cache(64)
def part(char, name):
    p = os.path.join(KDIR, char, name + ".png")
    return Image.open(p).convert("RGBA") if os.path.exists(p) else None


@lru_cache(16)
def background(name, w, h):
    im = Image.open(os.path.join(KDIR, "bg", name + ".png")).convert("RGB")
    s = h * 0.62 / im.height
    big = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 80, 2))
    out = Image.new("RGB", (max(big.width, w), h))
    out.paste(big, (0, 0))
    # zemin: alt kenarın ortalama rengiyle düz, aşağı doğru kararan taban + perspektif çizgileri
    base = np.asarray(big.crop((0, big.height - 14, big.width, big.height - 2))).reshape(-1, 3).mean(axis=0)
    fh = h - big.height
    g = np.linspace(0.92, 0.5, fh, dtype=np.float32)[:, None]
    floor = (base[None, :] * g)[:, None, :].repeat(out.width, axis=1)
    fl = Image.fromarray(np.clip(floor, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(fl)
    line = tuple(int(c * 0.75) for c in base)
    y, k = 0.0, 0
    while y < fh:
        d.line((0, int(y), out.width, int(y)), fill=line, width=2)
        k += 1
        y += 18 + k * 10
    out.paste(fl, (0, big.height))
    sh = Image.new("L", (out.width, 40), 0)
    for i in range(40):
        ImageDraw.Draw(sh).line((0, i, out.width, i), fill=int(120 * (1 - i / 40)))
    out.paste((0, 0, 0), (0, big.height), sh)
    return out


def bg_frame(sc, t, W, H):
    big = background(sc["bg"], W, H)
    dur = max(0.01, sc["_end"] - sc["t"])
    q = min(1.0, max(0.0, (t - sc["t"]) / dur))
    p0, p1 = sc.get("pan", (0.3, 0.5))
    z0, z1 = sc.get("zoom", (1.0, 1.06))
    z = z0 + (z1 - z0) * q
    vw, vh = W / z, H / z
    cx = (p0 + (p1 - p0) * q) * (big.width - vw) + vw / 2
    cy = H - vh / 2
    box = (cx - vw / 2, cy - vh / 2, cx + vw / 2, cy + vh / 2)
    return big.crop(tuple(int(round(v)) for v in box)).resize((W, H), Image.BILINEAR)


# ---------------------------------------------------------------- ses zarfı (ağız senkronu)
_ENV = None


def voice_env(build, fps=30):
    global _ENV
    if _ENV is not None:
        return _ENV
    cache = os.path.join(build, "mouth_env.json")
    if os.path.exists(cache):
        _ENV = json.load(open(cache))
        return _ENV
    voice = os.path.join(build, "voice.mp3")
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", voice, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    hop = 16000 // fps
    n = len(a) // hop
    rms = np.sqrt((a[: n * hop].reshape(n, hop) ** 2).mean(axis=1) + 1e-9)
    ref = np.percentile(rms, 95) or 1
    env = np.clip(rms / ref, 0, 1)
    env = np.where(env < 0.12, 0, env)
    _ENV = [round(float(v), 3) for v in env]
    tmp = cache + ".tmp%d" % os.getpid()
    json.dump(_ENV, open(tmp, "w"))
    os.replace(tmp, cache)
    return _ENV


def mouth_amp(build, t, fps=30):
    env = voice_env(build, fps)
    i = int(t * fps)
    if 0 <= i < len(env):
        # hafif titreşim: hece hissi
        return env[i] * (0.75 + 0.25 * abs(math.sin(t * 23)))
    return 0.0


# ---------------------------------------------------------------- iskelet çizimi
def _paste_rot(L, im, pin, at, ang, flip=False):
    """im'i pin (piksel) noktası at'a gelecek ve ang derece döndürülmüş şekilde yapıştır."""
    if flip:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        pin = (im.width - pin[0], pin[1])
        ang = -ang
    big = max(im.width, im.height) * 2 + 4
    canvas = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    canvas.alpha_composite(im, (int(big / 2 - pin[0]), int(big / 2 - pin[1])))
    if abs(ang) > 0.05:
        canvas = canvas.rotate(ang, Image.BICUBIC, center=(big / 2, big / 2))
    L.alpha_composite(canvas, (int(at[0] - big / 2), int(at[1] - big / 2)))


def _scaled(char, name, s):
    im = part(char, name)
    if im is None:
        return None
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)


@lru_cache(256)
def _scaled_cached(char, name, s100):
    return _scaled(char, name, s100 / 1000.0)


def _arm_at(arm_keys, t):
    cur = arm_keys[0][1] if arm_keys else "rest"
    prev, tc = cur, -9
    for k in arm_keys or []:
        if k[0] <= t:
            prev, cur, tc = cur, k[1], k[0]
    q = min(1.0, max(0.0, (t - tc) / 0.25))
    q = q * q * (3 - 2 * q)
    a0, a1 = ARM_POSES[prev], ARM_POSES[cur]
    l = a0[0] + (a1[0] - a0[0]) * q
    r = a0[1] + (a1[1] - a0[1]) * q
    if cur == "wave":
        r += 18 * math.sin(t * 9)
    return l, r


def _pos_at(path, t):
    """path [(t,x),...] -> x, hız (px/sn)"""
    if not path:
        return 540, 0.0
    if t <= path[0][0]:
        return path[0][1], 0.0
    for (ta, xa), (tb, xb) in zip(path, path[1:]):
        if ta <= t <= tb:
            q = (t - ta) / max(1e-6, tb - ta)
            return xa + (xb - xa) * q, (xb - xa) / max(1e-6, tb - ta)
    return path[-1][1], 0.0


def draw(L, ov, t, R):
    """render.py overlay'i: kuklayı L katmanına çizer."""
    char = ov["char"]
    rig = RIG[char]
    t0, t1 = ov["t0"], ov["t1"]
    if t < t0 or t > t1:
        return
    x, vx = _pos_at(ov.get("path", [(t0, ov.get("x", 540))]), t)
    walking = abs(vx) > 5
    face = ov.get("face", "r")
    if walking:
        face = "r" if vx > 0 else "l"
    flip = face == "l"
    H_total = ov.get("h", 900)
    torso = part(char, "torso")
    head = part(char, "head")
    leg = part(char, "lleg")
    # toplam yükseklik ≈ kafa + gövde*0.8 + bacak*0.45 (bacaklar gövde altına girer)
    raw_h = head.height * 0.9 + torso.height * rig["hip_l"][1] + leg.height
    s = H_total / raw_h
    s1000 = int(s * 1000)
    tor = _scaled_cached(char, "torso", s1000)
    y_feet = ov.get("y", 1500)
    # yürüme döngüsü
    ph = (t - t0) * 2 * math.pi * 1.9 if walking else 0.0
    swing = 22 * math.sin(ph) if walking else 0.0
    bob = -abs(math.sin(ph)) * 10 * s * 3 if walking else 0.0
    breathe = math.sin((t - t0) * 2 * math.pi * 0.5) * 3
    # düşme
    fall = ov.get("fall")
    fall_q = 0.0
    if fall is not None and t >= fall:
        fall_q = min(1.0, (t - fall) / 0.35)
        fall_q = 1 - (1 - fall_q) ** 3
    legs_h = leg.height * s
    hip_y = y_feet - legs_h * 0.97 + bob
    tor_top = hip_y - tor.height * rig["hip_l"][1]
    tor_left = x - tor.width / 2

    def tp(fr):
        fx, fy = fr
        if flip:
            fx = 1 - fx
        return (tor_left + fx * tor.width, tor_top + fy * tor.height + breathe * 0.3)

    layer = L if fall_q == 0 else Image.new("RGBA", L.size, (0, 0, 0, 0))
    lg = _scaled_cached(char, "lleg", s1000)
    rg = _scaled_cached(char, "rleg", s1000)
    pin = lambda im, fr: (im.width * fr[0], im.height * fr[1])
    # bacaklar
    _paste_rot(layer, lg, pin(lg, rig["leg_pin"]), tp(rig["hip_l"]), swing, flip)
    _paste_rot(layer, rg, pin(rg, rig["leg_pin"]), tp(rig["hip_r"]), -swing, flip)
    # arka kol (yürürken)
    la, ra = _arm_at(ov.get("arm"), t)
    if walking:
        la, ra = -swing * 0.8, swing * 0.8
    la_img = _scaled_cached(char, "larm", s1000)
    ra_img = _scaled_cached(char, "rarm", s1000)
    # gövde
    layer.alpha_composite(tor, (int(tor_left), int(tor_top + breathe * 0.3)))
    # kollar (sol kol ekranda solda: + açı dışa = saat yönü tersi)
    _paste_rot(layer, la_img, pin(la_img, rig["arm_pin"]), tp(rig["sh_l"]), -la, flip)
    _paste_rot(layer, ra_img, pin(ra_img, rig["arm_pin"]), tp(rig["sh_r"]), ra, flip)
    # kafa
    hname = "head"
    if walking and rig.get("side_head"):
        hname = rig["side_head"]
    hd = _scaled_cached(char, hname, s1000)
    talking = False
    tk = ov.get("talk")
    if tk is True:
        talking = True
    elif tk:
        talking = any(a <= t <= b for a, b in tk)
    amp = mouth_amp(R.BUILD, t) if talking else 0.0
    nod = (2.5 * math.sin((t - t0) * 7.3) * amp) + 1.2 * math.sin((t - t0) * 1.3)
    hp = pin(hd, rig["head_pin"])
    neck = tp(rig["neck"])
    hd2 = hd.copy()
    if hname == "head":
        _face(hd2, rig, amp, t, ov)
    _paste_rot(layer, hd2, hp, (neck[0], neck[1] + 6 * s * 3), nod, flip)
    if fall_q > 0:
        ang = 90 * fall_q * (-1 if face == "r" else 1)
        a = 1.0 if t - fall < 1.2 else max(0.0, 1 - (t - fall - 1.2) / 0.5)
        rot = layer.rotate(ang, Image.BICUBIC, center=(x, y_feet))
        if a < 1:
            rot.putalpha(rot.split()[3].point(lambda v: int(v * a)))
        L.alpha_composite(rot)


EYES = {  # elle ölçülmüş göz kutuları (kafa görselinde kesir)
    "anlatici": ((0.385, 0.565, 0.465, 0.735), (0.555, 0.565, 0.635, 0.735)),
    "padisah": ((0.395, 0.665, 0.475, 0.785), (0.565, 0.665, 0.645, 0.785)),
    "vezir": ((0.40, 0.62, 0.47, 0.77), (0.615, 0.62, 0.68, 0.77)),
    "sehzade": ((0.395, 0.595, 0.475, 0.725), (0.675, 0.595, 0.755, 0.725)),
}


@lru_cache(16)
def eye_boxes(char):
    if char in EYES:
        return EYES[char]
    return _detect_eyes(char)


@lru_cache(16)
def _detect_eyes(char):
    """Kafa görselinde iki gözü (yüz bölgesindeki en büyük, yuvarlak siyah lekeler) bul; kesir kutular döndür."""
    from collections import deque
    im = part(char, "head")
    a = np.asarray(im)
    h, w = a.shape[:2]
    dark0 = ((a[..., :3].max(axis=2) < 70) & (a[..., 3] > 200)).astype(np.uint8) * 255
    k = max(3, int(w * 0.022) | 1)
    dark = np.asarray(Image.fromarray(dark0).filter(ImageFilter.MinFilter(k)).filter(ImageFilter.MaxFilter(k))) > 0
    y_lo = int(h * 0.35)
    seen = np.zeros_like(dark)
    blobs = []
    for y in range(y_lo, int(h * 0.85)):
        for x in range(int(w * 0.15), int(w * 0.85)):
            if dark[y, x] and not seen[y, x]:
                q = deque([(y, x)]); seen[y, x] = True; pts = []
                while q:
                    cy, cx = q.popleft(); pts.append((cy, cx))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and dark[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                bw, bh = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
                fill = len(pts) / (bw * bh)
                if len(pts) > 40 and 0.35 < bw / bh < 1.4 and fill > 0.5 and bh < h * 0.3:
                    blobs.append((len(pts), min(xs), min(ys), max(xs), max(ys)))
    blobs.sort(reverse=True)
    eyes = sorted(blobs[:2], key=lambda b: b[1])
    return tuple((b[1] / w, b[2] / h, (b[3] + 1) / w, (b[4] + 1) / h) for b in eyes)


def _face(hd, rig, amp, t, ov):
    """ağız (ses zarfına göre) + göz kırpma, kafa görseline yerinde çizilir."""
    d = ImageDraw.Draw(hd)
    w, h = hd.size
    # göz kırpma: ~3.7 sn'de bir, 0.12 sn
    seed = (hash(ov["char"]) % 97) / 97.0
    cyc = (t + seed * 3) % 3.7
    if cyc < 0.12:
        eb = eye_boxes(ov["char"])
        if len(eb) == 2:
            sx = (eb[0][2] + eb[1][0]) / 2 * w
            sy = (eb[0][1] + eb[0][3]) / 2 * h
            skin = hd.getpixel((int(sx), int(sy)))[:3]
        for (x0, y0, x1, y1) in eb:
            x0, y0, x1, y1 = x0 * w, y0 * h, x1 * w, y1 * h
            pad = (x1 - x0) * 0.25
            d.ellipse((x0 - pad, y0 - pad, x1 + pad, y1 + pad), fill=skin + (255,))
            cy = (y0 + y1) / 2 + (y1 - y0) * 0.15
            d.line((x0 - pad * 0.6, cy, x1 + pad * 0.6, cy), fill=(15, 10, 10, 255), width=max(2, int((x1 - x0) * 0.22)))
    if amp > 0.05:
        mx, my = rig["mouth"][0] * w, rig["mouth"][1] * h
        mw = w * 0.085 * (0.8 + 0.4 * amp)
        mh = h * 0.075 * amp
        d.ellipse((mx - mw, my - mh * 0.3, mx + mw, my + mh), fill=(70, 12, 12, 255), outline=(10, 5, 5, 255),
                  width=max(2, int(w * 0.008)))
        if mh > h * 0.02:
            d.ellipse((mx - mw * 0.55, my + mh * 0.35, mx + mw * 0.55, my + mh * 0.95), fill=(225, 95, 105, 255))


# ---------------------------------------------------------------- yardımcı sahne nesneleri
def draw_tabut(L, ov, t):
    """Tabutlar: n adet, perspektifte sıralı; her biri 'every' sn arayla belirir."""
    n = ov.get("n", 19)
    t0 = ov["t0"]
    if t < t0 or t > ov["t1"]:
        return
    d = ImageDraw.Draw(L)
    cols = ov.get("cols", 5)
    for i in range(n):
        q = (t - t0 - i * ov.get("every", 0.08)) / 0.25
        if q <= 0:
            continue
        q = min(1.0, q)
        row, col = divmod(i, cols)
        sc = 1.0 - row * 0.16
        w, h = 150 * sc, 62 * sc
        x = 540 + (col - (cols - 1) / 2) * 175 * sc
        y = ov.get("y", 1560) - row * 120
        yy = y - (1 - q) * 60
        a = int(255 * q)
        d.rounded_rectangle((x - w / 2, yy - h, x + w / 2, yy), int(14 * sc), fill=(40, 90, 55, a), outline=(10, 10, 10, a), width=4)
        d.rounded_rectangle((x - w / 2 + 8, yy - h - 18 * sc, x + w / 2 - 8, yy - h + 8), int(12 * sc), fill=(30, 70, 45, a),
                            outline=(10, 10, 10, a), width=3)
        d.ellipse((x - 12 * sc, yy - h - 34 * sc, x + 12 * sc, yy - h - 10 * sc), fill=(235, 235, 225, a), outline=(10, 10, 10, a), width=3)
