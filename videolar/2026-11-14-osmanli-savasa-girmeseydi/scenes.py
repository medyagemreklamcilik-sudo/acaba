"""Timeline for "Osmanlı I. Dünya Savaşı'na girmeseydi ne olurdu?" (narration seconds)."""

DURATION = 89.73
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["enver", "harita", "sevr", "resadiye", "bagis", "sultanosman", "midilli", "istanbul", "istanbul2", "canakkale",
                                  "mk", "nikola", "iran", "yavuz", "bombardiman"]}
FACES = {"enver": (0.5, 0.2), "mk": (0.5, 0.2), "nikola": (0.5, 0.2)}

SCENES = [
    dict(t=0.00, img="enver", zoom=(1.25, 1.08), focus=(0.5, 0.22)),
    dict(t=3.40, img="harita", zoom=(1.0, 1.25), focus=(0.55, 0.45), tr="flash"),
    dict(t=6.70, img="sevr", grade="dark", zoom=(1.05, 1.3), focus=(0.45, 0.45), tr="glitch"),
    dict(t=9.70, img="resadiye", zoom=(1.0, 1.22), focus=(0.5, 0.5), tr="pushup"),
    dict(t=15.10, img="bagis", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="iris"),
    dict(t=18.40, img="sultanosman", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=22.90, img="midilli", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushright"),
    dict(t=27.10, img="istanbul", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="dip"),
    dict(t=30.80, mode="plate", bg="enver", tr="bars"),
    dict(t=36.60, img="canakkale", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=41.10, img="mk", zoom=(1.0, 1.18), focus=(0.5, 0.25), tr="iris"),
    dict(t=44.00, img="nikola", zoom=(1.0, 1.18), focus=(0.5, 0.25), tr="pushleft"),
    dict(t=47.50, img="istanbul2", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="dip"),
    dict(t=53.10, img="iran", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="glitch"),
    dict(t=56.30, mode="plate", bg="harita", tr="dip"),
    dict(t=63.50, img="yavuz", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=69.80, img="bombardiman", grade="dark", zoom=(1.05, 1.35), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=74.20, img="sevr", grade="dark", zoom=(1.1, 1.3), focus=(0.45, 0.45), tr="dip"),
    dict(t=76.90, mode="plate", bg="enver", tr="dip"),
    dict(t=84.10, mode="plate", bg="harita", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=3.3, lines=["OSMANLI SAVAŞA", "GİRMESEYDİ?"], y=330, size=118),
    dict(type="kinetic", t0=3.5, t1=6.6, text="HÂLÂ BİR\nİMPARATORLUK?", y=420, size=140, style="black"),
    dict(type="kinetic", t0=6.8, t1=9.5, text="YA DA\nHİÇBİR ŞEY", y=420, size=160, style="red"),
    dict(type="label", t0=9.8, t1=15.0, title="Sultan Osman ve Reşadiye", sub="İngiltere'de yapılan iki dev savaş gemisi", y=420),
    dict(type="label", t0=15.2, t1=18.2, title="Halkın bağışları", sub="Donanma Cemiyeti kampanyası", y=420),
    dict(type="stamp", t0=21.80, t1=22.8, text="EL KONDU", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="label", t0=23.0, t1=26.9, title="İki Alman savaş gemisi", sub="Goeben ve Breslau, Ağustos 1914", y=420),
    dict(type="kinetic", t0=29.0, t1=30.6, text="KİME\nGÜVENECEĞİZ?", y=420, size=140, style="red"),
    dict(type="kinetic", t0=30.8, t1=36.4, text="SEN OLSAN?", y=420, size=170, style="red"),
    dict(type="tagpair", t0=32.6, t1=36.4, tags=[("İNGİLTERE", 760, 32.7), ("ALMANYA", 900, 35.3)]),
    dict(type="label", t0=36.7, t1=40.9, title="Tarafsız bir Osmanlı", sub="Çanakkale'de savaş olmazdı", y=420),
    dict(type="label", t0=41.2, t1=43.8, title="Mustafa Kemal", sub="adını kimse duymayabilirdi", y=420),
    dict(type="label", t0=44.1, t1=47.3, title="Çar II. Nikola", sub="Rusya'nın hedefi: İstanbul", y=420),
    dict(type="stamp", t0=51.40, t1=52.9, text="GİZLİ SÖZ", y=900, size=160, color=RED, rot=-6, fill=True),
    dict(type="label", t0=53.2, t1=56.1, title="İran", sub="tarafsızdı, yine de işgal edildi", y=420),
    dict(type="kinetic", t0=56.3, t1=63.3, text="TARİHÇİLER\nİKİYE BÖLÜNÜYOR", y=420, size=120, style="black"),
    dict(type="tagpair", t0=58.6, t1=63.3, tags=[("PAYLAŞILIRDI", 760, 58.7), ("AYAKTA KALIRDI", 900, 62.0)]),
    dict(type="label", t0=63.6, t1=69.6, title="Yavuz ve Midilli", sub="Osmanlı bayrağı altında", y=420),
    dict(type="label", t0=69.9, t1=74.0, title="Ekim 1914", sub="Karadeniz'de Rus limanları bombalandı", y=420),
    dict(type="stamp", t0=72.90, t1=74.0, text="SAVAŞ", y=900, size=180, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=74.2, t1=76.7, text="4 YIL SONRA\nİMPARATORLUK YOK", y=420, size=120, style="red"),
    dict(type="kinetic", t0=79.9, t1=83.9, text="BİR SAVAŞ DEĞİL,\nBİR KARAR", y=420, size=130, style="black"),
    dict(type="kinetic", t0=84.1, t1=DURATION + 1, text="GİRMESEYDİ\nYAŞAR MIYDI?", y=420, size=140),
    dict(type="tagpair", t0=86.8, t1=DURATION + 1, tags=[("EVET", 760, 87.4), ("HAYIR", 900, 87.9)]),
    dict(type="cta", t0=88.8, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.3), (3.5, 9.5), (21.8, 22.8), (29.0, 36.4), (51.4, 52.9), (56.3, 63.3), (72.9, 74.0), (74.2, 76.7), (79.9, 83.9),
               (84.1, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 3.4, 6.7, 21.8, 30.8, 51.4, 72.9, 74.2, 79.9]
SHAKE = [21.8, 51.4, 72.9]
FLASH = [(3.40, 0.08)]

MUSIC = [(0, 9.7, 3), (9.7, 22.9, 2), (22.9, 30.8, 3), (30.8, 36.6, 1), (36.6, 56.3, 2), (56.3, 63.5, 1), (63.5, 76.9, 3), (76.9, 84.1, 1),
         (84.1, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=21.8, gain=0.35), dict(name="hit", t=51.4, gain=0.3),
       dict(name="hit", t=72.9, gain=0.4), dict(name="pop", t=88.8, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="enver", focus=(0.5, 0.22), zoom=1.1, lines=["OSMANLI SAVAŞA", "GİRMESEYDİ?"], y=250, size=124, style="red",
             stamp="TEK KARAR", stamp_y=1180, stamp_size=100, stamp_color=YELLOW, stamp_rot=-5, bottom="Enver Paşa · 1914", bottom_y=1360)
