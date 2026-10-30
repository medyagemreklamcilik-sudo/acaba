"""Timeline for "Osmanlı'da kahvehaneler neden yasaklandı?" (narration seconds)."""

DURATION = 104.0
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "murad4", "murad4b", "yangin", "yangin_gece", "yangin3", "kahve_min", "kahve_min2", "kahve_min3", "kahve_gr",
    "kahve_allom", "kahve_renk", "kahve_renk2", "kahve_tablo", "tahtakale", "katip", "cezve", "eyup", "galata",
    "kahve_foto", "kahve_foto2", "ferman", "ebussuud"]}

FACES = {"murad4": (0.5, 0.25), "murad4b": (0.5, 0.25), "katip": (0.5, 0.45), "ebussuud": (0.45, 0.3)}

SCENES = [
    # kanca: 1633 yangını
    dict(t=0.00, img="yangin_gece", zoom=(1.4, 1.05), focus=(0.7, 0.5)),
    dict(t=3.48, img="yangin", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    dict(t=7.86, mode="plate", bg="yangin3", tr="glitch"),
    dict(t=10.32, img="kahve_gr", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="zoomblur"),
    # IV. Murad ferman
    dict(t=11.12, img="murad4", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushup"),
    dict(t=14.08, img="ferman", mode="card", maxw=640, maxh=1000, tilt=-2, tr="pushleft"),
    dict(t=17.34, img="eyup", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="bars"),
    dict(t=21.76, img="cezve", zoom=(1.3, 1.0), focus=(0.5, 0.5), tr="dip"),
    # 1554
    dict(t=25.24, img="tahtakale", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    dict(t=29.84, img="kahve_min", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="pushup"),
    dict(t=34.04, img="kahve_allom", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    # Ebussuud
    dict(t=36.84, img="ebussuud", zoom=(1.0, 1.15), focus=(0.45, 0.35), tr="dip"),
    dict(t=44.32, img="kahve_min2", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    # yasaklar
    dict(t=50.50, img="galata", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="glitch"),
    dict(t=56.18, mode="plate", bg="ferman", tr="dip"),
    dict(t=59.38, img="kahve_renk", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    # asıl korku
    dict(t=62.54, img="kahve_renk2", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="flash"),
    dict(t=67.00, img="kahve_tablo", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=69.78, img="kahve_min3", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="bars"),
    # devlet pes etti
    dict(t=73.84, img="kahve_foto", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    dict(t=78.64, img="kahve_gr", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=81.84, mode="plate", bg="murad4", tr="dip"),
    dict(t=86.84, img="katip", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushup"),
    dict(t=91.14, img="kahve_foto2", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    # final
    dict(t=96.66, mode="plate", bg="kahve_min", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=3.4, lines=["2 EYLÜL 1633"], y=330, size=130),
    dict(type="label", t0=3.6, t1=7.7, title="Cibali yangını", sub="Temsili gravür", y=420),
    dict(type="kinetic", t0=7.86, t1=10.2, text="SUÇLU KİM?", y=760, size=150, style="red"),
    dict(type="stamp", t0=10.32, t1=11.0, text="KAHVEHANELER", y=820, size=120, color=RED, rot=-7, fill=True),
    dict(type="label", t0=11.2, t1=14.0, title="Dördüncü Murad", sub="1623 – 1640", y=420),
    dict(type="stamp", t0=15.3, t1=17.2, text="HEPSİ KAPANSIN", y=1050, size=110, color=RED, rot=-6, fill=True),
    dict(type="counter", t0=19.1, t1=21.6, **{"from": 0, "to": 120}, fmt="{}+ KAHVEHANE", dur=0.8, y=420, size=110),
    dict(type="stamp", t0=20.82, t1=21.6, text="YIKILDI", y=820, size=150, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=22.5, t1=25.1, text="BİR FİNCAN\nKAHVEDEN KORKU?", y=380, size=104),
    # --- 1554
    dict(type="title", t0=25.24, t1=29.7, lines=["1554 · TAHTAKALE"], y=330, size=110),
    dict(type="tagpair", t0=27.28, t1=29.7, tags=[("HALEPLİ HAKEM", 1060, 27.28), ("ŞAMLI ŞEMS", 1160, 28.76)]),
    dict(type="label", t0=30.0, t1=33.9, title="İstanbul'un ilk kahvehaneleri", sub="16. yüzyıl minyatürü", y=420),
    # --- Ebussuud
    dict(type="label", t0=38.88, t1=41.0, title="Şeyhülislam Ebussuud Efendi", sub="16. yüzyıl", y=420),
    dict(type="stamp", t0=41.18, t1=42.3, text="HARAM", y=820, size=170, color=RED, rot=-7, fill=True),
    dict(type="quote", t0=42.3, t1=44.2, y=760, by="Ebussuud Efendi",
         words=[("Fâsıkların", 42.42), ("içeceği.", 43.1)]),
    dict(type="tagpair", t0=45.5, t1=50.3, tags=[("TAVLA", 380, 45.54), ("SAATLERCE SOHBET", 520, 46.76), ("KAÇAN NAMAZ", 660, 48.52)]),
    # --- yasaklar
    dict(type="title", t0=50.5, t1=56.0, lines=["1568 · YASAK"], y=330, size=130, style="red"),
    dict(type="label", t0=54.6, t1=56.0, title="İstanbul ve Galata", sub="Meyhaneyle bir tutuldu", y=520),
    dict(type="title", t0=56.18, t1=59.2, lines=["1583 · YİNE YASAK"], y=760, size=110, style="red"),
    dict(type="kinetic", t0=60.28, t1=62.4, text="KAPANDIKÇA\nYENİSİ AÇILDI", y=380, size=104),
    # --- asıl korku
    dict(type="kinetic", t0=62.54, t1=64.2, text="ASIL KORKU", y=380, size=140, style="red"),
    dict(type="tagpair", t0=66.9, t1=69.7, tags=[("PAŞALAR", 380, 67.0), ("VERGİLER", 520, 67.92), ("PADİŞAH", 660, 68.78)]),
    dict(type="label", t0=69.9, t1=73.7, title="Yeniçeriler", sub="Kahvehanede toplanıyordu", y=420),
    # --- pes etti
    dict(type="stamp", t0=74.62, t1=75.6, text="PES ETTİ", y=820, size=150, color=YELLOW, rot=-6, fill=True),
    dict(type="kinetic", t0=75.92, t1=78.5, text="KAHVE VERGİSİ\n= HAZİNE", y=380, size=110),
    dict(type="label", t0=78.8, t1=81.7, title="Sadrazamların kahvehaneleri", sub="Peçevi'ye göre", y=420),
    dict(type="title", t0=81.84, t1=86.7, lines=["1633:", "SON GENEL YASAK"], y=760, size=110),
    dict(type="label", t0=87.0, t1=91.0, title="Kâtip Çelebi", sub="Sert yasağı onaylamadı", y=420),
    dict(type="counter", t0=91.44, t1=96.5, **{"from": 0, "to": 1631}, fmt="{} KAHVEHANE", dur=1.2, y=420, size=110),
    dict(type="tagpair", t0=91.44, t1=96.5, tags=[("İSTANBUL · 1792", 560, 91.44)]),
    # --- final
    dict(type="kinetic", t0=96.66, t1=DURATION + 1, text="YASAK DOĞRU MUYDU?", y=330, size=104),
    dict(type="tagpair", t0=97.6, t1=DURATION + 1, tags=[("DOĞRUYDU", 600, 98.52), ("KONUŞMADAN KORKTU", 740, 100.8)]),
    dict(type="cta", t0=102.5, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.4), (42.3, 44.2), (96.66, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 10.32, 15.3, 20.82, 41.18, 50.5, 62.54, 74.62]
SHAKE = [10.32, 20.82, 41.18]
FLASH = [(10.32, 0.15), (50.5, 0.12)]

MUSIC = [(0, 11.12, 3), (11.12, 25.24, 3), (25.24, 50.5, 2), (50.5, 73.84, 3), (73.84, 96.66, 2), (96.66, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.55), dict(name="hit", t=10.32, gain=0.35), dict(name="hit", t=20.82, gain=0.3),
       dict(name="impact", t=41.18, gain=0.4), dict(name="hit", t=50.5, gain=0.3), dict(name="riser", t=62.54, gain=0.2, pre=True),
       dict(name="pop", t=74.62, gain=0.3), dict(name="pop", t=102.5, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="kahve_min", focus=(0.5, 0.5), zoom=1.1, lines=["KAHVE İÇMEK", "NEDEN YASAKTI?"], y=260, size=112,
             style="white", stamp="YASAK!", stamp_y=1150, stamp_size=170, stamp_color=RED, stamp_rot=-8,
             bottom="1633 · Dördüncü Murad", bottom_y=1340)
