"""Timeline for "Kadir Mısıroğlu'nun iddiaları ve belgeler" (narration seconds)."""

DURATION = 166.1
CAP_Y = 1235
CX = 507
RED = (230, 40, 40)
YELLOW = (255, 214, 10)

IMAGES = {k: k + ".jpg" for k in [
    "popcorn", "misiroglu", "misiroglu2", "agamemnon", "mondros", "calthorpe", "isgal", "vahdettin", "damat", "mk1919",
    "harington", "malta", "isgal1920", "orient", "fetva", "durrizade", "inzibatiye", "malaya", "kacis", "lloyd", "ismet",
    "lozan", "meclis1924", "evren", "resmigazete", "londra", "mk_sert", "mk_son"]}

FACES = {"misiroglu": (0.5, 0.3), "misiroglu2": (0.5, 0.35), "calthorpe": (0.5, 0.25), "vahdettin": (0.5, 0.2),
         "damat": (0.55, 0.35), "mk1919": (0.45, 0.3), "harington": (0.5, 0.25), "durrizade": (0.62, 0.35),
         "lloyd": (0.5, 0.25), "evren": (0.5, 0.3), "mk_sert": (0.5, 0.35), "mk_son": (0.5, 0.3), "ismet": (0.3, 0.2)}

SCENES = [
    # kanca: patlamış mısır
    dict(t=0.00, img="popcorn", zoom=(1.0, 1.35), focus=(0.5, 0.45)),
    dict(t=2.80, img="misiroglu", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="glitch"),
    dict(t=6.62, mode="plate", bg="misiroglu2", tr="dip"),
    dict(t=11.40, img="mk_sert", grade="dark", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="flash"),
    # 1. iddia
    dict(t=14.62, img="mk1919", zoom=(1.0, 1.15), focus=(0.45, 0.3), tr="pushup"),
    dict(t=22.40, mode="plate", bg="mk1919", tr="dip"),
    dict(t=32.20, img="agamemnon", mode="card", maxw=880, maxh=700, tilt=-2, tr="flash"),
    dict(t=35.28, img="mondros", mode="card", maxw=820, maxh=900, tilt=2, tr="pushleft"),
    dict(t=36.40, img="isgal", zoom=(1.0, 1.2), focus=(0.6, 0.5), tr="pushup"),
    dict(t=38.50, img="vahdettin", zoom=(1.0, 1.15), focus=(0.5, 0.2), tr="zoomblur"),
    dict(t=40.18, img="damat", zoom=(1.0, 1.15), focus=(0.55, 0.35), tr="pushleft"),
    dict(t=46.00, img="calthorpe", zoom=(1.0, 1.15), focus=(0.5, 0.25), tr="glitch"),
    dict(t=52.00, img="isgal1920", mode="card", maxw=820, maxh=900, tilt=-2, tr="flash"),
    dict(t=54.18, img="malta", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    dict(t=55.10, mode="plate", bg="malta", tr="dip"),
    # İngiliz ajanı?
    dict(t=60.18, img="mk_sert", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.35), tr="glitch"),
    dict(t=63.64, mode="split", tr="bars", imgs=[dict(img="vahdettin", focus=(0.5, 0.2)), dict(img="lloyd", focus=(0.5, 0.25))]),
    dict(t=69.24, img="fetva", mode="card", maxw=700, maxh=1050, tilt=-2, tr="pushup"),
    dict(t=72.66, img="inzibatiye", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=75.40, img="kacis", zoom=(1.0, 1.2), focus=(0.4, 0.4), tr="flash"),
    dict(t=81.84, img="malaya", mode="card", maxw=860, maxh=1080, tilt=2, tr="zoomblur"),
    # 2. iddia: Lozan
    dict(t=85.92, img="ismet", zoom=(1.0, 1.15), focus=(0.3, 0.25), tr="glitch"),
    dict(t=88.74, mode="treaty", layer="sevr", tr="dip",
         marks=[(91.0, "YUNANİSTAN"), (93.2, "ERMENİSTAN"), (94.92, "BOĞAZLAR"), (95.6, "İTALYA"), (96.2, "FRANSA")]),
    dict(t=98.04, mode="treaty", layer="lozan", tr="flash"),
    # 3. iddia: adalar
    dict(t=102.16, mode="treaty", layer="adalar", tr="dip", marks=[(105.48, "onikiada"), (109.02, "1914"), (116.0, "tr")]),
    # 4. iddia: hilafet
    dict(t=119.68, img="lozan", mode="card", maxw=880, maxh=700, tilt=-2, tr="flash"),
    dict(t=127.42, img="meclis1924", zoom=(1.0, 1.2), focus=(0.5, 0.45), tr="pushup"),
    # 1980 ve sonrası
    dict(t=132.86, img="evren", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="glitch"),
    dict(t=136.46, img="misiroglu2", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=138.10, img="resmigazete", mode="card", maxw=700, maxh=1050, tilt=2, tr="pushup"),
    dict(t=141.36, mode="plate", bg="londra", tr="dip"),
    dict(t=147.06, img="londra", zoom=(1.0, 1.25), focus=(0.5, 0.35), tr="zoomblur"),
    # kapanış
    dict(t=152.62, img="mk_son", zoom=(1.0, 1.15), focus=(0.5, 0.3), tr="dip"),
    dict(t=160.90, mode="plate", bg="mk_sert", tr="dip"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

OVERLAYS = [
    # --- kanca
    dict(type="quote", t0=0.0, t1=2.75, y=1100, by="Kadir Mısıroğlu",
         words=[("Keşke", 0.0), ("Yunan", 0.56), ("galip", 0.98), ("gelseydi.", 1.34)]),
    dict(type="label", t0=3.0, t1=6.5, title="Kadir Mısıroğlu", sub="kendine tarihçi diyen", y=420),
    dict(type="tagpair", t0=7.7, t1=11.3, tags=[("HİLAFET YIKILMAZDI", 380, 8.86), ("ŞERİAT YIKILMAZDI", 520, 9.72)]),
    dict(type="kinetic", t0=11.4, t1=14.5, text="BELGELER\nNE DİYOR?", y=760, size=130),
    # --- 1. iddia
    dict(type="title", t0=14.62, t1=18.1, lines=["1. İDDİA"], y=330, size=110, style="red"),
    dict(type="kinetic", t0=16.82, t1=22.3, text="\"DANIŞIKLI\nDÖVÜŞ\"", y=520, size=110, style="black"),
    dict(type="kinetic", t0=22.4, t1=24.8, text="DİYELİM Kİ ÖYLE", y=760, size=110),
    dict(type="kinetic", t0=25.1, t1=32.1, text="BU YETKİYİ\nNEREDEN BULDU?", y=760, size=110, style="red"),
    dict(type="title", t0=32.2, t1=35.2, lines=["30 EKİM 1918 · MONDROS"], y=330, size=90),
    dict(type="label", t0=35.4, t1=36.3, title="Mondros'u imzalayan Osmanlı heyeti", sub="Agamemnon zırhlısı", y=330),
    dict(type="label", t0=36.5, t1=38.4, title="13 Kasım 1918", sub="İtilaf donanması İstanbul'da", y=420),
    dict(type="label", t0=38.6, t1=40.1, title="Sultan Vahdettin", sub="Saltanat hükümeti", y=420),
    dict(type="label", t0=40.3, t1=45.9, title="Sadrazam Damat Ferid Paşa", sub="1919 · padişahın hükümeti", y=420),
    dict(type="stamp", t0=43.78, t1=45.9, text="TAYİN: OSMANLI HÜKÜMETİ", y=1060, size=84, color=YELLOW, rot=-6, fill=True),
    dict(type="label", t0=46.1, t1=51.9, title="Amiral Calthorpe", sub="İngiliz Yüksek Komiseri · İstanbul", y=420),
    dict(type="kinetic", t0=50.32, t1=51.9, text="GERİ ÇAĞIRIN!", y=1060, size=110, style="red"),
    dict(type="label", t0=52.1, t1=54.1, title="16 Mart 1920", sub="İstanbul'un resmen işgali", y=330),
    dict(type="stamp", t0=54.18, t1=55.0, text="MALTA'YA SÜRGÜN", y=1050, size=104, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=55.1, t1=60.0, text="DANIŞIKLI DÖVÜŞTE\nSÜRGÜN OLMAZ", y=760, size=100, style="black"),
    # --- İngiliz ajanı?
    dict(type="stamp", t0=60.8, t1=63.5, text="\"İNGİLİZ AJANI\"?", y=1050, size=130, color=RED, rot=-7, fill=True),
    dict(type="tagpair", t0=63.7, t1=69.1, tags=[("SALTANAT", 380, 67.08), ("İNGİLTERE · LLOYD GEORGE", 1060, 65.06)]),
    dict(type="vs", t0=64.0, t1=69.1),
    dict(type="label", t0=69.4, t1=72.5, title="Şeyhülislam Dürrizade fetvası", sub="Takvim-i Vekâyi · Nisan 1920", y=330),
    dict(type="label", t0=72.8, t1=75.3, title="Kuva-yı İnzibâtiye", sub="Halife Ordusu · İngiliz desteğiyle", y=420),
    dict(type="title", t0=75.4, t1=81.7, lines=["17 KASIM 1922"], y=330, size=120),
    dict(type="label", t0=78.7, t1=81.7, title="Vahdettin ayrılıyor", sub="İngiliz subaylar eşliğinde", y=520),
    dict(type="stamp", t0=84.34, t1=85.8, text="HMS MALAYA", y=1100, size=120, color=RED, rot=-6, fill=True),
    dict(type="label", t0=82.0, t1=84.2, title="İngiliz zırhlısı", sub="\"Sultan İngiliz himayesinde\" · 1922 basını", y=330),
    # --- 2. iddia
    dict(type="title", t0=85.92, t1=88.6, lines=["2. İDDİA"], y=330, size=110, style="red"),
    dict(type="label", t0=86.2, t1=88.6, title="İsmet Paşa", sub="Lozan · 1923", y=520),
    dict(type="kinetic", t0=87.12, t1=88.6, text="\"LOZAN HEZİMET\"", y=760, size=104, style="black"),
    dict(type="title", t0=89.8, t1=97.9, lines=["SEVR · 1920"], y=330, size=110, style="red"),
    dict(type="stamp", t0=100.16, t1=101.9, text="KAPİTÜLASYONLAR KALKTI", y=1150, size=80, color=YELLOW, rot=-5, fill=True),
    # --- 3. iddia
    dict(type="title", t0=102.16, t1=105.3, lines=["3. İDDİA"], y=330, size=110, style="red"),
    dict(type="kinetic", t0=103.42, t1=105.3, text="\"ADALARI VERDİK\"", y=760, size=104, style="black"),
    dict(type="stamp", t0=112.94, t1=115.8, text="CUMHURİYETTEN ÖNCE", y=1250, size=96, color=RED, rot=-5, fill=True),
    # --- 4. iddia
    dict(type="title", t0=119.68, t1=123.5, lines=["4. İDDİA"], y=330, size=110, style="red"),
    dict(type="kinetic", t0=120.94, t1=123.5, text="\"GİZLİ ŞART\"", y=1060, size=110, style="black"),
    dict(type="counter", t0=124.02, t1=127.3, **{"from": 0, "to": 143}, fmt="{} MADDE", dur=0.7, y=330, size=130),
    dict(type="stamp", t0=125.96, t1=127.3, text="HİLAFET: YOK", y=1080, size=130, color=RED, rot=-7, fill=True),
    dict(type="title", t0=127.42, t1=132.7, lines=["3 MART 1924"], y=330, size=120),
    dict(type="label", t0=129.0, t1=132.7, title="TBMM", sub="Hilafeti kaldıran kanun", y=520),
    # --- 1980 ve sonrası
    dict(type="title", t0=133.96, t1=136.3, lines=["12 EYLÜL 1980"], y=330, size=110),
    dict(type="label", t0=136.6, t1=138.0, title="Kadir Mısıroğlu", sub="yurt dışına çıktı", y=420),
    dict(type="label", t0=138.2, t1=141.2, title="7 Eylül 1983 · Resmî Gazete", sub="Temsili sayfa", y=330),
    dict(type="stamp", t0=139.48, t1=141.2, text="VATANDAŞLIKTAN ÇIKARILDI", y=1100, size=80, color=RED, rot=-6, fill=True),
    dict(type="kinetic", t0=141.36, t1=144.0, text="HANGİ ÜLKEYİ\nSEÇTİ?", y=760, size=120),
    dict(type="handwrite", t0=144.14, t1=146.9, text="şeriatla yönetilen onca ülke...", y=760, size=76, dur=0.8),
    dict(type="stamp", t0=150.78, t1=152.5, text="İNGİLTERE", y=1050, size=170, color=RED, rot=-7, fill=True),
    # --- kapanış
    dict(type="kinetic", t0=155.26, t1=158.6, text="İŞGALCİNİN ZAFERİNİ\nDİLEMEK", y=380, size=96, style="red"),
    dict(type="kinetic", t0=158.68, t1=160.8, text="TARİHÇİLİK DEĞİL", y=380, size=110),
    dict(type="kinetic", t0=160.9, t1=DURATION + 1, text="NEDEN HÂLÂ\nYAYILIYOR?", y=330, size=120),
    dict(type="cta", t0=164.7, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.75), (88.74, 119.6), (160.9, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return 1440 if 88.74 <= t < 119.6 else CAP_Y


PUNCH = [2.8, 25.1, 32.2, 43.78, 54.18, 60.8, 84.34, 98.04, 125.96, 139.48, 150.78]
SHAKE = [54.18, 60.8, 125.96, 150.78]
FLASH = [(11.4, 0.12), (98.04, 0.18), (150.78, 0.15)]

MUSIC = [(0, 2.8, 0), (2.8, 14.62, 2), (14.62, 32.2, 2), (32.2, 60.18, 3), (60.18, 85.92, 3), (85.92, 119.68, 2),
         (119.68, 141.36, 3), (141.36, 152.62, 2), (152.62, 160.9, 3), (160.9, DURATION, 1)]

SFX = [dict(name="popcorn", t=0.0, gain=0.55), dict(name="hit", t=2.8, gain=0.3), dict(name="riser", t=25.1, gain=0.2, pre=True),
       dict(name="hit", t=43.78, gain=0.25), dict(name="hit", t=54.18, gain=0.3), dict(name="impact", t=60.8, gain=0.45),
       dict(name="hit", t=84.34, gain=0.3), dict(name="impact", t=98.04, gain=0.4), dict(name="hit", t=125.96, gain=0.3),
       dict(name="hit", t=139.48, gain=0.3), dict(name="impact", t=150.78, gain=0.45), dict(name="pop", t=164.7, gain=0.35)]
SFX += [dict(name="pen", t=144.14, gain=0.2)]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


COVER = dict(img="misiroglu", grade="dark", focus=(0.5, 0.3), zoom=1.05, lines=["\"KEŞKE YUNAN", "KAZANSAYDI\""], y=250, size=112,
             style="white", stamp="BELGELER KONUŞUYOR", stamp_y=1250, stamp_size=100, stamp_color=RED, stamp_rot=-6)
