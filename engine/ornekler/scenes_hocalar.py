"""Timeline for "Atatürk hocaları astı mı?" (narration seconds)."""

DURATION = 216.9
CAP_Y = 1235
CX = 507

IMAGES = {
    "at_prof": "ataturkportre_4.jpg",
    "at_dark": "ataturkportre_7.jpg",
    "at_suit": "ataturkportre_1.jpg",
    "said": "seyhsaid_4.jpg",
    "said_w": "seyhsaid_5.jpg",
    "said_cap": ("seyhsaid_6.jpg", (0.0, 0.0, 1.0, 0.78)),
    "said_crowd": "seyhsaid2_2.jpg",
    "said_map": "harita_1.jpg",
    "said_cartoon": "harita_0.jpg",
    "sark_kitap": "mahkeme_0.jpg",
    "diyarbakir": "diyarbakir_2.jpg",
    "atif": "atif_2.jpg",
    "atif_dark": "atif_3.jpg",
    "kitap": ("atifkitap_2.jpg", (0.0, 0.0, 1.0, 0.88)),
    "gazete": "atifkitap_6.jpg",
    "sapka": ("sapka_6.jpg", (0.0, 0.0, 1.0, 0.86)),
    "ankara_mahkeme": "mahkeme2_2.jpg",
    "belge": "beyanname_0.jpg",
    "ucak": ("yunanucak_1.jpg", (0.0, 0.0, 1.0, 0.9)),
    "menemen": "menemen_6.jpg",
    "kubilay": "kubilay_0.jpg",
    "kubilay_c": "kubilay_2.jpg",
    "hakimiyet": "divanharp_6.jpg",
    "menemen_kalabalik": "divanharp_4.jpg",
    "takvim": "durrizade_1.jpg",
    "hocalar": "ankarafetva_6.jpg",
    "diyanet_belge": "ankarafetva_7.jpg",
    "borekci": "ankarafetva_2.jpg",
    "arsiv": "arsiv_2.jpg",
    "elmalili": "elmalili_6.jpg",
    "hakdini": "hakdini_0.jpg",
    "akif": "akif_4.jpg",
}

FACES = {"said": (0.5, 0.3), "atif_dark": (0.5, 0.35), "kubilay": (0.5, 0.3)}

SCENES = [
    dict(t=0.00, img="at_prof", zoom=(1.25, 1.05), focus=(0.5, 0.4)),
    dict(t=2.44, mode="plate", bg="at_dark", tr="zoomblur"),
    dict(t=4.66, img="arsiv", zoom=(1.0, 1.15), focus=(0.5, 0.45), tr="pushup"),
    dict(t=9.80, img="ankara_mahkeme", grade="dark", zoom=(1.0, 1.1), **{"from": (0.35, 0.5), "to": (0.6, 0.5)}, tr="dip"),
    dict(t=14.80, mode="plate", bg="ankara_mahkeme", tr="pushup"),
    # 1 — Şeyh Said
    dict(t=17.36, img="said", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="iris"),
    dict(t=24.12, mode="plate", bg="said_cartoon", tr="pushleft"),
    dict(t=33.44, img="said_crowd", zoom=(1.0, 1.1), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushup"),
    dict(t=35.20, img="said_cap", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="flash"),
    dict(t=36.76, img="sark_kitap", mode="card", maxw=700, maxh=900, tilt=2, tr="pushleft"),
    dict(t=40.18, img="said_w", grade="dark", zoom=(1.0, 1.2), focus=(0.5, 0.35), tr="dip"),
    dict(t=43.84, mode="plate", bg="said", tr="pushup"),
    # 2 — İskilipli Âtıf
    dict(t=50.12, img="atif_dark", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="iris"),
    dict(t=52.66, img="atif", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.4), tr="dip"),
    dict(t=60.16, img="kitap", mode="card", maxw=700, maxh=900, tilt=-2, tr="pushup"),
    dict(t=65.96, img="sapka", zoom=(1.0, 1.1), **{"from": (0.35, 0.5), "to": (0.6, 0.5)}, tr="pushleft"),
    dict(t=68.82, mode="plate", bg="atif", tr="pushup"),
    dict(t=74.72, img="atif_dark", grade="dark", zoom=(1.2, 1.4), focus=(0.5, 0.4), tr="glitch"),
    dict(t=76.32, img="ankara_mahkeme", zoom=(1.0, 1.1), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="pushleft"),
    dict(t=78.66, img="arsiv", mode="card", maxw=740, maxh=900, tilt=2, tr="zoomblur"),
    dict(t=82.22, img="atif", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="pushup"),
    dict(t=87.42, img="belge", mode="card", maxw=640, maxh=920, tilt=-2, tr="pushleft"),
    dict(t=92.54, img="ucak", zoom=(1.0, 1.2), focus=(0.5, 0.4), tr="flash"),
    dict(t=99.36, mode="split", tr="bars", imgs=[dict(img="kitap", focus=(0.5, 0.35)), dict(img="ucak", focus=(0.5, 0.4))]),
    dict(t=105.62, img="atif_dark", grade="bw", zoom=(1.0, 1.15), focus=(0.5, 0.4), tr="dip"),
    dict(t=110.38, mode="plate", bg="ucak", tr="pushup"),
    # 3 — Menemen
    dict(t=117.68, img="menemen", zoom=(1.0, 1.1), **{"from": (0.3, 0.5), "to": (0.6, 0.5)}, tr="iris"),
    dict(t=122.06, mode="plate", bg="menemen", tr="dip"),
    dict(t=129.28, img="kubilay", zoom=(1.0, 1.15), focus=(0.5, 0.33), tr="flash"),
    dict(t=133.28, img="kubilay_c", grade="dark", zoom=(1.1, 1.3), focus=(0.5, 0.33), tr="glitch"),
    dict(t=134.52, img="menemen_kalabalik", grade="dark", zoom=(1.0, 1.1), focus=(0.5, 0.5), tr="pushup"),
    dict(t=137.10, img="hakimiyet", mode="card", maxw=700, maxh=950, tilt=2, tr="pushleft"),
    # Sonuç
    dict(t=142.54, mode="plate", bg="ankara_mahkeme", tr="dip"),
    # Diğer hocalar
    dict(t=154.68, img="hocalar", zoom=(1.0, 1.12), focus=(0.5, 0.45), tr="iris"),
    dict(t=158.14, img="takvim", mode="card", maxw=700, maxh=950, tilt=-2, tr="pushup"),
    dict(t=166.18, img="borekci", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="pushleft"),
    dict(t=170.74, mode="split", tr="bars", imgs=[dict(img="takvim", focus=(0.5, 0.3)), dict(img="borekci", focus=(0.5, 0.35))]),
    dict(t=175.74, img="diyanet_belge", mode="card", maxw=700, maxh=950, tilt=2, tr="pushup"),
    dict(t=183.56, img="elmalili", zoom=(1.0, 1.15), focus=(0.5, 0.35), tr="iris"),
    dict(t=190.64, img="hakdini", mode="card", maxw=780, maxh=900, tilt=-2, tr="pushleft"),
    dict(t=196.72, img="akif", zoom=(1.0, 1.15), focus=(0.5, 0.33), tr="pushup"),
    dict(t=202.52, mode="split", tr="bars", imgs=[dict(img="atif_dark", focus=(0.5, 0.4)), dict(img="borekci", focus=(0.5, 0.35))]),
    dict(t=209.30, mode="plate", bg="at_dark", tr="dip"),
    dict(t=210.50, img="at_dark", zoom=(1.0, 1.12), focus=(0.5, 0.35), tr="zoomblur"),
]
for _i, _s in enumerate(SCENES):
    _s["_end"] = SCENES[_i + 1]["t"] if _i + 1 < len(SCENES) else DURATION

RED = (255, 45, 45)
YEL = (255, 214, 10)
GREEN = (40, 200, 90)

OVERLAYS = [
    # hook
    dict(type="title", t0=0.0, t1=2.4, lines=["ATATÜRK", "HOCALARI ASTI MI?"], y=330, size=110),
    dict(type="finger", t0=2.44, t1=4.6, y=880, size=640, taps=[3.46]),
    dict(type="kinetic", t0=2.44, t1=4.6, text="SEN DE DUYDUN", y=330, size=120),
    dict(type="kinetic", t0=5.38, t1=7.2, text="GERÇEKTE NE OLDU?", y=520, size=110, style="black"),
    dict(type="handwrite", t0=8.22, t1=9.75, text="sadece belgeler", y=560, size=120, dur=0.6),
    dict(type="penline", t0=8.8, t1=9.75, x0=250, x1=780, y=640, color=YEL),
    dict(type="stamp", t0=13.54, t1=14.75, text="İDAM", y=700, size=170),
    dict(type="roster", t0=14.8, t1=17.3, size=230, items=[
        ("said", "ŞEYH SAİD", 15.2, (230, 720)), ("atif_dark", "ÂTIF HOCA", 15.6, (540, 720)),
        ("kubilay", "MENEMEN", 16.0, (850, 720))]),
    dict(type="kinetic", t0=16.2, t1=17.3, text="3 OLAY", y=1020, size=120),
    # 1 Şeyh Said
    dict(type="item", n=1, title="ŞEYH SAİD · 1925", t0=17.4, t1=50.0),
    dict(type="label", t0=22.2, t1=24.05, title="Şeyh Said", sub="Nakşibendi şeyhi", y=420),
    dict(type="kinetic", t0=25.22, t1=27.2, text="SİLAHLI İSYAN", y=700, size=120, style="red"),
    dict(type="handwrite", t0=28.04, t1=33.4, text="Genç", y=520, size=110, dur=0.4),
    dict(type="handwrite", t0=29.22, t1=33.4, text="Palu", y=650, size=110, dur=0.4),
    dict(type="handwrite", t0=30.12, t1=33.4, text="Elazığ", y=780, size=110, dur=0.4),
    dict(type="penarrow", t0=31.2, t1=33.4, src=(760, 780), dst=(620, 1010), bend=-0.3, dur=0.35),
    dict(type="kinetic", t0=31.76, t1=33.4, text="DİYARBAKIR KUŞATILDI", y=1060, size=86, style="red"),
    dict(type="kinetic", t0=33.72, t1=35.15, text="İSYAN BASTIRILDI", y=640, size=110, style="black"),
    dict(type="label", t0=35.3, t1=36.7, title="Şeyh Said yakalandı", sub="1925", y=420),
    dict(type="label", t0=36.9, t1=40.1, title="Şark İstiklal Mahkemesi", sub="Diyarbakır", y=420),
    dict(type="kinetic", t0=40.18, t1=42.4, text="29 HAZİRAN 1925", y=640, size=110),
    dict(type="stamp", t0=42.5, t1=43.8, text="İDAM", y=800, size=170),
    dict(type="handwrite", t0=44.7, t1=50.0, text="hoca olduğu için", y=560, size=110, dur=0.6, color=(255, 255, 255)),
    dict(type="pencross", t0=45.84, t1=50.0, cx=CX, cy=560, r=150),
    dict(type="handwrite", t0=46.56, t1=50.0, text="isyan lideri olduğu için", y=820, size=100, dur=0.8),
    dict(type="pencircle", t0=48.1, t1=50.0, cx=CX, cy=820, rx=430, ry=95, seed=3, color=YEL),
    dict(type="source", text="Şark İstiklal Mahkemesi kararları, 1925", t0=37.2, t1=50.0),
    # 2 Âtıf Hoca
    dict(type="item", n=2, title="İSKİLİPLİ ÂTIF HOCA", t0=50.2, t1=117.6),
    dict(type="label", t0=50.4, t1=52.6, title="İskilipli Âtıf Hoca", sub="1876 – 1926", y=420),
    dict(type="quote", t0=54.4, t1=57.7, y=760, by="Yaygın anlatı",
         words=[("Şapkaya", 54.56), ("karşı", 55.06), ("kitap", 55.36), ("yazdı,", 55.78), ("bu", 56.26), ("yüzden", 56.54), ("asıldı.", 56.82)]),
    dict(type="handwrite", t0=57.74, t1=60.1, text="?", y=760, size=360, dur=0.35, color=RED),
    dict(type="kinetic", t0=58.42, t1=60.1, text="BELGELER DAHA FAZLASINI SÖYLÜYOR", y=1060, size=66, style="black"),
    dict(type="label", t0=60.3, t1=65.9, title="Frenk Mukallitliği ve Şapka", sub="1924 · Maarif Vekâleti izniyle", y=420),
    dict(type="pencircle", t0=62.36, t1=65.9, cx=CX, cy=830, rx=380, ry=480, seed=5, a0=-110),
    dict(type="kinetic", t0=65.96, t1=67.6, text="ŞAPKA KANUNU · 1925", y=640, size=100, style="black"),
    dict(type="stamp", t0=67.68, t1=68.75, text="TUTUKLANDI", y=860, size=120),
    dict(type="label", t0=68.9, t1=74.6, title="Giresun İstiklal Mahkemesi", sub="Aralık 1925", y=420),
    dict(type="handwrite", t0=70.88, t1=74.6, text="kitap: 1924", y=700, size=110, dur=0.5),
    dict(type="handwrite", t0=71.74, t1=74.6, text="kanun: 1925", y=840, size=110, dur=0.5, color=(255, 255, 255)),
    dict(type="stamp", t0=73.56, t1=74.65, text="BERAAT", y=1030, size=150, color=GREEN, rot=-6),
    dict(type="kinetic", t0=75.34, t1=76.25, text="SERBEST BIRAKILMADI", y=640, size=96, style="red"),
    dict(type="label", t0=76.5, t1=78.6, title="Ankara İstiklal Mahkemesi", sub="Ocak 1926", y=420),
    dict(type="label", t0=78.8, t1=82.1, title="Mahkeme kararı", sub="3 Şubat 1926", y=420),
    dict(type="penline", t0=80.44, t1=82.1, x0=230, x1=790, y=1080, wavy=True),
    dict(type="kinetic", t0=80.44, t1=82.1, text="BAŞKA BİR SUÇLAMA", y=1080, size=90, style="red"),
    dict(type="label", t0=84.5, t1=87.3, title="Teali-i İslam Cemiyeti", sub="Başkan · Kurtuluş Savaşı yılları", y=420),
    dict(type="label", t0=87.6, t1=92.4, title="Beyanname", sub="Temsilî belge görseli", y=420),
    dict(type="kinetic", t0=89.72, t1=92.4, text="MİLLİ MÜCADELE'YE\nKARŞI", y=1020, size=96, style="red"),
    dict(type="pencircle", t0=91.08, t1=92.4, cx=CX, cy=760, rx=330, ry=470, seed=7),
    dict(type="kinetic", t0=94.12, t1=96.5, text="YUNAN UÇAKLARIYLA", y=330, size=110, style="red"),
    dict(type="papers", t0=94.5, t1=99.3, x0=250, x1=820, y0=560, spread=3.0, n=28),
    dict(type="penarrow", t0=97.06, t1=99.3, src=(760, 620), dst=(560, 1020), bend=0.25, dur=0.4),
    dict(type="handwrite", t0=97.5, t1=99.3, text="Anadolu köylerine!", y=1080, size=96, dur=0.6),
    dict(type="tagpair", t0=99.5, t1=105.5, tags=[("KİTAP", 430, 99.94), ("BEYANNAMELER", 1060, 102.64)]),
    dict(type="stamp", t0=103.92, t1=105.5, text="İDAM KARARI", y=960, size=120),
    dict(type="source", text="Ankara İstiklal Mahkemesi kararı, 3 Şubat 1926 · TBMM İstiklal Mahkemesi Zabıtları", t0=79.2, t1=105.5),
    dict(type="kinetic", t0=106.22, t1=110.3, text="4 ŞUBAT 1926", y=640, size=130, style="red"),
    dict(type="handwrite", t0=112.98, t1=117.6, text="şapka kitabı", y=560, size=110, dur=0.5, color=(255, 255, 255)),
    dict(type="handwrite", t0=114.36, t1=117.6, text="+ Yunan uçağından beyanname", y=740, size=86, dur=1.0),
    dict(type="pencircle", t0=116.3, t1=117.6, cx=CX, cy=740, rx=470, ry=95, seed=8),
    # 3 Menemen
    dict(type="item", n=3, title="MENEMEN · 1930", t0=118.0, t1=142.4),
    dict(type="label", t0=119.0, t1=122.0, title="Menemen", sub="23 Aralık 1930", y=420),
    dict(type="kinetic", t0=122.06, t1=124.1, text="DERVİŞ MEHMED", y=560, size=120),
    dict(type="handwrite", t0=124.2, t1=126.9, text="\"Ben mehdiyim\"", y=740, size=110, dur=0.6, color=(255, 255, 255)),
    dict(type="kinetic", t0=127.02, t1=129.2, text="\"ŞERİAT İSTERİZ\"", y=960, size=110, style="red"),
    dict(type="label", t0=129.4, t1=133.2, title="Mustafa Fehmi Kubilay", sub="Yedek subay · 1906 – 1930", y=420),
    dict(type="kinetic", t0=133.28, t1=134.45, text="ŞEHİT EDİLDİ", y=700, size=130, style="red"),
    dict(type="kinetic", t0=135.38, t1=137.0, text="DERVİŞ MEHMED\nÖLDÜRÜLDÜ", y=600, size=100, style="black"),
    dict(type="label", t0=137.3, t1=142.4, title="Divan-ı Harp", sub="Menemen, 1931", y=420),
    dict(type="stamp", t0=141.0, t1=142.4, text="İDAM", y=1000, size=150),
    # Sonuç
    dict(type="kinetic", t0=142.6, t1=145.1, text="HOCALAR İDAM\nEDİLDİ Mİ?", y=520, size=110, style="black"),
    dict(type="handwrite", t0=145.24, t1=146.3, text="Evet.", y=760, size=200, dur=0.4, color=RED),
    dict(type="handwrite", t0=148.06, t1=149.7, text="hoca olmak", y=560, size=130, dur=0.4, color=(255, 255, 255)),
    dict(type="pencross", t0=148.76, t1=149.7, cx=CX, cy=560, r=170),
    dict(type="kinetic", t0=149.74, t1=154.6, text="SİLAHLI İSYAN", y=480, size=100, style="red"),
    dict(type="kinetic", t0=151.26, t1=154.6, text="KIŞKIRTMA", y=650, size=100, style="red"),
    dict(type="kinetic", t0=152.34, t1=154.6, text="MİLLİ MÜCADELE'YE KARŞI", y=820, size=80, style="red"),
    # Diğer hocalar
    dict(type="kinetic", t0=156.16, t1=158.0, text="DİĞER HOCALAR?", y=330, size=110),
    dict(type="label", t0=158.3, t1=166.1, title="İstanbul Şeyhülislam fetvası", sub="Takvim-i Vekâyi · Nisan 1920", y=420),
    dict(type="handwrite", t0=162.4, t1=166.1, text="öldürülmesi caiz!", y=1080, size=100, dur=0.6, color=RED),
    dict(type="pencircle", t0=163.4, t1=166.1, cx=CX, cy=1080, rx=380, ry=90, seed=9),
    dict(type="label", t0=166.4, t1=170.6, title="Rifat Börekçi", sub="Ankara Müftüsü", y=420),
    dict(type="tagpair", t0=170.8, t1=175.6, tags=[("İSTANBUL FETVASI", 300, 170.8), ("ANKARA'NIN KARŞI FETVASI", 1060, 171.76)]),
    dict(type="vs", t0=171.0, t1=175.6),
    dict(type="label", t0=175.9, t1=180.8, title="Diyanet İşleri Reisliği", sub="Rifat Börekçi imzalı belge", y=420),
    dict(type="counter", t0=180.88, t1=183.4, **{"from": 0, "to": 17}, fmt="{} YIL", dur=0.6, y=1050, size=180),
    dict(type="label", t0=183.7, t1=190.5, title="Elmalılı Hamdi Yazır", sub="1878 – 1942", y=420),
    dict(type="stamp", t0=186.44, t1=190.5, text="MECLİS KARARI", y=960, size=110, color=YEL, rot=-6),
    dict(type="label", t0=190.8, t1=196.6, title="Hak Dini Kur'an Dili", sub="9 cilt · 1935 – 1938", y=420),
    dict(type="label", t0=196.9, t1=202.4, title="Mehmet Akif Ersoy", sub="İstiklal Marşı'nın şairi", y=420),
    dict(type="kinetic", t0=200.64, t1=202.4, text="KUR'AN MEALİ", y=1000, size=110),
    dict(type="tagpair", t0=202.6, t1=209.2, tags=[("İDAM EDİLENLER", 300, 203.58), ("GÖREV ALANLAR", 1060, 207.62)]),
    dict(type="vs", t0=203.0, t1=209.2),
    # Final
    dict(type="finger", t0=209.30, t1=210.45, y=880, size=640, taps=[209.86]),
    dict(type="kinetic", t0=209.30, t1=210.45, text="SANA SORUYORUM", y=330, size=110),
    dict(type="kinetic", t0=212.16, t1=DURATION + 1, text="DİNE Mİ?", y=480, size=130, style="black"),
    dict(type="kinetic", t0=214.22, t1=DURATION + 1, text="İSYANA MI?", y=660, size=130, style="red"),
    dict(type="cta", t0=215.38, t1=DURATION + 1, y=1000),
]

NO_CAPTIONS = [(0.0, 2.4), (54.4, 57.7), (215.3, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return CAP_Y


PUNCH = [1.10, 3.46, 13.54, 25.98, 42.50, 57.74, 73.56, 81.00, 94.52, 103.92, 127.02, 145.24, 186.44]
SHAKE = [0.0, 42.50, 103.92]
FLASH = [(0.0, 0.25)]

MUSIC = [(0, 9.8, 2), (9.8, 17.36, 1), (17.36, 50.12, 2), (50.12, 82.22, 2), (82.22, 110.38, 3), (110.38, 117.68, 1),
         (117.68, 142.54, 2), (142.54, 154.68, 0), (154.68, 202.52, 2), (202.52, 209.3, 3), (209.3, DURATION, 1)]

_PEN = [o["t0"] for o in OVERLAYS if o["type"] in ("pencircle", "penarrow", "penline", "pencross", "handwrite")]
SFX = [dict(name="impact", t=0.0, gain=0.9), dict(name="pop", t=3.46, gain=0.3), dict(name="hit", t=13.54, gain=0.5),
       dict(name="pop", t=15.2, gain=0.3), dict(name="pop", t=15.6, gain=0.3), dict(name="pop", t=16.0, gain=0.3),
       dict(name="hit", t=42.5, gain=0.5), dict(name="hit", t=67.68, gain=0.4), dict(name="hit", t=73.56, gain=0.45),
       dict(name="riser", t=80.44, gain=0.3, pre=True), dict(name="impact", t=80.44, gain=0.45),
       dict(name="paper", t=94.6, gain=0.35), dict(name="paper", t=95.8, gain=0.3), dict(name="paper", t=97.0, gain=0.3),
       dict(name="impact", t=103.92, gain=0.5), dict(name="hit", t=127.02, gain=0.4), dict(name="heartbeat", t=133.3, gain=0.45),
       dict(name="hit", t=141.0, gain=0.4), dict(name="hit", t=145.24, gain=0.45), dict(name="hit", t=171.0, gain=0.4),
       dict(name="hit", t=186.44, gain=0.4), dict(name="hit", t=203.0, gain=0.4), dict(name="pop", t=209.86, gain=0.3),
       dict(name="hit", t=212.16, gain=0.4), dict(name="hit", t=214.22, gain=0.45), dict(name="pop", t=215.4, gain=0.4)]
SFX += [dict(name="pen", t=p, gain=0.28) for p in _PEN]


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


if __name__ == "__main__":
    import json, sys
    json.dump(spec(), open(sys.argv[1], "w"))
