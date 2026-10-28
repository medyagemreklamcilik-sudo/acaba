"""Timeline for "Atatürk vatan haini mi? O zaman bu tarihi nasıl açıklayacaksınız?" (narration seconds)."""

DURATION = 172.7
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "mk1905", "sam", "hareket", "hareket2", "mart31", "trablus_arap", "trablus", "trablus3", "canakkale", "anafarta",
    "siper", "diyarbakir", "bitlis", "suriye", "yildirim", "isgal", "isgal2", "bandirma", "havza", "amasya", "erzurum",
    "erzurum2", "sivas", "istifa", "idam_irade", "idam_buyruk", "vahdettin", "takvim", "borekci", "tbmm", "tbmm2",
    "sakarya", "kocatepe", "zafer", "nutuk", "mk_sert", "mk_son", "hakimiyet", "ileri"]}

FACES = {"mk1905": (0.48, 0.12, 0.4), "trablus_arap": (0.5, 0.2, 0.45), "canakkale": (0.43, 0.17, 0.28), "suriye": (0.5, 0.11, 0.35),
         "erzurum": (0.5, 0.17, 0.32), "mk_sert": (0.5, 0.38, 0.6), "mk_son": (0.5, 0.25), "vahdettin": (0.5, 0.35),
         "borekci": (0.5, 0.4), "sakarya": (0.66, 0.55)}

# (anahtar, etiket, lon, lat, ölçek)
JOURNEY = [
    ("sam", "ŞAM", 36.29, 33.51, 55),
    ("istanbul", "İSTANBUL", 28.97, 41.01, 60),
    ("trablus", "TRABLUSGARP · DERNE", 22.64, 32.77, 48),
    ("canakkale", "ÇANAKKALE · ARIBURNU", 26.28, 40.23, 110),
    ("mus", "MUŞ · BİTLİS", 41.49, 38.75, 72),
    ("halep", "SURİYE · FİLİSTİN", 37.16, 36.2, 52),
    ("samsun", "SAMSUN", 36.33, 41.29, 95),
    ("havza", "HAVZA", 35.66, 40.97, 140),
    ("amasya", "AMASYA", 35.83, 40.65, 140),
    ("erzurum", "ERZURUM", 41.27, 39.9, 75),
    ("sivas", "SİVAS", 37.02, 39.75, 75),
    ("ankara", "ANKARA", 32.85, 39.93, 85),
    ("sakarya", "SAKARYA", 32.15, 39.58, 120),
    ("kocatepe", "KOCATEPE · AFYON", 30.62, 38.66, 100),
]


def J(t, stop, year, portrait, rank, role, **kw):
    return dict(t=t, mode="journey", stop=stop, year=year, portrait=portrait, rank=rank, role=role, **kw)


SCENES = [
    # kanca
    dict(t=0.00, img="mk_sert", grade="dark", zoom=(1.35, 1.05), focus=(0.5, 0.22)),
    dict(t=4.90, mode="plate", bg="mk_sert", tr="glitch"),
    # 1905 Şam
    J(11.90, 0, "1905", "mk1905", "KURMAY YÜZBAŞI", "5. Ordu · Şam"),
    dict(t=16.34, img="sam", mode="card", maxw=820, maxh=1000, tilt=-2, tr="zoomblur"),
    # 1909 İstanbul
    J(20.50, 1, "1909", "mk1905", "KOLAĞASI", "Hareket Ordusu kurmay heyeti"),
    dict(t=23.06, img="mart31", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="flash"),
    dict(t=24.58, img="hareket", mode="card", maxw=880, maxh=760, tilt=2, tr="pushup"),
    # 1911 Trablusgarp
    J(27.90, 2, "1911", "trablus_arap", "KOLAĞASI", "Gönüllü subay"),
    dict(t=32.88, img="trablus3", zoom=(1.0, 1.2), focus=(0.3, 0.4), tr="pushleft"),
    dict(t=36.24, img="trablus_arap", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="zoomblur"),
    dict(t=41.00, img="trablus", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushup"),
    # 1915 Çanakkale
    J(44.00, 3, "1915", "canakkale", "YARBAY", "19. Tümen Komutanı"),
    dict(t=49.70, img="canakkale", zoom=(1.0, 1.15), focus=(0.45, 0.3), tr="flash"),
    dict(t=51.52, img="siper", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="pushup"),
    dict(t=53.34, img="anafarta", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushleft"),
    # 1916 Doğu
    J(56.40, 4, "1916", "suriye", "MİRLİVA", "16. Kolordu Komutanı"),
    # 1917-18 Suriye
    J(62.70, 5, "1918", "suriye", "MİRLİVA", "7. Ordu Komutanı"),
    dict(t=67.32, img="yildirim", zoom=(1.0, 1.15), focus=(0.4, 0.4), tr="bars"),
    dict(t=70.00, img="isgal", grade="dark", zoom=(1.0, 1.25), focus=(0.5, 0.5), tr="glitch"),
    # bitti mi?
    dict(t=74.04, mode="plate", bg="mk_sert", tr="dip"),
    # 1919
    J(76.90, 6, "1919", "erzurum", "MÜFETTİŞ", "9. Ordu Müfettişi", tint=True),
    dict(t=79.30, img="bandirma", mode="card", maxw=880, maxh=700, tilt=-2, tr="pushup"),
    J(82.30, 7, "1919", "erzurum", "MÜFETTİŞ", "Havza", tint="on"),
    J(85.40, 8, "1919", "erzurum", "MÜFETTİŞ", "Amasya Genelgesi", tint="on"),
    J(88.50, 9, "1919", "erzurum", "SİVİL", "Erzurum Kongresi", tint="on"),
    J(90.30, 10, "1919", "erzurum", "SİVİL", "Sivas Kongresi", tint="on"),
    # istifa
    dict(t=92.46, img="istifa", mode="card", maxw=760, maxh=1050, tilt=2, tr="flash"),
    dict(t=99.66, img="erzurum2", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="pushleft"),
    # idam
    dict(t=101.76, img="vahdettin", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="dip"),
    dict(t=105.04, img="idam_buyruk", mode="card", maxw=700, maxh=1050, tilt=-2, tr="glitch"),
    dict(t=108.98, img="idam_irade", mode="card", maxw=760, maxh=1080, tilt=2, tr="pushup"),
    dict(t=112.46, img="takvim", mode="card", maxw=700, maxh=1050, tilt=-2, tr="pushleft"),
    dict(t=116.56, img="borekci", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="zoomblur"),
    # Meclis ve zafer
    dict(t=120.42, mode="plate", bg="tbmm", tr="dip"),
    J(122.90, 11, "1920", "mk_sert", "TBMM BAŞKANI", "23 Nisan 1920", tint="on"),
    dict(t=125.22, img="tbmm", zoom=(1.0, 1.2), focus=(0.5, 0.5), tr="flash"),
    J(127.20, 12, "1921", "mk_sert", "BAŞKOMUTAN", "Sakarya Meydan Muharebesi", tint="on"),
    J(129.60, 13, "1922", "mk_sert", "BAŞKOMUTAN", "Büyük Taarruz", tint="on"),
    dict(t=131.80, img="kocatepe", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="flash"),
    dict(t=133.94, img="hakimiyet", mode="card", maxw=760, maxh=1080, tilt=2, tr="pushup"),
    # sorgu
    dict(t=138.90, mode="plate", bg="mk_son", tr="dip"),
    dict(t=149.56, img="mk_son", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.25), tr="pushup"),
    dict(t=155.04, img="nutuk", mode="card", maxw=640, maxh=900, tilt=-2, tr="flash"),
    dict(t=157.00, mode="plate", bg="nutuk", tr="dip"),
    dict(t=165.92, mode="plate", bg="mk_sert", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="title", t0=0.0, t1=4.85, lines=["ATATÜRK", "VATAN HAİNİ Mİ?"], y=330, size=120, style="red"),
    dict(type="stamp", t0=1.98, t1=4.85, text="TARİH KONUŞSUN", y=1000, size=110, color=YELLOW, rot=-6, fill=True),
    dict(type="kinetic", t0=5.0, t1=8.7, text="BU VİDEOYU\nİYİ İZLEYİN", y=760, size=130),
    dict(type="tagpair", t0=8.82, t1=11.8, tags=[("YORUM DEĞİL", 900, 9.94), ("TARİH", 1040, 10.78)]),
    # --- Şam
    dict(type="label", t0=16.5, t1=20.4, title="Vatan ve Hürriyet Cemiyeti", sub="Şam · 1906", y=420),
    # --- 1909
    dict(type="title", t0=23.06, t1=24.5, lines=["31 MART VAKASI"], y=330, size=110, style="red"),
    dict(type="label", t0=24.7, t1=27.8, title="Hareket Ordusu", sub="1909 · kurmay heyeti", y=420),
    # --- Trablusgarp
    dict(type="stamp", t0=31.92, t1=32.8, text="İTALYAN İŞGALİ", y=1080, size=96, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=33.7, t1=36.1, text="NEREDEYSE\nİMKÂNSIZ", y=380, size=120, style="black"),
    dict(type="stamp", t0=36.96, t1=38.7, text="GÖNÜLLÜ", y=820, size=150, color=YELLOW, rot=-7, fill=True),
    dict(type="handwrite", t0=38.76, t1=40.9, text="kılık değiştirdi", y=420, size=110, dur=0.6),
    dict(type="pencircle", t0=39.3, t1=40.9, cx=CX, cy=780, rx=300, ry=360, seed=5, color=RED),
    dict(type="label", t0=41.1, t1=43.9, title="Trablusgarp · 1911-12", sub="Tobruk ve Derne cephesi", y=420),
    # --- Çanakkale
    dict(type="kinetic", t0=46.26, t1=49.6, text="HEDEF:\nİSTANBUL", y=1050, size=110, style="red"),
    dict(type="label", t0=49.8, t1=51.4, title="Mustafa Kemal", sub="Çanakkale · 1915", y=420),
    dict(type="stamp", t0=52.66, t1=53.3, text="DURDURDU", y=820, size=150, color=YELLOW, rot=-7, fill=True),
    dict(type="label", t0=53.5, t1=56.3, title="Anafartalar Grup Komutanı", sub="Ağustos 1915", y=420),
    # --- Doğu
    dict(type="stamp", t0=61.74, t1=62.6, text="GERİ ALINDI", y=1080, size=110, color=YELLOW, rot=-6, fill=True),
    dict(type="label", t0=67.4, t1=69.9, title="Yıldırım Orduları", sub="1918 · Suriye cephesi", y=420),
    dict(type="stamp", t0=71.34, t1=73.9, text="İŞGAL", y=820, size=170, color=RED, rot=-8, fill=True),
    # --- bitti mi
    dict(type="kinetic", t0=74.04, t1=76.1, text="HİKÂYE BİTTİ Mİ?", y=760, size=110),
    dict(type="kinetic", t0=76.26, t1=76.85, text="HAYIR!", y=760, size=200, style="red"),
    # --- 1919
    dict(type="label", t0=79.4, t1=82.2, title="Bandırma Vapuru", sub="19 Mayıs 1919", y=420),
    dict(type="tagpair", t0=88.9, t1=92.3, tags=[("ERZURUM KONGRESİ", 1080, 88.82), ("SİVAS KONGRESİ", 1170, 89.62)]),
    # --- istifa
    dict(type="title", t0=92.46, t1=95.2, lines=["8 TEMMUZ 1919"], y=330, size=120),
    dict(type="stamp", t0=96.9, t1=99.5, text="İSTİFA", y=1060, size=150, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=98.1, t1=99.55, text="RÜTBESİ YOK", y=330, size=110, style="black"),
    dict(type="kinetic", t0=99.66, t1=101.6, text="AMA DEVAM", y=380, size=130),
    # --- idam
    dict(type="label", t0=101.9, t1=104.9, title="Sultan Vahdettin", sub="İstanbul Hükûmeti", y=420),
    dict(type="stamp", t0=107.18, t1=108.9, text="İDAM", y=820, size=210, color=RED, rot=-9, fill=True),
    dict(type="title", t0=105.1, t1=107.1, lines=["GIYABİ İDAM · 1920"], y=330, size=96, style="red"),
    dict(type="label", t0=109.0, t1=112.3, title="24 Mayıs 1920", sub="Vahdettin'in onay iradesi", y=330),
    dict(type="label", t0=112.5, t1=116.4, title="Şeyhülislam Dürrizade fetvası", sub="Takvim-i Vekâyi · Nisan 1920", y=330),
    dict(type="label", t0=116.7, t1=120.3, title="Rifat Börekçi", sub="Ankara Müftüsü · karşı fetva", y=420),
    # --- Meclis, zafer
    dict(type="kinetic", t0=120.42, t1=122.8, text="İDAM KARARI\nDURDURDU MU?", y=760, size=110, style="black"),
    dict(type="title", t0=125.22, t1=127.1, lines=["23 NİSAN 1920"], y=330, size=120),
    dict(type="stamp", t0=132.98, t1=133.85, text="ZAFER", y=1050, size=170, color=YELLOW, rot=-7, fill=True),
    dict(type="title", t0=133.94, t1=138.8, lines=["29 EKİM 1923"], y=330, size=120),
    # --- sorgu
    dict(type="kinetic", t0=138.9, t1=140.0, text="ŞİMDİ SORUYORUM", y=330, size=104),
    dict(type="tagpair", t0=140.04, t1=146.2, tags=[("TRABLUSGARP'A GÖNÜLLÜ", 520, 140.04), ("ÇANAKKALE'DE CEPHEDE", 660, 141.92),
                                                    ("HAKKINDA İDAM KARARI", 800, 143.7)]),
    dict(type="stamp", t0=147.16, t1=149.45, text="VATAN HAİNİ?", y=1020, size=140, color=RED, rot=-7, fill=True),
    dict(type="kinetic", t0=151.48, t1=153.0, text="ELEŞTİRMEK BAŞKA", y=380, size=104),
    dict(type="kinetic", t0=153.02, t1=154.95, text="TARİHİ YOK SAYMAK\nBAŞKA!", y=380, size=104, style="red"),
    dict(type="label", t0=155.2, t1=156.9, title="Nutuk · 1927", sub="Mustafa Kemal Atatürk", y=330),
    dict(type="quote", t0=157.0, t1=165.8, y=760, by="Nutuk'tan özet · Millî Mücadele'nin başı",
         words=[("Padişahsız,", 157.74), ("halifesiz", 159.02), ("kurtuluş", 159.88), ("yolu", 160.38), ("arayan:", 160.64),
                ("dinsiz,", 161.78), ("vatansız,", 162.94), ("hain!", 163.98)]),
    # --- final
    dict(type="kinetic", t0=165.92, t1=DURATION + 1, text="BU TARİHİ\nNASIL AÇIKLIYORSUNUZ?", y=330, size=96),
    dict(type="cta", t0=170.9, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 4.85), (157.0, 165.8), (165.92, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [0.0, 12.14, 28.24, 44.3, 52.66, 71.34, 76.26, 96.9, 107.18, 132.98, 147.16]
SHAKE = [0.0, 76.26, 107.18, 147.16]
FLASH = [(28.24, 0.12), (76.26, 0.18), (107.18, 0.2), (132.98, 0.15)]

MUSIC = [(0, 11.9, 3), (11.9, 44.0, 2), (44.0, 74.0, 3), (74.0, 77.0, 1), (77.0, 101.7, 2), (101.7, 120.4, 3),
         (120.4, 138.9, 3), (138.9, 157.0, 2), (157.0, 165.9, 2), (165.9, DURATION, 1)]

SFX = [dict(name="impact", t=0.05, gain=0.6), dict(name="hit", t=1.98, gain=0.3), dict(name="impact", t=12.14, gain=0.35),
       dict(name="whoosh", t=27.9, gain=0.2), dict(name="whoosh", t=44.0, gain=0.2), dict(name="hit", t=52.66, gain=0.3),
       dict(name="hit", t=71.34, gain=0.3), dict(name="impact", t=76.26, gain=0.55), dict(name="hit", t=96.9, gain=0.3),
       dict(name="thunder", t=107.18, gain=0.35), dict(name="riser", t=132.98, gain=0.2, pre=True),
       dict(name="impact", t=132.98, gain=0.5), dict(name="hit", t=147.16, gain=0.35), dict(name="pop", t=170.9, gain=0.35)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="mk_sert", grade="dark", focus=(0.5, 0.25), zoom=1.05, lines=["ATATÜRK", "VATAN HAİNİ Mİ?"], y=250, size=118,
             style="red", stamp="BELGELERLE CEVAP", stamp_y=1390, stamp_size=104, stamp_color=YELLOW, stamp_rot=-6)
