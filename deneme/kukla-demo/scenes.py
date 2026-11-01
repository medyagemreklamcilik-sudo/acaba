"""Deneme: tamamen çizgi film (kukla) — kardeş katli, 24 sn."""

DURATION = 24.2
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {}
FACES = {}

SCENES = [
    dict(t=0.00, mode="anim", bg="taht", pan=(0.05, 0.25), zoom=(1.08, 1.0)),
    dict(t=5.86, mode="anim", bg="avlu", pan=(0.2, 0.45), zoom=(1.0, 1.05), tr="pushleft"),
    dict(t=14.34, mode="anim", bg="koridor", pan=(0.5, 0.5), zoom=(1.0, 1.12), tr="dip"),
    dict(t=19.50, mode="anim", bg="taht", pan=(0.3, 0.15), zoom=(1.05, 1.0), tr="pushleft"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

# 19 küçük şehzade: iki sıra, 2.34'ten itibaren tek tek düşer
SEHZADELER = []
for _i in range(19):
    row, col = divmod(_i, 10)
    SEHZADELER.append(dict(type="kukla", char="sehzade", t0=0.9 + _i * 0.035, t1=5.85,
                           x=95 + col * 99 + row * 48, y=1700 + row * 150, h=300, face="r" if col % 2 else "l",
                           fall=2.4 + _i * 0.07))

OVERLAYS = [
    # --- 0-5.8 taht odası
    dict(type="kukla", char="padisah", t0=0.0, t1=5.85, x=560, y=1480, h=760, arm=[(0, "rest"), (2.3, "point")]),
    *SEHZADELER,
    dict(type="kukla", char="anlatici", t0=3.4, t1=5.85, path=[(3.4, -150), (5.2, 230)], y=1880, h=720, talk=True,
         arm=[(5.2, "shrug")]),
    dict(type="title", t0=0.0, t1=3.4, lines=["BİR GECEDE", "19 KARDEŞ"], y=330, size=130, style="red"),
    dict(type="stamp", t0=2.34, t1=3.4, text="ÖLDÜRTTÜ", y=620, size=120, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=3.5, t1=5.8, text="İLK GECE!", y=360, size=140),
    # --- 5.86-14.3 avlu: neden?
    dict(type="kukla", char="anlatici", t0=5.86, t1=14.3, x=280, y=1600, h=900, face="r", talk=True,
         arm=[(5.86, "shrug"), (7.3, "rest"), (10.26, "cross")]),
    dict(type="kukla", char="vezir", t0=6.6, t1=14.3, path=[(6.6, 1250), (9.4, 770)], y=1600, h=900, face="l",
         talk=[(10.26, 14.2)], arm=[(9.4, "rest"), (10.1, "up")]),
    dict(type="balon", t0=5.86, t1=7.3, text="PEKİ NEDEN?", x=470, y=640, size=76, tail="left"),
    dict(type="quote", t0=10.26, t1=14.2, y=430, by="Fatih Kanunnâmesi",
         words=[("Tahta", 10.26), ("çıkan,", 10.5), ("dünyanın", 11.02), ("düzeni", 11.6), ("için", 11.94),
                ("kardeşlerini", 12.32), ("öldürebilir.", 13.02)]),
    # --- 14.34-19.45 gece koridoru: tabutlar
    dict(type="tabut", t0=14.5, t1=19.45, n=19, cols=5, y=1640, every=0.09),
    dict(type="kukla", char="anlatici", t0=14.34, t1=19.45, x=170, y=1880, h=700, face="r", talk=True,
         arm=[(14.34, "rest"), (17.72, "shrug")]),
    dict(type="kukla", char="sehzade", t0=17.6, t1=19.45, x=880, y=1880, h=430, face="l"),
    dict(type="counter", t0=15.8, t1=17.6, **{"from": 0, "to": 19}, fmt="{} TABUT", dur=0.6, y=380, size=140),
    dict(type="balon", t0=17.72, t1=19.4, text="BAZILARI ÇOCUKTU!", x=560, y=820, size=64, tail="left"),
    # --- 19.5-24.2 final
    dict(type="kukla", char="padisah", t0=19.5, t1=DURATION + 1, x=270, y=1560, h=820, face="r"),
    dict(type="kukla", char="anlatici", t0=19.5, t1=DURATION + 1, x=840, y=1600, h=900, face="l", talk=True,
         arm=[(19.5, "point"), (22.84, "wave")]),
    dict(type="kinetic", t0=19.5, t1=DURATION + 1, text="ZORUNLULUK MU,\nVAHŞET Mİ?", y=330, size=104),
    dict(type="tagpair", t0=20.3, t1=DURATION + 1, tags=[("ZORUNLULUK", 600, 20.36), ("VAHŞET", 740, 21.96)]),
]

NO_CAPTIONS = [(0.0, 3.4), (5.86, 7.3), (10.26, 14.2), (17.72, 19.4), (19.5, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return 560


PUNCH = [0.0, 2.34, 3.5, 14.34]
SHAKE = [2.34]
FLASH = []

MUSIC = [(0, 5.86, 3), (5.86, 14.34, 2), (14.34, 19.5, 3), (19.5, DURATION, 1)]
SFX = [dict(name="whoosh", t=0.0, gain=0.3), dict(name="hit", t=2.4, gain=0.35), dict(name="whoosh", t=5.86, gain=0.25),
       dict(name="bell", t=14.5, gain=0.2), dict(name="pop", t=17.72, gain=0.3), dict(name="pop", t=22.84, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(bg="taht", pan=0.1, zoom=1.0, lines=["BİR GECEDE", "19 KARDEŞ"], y=260, size=130, style="red",
             stamp="NEDEN?", stamp_y=640, stamp_size=120, stamp_color=YELLOW, stamp_rot=-6,
             marks=[dict(type="kukla", char="padisah", x=560, y=1480, h=760, arm=[(0, "point")]),
                    *[dict(type="kukla", char="sehzade", x=95 + (i % 10) * 99 + (i // 10) * 48, y=1700 + (i // 10) * 150,
                           h=300, face="r" if i % 2 else "l") for i in range(19)]])
