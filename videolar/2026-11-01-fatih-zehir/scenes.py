"""Timeline for "Fatih zehirlendi mi?" (narration seconds)."""

DURATION = 100.3
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "fatih", "fatih_gul", "fatih_min", "venedik", "venedik2", "konsey", "hekim", "hekim2", "hunkar", "anit", "asik",
    "turbe", "yeniceri", "babinger", "bayezid", "cem", "istanbul", "serbet"]}

FACES = {"fatih": (0.6, 0.35), "fatih_gul": (0.5, 0.2), "fatih_min": (0.55, 0.22), "bayezid": (0.5, 0.3)}

SCENES = [
    # kanca: Venedik 1472
    dict(t=0.00, img="venedik", grade="dark", zoom=(1.5, 1.1), focus=(0.5, 0.5)),
    dict(t=2.24, img="konsey", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="dip"),
    dict(t=8.54, img="fatih", zoom=(1.3, 1.05), focus=(0.6, 0.35), tr="flash"),
    dict(t=10.80, img="venedik2", zoom=(1.0, 1.2), focus=(0.4, 0.5), tr="pushleft"),
    dict(t=12.90, img="hekim", zoom=(1.0, 1.2), focus=(0.6, 0.5), tr="zoomblur"),
    # 12 plan
    dict(t=16.74, mode="plate", bg="venedik", tr="glitch"),
    dict(t=28.10, img="fatih_min", zoom=(1.0, 1.15), focus=(0.55, 0.3), tr="pushup"),
    # 1481
    dict(t=31.44, img="istanbul", zoom=(1.0, 1.25), focus=(0.6, 0.5), tr="flash"),
    dict(t=38.68, img="hunkar", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushleft"),
    # hekimler
    dict(t=42.86, img="hekim2", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=45.98, img="serbet", zoom=(1.0, 1.25), focus=(0.5, 0.4), tr="dip"),
    dict(t=50.56, img="fatih_gul", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="dip"),
    dict(t=53.36, img="anit", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="flash"),
    # Aşıkpaşazade
    dict(t=60.10, img="asik", mode="card", maxw=660, maxh=1000, tilt=-2, tr="pushup"),
    dict(t=62.90, mode="plate", bg="asik", tr="dip"),
    # isyan
    dict(t=70.96, img="yeniceri", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="glitch"),
    dict(t=76.88, img="hekim", grade="dark", zoom=(1.1, 1.3), focus=(0.6, 0.5), tr="bars"),
    # resmi sebep
    dict(t=80.44, img="fatih", grade="dark", zoom=(1.0, 1.15), focus=(0.6, 0.35), tr="dip"),
    dict(t=89.14, img="babinger", mode="card", maxw=660, maxh=1000, tilt=2, tr="pushleft"),
    # final
    dict(t=95.14, img="turbe", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=2.2, lines=["VENEDİK · 1472"], y=330, size=120),
    dict(type="kinetic", t0=3.48, t1=6.4, text="PADİŞAHI\nÖLDÜRMEK İÇİN", y=380, size=110, style="red"),
    dict(type="counter", t0=6.94, t1=8.4, **{"from": 0, "to": 10000}, fmt="{} ALTIN", sep=True, dur=0.6, y=820, size=130, sub="peşin"),
    dict(type="stamp", t0=9.04, t1=10.7, text="HEDEF: FATİH", y=1060, size=120, color=RED, rot=-7, fill=True),
    dict(type="stamp", t0=11.82, t1=12.8, text="KABUL", y=820, size=170, color=YELLOW, rot=-6, fill=True),
    dict(type="label", t0=13.1, t1=16.6, title="Hekim Yakup (Maestro Iacopo)", sub="Fatih'in hekimi · temsili minyatür", y=420),
    # --- 12 plan
    dict(type="title", t0=16.74, t1=21.0, lines=["1456 – 1479"], y=330, size=130),
    dict(type="counter", t0=21.0, t1=28.0, **{"from": 0, "to": 12}, fmt="{} PLAN", dur=0.9, y=600, size=200, sub="zehir"),
    dict(type="tagpair", t0=24.24, t1=28.0, tags=[("ARNAVUT BERBER", 900, 24.24), ("FLORANSALI", 1000, 25.6), ("YAHUDİ HEKİM", 1100, 26.7)]),
    dict(type="kinetic", t0=28.52, t1=31.3, text="ÇOĞU KÂĞIT\nÜZERİNDE KALDI", y=380, size=104, style="black"),
    # --- 1481
    dict(type="title", t0=31.44, t1=34.0, lines=["1481"], y=330, size=170),
    dict(type="stamp", t0=36.48, t1=38.5, text="HEDEF: GİZLİ", y=1060, size=120, color=YELLOW, rot=-6, fill=True),
    dict(type="label", t0=38.8, t1=42.7, title="Hünkâr Çayırı", sub="Gebze yakınları", y=420),
    # --- hekimler
    dict(type="label", t0=43.0, t1=45.8, title="Başhekim Lârî", sub="İlaç verdi · işe yaramadı", y=420),
    dict(type="label", t0=46.1, t1=50.4, title="Yakup Paşa", sub="Ağrı için şerbet · temsili görsel", y=420),
    dict(type="title", t0=53.36, t1=58.0, lines=["3 MAYIS 1481"], y=330, size=120, style="red"),
    dict(type="kinetic", t0=55.12, t1=58.0, text="İKİNDİ VAKTİ", y=1060, size=110, style="black"),
    dict(type="counter", t0=58.38, t1=60.0, **{"from": 0, "to": 49}, fmt="{} YAŞINDA", dur=0.5, y=760, size=150),
    # --- Aşıkpaşazade
    dict(type="label", t0=60.2, t1=62.8, title="Âşıkpaşazâde Tarihi", sub="15. yüzyıl", y=330),
    dict(type="quote", t0=62.9, t1=65.6, y=760, by="Âşıkpaşazâde",
         words=[("Tabibler", 63.02), ("şerbeti", 63.48), ("kim", 64.28), ("verdi", 64.44), ("Hana...", 64.72)]),
    dict(type="tagpair", t0=65.7, t1=70.8, tags=[("ZEHİR?", 640, 66.82), ("KÖTÜ TEDAVİ?", 780, 70.0)]),
    # --- isyan
    dict(type="kinetic", t0=70.96, t1=73.1, text="İSTANBUL KARIŞTI", y=380, size=110, style="red"),
    dict(type="stamp", t0=75.98, t1=76.8, text="ÖLDÜRÜLDÜ", y=900, size=130, color=RED, rot=-7, fill=True),
    dict(type="label", t0=73.3, t1=75.9, title="Sadrazam Karamânî Mehmed Paşa", sub="4 Mayıs 1481", y=420),
    dict(type="stamp", t0=79.32, t1=80.3, text="YAKUP PAŞA DA", y=820, size=110, color=RED, rot=-6, fill=True),
    # --- resmi sebep
    dict(type="kinetic", t0=80.44, t1=82.0, text="RESMİ SEBEP?", y=380, size=130),
    dict(type="title", t0=83.24, t1=89.0, lines=["NİKRİS · GUT"], y=760, size=120),
    dict(type="label", t0=89.3, t1=94.9, title="Franz Babinger", sub="Venedik arşivine dayanarak: zehir", y=330),
    # --- final
    dict(type="kinetic", t0=95.14, t1=DURATION + 1, text="ZEHİR Mİ,\nHASTALIK MI?", y=330, size=120),
    dict(type="tagpair", t0=95.8, t1=DURATION + 1, tags=[("ZEHİRLENDİ", 640, 96.06), ("HASTALIKTAN ÖLDÜ", 780, 97.46)]),
    dict(type="cta", t0=98.9, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.2), (62.9, 65.6), (95.14, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 9.04, 11.82, 21.0, 31.44, 53.36, 75.98, 83.24]
SHAKE = [9.04, 53.36, 75.98]
FLASH = [(8.54, 0.12), (53.36, 0.18)]

MUSIC = [(0, 16.74, 3), (16.74, 31.44, 2), (31.44, 60.1, 3), (60.1, 70.96, 2), (70.96, 80.44, 3), (80.44, 95.14, 2),
         (95.14, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.5), dict(name="hit", t=9.04, gain=0.3), dict(name="hit", t=11.82, gain=0.25),
       dict(name="riser", t=53.36, gain=0.2, pre=True), dict(name="impact", t=53.36, gain=0.45), dict(name="hit", t=75.98, gain=0.3),
       dict(name="pop", t=98.9, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="fatih", focus=(0.6, 0.35), zoom=1.05, lines=["FATİH", "ZEHİRLENDİ Mİ?"], y=250, size=120,
             style="red", stamp="12 SUİKAST PLANI", stamp_y=1260, stamp_size=104, stamp_color=YELLOW, stamp_rot=-6)
