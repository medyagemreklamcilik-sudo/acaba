"""Timeline for "Osmanlı'da kardeş katli" (narration seconds)."""

DURATION = 109.3
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "mehmed3", "mehmed3b", "murad3", "sanduka", "turbe", "kanunname", "kanunname_baski", "yildirim", "ankara", "savas",
    "kanuni", "mustafa", "ahmed1", "mustafa1", "kafes", "kafes2", "babussaade", "cenaze", "cenaze2", "cellat", "fatih"]}

FACES = {"mehmed3": (0.5, 0.35), "murad3": (0.5, 0.35), "yildirim": (0.5, 0.3), "kanuni": (0.5, 0.3), "mustafa": (0.5, 0.35),
         "ahmed1": (0.5, 0.35), "mustafa1": (0.5, 0.3), "fatih": (0.6, 0.35)}

SCENES = [
    # kanca
    dict(t=0.00, img="babussaade", grade="dark", zoom=(1.35, 1.05), focus=(0.5, 0.5)),
    dict(t=3.82, img="mehmed3", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="flash"),
    dict(t=5.96, img="cellat", grade="dark", zoom=(1.1, 1.3), focus=(0.4, 0.45), tr="glitch"),
    dict(t=9.78, img="cenaze", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="dip"),
    dict(t=12.78, img="sanduka", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="pushup"),
    dict(t=14.68, img="cenaze2", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=17.04, img="mehmed3b", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="flash"),
    dict(t=21.66, mode="plate", bg="murad3", tr="dip"),
    # neden?
    dict(t=24.92, img="murad3", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushup"),
    dict(t=31.86, img="savas", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="glitch"),
    dict(t=33.74, img="yildirim", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="pushleft"),
    dict(t=35.80, img="ankara", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="bars"),
    # Fatih kanunnamesi
    dict(t=41.72, img="fatih", zoom=(1.0, 1.15), focus=(0.6, 0.35), tr="flash"),
    dict(t=45.18, img="kanunname", mode="card", maxw=880, maxh=760, tilt=-2, tr="pushup"),
    dict(t=47.20, mode="plate", bg="kanunname", tr="dip"),
    dict(t=59.18, img="kanunname_baski", mode="card", maxw=700, maxh=1000, tilt=2, tr="pushleft"),
    dict(t=63.26, mode="plate", bg="kanunname_baski", tr="dip"),
    # 61 şehzade, Kanuni
    dict(t=71.62, img="turbe", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=77.00, mode="split", tr="bars", imgs=[dict(img="kanuni", focus=(0.5, 0.3)), dict(img="mustafa", focus=(0.5, 0.3))]),
    # son
    dict(t=81.70, img="cenaze", grade="dark", zoom=(1.2, 1.4), focus=(0.5, 0.5), tr="dip"),
    dict(t=88.18, mode="split", tr="bars", imgs=[dict(img="ahmed1", focus=(0.5, 0.35)), dict(img="mustafa1", focus=(0.5, 0.3))]),
    dict(t=92.28, img="kafes", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=97.78, img="kafes2", zoom=(1.0, 1.2), focus=(0.4, 0.5), tr="pushup"),
    # final
    dict(t=102.30, mode="plate", bg="mehmed3", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=3.7, lines=["27 OCAK 1595"], y=330, size=130),
    dict(type="label", t0=1.3, t1=3.7, title="Topkapı Sarayı", sub="Bâbüssaâde", y=520),
    dict(type="counter", t0=7.24, t1=9.6, **{"from": 0, "to": 19}, fmt="{} KARDEŞ", dur=0.7, y=420, size=150),
    dict(type="stamp", t0=8.52, t1=9.6, text="BOĞDURULDU", y=820, size=130, color=RED, rot=-7, fill=True),
    dict(type="counter", t0=11.04, t1=12.7, **{"from": 0, "to": 19}, fmt="{} TABUT", dur=0.6, y=420, size=150),
    dict(type="kinetic", t0=13.34, t1=14.6, text="BAZILARI ÇOCUKTU", y=380, size=110, style="red"),
    dict(type="label", t0=17.2, t1=21.5, title="Üçüncü Mehmed", sub="1595 – 1603", y=420),
    dict(type="kinetic", t0=21.66, t1=24.8, text="NEREDEN\nÇIKTI?", y=760, size=140),
    # --- neden
    dict(type="kinetic", t0=25.62, t1=27.6, text="SABİT KURAL YOK", y=380, size=110, style="black"),
    dict(type="label", t0=27.7, t1=31.7, title="Her şehzade", sub="tahtın adayı", y=420),
    dict(type="stamp", t0=32.36, t1=33.6, text="İÇ SAVAŞ", y=820, size=150, color=RED, rot=-7, fill=True),
    dict(type="label", t0=33.9, t1=35.7, title="Yıldırım Bayezid", sub="1389 – 1402", y=420),
    dict(type="counter", t0=36.44, t1=41.6, **{"from": 0, "to": 11}, fmt="{} YIL", dur=0.6, y=420, size=160, sub="Fetret Devri · 1402-1413"),
    # --- kanunname
    dict(type="label", t0=42.0, t1=45.0, title="Fatih Sultan Mehmed", sub="Kanunnâme-i Âl-i Osman", y=420),
    dict(type="quote", t0=47.2, t1=54.2, y=760, by="Fatih Kanunnâmesi",
         words=[("Her", 47.28), ("kimesneye", 47.5), ("evladımdan", 48.1), ("saltanat", 48.92), ("müyesser", 49.48), ("ola,", 49.98),
                ("karındaşların", 50.46), ("nizam-ı", 51.36), ("âlem", 51.94), ("için", 52.34), ("katletmek", 52.6), ("münasiptir.", 53.3)]),
    dict(type="kinetic", t0=54.34, t1=58.9, text="DÜNYANIN DÜZENİ İÇİN", y=380, size=104, style="red"),
    dict(type="label", t0=59.3, t1=63.1, title="\"Ekser ulemâ tecvîz etmiştir\"", sub="Ulemanın çoğu izin verdi", y=330),
    dict(type="tagpair", t0=64.12, t1=67.4, tags=[("\"LÂZIMDIR\" DEĞİL", 640, 64.68), ("\"MÜNASİPTİR\"", 780, 66.22)]),
    dict(type="kinetic", t0=67.48, t1=71.5, text="SONRADAN\nEKLENDİ Mİ?", y=330, size=110, style="black"),
    # --- 61 şehzade
    dict(type="counter", t0=74.08, t1=76.9, **{"from": 0, "to": 61}, fmt="{} ŞEHZADE", dur=0.8, y=420, size=150),
    dict(type="tagpair", t0=77.0, t1=81.6, tags=[("KANUNİ", 380, 77.0), ("ŞEHZADE MUSTAFA · 1553", 1060, 79.34)]),
    dict(type="stamp", t0=80.86, t1=81.6, text="BOĞDURDU", y=960, size=120, color=RED, rot=-7, fill=True),
    # --- son
    dict(type="title", t0=82.18, t1=86.0, lines=["1595 · O GECE"], y=330, size=120),
    dict(type="kinetic", t0=86.16, t1=88.1, text="HALK AYAKLANDI", y=380, size=110, style="red"),
    dict(type="tagpair", t0=88.2, t1=92.2, tags=[("I. AHMED", 380, 89.26), ("MUSTAFA · YAŞADI", 1060, 90.18)]),
    dict(type="kinetic", t0=93.4, t1=97.6, text="EN BÜYÜK ERKEK\nTAHTA ÇIKAR", y=380, size=104),
    dict(type="label", t0=98.0, t1=102.1, title="Kafes", sub="Topkapı'da şehzade daireleri", y=420),
    # --- final
    dict(type="kinetic", t0=102.3, t1=DURATION + 1, text="ZORUNLULUK MU,\nVAHŞET Mİ?", y=330, size=110),
    dict(type="tagpair", t0=103.0, t1=DURATION + 1, tags=[("ZORUNLULUKTU", 640, 105.2), ("VAHŞETTİ", 780, 107.0)]),
    dict(type="cta", t0=107.9, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.7), (47.2, 54.2), (102.3, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 8.52, 11.04, 32.36, 41.72, 54.34, 74.08, 80.86, 86.16]
SHAKE = [8.52, 32.36, 80.86]
FLASH = [(3.82, 0.12), (41.72, 0.15)]

MUSIC = [(0, 9.78, 3), (9.78, 21.66, 2), (21.66, 41.72, 2), (41.72, 71.62, 3), (71.62, 81.7, 3), (81.7, 102.3, 2),
         (102.3, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=8.52, gain=0.35), dict(name="bell", t=9.78, gain=0.25),
       dict(name="hit", t=32.36, gain=0.3), dict(name="riser", t=47.2, gain=0.2, pre=True), dict(name="hit", t=80.86, gain=0.3),
       dict(name="pop", t=107.9, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="mehmed3", focus=(0.5, 0.4), zoom=1.05, lines=["BİR GECEDE", "19 KARDEŞ"], y=250, size=130,
             style="red", stamp="KANUN BÖYLE", stamp_y=1200, stamp_size=120, stamp_color=YELLOW, stamp_rot=-6,
             bottom="Fatih Kanunnâmesi · 1595", bottom_y=1340)
