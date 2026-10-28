"""Timeline for "Osmanlı'da eşcinsellik: belgeler ne diyor?" (narration seconds)."""

DURATION = 138.9
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "tellak", "hamam", "hamam_gr", "tellak_foto", "istanbul", "istanbul2", "kocek", "kocek_levni", "kocek_gr",
    "kocek_gr2", "meyhane", "senlik", "mahbub", "mahbub2", "fazil_kitap", "kanunname", "akgunduz", "kanuni",
    "ebussuud", "ebussuud_kitap", "tanzimat", "tanzimat2", "cevdet", "cevdet_gr", "maruzat", "alipasa", "alipasa2",
    "londra", "meclis", "meclis2", "enderun", "kanun_cilt"]}

FACES = {"kanuni": (0.5, 0.3), "cevdet": (0.5, 0.25), "cevdet_gr": (0.5, 0.3), "alipasa": (0.5, 0.3),
         "alipasa2": (0.5, 0.2), "mahbub": (0.5, 0.2), "mahbub2": (0.5, 0.2), "ebussuud": (0.45, 0.3)}

SCENES = [
    # kanca: 1858 iddiası
    dict(t=0.00, img="tanzimat2", grade="dark", zoom=(1.35, 1.05), focus=(0.5, 0.5)),
    dict(t=6.40, img="londra", mode="card", maxw=860, maxh=700, tilt=-2, tr="zoomblur"),
    dict(t=9.02, img="kanun_cilt", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="glitch"),
    dict(t=11.84, mode="plate", bg="istanbul", tr="dip"),
    # Dellakname
    dict(t=14.02, img="istanbul", zoom=(1.25, 1.0), focus=(0.5, 0.5), tr="flash"),
    dict(t=16.36, img="tellak", zoom=(1.0, 1.15), focus=(0.5, 0.55), tr="pushup"),
    dict(t=19.66, img="hamam_gr", zoom=(1.0, 1.15), focus=(0.5, 0.6), tr="pushleft"),
    dict(t=22.94, img="hamam", zoom=(1.0, 1.2), focus=(0.4, 0.5), tr="bars"),
    dict(t=26.40, mode="plate", bg="hamam", tr="dip"),
    # terimler
    dict(t=30.50, img="meclis", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="iris"),
    dict(t=36.22, img="mahbub", zoom=(1.0, 1.12), focus=(0.5, 0.3), tr="pushleft"),
    dict(t=38.78, mode="plate", bg="mahbub2", tr="dip"),
    dict(t=42.44, img="meclis", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="pushup"),
    # edebiyat
    dict(t=48.12, img="meclis2", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="diag"),
    dict(t=54.58, img="enderun", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=57.64, img="fazil_kitap", mode="card", maxw=640, maxh=900, tilt=2, tr="zoomblur"),
    # köçekler
    dict(t=63.26, img="kocek", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="flash"),
    dict(t=65.58, img="kocek_levni", zoom=(1.0, 1.1), focus=(0.5, 0.35), tr="pushup"),
    dict(t=67.52, img="kocek_gr2", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=69.94, img="meyhane", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="glitch"),
    dict(t=71.64, img="kocek_gr", zoom=(1.0, 1.12), focus=(0.5, 0.45), tr="bars"),
    # devlet
    dict(t=74.56, img="kanuni", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="dip"),
    dict(t=77.12, img="akgunduz", mode="card", maxw=640, maxh=920, tilt=-2, tr="pushup"),
    dict(t=80.80, mode="plate", bg="akgunduz", tr="dip"),
    dict(t=86.48, img="ebussuud", zoom=(1.0, 1.15), focus=(0.45, 0.35), tr="flash"),
    dict(t=91.46, img="ebussuud_kitap", mode="card", maxw=640, maxh=920, tilt=2, tr="pushleft"),
    # 1858
    dict(t=94.48, img="tanzimat", grade="dark", zoom=(1.3, 1.0), focus=(0.5, 0.5), tr="glitch"),
    dict(t=105.60, mode="plate", bg="tanzimat", tr="dip"),
    # Cevdet Paşa
    dict(t=114.30, img="tanzimat2", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=115.88, img="cevdet", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="flash"),
    dict(t=118.80, mode="plate", bg="cevdet_gr", tr="dip"),
    dict(t=122.14, img="maruzat", mode="card", maxw=640, maxh=920, tilt=2, tr="pushup"),
    dict(t=125.88, img="alipasa", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="zoomblur"),
    dict(t=129.58, img="alipasa2", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.2), tr="pushleft"),
    # final
    dict(t=132.40, mode="plate", bg="hamam", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=3.85, lines=["\"OSMANLI", "SUÇ OLMAKTAN", "ÇIKARDI\""], y=330, size=104),
    dict(type="counter", t0=4.28, t1=6.3, **{"from": 1800, "to": 1858}, fmt="{}", dur=0.7, y=420, size=170),
    dict(type="label", t0=6.5, t1=8.9, title="İngiltere · 1967", sub="Sexual Offences Act", y=420),
    dict(type="stamp", t0=9.6, t1=11.75, text="DOĞRU MU?", y=820, size=130, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=11.84, t1=13.95, text="BELGELER\nNE DİYOR?", y=760, size=130),
    # --- Dellakname
    dict(type="title", t0=14.02, t1=16.3, lines=["1686 · İSTANBUL"], y=330, size=110),
    dict(type="label", t0=16.5, t1=19.5, title="Derviş İsmail", sub="Hamamcılar kethüdası", y=420),
    dict(type="counter", t0=20.48, t1=22.85, **{"from": 0, "to": 11}, fmt="{} TELLAK", dur=0.7, y=420, size=140),
    dict(type="handwrite", t0=23.0, t1=26.3, text="Dellâkname-i Dilküşâ", y=420, size=100, dur=0.7),
    dict(type="penline", t0=23.7, t1=26.3, x0=170, x1=850, y=490, dur=0.4, color=YELLOW, width=8),
    dict(type="quote", t0=26.4, t1=30.3, y=760, by="Dellâkname-i Dilküşâ · 1686",
         words=[("Ağzında", 26.45), ("akçe,", 26.7), ("kuruş,", 26.95), ("bahşiş", 27.2), ("lafı", 27.6), ("olmayub...", 28.0)]),
    dict(type="source", text="İstanbul Ansiklopedisi (R. E. Koçu) · Dellâknâme-i Dilküşâ", t0=16.5, t1=30.3),
    # --- terimler
    dict(type="tagpair", t0=33.2, t1=38.7, tags=[("GULÂMPÂRE", 380, 33.34), ("OĞLANCI", 520, 34.88), ("MAHBUB", 660, 37.92)]),
    dict(type="kinetic", t0=38.78, t1=42.35, text="BUGÜNKÜ ANLAMDA\nKİMLİK YOKTU", y=760, size=104, style="black"),
    dict(type="tagpair", t0=43.5, t1=48.0, tags=[("YETİŞKİN ERKEK", 380, 43.64), ("SAKALSIZ GENÇ", 520, 45.78)]),
    # --- edebiyat
    dict(type="kinetic", t0=48.12, t1=49.8, text="EDEBİYAT\nSAKLAMADI", y=380, size=110),
    dict(type="label", t0=49.9, t1=54.4, title="Deli Birader", sub="Dâfiü'l-gumûm · 16. yüzyıl", y=420),
    dict(type="label", t0=54.6, t1=57.5, title="Enderunlu Fazıl", sub="Saray okulu Enderun", y=420),
    dict(type="title", t0=57.64, t1=63.1, lines=["HUBANNAME · 1793"], y=330, size=100),
    # --- köçekler
    dict(type="kinetic", t0=63.4, t1=65.5, text="KÖÇEKLER", y=380, size=140),
    dict(type="label", t0=65.6, t1=67.4, title="Köçek", sub="Kadın kılığında dansçı", y=420),
    dict(type="stamp", t0=69.94, t1=71.55, text="KAVGA", y=820, size=140, color=RED, rot=-8, fill=True),
    dict(type="title", t0=71.64, t1=74.4, lines=["1837 · YASAK"], y=330, size=120, style="red"),
    # --- devlet
    dict(type="kinetic", t0=74.56, t1=76.4, text="DEVLET NE\nDİYORDU?", y=380, size=110),
    dict(type="label", t0=76.5, t1=80.7, title="Kanuni kanunnamesi · m.32-33", sub="Akgündüz, Osmanlı Kanunnameleri", y=420),
    dict(type="counter", t0=81.98, t1=83.95, **{"from": 0, "to": 300}, fmt="{} AKÇE", dur=0.5, y=420, size=140, sub="evli + zengin"),
    dict(type="counter", t0=84.0, t1=84.8, **{"from": 300, "to": 200}, fmt="{} AKÇE", dur=0.3, y=420, size=140, sub="orta hâlli"),
    dict(type="counter", t0=84.82, t1=86.4, **{"from": 200, "to": 100}, fmt="{} AKÇE", dur=0.3, y=420, size=140, sub="fakir"),
    dict(type="label", t0=86.6, t1=91.3, title="Şeyhülislam Ebussuud Efendi", sub="16. yüzyıl", y=420),
    dict(type="quote", t0=91.4, t1=94.4, y=760, by="Ebussuud fetvası · Veli-1, vr. 69b",
         words=[("Mu'tadı", 91.5), ("ise", 91.8), ("izn-i", 92.0), ("imam", 92.3), ("ile", 92.6), ("katlolunmak", 92.8), ("meşrudur.", 93.3)]),
    # --- 1858
    dict(type="title", t0=94.48, t1=96.8, lines=["1858"], y=380, size=170),
    dict(type="kinetic", t0=96.88, t1=101.1, text="LİVATAYA\nAYRI MADDE YOK", y=380, size=104),
    dict(type="label", t0=101.3, t1=105.5, title="1858 Ceza Kanunnamesi · m.202", sub="Sadece alenen yapılan fiiller", y=420),
    dict(type="stamp", t0=107.74, t1=109.4, text="SERBESTLİK DEĞİL", y=760, size=104, color=RED, rot=-6, fill=True),
    dict(type="tagpair", t0=110.3, t1=114.2, tags=[("IRZ", 380, 110.46), ("NAMUS", 520, 111.02)]),
    dict(type="source", text="Özsoy, Journal of Homosexuality 2020 · Avcı, SÜHFD 2018", t0=105.7, t1=114.2),
    # --- Cevdet Paşa
    dict(type="label", t0=116.0, t1=118.7, title="Ahmed Cevdet Paşa", sub="Tanzimat devlet adamı", y=420),
    dict(type="quote", t0=118.8, t1=122.0, y=760, by="Cevdet Paşa · Ma'rûzât",
         words=[("Zen-dostlar", 118.9), ("çoğalıp", 119.6), ("mahbublar", 120.48), ("azaldı.", 121.04)]),
    dict(type="tagpair", t0=122.3, t1=125.8, tags=[("KADIN SEVEN: ÇOĞALDI", 380, 122.38), ("OĞLAN SEVEN: AZALDI", 520, 124.12)]),
    dict(type="label", t0=126.0, t1=129.5, title="Sadrazam Âli Paşa", sub="Cevdet Paşa'nın iddiası", y=420),
    dict(type="handwrite", t0=130.3, t1=132.3, text="saklamaya çalışırdı", y=420, size=100, dur=0.6),
    dict(type="pencircle", t0=130.6, t1=132.3, cx=CX, cy=420, rx=380, ry=110, seed=4, color=RED),
    # --- final
    dict(type="kinetic", t0=132.4, t1=DURATION + 1, text="HOŞGÖRÜ MÜ,\nGÖZ YUMMAK MI?", y=330, size=100),
    dict(type="tagpair", t0=133.6, t1=DURATION + 1, tags=[("HOŞGÖRÜLÜYDÜ", 640, 134.08), ("GÖZ YUMUYORDU", 780, 136.26)]),
    dict(type="cta", t0=137.5, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.85), (26.4, 30.3), (91.4, 94.4), (118.8, 122.0), (132.4, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 4.28, 9.6, 14.02, 63.4, 71.64, 94.48, 107.74]
SHAKE = [9.6, 107.74]
FLASH = [(14.02, 0.15), (94.48, 0.15)]

MUSIC = [(0, 14.02, 3), (14.02, 48.12, 2), (48.12, 74.56, 2), (74.56, 94.48, 3), (94.48, 114.3, 3), (114.3, 132.4, 2),
         (132.4, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penline", "handwrite")]
SFX = [dict(name="impact", t=0.05, gain=0.55), dict(name="hit", t=9.6, gain=0.3), dict(name="impact", t=14.02, gain=0.4),
       dict(name="hit", t=71.64, gain=0.25), dict(name="riser", t=94.48, gain=0.2, pre=True), dict(name="impact", t=94.48, gain=0.45),
       dict(name="hit", t=107.74, gain=0.3), dict(name="pop", t=137.5, gain=0.35)]
SFX += [dict(name="pen", t=p, gain=0.2) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="hamam", grade="dark", focus=(0.4, 0.5), zoom=1.0, lines=["OSMANLI'DA", "EŞCİNSELLİK", "SERBEST MİYDİ?"],
             y=260, size=108, style="white", stamp="1858", stamp_y=1000, stamp_size=170, stamp_color=YELLOW, stamp_rot=-6,
             bottom="belgelerle", bottom_y=1330)
