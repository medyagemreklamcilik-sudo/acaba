"""Animated historical map renderer (vector, per frame) for the Ottoman timeline video."""
import json, math, os
from functools import lru_cache

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

import mapdata as M

W, H = 1080, 1920
KX = 0.80          # horizontal compression (approx. equirectangular at ~37°N)
CY = 880           # screen y of the camera centre
ROOT = os.path.dirname(os.path.abspath(__file__))
GEO = os.path.join(ROOT, "..", "geo")

SEA_TOP, SEA_BOT = np.array([8, 18, 32], np.float32), np.array([14, 30, 50], np.float32)
LAND = (58, 54, 48)
COAST = (92, 86, 76)
EMPIRE = (24, 128, 70)
VASSAL_A = 0.45
NEW = (130, 255, 150)
LOSS = (255, 45, 45)
GOLD = (255, 214, 10)


def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def ease(p):
    p = clamp(p)
    return p * p * (3 - 2 * p)


# ------------------------------------------------------------------ geo data
def _rings(path, bbox=(-20, 5, 72, 62), min_pts=4):
    d = json.load(open(path))
    out = []
    for f in d["features"]:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for p in polys:
            ring = np.array(p[0], np.float32)
            if len(ring) < min_pts:
                continue
            if ring[:, 0].max() < bbox[0] or ring[:, 0].min() > bbox[2] or ring[:, 1].max() < bbox[1] or ring[:, 1].min() > bbox[3]:
                continue
            out.append(ring)
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


# ------------------------------------------------------------------ camera
def cam(t):
    k = M.CAM
    if t <= k[0][0]:
        return k[0][1:]
    for a, b in zip(k, k[1:]):
        if a[0] <= t <= b[0]:
            p = ease((t - a[0]) / max(1e-6, b[0] - a[0]))
            # interpolate scale logarithmically for smooth zooms
            s = math.exp(math.log(a[3]) + (math.log(b[3]) - math.log(a[3])) * p)
            return (a[1] + (b[1] - a[1]) * p, a[2] + (b[2] - a[2]) * p, s)
    return k[-1][1:]


class View:
    def __init__(self, t):
        self.lon, self.lat, self.s = cam(t)

    def xy(self, lon, lat):
        return ((lon - self.lon) * KX * self.s + W / 2, -(lat - self.lat) * self.s + CY)

    def arr(self, ring):
        x = (ring[:, 0] - self.lon) * KX * self.s + W / 2
        y = -(ring[:, 1] - self.lat) * self.s + CY
        return x, y

    def visible(self, x, y):
        return not (x.max() < -50 or x.min() > W + 50 or y.max() < -50 or y.min() > H + 50)


def draw_rings(d, view, rings, fill):
    for r in rings:
        x, y = view.arr(r)
        if not view.visible(x, y):
            continue
        pts = list(zip(x.tolist(), y.tolist()))
        if len(pts) > 2:
            d.polygon(pts, fill=fill)


@lru_cache(1)
def regions():
    d = json.load(open(os.path.join(GEO, "regions.json")))
    reg = {k: [np.array(r, np.float32) for r in v] for k, v in d["regions"].items()}
    sev = {k: [np.array(r, np.float32) for r in v] for k, v in d["sevr"].items()}
    return reg, sev


def draw_region(d, view, name, fill):
    draw_rings(d, view, regions()[0][name], fill)


def region_lines(d, view, name, fill, width=2, progress=1.0):
    for r in regions()[0][name]:
        x, y = view.arr(r)
        if not view.visible(x, y):
            continue
        n = len(x)
        k = max(2, int(n * progress))
        pts = list(zip(x[:k].tolist(), y[:k].tolist()))
        if progress >= 1.0:
            pts.append(pts[0])
        d.line(pts, fill=fill, width=width, joint="curve")


# ------------------------------------------------------------------ territory state
def eff_time(op):
    return op[0] + (1.0 if op[1] == "sub" else 0.0)


def masks(view, T):
    main = Image.new("L", (W, H), 0)
    vas = Image.new("L", (W, H), 0)
    dm, dv = ImageDraw.Draw(main), ImageDraw.Draw(vas)
    for op in M.OPS:
        if eff_time(op) > T:
            continue
        kind, reg = op[1], op[2]
        if kind == "add":
            draw_region(dm, view, reg, 255)
            draw_region(dv, view, reg, 0)
        elif kind == "addv":
            draw_region(dv, view, reg, 255)
        elif kind == "sub":
            draw_region(dm, view, reg, 0)
            draw_region(dv, view, reg, 0)
    return main, vas


@lru_cache(1)
def sea_bg():
    g = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
    a = SEA_TOP * (1 - g) + SEA_BOT * g
    a = np.repeat(a, W, axis=1)
    return Image.fromarray(a.astype(np.uint8))


@lru_cache(1)
def hatch():
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)
    for k in range(-H, W, 26):
        d.line([(k, 0), (k + H, H)], fill=255, width=9)
    return im


def solid(color):
    return Image.new("RGB", (W, H), color)


def region_mask(view, name, landm):
    m = Image.new("L", (W, H), 0)
    draw_region(ImageDraw.Draw(m), view, name, 255)
    return ImageChops.multiply(m, landm.point(lambda v: 255 if v > 40 else v * 6))


def render(t, hook_state=None):
    """Return RGB map frame for time t."""
    view = View(t)
    img = sea_bg().copy()
    landm = Image.new("L", (W, H), 0)
    dl = ImageDraw.Draw(landm)
    draw_rings(dl, view, land(), 255)
    draw_rings(dl, view, lakes(), 0)
    landm = landm.filter(ImageFilter.GaussianBlur(0.7))
    # land + coast line
    img.paste(solid(LAND), (0, 0), landm)
    coast = ImageChops.subtract(landm, landm.filter(ImageFilter.MinFilter(3)))
    img.paste(solid(COAST), (0, 0), coast)

    # ---------------- territory
    if hook_state == "max":
        main, vas = masks(view, 122.0)
    elif hook_state == "turkey":
        main = Image.new("L", (W, H), 0)
        draw_rings(ImageDraw.Draw(main), view, turkey(), 255)
        vas = Image.new("L", (W, H), 0)
    elif hook_state == "none":
        main = Image.new("L", (W, H), 0)
        vas = Image.new("L", (W, H), 0)
    else:
        main, vas = masks(view, t)
    end_fade = 0.0
    if hook_state is None and t >= 198.2:
        end_fade = ease((t - 199.6) / 1.2)
    main = ImageChops.multiply(main, landm)
    vas = ImageChops.multiply(vas, landm)
    emp = EMPIRE
    if end_fade > 0:
        emp = tuple(int(c * (1 - end_fade) + l * end_fade) for c, l in zip(EMPIRE, LAND))
    img.paste(solid(emp), (0, 0), vas.point(lambda v: int(v * VASSAL_A)))
    img.paste(solid(emp), (0, 0), main)
    # border
    border = ImageChops.subtract(main.filter(ImageFilter.MaxFilter(5)), main)
    border = ImageChops.multiply(border, landm)
    img.paste(solid((170, 255, 190) if end_fade == 0 else (120, 120, 120)), (0, 0), border.point(lambda v: int(v * (1 - end_fade) * 0.9)))

    # province borders inside the empire (real administrative lines)
    if hook_state in (None, "max") and end_fade < 1:
        T = 122.0 if hook_state == "max" else t
        owned = []
        for op in M.OPS:
            if eff_time(op) > T or op[1] == "flash":
                continue
            if op[1] in ("add", "addv"):
                owned = [r for r in owned if r != op[2]] + [op[2]]
        lay = Image.new("L", (W, H), 0)
        dlay = ImageDraw.Draw(lay)
        for reg in owned:
            region_lines(dlay, view, reg, 255, width=1)
        lay = ImageChops.multiply(lay, ImageChops.lighter(main, vas))
        img.paste(solid((10, 60, 30)), (0, 0), lay.point(lambda v: int(v * 0.55 * (1 - end_fade))))

    if hook_state is None:
        # outlines of the region being taken / lost are drawn like a pen stroke
        line_lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dline = ImageDraw.Draw(line_lay)
        for op in M.OPS:
            kind, reg = op[1], op[2]
            dt = t - op[0]
            dur = 1.7 if kind == "sub" else 1.6
            if 0 <= dt < dur + 0.4:
                prog = min(1.0, dt / 0.8)
                a = 1.0 if dt < dur else 1 - (dt - dur) / 0.4
                col = (255, 70, 70) if kind == "sub" else (190, 255, 200)
                region_lines(dline, view, reg, col + (int(255 * a),), width=4, progress=prog)
        img.paste(line_lay.convert("RGB"), (0, 0), line_lay.split()[3])
        # new conquests flash green; losses pulse red then vanish
        for op in M.OPS:
            kind, reg = op[1], op[2]
            if kind in ("add", "addv", "flash"):
                dt = t - op[0]
                if 0 <= dt < 1.6:
                    a = (1 - dt / 1.6) ** 1.2 * 0.95
                    rm = region_mask(view, reg, landm)
                    if kind != "flash":
                        rm = ImageChops.multiply(rm, ImageChops.lighter(main, vas))
                    img.paste(solid(NEW), (0, 0), rm.point(lambda v: int(v * a)))
            elif kind == "sub":
                dt = t - op[0]
                if 0 <= dt < 1.7:
                    if dt < 1.0:
                        a = 0.55 + 0.4 * abs(math.sin(dt * math.pi * 3))
                        pm, pv = masks(view, op[0] + 0.5)
                    else:
                        a = 0.9 * (1 - (dt - 1.0) / 0.7)
                        pm, pv = masks(view, op[0] + 0.99)
                    prev = ImageChops.lighter(pm, pv)
                    rm = ImageChops.multiply(region_mask(view, reg, landm), prev)
                    img.paste(solid(LOSS), (0, 0), rm.point(lambda v: int(v * a)))
        # Sevr partition
        if 193.3 <= t < 199.5:
            a = min(1, (t - 193.3) / 0.6, (199.5 - t) / 0.5)
            for name, col, p, _ in M.SEVR:
                m = Image.new("L", (W, H), 0)
                draw_rings(ImageDraw.Draw(m), view, regions()[1][name], 255)
                m = ImageChops.multiply(ImageChops.multiply(m, landm), hatch())
                img.paste(solid(col), (0, 0), m.point(lambda v: int(v * 0.85 * a)))
        # 1923 Turkey
        if t >= 207.6:
            a = ease((t - 207.6) / 1.6)
            m = Image.new("L", (W, H), 0)
            draw_rings(ImageDraw.Draw(m), view, turkey(), 255)
            m = ImageChops.multiply(m, landm)
            img.paste(solid((200, 20, 30)), (0, 0), m.point(lambda v: int(v * 0.85 * a)))
            edge = ImageChops.subtract(m.filter(ImageFilter.MaxFilter(5)), m)
            img.paste(solid((255, 255, 255)), (0, 0), edge.point(lambda v: int(v * a)))
            glow = m.filter(ImageFilter.GaussianBlur(18))
            img = ImageChops.screen(img, Image.merge("RGB", [glow.point(lambda v: int(v * 0.35 * a))] * 3))
        # max-extent gold glow at 1683
        if 119.8 <= t < 124.4:
            a = min(1, (t - 119.8) / 0.5, (124.4 - t) / 0.4)
            m = ImageChops.lighter(main, vas)
            e = ImageChops.subtract(m.filter(ImageFilter.MaxFilter(7)), m)
            img.paste(solid(GOLD), (0, 0), e.point(lambda v: int(v * a)))
        # final comparison: 1683 outline over Turkey
        if t >= 211.0:
            a = ease((t - 211.0) / 0.8)
            m, v2 = masks(view, 122.0)
            m = ImageChops.multiply(ImageChops.lighter(m, v2), landm)
            e = ImageChops.subtract(m.filter(ImageFilter.MaxFilter(5)), m)
            img.paste(solid(GOLD), (0, 0), e.point(lambda v: int(v * a)))
    elif hook_state == "turkey":
        e = ImageChops.subtract(main.filter(ImageFilter.MaxFilter(5)), main)
        img.paste(solid((255, 255, 255)), (0, 0), e)
    return img, view
