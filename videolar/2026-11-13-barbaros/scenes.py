"""Timeline for "Barbaros: korsan mı, amiral mi?" (narration seconds)."""

DURATION = 92.03
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["barbaros", "barbaros2", "kardesler", "oruc", "gemi", "gemi2", "kadirga", "harita", "cezayir", "yavuz",
                                  "kanuni", "preveze", "preveze2", "turbe"]}
FACES = {"barbaros": (0.5, 0.3), "barbaros2": (0.5, 0.25), "oruc": (0.5, 0.3), "yavuz": (0.5, 0.3), "kanuni": (0.45, 0.35)}

SCENES = [
    dict(t=0.00, img="barbaros", zoom=(1.25, 1.08), focus=(0.5, 0.3)),
    dict(t=4.30, img="preveze2", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="flash"),
    dict(t=5.30, mode="plate", bg="barbaros", tr="dip"),
    dict(t=9.30, img="kardesler", zoom=(1.0, 1.2), focus=(0.5, 0.35), tr="pushup"),
    dict(t=15.40, img="oruc", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="iris"),
    dict(t=20.60, img="gemi", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=25.40, img="harita", zoom=(1.0, 1.25), focus=(0.4, 0.5), tr="pushright"),
    dict(t=32.30, img="kadirga", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="dip"),
    dict(t=36.00, mode="plate", bg="barbaros", tr="bars"),
    dict(t=45.40, img="cezayir", zoom=(1.0, 1.25), focus=(0.5, 0.45), tr="glitch"),
    dict(t=48.70, img="yavuz", zoom=(1.0, 1.18), focus=(0.5, 0.3), tr="pushup"),
    dict(t=51.90, img="kanuni", zoom=(1.0, 1.2), focus=(0.45, 0.35), tr="pushleft"),
    dict(t=54.90, img="preveze", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=59.80, img="preveze2", grade="dark", zoom=(1.1, 1.35), focus=(0.5, 0.5), tr="dip"),
    dict(t=66.60, img="gemi2", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="glitch"),
    dict(t=74.70, mode="plate", bg="barbaros2", tr="dip"),
    dict(t=80.90, img="turbe", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=87.60, mode="plate", bg="barbaros", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=5.2, lines=["AVRUPA'NIN EN", "KORKULAN KORSANI"], y=330, size=104),
    dict(type="stamp", t0=4.30, t1=5.2, text="OSMANLI AMİRALİ", y=900, size=110, color=YELLOW, rot=-6, fill=True),
    dict(type="kinetic", t0=5.4, t1=9.1, text="O AD\nONUN DEĞİLDİ", y=420, size=160, style="red"),
    dict(type="label", t0=9.4, t1=15.2, title="Hızır ve Oruç", sub="Akdeniz'de gemi basan iki kardeş", y=420),
    dict(type="label", t0=15.5, t1=18.0, title="Oruç Reis", sub="kızıl sakallı ağabey", y=420),
    dict(type="stamp", t0=18.10, t1=20.4, text="BARBAROSSA", y=900, size=140, color=RED, rot=-6, fill=True),
    dict(type="label", t0=20.7, t1=25.2, title="Oruç'un ölümü", sub="İspanyollarla savaşırken, 1518", y=420),
    dict(type="label", t0=25.5, t1=32.1, title="Endülüs'ten Afrika'ya", sub="İspanya'dan kaçan Müslümanlar", y=420),
    dict(type="counter", t0=33.9, t1=35.9, **{"from": 0, "to": 70}, fmt="{} BİN", dur=0.8, y=620, size=170),
    dict(type="kinetic", t0=36.0, t1=38.9, text="KARAR ANI", y=420, size=170, style="black"),
    dict(type="kinetic", t0=39.1, t1=45.2, text="SEN OLSAN?", y=420, size=170, style="red"),
    dict(type="tagpair", t0=41.3, t1=45.2, tags=[("KORSAN KRALI", 760, 41.5), ("PADİŞAHA BAĞLI", 900, 43.8)]),
    dict(type="label", t0=45.5, t1=48.5, title="Cezayir", sub="1519'da Osmanlı'ya bağlandı", y=420),
    dict(type="label", t0=48.8, t1=50.9, title="Yavuz Sultan Selim", sub="ona yeni bir ad verdi", y=420),
    dict(type="stamp", t0=51.00, t1=51.8, text="HAYREDDİN", y=900, size=150, color=YELLOW, rot=-5, fill=True),
    dict(type="label", t0=52.0, t1=54.7, title="Kanuni Sultan Süleyman", sub="1534: kaptan-ı derya", y=420),
    dict(type="label", t0=55.0, t1=59.6, title="Preveze, 1538", sub="karşısında Andrea Doria", y=420),
    dict(type="kinetic", t0=59.9, t1=63.5, text="122 GEMİYE KARŞI\n200'Ü AŞKIN", y=420, size=120, style="black"),
    dict(type="stamp", t0=64.50, t1=66.4, text="KAÇAN: AVRUPA", y=900, size=130, color=RED, rot=-6, fill=True),
    dict(type="label", t0=66.7, t1=74.5, title="Lipari, 1544", sub="binlerce kişinin esir alındığı yazılır", y=420),
    dict(type="kinetic", t0=78.0, t1=80.7, text="BİRİNİN KAHRAMANI\nÖTEKİNİN KÂBUSU", y=420, size=110, style="red"),
    dict(type="label", t0=81.0, t1=85.1, title="Barbaros Türbesi", sub="Beşiktaş, İstanbul", y=420),
    dict(type="kinetic", t0=85.3, t1=87.4, text="AYNI DENİZ", y=420, size=170, style="black"),
    dict(type="kinetic", t0=87.6, t1=DURATION + 1, text="KORSAN MI?\nAMİRAL Mİ?", y=420, size=150),
    dict(type="tagpair", t0=88.9, t1=DURATION + 1, tags=[("KORSAN", 760, 89.3), ("AMİRAL", 900, 90.0)]),
    dict(type="cta", t0=91.0, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 5.2), (5.4, 9.1), (18.1, 19.4), (33.9, 35.9), (36.0, 38.9), (39.1, 45.2), (51.0, 51.8), (59.9, 63.5), (64.5, 65.9),
               (78.0, 80.7), (85.3, 87.4), (87.6, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 4.3, 18.1, 33.9, 39.1, 51.0, 54.9, 64.5, 78.0]
SHAKE = [4.3, 54.9, 64.5]
FLASH = [(4.30, 0.08)]

MUSIC = [(0, 9.3, 3), (9.3, 25.4, 2), (25.4, 36.0, 2), (36.0, 45.4, 1), (45.4, 54.9, 2), (54.9, 66.6, 3), (66.6, 80.9, 2), (80.9, 87.6, 1),
         (87.6, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=4.3, gain=0.35), dict(name="hit", t=18.1, gain=0.3),
       dict(name="hit", t=54.9, gain=0.35), dict(name="hit", t=64.5, gain=0.3), dict(name="pop", t=91.0, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="barbaros", focus=(0.5, 0.3), zoom=1.08, lines=["KORSAN MI?", "AMİRAL Mİ?"], y=250, size=130, style="white",
             stamp="KIZIL SAKAL", stamp_y=1160, stamp_size=110, stamp_color=YELLOW, stamp_rot=-6, bottom="Hayreddin · Preveze 1538", bottom_y=1360)
