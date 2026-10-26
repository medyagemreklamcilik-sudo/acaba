"""Timeline for "Cumhuriyet ilan edilmeseydi ne olurdu?" (narration seconds)."""

DURATION = 125.9
CAP_Y = 1235
CX = 507

IMAGES = {
    "halife": "halife.jpg",
    "halife2": "halife2.jpg",
    "vahdettin": "vahdettin.jpg",
    "vahdettin_gemi": "vahdettin_gemi.jpg",
    "dolmabahce": "dolmabahce.jpg",
    "meclis_kalabalik": "meclis1920_6.jpg",
    "meclis": "meclis1920_0.jpg",
    "nutuk": "nutuk.jpg",
    "rauf": "rauf.jpg",
    "refet": "refet.jpg",
    "uclu": "uclu.jpg",
    "at_prof": "ataturkportre_4.jpg",
    "at_dark": "ataturkportre_7.jpg",
    "at_suit": "ataturkportre_1.jpg",
    "medrese": "medrese.jpg",
    "tekke": "tekke.jpg",
    "tahta": "tahta_5.jpg",
    "vekil": "kadinvekil_3.jpg",
    "sandik": "sandik_1.jpg",
    "rizasah": "rizasah.jpg",
    "faruk": "faruk.jpg",
    "anayasa": ("anayasa1924_2.jpg", (0.0, 0.0, 1.0, 1.0)),
    "kalabalik": "cumhuriyet_6.jpg",
    "osmanoglu": "osmanoglu.jpg",
    "bayrak": "bayrak_3.jpg",
}

FACES = {"halife": (0.5, 0.3), "halife2": (0.5, 0.25), "vahdettin": (0.5, 0.3), "rauf": (0.5, 0.3),
         "refet": (0.5, 0.25), "at_prof": (0.5, 0.3), "at_dark": (0.45, 0.3), "rizasah": (0.5, 0.3), "faruk": (0.5, 0.25)}

SCENES = [
    # hook
    dict(t=0.00, img="halife2", zoom=(1.3, 1.05), focus=(0.5, 0.25)),
    dict(t=4.56, img="dolmabahce", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="zoomblur"),
    # saltanat kalktı
    dict(t=8.94, img="meclis_kalabalik", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=12.54, img="vahdettin", mode="card", maxw=720, maxh=860, tilt=2, tr="pushleft"),
    dict(t=14.18, img="vahdettin_gemi", grade="dark", zoom=(1.0, 1.15), focus=(0.45, 0.5), tr="dip"),
    dict(t=17.36, img="dolmabahce", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=19.60, img="halife", mode="card", maxw=700, maxh=900, tilt=-2, tr="iris"),
    dict(t=22.60, img="dolmabahce", grade="dark", zoom=(1.15, 1.3), focus=(0.5, 0.5), tr="pushleft"),
    # Ankara'da muhalefet
    dict(t=27.06, img="meclis", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="bars"),
    dict(t=30.72, img="nutuk", mode="card", maxw=620, maxh=860, tilt=2, tr="pushup"),
    dict(t=31.34, img="rauf", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="zoomblur"),
    dict(t=38.34, img="uclu", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushleft"),
    # senaryo
    dict(t=40.52, mode="plate", bg="at_dark", tr="dip"),
    dict(t=42.80, img="halife2", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="flash"),
    dict(t=45.26, mode="split", tr="bars", imgs=[dict(img="meclis", focus=(0.5, 0.5)), dict(img="dolmabahce", focus=(0.5, 0.5))]),
    dict(t=48.74, mode="plate", bg="halife", tr="dip"),
    dict(t=50.66, img="halife", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.3), tr="glitch"),
    dict(t=56.20, img="medrese", zoom=(1.0, 1.15), focus=(0.5, 0.5), tr="pushup"),
    dict(t=59.02, img="tekke", zoom=(1.0, 1.12), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushleft"),
    dict(t=62.32, img="tahta", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="bars"),
    dict(t=68.40, img="vekil", mode="card", maxw=860, maxh=760, tilt=-2, tr="pushup"),
    dict(t=74.66, img="sandik", grade="dark", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="dip"),
    # öbür yüzü
    dict(t=77.46, mode="plate", bg="dolmabahce", tr="dip"),
    dict(t=79.50, img="rizasah", mode="card", maxw=700, maxh=900, tilt=2, tr="iris"),
    dict(t=87.02, img="faruk", mode="card", maxw=700, maxh=900, tilt=-2, tr="pushleft"),
    # asıl fark
    dict(t=90.84, img="at_prof", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="dip"),
    dict(t=95.68, img="anayasa", mode="card", maxw=860, maxh=720, tilt=2, tr="pushup"),
    dict(t=102.56, img="kalabalik", zoom=(1.0, 1.12), focus=(0.5, 0.5), tr="pushleft"),
    # bugün
    dict(t=106.28, img="osmanoglu", mode="card", maxw=820, maxh=820, tilt=-2, tr="iris"),
    dict(t=110.58, img="dolmabahce", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.5), tr="glitch"),
    dict(t=113.72, img="bayrak", zoom=(1.0, 1.12), focus=(0.5, 0.4), tr="flash"),
    dict(t=117.62, mode="plate", bg="at_dark", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- hook
    dict(type="title", t0=0.0, t1=4.5, lines=["CUMHURİYET", "OLMASAYDI?"], y=330, size=116),
    dict(type="kinetic", t0=5.92, t1=8.85, text="BAŞINDA\nBİR PADİŞAH", y=380, size=120, style="red"),
    # --- saltanat
    dict(type="kinetic", t0=8.94, t1=10.8, text="1 KASIM 1922", y=380, size=120),
    dict(type="stamp", t0=10.86, t1=12.45, text="SALTANAT KALDIRILDI", y=760, size=84),
    dict(type="label", t0=12.6, t1=14.1, title="Vahdettin", sub="son padişah", y=420),
    dict(type="label", t0=14.3, t1=17.3, title="17 Kasım 1922", sub="İngiliz savaş gemisi Malaya ile", y=420),
    dict(type="kinetic", t0=18.24, t1=19.5, text="HANEDAN BİTMEMİŞTİ", y=380, size=96, style="black"),
    dict(type="label", t0=19.7, t1=22.5, title="Abdülmecid Efendi", sub="son halife · 1922–1924", y=420),
    dict(type="handwrite", t0=24.14, t1=27.0, text="sarayda hâlâ bir şehzade", y=640, size=92, dur=0.8),
    # --- Ankara
    dict(type="kinetic", t0=28.58, t1=30.65, text="HERKES CUMHURİYET\nİSTEMİYORDU", y=380, size=96, style="black"),
    dict(type="label", t0=30.8, t1=31.3, title="Nutuk", sub="1927", y=420),
    dict(type="label", t0=31.4, t1=33.4, title="Rauf Bey (Orbay)", sub="Nutuk'tan", y=420),
    dict(type="quote", t0=33.4, t1=38.25, y=760, by="Rauf Bey · Nutuk",
         words=[("Ben", 33.50), ("vicdanen", 34.06), ("ve", 34.76), ("hissen", 34.98), ("saltanata", 35.48),
                ("ve", 36.16), ("hilafete", 36.42), ("bağlıyım.", 36.88)]),
    dict(type="label", t0=38.4, t1=40.45, title="Refet Paşa da katıldı", sub="Kâzım Karabekir · Rauf Bey · Refet Paşa", y=420),
    # --- senaryo
    dict(type="kinetic", t0=40.52, t1=41.45, text="ŞİMDİ DÜŞÜN", y=500, size=130),
    dict(type="kinetic", t0=41.50, t1=42.75, text="CUMHURİYET", y=760, size=130),
    dict(type="pencross", t0=42.16, t1=42.75, cx=CX, cy=760, r=230),
    dict(type="label", t0=43.0, t1=45.2, title="Devletin başı: Halife", sub="Abdülmecid Efendi", y=420),
    dict(type="tagpair", t0=45.4, t1=48.65, tags=[("ANKARA: MECLİS", 380, 45.26), ("İSTANBUL: HANEDAN", 1060, 46.86)]),
    dict(type="kinetic", t0=48.74, t1=50.6, text="NELER OLMAZDI?", y=600, size=120),
    dict(type="item", n=1, title="HALİFELİK KALDIRILAMAZDI", t0=50.7, t1=62.25),
    dict(type="pencross", t0=52.54, t1=56.1, cx=CX, cy=760, r=200),
    dict(type="label", t0=56.3, t1=58.95, title="Medreseler · şer'iye mahkemeleri", sub="1924'te kapatıldı", y=560),
    dict(type="label", t0=59.1, t1=62.25, title="Tekke ve zaviyeler", sub="1925'te kapatıldı", y=560),
    dict(type="item", n=2, title="HARF DEVRİMİ", t0=62.4, t1=68.3),
    dict(type="handwrite", t0=63.58, t1=68.3, text="halife onaylar mıydı?", y=640, size=96, dur=0.8),
    dict(type="item", n=3, title="KADIN HAKLARI", t0=68.5, t1=77.4),
    dict(type="tagpair", t0=72.5, t1=74.6, tags=[("TÜRKİYE 1934", 1000, 68.86), ("FRANSA 1944", 1100, 72.50)]),
    dict(type="kinetic", t0=74.76, t1=77.4, text="HİLAFETTE\nGELİR MİYDİ?", y=600, size=110, style="red"),
    # --- öbür yüzü
    dict(type="kinetic", t0=77.46, t1=79.4, text="AMA İŞİN\nÖBÜR YÜZÜ", y=600, size=110),
    dict(type="label", t0=79.6, t1=86.9, title="Rıza Şah", sub="İran · 1925–1941", y=420),
    dict(type="handwrite", t0=83.7, t1=86.9, text="tahtta kalıp reform", y=1060, size=88, dur=0.8),
    dict(type="label", t0=87.1, t1=90.75, title="Kral Faruk", sub="Mısır · 1952'de devrildi", y=420),
    # --- asıl fark
    dict(type="kinetic", t0=90.84, t1=93.2, text="ASIL FARK", y=380, size=140),
    dict(type="handwrite", t0=93.28, t1=95.6, text="padişahı seçimle değiştiremezdin", y=640, size=80, dur=0.9),
    dict(type="label", t0=95.8, t1=99.4, title="1924 Anayasası", sub="Teşkilât-ı Esasiye Kanunu", y=420),
    dict(type="quote", t0=99.45, t1=102.5, y=760, by="1924 Anayasası · Madde 3",
         words=[("Hâkimiyet", 99.54), ("bilâkaydüşart", 100.40), ("milletindir.", 101.32)]),
    dict(type="tagpair", t0=102.7, t1=106.2, tags=[("BİR AİLE", 380, 103.62), ("MİLLET", 1060, 105.06)]),
    dict(type="pencross", t0=104.52, t1=106.2, cx=300, cy=380, r=140),
    # --- bugün
    dict(type="label", t0=106.4, t1=110.5, title="Osmanoğlu ailesi", sub="bugün", y=420),
    dict(type="kinetic", t0=111.36, t1=113.65, text="TAHTTA\nONLARDAN BİRİ", y=380, size=110, style="black"),
    dict(type="tagpair", t0=113.8, t1=117.55, tags=[("VATANDAŞ", 380, 114.52), ("TEBAA", 1060, 115.98)]),
    dict(type="pencross", t0=115.10, t1=117.55, cx=300, cy=380, r=140),
    # --- final
    dict(type="kinetic", t0=117.62, t1=DURATION + 1, text="SENCE?", y=330, size=150),
    dict(type="tagpair", t0=120.3, t1=DURATION + 1, tags=[("DAHA GÜÇLÜ", 560, 121.22), ("DAHA GERİDE", 860, 122.68)]),
    dict(type="cta", t0=123.9, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 4.5), (33.4, 38.25), (99.45, 102.5), (117.62, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [4.56, 10.86, 42.16, 52.54, 90.84, 115.98]
SHAKE = [10.86, 42.16]
FLASH = [(42.80, 0.2), (113.72, 0.2)]

MUSIC = [(0, 8.94, 2), (8.94, 27.06, 1), (27.06, 40.52, 2), (40.52, 77.46, 2), (77.46, 90.84, 1),
         (90.84, 106.28, 3), (106.28, 117.62, 2), (117.62, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="impact", t=0.05, gain=0.8), dict(name="hit", t=5.92, gain=0.4), dict(name="impact", t=10.86, gain=0.55),
       dict(name="hit", t=42.16, gain=0.45), dict(name="hit", t=52.54, gain=0.4), dict(name="riser", t=90.84, gain=0.25, pre=True),
       dict(name="impact", t=90.84, gain=0.5), dict(name="hit", t=115.98, gain=0.45), dict(name="pop", t=123.9, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.3) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="halife", focus=(0.5, 0.36), zoom=1.1, lines=["CUMHURİYET", "OLMASAYDI?"], size=124, style="white", y=220,
             marks=[dict(type="pencircle", cx=560, cy=700, rx=260, ry=300, seed=3),
                    dict(type="handwrite", text="devletin başı bu olurdu", x=CX, y=1420, size=96, dur=0.1)])
