"""Timeline for "Piri Reis haritasının sırrı" (narration seconds)."""

DURATION = 92.68
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in ["harita", "harita2", "detay", "detay2", "pirireis", "kitab", "gemi", "kolomb", "antarktika", "hapgood"]}
FACES = {"pirireis": (0.5, 0.3), "kolomb": (0.5, 0.35)}

SCENES = [
    # kanca
    dict(t=0.00, img="detay2", grade="dark", zoom=(1.35, 1.1), focus=(0.55, 0.5)),
    dict(t=2.94, img="harita", zoom=(1.1, 1.3), focus=(0.4, 0.55), tr="flash"),
    dict(t=6.34, img="antarktika", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="zoomblur"),
    # bulunuş
    dict(t=11.74, img="harita2", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="dip"),
    dict(t=17.72, img="detay", zoom=(1.0, 1.25), focus=(0.5, 0.4), tr="pushup"),
    dict(t=21.70, img="pirireis", zoom=(1.0, 1.18), focus=(0.5, 0.3), tr="iris"),
    dict(t=24.56, img="gemi", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushleft"),
    dict(t=26.52, img="kitab", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="diag"),
    # not ve Kolomb
    dict(t=29.48, img="harita", zoom=(1.3, 1.6), focus=(0.65, 0.35), tr="zoomblur"),
    dict(t=35.14, img="kolomb", zoom=(1.0, 1.18), focus=(0.5, 0.35), tr="pushright"),
    dict(t=37.84, img="kolomb", grade="dark", zoom=(1.18, 1.35), focus=(0.5, 0.35), tr="glitch"),
    dict(t=40.84, img="harita2", zoom=(1.05, 1.25), focus=(0.5, 0.5), tr="bars"),
    # sen olsan
    dict(t=44.98, mode="plate", bg="harita", tr="dip"),
    # Hapgood
    dict(t=52.12, img="hapgood", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="pushup"),
    dict(t=56.12, img="antarktika", grade="dark", zoom=(1.1, 1.35), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=60.96, img="harita", zoom=(1.4, 1.7), focus=(0.4, 0.85), tr="pushdown"),
    dict(t=67.08, img="harita2", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
    # idam
    dict(t=71.22, img="pirireis", grade="dark", zoom=(1.15, 1.35), focus=(0.5, 0.3), tr="glitch"),
    dict(t=77.40, mode="plate", bg="pirireis", tr="dip"),
    dict(t=82.02, img="harita", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="iris"),
    # son
    dict(t=86.28, mode="plate", bg="harita", tr="bars"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=6.2, lines=["KOLOMB'DAN 21 YIL SONRA", "AMERİKA'YI ÇİZDİ"], y=330, size=96),
    dict(type="stamp", t0=2.94, t1=6.2, text="1513", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=8.2, t1=11.6, text="BUZSUZ\nANTARKTİKA?", y=420, size=140, style="red"),
    # --- bulunuş
    dict(type="label", t0=11.9, t1=17.5, title="Topkapı Sarayı, 1929", sub="unutulmuş belgelerin arasında", y=420),
    dict(type="stamp", t0=17.72, t1=21.5, text="CEYLAN DERİSİ", y=900, size=110, color=YELLOW, rot=-5, fill=True),
    dict(type="label", t0=21.8, t1=24.4, title="Piri Reis", sub="temsili tablo, gerçek portresi yok", y=420),
    dict(type="label", t0=24.6, t1=26.4, title="Kemal Reis'in yeğeni", sub="Osmanlı kadırgası, minyatür", y=420),
    dict(type="label", t0=26.6, t1=29.3, title="Kitâb-ı Bahriye", sub="Piri Reis'in Akdeniz kitabı", y=420),
    # --- not
    dict(type="kinetic", t0=32.64, t1=35.0, text="~20 HARİTA", y=420, size=160, style="black"),
    dict(type="label", t0=35.3, t1=37.7, title="Kristof Kolomb", sub="haritası bugün kayıp", y=420),
    dict(type="stamp", t0=39.44, t1=40.7, text="KAYIP", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=41.9, t1=44.8, text="TEK İZ\nBU HARİTA?", y=420, size=130, style="red"),
    # --- sen olsan
    dict(type="kinetic", t0=45.0, t1=51.9, text="İLK NEYE\nBAKARDIN?", y=420, size=140, style="black"),
    dict(type="tagpair", t0=47.6, t1=51.9, tags=[("AMERİKA", 800, 48.14), ("GİZEMLİ KIYI", 950, 50.62)]),
    # --- Hapgood
    dict(type="label", t0=52.3, t1=56.0, title="Charles Hapgood", sub="Maps of the Ancient Sea Kings, 1966", y=420),
    dict(type="stamp", t0=56.12, t1=60.8, text="BUZSUZ ANTARKTİKA?", y=900, size=96, color=YELLOW, rot=-5, fill=True),
    dict(type="kinetic", t0=63.2, t1=66.9, text="BÜKÜLMÜŞ\nGÜNEY AMERİKA", y=380, size=120, style="black"),
    dict(type="counter", t0=67.6, t1=71.0, **{"from": 0, "to": 3}, fmt="1/{}'Ü KALDI", dur=0.5, y=440, size=140),
    # --- idam
    dict(type="stamp", t0=75.56, t1=77.2, text="İDAM", y=900, size=170, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=82.1, t1=86.1, text="HARİTASIYLA\nHATIRLANDI", y=380, size=130, style="black"),
    # --- son
    dict(type="kinetic", t0=86.28, t1=DURATION + 1, text="DEHA MI?\nEFSANE Mİ?", y=420, size=140),
    dict(type="tagpair", t0=87.0, t1=DURATION + 1, tags=[("DEHA ESERİ", 760, 88.14), ("ABARTILMIŞ EFSANE", 900, 89.84)]),
    dict(type="cta", t0=91.7, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(17.7, 18.9), (39.3, 40.0), (56.1, 57.9), (75.5, 76.5), (0.0, 6.2), (8.2, 11.6), (32.6, 34.9), (44.98, 51.9), (63.2, 66.0), (82.0, 86.1), (86.28, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 2.94, 8.2, 17.72, 32.64, 39.44, 45.0, 56.12, 75.56, 86.28]
SHAKE = [2.94, 39.44, 75.56]
FLASH = [(2.94, 0.10), (60.96, 0.10)]

MUSIC = [(0, 11.74, 3), (11.74, 29.48, 2), (29.48, 44.98, 3), (44.98, 52.12, 1), (52.12, 71.22, 2), (71.22, 82.02, 3),
         (82.02, DURATION, 2)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=2.94, gain=0.4), dict(name="hit", t=39.44, gain=0.3),
       dict(name="riser", t=52.12, gain=0.2, pre=True), dict(name="hit", t=75.56, gain=0.35), dict(name="pop", t=91.7, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="harita", focus=(0.45, 0.6), zoom=1.05, lines=["BU HARİTADA", "ANTARKTİKA MI VAR?"], y=250, size=108,
             style="red", stamp="1513 · PİRİ REİS", stamp_y=1260, stamp_size=96, stamp_color=YELLOW, stamp_rot=-5,
             marks=[dict(type="pencircle", cx=520, cy=1000, rx=330, ry=150)])
