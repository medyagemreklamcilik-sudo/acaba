"""Timeline for "Vahdettin hain miydi?" (narration seconds)."""

DURATION = 88.92
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["vahdettin", "vahdettin2", "ayrilis", "ayrilis2", "malaya", "malaya2", "mektup", "fetva", "sevr", "isgal",
                                  "sanremo", "bandirma", "mezar", "mk"]}
FACES = {"vahdettin": (0.5, 0.3), "vahdettin2": (0.5, 0.25), "mk": (0.5, 0.2)}

SCENES = [
    dict(t=0.00, img="vahdettin", zoom=(1.25, 1.08), focus=(0.5, 0.3)),
    dict(t=2.92, img="malaya", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="flash"),
    dict(t=5.56, mode="plate", bg="vahdettin", tr="dip"),
    dict(t=10.30, img="vahdettin2", zoom=(1.0, 1.18), focus=(0.5, 0.25), tr="pushup"),
    dict(t=13.90, img="isgal", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=18.38, img="mk", zoom=(1.0, 1.2), focus=(0.5, 0.2), tr="iris"),
    dict(t=22.32, img="bandirma", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushright"),
    dict(t=29.26, img="fetva", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.35), tr="glitch"),
    dict(t=34.84, img="mk", grade="dark", zoom=(1.15, 1.35), focus=(0.5, 0.2), tr="dip"),
    dict(t=38.12, img="sevr", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=41.88, mode="plate", bg="isgal", tr="dip"),
    dict(t=50.24, img="vahdettin2", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.25), tr="dip"),
    dict(t=52.70, img="mektup", zoom=(1.0, 1.25), focus=(0.5, 0.4), tr="pushup"),
    dict(t=59.20, img="ayrilis", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushleft"),
    dict(t=61.38, img="malaya2", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="dip"),
    dict(t=64.64, img="sanremo", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    dict(t=68.02, img="mezar", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="dip"),
    dict(t=73.02, img="vahdettin", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="dip"),
    dict(t=77.46, img="malaya", zoom=(1.2, 1.45), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=83.54, mode="plate", bg="vahdettin", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=5.4, lines=["SON PADİŞAH", "İNGİLİZ GEMİSİYLE GİTTİ"], y=330, size=100),
    dict(type="kinetic", t0=5.6, t1=10.1, text="HAİN Mİ?\nÇARESİZ Mİ?", y=420, size=160, style="red"),
    dict(type="label", t0=10.4, t1=13.8, title="Sultan Vahdettin", sub="son Osmanlı padişahı, 1918-1922", y=420),
    dict(type="stamp", t0=15.14, t1=16.4, text="MONDROS", y=900, size=140, color=RED, rot=-6, fill=True),
    dict(type="stamp", t0=17.00, t1=18.3, text="İŞGAL", y=900, size=160, color=RED, rot=-6, fill=True),
    dict(type="tagpair", t0=18.4, t1=19.6, tags=[("SAVUNANLAR", 760, 18.54)]),
    dict(type="label", t0=22.4, t1=25.9, title="Samsun'a giden yol", sub="9. Ordu Müfettişi, Mayıs 1919", y=420),
    dict(type="kinetic", t0=26.0, t1=29.1, text="\"PAŞA, DEVLETİ\nKURTARABİLİRSİN\"", y=620, size=110),
    dict(type="tagpair", t0=29.3, t1=30.6, tags=[("SUÇLAYANLAR", 760, 29.46)]),
    dict(type="stamp", t0=32.48, t1=34.7, text="FETVA", y=900, size=160, color=RED, rot=-6, fill=True),
    dict(type="stamp", t0=35.68, t1=38.0, text="İDAM KARARI ONAYI", y=900, size=100, color=RED, rot=-6, fill=True),
    dict(type="label", t0=38.2, t1=41.7, title="Sevr Antlaşması", sub="10 Ağustos 1920", y=420),
    dict(type="kinetic", t0=41.88, t1=49.9, text="SEN OLSAN\nNE YAPARDIN?", y=420, size=130, style="red"),
    dict(type="tagpair", t0=45.9, t1=49.9, tags=[("UZLAŞIRDIM", 760, 46.46), ("GÖZE ALIRDIM", 900, 48.54)]),
    dict(type="stamp", t0=51.60, t1=52.6, text="SALTANAT KALDIRILDI", y=900, size=96, color=YELLOW, rot=-5, fill=True),
    dict(type="label", t0=52.9, t1=59.0, title="General Harington'a mektup", sub="16 Kasım 1922", y=420),
    dict(type="label", t0=59.3, t1=61.2, title="17 Kasım 1922", sub="saraydan son çıkış", y=420),
    dict(type="label", t0=61.5, t1=64.5, title="HMS Malaya", sub="İngiliz savaş gemisi", y=420),
    dict(type="label", t0=64.7, t1=67.9, title="San Remo, İtalya", sub="1926'da öldüğü şehir", y=420),
    dict(type="label", t0=68.1, t1=72.9, title="Şam'daki mezarı", sub="Süleymaniye Külliyesi", y=420),
    dict(type="kinetic", t0=79.44, t1=83.4, text="BİR GEMİ", y=380, size=180, style="black"),
    dict(type="kinetic", t0=83.54, t1=DURATION + 1, text="HAİN Mİ?\nÇARESİZ Mİ?", y=420, size=150),
    dict(type="tagpair", t0=84.0, t1=DURATION + 1, tags=[("HAİN", 760, 85.02), ("ÇARESİZ", 900, 86.56)]),
    dict(type="cta", t0=87.8, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(15.1, 16.4), (35.6, 37.2), (61.3, 62.5), (0.0, 5.4), (5.56, 10.1), (26.0, 29.1), (32.4, 33.4), (41.88, 49.9), (51.5, 52.6), (79.4, 80.4), (83.54, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 5.6, 15.14, 17.00, 32.48, 35.68, 41.88, 51.60, 62.20, 79.44]
SHAKE = [15.14, 32.48, 35.68]
FLASH = [(2.92, 0.08)]

MUSIC = [(0, 10.30, 3), (10.30, 29.26, 2), (29.26, 41.88, 3), (41.88, 50.24, 1), (50.24, 64.64, 2), (64.64, 77.46, 1), (77.46, 83.54, 3),
         (83.54, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=15.14, gain=0.3), dict(name="hit", t=32.48, gain=0.35),
       dict(name="hit", t=35.68, gain=0.3), dict(name="pop", t=87.8, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="malaya", grade="dark", focus=(0.5, 0.5), zoom=1.05, lines=["VAHDETTİN", "HAİN MİYDİ?"], y=250, size=124, style="red",
             portraits=[("vahdettin", 540, 820, 420)], stamp="İNGİLİZ GEMİSİYLE GİTTİ", stamp_y=1270, stamp_size=86, stamp_color=YELLOW, stamp_rot=-5)
