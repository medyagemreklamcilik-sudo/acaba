"""History with Berat · 01 · How did medieval people actually stay clean? (narration seconds)."""

LANG = "en"
DURATION = 121.2
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "hook", "diagram", "woman_tub", "paris", "town", "bankside", "winchester", "aquamanile", "feast", "feast2", "soapshop",
    "castile", "aleppo", "tooth", "trotula", "garderobe", "garderobe_seat", "bodiam", "moss", "syphilis", "plague", "doctor",
    "pomander", "ruff", "louis", "logo"]}

FACES = {"louis": (0.5, 0.25), "ruff": (0.5, 0.2)}

SCENES = [
    # hook (hızlı yakınlaşma)
    dict(t=0.00, img="hook", zoom=(1.45, 1.05), focus=(0.55, 0.55)),
    dict(t=2.82, img="woman_tub", zoom=(1.2, 1.35), focus=(0.5, 0.5), tr="glitch"),
    # imza
    dict(t=5.38, mode="plate", bg="hook", tr="flash"),
    # Paris
    dict(t=9.66, img="paris", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    dict(t=15.10, img="town", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushleft"),
    dict(t=19.76, img="diagram", mode="card", maxw=880, maxh=1000, tilt=-2, tr="zoomblur"),
    # Londra
    dict(t=24.00, img="bankside", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="bars"),
    dict(t=30.38, img="winchester", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="glitch"),
    # köylüler
    dict(t=34.30, img="woman_tub", zoom=(1.0, 1.15), focus=(0.5, 0.55), tr="dip"),
    dict(t=38.56, img="aquamanile", mode="card", maxw=760, maxh=900, tilt=2, tr="pushup"),
    dict(t=40.42, img="feast", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushleft"),
    # sabun
    dict(t=45.60, img="soapshop", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    dict(t=50.20, img="castile", zoom=(1.1, 1.3), focus=(0.4, 0.5), tr="pushup"),
    dict(t=54.70, img="aleppo", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    # dişler
    dict(t=57.84, img="tooth", zoom=(1.0, 1.25), focus=(0.4, 0.5), tr="glitch"),
    dict(t=62.90, img="trotula", mode="card", maxw=680, maxh=980, tilt=-2, tr="pushup"),
    dict(t=65.82, mode="plate", bg="trotula", tr="dip"),
    # tuvalet
    dict(t=71.04, img="garderobe", zoom=(1.0, 1.2), focus=(0.5, 0.55), tr="flash"),
    dict(t=76.80, img="garderobe_seat", zoom=(1.0, 1.25), focus=(0.5, 0.6), tr="pushup"),
    dict(t=79.12, img="bodiam", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="zoomblur"),
    dict(t=82.34, img="moss", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="pushleft"),
    # efsane nereden çıktı
    dict(t=88.04, mode="plate", bg="hook", tr="dip"),
    dict(t=94.18, img="syphilis", mode="card", maxw=620, maxh=1080, tilt=2, tr="glitch"),
    dict(t=96.30, img="plague", mode="card", maxw=680, maxh=1050, tilt=-2, tr="pushleft"),
    dict(t=99.36, img="doctor", zoom=(1.0, 1.2), focus=(0.3, 0.5), tr="pushup"),
    dict(t=103.74, img="pomander", zoom=(1.0, 1.25), focus=(0.5, 0.4), tr="pushleft"),
    dict(t=105.70, img="ruff", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="bars"),
    # sonuç ve soru
    dict(t=108.64, img="hook", grade="dark", zoom=(1.1, 1.3), focus=(0.55, 0.55), tr="dip"),
    dict(t=111.60, mode="split", tr="bars", imgs=[dict(img="hook", focus=(0.55, 0.5)), dict(img="louis", focus=(0.5, 0.25))]),
    # kapanış imzası
    dict(t=117.22, mode="plate", bg="hook", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=2.75, lines=["MEDIEVAL PEOPLE", "NEVER BATHED?"], y=330, size=116),
    dict(type="stamp", t0=2.82, t1=5.3, text="WRONG.", y=820, size=190, color=RED, rot=-8, fill=True),
    # --- imza: logo
    dict(type="logo", t0=5.38, t1=9.55, img="logo", xy=(CX, 700), size=520, name="I'M BERAT",
         sub="the history they never taught you"),
    # --- Paris
    dict(type="title", t0=9.66, t1=15.0, lines=["PARIS · 1292"], y=330, size=120),
    dict(type="counter", t0=12.66, t1=15.0, **{"from": 0, "to": 26}, fmt="{}+ BATHHOUSES", dur=0.7, y=520, size=110),
    dict(type="kinetic", t0=17.34, t1=19.7, text="\"THE WATER\nIS HOT!\"", y=380, size=120),
    dict(type="tagpair", t0=20.0, t1=23.9, tags=[("STEAM BATH · 2 DENIERS", 380, 20.0), ("FULL BATH · 4 DENIERS", 520, 22.08)]),
    # --- Londra
    dict(type="label", t0=24.1, t1=28.7, title="London · Bankside", sub="along the Thames", y=420),
    dict(type="stamp", t0=29.34, t1=30.3, text="BROTHELS", y=820, size=150, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=30.38, t1=32.2, text="GUESS WHO\nOWNED THEM?", y=380, size=110, style="black"),
    dict(type="label", t0=32.3, t1=34.2, title="The Bishop of Winchester", sub="Winchester Palace, Southwark", y=420),
    # --- köylüler
    dict(type="tagpair", t0=36.7, t1=38.5, tags=[("RIVERS", 380, 37.02), ("LAKES", 520, 37.84)]),
    dict(type="label", t0=38.7, t1=40.3, title="Aquamanile", sub="medieval hand-washing jug", y=330),
    dict(type="kinetic", t0=41.14, t1=45.5, text="WASH YOUR HANDS\nBEFORE MEALS", y=380, size=100),
    # --- sabun
    dict(type="kinetic", t0=45.6, t1=47.2, text="SOAP?", y=380, size=160),
    dict(type="tagpair", t0=47.3, t1=50.1, tags=[("ANIMAL FAT", 380, 48.24), ("WOOD ASH", 520, 49.2)]),
    dict(type="label", t0=50.3, t1=54.6, title="Castile soap", sub="Spain · 12th century · olive oil", y=420),
    dict(type="label", t0=54.8, t1=57.7, title="Aleppo soap", sub="from the East", y=420),
    # --- dişler
    dict(type="kinetic", t0=57.84, t1=59.1, text="TEETH?", y=380, size=160),
    dict(type="stamp", t0=59.2, t1=60.3, text="NO TOOTHBRUSH", y=820, size=110, color=RED, rot=-6, fill=True),
    dict(type="label", t0=63.0, t1=65.7, title="The Trotula", sub="medieval medical text", y=330),
    dict(type="tagpair", t0=65.82, t1=70.9, tags=[("SAGE + SALT", 640, 65.82), ("BAKE UNTIL BURNT", 780, 66.98),
                                                   ("GRIND · RUB ON TEETH", 920, 68.3)]),
    # --- tuvalet
    dict(type="kinetic", t0=71.04, t1=72.8, text="NOW... THE TOILET", y=380, size=110, style="black"),
    dict(type="pencircle", t0=74.3, t1=76.7, cx=540, cy=1000, rx=150, ry=190, seed=4, color=RED),
    dict(type="handwrite", t0=74.84, t1=76.7, text="the toilet", y=740, size=90, dur=0.5),
    dict(type="stamp", t0=78.4, t1=79.0, text="INTO THE MOAT", y=820, size=110, color=RED, rot=-6, fill=True),
    dict(type="label", t0=79.2, t1=80.7, title="Bodiam Castle", sub="England · 1385", y=420),
    dict(type="counter", t0=80.84, t1=82.2, **{"from": 0, "to": 28}, fmt="{} TOILETS", dur=0.6, y=420, size=130),
    dict(type="kinetic", t0=82.34, t1=83.0, text="TOILET PAPER?", y=380, size=110),
    dict(type="tagpair", t0=83.0, t1=87.9, tags=[("MOSS", 380, 83.0), ("HAY", 520, 84.12), ("LEAVES", 660, 84.84),
                                                 ("RICH: WOOL", 800, 86.7)]),
    # --- efsane
    dict(type="kinetic", t0=88.04, t1=91.2, text="THE \"DIRTY\nMIDDLE AGES\" MYTH", y=760, size=104),
    dict(type="stamp", t0=92.68, t1=94.0, text="IT CAME AFTER", y=1060, size=120, color=YELLOW, rot=-6, fill=True),
    dict(type="title", t0=94.18, t1=96.2, lines=["1500s"], y=330, size=130, style="red"),
    dict(type="label", t0=94.4, t1=96.2, title="Syphilis", sub="Albrecht Dürer, 1496", y=520),
    dict(type="label", t0=96.4, t1=99.2, title="Plague", sub="bathhouses close one by one", y=330),
    dict(type="handwrite", t0=101.24, t1=103.6, text="\"water opens your pores\"", y=420, size=80, dur=0.6),
    dict(type="tagpair", t0=104.1, t1=108.5, tags=[("NO WASHING", 380, 104.1), ("NEW SHIRTS", 520, 105.7), ("PERFUME", 660, 107.22)]),
    # --- sonuç
    dict(type="kinetic", t0=108.64, t1=111.5, text="THE MIDDLE AGES\nWEREN'T THE SMELLY ONES", y=760, size=86),
    dict(type="tagpair", t0=111.6, t1=117.1, tags=[("MEDIEVAL", 380, 112.5), ("1600s", 1060, 113.96)]),
    dict(type="vs", t0=112.0, t1=117.1),
    dict(type="cta", t0=115.82, t1=117.1, y=1250),
    # --- kapanış imzası
    dict(type="logo", t0=117.22, t1=DURATION + 1, img="logo", xy=(CX, 700), size=520, name="I'M BERAT",
         sub="follow for more history"),
]

NO_CAPTIONS = [(0.0, 2.75), (5.38, 9.55), (88.04, 91.2), (108.64, 111.5), (117.22, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


# kamera kancaları: ölçülü punch/shake, her bölümün başında
PUNCH = [0.0, 2.82, 5.38, 12.66, 29.34, 45.6, 57.84, 71.04, 78.4, 92.68, 108.64]
SHAKE = [2.82, 29.34, 78.4]
FLASH = [(5.38, 0.12), (117.22, 0.12)]

MUSIC = [(0, 5.38, 3), (5.38, 9.66, 1), (9.66, 45.6, 2), (45.6, 71.04, 2), (71.04, 88.04, 3), (88.04, 108.64, 3),
         (108.64, 117.22, 2), (117.22, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=2.82, gain=0.4), dict(name="shimmer", t=5.38, gain=0.25),
       dict(name="pop", t=12.66, gain=0.2), dict(name="hit", t=29.34, gain=0.25), dict(name="hit", t=59.2, gain=0.2),
       dict(name="hit", t=78.4, gain=0.25), dict(name="riser", t=92.68, gain=0.2, pre=True), dict(name="pop", t=115.82, gain=0.3),
       dict(name="shimmer", t=117.22, gain=0.25)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="hook", focus=(0.55, 0.55), zoom=1.1, lines=["MEDIEVAL PEOPLE", "NEVER BATHED?"], y=260, size=116,
             stamp="WRONG.", stamp_y=1150, stamp_size=170, stamp_color=RED, stamp_rot=-8,
             marks=[dict(type="logo", img="logo", xy=(870, 1430), size=170)])
