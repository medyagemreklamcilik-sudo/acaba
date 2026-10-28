"""Harita üzerinde yolculuk sahnesi (render.py "journey" modu).

scenes.py içinde:
  JOURNEY = [(anahtar, "ETİKET", lon, lat, ölçek), ...]   # durak sırası
  sahne: dict(t=..., mode="journey", stop=<indeks>, year="1911", portrait="img_anahtarı", rank="RÜTBE",
              tint=True)   # tint: 1919 sonrası Anadolu'yu kırmızı vurgula
Kamera önceki duraktan bu durağa uzaklaşıp yakınlaşarak uçar, rota çizgisi uzar, durak iğnesi atar.
"""
import json, math, os
from functools import lru_cache

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

W, H = 1080, 1920
KX = 0.80
CY = 820
GEO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "geo")
SEA_TOP, SEA_BOT = np.array([10, 16, 26], np.float32), np.array([16, 26, 40], np.float32)
LAND = (64, 58, 50)
COAST = (110, 100, 86)
ROUTE = (255, 214, 10)
PIN = (235, 40, 40)
FLY = 1.5


def _rings(path, bbox=(5, 20, 55, 50)):
    d = json.load(open(path))
    out = []
    for f in d["features"]:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for p in polys:
            r = np.array(p[0], np.float32)
            if len(r) < 4:
                continue
            if r[:, 0].max() < bbox[0] or r[:, 0].min() > bbox[2] or r[:, 1].max() < bbox[1] or r[:, 1].min() > bbox[3]:
                continue
            out.append(r)
    return out


@lru_cache(1)
def land():
    return _rings(os.path.join(GEO, "ne_50m_land.geojson"))


@lru_cache(1)
def lakes():
    return _rings(os.path.join(GEO, "ne_50m_lakes.geojson"))


@lru_cache(1)
def turkey():
    d = json.load(open(os.path.join(GEO, "ne_50m_admin_0_countries.geojson")))
    for f in d["features"]:
        p = f["properties"]
        if p.get("ADM0_A3") == "TUR" or p.get("ISO_A3") == "TUR":
            g = f["geometry"]
            polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            return [np.array(pp[0], np.float32) for pp in polys]
    return []


@lru_cache(1)
def sea():
    g = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
    a = np.repeat(SEA_TOP * (1 - g) + SEA_BOT * g, W, axis=1)
    return Image.fromarray(a.astype(np.uint8))


class View:
    def __init__(self, lon, lat, s):
        self.lon, self.lat, self.s = lon, lat, s

    def xy(self, lon, lat):
        return (lon - self.lon) * KX * self.s + W / 2, -(lat - self.lat) * self.s + CY

    def poly(self, d, rings, fill):
        for r in rings:
            x = (r[:, 0] - self.lon) * KX * self.s + W / 2
            y = -(r[:, 1] - self.lat) * self.s + CY
            if x.max() < -50 or x.min() > W + 50 or y.max() < -50 or y.min() > H + 50:
                continue
            pts = list(zip(x.tolist(), y.tolist()))
            if len(pts) > 2:
                d.polygon(pts, fill=fill)


def _ease(p):
    p = min(1.0, max(0.0, p))
    return p * p * (3 - 2 * p)


def camera(S, i, t, t0):
    J = S.JOURNEY
    cur = J[i]
    if i == 0:
        p = _ease((t - t0) / FLY)
        s = math.exp(math.log(14) + (math.log(cur[4]) - math.log(14)) * p)
        return View(cur[2] + (31 - cur[2]) * (1 - p), cur[3] + (36 - cur[3]) * (1 - p), s)
    prev = J[i - 1]
    p = _ease((t - t0) / FLY)
    lon = prev[2] + (cur[2] - prev[2]) * p
    lat = prev[3] + (cur[3] - prev[3]) * p
    dist = math.hypot((cur[2] - prev[2]) * KX, cur[3] - prev[3])
    s = math.exp(math.log(prev[4]) + (math.log(cur[4]) - math.log(prev[4])) * p)
    dip = min(0.55, dist / 25.0)
    s *= 1 - dip * math.sin(math.pi * p)
    # yavaş itme
    s *= 1 + 0.04 * max(0.0, t - t0 - FLY)
    return View(lon, lat, s)


def frame(sc, t, R):
    S = R.S
    i = sc["stop"]
    J = S.JOURNEY
    v = camera(S, i, t, sc["t"])
    img = sea().copy()
    landm = Image.new("L", (W, H), 0)
    dl = ImageDraw.Draw(landm)
    v.poly(dl, land(), 255)
    v.poly(dl, lakes(), 0)
    landm = landm.filter(ImageFilter.GaussianBlur(0.8))
    img.paste(Image.new("RGB", (W, H), LAND), (0, 0), landm)
    coast = ImageChops.subtract(landm, landm.filter(ImageFilter.MinFilter(3)))
    img.paste(Image.new("RGB", (W, H), COAST), (0, 0), coast)
    if sc.get("tint"):
        a = 1.0 if sc.get("tint") == "on" else _ease((t - sc["t"]) / 1.2)
        tm = Image.new("L", (W, H), 0)
        v.poly(ImageDraw.Draw(tm), turkey(), 255)
        tm = ImageChops.multiply(tm, landm)
        img.paste(Image.new("RGB", (W, H), (150, 25, 30)), (0, 0), tm.point(lambda q: int(q * 0.55 * a)))
        edge = ImageChops.subtract(tm.filter(ImageFilter.MaxFilter(5)), tm)
        img.paste(Image.new("RGB", (W, H), (255, 120, 110)), (0, 0), edge.point(lambda q: int(q * 0.8 * a)))

    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    pts = [v.xy(j[2], j[3]) for j in J[: i + 1]]
    # rota
    for k in range(1, len(pts)):
        x0, y0 = pts[k - 1]
        x1, y1 = pts[k]
        prog = 1.0 if k < i else _ease((t - sc["t"] - 0.15) / (FLY - 0.2))
        if prog <= 0:
            continue
        # hafif kavis
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        nx, ny = -(y1 - y0), (x1 - x0)
        nl = max(1.0, math.hypot(nx, ny))
        bend = 0.18 * math.hypot(x1 - x0, y1 - y0)
        cx, cy = mx + nx / nl * bend, my + ny / nl * bend
        n = 40
        curve = []
        for q in range(int(n * prog) + 1):
            u = q / n
            curve.append(((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1))
        if len(curve) > 1:
            al = 255 if k == i else 150
            d.line(curve, fill=(0, 0, 0, int(al * 0.7)), width=13, joint="curve")
            d.line(curve, fill=ROUTE + (al,), width=7, joint="curve")
            if k == i and prog < 1:
                hx, hy = curve[-1]
                d.ellipse((hx - 12, hy - 12, hx + 12, hy + 12), fill=ROUTE + (255,))
    # eski duraklar
    for k, (x, y) in enumerate(pts[:-1]):
        d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=(0, 0, 0, 200))
        d.ellipse((x - 6, y - 6, x + 6, y + 6), fill=(255, 255, 255, 220))
        if sc.get("names", True):
            d.text((x + 14, y), J[k][1].split(" · ")[0], font=R.font("mont", 24, 700), fill=(230, 230, 230, 200), anchor="lm",
                   stroke_width=3, stroke_fill=(0, 0, 0, 200))
    # şimdiki durak
    x, y = pts[-1]
    q = (t - sc["t"] - FLY + 0.15) / 0.35
    if q > 0:
        s = R.back_out(min(1.0, q))
        for ring in range(3):
            ph = ((t * 1.1) + ring / 3) % 1.0
            rr = 18 + 70 * ph
            d.ellipse((x - rr, y - rr, x + rr, y + rr), outline=PIN + (int(220 * (1 - ph)),), width=5)
        r = 16 * s
        d.ellipse((x - r - 5, y - r - 5, x + r + 5, y + r + 5), fill=(255, 255, 255, 255))
        d.ellipse((x - r, y - r, x + r, y + r), fill=PIN + (255,))
        lab = J[i][1]
        if sc.get("year"):
            lab = f"{sc['year']} · {lab}"
        f = R.font("anton", int(60 * min(1.0, 0.6 + 0.4 * s)))
        tw = d.textlength(lab, font=f)
        lx = min(max(x, R.SAFE_L + tw / 2 + 30), R.SAFE_R - tw / 2 - 30)
        ly = y - 92
        R.pill_text(d, lx, ly, lab, f, (0, 0, 0), bg=ROUTE + (255,), padx=22, pady=10)
    # portre kartı
    if sc.get("portrait"):
        qa = (t - sc["t"] - 0.3) / 0.4
        if qa > 0:
            disc = portrait_disc(R, sc["portrait"], 230)
            s = 0.6 + 0.4 * R.back_out(min(1.0, qa))
            dd = disc.resize((int(disc.width * s), int(disc.height * s)), Image.BILINEAR)
            cx, cy = R.SAFE_L + 130, 360
            L.alpha_composite(dd, (int(cx - dd.width / 2), int(cy - dd.height / 2)))
            if sc.get("rank"):
                f = R.font("anton", 50)
                tx = R.SAFE_L + 265 + int((1 - R.eout(min(1.0, qa), 3)) * 60)
                rk = sc["rank"]
                tw = d.textlength(rk, font=f)
                d.rectangle((tx, 318, tx + tw + 36, 378), fill=(0, 0, 0, 225))
                d.text((tx + 18, 348), rk, font=f, fill=ROUTE + (255,), anchor="lm")
                if sc.get("role"):
                    f2 = R.font("mont", 30, 800)
                    tw2 = d.textlength(sc["role"], font=f2)
                    d.rectangle((tx, 384, tx + tw2 + 28, 428), fill=(255, 255, 255, 235))
                    d.text((tx + 14, 406), sc["role"], font=f2, fill=(0, 0, 0, 255), anchor="lm")
    img = img.convert("RGBA")
    img.alpha_composite(L)
    return img.convert("RGB")


_disc_cache = {}


def portrait_disc(R, key, size):
    k = (key, size)
    if k in _disc_cache:
        return _disc_cache[k]
    im = R.load(key, "std")
    fc = R.S.FACES.get(key, (0.5, 0.3))
    fx, fy = fc[0], fc[1]
    side = min(im.width, im.height) * (fc[2] if len(fc) > 2 else 0.62)
    cx = min(max(fx * im.width, side / 2), im.width - side / 2)
    cy = min(max(fy * im.height, side / 2), im.height - side / 2)
    tile = im.crop((int(cx - side / 2), int(cy - side / 2), int(cx + side / 2), int(cy + side / 2))).resize((size, size), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((0, 0, size - 1, size - 1), fill=255)
    tile.putalpha(m)
    ring = Image.new("RGBA", (size + 16, size + 16), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, size + 15, size + 15), fill=ROUTE + (255,))
    ring.alpha_composite(tile, (8, 8))
    _disc_cache[k] = ring
    return ring
