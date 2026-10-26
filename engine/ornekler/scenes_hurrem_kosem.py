"""Timeline for "Hürrem Sultan mı daha güçlüydü, Kösem Sultan mı?" (narration seconds)."""

DURATION = 108.3

IMAGES = {
    "hurrem_rosa": ("hurremp_5.jpg", (0.06, 0.05, 0.94, 0.95)),
    "hurrem_titian": ("hurremp_1.jpg", (0.11, 0.09, 0.89, 0.91)),
    "hurrem_red": ("hurremp_2.jpg", (0.09, 0.07, 0.91, 0.93)),
    "kanuni": "kanuni_1.jpg",
    "kanuni_prof": "kanuni_0.jpg",
    "mihrimah": "mihrimah_0.jpg",
    "rustem": "rustem_0.jpg",
    "ahmed": "ahmed1_0.jpg",
    "mustafa1": "mustafa1_4.jpg",
    "osman2": ("osman2_4.jpg", (0.0, 0.16, 1.0, 0.84)),
    "murad": "murad4_0.jpg",
    "ibrahim": "ibrahim_2.jpg",
    "mehmed4": "mehmed4_5.jpg",
    "turhan": ("turhan_6.jpg", (0.04, 0.03, 0.96, 0.9)),
    "kosem_a": "kosem_a.jpg",
    "kosem_b": "kosem_b.jpg",
    "kosem_c": "kosem_c.jpg",
    "kosem_d": "kosem_d.jpg",
    "ege": "ege_7.jpg",
    "harem": "harem_6.jpg",
    "harem_room": "harem_1.jpg",
    "turbe": "hurremturbe_2.jpg",
    "kanuni_turbe": "haseki_2.jpg",
    "olum": "kosemolum_2.jpg",
    "rohatyn": "hurrem_2.jpg",
    "tatar": "tatar_captives.jpg",
    "esir": "slave_market.jpg",
    "mektup": "tughra2_0.jpg",
    "sigismund": ("sigismund_1.jpg", (0.0, 0.0, 0.86, 1.0)),
    "divan": "sadrazam_4.jpg",
    "istanbul": ("topk4_1.jpg", (0.03, 0.05, 0.97, 0.82)),
}

FACES = {"ahmed": (0.5, 0.35), "mustafa1": (0.5, 0.25), "osman2": (0.5, 0.25), "murad": (0.5, 0.25),
         "ibrahim": (0.5, 0.25), "mehmed4": (0.5, 0.3)}

SPLIT_HK = [dict(img="hurrem_red", focus=(0.5, 0.35)), dict(img="kosem_d", focus=(0.45, 0.3))]

SCENES = [
    dict(t=0.00, mode="split", imgs=SPLIT_HK),
    dict(t=3.84, img="harem", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="zoomblur"),
    dict(t=6.58, mode="split", tr="bars", imgs=[dict(img="kanuni", focus=(0.5, 0.3)), dict(img="ahmed", focus=(0.5, 0.35))]),
    dict(t=9.20, img="esir", zoom=(1.0, 1.1), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=11.54, mode="split", tr="diag", imgs=[dict(img="hurrem_titian", focus=(0.5, 0.3)), dict(img="kosem_b", focus=(0.5, 0.35))]),
    dict(t=14.40, img="kosem_d", grade="dark", zoom=(1.6, 1.9), focus=(0.45, 0.3), tr="glitch"),
    # Hürrem
    dict(t=17.68, img="hurrem_rosa", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="iris"),
    dict(t=18.44, img="rohatyn", mode="card", maxw=640, maxh=860, tilt=2, tr="pushleft"),
    dict(t=18.98, img="tatar", zoom=(1.0, 1.1), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=21.22, img="kanuni", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="flash"),
    dict(t=24.34, mode="split", tr="bars", imgs=[dict(img="kanuni_prof", focus=(0.5, 0.3)), dict(img="hurrem_red", focus=(0.5, 0.35))]),
    dict(t=27.00, img="hurrem_titian", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="glitch"),
    dict(t=32.26, img="mektup", mode="card", maxw=480, maxh=1000, tilt=-2, tr="pushup"),
    dict(t=35.04, mode="split", tr="diag", imgs=[dict(img="mihrimah", focus=(0.5, 0.25)), dict(img="rustem", focus=(0.5, 0.25))]),
    dict(t=37.12, img="sigismund", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=39.74, img="kanuni_prof", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="dip"),
    # Kösem
    dict(t=43.48, img="kosem_a", mode="card", maxw=700, maxh=1000, tilt=2, tr="iris"),
    dict(t=44.12, img="ege", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushleft"),
    dict(t=46.40, img="ahmed", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="flash"),
    dict(t=47.20, img="kosem_c", mode="card", maxw=900, maxh=900, tilt=-2, tr="pushup"),
    dict(t=48.84, img="kosem_d", zoom=(1.0, 1.2), focus=(0.45, 0.3), tr="diag"),
    dict(t=52.18, img="murad", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="bars"),
    dict(t=55.70, img="kosem_b", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="zoomblur"),
    dict(t=59.10, img="divan", zoom=(1.0, 1.08), **{"from": (0.25, 0.5), "to": (0.7, 0.5)}, tr="pushup"),
    dict(t=61.66, img="kosem_d", zoom=(1.5, 1.8), focus=(0.45, 0.28), tr="glitch"),
    dict(t=63.46, img="ibrahim", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=65.74, img="mehmed4", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=68.98, mode="plate", bg="kosem_d", tr="iris"),
    dict(t=71.04, img="kosem_b", grade="std", zoom=(1.1, 1.3), focus=(0.5, 0.35), tr="zoomblur"),
    # Karşılaştırma
    dict(t=73.42, mode="split", tr="bars", imgs=SPLIT_HK),
    # Sonları
    dict(t=79.24, img="harem_room", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.5), tr="dip"),
    dict(t=80.98, img="turbe", zoom=(1.0, 1.12), **{"from": (0.35, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=84.56, img="kanuni_turbe", mode="card", maxw=700, maxh=950, tilt=2, tr="diag"),
    dict(t=86.64, img="kosem_a", mode="card", grade="dark", maxw=700, maxh=1000, tilt=-2, tr="glitch"),
    dict(t=88.92, img="harem_room", zoom=(1.0, 1.15), **{"from": (0.6, 0.5), "to": (0.35, 0.5)}, tr="pushleft"),
    dict(t=90.12, img="turhan", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="flash"),
    dict(t=91.56, img="olum", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="glitch"),
    dict(t=94.50, img="istanbul", grade="bw", zoom=(1.0, 1.1), focus=(0.5, 0.55), tr="dip"),
    # Final
    dict(t=97.34, img="hurrem_red", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="iris"),
    dict(t=100.00, img="kosem_d", zoom=(1.0, 1.12), focus=(0.45, 0.3), tr="pushup"),
    dict(t=101.72, mode="split", tr="bars", imgs=SPLIT_HK),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

R1 = [(330 + 120 * 0, 0)]
OVERLAYS = [
    dict(type="vs", t0=0.0, t1=3.8),
    dict(type="tagpair", t0=0.0, t1=3.8, tags=[("HÜRREM", 300, 0.05), ("KÖSEM", 1060, 2.36)]),
    dict(type="kinetic", t0=6.58, t1=9.15, text="PADİŞAHLAR BİLE\nGÖLGEDE KALDI", y=880, size=100, style="black"),
    dict(type="label", t0=9.4, t1=11.45, title="Esir Pazarı", sub="İstanbul", y=420),
    dict(type="vs", t0=11.6, t1=14.35),
    dict(type="kinetic", t0=14.66, t1=17.6, text="SADECE BİRİ\nDEVLETİ YÖNETTİ", y=640, size=110),
    # Hürrem
    dict(type="item", n=1, title="HÜRREM SULTAN", t0=17.7, t1=43.35),
    dict(type="label", t0=17.9, t1=18.4, title="Hürrem Sultan", sub="~1505 – 1558", y=420),
    dict(type="label", t0=18.5, t1=18.95, title="Rohatyn · Rutenya", sub="Bugün Ukrayna", y=420),
    dict(type="label", t0=21.4, t1=24.3, title="Kanuni Sultan Süleyman", sub="1494 – 1566", y=420),
    dict(type="stamp", t0=25.9, t1=26.95, text="NİKÂH", y=960, size=150, color=(255, 214, 10), rot=-6),
    dict(type="kinetic", t0=27.0, t1=28.7, text="KURALLARI YIKTI", y=700, size=120, style="red"),
    dict(type="counter", t0=28.76, t1=31.9, **{"from": 0, "to": 5}, fmt="{} ŞEHZADE", dur=0.6, y=760, size=170),
    dict(type="label", t0=32.4, t1=35.0, title="Saray mektupları", sub="Tuğralı Osmanlı belgesi", y=420),
    dict(type="kinetic", t0=33.72, t1=35.0, text="GÖZÜ KULAĞI", y=1060, size=110, style="black"),
    dict(type="tagpair", t0=35.04, t1=37.05, tags=[("MİHRİMAH · KIZI", 420, 35.04), ("RÜSTEM PAŞA · SADRAZAM", 1060, 35.36)]),
    dict(type="label", t0=37.3, t1=39.7, title="II. Zygmunt August", sub="Lehistan Kralı", y=420),
    dict(type="kinetic", t0=40.68, t1=43.4, text="GÜCÜ BİR\nADAMA BAĞLIYDI", y=640, size=110, style="black"),
    # Kösem
    dict(type="item", n=2, title="KÖSEM SULTAN", t0=43.5, t1=72.95),
    dict(type="label", t0=43.6, t1=44.05, title="Kösem Sultan", sub="~1589 – 1651", y=420),
    dict(type="label", t0=44.3, t1=46.35, title="Ege Adaları", sub="Kösem'in memleketi", y=420),
    dict(type="label", t0=46.5, t1=47.15, title="I. Ahmed", sub="Kösem'in eşi", y=420),
    dict(type="kinetic", t0=47.2, t1=48.8, text="HASEKİ SULTAN", y=1080, size=110),
    dict(type="kinetic", t0=49.84, t1=52.1, text="ASIL GÜÇ\nŞİMDİ BAŞLIYOR", y=640, size=110, style="black"),
    dict(type="label", t0=52.3, t1=55.6, title="IV. Murad", sub="Kösem'in oğlu · 1623", y=420),
    dict(type="counter", t0=54.7, t1=55.65, **{"from": 0, "to": 11}, fmt="{} YAŞINDA", dur=0.5, y=780, size=170),
    dict(type="stamp", t0=57.06, t1=59.0, text="NAİB", y=820, size=190, color=(255, 214, 10), rot=-6),
    dict(type="kinetic", t0=60.44, t1=61.6, text="EMİRLER", y=700, size=150, style="black"),
    dict(type="kinetic", t0=62.14, t1=63.4, text="KARARLAR ONDA", y=1060, size=110),
    dict(type="label", t0=63.6, t1=65.7, title="Sultan İbrahim", sub="Kösem'in oğlu", y=420),
    dict(type="label", t0=65.9, t1=68.9, title="IV. Mehmed", sub="Kösem'in torunu", y=420),
    dict(type="roster", t0=68.98, t1=71.0, size=180, items=[
        ("ahmed", "I. AHMED", 69.00, (190, 520)), ("mustafa1", "I. MUSTAFA", 69.18, (420, 520)),
        ("osman2", "II. OSMAN", 69.36, (650, 520)), ("mustafa1", "I. MUSTAFA", 69.54, (880, 520)),
        ("murad", "IV. MURAD", 69.72, (300, 830)), ("ibrahim", "İBRAHİM", 69.90, (530, 830)),
        ("mehmed4", "IV. MEHMED", 70.08, (760, 830))]),
    dict(type="kinetic", t0=69.3, t1=71.0, text="7 PADİŞAH", y=1070, size=120),
    dict(type="counter", t0=71.6, t1=72.95, **{"from": 0, "to": 48}, fmt="{} YIL", dur=0.7, y=780, size=200),
    # Karşılaştırma
    dict(type="vs", t0=73.42, t1=79.2),
    dict(type="tagpair", t0=73.5, t1=79.2, tags=[("AŞK HİKÂYESİ", 300, 74.78), ("İKTİDAR HİKÂYESİ", 1060, 77.62)]),
    # Sonları
    dict(type="item", n=3, title="SONLARI", t0=79.3, t1=97.25),
    dict(type="label", t0=81.1, t1=84.5, title="Hürrem Sultan Türbesi", sub="Süleymaniye · 1558", y=420),
    dict(type="label", t0=84.7, t1=86.6, title="Kanuni'nin Türbesi", sub="Hürrem'in hemen yanında", y=420),
    dict(type="counter", t0=87.42, t1=88.9, **{"from": 1600, "to": 1651}, dur=0.7, y=780, size=200),
    dict(type="label", t0=89.0, t1=90.05, title="Topkapı Haremi", sub="Kösem'in öldürüldüğü saray", y=420),
    dict(type="label", t0=90.2, t1=91.5, title="Turhan Sultan", sub="Kösem'in gelini · temsilî gravür", y=420),
    dict(type="stamp", t0=92.58, t1=94.45, text="BOĞULDU", y=760, size=150),
    dict(type="counter", t0=95.5, t1=97.25, **{"from": 0, "to": 3}, fmt="{} GÜN YAS", dur=0.4, y=760, size=160),
    # Final
    dict(type="kinetic", t0=98.52, t1=99.95, text="KALBİNİ", y=700, size=170),
    dict(type="kinetic", t0=100.52, t1=101.65, text="İMPARATORLUĞU", y=700, size=130, style="red"),
    dict(type="vs", t0=101.72, t1=DURATION + 1),
    dict(type="tagpair", t0=101.8, t1=DURATION + 1, tags=[("HÜRREM Mİ?", 300, 105.02), ("KÖSEM Mİ?", 1060, 105.78)]),
    dict(type="cta", t0=106.54, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(106.5, DURATION + 1)]


def CAPTION_Y(t):
    return 1235


PUNCH = [0.0, 13.36, 16.66, 26.38, 28.76, 42.46, 57.06, 60.44, 69.3, 77.62, 92.58, 98.52, 100.52]
SHAKE = [0.0, 27.0, 92.58]
FLASH = [(0.0, 0.3)]

MUSIC = [(0, 3.84, 3), (3.84, 17.68, 2), (17.68, 39.74, 2), (39.74, 43.48, 1), (43.48, 52.18, 2),
         (52.18, 73.42, 3), (73.42, 79.24, 2), (79.24, 86.64, 1), (86.64, 97.34, 0), (97.34, 101.72, 3),
         (101.72, DURATION, 1)]

_W = [s["t"] for s in SCENES[1:]]
SFX = [dict(name="impact", t=0.0, gain=0.95), dict(name="whoosh", t=0.1, gain=0.4), dict(name="hit", t=2.36, gain=0.5),
       dict(name="riser", t=11.54, gain=0.3, pre=True), dict(name="impact", t=14.66, gain=0.5),
       dict(name="riser", t=17.68, gain=0.35, pre=True), dict(name="hit", t=17.7, gain=0.5),
       dict(name="chains", t=19.0, gain=0.3), dict(name="shutter", t=21.22, gain=0.3), dict(name="bell", t=25.9, gain=0.4),
       dict(name="impact", t=27.0, gain=0.5), dict(name="pop", t=28.8, gain=0.35), dict(name="pop", t=29.1, gain=0.3),
       dict(name="paper", t=32.3, gain=0.35), dict(name="hit", t=33.72, gain=0.4), dict(name="shutter", t=37.12, gain=0.3),
       dict(name="heartbeat", t=40.0, gain=0.45), dict(name="hit", t=42.46, gain=0.5),
       dict(name="riser", t=43.48, gain=0.35, pre=True), dict(name="hit", t=43.5, gain=0.5),
       dict(name="shimmer", t=47.2, gain=0.3), dict(name="riser", t=52.18, gain=0.3, pre=True), dict(name="hit", t=52.2, gain=0.45),
       dict(name="pop", t=54.8, gain=0.35), dict(name="impact", t=57.06, gain=0.55), dict(name="hit", t=60.44, gain=0.45),
       dict(name="glitch", t=61.6, gain=0.3), dict(name="shutter", t=63.46, gain=0.3), dict(name="shutter", t=65.74, gain=0.3)]
SFX += [dict(name="pop", t=69.0 + 0.18 * k, gain=0.35) for k in range(7)]
SFX += [dict(name="hit", t=69.3, gain=0.4), dict(name="pop", t=71.7, gain=0.3), dict(name="impact", t=73.42, gain=0.5),
        dict(name="hit", t=74.78, gain=0.4), dict(name="hit", t=77.62, gain=0.45), dict(name="heartbeat", t=79.4, gain=0.45),
        dict(name="shimmer", t=81.0, gain=0.3), dict(name="glitch", t=86.6, gain=0.35), dict(name="heartbeat", t=88.9, gain=0.5),
        dict(name="sword", t=92.58, gain=0.5), dict(name="thunder", t=92.65, gain=0.5), dict(name="bell", t=94.6, gain=0.4),
        dict(name="riser", t=97.34, gain=0.3, pre=True), dict(name="hit", t=98.52, gain=0.5), dict(name="impact", t=100.52, gain=0.55),
        dict(name="impact", t=101.72, gain=0.5), dict(name="hit", t=105.02, gain=0.45), dict(name="hit", t=105.78, gain=0.45),
        dict(name="pop", t=106.6, gain=0.45)]
SFX += [dict(name="whoosh", t=w - 0.15, gain=0.3) for w in _W]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


if __name__ == "__main__":
    import json, sys
    json.dump(spec(), open(sys.argv[1], "w"))
