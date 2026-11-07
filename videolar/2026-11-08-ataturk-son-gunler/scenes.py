"""Timeline for "Atatürk'ün son günleri" (narration seconds)."""

DURATION = 80.93
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["son", "portre", "yuruyus", "dinlenme", "savarona", "savarona2", "mersin", "oda", "saat", "hatay", "cenaze", "dolmabahce"]}
FACES = {"son": (0.5, 0.3), "portre": (0.5, 0.3), "yuruyus": (0.5, 0.2), "dinlenme": (0.4, 0.4), "mersin": (0.45, 0.3)}

SCENES = [
    # kanca: net yüz ilk karede
    dict(t=0.00, img="portre", zoom=(1.25, 1.08), focus=(0.5, 0.3)),
    dict(t=3.74, img="son", grade="dark", zoom=(1.05, 1.25), focus=(0.5, 0.35), tr="dip"),
    # hastalık
    dict(t=7.06, img="yuruyus", zoom=(1.0, 1.2), focus=(0.5, 0.25), tr="pushup"),
    dict(t=13.78, mode="plate", bg="portre", tr="flash"),
    # Hatay
    dict(t=20.24, img="portre", grade="dark", zoom=(1.15, 1.35), focus=(0.5, 0.3), tr="glitch"),
    dict(t=25.82, img="mersin", zoom=(1.0, 1.2), focus=(0.45, 0.35), tr="pushleft"),
    # sen olsan
    dict(t=31.10, mode="plate", bg="son", tr="dip"),
    # Savarona
    dict(t=35.06, img="savarona", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushright"),
    dict(t=37.38, img="dinlenme", grade="dark", zoom=(1.05, 1.25), focus=(0.4, 0.45), tr="dip"),
    dict(t=39.64, img="hatay", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="pushup"),
    # koma
    dict(t=42.56, img="son", grade="dark", zoom=(1.2, 1.45), focus=(0.5, 0.35), tr="dip"),
    dict(t=47.80, img="oda", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.55), tr="dip"),
    dict(t=52.18, mode="plate", bg="oda", tr="dip"),
    dict(t=56.16, img="saat", zoom=(1.1, 1.35), focus=(0.5, 0.75), tr="dip"),
    dict(t=59.04, img="dolmabahce", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    # son
    dict(t=64.12, img="cenaze", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="dip"),
    dict(t=67.82, img="hatay", zoom=(1.15, 1.35), focus=(0.5, 0.35), tr="pushup"),
    dict(t=71.94, img="portre", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="dip"),
    dict(t=73.96, mode="plate", bg="portre", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=3.6, lines=["CANI ENGİNAR ÇEKTİ"], y=330, size=112),
    dict(type="stamp", t0=5.44, t1=7.0, text="YİYEMEDİ", y=900, size=150, color=RED, rot=-6, fill=True),
    dict(type="label", t0=7.2, t1=13.6, title="1937", sub="ilk belirtiler: burun kanaması, kaşıntı", y=420),
    dict(type="kinetic", t0=13.9, t1=17.4, text="PARİS'TEN\nBİR DOKTOR", y=420, size=130, style="black"),
    dict(type="stamp", t0=18.90, t1=20.1, text="SİROZ", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=21.12, t1=24.9, text="DİNLENMEYİ\nREDDETTİ", y=420, size=130, style="black"),
    dict(type="stamp", t0=25.04, t1=25.8, text="HATAY", y=900, size=170, color=YELLOW, rot=-5, fill=True),
    dict(type="label", t0=26.0, t1=30.9, title="Mersin, Mayıs 1938", sub="hasta haliyle birlikleri denetledi", y=420),
    dict(type="kinetic", t0=31.1, t1=34.9, text="SEN OLSAN\nNEYE HARCARDIN?", y=420, size=120, style="red"),
    dict(type="label", t0=35.2, t1=37.2, title="Savarona", sub="yaz 1938", y=420),
    dict(type="label", t0=39.8, t1=42.4, title="Hatay", sub="gazete manşeti, 1938", y=420),
    dict(type="counter", t0=42.56, t1=47.6, **{"from": 0, "to": 1}, fmt="{}. KOMA", dur=0.3, y=440, size=150),
    dict(type="stamp", t0=46.78, t1=47.6, text="UYANDI", y=900, size=140, color=YELLOW, rot=-5, fill=True),
    dict(type="counter", t0=47.80, t1=52.0, **{"from": 1, "to": 2}, fmt="{}. KOMA", dur=0.3, y=440, size=150),
    dict(type="kinetic", t0=54.70, t1=56.0, text="\"ALEYKÜMSELAM\"", y=620, size=120),
    dict(type="kinetic", t0=59.66, t1=63.9, text="09:05", y=420, size=220, style="black"),
    dict(type="label", t0=60.74, t1=63.9, title="Dolmabahçe Sarayı", sub="10 Kasım 1938", y=640),
    dict(type="kinetic", t0=67.9, t1=71.8, text="HATAY\n29 HAZİRAN 1939", y=420, size=120, style="black"),
    dict(type="kinetic", t0=71.94, t1=73.8, text="ÖMRÜ\nYETMEDİ", y=620, size=170, style="red"),
    dict(type="kinetic", t0=73.96, t1=DURATION + 1, text="DİNLENSEYDİ\nYAŞAR MIYDI?", y=420, size=130),
    dict(type="tagpair", t0=74.4, t1=DURATION + 1, tags=[("EVET, YAŞARDI", 760, 75.82), ("KİMSE DURDURAMAZDI", 900, 78.4)]),
    dict(type="cta", t0=79.9, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.6), (5.4, 7.0), (18.9, 19.9), (21.1, 22.2), (31.1, 34.9), (54.6, 56.0), (71.94, 73.8), (73.96, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 5.44, 18.90, 25.04, 31.1, 46.78, 50.52, 59.66, 71.94]
SHAKE = [5.44, 18.90]
FLASH = [(13.78, 0.08)]

MUSIC = [(0, 7.06, 2), (7.06, 20.24, 2), (20.24, 31.10, 3), (31.10, 35.06, 1), (35.06, 52.18, 2), (52.18, 64.12, 1), (64.12, 73.96, 3),
         (73.96, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=5.44, gain=0.35), dict(name="hit", t=18.90, gain=0.35),
       dict(name="riser", t=47.80, gain=0.15, pre=True), dict(name="hit", t=59.66, gain=0.3), dict(name="pop", t=79.9, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="portre", grade="dark", focus=(0.5, 0.32), zoom=1.08, lines=["CANI ENGİNAR ÇEKTİ", "YİYEMEDEN GİTTİ"], y=250,
             size=100, style="yellow", stamp="09:05", stamp_y=1240, stamp_size=150, stamp_color=RED, stamp_rot=-6,
             bottom="10 Kasım 1938", bottom_y=1400)
