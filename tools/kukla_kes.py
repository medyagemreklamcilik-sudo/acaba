"""Karakter parça sayfalarından (beyaz zemin) parçaları keser: python3 tools/kukla_kes.py
Her bölgede beyaz zemin kenardan flood-fill ile silinir, en büyük bağlı bileşen tutulur (etiket yazıları atılır)."""
import json, os
from collections import deque
import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine", "assets", "kukla")
SRC = os.path.join(ROOT, "src")

STD = {"head": (20, 790, 420, 1082), "torso": (415, 790, 745, 1095), "larm": (30, 1125, 200, 1348),
       "rarm": (195, 1125, 412, 1350), "lleg": (400, 1120, 562, 1366), "rleg": (595, 1120, 768, 1366)}
SHEETS = {
    "sehzade": ("sehzade.jpg", STD),
    "vezir": ("vezir.jpg", dict(STD, head=(20, 760, 425, 1082), torso=(425, 760, 745, 1095))),
    "padisah": ("padisah.jpg", dict(STD, head=(20, 765, 400, 1082), torso=(415, 770, 745, 1095))),
    "anlatici": ("anlatici_parca.jpg", {"head": (5, 25, 370, 322), "head_side": (15, 405, 365, 728),
                                         "larm": (352, 145, 460, 500), "torso": (452, 95, 668, 522), "rarm": (660, 145, 762, 500),
                                         "lleg": (366, 520, 560, 985), "rleg": (563, 520, 758, 985),
                                         "lhand_open": (130, 1000, 345, 1102), "rhand_open": (432, 1000, 648, 1102),
                                         "lhand_point": (130, 1132, 348, 1216), "rhand_point": (430, 1132, 648, 1216),
                                         "lhand_fist": (130, 1248, 316, 1333), "rhand_fist": (460, 1248, 648, 1333)}),
}


def components(mask):
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    sizes = [0]
    k = 0
    ys, xs = np.nonzero(mask)
    for y0, x0 in zip(ys, xs):
        if lab[y0, x0]:
            continue
        k += 1
        q = deque([(y0, x0)])
        lab[y0, x0] = k
        n = 0
        while q:
            y, x = q.popleft()
            n += 1
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                    lab[ny, nx] = k
                    q.append((ny, nx))
        sizes.append(n)
    return lab, sizes


def cut(im, box):
    c = np.asarray(im.crop(box)).astype(np.int16)
    h, w, _ = c.shape
    wh = c.min(axis=2) > 222
    bg = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if wh[y, x]:
                bg[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if wh[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not bg[ny, nx] and wh[ny, nx]:
                bg[ny, nx] = True
                q.append((ny, nx))
    fg = ~bg
    lab, sizes = components(fg)
    big = int(np.argmax(sizes))
    keep = lab == big
    alpha = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7))
    out = Image.fromarray(c.astype(np.uint8)).convert("RGBA")
    out.putalpha(alpha)
    return out.crop(out.getbbox())


if __name__ == "__main__":
    for name, (f, boxes) in SHEETS.items():
        im = Image.open(os.path.join(SRC, f)).convert("RGB")
        d = os.path.join(ROOT, name)
        os.makedirs(d, exist_ok=True)
        for part, box in boxes.items():
            p = cut(im, box)
            p.save(os.path.join(d, part + ".png"))
            print(name, part, p.size)
