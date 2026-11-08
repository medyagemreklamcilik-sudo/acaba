"""Timeline for "Atatürk'ün vasiyeti" (narration seconds)."""

DURATION = 84.11
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["portre", "portre2", "vasiyet", "gazete", "vasiyet2", "imza", "isbank", "tdk", "ttk", "makbule", "ulku", "inonu"]}
FACES = {"portre": (0.5, 0.3), "portre2": (0.5, 0.2), "makbule": (0.5, 0.25), "ulku": (0.3, 0.3), "inonu": (0.5, 0.2)}

SCENES = [
    dict(t=0.00, img="portre", zoom=(1.25, 1.08), focus=(0.5, 0.3)),
    dict(t=2.56, img="vasiyet", zoom=(1.0, 1.3), focus=(0.5, 0.35), tr="flash"),
    dict(t=8.34, mode="plate", bg="vasiyet", tr="dip"),
    dict(t=10.70, img="vasiyet2", zoom=(1.0, 1.25), focus=(0.5, 0.4), tr="pushup"),
    dict(t=13.12, img="portre2", grade="dark", zoom=(1.05, 1.25), focus=(0.5, 0.25), tr="dip"),
    dict(t=16.60, img="isbank", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushleft"),
    dict(t=21.20, mode="plate", bg="isbank", tr="dip"),
    dict(t=26.24, img="tdk", zoom=(1.0, 1.25), focus=(0.5, 0.3), tr="pushup"),
    dict(t=27.50, img="ttk", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushright"),
    dict(t=29.20, img="makbule", zoom=(1.0, 1.2), focus=(0.5, 0.25), tr="iris"),
    dict(t=31.86, img="ulku", zoom=(1.0, 1.2), focus=(0.35, 0.35), tr="pushleft"),
    dict(t=34.92, img="inonu", zoom=(1.0, 1.18), focus=(0.5, 0.2), tr="pushup"),
    dict(t=38.52, mode="plate", bg="portre", tr="dip"),
    dict(t=44.56, img="gazete", grade="dark", zoom=(1.0, 1.25), focus=(0.4, 0.3), tr="glitch"),
    dict(t=53.54, img="isbank", grade="dark", zoom=(1.15, 1.4), focus=(0.5, 0.4), tr="diag"),
    dict(t=60.38, img="vasiyet", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.7), tr="dip"),
    dict(t=63.16, img="isbank", zoom=(1.2, 1.45), focus=(0.5, 0.3), tr="zoomblur"),
    dict(t=68.20, img="portre2", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.2), tr="dip"),
    dict(t=73.34, img="vasiyet", zoom=(1.35, 1.6), focus=(0.55, 0.93), tr="dip"),
    dict(t=78.00, mode="plate", bg="portre", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=2.5, lines=["ÖLÜMÜNDEN 66 GÜN ÖNCE"], y=330, size=100),
    dict(type="stamp", t0=4.10, t1=8.2, text="VASİYET", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=6.62, t1=8.2, text="İKİ KURUMA", y=420, size=140, style="black"),
    dict(type="kinetic", t0=8.34, t1=10.6, text="BUGÜN NE OLDU?", y=620, size=130, style="red"),
    dict(type="label", t0=10.8, t1=13.0, title="5 Eylül 1938", sub="Dolmabahçe Sarayı", y=420),
    dict(type="label", t0=16.7, t1=21.0, title="Türkiye İş Bankası", sub="Atatürk'ün hisseleri", y=420),
    dict(type="kinetic", t0=21.2, t1=26.1, text="GELİR\nPARTİYE DEĞİL", y=420, size=130, style="black"),
    dict(type="stamp", t0=24.26, t1=26.1, text="İKİ KURUMA", y=1000, size=110, color=YELLOW, rot=-5, fill=True),
    dict(type="label", t0=26.3, t1=27.4, title="Türk Dil Kurumu", sub="1932", y=420),
    dict(type="label", t0=27.6, t1=29.1, title="Türk Tarih Kurumu", sub="1931", y=420),
    dict(type="label", t0=30.0, t1=31.7, title="Makbule Atadan", sub="kız kardeşi", y=420),
    dict(type="label", t0=31.9, t1=34.8, title="Manevi kızları", sub="Ülkü ile", y=420),
    dict(type="label", t0=35.0, t1=38.4, title="İsmet İnönü", sub="çocuklarının okuması için pay", y=420),
    dict(type="kinetic", t0=38.52, t1=44.4, text="SEN KİME\nBIRAKIRDIN?", y=420, size=130, style="red"),
    dict(type="tagpair", t0=41.4, t1=44.4, tags=[("AİLENE", 760, 41.62), ("BİR FİKRE", 900, 43.76)]),
    dict(type="stamp", t0=45.70, t1=47.0, text="RAHAT BIRAKILMADI", y=900, size=96, color=RED, rot=-6, fill=True),
    dict(type="counter", t0=47.16, t1=53.4, **{"from": 1900, "to": 1953}, fmt="{}", dur=0.5, y=440, size=170),
    dict(type="stamp", t0=49.72, t1=51.2, text="HAZİNE'YE", y=900, size=130, color=RED, rot=-6, fill=True),
    dict(type="stamp", t0=52.78, t1=53.4, text="İPTAL", y=900, size=150, color=YELLOW, rot=-5, fill=True),
    dict(type="counter", t0=53.54, t1=60.2, **{"from": 1953, "to": 1980}, fmt="{}", dur=0.5, y=440, size=170),
    dict(type="stamp", t0=56.64, t1=58.4, text="KAPATILDI", y=900, size=130, color=RED, rot=-6, fill=True),
    dict(type="counter", t0=60.38, t1=63.0, **{"from": 1980, "to": 1992}, fmt="{}", dur=0.5, y=440, size=170),
    dict(type="stamp", t0=61.98, t1=63.0, text="GERİ VERİLDİ", y=900, size=120, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=63.2, t1=68.0, text="BUGÜN HÂLÂ\nTARTIŞILIYOR", y=420, size=130, style="black"),
    dict(type="kinetic", t0=72.0, t1=73.2, text="NEYE İNANDIĞI", y=620, size=130, style="red"),
    dict(type="kinetic", t0=75.92, t1=77.9, text="DİL VE TARİH", y=380, size=150, style="black"),
    dict(type="kinetic", t0=78.0, t1=DURATION + 1, text="VASİYETE\nSADIK KALINDI MI?", y=420, size=120),
    dict(type="tagpair", t0=81.3, t1=DURATION + 1, tags=[("EVET", 760, 81.5), ("HAYIR", 900, 82.26)]),
    dict(type="cta", t0=82.8, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(49.6, 50.7), (56.6, 57.6), (0.0, 2.5), (4.0, 5.0), (8.34, 10.6), (21.2, 22.5), (24.2, 26.1), (38.52, 44.4), (63.2, 66.4), (72.0, 73.2), (75.9, 77.9), (78.0, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 4.10, 8.34, 24.26, 38.52, 45.70, 49.72, 56.64, 61.98, 63.2]
SHAKE = [4.10, 49.72, 56.64]
FLASH = [(2.56, 0.08)]

MUSIC = [(0, 8.34, 2), (8.34, 26.24, 2), (26.24, 38.52, 2), (38.52, 44.56, 1), (44.56, 63.16, 3), (63.16, 78.0, 2), (78.0, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=4.10, gain=0.35), dict(name="hit", t=49.72, gain=0.3),
       dict(name="hit", t=56.64, gain=0.3), dict(name="pop", t=82.8, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="vasiyet", grade="dark", focus=(0.5, 0.4), zoom=1.05, lines=["ATATÜRK'ÜN", "VASİYETİNE NE OLDU?"], y=250, size=104,
             style="red", portraits=[("portre", 540, 820, 400)], stamp="66 GÜN ÖNCE", stamp_y=1260, stamp_size=104, stamp_color=YELLOW, stamp_rot=-5)
