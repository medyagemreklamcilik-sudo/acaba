"""Timeline for "Abdülaziz: intihar mı, cinayet mi?" (narration seconds)."""

DURATION = 84.35
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["aziz", "aziz2", "aziz3", "saray", "ic", "avni", "midhat", "midhat2", "hamid", "bogaz"]}
FACES = {"aziz": (0.5, 0.3), "aziz2": (0.5, 0.3), "aziz3": (0.5, 0.25), "avni": (0.5, 0.35), "midhat": (0.5, 0.4),
         "midhat2": (0.5, 0.2), "hamid": (0.5, 0.25)}

SCENES = [
    # kanca
    dict(t=0.00, img="aziz2", grade="dark", zoom=(1.35, 1.12), focus=(0.5, 0.3)),
    dict(t=5.14, mode="plate", bg="aziz2", tr="flash"),
    dict(t=10.46, img="aziz", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="dip"),
    # darbe
    dict(t=13.72, img="bogaz", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=16.44, img="avni", zoom=(1.0, 1.18), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=17.64, img="midhat", zoom=(1.0, 1.18), focus=(0.5, 0.4), tr="pushright"),
    dict(t=20.26, img="aziz3", grade="dark", zoom=(1.05, 1.3), focus=(0.5, 0.25), tr="glitch"),
    dict(t=22.74, img="saray", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="bars"),
    # 4 Haziran
    dict(t=25.40, img="ic", grade="dark", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="dip"),
    dict(t=32.98, mode="plate", bg="ic", tr="pushup"),
    dict(t=36.86, img="aziz2", grade="dark", zoom=(1.2, 1.45), focus=(0.5, 0.35), tr="zoomblur"),
    # sen olsan
    dict(t=41.74, mode="plate", bg="saray", tr="diag"),
    # Yıldız Mahkemesi
    dict(t=47.80, img="hamid", zoom=(1.0, 1.2), focus=(0.5, 0.25), tr="iris"),
    dict(t=51.92, mode="plate", bg="hamid", tr="pushup"),
    dict(t=54.98, img="midhat2", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="pushleft"),
    dict(t=58.34, img="midhat", grade="dark", zoom=(1.15, 1.35), focus=(0.5, 0.4), tr="glitch"),
    # iki hikâye
    dict(t=64.38, mode="plate", bg="aziz", tr="dip"),
    dict(t=70.50, img="aziz3", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="diag"),
    dict(t=74.54, img="ic", grade="dark", zoom=(1.3, 1.55), focus=(0.45, 0.55), tr="dip"),
    # son
    dict(t=80.72, mode="plate", bg="aziz2", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=5.0, lines=["TAHTTAN İNDİRİLDİ", "5 GÜN SONRA ÖLDÜ"], y=330, size=106),
    dict(type="stamp", t0=2.76, t1=5.0, text="BİLEKLERİ KESİK", y=900, size=104, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=5.2, t1=7.2, text="RESMİ RAPOR:\nİNTİHAR", y=560, size=140, style="black"),
    dict(type="kinetic", t0=7.28, t1=9.3, text="5 YIL SONRA\nMAHKEME:", y=560, size=130, style="black"),
    dict(type="kinetic", t0=9.42, t1=10.4, text="CİNAYET", y=620, size=190, style="red"),
    # --- darbe
    dict(type="label", t0=10.6, t1=13.6, title="Sultan Abdülaziz", sub="32. Osmanlı padişahı", y=420),
    dict(type="label", t0=13.9, t1=16.3, title="30 Mayıs 1876", sub="darbe gecesi", y=420),
    dict(type="label", t0=16.5, t1=17.5, title="Hüseyin Avni Paşa", sub="Serasker", y=420),
    dict(type="label", t0=17.7, t1=20.1, title="Midhat Paşa", sub="darbecilerden", y=420),
    dict(type="stamp", t0=20.80, t1=22.6, text="DARBE", y=900, size=160, color=RED, rot=-6, fill=True),
    dict(type="label", t0=22.9, t1=25.2, title="Çırağan sahili", sub="Feriye Sarayı'na kapatıldı", y=420),
    # --- 4 Haziran
    dict(type="label", t0=25.5, t1=28.2, title="4 Haziran 1876", sub="Feriye Sarayı", y=420),
    dict(type="kinetic", t0=28.26, t1=32.9, text="MAKAS", y=420, size=200, style="black"),
    dict(type="kinetic", t0=33.0, t1=36.7, text="DOKTORLARIN\nRAPORU", y=620, size=140, style="red"),
    dict(type="stamp", t0=40.12, t1=41.6, text="BAŞKA İZLER?", y=900, size=110, color=YELLOW, rot=-5, fill=True),
    # --- sen olsan
    dict(type="kinetic", t0=41.8, t1=47.6, text="SEN O DOKTOR\nOLSAN?", y=420, size=130, style="black"),
    dict(type="tagpair", t0=43.0, t1=47.6, tags=[("GÖRDÜĞÜNÜ YAZ", 800, 43.96), ("SÖYLENENİ YAZ", 950, 45.74)]),
    # --- mahkeme
    dict(type="label", t0=47.9, t1=51.8, title="İkinci Abdülhamid", sub="davayı 1881'de yeniden açtı", y=420),
    dict(type="kinetic", t0=52.0, t1=54.9, text="YILDIZ\nMAHKEMESİ", y=420, size=140, style="black"),
    dict(type="stamp", t0=53.68, t1=54.9, text="SUÇLU", y=950, size=160, color=RED, rot=-6, fill=True),
    dict(type="label", t0=55.1, t1=58.2, title="Midhat Paşa", sub="Taif'e sürüldü", y=420),
    dict(type="stamp", t0=57.64, t1=58.2, text="ÖLDÜRÜLDÜ", y=900, size=130, color=RED, rot=-6, fill=True),
    dict(type="stamp", t0=62.92, t1=64.2, text="BASKIYLA İTİRAF?", y=900, size=100, color=YELLOW, rot=-5, fill=True),
    # --- iki hikâye
    dict(type="kinetic", t0=64.6, t1=70.3, text="İKİ HİKÂYE", y=380, size=150, style="black"),
    dict(type="tagpair", t0=66.5, t1=70.3, tags=[("DARBECİLERİNKİ", 760, 66.74), ("DÜŞMANLARININKİ", 900, 68.04)]),
    dict(type="kinetic", t0=74.6, t1=80.5, text="O ODADA\nNE OLDU?", y=380, size=140, style="red"),
    # --- son
    dict(type="kinetic", t0=80.72, t1=DURATION + 1, text="İNTİHAR MI?\nCİNAYET Mİ?", y=420, size=130),
    dict(type="tagpair", t0=81.0, t1=DURATION + 1, tags=[("İNTİHAR", 760, 81.12), ("CİNAYET", 900, 82.36)]),
    dict(type="cta", t0=83.4, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(64.38, 70.3), (0.0, 5.0), (5.14, 10.3), (28.2, 28.9), (33.0, 36.7), (41.74, 47.6), (52.0, 54.9), (80.72, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 2.76, 6.40, 9.42, 20.80, 28.26, 33.0, 41.8, 53.68, 57.64, 74.6]
SHAKE = [2.76, 20.80, 53.68]
FLASH = [(5.14, 0.12), (32.98, 0.10)]

MUSIC = [(0, 10.46, 3), (10.46, 25.40, 2), (25.40, 41.74, 3), (41.74, 47.80, 1), (47.80, 64.38, 2), (64.38, 80.72, 3),
         (80.72, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=2.76, gain=0.4), dict(name="hit", t=9.42, gain=0.35),
       dict(name="hit", t=20.80, gain=0.3), dict(name="riser", t=25.40, gain=0.2, pre=True), dict(name="hit", t=53.68, gain=0.35),
       dict(name="pop", t=83.4, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="aziz2", focus=(0.5, 0.3), zoom=1.1, lines=["İNTİHAR MI,", "CİNAYET Mİ?"], y=250, size=124,
             style="yellow", stamp="5 GÜN SONRA ÖLÜ", stamp_y=1240, stamp_size=100, stamp_color=RED, stamp_rot=-6,
             bottom="Sultan Abdülaziz · 1876", bottom_y=1370)
