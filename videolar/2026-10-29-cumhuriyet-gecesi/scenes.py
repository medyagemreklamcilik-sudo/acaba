"""Timeline for "29 Ekim 1923 gecesi Ankara'da ne oldu?" (narration seconds)."""

DURATION = 120.9
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "cankaya", "sofra", "sofra2", "ismet", "mk_ismet", "fethi", "kazim", "kemalettin", "latife", "hakimiyet", "ileri",
    "resimli", "meclis", "meclis_kalabalik", "ankara", "mk1923", "mk_portre", "rauf", "kalamis", "tevhid", "rauf_eski",
    "meclis_ic", "mk_dark"]}

FACES = {"ismet": (0.5, 0.25), "fethi": (0.5, 0.3), "kazim": (0.5, 0.3), "kemalettin": (0.5, 0.3), "mk1923": (0.5, 0.25),
         "mk_portre": (0.5, 0.35), "rauf": (0.5, 0.3), "rauf_eski": (0.5, 0.3), "mk_dark": (0.45, 0.3), "latife": (0.4, 0.2)}

SCENES = [
    # kanca: Çankaya, 28 Ekim akşamı
    dict(t=0.00, img="cankaya", grade="dark", zoom=(1.4, 1.05), focus=(0.5, 0.45)),
    dict(t=4.48, img="sofra", zoom=(1.0, 1.2), focus=(0.5, 0.55), tr="dip"),
    dict(t=7.34, img="ankara", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    # kriz
    dict(t=11.44, img="meclis", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    dict(t=14.98, img="fethi", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushleft"),
    dict(t=17.46, img="meclis_ic", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="bars"),
    # sofradakiler
    dict(t=22.74, mode="grid", bg="sofra", tr="iris",
         tiles=[dict(img="ismet", at=23.18, name="İsmet Paşa", focus=(0.5, 0.25)), dict(img="fethi", at=24.32, name="Fethi Bey", focus=(0.5, 0.3)), dict(img="kazim", at=25.24, name="Kâzım Paşa", focus=(0.5, 0.3)), dict(img="kemalettin", at=26.38, name="Kemalettin Sami", focus=(0.5, 0.3))]),
    dict(t=29.10, img="latife", zoom=(1.0, 1.15), focus=(0.4, 0.25), tr="pushup"),
    dict(t=32.10, img="sofra2", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.55), tr="dip"),
    # cümle
    dict(t=34.56, img="mk1923", zoom=(1.0, 1.18), focus=(0.5, 0.25), tr="pushleft"),
    dict(t=37.40, mode="plate", bg="mk1923", tr="flash"),
    dict(t=40.00, img="sofra", grade="dark", zoom=(1.2, 1.0), focus=(0.5, 0.55), tr="pushup"),
    dict(t=45.24, img="mk_ismet", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="zoomblur"),
    # gece yazılan anayasa
    dict(t=48.30, img="cankaya", grade="dark", zoom=(1.0, 1.3), focus=(0.5, 0.45), tr="dip"),
    dict(t=52.64, mode="plate", bg="cankaya", tr="dip"),
    # hastalık
    dict(t=58.42, img="mk_dark", grade="dark", zoom=(1.0, 1.15), focus=(0.45, 0.3), tr="pushleft"),
    # 29 Ekim
    dict(t=66.08, img="meclis_kalabalik", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    dict(t=69.44, img="meclis", grade="dark", zoom=(1.2, 1.0), focus=(0.5, 0.5), tr="pushup"),
    dict(t=71.88, mode="plate", bg="meclis", tr="glitch"),
    dict(t=75.14, img="meclis_ic", zoom=(1.0, 1.2), focus=(0.5, 0.55), tr="flash"),
    dict(t=78.62, img="mk_portre", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=84.34, img="hakimiyet", mode="card", maxw=740, maxh=1000, tilt=-2, tr="pushup"),
    dict(t=88.06, img="ileri", mode="card", maxw=740, maxh=1000, tilt=2, tr="flash"),
    # İstanbul, Rauf Bey
    dict(t=90.38, img="kalamis", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="dip"),
    dict(t=92.96, img="rauf", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushup"),
    dict(t=98.20, mode="plate", bg="rauf_eski", tr="dip"),
    dict(t=100.40, img="tevhid", mode="card", maxw=740, maxh=1000, tilt=-2, tr="pushleft"),
    dict(t=106.08, mode="split", tr="bars", imgs=[dict(img="mk1923", focus=(0.5, 0.2)), dict(img="rauf_eski", focus=(0.5, 0.25))]),
    # final
    dict(t=113.18, mode="plate", bg="meclis", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=4.4, lines=["28 EKİM 1923"], y=330, size=130),
    dict(type="label", t0=1.2, t1=4.4, title="Çankaya Köşkü", sub="Ankara · akşam", y=520),
    dict(type="kinetic", t0=7.34, t1=11.3, text="TARİH O GECE\nDEĞİŞTİ", y=380, size=110),
    # --- kriz
    dict(type="stamp", t0=12.62, t1=14.9, text="HÜKÜMET YOK", y=820, size=130, color=RED, rot=-7, fill=True),
    dict(type="label", t0=15.0, t1=17.3, title="Ali Fethi Bey", sub="27 Ekim · istifa", y=420),
    dict(type="kinetic", t0=20.02, t1=22.6, text="KİMSE\nİSTEMİYOR", y=380, size=120, style="red"),
    # --- sofradakiler
    dict(type="label", t0=29.2, t1=32.0, title="Latife Hanım", sub="Ev sahibi", y=420),
    dict(type="kinetic", t0=32.1, t1=34.4, text="HÜKÜMET KRİZİ", y=380, size=110, style="black"),
    # --- cümle
    dict(type="label", t0=34.7, t1=37.3, title="Mustafa Kemal Paşa", sub="28 Ekim 1923 akşamı", y=420),
    dict(type="quote", t0=37.4, t1=39.9, y=760, by="Nutuk",
         words=[("Yarın", 37.5), ("Cumhuriyet'i", 37.78), ("ilan", 38.5), ("edeceğiz.", 38.88)]),
    dict(type="kinetic", t0=45.24, t1=48.2, text="UYUMADILAR", y=380, size=140),
    # --- anayasa
    dict(type="handwrite", t0=49.08, t1=52.5, text="1921 Anayasası", y=420, size=120, dur=0.6),
    dict(type="penline", t0=49.8, t1=52.5, x0=200, x1=820, y=500, dur=0.4, color=YELLOW, width=8),
    dict(type="typewriter", t0=55.4, t1=58.3, text="HÜKÛMET ŞEKLİ CUMHURİYETTİR", y=760, size=46, dur=1.4),
    dict(type="label", t0=52.7, t1=55.3, title="Teşkilât-ı Esasiye Kanunu", sub="Madde 1 · değişiklik", y=420),
    # --- hastalık
    dict(type="tagpair", t0=61.9, t1=65.9, tags=[("AĞIR SOĞUK ALGINLIĞI", 380, 62.38), ("DİŞ AĞRISI", 520, 64.44)]),
    # --- 29 Ekim
    dict(type="title", t0=66.08, t1=69.3, lines=["29 EKİM 1923"], y=330, size=130),
    dict(type="counter", t0=69.68, t1=71.8, **{"from": 12, "to": 18}, fmt="SAAT {}.00", dur=0.6, y=420, size=130),
    dict(type="counter", t0=72.32, t1=75.0, **{"from": 18, "to": 20}, fmt="SAAT {}.30", dur=0.5, y=420, size=150),
    dict(type="stamp", t0=73.78, t1=75.0, text="KABUL", y=820, size=160, color=YELLOW, rot=-6, fill=True),
    dict(type="kinetic", t0=77.3, t1=78.5, text="YAŞASIN\nCUMHURİYET!", y=380, size=120, style="red"),
    dict(type="counter", t0=81.66, t1=84.2, **{"from": 0, "to": 158}, fmt="{} OY", dur=0.8, y=420, size=170),
    dict(type="label", t0=84.4, t1=87.9, title="İlk Cumhurbaşkanı", sub="Oybirliğiyle · saat 20.45", y=420),
    dict(type="kinetic", t0=88.06, t1=90.2, text="TOPLAR ATILDI", y=380, size=120),
    # --- Rauf Bey
    dict(type="kinetic", t0=90.38, t1=92.8, text="HERKES\nSEVİNDİ Mİ?", y=380, size=120, style="black"),
    dict(type="label", t0=93.0, t1=98.0, title="Rauf (Orbay) Bey", sub="İstanbul · Kalamış", y=420),
    dict(type="quote", t0=98.2, t1=100.3, y=760, by="Rauf Orbay'ın anıları",
         words=[("Mutlaka", 98.68), ("Cumhuriyettir.", 99.12)]),
    dict(type="quote", t0=102.3, t1=105.9, y=760, by="Rauf Bey · Tevhid-i Efkâr ve Vatan, 1923",
         words=[("Cumhuriyet'in", 103.26), ("ilanında", 103.92), ("acele", 104.62), ("edilmiştir.", 105.02)]),
    dict(type="vs", t0=106.4, t1=113.0),
    dict(type="kinetic", t0=109.64, t1=113.0, text="AYRILIK", y=330, size=130, style="red"),
    # --- final
    dict(type="kinetic", t0=113.18, t1=DURATION + 1, text="RAUF BEY\nHAKLI MIYDI?", y=330, size=110),
    dict(type="tagpair", t0=115.2, t1=DURATION + 1, tags=[("ACELE EDİLDİ", 640, 116.48), ("TAM ZAMANIYDI", 780, 118.16)]),
    dict(type="cta", t0=119.4, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 4.4), (37.4, 39.9), (55.4, 58.3), (98.2, 100.3), (102.3, 105.9), (113.18, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 12.62, 37.4, 45.24, 66.08, 73.78, 77.3, 88.06, 103.26]
SHAKE = [12.62, 73.78]
FLASH = [(37.4, 0.15), (73.78, 0.2), (88.06, 0.2)]

MUSIC = [(0, 11.44, 1), (11.44, 34.56, 2), (34.56, 48.3, 3), (48.3, 66.08, 2), (66.08, 90.38, 3), (90.38, 113.18, 2),
         (113.18, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("penline", "handwrite")]
SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=12.62, gain=0.3), dict(name="riser", t=37.4, gain=0.2, pre=True),
       dict(name="impact", t=37.4, gain=0.45), dict(name="hit", t=73.78, gain=0.35), dict(name="thunder", t=88.06, gain=0.35),
       dict(name="pop", t=119.4, gain=0.35)]
SFX += [dict(name="pen", t=p, gain=0.2) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="cankaya", grade="dark", focus=(0.5, 0.45), zoom=1.1, lines=["28 EKİM 1923", "GECESİ NE OLDU?"], y=260, size=112,
             portraits=[("mk1923", 330, 900, 330), ("ismet", 690, 900, 330)],
             stamp="UYUMADILAR", stamp_y=1200, stamp_size=120, stamp_color=RED, stamp_rot=-6)
