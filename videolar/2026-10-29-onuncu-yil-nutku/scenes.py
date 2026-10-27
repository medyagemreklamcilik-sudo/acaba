"""Timeline for "Onuncu Yıl Nutku" (narration seconds)."""

DURATION = 103.3
CAP_Y = 1235
CX = 507

IMAGES = {
    "nutuk_yakin": "nutuk_yakin.jpg",
    "nutuk_yakin2": "nutuk_yakin2.jpg",
    "nutuk_kursu": "nutuk_kursu.jpg",
    "nutuk_genis": "nutuk_genis.jpg",
    "abide": "abide.jpg",
    "abide2": "abide2.jpg",
    "balkon": "balkon.jpg",
    "heyet": "heyet.jpg",
    "kalabalik": "kalabalik.jpg",
    "kalabalik2": "kalabalik2.jpg",
    "fabrika": "fabrika.jpg",
    "fabrika_afis": "fabrika_afis.jpg",
    "tren_acilis": "tren_acilis.jpg",
    "tren_isci": "tren_isci.jpg",
    "ray": "ray.jpg",
    "sinif": "sinif.jpg",
    "ogrenciler": "ogrenciler.jpg",
    "dtcf": "dtcf.jpg",
    "halk": "halk.jpg",
    "kutuphane": "kutuphane.jpg",
    "at_prof": "ataturkportre_4.jpg",
    "at_dark": "ataturkportre_7.jpg",
    "at_suit": "ataturkportre_1.jpg",
    "tahta": "tahta_5.jpg",
    "bayrak": "bayrak_3.jpg",
    "vekil": "kadinvekil_3.jpg",
}

FACES = {"at_prof": (0.5, 0.3), "at_dark": (0.45, 0.3), "at_suit": (0.5, 0.25)}

SCENES = [
    # giriş
    dict(t=0.00, img="nutuk_genis", zoom=(1.3, 1.05), focus=(0.5, 0.45)),
    dict(t=2.76, img="kalabalik", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    dict(t=4.46, img="abide", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="pushup"),
    dict(t=6.38, img="nutuk_kursu", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="pushleft"),
    dict(t=10.30, img="at_dark", grade="bw", zoom=(1.0, 1.15), focus=(0.45, 0.3), tr="dip"),
    # nutuk
    dict(t=14.24, img="nutuk_yakin", zoom=(1.0, 1.06), focus=(0.6, 0.4), tr="flash"),
    dict(t=19.24, img="abide2", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="pushup"),
    dict(t=24.08, img="balkon", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="pushleft"),
    dict(t=26.44, img="heyet", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="bars"),
    dict(t=29.36, img="kalabalik2", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushup"),
    dict(t=35.92, img="at_prof", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="dip"),
    dict(t=39.20, img="ray", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=44.52, img="fabrika", zoom=(1.0, 1.15), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="iris"),
    dict(t=47.06, img="fabrika_afis", mode="card", maxw=700, maxh=980, tilt=2, tr="pushup"),
    dict(t=50.12, img="tren_acilis", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=53.54, img="tren_isci", zoom=(1.0, 1.12), focus=(0.5, 0.45), tr="pushup"),
    dict(t=55.10, img="dtcf", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="bars"),
    dict(t=59.56, img="nutuk_yakin2", grade="dark", zoom=(1.0, 1.06), focus=(0.6, 0.4), tr="dip"),
    dict(t=64.32, img="tahta", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="pushup"),
    dict(t=68.30, img="sinif", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=71.78, img="ogrenciler", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushup"),
    dict(t=75.50, img="halk", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="iris"),
    dict(t=78.26, img="vekil", mode="card", maxw=860, maxh=760, tilt=-2, tr="pushleft"),
    dict(t=80.20, img="sinif", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="pushup"),
    dict(t=82.00, img="kutuphane", zoom=(1.0, 1.15), focus=(0.4, 0.5), tr="dip"),
    # kapanış
    dict(t=90.66, img="bayrak", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="flash"),
    dict(t=92.84, img="nutuk_genis", zoom=(1.0, 1.1), focus=(0.5, 0.45), tr="dip"),
    dict(t=95.52, mode="plate", bg="at_dark", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- giriş
    dict(type="title", t0=0.0, t1=2.7, lines=["29 EKİM 1933"], y=330, size=130),
    dict(type="label", t0=2.85, t1=4.4, title="Ankara Hipodromu", sub="Cumhuriyet'in 10. yılı", y=420),
    dict(type="counter", t0=4.46, t1=6.3, **{"from": 1, "to": 10}, fmt="{}. YIL", dur=0.7, y=820, size=150),
    dict(type="handwrite", t0=10.48, t1=14.1, text="hâlâ unutulmadı", y=640, size=110, dur=0.7),
    # --- nutuk
    dict(type="source", text="Onuncu Yıl Nutku'ndan bölümler · Atatürk, 29 Ekim 1933", t0=14.3, t1=24.0),
    dict(type="kinetic", t0=14.24, t1=19.1, text="\"TÜRK MİLLETİ!\"", y=380, size=120),
    dict(type="kinetic", t0=24.08, t1=26.3, text="KUTLU OLSUN!", y=380, size=130, style="red"),
    dict(type="kinetic", t0=26.44, t1=29.2, text="AZ ZAMANDA\nÇOK VE BÜYÜK İŞLER", y=380, size=96),
    dict(type="kinetic", t0=37.14, t1=39.1, text="ASLA KÂFİ\nGÖREMEYİZ", y=380, size=110, style="black"),
    dict(type="kinetic", t0=46.26, t1=50.0, text="EN MAMUR, EN MEDENİ", y=380, size=96),
    dict(type="kinetic", t0=51.04, t1=55.0, text="EN GENİŞ REFAH", y=380, size=110),
    dict(type="handwrite", t0=56.18, t1=59.45, text="muasır medeniyetin üstüne", y=420, size=84, dur=0.9),
    dict(type="penline", t0=57.2, t1=59.45, x0=180, x1=840, y=500, dur=0.4, color=(255, 214, 10), width=8),
    dict(type="kinetic", t0=65.12, t1=68.2, text="ASRIMIZIN\nSÜRAT VE HAREKETİ", y=380, size=96, style="black"),
    dict(type="kinetic", t0=71.78, t1=75.4, text="DAHA AZ ZAMANDA\nDAHA BÜYÜK İŞLER", y=380, size=96),
    dict(type="kinetic", t0=76.44, t1=78.15, text="KARAKTERİ YÜKSEK", y=380, size=104),
    dict(type="kinetic", t0=78.92, t1=80.1, text="ÇALIŞKAN", y=380, size=130),
    dict(type="kinetic", t0=80.92, t1=81.95, text="ZEKİ", y=380, size=150),
    dict(type="handwrite", t0=88.50, t1=90.6, text="müspet ilim", y=420, size=150, dur=0.6),
    dict(type="pencircle", t0=89.3, t1=90.6, cx=CX, cy=420, rx=330, ry=120, seed=6, color=(255, 214, 10)),
    # --- kapanış
    dict(type="title", t0=90.66, t1=92.8, lines=["NE MUTLU", "TÜRK'ÜM DİYENE!"], y=330, size=110),
    dict(type="counter", t0=92.84, t1=95.45, **{"from": 1, "to": 103}, fmt="{}. YIL KUTLU OLSUN", dur=0.8, y=420, size=84),
    dict(type="kinetic", t0=95.52, t1=DURATION + 1, text="SENCE\nULAŞABİLDİK Mİ?", y=380, size=110),
    dict(type="tagpair", t0=97.0, t1=DURATION + 1, tags=[("1933 · HEDEF", 760, 97.02), ("2026 · BUGÜN", 900, 98.34)]),
    dict(type="cta", t0=101.7, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.7), (90.66, 92.8), (95.52, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [14.24, 24.08, 90.66]
SHAKE = []
FLASH = [(14.24, 0.2), (90.66, 0.25)]

MUSIC = [(0, 14.24, 1), (14.24, 44.52, 2), (44.52, 75.50, 2), (75.50, 90.66, 3), (90.66, 95.52, 3), (95.52, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="impact", t=0.05, gain=0.6), dict(name="riser", t=14.24, gain=0.25, pre=True), dict(name="impact", t=14.24, gain=0.5),
       dict(name="riser", t=90.66, gain=0.3, pre=True), dict(name="impact", t=90.66, gain=0.6), dict(name="pop", t=101.7, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.25) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="nutuk_genis", focus=(0.5, 0.42), zoom=1.0, lines=["ATATÜRK'ÜN", "KENDİ SÖZLERİYLE"], y=260, size=104,
             style="red", marks=[dict(type="handwrite", text="Onuncu Yıl Nutku · 1933", x=CX, y=1360, size=88, dur=0.1),
                                 dict(type="penline", x0=170, x1=850, y=1430, dur=0.1, color=(255, 214, 10), width=8)])
