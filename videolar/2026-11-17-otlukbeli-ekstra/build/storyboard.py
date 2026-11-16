# Otlukbeli: Türk'ü Türk'e kırdıran savaş (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Fatih ve Uzun Hasan: Otlukbeli 1473. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1455, 1480], 5, 1473.6
# ---- KANCA ----
SC('board', 'Türk’ü Türk’e kırdıran', [
    P('fatih', 'Türk’ü Türk’e', 'FATİH SULTAN MEHMED', w=860, crop=[.1, .05, .8, .85], shift=-1.2),
    TI('Türk’ü Türk’e', 'TÜRK’Ü TÜRK’E\nKIRDIRAN SAVAŞ', 110, x=0, j=1, shift=-1.2),
    BD('Otlukbeli.', 'OTLUKBELİ · 1473', red=True, size=70),
], lead=.0, year=1473.6)
SC('dark', 'Bre kahbe oğlu', [
    TI('Bre kahbe oğlu', '“BRE KAHBE OĞLU,\nNE DERYADIR!”', 110, color='#f0754e', lineAt=[0, 'ne deryadır']),
    TI('Bu sözü bir Türk', 'BİR TÜRK HÜKÜMDARI', 100),
    TI('karşısındaki Türk ordusunu', 'TÜRK ORDUSUNA\nBAKARKEN', 120, color='#f0754e'),
], glitch=[('Bre kahbe', .3, .7)], boom=True)
# ---- İKİ HÜKÜMDAR ----
SC('board', 'Bir yanda Fatih', [
    P('fatihgul', 'Bir yanda Fatih', 'FATİH · OSMANLI', w=760, crop=[0, 0, 1, .7]),
    P('uzunhasan', 'öbür yanda Akkoyunlu', 'UZUN HASAN · AKKOYUNLU (TEMSİLİ)', w=760, crop=[0, 0, 1, .6]),
    TH('fatihgul', 'uzunhasan'),
    TG('İkisi de Oğuz’du', 'İKİSİ DE', 'OĞUZ', 'İKİSİ DE MÜSLÜMAN'),
], year=1460)
SC('dark', 'Anlatılanlara göre Uzun', [
    TI('Anlatılanlara göre', 'ANNESİ SARA HATUN', 100),
    TI('Fatih’e "oğul"', '“OĞUL”', 220, color='#f0754e'),
], year=1461)
# ---- TRABZON ----
SC('board', 'Ama Uzun Hasan, Trabzon’un', [
    P('trabzon', 'Trabzon’un vergisini', 'TRABZON', w=920),
    DC('Rivayete göre Fatih’in', ['ELÇİ MURAD BEY', 'İSTANBUL', '1459'], 'SENEYE BEN GETİRİRİM', keyAt='İstediklerini seneye', h=980),
    TI('İstediklerini seneye', '“İSTEDİKLERİNİ SENEYE\nBEN KENDİM GETİRİRİM.”', 76, x=0, j=1, lineAt=[0, 'ben kendim']),
    TH('trabzon', 'doc1'),
    BD('Ertesi yıl ordusuyla', 'TRABZON ALINDI · 1461', red=True, size=62),
], year=1461)
# ---- TOKAT, VENEDİK, MEKTUP ----
SC('board', 'Uzun Hasan Tokat’ı yaktı', [
    P('tokat', 'Uzun Hasan Tokat’ı', 'TOKAT YAKILDI · 1472', w=920),
    P('venedik', 'Venedik’ten top', 'VENEDİK’TEN TOP İSTEDİ', w=900),
    TH('tokat', 'venedik'),
    DC('Bir mektubunda da', ['UZUN HASAN’IN MEKTUBU', 'TDV İSLÂM ANS.', '“OTLUKBELİ SAVAŞI”'], 'TRABZON + KAPADOKYA = BARIŞ', keyAt='Kapadokya verilirse', h=980),
], year=1472.5)
SC('dark', 'Fatih’in cevabı', [
    P('mektup', 'Fatih’in cevabı', None, w=900, crop=[0, 0, 1, .6]),
    TI('Er isen meydana', '“ER İSEN\nMEYDANA GEL”', 140, color='#f0754e'),
    TI('delikten deliğe', '“DELİKTEN DELİĞE GİRME.”', 74),
], boom=True)
SC('dark', 'Sen Fatih olsan', [
    TI('Sen Fatih olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('barışır mıydın', 'BARIŞIR MIYDIN?', 120),
    TI('yoksa atını', 'ATINI MI\nEYERLERDİN?', 130, color='#f0754e'),
])
# ---- FIRAT ----
SC('board', '1473. İlk çarpışmada', [
    TG('1473.', '4 AĞUSTOS', '1473', 'FIRAT KIYISI'),
    P('okcu', 'sahte bir geri', 'SAHTE GERİ ÇEKİLME', w=820),
    TH('tag1', 'okcu'),
    P('firat', 'Peşlerine düşen', 'FIRAT', w=880),
    BD('Has Murad Paşa', 'BEYLERBEYİ HAS MURAD PAŞA', size=58),
    ST('Fırat’ta boğuldu.', 'HAS MURAD', 'boğuldu.', 120),
], year=1473.59)
# ---- OTLUKBELİ ----
SC('board', 'Bir hafta sonra Otlukbeli.', [
    TG('Bir hafta sonra', '11 AĞUSTOS', '1473', 'OTLUKBELİ · TERCAN'),
    P('uzunhasan2', 'Uzun Hasan tepeden', 'UZUN HASAN (TEMSİLİ)', w=820),
    TH('tag1', 'uzunhasan2'),
    TI('o sözü söyledi', '“NE DERYADIR!”', 130, x=0),
], year=1473.61)
SC('dark', 'Osmanlı topları ateşlendi.', [
    P('savas2', 'Osmanlı topları', None, w=900, crop=[0, 0, 1, .7]),
    TI('Akkoyunlu süvarisi barut', 'BARUT SESİ', 170, color='#f0754e'),
], glitch=[('Osmanlı topları', .2, .6)], boom=True)
SC('board', 'Uzun Hasan’ın oğlu Zeynel’i', [
    P('turkmen', 'Uzun Hasan’ın oğlu', 'ZEYNEL MİRZA (TEMSİLİ)', w=740, crop=[0, 0, 1, .6]),
    BD('sıradan bir azap', 'BİR AZAP ASKERİ: KILIÇÇI AHMED', red=True, size=50),
    TI('Uzun Hasan kaçtı.', 'UZUN HASAN\nKAÇTI', 130, x=0),
], year=1473.61)
SC('dark', 'Venedik’in topları mı?', [
    P('venedik', 'Venedik’in topları', None, w=1000),
    TI('Hiç yetişmedi.', 'HİÇ YETİŞMEDİ', 140, color='#f0754e'),
])
# ---- KAPANIŞ ----
SC('dark', 'Bazen en ağır savaş', [
    TI('Bazen en ağır', 'EN AĞIR SAVAŞ', 140),
    TI('en çok benzediğin', 'EN ÇOK BENZEDİĞİN\nİNSANLA YAPILIR', 100, color='#f0754e', lineAt=[0, 'insanla yapılır']),
])
SC('dark', 'Sence haklı olan', [
    TI('Sence haklı', 'HAKLI KİM?', 160),
    TI('Fatih mi', 'FATİH Mİ?', 130, color='#f0754e'),
    TI('Uzun Hasan mı', 'UZUN HASAN MI?', 120),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
