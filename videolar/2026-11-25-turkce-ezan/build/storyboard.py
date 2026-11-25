# Atatürk ezanı neden Türkçeleştirdi? (belgelerle; sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Türkçe ezan 1932-1950: belgeler. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1930, 1950], 5, 1932
# ---- KANCA ----
SC('board', 'Atatürk ezanı yasakladı mı?', [
    P('ataturk', 'Atatürk ezanı', 'MUSTAFA KEMAL ATATÜRK', w=1000, crop=[.05, .02, .95, .6], shift=-1.2),
    TI('Atatürk ezanı', 'EZANI\nYASAKLADI MI?', 165, x=0, j=1, shift=-1.2, font='cond'),
    BD('18 yıl boyunca', '18 YIL TÜRKÇE EZAN', red=True, size=62),
], lead=.0, year=1932)
SC('board', 'minarelerden', [
    P('fatih', 'minarelerden', 'FATİH CAMİİ', w=880),
    TI('Tanrı uludur', '“TANRI\nULUDUR”', 150, x=0, font='cond'),
], year=1932)
SC('dark', 'Ama belgeler', [
    TI('Ama belgeler', 'BELGELER', 170),
    TI('farklı bir şey', 'BAŞKA BİR ŞEY\nSÖYLÜYOR', 120, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Arapça ezan okuyana', [
    DC('hapis cezası', ['KANUN NO. 4055', 'TCK MADDE 526', '1941'], 'HAPİS CEZASI', keyAt='hapis cezası'),
    BD('Atatürk öldükten', 'ATATÜRK ÖLDÜKTEN 3 YIL SONRA', red=True, size=54),
    TG('1941’de çıktı', 'KANUN', '1941', 'İNÖNÜ DÖNEMİ'),
], year=1941, boom=True)
SC('board', 'Atatürk döneminde böyle', [
    P('ataturk_k', 'Atatürk döneminde', 'ATATÜRK DÖNEMİ', w=700, crop=[0, 0, 1, .7]),
    ST('böyle bir kanun', 'KANUN', 'kanun yoktu', 130),
    DC('Diyanet bir genelge', ['GENELGE', 'DİYANET İŞLERİ', '18 TEMMUZ 1932'], 'TÜRKÇE OKUNACAK', keyAt='Türkçe okunacak'),
], year=1932.5)
SC('board', 'İlk Türkçe ezan', [
    P('gazete_ilk', 'İlk Türkçe ezan', '“İLK TÜRKÇE EZAN”', w=900, crop=[0, 0, 1, .55]),
    TG('Fatih Camii’nde', 'FATİH CAMİİ', '1932', 'OCAK'),
], year=1932.1)
SC('dark', 'Sen olsan, ömür boyu', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('sevinir miydin', 'SEVİNİR MİYDİN,\nKIZAR MIYDIN?', 115),
], boom=True)
# ---- BURSA ----
SC('board', '1933’te Bursa Ulu', [
    P('bursa_ulu', 'Bursa Ulu Cami’de', 'BURSA ULU CAMİİ', w=820),
    BD('Arapça ezan okudu', 'ARAPÇA EZAN OKUNDU', red=True, size=60),
    P('gazete_bursa', 'Gözaltılar başlayınca', '“BURSA’DA 24 MAZNUN”', w=860, crop=[0, 0, 1, .6]),
    TH('bursa_ulu', 'gazete_bursa'),
], year=1933.1)
SC('board', 'Atatürk hemen Bursa’ya', [
    P('ataturk_b', 'Atatürk hemen', 'ATATÜRK, BURSA 1933', w=900, crop=[.05, .02, .95, .6]),
    DC('Gazetelere aktarılan', ['DEMEÇ', 'BURSA', 'ŞUBAT 1933'], 'DİL MESELESİ', keyAt='dil meselesidir'),
    TI('Mesele din değil', 'DİN DEĞİL,\nDİL MESELESİ', 120, x=0, font='cond'),
], year=1933.1)
SC('board', 'Ona göre halk', [
    TI('ne söylediğini anlamalıydı', 'ANLAYARAK\nİBADET', 140, x=0, font='cond'),
    P('cemaat', 'Karşı çıkanlara göre', 'KARŞI ÇIKANLAR', w=760),
    BD('dine müdahaleydi', '“DİNE MÜDAHALE”', red=True, size=64),
], year=1933.5)
SC('dark', 'Sen de hiç anlamını', [
    TI('anlamını bilmeden', 'ANLAMINI\nBİLMEDEN?', 150, color='#f0754e', font='cond'),
])
SC('board', '1950’de Meclis cezayı', [
    P('menderes', '1950’de Meclis', 'ADNAN MENDERES', w=700, crop=[0, 0, 1, .65]),
    P('gazete_1950', 'cezayı kaldırdı', '“ARAPÇA SERBEST”', w=900, crop=[0, 0, 1, .5]),
    P('gazete_dun', 'Ertesi gün', '“DÜN ARABCA OKUNDU”', w=760, crop=[0, 0, 1, .7]),
    TH('gazete_1950', 'gazete_dun'),
], year=1950)
SC('dark', 'Atatürk ezanı yasaklamadı', [
    HT('ataturk', 'Atatürk ezanı yasaklamadı', crop=[.1, .02, .9, .5], w=1000),
    ST('yasaklamadı', 'YASAKLADI', 'yasaklamadı', 160),
    TI('Türkçeleştirdi', 'TÜRKÇELEŞTİRDİ', 120, color='#f0754e', font='cond'),
    TI('Ceza ondan sonra', 'CEZA ONDAN\nSONRA GELDİ', 100),
], boom=True)
SC('dark', 'Sence hangisi önemliydi?', [
    TI('Sence hangisi', 'HANGİSİ?', 160),
    TI('Dil mi, din mi?', 'DİL Mİ, DİN Mİ?', 120, color='#f0754e', font='cond'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
