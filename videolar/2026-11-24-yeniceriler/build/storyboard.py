# Yeniçeriler: padişah indiren ordu (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Yeniçeri Ocağı: 1622-1826. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1600, 1830], 50, 1622.4
# ---- KANCA ----
SC('board', 'Osmanlı’da padişahı boğan', [
    P('yeniceri', 'Osmanlı’da padişahı', 'YENİÇERİ', w=1000, crop=[.26, .03, .48, .38], shift=-1.2),
    TI('Osmanlı’da padişahı', 'PADİŞAHI\nKENDİ ORDUSU\nBOĞDU', 150, x=0, j=1, shift=-1.2, font='cond'),
], lead=.0, year=1622.4)
SC('board', 'Yeniçeriler, devletin en korkulan', [
    P('yeniceri2', 'Yeniçeriler, devletin', 'YENİÇERİ OCAĞI', w=900),
    BD('en korkulan askerleriydi', 'EN KORKULAN ASKER', size=58),
    ST('kılıçlarını saraya', 'DÜŞMANA', 'saraya çevirdiler', 140),
], year=1600)
SC('board', 'İsyanın işareti basitti', [
    P('kazan', 'çorba kazanlarını', 'KAZAN TAŞIYAN YENİÇERİLER', w=920),
    TI('kazanlarını devirirlerdi', 'KAZAN\nKALDIRMA', 150, x=0, color='#f0754e', font='cond'),
    P('kazan2', 'Kazan devrildiyse', 'YENİÇERİ KAZANI', w=600),
    TH('kazan', 'kazan2'),
], year=1620, boom=True)
# ---- GENÇ OSMAN ----
SC('board', '1622’de genç padişah', [
    TG('1622’de', 'GENÇ OSMAN', '1622', '17 YAŞINDA'),
    P('osman', 'İkinci Osman', 'SULTAN II. OSMAN', w=860, crop=[.05, .02, .9, .65]),
    TH('tag1', 'osman'),
    P('yedikule', 'Yedikule’de boğdu', 'YEDİKULE', w=760),
], year=1622.4, boom=True)
SC('dark', 'Bir Osmanlı padişahını ilk kez', [
    HT('osman', 'Bir Osmanlı', crop=[.2, .1, .6, .45], w=1000),
    TI('ilk kez kendi askeri', 'İLK KEZ\nKENDİ ASKERİ', 140, color='#f0754e', font='cond'),
], year=1622.4)
SC('board', 'Sonra sıra diğerlerine', [
    P('ibrahim', 'Sultan İbrahim', 'SULTAN İBRAHİM · 1648', w=820, crop=[.05, .05, .9, .7]),
    BD('indirildi ve boğuldu', 'İNDİRİLDİ, BOĞULDU', red=True, size=60),
    TG('Dördüncü Mehmed', 'IV. MEHMED', '1687', 'İNDİRİLDİ'),
    TG('İkinci Mustafa', 'II. MUSTAFA', '1703', 'İNDİRİLDİ'),
    TG('Üçüncü Ahmed', 'III. AHMED', '1730', 'İNDİRİLDİ'),
    TI('Hepsi isyanlarla', 'HEPSİ\nTAHTI KAYBETTİ', 120, x=0, font='cond'),
], year=1700)
SC('dark', 'Sen padişah olsan', [
    TI('Sen padişah olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('korkar mıydın', 'KENDİ ASKERİNDEN\nKORKAR MIYDIN?', 110),
], boom=True)
SC('board', 'Islahat isteyen Üçüncü Selim', [
    P('selim3', 'Üçüncü Selim', 'SULTAN III. SELİM', w=860, crop=[.08, .05, .85, .6]),
    BD('ertesi yıl öldürüldü', '1808: ÖLDÜRÜLDÜ', red=True, size=62),
], year=1807.4)
# ---- MAHMUD ----
SC('board', 'Ve tahta İkinci Mahmud', [
    P('mahmud', 'İkinci Mahmud', 'SULTAN II. MAHMUD', w=820, crop=[.05, .02, .9, .5]),
    P('nizam', 'yeni bir ordu', 'YENİ ORDU', w=720),
    TH('mahmud', 'nizam'),
], year=1808.6)
SC('dark', '15 Haziran 1826.', [
    TI('15 Haziran 1826', '15 HAZİRAN 1826', 110),
    TI('yine kazanlarını', 'KAZANLAR DEVRİLDİ', 120, color='#f0754e', font='cond'),
    TI('karşılarında toplar', 'BU SEFER: TOP', 170, font='cond'),
], year=1826.45, boom=True, glitch=[('toplar vardı', .3, .8)])
SC('board', 'Et Meydanı’ndaki kışlalar', [
    P('meydan', 'Et Meydanı’ndaki', 'İSTANBUL, 1826', w=920),
    TI('Binlerce yeniçeri', 'BİNLERCE\nYENİÇERİ ÖLDÜ', 130, x=0, font='cond'),
    BD('bir günde tarihe', 'BİR GÜNDE BİTTİ', red=True, size=66),
], year=1826.45)
SC('board', 'Buna "Hayırlı Olay"', [
    DC('Hayırlı Olay', ['VAKA-İ HAYRİYE', 'HAYIRLI OLAY', '1826'], 'HAYIRLI OLAY', keyAt='Hayırlı Olay',
       stamp=dict(text='HAYIRLI?', t='dediler', x=.1, y=.3, rot=-.1)),
], year=1826.45)
# ---- KAPANIŞ ----
SC('dark', 'Bazen seni korusun', [
    TI('Bazen seni korusun', 'SENİ KORUYAN GÜÇ', 110),
    TI('sana emir vermeye', 'BİR GÜN\nEMİR VERİR', 130, color='#f0754e', font='cond'),
])
SC('dark', 'Padişahları deviren ordu', [
    HT('mahmud', 'Padişahları deviren', crop=[.15, .05, .7, .35], w=1000),
    TI('bir padişah tarafından', 'BİR PADİŞAH\nDEVİRDİ', 150, color='#f0754e', font='cond'),
])
SC('dark', 'Sence Mahmud haklı', [
    TI('Sence Mahmud', 'MAHMUD\nHAKLI MIYDI?', 120),
    TI('zalim mi', 'HAKLI MI, ZALİM Mİ?', 100, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
