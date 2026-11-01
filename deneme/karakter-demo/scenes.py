"""Deneme: maskot karakterle 24 sn'lik anlatım (kardeş katli)."""

DURATION = 24.2
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["mehmed3", "cenaze", "sanduka", "kanunname", "fatih", "babussaade"]}
FACES = {"mehmed3": (0.5, 0.35), "fatih": (0.6, 0.35)}

SCENES = [
    dict(t=0.00, img="mehmed3", grade="dark", zoom=(1.3, 1.05), focus=(0.5, 0.35)),
    dict(t=5.86, img="babussaade", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="glitch"),
    dict(t=7.36, img="fatih", zoom=(1.0, 1.15), focus=(0.6, 0.35), tr="pushleft"),
    dict(t=10.26, mode="plate", bg="kanunname", tr="dip"),
    dict(t=14.34, img="cenaze", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="flash"),
    dict(t=17.72, img="sanduka", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=19.50, mode="plate", bg="mehmed3", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

K = dict(type="karakter", x=280, y=1500, h=470, desk=True)
OVERLAYS = [
    # karakter (alt sol, sabit yerinde; poz cümleye göre değişir)
    dict(type="karakter", t0=0.0, t1=3.45, pose="tam", x=790, y=1500, h=860, enter="right"),
    dict(K, t0=3.5, t1=5.82, pose="kizgin"),
    dict(K, t0=5.86, t1=9.0, pose="dusunen", talk=False),
    dict(K, t0=9.0, t1=14.3, pose="anlatan"),
    dict(K, t0=14.34, t1=17.68, pose="suphe", talk=False),
    dict(K, t0=17.72, t1=19.45, pose="kizgin"),
    dict(K, t0=19.5, t1=22.8, pose="anlatan"),
    dict(K, t0=22.84, t1=DURATION + 1, pose="sevincli"),
    # metinler
    dict(type="title", t0=0.0, t1=3.4, lines=["BİR GECEDE", "19 KARDEŞ"], y=330, size=130, style="red"),
    dict(type="counter", t0=1.02, t1=3.4, **{"from": 0, "to": 19}, fmt="{}", dur=0.6, y=640, size=220),
    dict(type="stamp", t0=2.34, t1=3.4, text="ÖLDÜRTTÜ", y=860, size=120, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=3.5, t1=5.8, text="İLK GECE!", y=420, size=140),
    dict(type="balon", t0=5.86, t1=7.3, text="PEKİ NEDEN?", x=600, y=1060, size=72, tail="left"),
    dict(type="label", t0=7.5, t1=10.1, title="Fatih Sultan Mehmed", sub="Kanunnâme", y=420),
    dict(type="quote", t0=10.26, t1=14.2, y=560, by="Fatih Kanunnâmesi",
         words=[("Tahta", 10.26), ("çıkan,", 10.5), ("dünyanın", 11.02), ("düzeni", 11.6), ("için", 11.94),
                ("kardeşlerini", 12.32), ("öldürebilir.", 13.02)]),
    dict(type="counter", t0=15.8, t1=17.6, **{"from": 0, "to": 19}, fmt="{} TABUT", dur=0.6, y=420, size=140),
    dict(type="balon", t0=17.72, t1=19.4, text="BAZILARI ÇOCUKTU!", x=640, y=1060, size=64, tail="left"),
    dict(type="kinetic", t0=19.5, t1=DURATION + 1, text="ZORUNLULUK MU,\nVAHŞET Mİ?", y=360, size=110),
    dict(type="tagpair", t0=20.3, t1=DURATION + 1, tags=[("ZORUNLULUK", 600, 20.36), ("VAHŞET", 740, 21.96)]),
]

NO_CAPTIONS = [(0.0, 3.4), (5.86, 7.3), (10.26, 14.2), (17.72, 19.4), (19.5, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return 880


PUNCH = [0.0, 2.34, 3.5, 14.34, 17.72]
SHAKE = [2.34, 17.72]
FLASH = []

MUSIC = [(0, 5.86, 3), (5.86, 14.34, 2), (14.34, 19.5, 3), (19.5, DURATION, 1)]
SFX = [dict(name="whoosh", t=0.0, gain=0.3), dict(name="hit", t=2.34, gain=0.35), dict(name="pop", t=5.86, gain=0.3),
       dict(name="pop", t=17.72, gain=0.3), dict(name="pop", t=22.84, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="mehmed3", grade="dark", focus=(0.5, 0.35), zoom=1.05, lines=["BİR GECEDE", "19 KARDEŞ"], y=260, size=130,
             style="red", marks=[dict(type="karakter", pose="kizgin", x=300, y=1500, h=560, talk=False, desk=True)],
             stamp="NEDEN?", stamp_y=860, stamp_size=130, stamp_color=YELLOW, stamp_rot=-6)
