"""Timeline for "Genç Osman'ı kim öldürdü?" (narration seconds)."""

DURATION = 89.16
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["osman", "osman2", "osmanyoung", "osmanat", "osmanmin", "mustafa", "mustafamin", "yeniceri", "yeniceri2",
                                  "savas", "hotin", "hotinsavas", "kabe", "yedikule", "yedikule2", "cellat", "topkapi", "topkapi2"]}
FACES = {"osman": (0.5, 0.3), "osman2": (0.5, 0.25), "osmanyoung": (0.5, 0.3), "mustafa": (0.5, 0.28), "yeniceri": (0.5, 0.25)}

SCENES = [
    dict(t=0.00, img="osman", zoom=(1.25, 1.08), focus=(0.5, 0.3)),
    dict(t=2.90, img="cellat", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.45), tr="flash"),
    dict(t=5.50, img="yeniceri", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="pushup"),
    dict(t=10.00, mode="plate", bg="yedikule", tr="dip"),
    dict(t=13.90, img="osman2", zoom=(1.0, 1.18), focus=(0.5, 0.3), tr="pushleft"),
    dict(t=16.70, img="yeniceri2", zoom=(1.0, 1.2), focus=(0.5, 0.35), tr="iris"),
    dict(t=19.60, img="hotin", zoom=(1.0, 1.22), focus=(0.5, 0.5), tr="pushright"),
    dict(t=23.20, img="hotinsavas", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="glitch"),
    dict(t=25.90, img="kabe", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=28.20, mode="plate", bg="yeniceri", tr="dip"),
    dict(t=36.90, mode="plate", bg="osman", tr="bars"),
    dict(t=42.50, img="savas", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="glitch"),
    dict(t=45.80, img="topkapi", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=49.50, img="osmanyoung", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="dip"),
    dict(t=51.60, img="yedikule", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.45), tr="pushup"),
    dict(t=54.90, img="mustafa", zoom=(1.0, 1.18), focus=(0.5, 0.28), tr="iris"),
    dict(t=57.40, img="cellat", grade="dark", zoom=(1.15, 1.4), focus=(0.5, 0.4), tr="dip"),
    dict(t=60.30, img="mustafamin", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushright"),
    dict(t=65.80, mode="plate", bg="osman", tr="dip"),
    dict(t=72.40, img="yedikule2", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=78.40, img="osmanmin", zoom=(1.05, 1.3), focus=(0.5, 0.35), tr="zoomblur"),
    dict(t=81.00, img="topkapi2", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="dip"),
    dict(t=83.90, mode="plate", bg="osman", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=5.3, lines=["17 YAŞINDAKİ PADİŞAHI", "BOĞDULAR"], y=330, size=100),
    dict(type="stamp", t0=3.10, t1=5.3, text="KULAĞI SARAYA", y=900, size=120, color=RED, rot=-6, fill=True),
    dict(type="stamp", t0=6.60, t1=9.8, text="İLK KEZ", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=10.6, t1=13.7, text="KEMENTİ\nKİM UZATTI?", y=420, size=150, style="red"),
    dict(type="label", t0=14.0, t1=16.5, title="Genç Osman", sub="II. Osman, 14 yaşında tahtta (1618)", y=420),
    dict(type="label", t0=16.8, t1=19.4, title="Yeniçeri Ocağı", sub="sarayın en büyük gücü", y=420),
    dict(type="label", t0=19.7, t1=22.0, title="Hotin Kalesi", sub="1621 Lehistan seferi", y=420),
    dict(type="stamp", t0=22.30, t1=23.1, text="ALINAMADI", y=900, size=150, color=RED, rot=-6, fill=True),
    dict(type="stamp", t0=24.30, t1=25.8, text="SUÇLU: YENİÇERİ", y=900, size=110, color=YELLOW, rot=-5, fill=True),
    dict(type="label", t0=26.0, t1=28.0, title="Hac yolculuğu", sub="Padişahın açıkladığı niyet", y=420),
    dict(type="kinetic", t0=28.3, t1=30.4, text="SÖYLENTİ", y=420, size=170, style="black"),
    dict(type="kinetic", t0=30.5, t1=36.6, text="HAC DEĞİL,\nYENİ ORDU", y=420, size=150, style="red"),
    dict(type="kinetic", t0=36.9, t1=42.3, text="SEN OLSAN\nGÜVENİR MİYDİN?", y=420, size=130, style="red"),
    dict(type="tagpair", t0=39.4, t1=42.3, tags=[("GÜVENİRDİM", 760, 39.5), ("ASLA", 900, 41.4)]),
    dict(type="label", t0=42.6, t1=45.6, title="Mayıs 1622", sub="yeniçeri ayaklanması", y=420),
    dict(type="stamp", t0=44.90, t1=45.7, text="İSYAN", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="label", t0=45.9, t1=49.3, title="Saraydan Yedikule'ye", sub="bir pazar arabasıyla", y=420),
    dict(type="source", t0=49.6, t1=51.4, text="anlatılanlara göre"),
    dict(type="label", t0=51.7, t1=54.7, title="Yedikule Zindanları", sub="bekleyen: Kara Davud Paşa", y=420),
    dict(type="label", t0=55.0, t1=57.2, title="I. Mustafa", sub="yeni padişah; Davud Paşa eniştesi", y=420),
    dict(type="stamp", t0=58.80, t1=60.2, text="KEMENT", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="label", t0=60.4, t1=65.6, title="Kulağı kesildi", sub="yeni padişahın annesine gönderildi", y=420),
    dict(type="kinetic", t0=65.8, t1=71.9, text="\"SEN DAHA\nÇOCUKSUN\"", y=420, size=150, style="black"),
    dict(type="label", t0=72.5, t1=77.0, title="1623, Yedikule", sub="Davud Paşa'nın sonu", y=420),
    dict(type="stamp", t0=77.20, t1=78.3, text="AYNI YERDE İDAM", y=900, size=110, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=78.4, t1=80.9, text="KEMENTİ ÇEKEN:\nASKER", y=420, size=130, style="black"),
    dict(type="kinetic", t0=81.0, t1=83.8, text="KEMENTİ UZATAN:\nSARAY", y=420, size=130, style="red"),
    dict(type="kinetic", t0=83.9, t1=DURATION + 1, text="YENİÇERİLER Mİ?\nDAVUD PAŞA MI?", y=420, size=120),
    dict(type="tagpair", t0=86.0, t1=DURATION + 1, tags=[("YENİÇERİ", 760, 86.2), ("DAVUD PAŞA", 900, 87.3)]),
    dict(type="cta", t0=88.2, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 5.3), (6.6, 7.6), (10.6, 13.7), (22.3, 23.1), (24.3, 25.3), (28.3, 36.6), (36.9, 42.3), (44.9, 45.7), (58.8, 59.8),
               (65.8, 71.9), (77.2, 78.3), (78.4, 83.8), (83.9, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 3.1, 6.6, 22.3, 36.9, 44.9, 58.8, 77.2, 81.0]
SHAKE = [3.1, 44.9, 58.8]
FLASH = [(2.90, 0.08)]

MUSIC = [(0, 10.0, 3), (10.0, 28.2, 2), (28.2, 36.9, 3), (36.9, 42.5, 1), (42.5, 57.4, 3), (57.4, 65.8, 2), (65.8, 72.4, 1), (72.4, 83.9, 3),
         (83.9, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=3.1, gain=0.35), dict(name="hit", t=44.9, gain=0.3),
       dict(name="hit", t=58.8, gain=0.35), dict(name="hit", t=77.2, gain=0.3), dict(name="pop", t=88.2, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="osman", focus=(0.5, 0.32), zoom=1.1, lines=["17 YAŞINDAKİ", "PADİŞAHI BOĞDULAR"], y=250, size=112, style="yellow",
             stamp="KİM ÖLDÜRDÜ?", stamp_y=1150, stamp_size=110, stamp_color=RED, stamp_rot=-6, bottom="II. Osman · Yedikule · 1622", bottom_y=1360)
