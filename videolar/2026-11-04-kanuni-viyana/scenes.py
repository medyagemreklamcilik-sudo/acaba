"""Timeline for "Kanuni Viyana'yı alsaydı ne olurdu?" (narration seconds)."""

DURATION = 94.28
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "kanuni", "kanuni_yuz", "kanuni_genc", "ordu", "ordu2", "viyana_min", "meldeman", "cekilis",
    "viyana1683", "yeniceri", "sarlken", "luther"]}
IMAGES["kusatma"] = ("kusatma.jpg", (0.0, 0.1, 1.0, 1.0))   # üstteki renk kartını kes

FACES = {"kanuni": (0.55, 0.35), "kanuni_yuz": (0.4, 0.3), "kanuni_genc": (0.45, 0.25), "sarlken": (0.5, 0.3),
         "luther": (0.5, 0.25)}

# (anahtar, etiket, lon, lat, ölçek)
JOURNEY = [
    ("istanbul", "İSTANBUL", 28.97, 41.01, 40),
    ("viyana", "VİYANA", 16.37, 48.21, 56),
    ("almanya", "ALMANYA?", 11.58, 48.14, 46),
]


def J(t, stop, year, role, **kw):
    return dict(t=t, mode="journey", stop=stop, year=year, portrait="kanuni", rank="KANUNİ", role=role, **kw)


SCENES = [
    # kanca
    dict(t=0.00, img="meldeman", grade="dark", zoom=(1.35, 1.1), focus=(0.5, 0.5)),
    dict(t=2.30, img="viyana_min", grade="dark", zoom=(1.05, 1.25), focus=(0.4, 0.4), tr="glitch"),
    dict(t=3.86, img="kanuni_yuz", zoom=(1.0, 1.18), focus=(0.4, 0.3), tr="flash"),
    # sefer
    J(8.96, 0, "1529", "Viyana seferi"),
    J(11.40, 1, "1529", "Habsburg başkenti"),
    dict(t=14.32, img="ordu", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushup"),
    dict(t=17.48, img="ordu2", zoom=(1.05, 1.25), focus=(0.5, 0.55), tr="pushleft"),
    # kuşatma
    dict(t=21.90, img="meldeman", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=26.76, img="kusatma", zoom=(1.0, 1.2), focus=(0.5, 0.6), tr="bars"),
    dict(t=29.88, img="viyana_min", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    dict(t=33.16, mode="plate", bg="meldeman", tr="dip"),
    # kar, çekiliş
    dict(t=42.86, img="cekilis", grade="dark", zoom=(1.0, 1.2), focus=(0.4, 0.5), tr="flash"),
    # ikinci merak boşluğu
    dict(t=47.96, mode="plate", bg="kanuni_genc", tr="diag"),
    dict(t=52.22, img="sarlken", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushleft"),
    dict(t=56.04, img="luther", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="pushup"),
    dict(t=60.22, mode="plate", bg="luther", tr="dip"),
    # ya düşseydi
    J(65.92, 2, "", "önü açılırdı"),
    dict(t=69.66, img="sarlken", grade="dark", zoom=(1.2, 1.35), focus=(0.5, 0.3), tr="glitch"),
    dict(t=74.16, img="ordu", grade="dark", zoom=(1.2, 1.0), focus=(0.5, 0.5), tr="pushright"),
    # 1683
    dict(t=78.22, img="viyana1683", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=84.22, img="viyana1683", grade="dark", zoom=(1.3, 1.5), focus=(0.35, 0.7), tr="dip"),
    # son
    dict(t=87.62, mode="plate", bg="kanuni", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=3.8, lines=["VİYANA'YI", "YAĞMUR KURTARDI"], y=330, size=116),
    dict(type="stamp", t0=1.0, t1=3.8, text="ORDU DEĞİL", y=900, size=110, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=4.2, t1=8.9, text="KANUNİ\nALSAYDI?", y=380, size=140, style="red"),
    # --- sefer
    dict(type="kinetic", t0=14.6, t1=17.4, text="HAFTALARCA\nYAĞMUR", y=380, size=120, style="black"),
    dict(type="label", t0=17.7, t1=19.7, title="Kanuni'nin ordusu", sub="Süleymannâme minyatürü", y=420),
    dict(type="stamp", t0=19.84, t1=21.8, text="TOPLAR GERİDE KALDI", y=900, size=96, color=RED, rot=-6, fill=True),
    # --- kuşatma
    dict(type="label", t0=22.2, t1=24.2, title="Viyana, 1529", sub="Nikolaus Meldeman'ın çizimi", y=420),
    dict(type="stamp", t0=24.5, t1=26.6, text="BÜYÜK TOP YOK", y=900, size=110, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=27.0, t1=29.8, text="SURLARIN ALTINA\nTÜNEL", y=380, size=110, style="black"),
    dict(type="label", t0=30.1, t1=33.0, title="Viyana kuşatması", sub="Hünernâme minyatürü", y=420),
    dict(type="counter", t0=34.9, t1=42.8, **{"from": 0, "to": 20}, fmt="{} BİN", dur=0.5, y=440, size=150),
    dict(type="label", t0=35.3, t1=42.8, title="Viyana'daki askerler", sub="kaynaklara göre", y=560),
    dict(type="counter", t0=37.6, t1=42.8, **{"from": 0, "to": 100}, fmt="{} BİN+", dur=0.6, y=860, size=150),
    dict(type="label", t0=38.0, t1=42.8, title="Osmanlı ordusu", sub="tahmini", y=980),
    dict(type="stamp", t0=40.5, t1=42.8, text="ŞEHİR DÜŞMEDİ", y=270, size=110, color=RED, rot=-6, fill=True),
    # --- kar
    dict(type="kinetic", t0=43.0, t1=44.7, text="KAR", y=420, size=190, style="black"),
    dict(type="label", t0=44.9, t1=47.8, title="Ekim 1529", sub="kuşatma kalktı", y=420),
    # --- ikinci merak
    dict(type="kinetic", t0=48.1, t1=52.1, text="KİMİN İŞİNE\nYARADI?", y=700, size=140, style="red"),
    dict(type="label", t0=52.5, t1=55.9, title="Şarlken", sub="Kutsal Roma İmparatoru", y=420),
    dict(type="label", t0=56.3, t1=60.1, title="Martin Luther", sub="Protestanlığın kurucusu", y=420),
    dict(type="stamp", t0=58.4, t1=60.1, text="ANLAŞMAK ZORUNDA KALDI", y=900, size=88, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=60.3, t1=65.8, text="PROTESTANLIĞI\nOSMANLI MI\nKURTARDI?", y=620, size=120),
    dict(type="source", t0=61.2, t1=65.8, text="Stephen Fischer-Galati, Ottoman Imperialism and German Protestantism (1959)"),
    # --- ya düşseydi
    dict(type="stamp", t0=70.3, t1=74.0, text="HABSBURGLAR ÇÖKERDİ?", y=900, size=92, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=74.4, t1=78.1, text="KORUNAMAYACAK\nKADAR UZAK", y=380, size=110, style="black"),
    # --- 1683
    dict(type="counter", t0=78.3, t1=81.2, **{"from": 0, "to": 154}, fmt="{} YIL SONRA", dur=0.8, y=900, size=120),
    dict(type="label", t0=81.3, t1=84.1, title="Viyana, 1683", sub="ikinci kuşatma", y=420),
    dict(type="stamp", t0=84.6, t1=87.5, text="GERİ ÇEKİLİŞ", y=900, size=130, color=RED, rot=-6, fill=True),
    # --- son
    dict(type="kinetic", t0=87.62, t1=DURATION + 1, text="DAHA GÜÇLÜ MÜ,\nDAHA ERKEN Mİ\nÇÖKERDİ?", y=330, size=112),
    dict(type="tagpair", t0=88.4, t1=DURATION + 1, tags=[("DAHA GÜÇLÜ", 760, 90.2), ("ERKEN ÇÖKÜŞ", 900, 91.7)]),
    dict(type="cta", t0=93.3, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.8), (48.0, 52.1), (60.3, 65.8), (87.62, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 1.0, 4.2, 19.84, 24.5, 40.5, 43.0, 48.1, 70.3, 84.6]
SHAKE = [1.0, 19.84, 40.5, 70.3, 84.6]
FLASH = [(3.86, 0.12), (42.86, 0.12)]

MUSIC = [(0, 8.96, 3), (8.96, 21.9, 2), (21.9, 42.86, 3), (42.86, 47.96, 1), (47.96, 65.92, 2), (65.92, 78.22, 3),
         (78.22, 87.62, 3), (87.62, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=1.0, gain=0.35), dict(name="hit", t=19.84, gain=0.3),
       dict(name="hit", t=40.5, gain=0.35), dict(name="riser", t=48.1, gain=0.2, pre=True), dict(name="hit", t=70.3, gain=0.3),
       dict(name="hit", t=84.6, gain=0.35), dict(name="pop", t=93.3, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="viyana_min", grade="dark", focus=(0.5, 0.45), zoom=1.1, lines=["KANUNİ VİYANA'YI", "ALSAYDI?"], y=250,
             size=104, style="red", portraits=[("kanuni", 540, 760, 420)],
             stamp="YAĞMUR KURTARDI", stamp_y=1250, stamp_size=104, stamp_color=YELLOW, stamp_rot=-5,
             bottom="1529 · Avrupa'nın kaderi", bottom_y=1370)
