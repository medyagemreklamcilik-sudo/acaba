"""Kepenk · "Telsim: Motorola'nın 2 milyar dolarını batıran Türk şirketi" (narration seconds).
Hızlı kurgu: kısa sahneler, sert zoom'lar, finans efektleri (chart / moneyrain / ticker / counter)."""

DURATION = 126.9
CAP_Y = 1235
CX = 507
ACCENT = (255, 122, 0)           # Kepenk turuncu nokta
ORANGE = ACCENT
RED = (255, 50, 50)
WHITE_C = (235, 240, 255)

IMAGES = {
    "telsim": "telsim.jpg",
    "telsim_eski": "telsim_eski.jpg",
    "uzan_grup": "uzan_grup.jpg",
    "billboard": "billboard.jpg",
    "afisler": "afisler.jpg",
    "cem_genc": "cem_genc.jpg",
    "cem_basin": "cem_basin.jpg",
    "cem_miting": "cem_miting.jpg",
    "kontor": "kontor.jpg",
    "kontor2": "kontor2.jpg",
    "motorola": "motorola.jpg",
    "motorola2": "motorola2.jpg",
    "nokia": "nokia.jpg",
    "rakoff": "rakoff.jpg",
    "imar_ilan": "imar_ilan.jpg",
    "imar_tv": "imar_tv.jpg",
    "tmsf": "tmsf.jpg",
    "erdogan": "erdogan.jpg",
    "vodafone": "vodafone.jpg",
    "nokia3310": "nokia3310.jpg",
    "logo": "logo.jpg",
}

FACES = {"cem_genc": (0.55, 0.35), "cem_basin": (0.5, 0.35), "cem_miting": (0.45, 0.3), "rakoff": (0.5, 0.3),
         "erdogan": (0.5, 0.25)}

SCENES = [
    # hook
    dict(t=0.00, img="motorola", grade="dark", zoom=(1.5, 1.0), focus=(0.5, 0.4)),
    dict(t=3.90, mode="plate", bg="logo", tr="zoomblur"),
    # kuruluş
    dict(t=8.06, img="telsim_eski", mode="card", maxw=900, maxh=500, tilt=-2, tr="flash"),
    dict(t=11.48, img="billboard", zoom=(1.0, 1.3), focus=(0.5, 0.45), tr="pushup"),
    dict(t=15.86, img="afisler", zoom=(1.0, 1.25), focus=(0.4, 0.5), tr="pushleft"),
    dict(t=18.08, img="uzan_grup", mode="card", maxw=820, maxh=900, tilt=2, tr="zoomblur"),
    # kredi
    dict(t=20.08, img="nokia3310", zoom=(1.4, 1.0), focus=(0.5, 0.5), tr="spin"),
    dict(t=21.56, mode="split", tr="bars", imgs=[dict(img="motorola2", focus=(0.5, 0.4)), dict(img="nokia", focus=(0.5, 0.5))]),
    dict(t=26.00, mode="plate", bg="logo", tr="dip"),
    dict(t=28.92, img="telsim", grade="dark", zoom=(1.0, 1.6), focus=(0.5, 0.5), tr="glitch"),
    # mahkeme
    dict(t=33.46, img="motorola", grade="dark", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="pushup"),
    dict(t=37.44, img="rakoff", mode="card", maxw=740, maxh=860, tilt=-2, tr="zoomblur"),
    dict(t=40.68, mode="plate", bg="logo", tr="flash"),
    # İmar / TMSF
    dict(t=45.34, img="imar_tv", grade="dark", zoom=(1.0, 1.35), focus=(0.55, 0.5), tr="glitch"),
    dict(t=48.26, img="imar_ilan", mode="card", maxw=860, maxh=700, tilt=2, tr="pushleft"),
    dict(t=52.58, img="tmsf", zoom=(1.0, 1.3), focus=(0.5, 0.6), tr="pushup"),
    dict(t=60.96, mode="plate", bg="tmsf", tr="flash"),
    # villa
    dict(t=67.98, img="kontor2", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="glitch"),
    dict(t=71.32, img="kontor", zoom=(1.1, 1.5), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=77.54, img="cem_basin", zoom=(1.0, 1.3), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=79.40, mode="plate", bg="cem_genc", tr="dip"),
    dict(t=85.76, img="erdogan", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.25), tr="pushup"),
    dict(t=89.90, mode="plate", bg="erdogan", tr="dip"),
    dict(t=92.70, img="cem_miting", zoom=(1.0, 1.3), focus=(0.45, 0.3), tr="glitch"),
    dict(t=98.70, img="cem_genc", grade="dark", zoom=(1.1, 1.4), focus=(0.55, 0.35), tr="pushleft"),
    # satış
    dict(t=101.90, img="vodafone", zoom=(1.4, 1.0), focus=(0.5, 0.5), tr="flash"),
    dict(t=106.88, mode="plate", bg="logo", tr="zoomblur"),
    dict(t=109.66, mode="split", tr="bars", imgs=[dict(img="motorola2", focus=(0.5, 0.4)), dict(img="nokia", focus=(0.5, 0.5))]),
    dict(t=116.26, img="telsim", grade="bw", zoom=(1.0, 1.4), focus=(0.5, 0.5), tr="dip"),
    dict(t=118.34, img="vodafone", zoom=(1.0, 1.3), focus=(0.5, 0.5), tr="pushup"),
    dict(t=121.02, mode="plate", bg="logo", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- hook
    dict(type="counter", t0=0.0, t1=3.85, **{"from": 0, "to": 2000000000}, fmt="${}", sep=True, dur=1.2, y=420, size=118),
    dict(type="kinetic", t0=1.8, t1=3.85, text="MOTOROLA'NIN PARASI", y=600, size=84, style="black"),
    dict(type="stamp", t0=4.90, t1=7.95, text="GERİ ALINAMADI", y=820, size=110, color=RED, rot=-7),
    dict(type="ticker", t0=3.90, t1=7.95, y=1500, speed=260,
         items=[("MOTOROLA", "-$2 MLR"), ("NOKIA", "-$700 MLN"), ("TELSIM", "-TEMERRÜT"), ("VODAFONE", "+$4,55 MLR")]),
    # --- kuruluş
    dict(type="title", t0=8.06, t1=11.4, lines=["1994"], y=380, size=150),
    dict(type="label", t0=8.4, t1=11.4, title="Telsim", sub="Uzan ailesi kurdu", y=620),
    dict(type="kinetic", t0=12.82, t1=15.8, text="DEV GSM\nOPERATÖRÜ", y=380, size=110),
    dict(type="tagpair", t0=15.9, t1=19.9, tags=[("ABONE", 380, 15.86), ("REKLAM", 520, 17.2), ("TV + GAZETE", 660, 18.08)]),
    # --- kredi
    dict(type="kinetic", t0=20.08, t1=21.5, text="PARA LAZIM", y=380, size=130),
    dict(type="tagpair", t0=21.7, t1=25.9, tags=[("MOTOROLA", 380, 24.34), ("NOKIA", 1060, 24.88)]),
    dict(type="moneyrain", t0=26.0, t1=28.85, n=30, spread=1.2),
    dict(type="counter", t0=26.0, t1=28.85, **{"from": 0, "to": 2700000000}, fmt="${}", sep=True, dur=1.0, y=520, size=118),
    dict(type="title", t0=29.86, t1=31.35, lines=["2001"], y=380, size=150),
    dict(type="stamp", t0=31.82, t1=33.4, text="ÖDEME YOK", y=760, size=150, color=RED, rot=-8, fill=True),
    # --- mahkeme
    dict(type="label", t0=33.6, t1=37.35, title="New York · Federal Mahkeme", sub="Motorola ve Nokia - Uzan ailesi", y=420),
    dict(type="label", t0=37.6, t1=40.6, title="Yargıç Jed Rakoff", sub="2003 kararı", y=420),
    dict(type="chart", t0=40.68, t1=45.25, dur=2.6, title="Motorola · milyar $", crash=3, color=ORANGE,
         points=[("1998", 0.0), ("kredi", 2.0), ("karar 2003", 4.26), ("tahsil 2005", 0.41)], box=(150, 520, 870, 980)),
    dict(type="counter", t0=41.9, t1=45.25, **{"from": 0, "to": 4260000000}, fmt="${}", sep=True, dur=1.4, y=360, size=100),
    # --- İmar / TMSF
    dict(type="kinetic", t0=45.48, t1=48.2, text="ASIL DEPREM\nTÜRKİYE'DE", y=380, size=110, style="red"),
    dict(type="label", t0=48.4, t1=52.5, title="İmar Bankası", sub="Temmuz 2003 · lisans iptal", y=420),
    dict(type="stamp", t0=51.24, t1=52.5, text="LİSANS İPTAL", y=1000, size=100, color=RED, rot=-6, fill=True),
    dict(type="quote", t0=54.9, t1=60.9, y=760, by="TMSF yazılı açıklaması · 14 Şubat 2004",
         words=[("Dünya", 55.0), ("finans", 55.76), ("tarihinde", 56.10), ("eşine", 56.80), ("ender", 57.32),
                ("rastlanan", 57.82), ("bir", 58.40), ("para", 58.78), ("ve", 58.92), ("mal", 59.20), ("kaçırma", 59.44),
                ("operasyonu.", 59.88)]),
    dict(type="typewriter", t0=60.96, t1=62.85, text="13 ŞUBAT 2004", y=420, size=72, dur=0.6),
    dict(type="counter", t0=64.64, t1=67.9, **{"from": 0, "to": 200}, fmt="{}+ ŞİRKET", dur=0.9, y=620, size=130),
    dict(type="stamp", t0=66.88, t1=67.9, text="EL KONULDU", y=860, size=120, color=ORANGE, rot=-6, fill=True),
    # --- villa
    dict(type="label", t0=68.1, t1=71.2, title="Cem Uzan'ın villası", sub="19 Şubat 2004 · polis araması", y=420),
    dict(type="counter", t0=72.04, t1=73.55, **{"from": 0, "to": 1130}, fmt="{} KOLİ", sep=True, dur=0.6, y=420, size=120),
    dict(type="counter", t0=74.24, t1=77.45, **{"from": 0, "to": 3800000}, fmt="{} KONTÖR", sep=True, dur=1.0, y=420, size=96),
    dict(type="pencircle", t0=75.4, t1=77.45, cx=CX, cy=900, rx=360, ry=260, seed=3, color=ORANGE),
    dict(type="label", t0=77.6, t1=79.35, title="Cem Uzan", sub="Şubat 2004", y=420),
    dict(type="quote", t0=79.4, t1=85.6, y=760, by="Cem Uzan · Şubat 2004",
         words=[("Telsim", 79.54), ("benim.", 79.96), ("Kontör", 80.48), ("kartlarını", 80.92), ("ister", 81.42),
                ("evimde,", 81.74), ("ister", 82.56), ("başka", 82.74), ("yerde", 83.10), ("saklarım.", 83.34),
                ("Buna", 83.92), ("kimse", 84.32), ("karışamaz.", 84.72)]),
    dict(type="label", t0=85.9, t1=89.8, title="Başbakan Erdoğan", sub="Niğde · Şubat 2004 · isim vermeden", y=420),
    dict(type="quote", t0=89.9, t1=92.6, y=760, by="Başbakan Erdoğan · Niğde, Şubat 2004",
         words=[("Bunlar", 90.26), ("halkın", 90.50), ("önüne", 90.86), ("hangi", 91.18), ("yüzle", 91.56), ("çıkıyorlar?", 91.84)]),
    dict(type="kinetic", t0=92.70, t1=94.6, text="GERİ ADIM YOK", y=380, size=120),
    dict(type="kinetic", t0=96.26, t1=98.6, text="\"GİZLİ ANLAŞMA\"\nİDDİASI", y=380, size=100, style="black"),
    dict(type="source", text="Cem Uzan'ın iddiası · TMSF-Motorola", t0=94.8, t1=98.6),
    dict(type="kinetic", t0=99.06, t1=101.8, text="\"BIRAKIN\nBEN SATAYIM\"", y=380, size=110),
    # --- satış
    dict(type="typewriter", t0=101.9, t1=103.3, text="ARALIK 2005 · İHALE", y=420, size=60, dur=0.6),
    dict(type="stamp", t0=105.48, t1=106.8, text="KAZANAN: VODAFONE", y=820, size=96, color=ORANGE, rot=-6, fill=True),
    dict(type="moneyrain", t0=107.3, t1=109.6, n=36, spread=1.0),
    dict(type="counter", t0=106.88, t1=109.6, **{"from": 0, "to": 4550000000}, fmt="${}", sep=True, dur=1.2, y=520, size=112),
    dict(type="tagpair", t0=109.8, t1=116.2, tags=[("MOTOROLA: $410 MLN", 380, 112.18), ("NOKIA: $340 MLN", 1060, 114.06)]),
    dict(type="kinetic", t0=116.26, t1=118.25, text="TELSIM\nTARİHE KARIŞTI", y=380, size=110, style="black"),
    dict(type="stamp", t0=119.42, t1=120.95, text="BUGÜN: VODAFONE", y=900, size=100, color=ORANGE, rot=-5, fill=True),
    # --- final
    dict(type="kinetic", t0=121.02, t1=DURATION + 1, text="SENCE NE BATIRDI?", y=330, size=104),
    dict(type="tagpair", t0=122.0, t1=DURATION + 1, tags=[("KÖTÜ YÖNETİM", 560, 122.80), ("SİYASET", 700, 124.34)]),
    dict(type="cta", t0=125.3, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 3.85), (54.9, 60.9), (79.4, 85.6), (89.9, 92.6), (121.02, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


# hyper-motion: sık punch, kısa sarsıntı
PUNCH = [0.0, 3.90, 8.06, 20.08, 26.0, 29.86, 31.82, 40.68, 45.48, 51.24, 60.96, 66.88, 71.32, 77.54, 101.9, 105.48,
         106.88, 116.26, 119.42]
SHAKE = [31.82, 45.48, 66.88]
FLASH = [(8.06, 0.15), (60.96, 0.15), (101.9, 0.15)]

MUSIC = [(0, 8.06, 3), (8.06, 20.08, 2), (20.08, 33.46, 3), (33.46, 45.34, 2), (45.34, 67.98, 3), (67.98, 92.7, 2),
         (92.7, 101.9, 2), (101.9, 116.26, 3), (116.26, DURATION, 1)]

# ses efektleri az ve kısık (kullanıcı isteği)
SFX = [dict(name="impact", t=0.0, gain=0.45), dict(name="hit", t=4.90, gain=0.25), dict(name="hit", t=31.82, gain=0.3),
       dict(name="riser", t=40.68, gain=0.15, pre=True), dict(name="impact", t=45.48, gain=0.35), dict(name="hit", t=66.88, gain=0.25),
       dict(name="shutter", t=60.96, gain=0.2), dict(name="hit", t=105.48, gain=0.25), dict(name="pop", t=125.3, gain=0.25)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="cem_miting", grade="dark", focus=(0.45, 0.12), zoom=1.0, lines=["TELSİM", "MOTOROLA'NIN", "2 MİLYAR $'INI", "NASIL BATIRDI?"],
             y=150, size=86, stamp="BATTI", stamp_y=1560, stamp_size=150, stamp_color=RED, stamp_rot=-6,
             marks=[dict(type="chart", dur=0.01, color=ORANGE, crash=3, points=[("", 0.3), ("", 2.0), ("", 2.7), ("", 0.2)],
                         box=(560, 1120, 900, 1380))])
