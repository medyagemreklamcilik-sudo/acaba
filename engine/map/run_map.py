"""Harita videosu giriş noktası: render.py arka planını animasyonlu haritayla değiştirir.
Kullanım: VIDEO_DIR=videolar/<klasör> python3 engine/map/run_map.py <outdir> [workers]
Video klasöründe mapdata.py + scenes.py olmalı."""
import math, os, sys
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFont, ImageChops

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import render as R
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mapviz as MV
import mapdata as MD

W, H = R.W, R.H
YEL, WHITE = R.YEL, R.WHITE
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


@lru_cache(8)
def dejavu(size):
    return ImageFont.truetype(DEJAVU, size)


def base_frame(t):
    if t < 2.98:
        img, _ = MV.render(t, "max")
    elif t < 4.3:
        img, view = MV.render(t, "max")
        m, v2 = MV.masks(view, 122.0)
        landm = Image.new("L", (W, H), 0)
        MV.draw_rings(ImageDraw.Draw(landm), view, MV.land(), 255)
        tm = Image.new("L", (W, H), 0)
        MV.draw_rings(ImageDraw.Draw(tm), view, MV.turkey(), 255)
        lost = ImageChops.multiply(ImageChops.subtract(ImageChops.lighter(m, v2), tm), landm)
        dt = t - 2.98
        a = 0.55 + 0.4 * abs(math.sin(dt * math.pi * 3)) if dt < 0.9 else 0.95
        img.paste((255, 45, 45), (0, 0), lost.point(lambda v: int(v * a)))
        if dt > 0.9:
            tur, _ = MV.render(t, "turkey")
            img = Image.blend(img, tur, R.ease((dt - 0.9) / 0.4))
    elif t < 10.3:
        img, _ = MV.render(t, "turkey")
    elif t < 11.6:
        img, _ = MV.render(t, "none")
    else:
        img, _ = MV.render(t)
    return img


@lru_cache(40)
def sultan_disc(idx, size):
    s = [x for x in MD.SULTANS if x[1] == idx][0]
    fx, fy, dfrac = s[4]
    im = Image.open(os.path.join(R.IMG, f"s{idx:02d}.jpg")).convert("RGB")
    w, h = im.size
    d = dfrac * w
    cx, cy = fx * w, fy * h
    box = (int(cx - d / 2), int(cy - d / 2), int(cx + d / 2), int(cy + d / 2))
    tile = im.crop(box).resize((size, size), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((0, 0, size - 1, size - 1), fill=255)
    tile.putalpha(m)
    ring = Image.new("RGBA", (size + 14, size + 14), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, size + 13, size + 13), fill=YEL + (255,))
    ring.alpha_composite(tile, (7, 7))
    return ring


def year_at(t):
    ys = MD.YEARS
    if t < ys[0][0]:
        return None
    cur, prev = ys[0], ys[0][1]
    for i, (tt, y) in enumerate(ys):
        if tt <= t:
            cur = (tt, y)
            prev = ys[i - 1][1] if i > 0 else y
    q = R.eout((t - cur[0]) / 0.7, 3)
    return int(round(prev + (cur[1] - prev) * q))


def ov_mapui(L, ov, t):
    d = ImageDraw.Draw(L)
    view = MV.View(t)
    pill, font, clamp, back_out, eout, ease = R.pill_text, R.font, R.clamp, R.back_out, R.eout, R.ease
    # capital star
    if 12.0 <= t < 198.0:
        cap = [c for c in MD.CAPITALS if c[0] <= t][-1]
        x, y = view.xy(*cap[2])
        if -50 < x < W + 50 and -50 < y < H + 50:
            f = dejavu(int(34 * (1 + 0.15 * math.sin(t * 5))))
            d.text((x + 2, y + 2), "★", font=f, fill=(0, 0, 0, 200), anchor="mm")
            d.text((x, y), "★", font=f, fill=YEL + (255,), anchor="mm")
    # battles
    for bt, name, ll, dur in MD.BATTLES:
        dt = t - bt
        if 0 <= dt < dur:
            a = min(1, dt / 0.2, (dur - dt) / 0.3)
            x, y = view.xy(*ll)
            sc = 1 + 0.6 * max(0, 1 - dt / 0.25)
            col = (255, 80, 80) if ("VİYANA" in name or "ANKARA" in name) else (255, 255, 255)
            d.ellipse((x - 40 * sc, y - 40 * sc, x + 40 * sc, y + 40 * sc), fill=(0, 0, 0, int(170 * a)))
            d.text((x, y + 2), "⚔", font=dejavu(int(54 * sc)), fill=col + (int(255 * a),), anchor="mm")
            pill(d, x, y + 76, name, font("anton", 38), WHITE, bg=(0, 0, 0, int(220 * a)), padx=14, pady=8)
    # region labels
    for t0, kind, reg, lab in MD.OPS:
        if not lab:
            continue
        dt = t - t0
        if 0 <= dt < 2.4:
            ll = MD.ANCHOR.get(reg)
            if not ll:
                continue
            a = min(1, dt / 0.15, (2.4 - dt) / 0.35)
            x, y = view.xy(*ll)
            x = clamp(x, R.SAFE_L + 170, R.SAFE_R - 170)
            y = clamp(y, 640, 1260)
            f = font("anton", int(40 * (0.8 + 0.2 * back_out(dt / 0.3))))
            bg, fg = ((230, 30, 30), WHITE) if kind == "sub" else (((0, 0, 0), YEL) if kind == "flash" else ((30, 160, 80), WHITE))
            pill(d, x, y - 46, lab, f, fg + (int(255 * a),), bg=bg + (int(235 * a),), padx=16, pady=9)
            d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=WHITE + (int(255 * a),))
    # Sevr labels
    if 193.6 <= t < 199.4:
        a = min(1, (t - 193.6) / 0.4, (199.4 - t) / 0.4)
        for i, (name, col, p, ll) in enumerate(MD.SEVR):
            if t >= 193.6 + 0.25 * i:
                x, y = view.xy(*ll)
                pill(d, x, y, name, font("anton", 34), WHITE, bg=col + (int(235 * a),), padx=12, pady=7)
    # sultan card
    if 12.42 <= t < 201.5:
        cur = [s for s in MD.SULTANS if s[0] <= t][-1]
        q = (t - cur[0]) / 0.3
        out = 1 - ease((t - 200.8) / 0.6)
        disc = sultan_disc(cur[1], 190)
        s = 0.5 + 0.5 * back_out(q)
        dd = disc.resize((max(1, int(disc.width * s)), max(1, int(disc.height * s))), Image.BILINEAR)
        if out < 1:
            dd.putalpha(dd.split()[3].point(lambda v: int(v * out)))
        cx, cy = R.SAFE_L + 105, 340
        L.alpha_composite(dd, (int(cx - dd.width / 2), int(cy - dd.height / 2)))
        al = int(255 * out)
        tx = R.SAFE_L + 222 + int((1 - eout(q, 3)) * 80)
        name = cur[2]
        fn = font("anton", 58 if len(name) < 16 else 48 if len(name) < 21 else 42)
        d.rectangle((tx, 290, tx + 80, 352), fill=YEL + (al,))
        d.text((tx + 40, 322), str(cur[1]), font=font("anton", 46), fill=(0, 0, 0, al), anchor="mm")
        nw = d.textlength(name, font=fn)
        d.rectangle((tx + 80, 290, tx + 80 + nw + 34, 352), fill=(0, 0, 0, int(225 * out)))
        d.text((tx + 97, 322), name, font=fn, fill=WHITE + (al,), anchor="lm")
        d.rectangle((tx, 360, tx + 250, 406), fill=(0, 0, 0, int(200 * out)))
        d.text((tx + 14, 383), cur[3], font=font("mont", 30, 800), fill=YEL + (al,), anchor="lm")
    # year counter
    yv = year_at(t)
    if yv is not None and t < 211.0:
        f = font("anton", 130)
        x, y = R.SAFE_R - 10, 530
        d.text((x + 5, y + 7), str(yv), font=f, fill=(0, 0, 0, 180), anchor="rm")
        d.text((x, y), str(yv), font=f, fill=YEL + (255,), anchor="rm", stroke_width=3, stroke_fill=(0, 0, 0, 255))
    # legend
    if 12.4 <= t < 198:
        y, x = 1330, R.SAFE_L + 8
        d.rounded_rectangle((x, y - 22, x + 540, y + 22), 10, fill=(0, 0, 0, 170))
        d.rectangle((x + 14, y - 10, x + 38, y + 10), fill=(130, 255, 150, 255))
        d.text((x + 46, y), "Fetih", font=font("mont", 24, 700), fill=WHITE + (255,), anchor="lm")
        d.rectangle((x + 140, y - 10, x + 164, y + 10), fill=(255, 45, 45, 255))
        d.text((x + 172, y), "Kayıp", font=font("mont", 24, 700), fill=WHITE + (255,), anchor="lm")
        d.text((x + 275, y), "Sınırlar yaklaşıktır", font=font("mont", 20, 500), fill=(200, 200, 200, 255), anchor="lm")


R.base_frame = base_frame
R.OV["mapui"] = ov_mapui

if __name__ == "__main__":
    R.main()
