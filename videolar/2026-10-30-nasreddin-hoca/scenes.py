"""Timeline for "Nasreddin Hoca gerçekten yaşadı mı?" (narration seconds)."""

DURATION = 106.1
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "turbe_eski", "turbe_kart", "turbe", "turbe_kapi", "turbe2", "sanduka", "sutun", "minyatur", "minyatur2", "cocuklar",
    "saltukname", "timur", "sivrihisar", "heykel", "fatih", "yazma", "letaif", "arsiv"]}

FACES = {"minyatur": (0.5, 0.25), "minyatur2": (0.5, 0.2), "timur": (0.5, 0.3), "fatih": (0.4, 0.4)}

SCENES = [
    # kanca: mezar taşı
    dict(t=0.00, img="sanduka", grade="dark", zoom=(1.4, 1.05), focus=(0.4, 0.55)),
    dict(t=4.80, mode="plate", bg="sanduka", tr="glitch"),
    dict(t=8.62, img="minyatur", zoom=(1.0, 1.2), focus=(0.5, 0.3), tr="pushup"),
    dict(t=12.58, mode="plate", bg="minyatur", tr="dip"),
    dict(t=18.32, img="minyatur2", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="flash"),
    # rivayet
    dict(t=23.66, img="sivrihisar", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=28.12, img="cocuklar", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushup"),
    dict(t=29.56, img="turbe_kart", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="bars"),
    dict(t=33.18, mode="plate", bg="yazma", tr="glitch"),
    # kanıtlar
    dict(t=41.16, img="turbe_eski", zoom=(1.0, 1.2), focus=(0.45, 0.5), tr="flash"),
    dict(t=45.14, img="sutun", zoom=(1.0, 1.2), focus=(0.4, 0.5), tr="pushleft"),
    dict(t=49.56, img="turbe", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushup"),
    dict(t=53.76, img="fatih", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="dip"),
    dict(t=56.46, img="arsiv", mode="card", maxw=640, maxh=980, tilt=-2, tr="pushup"),
    dict(t=60.92, img="saltukname", mode="card", maxw=700, maxh=1000, tilt=2, tr="flash"),
    dict(t=64.26, img="yazma", mode="card", maxw=880, maxh=700, tilt=-2, tr="pushleft"),
    dict(t=69.34, mode="plate", bg="sivrihisar", tr="bars"),
    # Timur
    dict(t=74.98, img="timur", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="glitch"),
    dict(t=79.44, mode="split", tr="bars", imgs=[dict(img="timur", focus=(0.5, 0.3)), dict(img="minyatur", focus=(0.5, 0.25))]),
    # türbe şakası
    dict(t=86.48, img="turbe_kapi", zoom=(1.0, 1.3), focus=(0.45, 0.6), tr="dip"),
    dict(t=93.22, img="turbe2", zoom=(1.2, 1.0), focus=(0.5, 0.5), tr="pushup"),
    # final
    dict(t=99.30, mode="plate", bg="minyatur", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=4.7, lines=["MEZAR TAŞINDAKİ", "TARİH"], y=330, size=110),
    dict(type="counter", t0=2.18, t1=4.7, **{"from": 0, "to": 386}, fmt="{}", dur=0.8, y=760, size=230),
    dict(type="kinetic", t0=4.8, t1=8.5, text="TÜRKLER HENÜZ\nANADOLU'DA YOK", y=380, size=104, style="red"),
    dict(type="stamp", t0=6.7, t1=8.5, text="İMKÂNSIZ", y=900, size=150, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=10.6, t1=12.5, text="SON ŞAKA?", y=380, size=130),
    dict(type="kinetic", t0=12.58, t1=14.3, text="386", y=760, size=260, style="black"),
    dict(type="kinetic", t0=14.44, t1=16.2, text="683", y=760, size=260, style="red"),
    dict(type="handwrite", t0=13.3, t1=16.2, text="tersten oku", y=420, size=110, dur=0.6),
    dict(type="title", t0=16.24, t1=18.2, lines=["YANİ 1284"], y=760, size=140),
    dict(type="kinetic", t0=18.32, t1=23.5, text="GERÇEK Mİ,\nEFSANE Mİ?", y=380, size=120),
    # --- rivayet
    dict(type="label", t0=23.8, t1=28.0, title="Sivrihisar · Hortu köyü", sub="Rivayete göre doğum yeri · 1208", y=420),
    dict(type="label", t0=29.7, t1=33.0, title="Akşehir", sub="Öldüğü yer", y=420),
    dict(type="stamp", t0=33.3, t1=37.7, text="RİVAYET", y=820, size=170, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=37.86, t1=41.0, text="DÖNEMİNDEN\nTEK KAYIT YOK", y=380, size=110, style="black"),
    # --- kanıtlar
    dict(type="label", t0=42.9, t1=45.0, title="Nasreddin Hoca Türbesi", sub="Akşehir · eski fotoğraf", y=420),
    dict(type="counter", t0=46.12, t1=49.4, **{"from": 1300, "to": 1393}, fmt="{}", dur=0.8, y=420, size=170),
    dict(type="handwrite", t0=47.96, t1=49.4, text="bir sipahi adını kazıdı", y=600, size=84, dur=0.6),
    dict(type="stamp", t0=50.56, t1=53.6, text="ZİYARET EDİLİYORDU", y=1050, size=90, color=YELLOW, rot=-6, fill=True),
    dict(type="label", t0=53.9, t1=56.3, title="Fatih Sultan Mehmed dönemi", sub="15. yüzyıl", y=420),
    dict(type="label", t0=56.6, t1=60.8, title="Hoca adına vakıf kaydı", sub="Arşiv belgesi (temsili görsel)", y=330),
    dict(type="title", t0=60.92, t1=64.1, lines=["1480 · SALTUKNÂME"], y=330, size=96),
    dict(type="tagpair", t0=63.9, t1=68.9, tags=[("2 FIKRA", 1060, 63.96), ("EN ESKİ KAYIT", 1160, 67.82)]),
    dict(type="label", t0=69.5, t1=74.8, title="Sivrihisar çevresi", sub="Oğullarına ve kızına ait denilen mezar taşları", y=760),
    # --- Timur
    dict(type="kinetic", t0=74.98, t1=77.2, text="TİMUR\nFIKRALARI?", y=380, size=120),
    dict(type="tagpair", t0=79.44, t1=86.3, tags=[("TİMUR · 1402", 380, 78.38), ("HOCA · ÖLÜM 1284", 1180, 80.04)]),
    dict(type="vs", t0=80.0, t1=86.3),
    dict(type="stamp", t0=85.5, t1=86.4, text="SONRADAN EKLENDİ", y=760, size=96, color=RED, rot=-6, fill=True),
    # --- türbe
    dict(type="kinetic", t0=90.34, t1=90.9, text="KİLİT VAR", y=380, size=140),
    dict(type="kinetic", t0=90.92, t1=93.1, text="DUVAR YOK!", y=380, size=140, style="red"),
    dict(type="handwrite", t0=97.16, t1=99.2, text="Hoca'nın son şakası", y=420, size=100, dur=0.6),
    # --- final
    dict(type="kinetic", t0=99.3, t1=DURATION + 1, text="GERÇEKTEN\nYAŞADI MI?", y=330, size=120),
    dict(type="tagpair", t0=100.4, t1=DURATION + 1, tags=[("YAŞADI", 640, 101.16), ("HALKIN KAHRAMANI", 780, 103.04)]),
    dict(type="cta", t0=104.6, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 4.7), (12.58, 18.2), (99.3, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 6.7, 12.58, 14.44, 33.3, 46.12, 85.5, 90.92]
SHAKE = [6.7, 14.44, 33.3]
FLASH = [(14.44, 0.15), (41.16, 0.15)]

MUSIC = [(0, 18.32, 3), (18.32, 41.16, 2), (41.16, 74.98, 2), (74.98, 86.48, 3), (86.48, 99.3, 2), (99.3, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] == "handwrite"]
SFX = [dict(name="impact", t=0.05, gain=0.55), dict(name="hit", t=6.7, gain=0.3), dict(name="impact", t=14.44, gain=0.45),
       dict(name="hit", t=33.3, gain=0.3), dict(name="hit", t=85.5, gain=0.3), dict(name="pop", t=90.92, gain=0.3),
       dict(name="pop", t=104.6, gain=0.35)]
SFX += [dict(name="pen", t=p, gain=0.2) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="minyatur", focus=(0.5, 0.3), zoom=1.05, lines=["NASREDDİN HOCA", "GERÇEKTEN", "YAŞADI MI?"], y=250, size=110,
             stamp="386 = 683?", stamp_y=1250, stamp_size=130, stamp_color=(255, 255, 255), stamp_rot=-6)
