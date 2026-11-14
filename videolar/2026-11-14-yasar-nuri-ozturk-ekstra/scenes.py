"""Timeline for "Yaşar Nuri Öztürk: iki tarafın da kızdığı ilahiyatçı" (narration seconds)."""

DURATION = 93.88
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["yno", "yno2", "yno3", "ynotv", "kutuphane", "siyaset", "mushaf", "mushaf2", "medrese", "medrese2",
                                  "ilahiyat", "meal", "kitap", "cenaze"]}
FACES = {"yno": (0.5, 0.25), "yno2": (0.55, 0.3), "yno3": (0.5, 0.3), "ynotv": (0.45, 0.35), "siyaset": (0.35, 0.3)}

SCENES = [
    dict(t=0.00, img="yno", zoom=(1.2, 1.06), focus=(0.5, 0.25)),
    dict(t=6.40, img="yno3", grade="dark", zoom=(1.05, 1.25), focus=(0.5, 0.35), tr="glitch"),
    dict(t=8.40, mode="plate", bg="yno", tr="dip"),
    dict(t=12.50, img="mushaf", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=14.20, img="medrese", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=16.00, img="medrese2", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushright"),
    dict(t=18.90, img="kutuphane", zoom=(1.0, 1.25), focus=(0.6, 0.45), tr="iris"),
    dict(t=22.00, img="ilahiyat", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=25.90, img="yno2", zoom=(1.0, 1.2), focus=(0.55, 0.35), tr="pushleft"),
    dict(t=29.20, mode="plate", bg="yno", tr="dip"),
    dict(t=31.70, img="mushaf2", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.5), tr="bars"),
    dict(t=39.00, img="ynotv", zoom=(1.0, 1.2), focus=(0.45, 0.4), tr="pushup"),
    dict(t=43.80, mode="plate", bg="yno", tr="bars"),
    dict(t=50.90, img="meal", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushup"),
    dict(t=57.50, img="yno3", grade="dark", zoom=(1.1, 1.35), focus=(0.5, 0.35), tr="glitch"),
    dict(t=63.00, img="siyaset", zoom=(1.0, 1.2), focus=(0.4, 0.4), tr="pushleft"),
    dict(t=67.00, mode="plate", bg="kitap", tr="dip"),
    dict(t=74.10, img="cenaze", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.45), tr="dip"),
    dict(t=78.30, img="yno2", grade="dark", zoom=(1.1, 1.3), focus=(0.55, 0.35), tr="dip"),
    dict(t=83.20, img="mushaf", grade="dark", zoom=(1.1, 1.35), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=87.90, mode="plate", bg="yno", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    dict(type="title", t0=0.0, t1=6.3, lines=["DOKUZ YAŞINDA", "HAFIZ OLDU"], y=1000, size=118),
    dict(type="stamp", t0=4.80, t1=6.3, text="EN SERT TEPKİ: DİNDARLAR", y=1300, size=84, color=RED, rot=-5, fill=True),
    dict(type="kinetic", t0=6.5, t1=8.3, text="LAİKLER DE\nGÜVENMEDİ", y=420, size=140, style="black"),
    dict(type="kinetic", t0=8.5, t1=10.3, text="İKİ TARAF DA\nKIZDI", y=420, size=150, style="red"),
    dict(type="label", t0=10.4, t1=12.3, title="Yaşar Nuri Öztürk", sub="ilahiyat profesörü", y=420),
    dict(type="label", t0=12.6, t1=14.0, title="Babasından Kur'an", sub="dokuz yaşında hafız", y=420),
    dict(type="label", t0=14.3, t1=15.9, title="10 yıl medrese", sub="klasik din eğitimi", y=420),
    dict(type="label", t0=16.1, t1=18.8, title="12 yıl imam ve vaiz", sub="cami kürsüsünde", y=420),
    dict(type="label", t0=19.0, t1=21.8, title="Hukuk + İlahiyat", sub="İslam felsefesinde doktora", y=420),
    dict(type="label", t0=22.1, t1=25.7, title="İstanbul Üni. İlahiyat Fakültesi", sub="kurucu dekan, 1993", y=420),
    dict(type="kinetic", t0=26.0, t1=29.0, text="KAYNAĞINDAN\nÖĞRENDİ", y=420, size=140, style="black"),
    dict(type="kinetic", t0=29.3, t1=31.5, text="NEDEN TEPKİ?", y=420, size=160, style="red"),
    dict(type="kinetic", t0=34.2, t1=35.9, text="DİN KUR'AN'DAN\nÖĞRENİLİR", y=420, size=130),
    dict(type="kinetic", t0=36.0, t1=38.9, text="TARİKATTAN, ŞEYHTEN,\nHURAFEDEN DEĞİL", y=420, size=100, style="red"),
    dict(type="label", t0=39.1, t1=43.6, title="Ona göre", sub="pek çok kural dine sonradan eklendi", y=420),
    dict(type="kinetic", t0=43.8, t1=50.7, text="SEN OLSAN?", y=420, size=170, style="red"),
    dict(type="tagpair", t0=47.9, t1=50.7, tags=[("KIZARDIM", 760, 48.1), ("AÇIP BAKARDIM", 900, 49.6)]),
    dict(type="label", t0=51.0, t1=54.2, title="Kur'an-ı Kerim Meali", sub="sade Türkçe ile", y=420),
    dict(type="counter", t0=54.4, t1=57.3, **{"from": 1, "to": 120}, fmt="{}+ BASKI", dur=0.8, y=470, size=150),
    dict(type="label", t0=57.6, t1=62.8, title="1999", sub="radikal örgüt üyeleri itiraf etti", y=420),
    dict(type="stamp", t0=60.30, t1=62.8, text="SUİKAST PLANI", y=900, size=120, color=RED, rot=-6, fill=True),
    dict(type="label", t0=63.1, t1=66.8, title="2002: milletvekili", sub="sonra kendi partisini kurdu", y=420),
    dict(type="kinetic", t0=67.0, t1=69.8, text="\"DİNİ\nDEĞİŞTİRİYOR\"", y=420, size=140, style="red"),
    dict(type="kinetic", t0=69.9, t1=73.9, text="\"İLAHİYATÇI\nSİYASETE GİRMESİN\"", y=420, size=110, style="black"),
    dict(type="label", t0=74.2, t1=76.6, title="2016", sub="mide kanseri", y=420),
    dict(type="stamp", t0=76.80, t1=78.2, text="DOĞUM GÜNÜNDE", y=900, size=120, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=84.9, t1=87.7, text="KUR'AN'I AÇ,\nKENDİN OKU", y=420, size=140),
    dict(type="kinetic", t0=87.9, t1=DURATION + 1, text="DİNİ SAVUNDU MU?\nDEĞİŞTİRDİ Mİ?", y=420, size=120),
    dict(type="tagpair", t0=89.9, t1=DURATION + 1, tags=[("SAVUNDU", 760, 90.0), ("DEĞİŞTİRDİ", 900, 91.3)]),
    dict(type="cta", t0=92.9, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 6.3), (6.5, 10.3), (26.0, 31.5), (34.2, 38.9), (43.8, 50.7), (54.4, 57.3), (60.3, 61.5), (67.0, 73.9), (76.8, 78.2),
               (84.9, 87.7), (87.9, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 4.8, 8.5, 29.3, 36.0, 43.8, 60.3, 67.0, 84.9]
SHAKE = [4.8, 60.3]
FLASH = [(6.40, 0.06)]

MUSIC = [(0, 12.5, 3), (12.5, 29.2, 2), (29.2, 43.8, 2), (43.8, 50.9, 1), (50.9, 67.0, 2), (67.0, 74.1, 3), (74.1, 87.9, 1), (87.9, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.45), dict(name="hit", t=4.8, gain=0.3), dict(name="hit", t=60.3, gain=0.35),
       dict(name="pop", t=92.9, gain=0.3)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="yno", focus=(0.5, 0.25), zoom=1.08, lines=["İKİ TARAF DA", "ONA KIZDI"], y=960, size=128, style="white",
             stamp="DOKUZ YAŞINDA HAFIZ", stamp_y=1310, stamp_size=90, stamp_color=RED, stamp_rot=-5, bottom="Yaşar Nuri Öztürk", bottom_y=1450)
