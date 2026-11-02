"""Timeline for "Yavuz 8 yılda imparatorluğu nasıl ikiye katladı?" (narration seconds)."""

DURATION = 99.9
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "yavuz", "yavuz_eu", "yavuz_tahtta", "bayezid", "ismail", "caldiran", "tebriz", "mercidabik", "kahire",
    "babzuwayla", "kabe", "yeniceri", "top", "sina", "kanuni", "turbe", "hilafet"]}

FACES = {"yavuz": (0.5, 0.3), "yavuz_eu": (0.5, 0.4), "yavuz_tahtta": (0.5, 0.3), "bayezid": (0.45, 0.45),
         "ismail": (0.55, 0.4), "kanuni": (0.5, 0.35), "yeniceri": (0.5, 0.2)}

# (anahtar, etiket, lon, lat, ölçek)
JOURNEY = [
    ("istanbul", "İSTANBUL", 28.97, 41.01, 42),
    ("caldiran", "ÇALDIRAN", 43.9, 39.15, 62),
    ("tebriz", "TEBRİZ", 46.29, 38.08, 62),
    ("mercidabik", "MERCİDABIK", 37.27, 36.54, 58),
    ("sina", "SİNA ÇÖLÜ", 33.8, 30.4, 48),
    ("kahire", "KAHİRE · RİDANİYE", 31.25, 30.05, 58),
    ("mekke", "MEKKE · MEDİNE", 39.8, 22.6, 40),
]


def J(t, stop, year, role, **kw):
    return dict(t=t, mode="journey", stop=stop, year=year, portrait="yavuz", rank="YAVUZ", role=role, **kw)


SCENES = [
    # kanca
    dict(t=0.00, img="yavuz_eu", grade="dark", zoom=(1.3, 1.05), focus=(0.5, 0.4)),
    dict(t=2.18, img="yavuz", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="glitch"),
    J(3.40, 0, "1512", "8 yıl"),
    # Yavuz, Bayezid
    dict(t=7.78, img="yavuz", zoom=(1.05, 1.2), focus=(0.5, 0.3), tr="flash"),
    dict(t=10.30, img="yeniceri", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="pushleft"),
    dict(t=12.66, img="bayezid", zoom=(1.0, 1.15), focus=(0.45, 0.45), tr="pushup"),
    dict(t=15.54, img="bayezid", grade="dark", zoom=(1.2, 1.4), focus=(0.45, 0.45), tr="dip"),
    dict(t=22.48, mode="plate", bg="yavuz_tahtta", tr="bars"),
    # Çaldıran
    J(25.92, 1, "1514", "Çaldıran"),
    dict(t=29.80, img="ismail", zoom=(1.0, 1.15), focus=(0.55, 0.4), tr="pushleft"),
    dict(t=33.22, img="caldiran", zoom=(1.0, 1.25), focus=(0.5, 0.45), tr="glitch"),
    J(36.32, 2, "1514", "Tebriz'e giriş"),
    # Mercidabık
    J(39.56, 3, "1516", "Mercidabık"),
    dict(t=42.36, img="mercidabik", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    dict(t=45.10, img="mercidabik", grade="dark", zoom=(1.3, 1.5), focus=(0.4, 0.4), tr="dip"),
    dict(t=48.78, img="tebriz", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    # Sina, Kahire
    dict(t=51.52, img="sina", zoom=(1.0, 1.2), focus=(0.5, 0.6), tr="flash"),
    J(54.04, 4, "1517", "Sina Çölü"),
    J(57.04, 5, "1517", "Ridaniye"),
    dict(t=60.00, img="kahire", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=63.50, img="babzuwayla", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="bars"),
    # Haremeyn
    J(66.20, 6, "1517", "Haremeyn"),
    dict(t=69.70, img="kabe", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    # halifelik
    dict(t=75.02, img="hilafet", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="glitch"),
    dict(t=78.82, mode="plate", bg="hilafet", tr="dip"),
    # son
    dict(t=84.66, img="turbe", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=88.66, img="kanuni", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="flash"),
    dict(t=93.78, mode="plate", bg="yavuz_eu", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=2.1, lines=["BABASINI", "TAHTTAN İNDİRDİ"], y=330, size=118),
    dict(type="stamp", t0=2.7, t1=3.35, text="KARDEŞLERİNİ ÖLDÜRTTÜ", y=820, size=96, color=RED, rot=-6, fill=True),
    dict(type="counter", t0=4.4, t1=7.7, **{"from": 0, "to": 8}, fmt="{} YIL", dur=0.6, y=900, size=170),
    dict(type="stamp", t0=6.26, t1=7.7, text="İKİYE KATLADI", y=1090, size=100, color=YELLOW, rot=-5, fill=True),
    # --- Yavuz, Bayezid
    dict(type="label", t0=8.2, t1=10.2, title="Yavuz Sultan Selim", sub="1512 – 1520", y=420),
    dict(type="kinetic", t0=11.18, t1=12.6, text="YENİÇERİ DESTEĞİ", y=380, size=104, style="black"),
    dict(type="label", t0=12.8, t1=15.4, title="İkinci Bayezid", sub="babası", y=420),
    dict(type="stamp", t0=14.2, t1=15.4, text="TAHTTAN İNDİRİLDİ", y=900, size=100, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=18.44, t1=20.1, text="ZEHİR Mİ?", y=380, size=130, style="red"),
    dict(type="stamp", t0=20.6, t1=22.3, text="KANITLANAMADI", y=900, size=110, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=22.48, t1=25.8, text="8 YILA NASIL\nSIĞDIRDI?", y=760, size=130),
    # --- Çaldıran
    dict(type="label", t0=30.0, t1=33.1, title="Şah İsmail", sub="Safevi hükümdarı", y=420),
    dict(type="kinetic", t0=33.3, t1=36.2, text="OSMANLI TOPLARI", y=380, size=110, style="red"),
    # --- Mercidabık
    dict(type="label", t0=42.5, t1=45.0, title="Mercidabık", sub="Selimname minyatürü", y=420),
    dict(type="label", t0=45.3, t1=48.6, title="Kansu Gavri", sub="Memlük sultanı", y=420),
    dict(type="stamp", t0=47.3, t1=48.6, text="SAVAŞTA ÖLDÜ", y=900, size=120, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=48.78, t1=51.4, text="SURİYE + FİLİSTİN", y=380, size=100, style="black"),
    # --- Sina, Kahire
    dict(type="kinetic", t0=51.6, t1=54.0, text="KİMSE\nBEKLEMİYORDU", y=380, size=110, style="red"),
    dict(type="label", t0=60.2, t1=63.4, title="Kahire", sub="16. yüzyıl haritası", y=420),
    dict(type="label", t0=63.6, t1=66.1, title="Tomanbay", sub="son Memlük sultanı", y=420),
    dict(type="stamp", t0=64.9, t1=66.1, text="ASILDI", y=900, size=150, color=RED, rot=-7, fill=True),
    # --- Haremeyn
    dict(type="title", t0=70.0, t1=74.9, lines=["HÂDİMÜ'L-HAREMEYN"], y=330, size=96),
    dict(type="label", t0=72.6, t1=74.9, title="İki kutsal şehrin", sub="hizmetkârı", y=560),
    # --- halifelik
    dict(type="kinetic", t0=75.4, t1=78.7, text="HALİFELİK?", y=380, size=140, style="red"),
    dict(type="kinetic", t0=78.82, t1=84.5, text="RESMİ DEVİR\nTÖRENİ", y=500, size=120),
    dict(type="stamp", t0=82.0, t1=84.5, text="SONRADAN ANLATILDI", y=900, size=96, color=YELLOW, rot=-5, fill=True),
    # --- son
    dict(type="label", t0=85.0, t1=88.5, title="Yavuz Sultan Selim Türbesi", sub="1520 · İstanbul", y=420),
    dict(type="label", t0=89.0, t1=93.6, title="Kanuni Sultan Süleyman", sub="oğlu", y=420),
    dict(type="kinetic", t0=93.78, t1=DURATION + 1, text="DÂHİ Mİ,\nACIMASIZ MI?", y=330, size=120),
    dict(type="tagpair", t0=94.4, t1=DURATION + 1, tags=[("DÂHİ", 640, 94.9), ("ACIMASIZ FATİH", 780, 96.5)]),
    dict(type="cta", t0=98.3, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.35), (22.48, 25.8), (93.78, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 2.7, 6.26, 14.2, 25.92, 35.26, 47.82, 57.04, 65.2, 82.0]
SHAKE = [2.7, 14.2, 35.26, 47.82, 65.2]
FLASH = [(7.78, 0.12), (51.52, 0.12)]

MUSIC = [(0, 7.78, 3), (7.78, 22.48, 2), (22.48, 39.56, 3), (39.56, 51.52, 3), (51.52, 66.2, 3), (66.2, 84.66, 2),
         (84.66, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=2.7, gain=0.35), dict(name="hit", t=14.2, gain=0.3),
       dict(name="riser", t=25.92, gain=0.2, pre=True), dict(name="hit", t=35.26, gain=0.3), dict(name="hit", t=47.82, gain=0.3),
       dict(name="hit", t=65.2, gain=0.35), dict(name="pop", t=98.3, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="yavuz_eu", focus=(0.5, 0.42), zoom=1.08, lines=["8 YILDA", "2 KATINA ÇIKARDI"], y=250, size=116,
             style="yellow", stamp="BABASINI İNDİRDİ", stamp_y=1230, stamp_size=100, stamp_color=RED, stamp_rot=-6,
             bottom="Çaldıran'dan Kahire'ye", bottom_y=1360)
