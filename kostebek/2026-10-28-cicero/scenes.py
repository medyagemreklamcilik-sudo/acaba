"""Köstebek · "Çiçero: Ankara'daki uşak casus" (narration seconds)."""

DURATION = 134.4
CAP_Y = 1235
CX = 507
ACCENT = (150, 255, 40)          # Köstebek neon yeşil
GREEN = ACCENT
RED = (255, 45, 45)

IMAGES = {
    "bazna": "bazna.jpg",
    "bazna_yasli": "bazna_yasli.jpg",
    "bazna_50ler": "bazna_50ler.jpg",
    "kitap": "kitap.jpg",
    "hugessen": ("hugessen.jpg", (0.04, 0.03, 0.96, 0.6)),
    "elcilik": "elcilik.jpg",
    "ankara": "ankara.jpg",
    "ankara2": "ankara2.jpg",
    "papen": ("papen.jpg", (0.0, 0.0, 1.0, 0.82)),
    "kamera": "kamera.jpg",
    "kasa": "kasa.jpg",
    "kasa2": "kasa2.jpg",
    "negatif": "negatif.jpg",
    "sterlin": "sterlin.jpg",
    "sandiklar": "sandiklar.jpg",
    "tahran": "tahran.jpg",
    "dday": "dday.jpg",
    "film_afis": "film_afis.jpg",
    "noir": "noir.jpg",
    "bank": "bank.jpg",
    "piyano": "piyano.jpg",
    "logo": "logo.jpg",
}

FACES = {"bazna": (0.5, 0.25), "bazna_yasli": (0.5, 0.35), "hugessen": (0.45, 0.35), "papen": (0.5, 0.3)}

SCENES = [
    # hook
    dict(t=0.00, img="piyano", grade="dark", zoom=(1.3, 1.05), focus=(0.5, 0.5)),
    dict(t=5.80, img="kasa2", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="glitch"),
    dict(t=8.88, img="bazna", zoom=(1.2, 1.05), focus=(0.5, 0.25), tr="flash"),
    dict(t=11.58, mode="plate", bg="noir", tr="dip"),
    # geçmişi
    dict(t=14.62, img="ankara", grade="bw", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushup"),
    dict(t=21.06, img="elcilik", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=25.32, img="hugessen", mode="card", maxw=720, maxh=820, tilt=2, tr="iris"),
    dict(t=28.82, img="negatif", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushup"),
    # kasa
    dict(t=34.58, img="kasa", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.45), tr="zoomblur"),
    dict(t=36.84, img="piyano", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="dip"),
    dict(t=40.10, img="kamera", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    # almanlar
    dict(t=44.44, img="ankara2", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="bars"),
    dict(t=46.36, img="papen", mode="card", maxw=680, maxh=900, tilt=-2, tr="pushup"),
    dict(t=48.84, img="negatif", zoom=(1.2, 1.4), focus=(0.4, 0.5), tr="glitch"),
    dict(t=53.62, img="tahran", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="pushup"),
    dict(t=60.58, img="dday", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="flash"),
    dict(t=66.16, mode="plate", bg="papen", tr="dip"),
    dict(t=69.64, img="papen", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="pushleft"),
    # sahte para
    dict(t=77.76, mode="plate", bg="sterlin", tr="dip"),
    dict(t=79.96, img="sterlin", zoom=(1.0, 1.25), focus=(0.4, 0.4), tr="pushup"),
    dict(t=85.76, img="sterlin", grade="dark", zoom=(1.4, 1.7), focus=(0.3, 0.3), tr="glitch"),
    dict(t=86.80, img="sandiklar", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    # sonrası
    dict(t=91.52, img="bazna_50ler", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="pushup"),
    dict(t=95.90, img="bank", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=99.92, img="bazna_yasli", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.35), tr="dip"),
    dict(t=106.44, img="kitap", mode="card", maxw=640, maxh=980, tilt=2, tr="pushup"),
    dict(t=108.32, img="bazna_yasli", grade="bw", zoom=(1.2, 1.4), focus=(0.5, 0.35), tr="dip"),
    # soru
    dict(t=111.96, img="film_afis", mode="card", maxw=660, maxh=980, tilt=-2, tr="iris"),
    dict(t=114.52, img="noir", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="dip"),
    dict(t=121.68, mode="split", tr="bars", imgs=[dict(img="bazna", focus=(0.5, 0.25)), dict(img="hugessen", focus=(0.45, 0.35))]),
    dict(t=127.56, mode="plate", bg="noir", tr="dip"),
    dict(t=133.0, img="logo", mode="card", maxw=820, maxh=820, tilt=0, tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- hook
    dict(type="typewriter", t0=0.0, t1=5.7, text="ANKARA · 1943", y=330, size=60, dur=1.0),
    dict(type="stamp", t0=1.2, t1=5.7, text="GİZLİ", y=520, size=130, color=RED, rot=-8),
    dict(type="kinetic", t0=5.80, t1=8.8, text="UŞAK KASAYI\nAÇIYORDU", y=380, size=110),
    dict(type="label", t0=9.0, t1=11.5, title="Elyesa Bazna", sub="1904–1970", y=420),
    dict(type="stamp", t0=13.60, t1=14.55, text="KOD ADI: ÇİÇERO", y=820, size=100, color=GREEN, rot=-6),
    # --- geçmişi
    dict(type="handwrite", t0=18.2, t1=21.0, text="mektupları okurken yakalandı", y=640, size=80, dur=0.9),
    dict(type="label", t0=21.2, t1=25.2, title="İngiliz Büyükelçiliği", sub="Ankara", y=420),
    dict(type="label", t0=25.4, t1=28.7, title="Sir Hughe Knatchbull-Hugessen", sub="İngiltere'nin Ankara büyükelçisi", y=420),
    dict(type="kinetic", t0=30.66, t1=34.5, text="GİZLİ BELGELERİ\nEVE GETİRİYORDU", y=380, size=100, style="red"),
    # --- kasa
    dict(type="handwrite", t0=35.48, t1=36.75, text="anahtarın kalıbı", y=420, size=110, dur=0.5),
    dict(type="tagpair", t0=36.9, t1=40.0, tags=[("UYURKEN", 380, 37.36), ("BANYODAYKEN", 560, 38.32), ("PİYANO ÇALARKEN", 740, 39.24)]),
    dict(type="kinetic", t0=42.34, t1=44.35, text="TEK TEK\nFOTOĞRAFLADI", y=380, size=110),
    # --- almanlar
    dict(type="typewriter", t0=44.44, t1=46.3, text="26 EKİM 1943", y=420, size=72, dur=0.6),
    dict(type="label", t0=46.5, t1=48.75, title="Alman Büyükelçiliği", sub="Büyükelçi Franz von Papen", y=420),
    dict(type="counter", t0=50.28, t1=52.15, **{"from": 0, "to": 20000}, fmt="£{}", dur=0.8, y=420, size=150),
    dict(type="handwrite", t0=50.0, t1=52.15, text="2 rulo film için", y=640, size=96, dur=0.5),
    dict(type="stamp", t0=52.96, t1=53.55, text="ÖDENDİ", y=820, size=140, color=GREEN, rot=-7),
    dict(type="label", t0=53.8, t1=60.5, title="Tahran Konferansı", sub="1943 · belgeleri Almanlara gitti", y=420),
    dict(type="typewriter", t0=63.56, t1=66.1, text="KOD ADI: OVERLORD", y=420, size=64, dur=0.9),
    dict(type="label", t0=63.0, t1=66.1, title="Normandiya çıkarması", sub="6 Haziran 1944", y=640),
    dict(type="kinetic", t0=66.16, t1=68.0, text="PEKİ ALMANLAR\nNE YAPTI?", y=600, size=104),
    dict(type="stamp", t0=68.62, t1=69.55, text="HİÇBİR ŞEY", y=900, size=120),
    dict(type="handwrite", t0=72.68, t1=77.7, text="fazla mükemmel…", y=420, size=110, dur=0.6),
    dict(type="kinetic", t0=75.26, t1=77.7, text="İNGİLİZ TUZAĞI MI?", y=640, size=96, style="red"),
    # --- sahte para
    dict(type="kinetic", t0=77.76, t1=79.9, text="ASIL TERS KÖŞE", y=600, size=120),
    dict(type="counter", t0=81.86, t1=85.7, **{"from": 0, "to": 300000}, fmt="£{}", dur=0.9, y=420, size=140),
    dict(type="stamp", t0=85.76, t1=86.75, text="SAHTE", y=700, size=170, rot=-10),
    dict(type="label", t0=87.0, t1=91.45, title="Bernhard Operasyonu", sub="Nazilerin sahte sterlin planı", y=420),
    # --- sonrası
    dict(type="handwrite", t0=94.1, t1=95.8, text="otel yaptıracaktı", y=640, size=100, dur=0.5),
    dict(type="label", t0=96.0, t1=99.8, title="İngiltere Merkez Bankası", sub="paraların sahte olduğunu tespit etti", y=420),
    dict(type="tagpair", t0=100.0, t1=106.35, tags=[("HAPİS", 380, 101.56), ("GECE BEKÇİSİ", 560, 102.68)]),
    dict(type="stamp", t0=106.66, t1=108.2, text="0 KURUŞ", y=420, size=130),
    dict(type="typewriter", t0=108.32, t1=111.9, text="MÜNİH · 1970", y=420, size=64, dur=0.6),
    # --- soru
    dict(type="label", t0=112.1, t1=114.45, title="5 Fingers (1952)", sub="Çiçero'nun hikâyesi Hollywood'da", y=420),
    dict(type="quote", t0=118.8, t1=121.6, y=760, by="İngiliz istihbarat şefine atfedilir",
         words=[("Çiçero", 118.92), ("zaten", 119.24), ("bizim", 119.74), ("kontrolümüzdeydi.", 120.10)]),
    dict(type="tagpair", t0=121.8, t1=127.5, tags=[("ÇİÇERO KANDIRDI?", 380, 122.0), ("İNGİLİZLER KANDIRDI?", 1060, 124.16)]),
    dict(type="vs", t0=122.5, t1=127.5),
    # --- final
    dict(type="kinetic", t0=127.56, t1=133.0, text="SENCE?", y=330, size=150),
    dict(type="tagpair", t0=128.4, t1=133.0, tags=[("EN BÜYÜK CASUS", 1000, 129.58), ("EN BÜYÜK ENAYİ", 1130, 131.76)]),
    dict(type="cta", t0=131.6, t1=133.0, y=1330),
]

NO_CAPTIONS = [(0.0, 5.7), (118.8, 121.6), (127.56, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [5.80, 13.60, 52.96, 68.62, 85.76, 106.66]
SHAKE = [85.76]
FLASH = [(8.88, 0.2), (60.58, 0.2)]

MUSIC = [(0, 14.62, 1), (14.62, 34.58, 1), (34.58, 53.62, 2), (53.62, 77.76, 2), (77.76, 91.52, 3),
         (91.52, 111.96, 1), (111.96, 127.56, 2), (127.56, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="heartbeat", t=0.0, gain=0.45), dict(name="type", t=0.0, gain=0.45), dict(name="hit", t=1.2, gain=0.4),
       dict(name="hit", t=13.60, gain=0.45), dict(name="type", t=44.44, gain=0.45), dict(name="hit", t=52.96, gain=0.4),
       dict(name="type", t=63.56, gain=0.45), dict(name="hit", t=68.62, gain=0.4), dict(name="impact", t=85.76, gain=0.6),
       dict(name="hit", t=106.66, gain=0.4), dict(name="type", t=108.32, gain=0.4), dict(name="pop", t=132.7, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.25) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="bazna", grade="dark", focus=(0.5, 0.25), zoom=1.15, lines=["ANKARA'DAKİ", "UŞAK CASUS"], y=760, size=118,
             stamp="KOD ADI: ÇİÇERO", stamp_y=1180, stamp_size=96, stamp_color=GREEN, stamp_rot=-6,
             bottom="sahte parayla ödendi", bottom_y=1420)
