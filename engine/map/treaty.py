"""Sevr / Lozan / Ege adaları haritası (render.py "treaty" modu).

sahne: dict(t=..., mode="treaty", layer="sevr" | "lozan" | "adalar", marks=[(t, anahtar), ...])
  sevr  : Sevr bölgeleri sırayla taranır, etiketlenir
  lozan : Sevr bölgeleri söner, 1923 Türkiye sınırı kırmızı dolar
  adalar: Onikiada (İtalya 1912), Kuzey/Doğu Ege adaları (Yunanistan 1914), Gökçeada-Bozcaada (Türkiye 1923)
"""
import math
from PIL import Image, ImageDraw, ImageFilter, ImageChops

import journey as JY

W, H = JY.W, JY.H
SEVR = [("YUNANİSTAN", (233, 90, 70), (27.6, 38.6)), ("İTALYA", (40, 160, 90), (31.3, 37.6)),
        ("FRANSA", (60, 110, 230), (36.4, 37.3)), ("ERMENİSTAN", (190, 70, 190), (41.6, 40.0)),
        ("BOĞAZLAR", (230, 190, 60), (28.0, 41.05))]
ISLANDS_1914 = [("LİMNİ", 25.25, 39.9), ("MİDİLLİ", 26.3, 39.2), ("SAKIZ", 26.0, 38.4), ("SEMADİREK", 25.55, 40.47),
                ("SİSAM", 26.8, 37.75), ("İKARYA", 26.15, 37.6)]
ISLANDS_TR = [("GÖKÇEADA", 25.85, 40.18), ("BOZCAADA", 26.05, 39.83)]
VIEWS = {"sevr": (35.4, 38.9, 52), "lozan": (35.4, 38.9, 52), "adalar": (26.7, 38.9, 175)}


def _ease(p):
    p = min(1.0, max(0.0, p))
    return p * p * (3 - 2 * p)


def _hatch():
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)
    for k in range(-H, W, 24):
        d.line([(k, 0), (k + H, H)], fill=255, width=9)
    return im


_HATCH = None


def frame(sc, t, R):
    global _HATCH
    import mapviz_regions as MR
    layer = sc["layer"]
    dt = t - sc["t"]
    lon, lat, s = VIEWS[layer]
    s *= 1 + (0.008 if layer == "adalar" else 0.035) * dt
    v = JY.View(lon, lat, s)
    img = JY.sea().copy()
    landm = Image.new("L", (W, H), 0)
    dl = ImageDraw.Draw(landm)
    v.poly(dl, JY.land(), 255)
    v.poly(dl, JY.lakes(), 0)
    landm = landm.filter(ImageFilter.GaussianBlur(0.8))
    img.paste(Image.new("RGB", (W, H), JY.LAND), (0, 0), landm)
    coast = ImageChops.subtract(landm, landm.filter(ImageFilter.MinFilter(3)))
    img.paste(Image.new("RGB", (W, H), JY.COAST), (0, 0), coast)
    tm = Image.new("L", (W, H), 0)
    v.poly(ImageDraw.Draw(tm), JY.turkey(), 255)
    tm = ImageChops.multiply(tm, landm)
    edge = ImageChops.subtract(tm.filter(ImageFilter.MaxFilter(5)), tm)
    if _HATCH is None:
        _HATCH = _hatch()
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    marks = sc.get("marks", [])

    def at(key, default=0.0):
        for mt, k in marks:
            if k == key:
                return mt
        return sc["t"] + default

    if layer in ("sevr", "lozan"):
        fade = 1.0 if layer == "sevr" else 1 - _ease(dt / 1.2)
        for i, (name, col, ll) in enumerate(SEVR):
            a = _ease((t - at(name, 0.4 + 0.5 * i)) / 0.5) * fade
            if a <= 0:
                continue
            m = Image.new("L", (W, H), 0)
            v.poly(ImageDraw.Draw(m), MR.sevr(name), 255)
            m = ImageChops.multiply(ImageChops.multiply(m, landm), _HATCH)
            img.paste(Image.new("RGB", (W, H), col), (0, 0), m.point(lambda q: int(q * 0.9 * a)))
            x, y = v.xy(*ll)
            R.pill_text(d, x, y, name, R.font("anton", 40), R.WHITE + (int(255 * a),), bg=col + (int(235 * a),), padx=14, pady=8)
        img.paste(Image.new("RGB", (W, H), (255, 255, 255)), (0, 0), edge.point(lambda q: int(q * 0.5)))
        if layer == "lozan":
            a = _ease((dt - 0.6) / 1.4)
            img.paste(Image.new("RGB", (W, H), (200, 20, 30)), (0, 0), tm.point(lambda q: int(q * 0.8 * a)))
            img.paste(Image.new("RGB", (W, H), (255, 255, 255)), (0, 0), edge.point(lambda q: int(q * a)))
            glow = tm.filter(ImageFilter.GaussianBlur(16))
            img = ImageChops.screen(img, Image.merge("RGB", [glow.point(lambda q: int(q * 0.3 * a))] * 3))
            if a > 0.3:
                x, y = v.xy(34.0, 39.2)
                R.pill_text(d, x, y, "LOZAN · 1923", R.font("anton", 64), (0, 0, 0, int(255 * a)), bg=R.YEL + (int(255 * a),), padx=24, pady=12)
    else:
        img.paste(Image.new("RGB", (W, H), (255, 255, 255)), (0, 0), edge.point(lambda q: int(q * 0.35)))
        # Onikiada · İtalya 1912
        a = _ease((t - at("onikiada", 0.5)) / 0.6)
        if a > 0:
            m = Image.new("L", (W, H), 0)
            v.poly(ImageDraw.Draw(m), MR.region("onikiada"), 255)
            m = ImageChops.multiply(m, landm)
            img.paste(Image.new("RGB", (W, H), (40, 160, 90)), (0, 0), m.point(lambda q: int(q * 0.95 * a)))
            x, y = v.xy(27.8, 36.0)
            R.pill_text(d, x, y + 40, "ONİKİADA · İTALYA 1912", R.font("anton", 44), R.WHITE + (int(255 * a),), bg=(40, 140, 80, int(240 * a)), padx=16, pady=9)
        # Yunanistan 1914
        a = _ease((t - at("1914", 4.0)) / 0.6)
        for i, (name, lo, la) in enumerate(ISLANDS_1914):
            ai = _ease((t - at("1914", 4.0) - 0.15 * i) / 0.4)
            if ai <= 0:
                continue
            x, y = v.xy(lo, la)
            r = 38
            d.ellipse((x - r, y - r, x + r, y + r), outline=(80, 140, 255, int(255 * ai)), width=7)
            d.text((x - r - 10, y), name, font=R.font("anton", 34), fill=R.WHITE + (int(255 * ai),), anchor="rm",
                   stroke_width=4, stroke_fill=(0, 0, 0, int(255 * ai)))
        if a > 0:
            R.pill_text(d, W / 2, 255, "YUNANİSTAN'A · 1914", R.font("anton", 52), R.WHITE + (int(255 * a),), bg=(50, 100, 220, int(240 * a)), padx=20, pady=10)
        # Türkiye 1923
        a = _ease((t - at("tr", 8.0)) / 0.5)
        for name, lo, la in ISLANDS_TR:
            if a <= 0:
                continue
            x, y = v.xy(lo, la)
            ph = (t * 1.2) % 1.0
            rr = 30 + 50 * ph
            d.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(255, 60, 60, int(220 * (1 - ph) * a)), width=5)
            d.ellipse((x - 16, y - 16, x + 16, y + 16), fill=(230, 30, 30, int(255 * a)))
            d.text((x + 28, y), name, font=R.font("anton", 40), fill=R.YEL + (int(255 * a),), anchor="lm",
                   stroke_width=4, stroke_fill=(0, 0, 0, int(255 * a)))
        if a > 0:
            R.pill_text(d, W / 2, 360, "TÜRKİYE'DE KALDI · 1923", R.font("anton", 52), (0, 0, 0, int(255 * a)), bg=R.YEL + (int(255 * a),), padx=20, pady=10)
    img = img.convert("RGBA")
    img.alpha_composite(L)
    return img.convert("RGB")
