"""Timeline for "Atatürk 20 yıl daha yaşasaydı ne olurdu?" (narration seconds)."""

DURATION = 85.16
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["portre", "portre2", "inonu", "savas", "yikim", "adana", "montro", "balkan", "serbest", "sandik"]}
FACES = {"portre": (0.5, 0.3), "portre2": (0.5, 0.2), "inonu": (0.5, 0.2)}

SCENES = [
    dict(t=0.00, img="portre", zoom=(1.25, 1.08), focus=(0.5, 0.3)),
    dict(t=2.70, img="savas", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="glitch"),
    dict(t=5.38, img="sandik", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=8.82, img="portre2", zoom=(1.0, 1.2), focus=(0.5, 0.25), tr="dip"),
    dict(t=16.92, img="yikim", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=21.06, img="inonu", zoom=(1.0, 1.18), focus=(0.5, 0.2), tr="pushleft"),
    dict(t=23.26, img="adana", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushright"),
    dict(t=25.60, img="portre", grade="dark", zoom=(1.15, 1.35), focus=(0.5, 0.3), tr="dip"),
    dict(t=28.80, mode="plate", bg="portre", tr="dip"),
    dict(t=34.08, img="montro", zoom=(1.0, 1.25), focus=(0.4, 0.35), tr="pushup"),
    dict(t=36.86, img="balkan", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushleft"),
    dict(t=40.74, mode="plate", bg="savas", tr="dip"),
    dict(t=46.06, img="serbest", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="iris"),
    dict(t=55.26, img="sandik", zoom=(1.1, 1.35), focus=(0.5, 0.5), tr="pushup"),
    dict(t=60.06, mode="plate", bg="sandik", tr="dip"),
    dict(t=68.50, img="portre2", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.2), tr="dip"),
    dict(t=72.96, img="portre", grade="dark", zoom=(1.2, 1.4), focus=(0.5, 0.3), tr="dip"),
    dict(t=78.16, mode="plate", bg="portre", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=5.2, lines=["ATATÜRK 20 YIL", "DAHA YAŞASAYDI?"], y=330, size=110),
    dict(type="stamp", t0=3.42, t1=5.2, text="2. DÜNYA SAVAŞI", y=900, size=104, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=5.5, t1=8.7, text="ÇOK PARTİ\nDAHA ERKEN?", y=420, size=130, style="black"),
    dict(type="counter", t0=9.9, t1=11.5, **{"from": 0, "to": 57}, fmt="{} YAŞINDA", dur=0.5, y=440, size=140),
    dict(type="counter", t0=13.56, t1=16.8, **{"from": 1938, "to": 1958}, fmt="{}", dur=0.8, y=440, size=180),
    dict(type="label", t0=17.0, t1=20.9, title="1939", sub="İkinci Dünya Savaşı başlıyor", y=420),
    dict(type="label", t0=21.2, t1=23.1, title="İsmet İnönü", sub="Milli Şef", y=420),
    dict(type="label", t0=23.4, t1=25.4, title="Adana Görüşmesi, 1943", sub="İnönü ve Churchill", y=420),
    dict(type="stamp", t0=24.38, t1=25.4, text="TARAFSIZ", y=950, size=140, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=31.14, t1=33.9, text="\"YURTTA SULH,\nCİHANDA SULH\"", y=620, size=120),
    dict(type="label", t0=34.2, t1=36.7, title="Montrö, 1936", sub="Boğazların kontrolü", y=420),
    dict(type="label", t0=37.0, t1=40.5, title="Balkan Antantı, 1934", sub="barış ittifakı", y=420),
    dict(type="kinetic", t0=40.74, t1=45.9, text="SEN OLSAN\nSAVAŞA GİRER MİYDİN?", y=420, size=110, style="red"),
    dict(type="kinetic", t0=46.1, t1=47.3, text="DEMOKRASİ?", y=420, size=150, style="black"),
    dict(type="label", t0=47.5, t1=52.9, title="Serbest Cumhuriyet Fırkası", sub="1930", y=420),
    dict(type="stamp", t0=54.60, t1=55.2, text="3 AYDA KAPANDI", y=900, size=110, color=RED, rot=-6, fill=True),
    dict(type="counter", t0=57.76, t1=59.9, **{"from": 1930, "to": 1946}, fmt="{}", dur=0.6, y=440, size=180),
    dict(type="tagpair", t0=60.2, t1=68.3, tags=[("KENDİSİ YÖNETİRDİ", 760, 62.56), ("TEK PARTİ UZARDI", 900, 65.0)]),
    dict(type="kinetic", t0=74.0, t1=78.0, text="SORU\nHÂLÂ DURUYOR", y=620, size=140, style="red"),
    dict(type="kinetic", t0=78.16, t1=DURATION + 1, text="DEMOKRASİ\nERKEN Mİ, GEÇ Mİ?", y=420, size=120),
    dict(type="tagpair", t0=80.5, t1=DURATION + 1, tags=[("DAHA ERKEN", 760, 81.18), ("DAHA GEÇ", 900, 83.22)]),
    dict(type="cta", t0=84.2, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 5.2), (5.4, 8.7), (31.1, 33.9), (40.74, 45.9), (60.1, 68.3), (74.0, 78.0), (78.16, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 3.42, 13.56, 24.38, 31.14, 40.74, 54.60, 57.76, 74.0]
SHAKE = [3.42, 54.60]
FLASH = [(2.70, 0.08)]

MUSIC = [(0, 8.82, 3), (8.82, 25.60, 2), (25.60, 40.74, 2), (40.74, 46.06, 1), (46.06, 68.50, 2), (68.50, 78.16, 3), (78.16, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=3.42, gain=0.35), dict(name="hit", t=54.60, gain=0.3),
       dict(name="pop", t=84.2, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(imgs=[dict(img="portre", focus=(0.5, 0.3)), dict(img="savas", focus=(0.5, 0.5))], lines=["20 YIL DAHA", "YAŞASAYDI?"], y=250,
             size=124, style="white", stamp="1938 → 1958", stamp_y=1260, stamp_size=110, stamp_color=RED, stamp_rot=-6,
             bottom="savaş mı, barış mı?", bottom_y=1390)
