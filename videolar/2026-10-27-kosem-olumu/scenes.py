"""Timeline for "Kösem Sultan nasıl öldürüldü?" (narration seconds)."""

DURATION = 138.7
CAP_Y = 1235
CX = 507

IMAGES = {
    "kosem_a": "kosem_a.jpg",
    "kosem_b": "kosem_b.jpg",
    "kosem_c": "kosem_c.jpg",
    "kosem_d": "kosem_d.jpg",
    "ahmed": "ahmed1_0.jpg",
    "murad": "murad4_0.jpg",
    "ibrahim": "ibrahim_2.jpg",
    "mehmed4": "mehmed4_5.jpg",
    "turhan": ("turhan_6.jpg", (0.04, 0.03, 0.96, 0.9)),
    "olum": "kosemolum_2.jpg",
    "harem": "harem_6.jpg",
    "haremoda": "haremoda.jpg",
    "koridor": "koridor.jpg",
    "dolap": "dolap.jpg",
    "dolap2": "dolap2.jpg",
    "darussaade": "darussaade.jpg",
    "darussaade_grv": "darussaade_grv.jpg",
    "yeniceri": "yeniceri.jpg",
    "baltaci": "baltaci.jpg",
    "turbe": "turbe.jpg",
    "cinili": "cinili.jpg",
    "suleyman2": "suleyman2.jpg",
    "serbet": "serbet.jpg",
    "istanbul": "istanbul.jpg",
    "istanbul_grv": "istanbul_grv.jpg",
}

FACES = {"kosem_a": (0.5, 0.3), "kosem_b": (0.5, 0.3), "kosem_d": (0.45, 0.3), "ahmed": (0.5, 0.35),
         "murad": (0.5, 0.3), "ibrahim": (0.5, 0.25), "mehmed4": (0.5, 0.3), "turhan": (0.5, 0.35),
         "suleyman2": (0.5, 0.35), "darussaade": (0.5, 0.2)}

SCENES = [
    # hook: gece, dolap, etek
    dict(t=0.00, img="koridor", grade="dark", zoom=(1.3, 1.05), focus=(0.5, 0.55)),
    dict(t=3.02, img="kosem_d", grade="dark", zoom=(1.4, 1.6), focus=(0.45, 0.3), tr="glitch"),
    dict(t=6.12, img="dolap", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=8.98, img="dolap2", grade="dark", zoom=(1.3, 1.5), focus=(0.5, 0.85), tr="zoomblur"),
    # kim
    dict(t=12.16, img="kosem_b", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="iris"),
    dict(t=14.16, img="ahmed", mode="card", maxw=720, maxh=820, tilt=2, tr="pushleft"),
    dict(t=16.02, img="murad", mode="card", maxw=700, maxh=880, tilt=-2, tr="pushleft"),
    dict(t=17.38, img="ibrahim", mode="card", maxw=700, maxh=880, tilt=2, tr="pushleft"),
    dict(t=18.82, img="mehmed4", mode="card", maxw=720, maxh=860, tilt=-2, tr="pushleft"),
    dict(t=20.94, mode="plate", bg="kosem_a", tr="dip"),
    dict(t=22.82, img="kosem_c", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="bars"),
    # iki valide
    dict(t=29.00, img="mehmed4", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushup"),
    dict(t=32.70, mode="split", tr="bars", imgs=[dict(img="kosem_d", focus=(0.45, 0.3)), dict(img="turhan", focus=(0.5, 0.35))]),
    dict(t=40.90, img="turhan", mode="card", maxw=720, maxh=900, tilt=2, tr="iris"),
    dict(t=44.22, img="kosem_a", mode="card", maxw=700, maxh=900, tilt=-2, tr="pushleft"),
    dict(t=47.28, img="turhan", grade="dark", zoom=(1.2, 1.4), focus=(0.5, 0.35), tr="dip"),
    # plan
    dict(t=50.02, mode="plate", bg="istanbul_grv", tr="pushup"),
    dict(t=52.10, mode="split", tr="pushleft", imgs=[dict(img="mehmed4", focus=(0.5, 0.3)), dict(img="suleyman2", focus=(0.5, 0.35))]),
    dict(t=55.72, img="serbet", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="zoomblur"),
    dict(t=59.68, img="haremoda", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="dip"),
    dict(t=64.52, img="darussaade", mode="card", maxw=680, maxh=920, tilt=2, tr="pushup"),
    # o gece
    dict(t=70.52, img="koridor", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.55), tr="dip"),
    dict(t=72.44, img="baltaci", mode="card", grade="dark", maxw=640, maxh=920, tilt=-2, tr="pushleft"),
    dict(t=74.84, img="yeniceri", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushup"),
    dict(t=78.84, img="kosem_d", grade="dark", zoom=(1.5, 1.7), focus=(0.45, 0.3), tr="glitch"),
    dict(t=80.40, img="dolap", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="pushup"),
    dict(t=82.88, img="dolap2", zoom=(1.3, 1.5), focus=(0.5, 0.85), tr="flash"),
    dict(t=84.56, img="baltaci", grade="dark", zoom=(1.2, 1.4), focus=(0.5, 0.4), tr="glitch"),
    dict(t=86.30, img="kosem_b", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=89.76, img="kosem_b", zoom=(1.6, 1.8), focus=(0.4, 0.33), tr="zoomblur"),
    dict(t=93.50, img="harem", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    dict(t=95.80, img="olum", zoom=(1.1, 1.3), focus=(0.5, 0.55), tr="flash"),
    dict(t=101.24, img="koridor", grade="dark", zoom=(1.2, 1.0), focus=(0.5, 0.55), tr="glitch"),
    dict(t=104.06, img="olum", grade="bw", zoom=(1.3, 1.5), focus=(0.5, 0.6), tr="flash"),
    dict(t=106.88, img="kosem_d", grade="bw", zoom=(1.0, 1.2), focus=(0.45, 0.3), tr="dip"),
    # sonrası
    dict(t=112.82, img="istanbul", grade="dark", zoom=(1.1, 1.25), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=115.28, img="cinili", zoom=(1.0, 1.12), focus=(0.5, 0.45), tr="pushleft"),
    dict(t=117.48, img="turbe", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="bars"),
    # öbür yüzü
    dict(t=121.96, mode="plate", bg="kosem_d", tr="dip"),
    dict(t=124.08, img="serbet", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.45), tr="glitch"),
    dict(t=126.06, img="turhan", mode="card", maxw=700, maxh=880, tilt=-2, tr="pushleft"),
    dict(t=129.20, mode="split", tr="pushup", imgs=[dict(img="turhan", focus=(0.5, 0.35)), dict(img="kosem_d", focus=(0.45, 0.3))]),
    dict(t=132.32, mode="plate", bg="kosem_d", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- hook
    dict(type="title", t0=0.0, t1=2.95, lines=["2 EYLÜL 1651", "GECESİ…"], y=330, size=110),
    dict(type="kinetic", t0=3.02, t1=6.05, text="OSMANLI'NIN\nEN GÜÇLÜ KADINI", y=380, size=104),
    dict(type="handwrite", t0=6.64, t1=8.9, text="bir dolaba saklandı", y=420, size=96, dur=0.8),
    dict(type="kinetic", t0=9.02, t1=12.1, text="ETEĞİ GÖRÜNÜYORDU", y=380, size=96, style="red"),
    dict(type="pencircle", t0=9.56, t1=12.1, cx=CX, cy=1560, rx=430, ry=130, seed=2),
    dict(type="penarrow", t0=10.0, t1=12.1, src=(860, 1000), dst=(700, 1430), bend=-0.3, dur=0.35),
    # --- kim
    dict(type="label", t0=12.3, t1=14.1, title="Kösem Sultan", sub="Mahpeyker · 1589?–1651", y=420),
    dict(type="label", t0=14.25, t1=15.95, title="I. Ahmed", sub="eşi", y=420),
    dict(type="label", t0=16.1, t1=17.3, title="IV. Murad", sub="oğlu", y=420),
    dict(type="label", t0=17.45, t1=18.75, title="İbrahim", sub="oğlu", y=420),
    dict(type="label", t0=18.9, t1=20.85, title="IV. Mehmed", sub="torunu", y=420),
    dict(type="counter", t0=20.94, t1=22.75, **{"from": 1, "to": 6}, fmt="{} PADİŞAH", dur=0.6, y=640, size=150),
    dict(type="handwrite", t0=23.48, t1=28.9, text="Nâib-i Saltanat", y=420, size=110, dur=0.8),
    dict(type="kinetic", t0=25.10, t1=28.9, text="PADİŞAH ADINA\nDEVLETİ YÖNETTİ", y=640, size=96, style="black"),
    # --- iki valide
    dict(type="counter", t0=29.0, t1=31.2, **{"from": 1640, "to": 1648}, dur=0.6, y=420, size=150),
    dict(type="kinetic", t0=31.28, t1=32.65, text="6 YAŞINDA", y=640, size=140),
    dict(type="tagpair", t0=33.2, t1=40.8, tags=[("KÖSEM · TECRÜBE", 380, 35.34), ("TURHAN · GENÇ ANNE", 1060, 38.18)]),
    dict(type="vs", t0=33.9, t1=40.8),
    dict(type="label", t0=41.0, t1=44.1, title="Turhan Sultan", sub="IV. Mehmed'in annesi", y=420),
    dict(type="handwrite", t0=42.38, t1=44.1, text="kendi gelini!", y=1060, size=100, dur=0.6),
    dict(type="stamp", t0=45.26, t1=47.2, text="BÜYÜK VALİDE", y=1050, size=104, color=(255, 214, 10), rot=-6),
    dict(type="kinetic", t0=48.24, t1=49.95, text="SESSİZCE BEKLEDİ", y=380, size=104, style="black"),
    # --- plan
    dict(type="handwrite", t0=50.1, t1=52.0, text="Naîmâ'ya göre…", y=560, size=110, dur=0.7),
    dict(type="source", text="Târih-i Naîmâ · 18. yüzyıl başı", t0=50.3, t1=52.0),
    dict(type="tagpair", t0=52.2, t1=55.65, tags=[("IV. MEHMED", 380, 52.10), ("SÜLEYMAN", 1060, 54.36)]),
    dict(type="pencross", t0=52.6, t1=55.65, cx=CX, cy=520, r=200),
    dict(type="kinetic", t0=57.48, t1=59.6, text="ZEHİRLİ ŞERBET", y=380, size=120, style="red"),
    dict(type="stamp", t0=60.26, t1=64.45, text="İHANET", y=560, size=150),
    dict(type="handwrite", t0=62.0, t1=64.45, text="cariyesi Meleki Hatun", y=900, size=92, dur=0.8),
    dict(type="label", t0=64.6, t1=70.4, title="Süleyman Ağa", sub="Darüssaade Ağası · temsili", y=420),
    dict(type="kinetic", t0=68.16, t1=70.4, text="İKİ TARAFI\nKIŞKIRTTI?", y=1010, size=96, style="black"),
    # --- o gece
    dict(type="kinetic", t0=70.52, t1=72.35, text="O GECE", y=380, size=140),
    dict(type="kinetic", t0=72.44, t1=74.75, text="SİLAHLI HADIMLAR", y=330, size=96, style="red"),
    dict(type="handwrite", t0=76.92, t1=78.75, text="yeniçeriler mi?", y=420, size=100, dur=0.6),
    dict(type="kinetic", t0=79.08, t1=80.35, text="SESİ TANIDI", y=380, size=120, style="red"),
    dict(type="kinetic", t0=81.40, t1=82.8, text="DOLABA SAKLANDI", y=380, size=104),
    dict(type="pencircle", t0=83.12, t1=84.5, cx=CX, cy=1560, rx=430, ry=130, seed=4),
    dict(type="handwrite", t0=83.12, t1=84.5, text="eteği!", y=640, size=120, dur=0.4),
    dict(type="kinetic", t0=85.28, t1=86.25, text="SÜRÜKLENDİ", y=380, size=130, style="red"),
    dict(type="kinetic", t0=86.30, t1=88.6, text="ALTIN TEKLİF ETTİ", y=380, size=104),
    dict(type="pencross", t0=88.66, t1=89.7, cx=CX, cy=380, r=170),
    dict(type="label", t0=89.9, t1=93.4, title="Küpeleri koparıldı", sub="I. Ahmed'in hediyesi", y=420),
    dict(type="handwrite", t0=93.50, t1=95.7, text="perde ipi", y=640, size=130, dur=0.6),
    dict(type="kinetic", t0=96.58, t1=97.9, text="PARMAĞINI ISIRDI", y=380, size=104, style="red"),
    dict(type="kinetic", t0=99.96, t1=101.2, text="ÖLDÜ SANDILAR", y=380, size=110, style="black"),
    dict(type="stamp", t0=101.86, t1=104.0, text="AYILDI", y=640, size=150),
    dict(type="kinetic", t0=104.06, t1=106.8, text="YAKALANDI", y=380, size=130, style="red"),
    dict(type="kinetic", t0=109.04, t1=112.75, text="KENDİ GELİNİNİN\nADAMLARI", y=380, size=104, style="black"),
    # --- sonrası
    dict(type="counter", t0=113.56, t1=115.2, **{"from": 1, "to": 3}, fmt="{} GÜN YAS", dur=0.5, y=420, size=140),
    dict(type="label", t0=115.4, t1=117.4, title="Çinili Camii", sub="Kösem'in yaptırdığı cami, 1640", y=420),
    dict(type="label", t0=117.6, t1=121.9, title="I. Ahmed Türbesi", sub="Kösem burada yatıyor", y=420),
    dict(type="handwrite", t0=117.96, t1=121.9, text="Vâlide-i Maktûle", y=760, size=110, dur=0.8),
    # --- öbür yüzü
    dict(type="kinetic", t0=121.96, t1=124.0, text="AMA İŞİN\nÖBÜR YÜZÜ", y=600, size=110),
    dict(type="handwrite", t0=125.60, t1=126.0, text="Naîmâ", y=420, size=120, dur=0.3),
    dict(type="label", t0=126.2, t1=129.1, title="Turhan Sultan", sub="torunu III. Ahmed tahttayken yazıldı", y=420),
    dict(type="kinetic", t0=130.30, t1=132.25, text="KAZANANLARIN\nHİKAYESİ", y=380, size=104, style="black"),
    # --- final
    dict(type="kinetic", t0=132.32, t1=DURATION + 1, text="SENCE?", y=330, size=150),
    dict(type="tagpair", t0=133.2, t1=DURATION + 1, tags=[("KURBAN", 560, 133.42), ("KAYBEDEN OYUNCU", 860, 135.36)]),
    dict(type="cta", t0=137.1, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.95), (132.32, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [3.02, 45.26, 57.48, 60.26, 85.28, 101.86, 104.06]
SHAKE = [3.02, 85.28, 104.06]
FLASH = [(82.88, 0.2), (95.80, 0.2)]

MUSIC = [(0, 12.16, 1), (12.16, 29.0, 2), (29.0, 50.02, 1), (50.02, 70.52, 2), (70.52, 106.88, 3),
         (106.88, 112.82, 0), (112.82, 121.96, 1), (121.96, 132.32, 2), (132.32, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="heartbeat", t=0.0, gain=0.5), dict(name="impact", t=3.02, gain=0.7), dict(name="hit", t=9.02, gain=0.4),
       dict(name="hit", t=45.26, gain=0.35), dict(name="hit", t=60.26, gain=0.45), dict(name="heartbeat", t=70.52, gain=0.4),
       dict(name="impact", t=85.28, gain=0.5), dict(name="hit", t=101.86, gain=0.4), dict(name="impact", t=104.06, gain=0.55),
       dict(name="riser", t=121.96, gain=0.25, pre=True), dict(name="pop", t=137.1, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.3) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(imgs=[dict(img="kosem_d", focus=(0.45, 0.3)), dict(img="turhan", focus=(0.5, 0.42))],
             lines=["KÖSEM'İ KİM", "ÖLDÜRDÜ?"], y=250, size=112, style="red",
             marks=[dict(type="vs")], stamp="GELİNİ Mİ?", stamp_y=1700, stamp_size=100,
             stamp_color=(255, 214, 10), stamp_rot=-5)
