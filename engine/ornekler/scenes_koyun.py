"""Timeline for "Osmanlı zamanında sen bir koyundun" (narration seconds)."""

DURATION = 119.3

IMAGES = {
    "koylu_fam": "koylu_2.jpg",
    "koylu_ox": "koylu2_5.jpg",
    "koylu_grp": "koylu_0.jpg",
    "koylu_cart": "koylu2_1.jpg",
    "koyun_man": "koyun_6.jpg",
    "koyun_flock": "koyun_3.jpg",
    "koyun_hill": "koyun_0.jpg",
    "padisah": "padisah_2.jpg",
    "padisah2": "padisah_6.jpg",
    "tarla": "tarla_0.jpg",
    "tarla2": "tarla_4.jpg",
    "tapu": "tapu_5.jpg",
    "tapu2": "tapu_1.jpg",
    "kahve": "kahve_4.jpg",
    "aile": "aile_3.jpg",
    "aile2": "aile_1.jpg",
    "kadin": "kadin_1.jpg",
    "kadin2": "kadin_6.jpg",
    "anayasa": "anayasa1924_2.jpg",
    "medeni": "medeni_0.jpg",
    "tahta": "tahta_5.jpg",
    "mektep": "milletmektebi_1.jpg",
    "nufus": "soyadi_6.jpg",
    "vekil": "kadinvekil_3.jpg",
    "vekil2": "kadinvekil_1.jpg",
    "oy": "sandik_1.jpg",
    "oy2": "sandik_0.jpg",
    "kalabalik": "cumhuriyet_6.jpg",
    "bayrak": "bayrak_3.jpg",
}

SCENES = [
    dict(t=0.00, mode="plate", bg="koyun_flock"),
    dict(t=2.94, img="koylu_fam", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.45), tr="zoomblur"),
    dict(t=5.58, img="koyun_man", zoom=(1.05, 1.2), focus=(0.4, 0.45), tr="pushup"),
    dict(t=8.84, mode="plate", bg="koyun_hill", tr="dip"),
    dict(t=17.54, mode="split", tr="pushup", imgs=[dict(img="padisah", focus=(0.5, 0.35)),
                                                    dict(img="koyun_flock", focus=(0.5, 0.5))]),
    dict(t=21.76, img="koyun_hill", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="dip"),
    dict(t=27.38, img="padisah2", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=31.26, img="koylu_ox", grade="dark", zoom=(1.0, 1.15), focus=(0.6, 0.45), tr="zoomblur"),
    dict(t=34.56, mode="plate", bg="koylu_grp", tr="dip"),
    dict(t=35.58, img="koylu_grp", zoom=(1.0, 1.1), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    # 1 — toprak
    dict(t=39.12, img="tarla", zoom=(1.0, 1.12), focus=(0.5, 0.45), tr="bars"),
    dict(t=40.94, img="tarla2", zoom=(1.0, 1.08), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushleft"),
    dict(t=43.28, img="tapu", mode="card", maxw=720, maxh=900, tilt=2, tr="pushup"),
    dict(t=49.48, img="koylu_cart", zoom=(1.0, 1.1), **{"from": (0.35, 0.5), "to": (0.6, 0.5)}, tr="zoomblur"),
    # 2 — okuma yazma
    dict(t=53.36, img="kahve", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.5), tr="iris"),
    dict(t=58.52, mode="plate", bg="kahve", tr="pushup"),
    # 3 — soyadı
    dict(t=64.26, img="aile", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="bars"),
    # 4 — kadın
    dict(t=68.72, img="kadin", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=71.90, img="kadin2", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="pushup"),
    # 1923
    dict(t=75.60, img="bayrak", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="flash"),
    dict(t=78.36, img="anayasa", mode="card", maxw=820, maxh=820, tilt=-2, tr="pushup"),
    dict(t=81.80, img="kalabalik", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.5), tr="dip"),
    dict(t=88.16, mode="split", tr="bars", imgs=[dict(img="koyun_flock", focus=(0.5, 0.5)),
                                                  dict(img="kalabalik", focus=(0.5, 0.5))]),
    dict(t=90.96, img="medeni", mode="card", maxw=640, maxh=900, tilt=2, tr="pushup"),
    dict(t=94.04, img="aile2", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="pushleft"),
    dict(t=97.96, img="tahta", zoom=(1.0, 1.15), focus=(0.55, 0.45), tr="zoomblur"),
    dict(t=99.16, img="mektep", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="pushleft"),
    dict(t=100.74, img="nufus", mode="card", maxw=860, maxh=800, tilt=-2, tr="pushup"),
    dict(t=102.86, img="vekil", zoom=(1.0, 1.1), focus=(0.5, 0.45), tr="bars"),
    dict(t=104.84, img="oy", zoom=(1.0, 1.12), focus=(0.4, 0.45), tr="pushleft"),
    dict(t=107.10, img="vekil2", grade="dark", zoom=(1.0, 1.08), focus=(0.5, 0.5), tr="dip"),
    dict(t=109.34, img="oy2", zoom=(1.0, 1.12), focus=(0.5, 0.45), tr="zoomblur"),
    dict(t=111.30, mode="plate", bg="koylu_grp", tr="dip"),
    dict(t=113.12, mode="split", tr="pushup", imgs=[dict(img="koylu_grp", focus=(0.5, 0.45)),
                                                     dict(img="kalabalik", focus=(0.5, 0.5))]),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

CAP_Y = 1235
CX = 507
OVERLAYS = [
    # --- hook
    dict(type="finger", t0=0.0, t1=2.9, y=930, size=720, taps=[1.26, 1.82]),
    dict(type="title", t0=0.0, t1=2.9, lines=["OSMANLI ZAMANINDA", "SEN BİR KOYUNDUN"], y=330, size=96),
    dict(type="finger", t0=2.94, t1=5.5, y=860, size=640, taps=[2.94, 4.30]),
    dict(type="kinetic", t0=2.94, t1=5.5, text="EVET, SEN", y=330, size=150),
    dict(type="kinetic", t0=6.80, t1=7.55, text="BİR KOYUNDUN", y=520, size=130),
    dict(type="stamp", t0=7.84, t1=8.8, text="ŞAKA YAPMIYORUM", y=700, size=110),
    # --- reaya
    dict(type="handwrite", t0=10.76, t1=17.5, text="Reaya", y=430, size=190, dur=0.7),
    dict(type="penline", t0=11.4, t1=17.5, x0=330, x1=750, y=545, dur=0.3, color=(255, 214, 10), width=9),
    dict(type="handwrite", t0=13.18, t1=17.5, text="رَعِيَّة", font="amiri", size=170, y=740, dur=0.8, rtl=True,
         color=(255, 255, 255)),
    dict(type="penarrow", t0=14.6, t1=17.5, src=(780, 700), dst=(700, 950), bend=-0.35, dur=0.35),
    dict(type="handwrite", t0=16.0, t1=17.5, text="= güdülen sürü", y=1010, size=110, dur=0.8),
    dict(type="pencircle", t0=16.9, t1=17.5, cx=730, cy=1010, rx=150, ry=70, seed=2),
    dict(type="tagpair", t0=17.6, t1=21.7, tags=[("PADİŞAH = ÇOBAN", 300, 17.6), ("SEN = SÜRÜ", 1060, 18.9)]),
    dict(type="penarrow", t0=19.64, t1=21.7, src=(820, 380), dst=(760, 1100), bend=0.18, dur=0.45),
    dict(type="quote", t0=24.4, t1=27.3, y=760, by="Buhârî, Ahkâm 1",
         words=[("Hepiniz", 24.52), ("çobansınız", 24.90), ("ve", 25.68), ("sürünüzden", 25.98), ("sorumlusunuz.", 26.68)]),
    dict(type="kinetic", t0=29.46, t1=31.2, text="ÇOBAN SENİ KORUR", y=560, size=110),
    dict(type="kinetic", t0=32.84, t1=34.5, text="HESAP\nSORAMAZDIN", y=520, size=130, style="red"),
    dict(type="finger", t0=34.56, t1=35.55, y=880, size=600, taps=[35.02]),
    dict(type="kinetic", t0=34.56, t1=35.55, text="ŞİMDİ BİR DÜŞÜN", y=330, size=110),
    dict(type="kinetic", t0=36.66, t1=39.0, text="KOYUN OLARAK\nHAYATIN", y=520, size=120, style="black"),
    # --- 1 toprak
    dict(type="item", n=1, title="TOPRAĞIN SENİN DEĞİLDİ", t0=39.2, t1=53.3),
    dict(type="source", text="Miri arazi · 1858 Arazi Kanunnamesi", t0=39.6, t1=53.3),
    dict(type="kinetic", t0=41.9, t1=43.2, text="SAHİBİ: DEVLET", y=700, size=120, style="black"),
    dict(type="label", t0=43.4, t1=46.2, title="Osmanlı tapu senedi", sub="Belge", y=420),
    dict(type="pencircle", t0=43.74, t1=49.4, cx=540, cy=830, rx=400, ry=470, seed=3, a0=-120),
    dict(type="handwrite", t0=47.1, t1=49.4, text="sadece kullanım hakkı!", y=1080, size=100, dur=0.9),
    dict(type="kinetic", t0=49.86, t1=50.7, text="SATAMAZDIN", y=640, size=140, style="red"),
    dict(type="pencross", t0=49.9, t1=50.75, cx=540, cy=640, r=220),
    dict(type="kinetic", t0=51.04, t1=53.3, text="3 YIL BOŞ =\nELİNDEN ALINIR", y=580, size=110, style="black"),
    # --- 2 okuma yazma
    dict(type="item", n=2, title="OKUMA YAZMA", t0=53.4, t1=64.2),
    dict(type="kinetic", t0=54.66, t1=58.45, text="BU ALTYAZIYI\nOKUYAMAZDIN", y=560, size=120),
    dict(type="pencircle", t0=55.66, t1=58.45, cx=CX, cy=CAP_Y, rx=470, ry=120, seed=4, a0=-170),
    dict(type="penarrow", t0=56.1, t1=58.45, src=(830, 900), dst=(700, 1090), bend=-0.3, dur=0.35),
    dict(type="people", t0=58.6, t1=64.2, y=760, gray_t=61.38, keep=4),
    dict(type="kinetic", t0=61.9, t1=64.2, text="10 KİŞİDEN 1'İ", y=1010, size=110),
    dict(type="source", text="1927 Genel Nüfus Sayımı · okuryazarlık %10,6", t0=59.3, t1=64.2),
    # --- 3 soyadı
    dict(type="item", n=3, title="SOYADIN YOKTU", t0=64.3, t1=68.65),
    dict(type="typewriter", t0=66.2, t1=68.65, text="TOPAL AHMET'İN OĞLU MEHMET", y=760, size=44, dur=1.5),
    # --- 4 kadın
    dict(type="item", n=4, title="KADINSAN…", t0=68.8, t1=75.5),
    dict(type="kinetic", t0=70.74, t1=71.85, text="TEK SÖZLE BOŞANMA", y=640, size=110, style="red"),
    dict(type="kinetic", t0=73.28, t1=75.5, text="ÇOK EŞLİLİK", y=640, size=130, style="black"),
    # --- 1923
    dict(type="counter", t0=76.08, t1=78.3, **{"from": 1900, "to": 1923}, dur=1.0, y=760, size=240),
    dict(type="label", t0=78.5, t1=81.7, title="1924 Anayasası", sub="Teşkilât-ı Esasiye Kanunu", y=420),
    dict(type="quote", t0=81.8, t1=88.05, y=760, by="1924 Anayasası · Madde 88",
         words=[("Türkiye", 81.80), ("ahalisine,", 82.52), ("din", 83.40), ("ve", 83.80), ("ırk", 84.04), ("farkı", 84.38),
                ("olmaksızın", 84.74), ("vatandaşlık", 85.50), ("itibarıyla", 86.20), ("Türk", 86.96), ("denir.", 87.28)]),
    dict(type="tagpair", t0=88.2, t1=90.9, tags=[("SÜRÜ", 300, 88.48), ("VATANDAŞ", 1060, 89.26)]),
    dict(type="pencross", t0=88.8, t1=90.9, cx=CX, cy=470, r=170),
    dict(type="pencircle", t0=89.3, t1=90.9, cx=255, cy=1060, rx=230, ry=80, seed=5, color=(255, 214, 10)),
    # --- Cumhuriyet
    dict(type="label", t0=91.1, t1=93.9, title="Türk Kanunu Medenisi", sub="1926", y=420),
    dict(type="handwrite", t0=92.88, t1=93.95, text="toprak artık senin!", y=1080, size=100, dur=0.8),
    dict(type="kinetic", t0=96.0, t1=97.9, text="EŞİT HAK", y=600, size=150),
    dict(type="label", t0=98.1, t1=99.1, title="Harf Devrimi", sub="1928", y=420),
    dict(type="handwrite", t0=99.48, t1=100.7, text="artık okuyabiliyorsun", y=560, size=96, dur=0.8),
    dict(type="pencircle", t0=99.6, t1=100.7, cx=CX, cy=CAP_Y, rx=440, ry=110, seed=6, color=(255, 214, 10)),
    dict(type="label", t0=100.9, t1=102.8, title="Soyadı Kanunu", sub="1934", y=420),
    dict(type="label", t0=103.0, t1=104.8, title="İlk kadın milletvekilleri", sub="1935", y=420),
    dict(type="kinetic", t0=104.84, t1=107.05, text="SEÇME & SEÇİLME", y=640, size=110, style="black"),
    dict(type="kinetic", t0=107.10, t1=109.3, text="TÜRKİYE 1934\nFRANSA 1944", y=560, size=120),
    dict(type="pencircle", t0=108.22, t1=109.3, cx=CX, cy=560, rx=400, ry=100, seed=7),
    dict(type="kinetic", t0=110.26, t1=111.25, text="ÇOBANINI KENDİN\nSEÇİYORDUN", y=560, size=100),
    # --- final
    dict(type="finger", t0=111.30, t1=113.05, y=880, size=640, taps=[111.96, 112.20]),
    dict(type="kinetic", t0=111.30, t1=113.05, text="SANA SORUYORUM", y=330, size=110),
    dict(type="tagpair", t0=113.2, t1=DURATION + 1, tags=[("OSMANLI", 300, 113.12), ("CUMHURİYET", 1060, 113.78)]),
    dict(type="kinetic", t0=116.52, t1=DURATION + 1, text="KURTULUŞ MU?", y=960, size=110),
    dict(type="cta", t0=117.58, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.9), (24.4, 27.3), (81.8, 88.05), (117.5, DURATION + 1)]
BLUR_CAPS = [(56.9, 58.5, 11)]


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 1.82, 4.30, 7.84, 33.14, 49.86, 76.08, 88.48, 108.22]
SHAKE = [0.0, 7.84]
FLASH = [(0.0, 0.25)]

MUSIC = [(0, 8.84, 2), (8.84, 34.56, 1), (34.56, 53.36, 2), (53.36, 75.6, 2), (75.6, 77.3, 0),
         (77.3, 111.3, 3), (111.3, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="impact", t=0.0, gain=0.9), dict(name="pop", t=2.94, gain=0.35), dict(name="pop", t=4.30, gain=0.35),
       dict(name="hit", t=7.84, gain=0.55), dict(name="heartbeat", t=31.5, gain=0.4), dict(name="pop", t=35.02, gain=0.3),
       dict(name="hit", t=49.86, gain=0.45), dict(name="glitch", t=56.9, gain=0.25),
       dict(name="type", t=66.2, gain=0.5), dict(name="riser", t=76.08, gain=0.35, pre=True), dict(name="impact", t=76.08, gain=0.55),
       dict(name="hit", t=88.48, gain=0.45), dict(name="pop", t=111.96, gain=0.3), dict(name="hit", t=116.52, gain=0.4),
       dict(name="pop", t=117.6, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.3) for p in _PEN]
SFX += [dict(name="pop", t=58.6 + 0.06 * k, gain=0.12) for k in range(10)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


if __name__ == "__main__":
    import json, sys
    json.dump(spec(), open(sys.argv[1], "w"))
