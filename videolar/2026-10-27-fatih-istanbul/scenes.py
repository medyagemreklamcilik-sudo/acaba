"""Timeline for "Fatih İstanbul'u alamasaydı ne olurdu?" (narration seconds)."""

DURATION = 135.6
CAP_Y = 1235
CX = 507

IMAGES = {
    "fatih": ("fatih.jpg", (0.06, 0.12, 0.94, 0.84)),
    "fatih2": ("fatih2.jpg", (0.0, 0.0, 0.5, 1.0)),
    "giris": ("giris.jpg", (0.05, 0.08, 0.95, 0.92)),
    "gemiler": ("gemiler.jpg", (0.15, 0.18, 0.96, 0.82)),
    "ordu": "ordu.jpg",
    "panorama": "panorama.jpg",
    "top": "top.jpg",
    "toplar": "toplar.jpg",
    "surlar": "surlar.jpg",
    "topkapi": "topkapi.jpg",
    "gedik": "gedik.jpg",
    "rumeli": "rumeli.jpg",
    "bayezid": "bayezid.jpg",
    "murad": "murad.jpg",
    "murad_min": "murad_min.jpg",
    "edirne": "edirne.jpg",
    "venedik": "venedik.jpg",
    "galata": "galata.jpg",
    "konstantin": ("konstantin.jpg", (0.17, 0.04, 0.83, 0.96)),
    "yavuz": "yavuz.jpg",
    "kanuni": "kanuni.jpg",
    "viyana": "viyana.jpg",
    "bessarion": "bessarion.jpg",
    "atina": "atina.jpg",
    "harita": "harita.jpg",
    "hacli": "hacli.jpg",
}

FACES = {"fatih": (0.45, 0.3), "fatih2": (0.5, 0.33), "bayezid": (0.5, 0.35), "murad": (0.5, 0.4),
         "yavuz": (0.5, 0.3), "kanuni": (0.5, 0.4), "bessarion": (0.5, 0.35), "konstantin": (0.5, 0.45)}

SCENES = [
    # hook
    dict(t=0.00, img="fatih", zoom=(1.35, 1.05), focus=(0.45, 0.3)),
    dict(t=2.52, img="giris", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="zoomblur"),
    dict(t=5.04, img="harita", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="pushup"),
    # Fatih 21
    dict(t=8.28, img="fatih2", zoom=(1.0, 1.15), focus=(0.5, 0.33), tr="iris"),
    dict(t=11.88, img="panorama", zoom=(1.0, 1.1), **{"from": (0.25, 0.5), "to": (0.7, 0.5)}, tr="pushleft"),
    dict(t=15.08, img="surlar", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=20.70, img="bayezid", mode="card", maxw=680, maxh=900, tilt=2, tr="pushleft"),
    dict(t=23.16, img="murad", mode="card", maxw=720, maxh=820, tilt=-2, tr="pushleft"),
    dict(t=25.50, img="murad_min", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="dip"),
    # Çandarlı
    dict(t=27.54, mode="plate", bg="murad_min", tr="pushup"),
    dict(t=32.06, img="fatih2", grade="bw", zoom=(1.1, 1.3), focus=(0.5, 0.33), tr="glitch"),
    # başarısız kuşatma
    dict(t=36.98, mode="plate", bg="panorama", tr="dip"),
    dict(t=40.68, img="gemiler", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.65, 0.5)}, tr="bars"),
    dict(t=42.58, img="top", zoom=(1.0, 1.15), focus=(0.6, 0.6), tr="pushup"),
    dict(t=44.16, img="toplar", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.6), tr="pushleft"),
    dict(t=45.30, mode="plate", bg="toplar", tr="dip"),
    dict(t=47.66, img="fatih2", grade="dark", zoom=(1.15, 1.35), focus=(0.5, 0.33), tr="glitch"),
    dict(t=50.94, img="ordu", zoom=(1.0, 1.12), **{"from": (0.25, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=53.58, mode="plate", bg="ordu", tr="dip"),
    dict(t=54.96, img="fatih", grade="bw", zoom=(1.0, 1.2), focus=(0.45, 0.3), tr="flash"),
    # Edirne, boğazlar
    dict(t=60.80, img="edirne", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="bars"),
    dict(t=62.66, img="harita", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="pushup"),
    dict(t=68.78, img="rumeli", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.65, 0.5)}, tr="pushleft"),
    dict(t=72.30, mode="split", tr="bars", imgs=[dict(img="venedik", focus=(0.5, 0.45)), dict(img="galata", focus=(0.5, 0.35))]),
    # Bizans
    dict(t=74.90, img="konstantin", mode="card", maxw=700, maxh=820, tilt=2, tr="iris"),
    dict(t=78.12, img="harita", grade="dark", zoom=(1.0, 1.15), focus=(0.45, 0.5), tr="pushup"),
    dict(t=81.06, img="surlar", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=84.06, img="topkapi", zoom=(1.0, 1.12), focus=(0.45, 0.5), tr="zoomblur"),
    # Avrupa ve sonraki fetihler
    dict(t=87.76, mode="plate", bg="giris", tr="dip"),
    dict(t=90.52, img="hacli", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushup"),
    dict(t=94.36, img="yavuz", mode="card", maxw=700, maxh=880, tilt=-2, tr="pushleft"),
    dict(t=95.98, img="kanuni", mode="card", maxw=720, maxh=860, tilt=2, tr="pushleft"),
    dict(t=97.30, img="viyana", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="flash"),
    dict(t=99.32, img="giris", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="pushup"),
    # Rönesans
    dict(t=105.68, mode="plate", bg="atina", tr="dip"),
    dict(t=106.94, img="bessarion", mode="card", maxw=700, maxh=900, tilt=-2, tr="pushleft"),
    dict(t=110.58, img="atina", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="bars"),
    dict(t=116.84, mode="split", tr="pushup", imgs=[dict(img="fatih", focus=(0.45, 0.3)), dict(img="atina", focus=(0.5, 0.45))]),
    # final
    dict(t=121.98, img="gedik", zoom=(1.2, 1.35), focus=(0.5, 0.32), tr="zoomblur"),
    dict(t=125.72, img="giris", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="flash"),
    dict(t=128.22, mode="plate", bg="fatih", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- hook
    dict(type="title", t0=0.0, t1=2.45, lines=["FATİH İSTANBUL'U", "ALAMASAYDI?"], y=330, size=104),
    dict(type="kinetic", t0=2.52, t1=4.95, text="DÜNYA\nİMPARATORLUĞU…", y=380, size=110),
    dict(type="kinetic", t0=5.04, t1=8.2, text="…YOK", y=330, size=150, style="red"),
    dict(type="handwrite", t0=5.68, t1=8.2, text="sıradan bir Balkan devleti", y=720, size=88, dur=0.9),
    dict(type="pencircle", t0=6.6, t1=8.2, cx=CX, cy=725, rx=440, ry=95, seed=3),
    # --- Fatih 21
    dict(type="label", t0=8.4, t1=11.8, title="Fatih Sultan Mehmed", sub="Gentile Bellini, 1480", y=420),
    dict(type="counter", t0=10.62, t1=11.85, **{"from": 1, "to": 21}, fmt="{} YAŞINDA", dur=0.6, y=760, size=130),
    dict(type="kinetic", t0=12.6, t1=15.0, text="BU KUŞATMA\nHER ŞEYİYDİ", y=380, size=110, style="black"),
    dict(type="kinetic", t0=17.38, t1=20.6, text="DAHA ÖNCE DE\nDENENDİ", y=380, size=110),
    dict(type="label", t0=20.8, t1=23.1, title="Yıldırım Bayezid", sub="1394–1402 kuşatması", y=420),
    dict(type="pencross", t0=22.42, t1=23.1, cx=CX, cy=760, r=200),
    dict(type="label", t0=23.25, t1=25.4, title="II. Murad", sub="1422 kuşatması", y=420),
    dict(type="pencross", t0=24.68, t1=25.4, cx=CX, cy=760, r=200),
    dict(type="kinetic", t0=25.88, t1=27.45, text="SARAY GÜVENMİYORDU", y=600, size=96, style="black"),
    # --- Çandarlı
    dict(type="handwrite", t0=27.6, t1=32.0, text="Çandarlı Halil Paşa", y=480, size=110, dur=0.9),
    dict(type="penline", t0=28.6, t1=32.0, x0=200, x1=820, y=560, dur=0.3, color=(255, 214, 10), width=8),
    dict(type="source", text="Veziriazam · portresi günümüze ulaşmadı", t0=27.9, t1=32.0),
    dict(type="stamp", t0=30.9, t1=32.0, text="KUŞATMAYA KARŞI", y=800, size=96),
    dict(type="kinetic", t0=32.06, t1=36.9, text="1446\nTAHTTAN İNDİRİLDİ", y=380, size=110, style="red"),
    dict(type="handwrite", t0=34.86, t1=36.9, text="arkasında o mu vardı?", y=1050, size=84, dur=0.8),
    # --- başarısız kuşatma
    dict(type="kinetic", t0=36.98, t1=37.8, text="ŞİMDİ DÜŞÜN", y=380, size=120),
    dict(type="counter", t0=37.86, t1=40.6, **{"from": 1, "to": 53}, fmt="{} GÜN", dur=0.8, y=600, size=170),
    dict(type="stamp", t0=39.44, t1=40.6, text="BAŞARISIZ", y=860, size=120, color=(255, 45, 45), rot=-6),
    dict(type="label", t0=40.8, t1=42.5, title="Gemiler karadan yürütüldü", sub="Fausto Zonaro", y=420),
    dict(type="kinetic", t0=42.58, t1=44.1, text="DEV TOPLAR", y=380, size=130),
    dict(type="kinetic", t0=44.16, t1=45.25, text="HAZİNE BOŞ", y=380, size=130, style="red"),
    dict(type="kinetic", t0=45.70, t1=47.6, text="SONUÇ:\nHİÇBİR ŞEY", y=620, size=130, style="black"),
    dict(type="kinetic", t0=48.28, t1=50.85, text="İLK KAYBEDEN:\nFATİH", y=380, size=110, style="red"),
    dict(type="tagpair", t0=51.0, t1=53.5, tags=[("ORDU ÖFKELİ", 380, 51.24), ("YENİÇERİ HUZURSUZ", 1060, 52.2)]),
    dict(type="handwrite", t0=53.6, t1=54.9, text="Çandarlı haklı çıktı", y=640, size=100, dur=0.7),
    dict(type="kinetic", t0=57.82, t1=59.35, text="TAHTIN SONU", y=380, size=130, style="red"),
    dict(type="kinetic", t0=59.40, t1=60.75, text="BELKİ DE\nHAYATI", y=640, size=120, style="black"),
    # --- Edirne / boğazlar
    dict(type="label", t0=60.9, t1=62.6, title="Edirne", sub="başkent olarak kalırdı", y=420),
    dict(type="kinetic", t0=65.38, t1=68.7, text="İKİYE BÖLÜNMÜŞ\nBİR DEVLET", y=380, size=110),
    dict(type="handwrite", t0=63.48, t1=68.7, text="ortada düşman şehri", y=1020, size=88, dur=0.9),
    dict(type="penarrow", t0=64.3, t1=68.7, src=(780, 960), dst=(560, 760), bend=-0.3, dur=0.4),
    dict(type="kinetic", t0=68.78, t1=72.2, text="BOĞAZ = TİCARET", y=380, size=110),
    dict(type="label", t0=69.0, t1=72.2, title="Rumeli Hisarı", sub="1452", y=560),
    dict(type="tagpair", t0=72.4, t1=74.85, tags=[("VENEDİK", 380, 72.74), ("CENEVİZ", 1060, 73.64)]),
    # --- Bizans
    dict(type="label", t0=75.0, t1=78.0, title="XI. Konstantinos", sub="son Bizans imparatoru", y=420),
    dict(type="kinetic", t0=75.28, t1=77.1, text="BİZANS\nKURTULUR MUYDU?", y=1000, size=90, style="black"),
    dict(type="stamp", t0=77.20, t1=78.05, text="HAYIR", y=1010, size=150, color=(255, 45, 45), rot=-5),
    dict(type="counter", t0=79.04, t1=81.0, **{"from": 0, "to": 50}, fmt="≈{} BİN KİŞİ", dur=0.8, y=600, size=120),
    dict(type="source", text="1453'te şehrin nüfusu · tahmini", t0=79.2, t1=81.0),
    dict(type="kinetic", t0=81.78, t1=84.0, text="İMPARATORLUK =\nSURLAR", y=380, size=110),
    dict(type="kinetic", t0=85.06, t1=87.7, text="YİNE KUŞATILACAKTI", y=380, size=96, style="black"),
    # --- Avrupa
    dict(type="kinetic", t0=87.76, t1=90.45, text="AMA HER YIL\nTARİHİ DEĞİŞTİRİRDİ", y=600, size=96),
    dict(type="label", t0=90.6, t1=94.3, title="Haçlı ordusu", sub="Varna, 1444 · Jan Matejko", y=420),
    dict(type="label", t0=94.45, t1=95.9, title="Yavuz Sultan Selim", sub="Mısır seferi 1516–17", y=420),
    dict(type="label", t0=96.05, t1=97.25, title="Kanuni Sultan Süleyman", sub="Viyana 1529", y=420),
    dict(type="kinetic", t0=97.58, t1=99.25, text="HİÇ\nYAŞANMAZDI?", y=600, size=130, style="red"),
    dict(type="kinetic", t0=102.98, t1=105.6, text="GÜÇ", y=380, size=120),
    dict(type="kinetic", t0=103.52, t1=105.6, text="PARA", y=540, size=120),
    dict(type="kinetic", t0=104.26, t1=105.6, text="ÖZGÜVEN", y=700, size=120),
    # --- Rönesans
    dict(type="kinetic", t0=105.68, t1=106.9, text="BİR DE ŞU VAR", y=600, size=120, style="black"),
    dict(type="label", t0=107.0, t1=110.5, title="Kardinal Bessarion", sub="Bizanslı alim · kitapları Venedik'te", y=420),
    dict(type="penarrow", t0=109.2, t1=110.5, src=(250, 1030), dst=(800, 900), bend=0.3, dur=0.4),
    dict(type="handwrite", t0=111.6, t1=113.0, text="Platon, Aristoteles...", y=420, size=90, dur=0.7),
    dict(type="kinetic", t0=115.20, t1=116.8, text="RÖNESANS", y=420, size=140),
    dict(type="source", text="Bazı tarihçilere göre · tartışmalı tez", t0=113.2, t1=116.8),
    dict(type="tagpair", t0=117.0, t1=121.9, tags=[("İSTANBUL", 380, 117.04), ("AVRUPA", 1060, 118.56)]),
    # --- final
    dict(type="kinetic", t0=121.98, t1=123.0, text="TEK BİR SABAH", y=380, size=120),
    dict(type="label", t0=123.06, t1=125.6, title="Topkapı surları", sub="1453'te gedik açılan yer", y=420),
    dict(type="pencircle", t0=124.54, t1=125.65, cx=CX, cy=880, rx=340, ry=250, seed=5),
    dict(type="counter", t0=125.72, t1=128.15, **{"from": 1, "to": 500}, fmt="{} YIL", dur=0.8, y=600, size=170),
    dict(type="kinetic", t0=128.22, t1=DURATION + 1, text="SENCE?", y=330, size=150),
    dict(type="tagpair", t0=129.3, t1=DURATION + 1, tags=[("YİNE İMPARATORLUK", 560, 130.58), ("BALKAN DEVLETİ", 860, 131.58)]),
    dict(type="cta", t0=133.6, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.45), (128.22, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 39.44, 45.70, 57.82, 77.20, 97.58, 115.20]
SHAKE = [0.0, 39.44, 77.20]
FLASH = [(0.0, 0.25), (54.96, 0.2)]

MUSIC = [(0, 8.28, 2), (8.28, 27.54, 1), (27.54, 36.98, 1), (36.98, 47.66, 3), (47.66, 60.8, 2),
         (60.8, 87.76, 1), (87.76, 105.68, 2), (105.68, 121.98, 1), (121.98, 128.22, 3), (128.22, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="impact", t=0.0, gain=0.9), dict(name="hit", t=5.04, gain=0.4),
       dict(name="impact", t=39.44, gain=0.55), dict(name="hit", t=45.70, gain=0.4),
       dict(name="hit", t=57.82, gain=0.4), dict(name="impact", t=77.20, gain=0.5),
       dict(name="hit", t=97.58, gain=0.4), dict(name="riser", t=121.98, gain=0.3, pre=True),
       dict(name="impact", t=121.98, gain=0.5), dict(name="pop", t=133.6, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.3) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}
