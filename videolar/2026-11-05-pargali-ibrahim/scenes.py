"""Timeline for "Pargalı İbrahim neden boğduruldu?" (narration seconds)."""

DURATION = 95.09
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["ibrahim", "ibrahim2", "kanuni", "kanuni2", "hurrem", "mustafa", "iran", "iran2", "saray",
                                  "topkapi", "topkapi2", "divan", "kosk"]}
FACES = {"ibrahim": (0.5, 0.45), "ibrahim2": (0.5, 0.42), "kanuni": (0.45, 0.4), "kanuni2": (0.5, 0.3), "hurrem": (0.5, 0.3),
         "mustafa": (0.5, 0.3)}

SCENES = [
    # kanca
    dict(t=0.00, img="kanuni", grade="dark", zoom=(1.3, 1.1), focus=(0.45, 0.4)),
    dict(t=4.86, img="ibrahim", zoom=(1.05, 1.25), focus=(0.5, 0.45), tr="flash"),
    dict(t=9.66, mode="plate", bg="ibrahim", tr="dip"),
    # kim
    dict(t=12.84, img="ibrahim2", zoom=(1.0, 1.18), focus=(0.5, 0.42), tr="pushup"),
    dict(t=16.70, img="kanuni2", zoom=(1.05, 1.2), focus=(0.5, 0.3), tr="pushleft"),
    dict(t=19.60, img="divan", zoom=(1.0, 1.25), focus=(0.5, 0.35), tr="zoomblur"),
    # çizgiyi aştı
    dict(t=26.52, img="iran", grade="dark", zoom=(1.05, 1.25), focus=(0.5, 0.45), tr="glitch"),
    dict(t=28.92, img="iran2", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushup"),
    dict(t=36.06, img="saray", zoom=(1.05, 1.25), focus=(0.5, 0.5), tr="bars"),
    dict(t=39.64, img="topkapi", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushright"),
    dict(t=43.90, img="kosk", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="diag"),
    dict(t=47.20, img="kanuni", grade="dark", zoom=(1.15, 1.35), focus=(0.45, 0.35), tr="dip"),
    # Hürrem
    dict(t=53.66, img="hurrem", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="iris"),
    dict(t=59.26, img="mustafa", zoom=(1.0, 1.18), focus=(0.5, 0.3), tr="pushleft"),
    # gece
    dict(t=62.38, img="topkapi2", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=67.70, mode="plate", bg="ibrahim", tr="flash"),
    dict(t=69.86, img="topkapi", grade="dark", zoom=(1.2, 1.45), focus=(0.4, 0.55), tr="dip"),
    # yemin
    dict(t=74.16, img="kanuni2", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="glitch"),
    dict(t=77.80, mode="plate", bg="kanuni2", tr="dip"),
    dict(t=79.56, img="kanuni", zoom=(1.2, 1.4), focus=(0.45, 0.35), tr="pushup"),
    # Makbul / Maktul
    dict(t=84.08, img="ibrahim", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="bars"),
    # son
    dict(t=90.18, mode="plate", bg="hurrem", tr="diag"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=4.7, lines=["EN YAKIN DOSTUNU", "BOĞDURTTU"], y=330, size=112),
    dict(type="stamp", t0=1.98, t1=4.7, text="İFTARDAN SONRA", y=900, size=104, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=6.0, t1=9.5, text="\"SENİ ASLA\nÖLDÜRMEYECEĞİM\"", y=380, size=104, style="black"),
    dict(type="kinetic", t0=9.8, t1=12.7, text="NEDEN\nÖLDÜ?", y=620, size=160, style="red"),
    # --- kim
    dict(type="label", t0=13.0, t1=16.5, title="Pargalı İbrahim", sub="Parga'dan getirilen köle", y=420),
    dict(type="label", t0=16.9, t1=19.4, title="Şehzade Süleyman", sub="en yakın arkadaşı", y=420),
    dict(type="stamp", t0=21.96, t1=26.3, text="DOĞRUDAN SADRAZAM", y=900, size=96, color=YELLOW, rot=-5, fill=True),
    dict(type="counter", t0=23.24, t1=26.3, **{"from": 0, "to": 13}, fmt="{} YIL", dur=0.6, y=440, size=150),
    # --- çizgiyi aştı
    dict(type="kinetic", t0=26.6, t1=28.8, text="ÇİZGİYİ\nAŞTI", y=420, size=150, style="black"),
    dict(type="label", t0=29.0, t1=30.6, title="İran seferi", sub="Süleymannâme minyatürü", y=420),
    dict(type="stamp", t0=30.78, t1=35.9, text="SERASKER SULTAN", y=900, size=104, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=32.7, t1=35.9, text="SULTAN =\nPADİŞAH", y=400, size=120, style="black"),
    dict(type="label", t0=36.2, t1=39.4, title="İbrahim Paşa Sarayı", sub="At Meydanı", y=420),
    dict(type="stamp", t0=37.04, t1=39.4, text="HEYKELLER", y=900, size=130, color=YELLOW, rot=-5, fill=True),
    dict(type="stamp", t0=41.7, t1=43.7, text="ŞAİR İDAM EDİLDİ", y=900, size=100, color=RED, rot=-6, fill=True),
    dict(type="label", t0=44.0, t1=47.0, title="Defterdar İskender Çelebi", sub="temsili minyatür", y=420),
    dict(type="stamp", t0=46.26, t1=47.0, text="ASILDI", y=900, size=140, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=51.84, t1=53.5, text="İHANET!", y=620, size=180, style="red"),
    # --- Hürrem
    dict(type="label", t0=55.8, t1=59.1, title="Hürrem Sultan", sub="Kanuni'nin eşi", y=420),
    dict(type="label", t0=59.3, t1=62.2, title="Şehzade Mustafa", sub="tahtın büyük varisi", y=420),
    # --- gece
    dict(type="label", t0=62.5, t1=67.5, title="15 Mart 1536", sub="Topkapı Sarayı, Ramazan", y=420),
    dict(type="stamp", t0=68.86, t1=69.8, text="BOĞULDU", y=900, size=150, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=71.6, t1=74.0, text="KAN İZLERİ", y=420, size=140, style="black"),
    # --- yemin
    dict(type="kinetic", t0=74.4, t1=77.7, text="YEMİN?", y=420, size=170, style="red"),
    dict(type="kinetic", t0=77.86, t1=79.5, text="\"UYKU ÖLÜM\nGİBİDİR\"", y=620, size=130),
    dict(type="source", t0=77.9, t1=79.5, text="rivayet; çağdaş kaynaklarda doğrulanmaz"),
    dict(type="stamp", t0=82.5, t1=84.0, text="SÖZ BOZULMADI?", y=900, size=100, color=YELLOW, rot=-5, fill=True),
    # --- makbul / maktul
    dict(type="tagpair", t0=84.3, t1=90.0, tags=[("MAKBUL", 760, 84.56), ("MAKTUL", 900, 88.44)]),
    # --- son
    dict(type="kinetic", t0=90.18, t1=DURATION + 1, text="HÜRREM Mİ?\nKİBRİ Mİ?", y=420, size=130),
    dict(type="tagpair", t0=90.6, t1=DURATION + 1, tags=[("HÜRREM", 760, 91.28), ("KİBİR", 900, 93.24)]),
    dict(type="cta", t0=94.1, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 4.7), (6.0, 9.5), (9.66, 12.7), (21.9, 23.2), (30.7, 32.6), (68.8, 69.8), (77.8, 79.5), (84.3, 90.0), (90.18, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 1.98, 3.68, 9.8, 21.96, 30.78, 41.7, 46.26, 51.84, 68.86, 74.4, 88.44]
SHAKE = [3.68, 30.78, 46.26, 68.86]
FLASH = [(4.86, 0.12), (67.70, 0.12)]

MUSIC = [(0, 9.66, 3), (9.66, 26.52, 2), (26.52, 53.66, 3), (53.66, 62.38, 2), (62.38, 74.16, 3), (74.16, 84.08, 2),
         (84.08, 90.18, 3), (90.18, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=3.68, gain=0.4), dict(name="hit", t=30.78, gain=0.3),
       dict(name="hit", t=46.26, gain=0.3), dict(name="riser", t=62.38, gain=0.2, pre=True), dict(name="hit", t=68.86, gain=0.4),
       dict(name="hit", t=88.44, gain=0.3), dict(name="pop", t=94.1, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="ibrahim", grade="dark", focus=(0.5, 0.45), zoom=1.08, lines=["EN YAKIN DOSTUNU", "BOĞDURTTU"], y=250,
             size=108, style="white", portraits=[("kanuni", 540, 800, 380)],
             stamp="MAKBUL → MAKTUL", stamp_y=1240, stamp_size=100, stamp_color=RED, stamp_rot=-6,
             bottom="Pargalı İbrahim · 1536", bottom_y=1370)
