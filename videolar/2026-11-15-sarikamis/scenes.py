"""Timeline for "Sarıkamış faciası: 90 bin asker dondu mu?" (narration seconds)."""

DURATION = 88.53
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["enver", "enver2", "kar1", "kar2", "tirmanis", "kayak", "harita", "dag", "orman", "rus", "esir",
                                  "tifus", "kamuflaj"]}
FACES = {"enver": (0.5, 0.2), "yudenic": (0.45, 0.35), "enver2": (0.5, 0.15)}

SCENES = [
    dict(t=0.00, img="enver", zoom=(1.25, 1.08), focus=(0.5, 0.2)),
    dict(t=4.40, img="kar1", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="flash"),
    dict(t=5.90, mode="plate", bg="kar1", tr="dip"),
    dict(t=10.50, img="kar2", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushup"),
    dict(t=13.50, img="harita", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=20.80, img="orman", grade="dark", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="dip"),
    dict(t=27.50, img="dag", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=31.10, img="tirmanis", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="iris"),
    dict(t=33.40, img="kayak", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.45), tr="dip"),
    dict(t=37.00, mode="plate", bg="enver", tr="bars"),
    dict(t=42.00, mode="plate", bg="kar1", tr="glitch"),
    dict(t=44.30, mode="plate", bg="harita", tr="dip"),
    dict(t=54.30, img="esir", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=59.10, img="tifus", zoom=(1.0, 1.2), focus=(0.5, 0.35), tr="iris"),
    dict(t=62.70, img="rus", zoom=(1.0, 1.35), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=70.10, img="enver2", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.25), tr="dip"),
    dict(t=74.20, img="kamuflaj", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    dict(t=77.80, img="kar1", grade="dark", zoom=(1.1, 1.35), focus=(0.5, 0.5), tr="dip"),
    dict(t=82.80, mode="plate", bg="orman", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=4.3, lines=["90 BİN ASKER", "DONARAK ŞEHİT OLDU?"], y=330, size=108),
    dict(type="stamp", t0=4.40, t1=5.8, text="HEPİMİZ DUYDUK", y=900, size=120, color=YELLOW, rot=-6, fill=True),
    dict(type="kinetic", t0=6.0, t1=10.3, text="TARİHÇİLER:\nRAKAM DOĞRU DEĞİL", y=420, size=120, style="red"),
    dict(type="kinetic", t0=10.6, t1=13.3, text="GERÇEK HİKÂYE\nDAHA ACI", y=420, size=130, style="black"),
    dict(type="label", t0=13.6, t1=20.6, title="Enver Paşa'nın planı", sub="Rusları Sarıkamış'ta kuşatmak", y=420),
    dict(type="stamp", t0=24.10, t1=24.8, text="KIŞ", y=900, size=200, color=RED, rot=-6, fill=True),
    dict(type="label", t0=24.9, t1=27.3, title="Aralık 1914", sub="Kafkas cephesi", y=420),
    dict(type="label", t0=27.6, t1=30.9, title="Allahuekber Dağları", sub="karlı geçit", y=420),
    dict(type="counter", t0=31.8, t1=33.3, **{"from": 1, "to": 14}, fmt="{} SAAT", dur=0.6, y=620, size=170),
    dict(type="kinetic", t0=37.0, t1=41.8, text="SEN OLSAN\nİTİRAZ EDER MİYDİN?", y=420, size=120, style="red"),
    dict(type="tagpair", t0=39.4, t1=41.8, tags=[("EDERDİM", 760, 39.5), ("EMİR EMİRDİR", 900, 41.0)]),
    dict(type="kinetic", t0=42.0, t1=44.1, text="KAÇ KİŞİ?", y=420, size=190, style="black"),
    dict(type="kinetic", t0=44.3, t1=46.4, text="POPÜLER ANLATI\n90.000", y=420, size=130, style="black"),
    dict(type="kinetic", t0=46.5, t1=50.3, text="GENELKURMAY\n~60.000 KAYIP", y=420, size=130, style="red"),
    dict(type="kinetic", t0=50.4, t1=54.1, text="RUS KAYITLARI\n~23.000 ŞEHİT", y=420, size=130),
    dict(type="source", t0=46.5, t1=54.1, text="TDV İslâm Ansiklopedisi · Sarıkamış Harekâtı"),
    dict(type="label", t0=54.4, t1=58.9, title="Çarpışmada ölenler", sub="toplam kaybın üçte birinden az", y=420),
    dict(type="label", t0=59.2, t1=62.5, title="Soğuk, tifüs, esaret", sub="kayıpların büyük kısmı", y=420),
    dict(type="label", t0=62.8, t1=66.2, title="Rus Kafkas Ordusu", sub="kış onları da vurdu", y=420),
    dict(type="counter", t0=67.0, t1=69.9, **{"from": 0, "to": 9}, fmt="{} BİNDEN FAZLA", dur=0.6, y=620, size=120),
    dict(type="kinetic", t0=70.9, t1=74.0, text="BEDELİ\nUYGULAYANLAR ÖDER", y=420, size=120, style="red"),
    dict(type="kinetic", t0=80.5, t1=82.6, text="HER ASKER\nBİRİNİN OĞLUYDU", y=420, size=130, style="black"),
    dict(type="kinetic", t0=82.8, t1=DURATION + 1, text="KIŞ MI?\nENVER PAŞA MI?", y=420, size=140),
    dict(type="tagpair", t0=85.6, t1=DURATION + 1, tags=[("KIŞ", 760, 85.8), ("ENVER PAŞA", 900, 86.6)]),
    dict(type="cta", t0=87.6, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 5.8), (6.0, 13.3), (24.1, 24.8), (31.8, 33.3), (37.0, 54.1), (67.0, 69.9), (70.9, 74.0), (80.5, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 4.4, 6.0, 24.1, 37.0, 42.0, 46.5, 50.4, 70.9]
SHAKE = [4.4, 24.1, 42.0]
FLASH = [(4.40, 0.08)]

MUSIC = [(0, 13.5, 3), (13.5, 27.5, 2), (27.5, 37.0, 3), (37.0, 42.0, 1), (42.0, 54.3, 2), (54.3, 70.1, 2), (70.1, 82.8, 1), (82.8, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=4.4, gain=0.3), dict(name="hit", t=24.1, gain=0.35),
       dict(name="hit", t=42.0, gain=0.35), dict(name="pop", t=87.6, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="kar2", grade="dark", focus=(0.5, 0.4), zoom=1.05, lines=["90 BİN ASKER", "DONDU MU?"], y=250, size=130, style="yellow",
             portraits=[("enver", 540, 860, 380)], stamp="RAKAMLAR BAŞKA", stamp_y=1200, stamp_size=100, stamp_color=RED, stamp_rot=-5,
             bottom="Sarıkamış · Aralık 1914", bottom_y=1360)
