"""Timeline for "Şems-i Tebrizi'ye ne oldu?" (narration seconds)."""

DURATION = 128.2
CAP_Y = 1235
CX = 507

IMAGES = {
    "konya": "konya.jpg",
    "konya2": "konya2.jpg",
    "turbe_eski": "turbe_eski.jpg",
    "turbe": "turbe.jpg",
    "mevlana": ("mevlana.jpg", (0.22, 0.14, 0.78, 0.66)),
    "mevlana_dans": "mevlana_dans.jpg",
    "menakib": "menakib.jpg",
    "divan": "divan.jpg",
    "dervis": "dervis.jpg",
    "sema": "sema.jpg",
    "sema2": "sema2.jpg",
    "medrese": "medrese.jpg",
    "sam": "sam.jpg",
    "sam2": "sam2.jpg",
    "sems_makam": "sems_makam.jpg",
    "sems_cami": "sems_cami.jpg",
    "hoy": "hoy.jpg",
}

FACES = {"mevlana": (0.5, 0.45), "dervis": (0.5, 0.2)}

SCENES = [
    # hook
    dict(t=0.00, img="konya2", grade="dark", zoom=(1.3, 1.05), focus=(0.5, 0.5)),
    dict(t=3.64, img="turbe_eski", grade="bw", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    # Şems kim
    dict(t=10.34, mode="plate", bg="mevlana_dans", tr="iris"),
    dict(t=12.62, img="dervis", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="pushup"),
    dict(t=17.22, img="mevlana", mode="card", maxw=720, maxh=920, tilt=2, tr="pushleft"),
    dict(t=20.22, img="mevlana_dans", zoom=(1.0, 1.2), focus=(0.4, 0.5), tr="zoomblur"),
    dict(t=25.08, img="medrese", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="pushup"),
    dict(t=28.00, img="sema", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="bars"),
    dict(t=31.06, img="medrese", grade="dark", zoom=(1.1, 1.25), focus=(0.5, 0.45), tr="pushleft"),
    dict(t=34.56, img="dervis", grade="dark", zoom=(1.2, 1.4), focus=(0.5, 0.25), tr="glitch"),
    # Şam, Kimya
    dict(t=38.50, img="sam", zoom=(1.0, 1.15), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=41.62, mode="plate", bg="sam2", tr="dip"),
    dict(t=45.40, img="turbe", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="pushleft"),
    # o gece
    dict(t=52.52, img="konya2", grade="dark", zoom=(1.1, 1.35), focus=(0.5, 0.5), tr="glitch"),
    dict(t=54.24, img="menakib", mode="card", maxw=700, maxh=960, tilt=-2, tr="iris"),
    dict(t=58.78, mode="plate", bg="menakib", tr="dip"),
    dict(t=62.10, mode="plate", bg="mevlana_dans", tr="flash"),
    dict(t=67.12, mode="plate", bg="turbe_eski", tr="dip"),
    # ama dikkat
    dict(t=70.58, img="menakib", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushup"),
    dict(t=75.40, img="mevlana", mode="card", maxw=720, maxh=920, tilt=-2, tr="pushleft"),
    dict(t=81.80, mode="plate", bg="sema2", tr="dip"),
    dict(t=84.82, img="sam", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="pushup"),
    dict(t=89.66, img="divan", zoom=(1.0, 1.2), focus=(0.5, 0.35), tr="bars"),
    # nerede
    dict(t=97.74, mode="plate", bg="konya", tr="dip"),
    dict(t=99.38, img="sems_cami", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="pushup"),
    dict(t=101.14, img="hoy", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=104.18, img="sems_makam", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    dict(t=110.54, mode="split", tr="bars", imgs=[dict(img="turbe_eski", focus=(0.5, 0.5)), dict(img="hoy", focus=(0.5, 0.35))]),
    dict(t=122.82, mode="plate", bg="mevlana", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- hook
    dict(type="title", t0=0.0, t1=3.55, lines=["8 ARALIK 1247", "KONYA"], y=330, size=116),
    dict(type="handwrite", t0=3.64, t1=8.0, text="Mevlana'nın en yakın dostu", y=420, size=86, dur=0.9),
    dict(type="kinetic", t0=8.10, t1=10.25, text="BİR DAHA\nGÖRÜLMEDİ", y=640, size=130, style="red"),
    # --- Şems
    dict(type="handwrite", t0=10.84, t1=12.55, text="Şems-i Tebrîzî", y=560, size=140, dur=0.7),
    dict(type="source", text="Gerçek portresi günümüze ulaşmadı", t0=11.0, t1=12.55),
    dict(type="tagpair", t0=12.7, t1=17.15, tags=[("GEZGİN", 380, 12.62), ("SERT DİLLİ", 1060, 13.66)]),
    dict(type="label", t0=17.3, t1=20.15, title="Mevlânâ Celâleddîn-i Rûmî", sub="1244'te Şems ile karşılaştı", y=420),
    dict(type="kinetic", t0=22.36, t1=25.0, text="ESKİ MEVLANA\nOLMADI", y=380, size=110),
    dict(type="kinetic", t0=25.08, t1=27.95, text="DERSİ BIRAKTI", y=380, size=110, style="black"),
    dict(type="kinetic", t0=26.64, t1=27.95, text="TALEBEYİ BIRAKTI", y=560, size=96, style="black"),
    dict(type="kinetic", t0=29.52, t1=30.95, text="SADECE ŞEMS", y=380, size=130),
    dict(type="tagpair", t0=31.2, t1=34.5, tags=[("ÂLİMLER ÖFKELİ", 380, 31.90), ("TALEBELER KISKANÇ", 1060, 33.0)]),
    dict(type="handwrite", t0=35.06, t1=38.4, text="hocamızı elimizden aldı", y=640, size=90, dur=0.8),
    # --- Şam, Kimya
    dict(type="label", t0=38.6, t1=41.55, title="Şam", sub="Şems Konya'yı terk etti", y=420),
    dict(type="handwrite", t0=42.64, t1=45.3, text="Sultan Veled onu geri getirdi", y=640, size=84, dur=0.9),
    dict(type="label", t0=45.5, t1=49.45, title="Kimyâ Hatun", sub="Mevlana'nın evlatlığı · Şems'in eşi", y=420),
    dict(type="kinetic", t0=50.68, t1=52.45, text="KISA SÜRE\nSONRA ÖLDÜ", y=640, size=110, style="black"),
    # --- o gece
    dict(type="kinetic", t0=52.52, t1=54.15, text="VE O GECE…", y=380, size=130, style="red"),
    dict(type="label", t0=54.35, t1=58.7, title="Menâkıbü'l-Ârifîn", sub="Eflâkî · 14. yüzyıl", y=420),
    dict(type="counter", t0=58.78, t1=61.0, **{"from": 1, "to": 7}, fmt="{} KİŞİ", dur=0.5, y=520, size=160),
    dict(type="stamp", t0=61.02, t1=62.05, text="BIÇAKLANDI", y=800, size=130),
    dict(type="handwrite", t0=63.76, t1=67.05, text="kendi oğlu mu?", y=420, size=110, dur=0.6),
    dict(type="label", t0=64.1, t1=67.05, title="Alâeddin Çelebi", sub="Mevlana'nın oğlu · iddia", y=640),
    dict(type="handwrite", t0=69.32, t1=70.5, text="bir kuyuya atıldı?", y=640, size=110, dur=0.6),
    # --- ama dikkat
    dict(type="kinetic", t0=70.72, t1=72.85, text="AMA DİKKAT", y=380, size=130, style="red"),
    dict(type="kinetic", t0=72.94, t1=75.3, text="70+ YIL SONRA\nYAZILDI", y=640, size=110, style="black"),
    dict(type="tagpair", t0=75.5, t1=81.7, tags=[("MEVLANA: CİNAYET YOK", 380, 75.40), ("SULTAN VELED: YOK", 1060, 77.86)]),
    dict(type="handwrite", t0=83.16, t1=84.75, text="sadece kayboldu", y=640, size=120, dur=0.6),
    dict(type="kinetic", t0=86.86, t1=88.7, text="DEFALARCA ŞAM'A", y=380, size=110),
    dict(type="stamp", t0=88.76, t1=89.6, text="BULAMADI", y=760, size=130),
    dict(type="label", t0=89.8, t1=97.65, title="Divan-ı Kebîr", sub="Dîvân-ı Şems-i Tebrîzî", y=420),
    dict(type="handwrite", t0=95.56, t1=97.65, text="Şems", y=900, size=200, dur=0.5),
    dict(type="pencircle", t0=96.0, t1=97.65, cx=CX, cy=900, rx=260, ry=150, seed=4),
    # --- nerede
    dict(type="kinetic", t0=97.74, t1=99.3, text="PEKİ ŞEMS\nNEREDE?", y=600, size=120),
    dict(type="label", t0=99.5, t1=101.05, title="Konya", sub="Şems-i Tebrîzî makamı", y=420),
    dict(type="label", t0=101.25, t1=104.1, title="Hoy, İran", sub="Şems minaresi ve türbesi", y=420),
    dict(type="handwrite", t0=107.26, t1=110.45, text="sessizce gitti mi?", y=640, size=100, dur=0.7),
    dict(type="kinetic", t0=111.10, t1=114.0, text="800 YILLIK SIR", y=960, size=100, style="black"),
    dict(type="tagpair", t0=114.2, t1=122.75, tags=[("ÖLDÜRÜLDÜ", 380, 117.84), ("GİTTİ", 1060, 121.94)]),
    # --- final
    dict(type="kinetic", t0=122.82, t1=DURATION + 1, text="SENCE?", y=330, size=150),
    dict(type="tagpair", t0=123.6, t1=DURATION + 1, tags=[("ÖLDÜRÜLDÜ", 560, 124.38), ("GİTTİ", 860, 125.72)]),
    dict(type="cta", t0=126.5, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.55), (122.82, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [8.10, 52.52, 61.02, 70.72, 88.76]
SHAKE = [61.02, 88.76]
FLASH = [(62.10, 0.2)]

MUSIC = [(0, 10.34, 1), (10.34, 25.08, 2), (25.08, 52.52, 1), (52.52, 70.58, 3), (70.58, 97.74, 2),
         (97.74, 110.54, 1), (110.54, 122.82, 2), (122.82, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="heartbeat", t=0.0, gain=0.45), dict(name="hit", t=8.10, gain=0.45), dict(name="impact", t=52.52, gain=0.55),
       dict(name="impact", t=61.02, gain=0.5), dict(name="hit", t=70.72, gain=0.4), dict(name="hit", t=88.76, gain=0.4),
       dict(name="riser", t=110.54, gain=0.25, pre=True), dict(name="pop", t=126.5, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.3) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="menakib", grade="dark", focus=(0.5, 0.4), zoom=1.15, lines=["ŞEMS NEREDE?"], y=280, size=130,
             portraits=[("mevlana", CX, 900, 460)],
             stamp="ÖLDÜRÜLDÜ MÜ?", stamp_y=1330, stamp_size=104, bottom="800 yıllık sır", bottom_y=1560)
