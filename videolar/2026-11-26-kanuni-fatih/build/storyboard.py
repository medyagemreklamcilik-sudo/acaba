# Kanuni mi, Fatih mi? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Fatih mi, Kanuni mi? En büyük padişah. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1450, 1570], 20, 1453
# ---- KANCA ----
SC('board', 'Fatih mi daha', [
    P('fatih', 'Fatih mi daha', 'FATİH SULTAN MEHMED', w=1000, crop=[.12, .12, .88, .62], shift=-1.2),
    TI('Fatih mi daha', 'FATİH Mİ,\nKANUNİ Mİ?', 160, x=0, j=1, shift=-1.2, font='cond'),
    P('kanuni', 'Öbürü Viyana’nın', 'KANUNİ SULTAN SÜLEYMAN', w=760, crop=[.1, .05, .9, .6]),
    TH('fatih', 'kanuni'),
], lead=.0, year=1453)
SC('dark', 'Osmanlı’nın en büyük', [
    TI('en büyük padişahı', 'EN BÜYÜK PADİŞAH?', 120),
    TI('padişahı hangisi?', 'HANGİSİ?', 170, color='#f0754e', font='cond'),
], boom=True)
# ---- FATİH ----
SC('board', 'Önce Fatih.', [
    P('fatih_gul', 'Önce Fatih.', 'FATİH', w=760),
    CT('Yirmi bir yaşındaydı', 0, 21, 'v => Math.round(v) + " YAŞINDA"', 170, dur=.8, sub='1453'),
    P('gemiler', 'Gemileri karadan', 'GEMİLER KARADAN', w=900),
    TH('fatih_gul', 'gemiler'),
], year=1453.3)
SC('board', 've 1453’te bin yıllık', [
    P('fetih', 'bin yıllık Bizans’ı', 'İSTANBUL’UN FETHİ · 1453', w=960),
    BD('bin yıllık Bizans’ı', 'BİN YILLIK BİZANS BİTTİ', red=True, size=58),
], year=1453.4, boom=True)
SC('dark', 'Bir çağı kapatıp', [
    TI('Bir çağı kapatıp', 'BİR ÇAĞ KAPANDI', 130),
    ST('bir beylik değil', 'BEYLİK', 'bir beylik değil', 150),
    TI('bir imparatorluktu', 'İMPARATORLUK', 150, color='#f0754e', font='cond'),
])
# ---- KANUNİ ----
SC('board', 'Kanuni ise yirmi altı', [
    P('kanuni2', 'Kanuni ise', 'KANUNİ', w=760, crop=[.1, .05, .9, .7]),
    CT('tam 46 yıl', 0, 46, 'v => Math.round(v) + " YIL"', 200, dur=1.0, sub='EN UZUN SALTANAT'),
], year=1520.8)
SC('board', 'Belgrad, Rodos, Mohaç, Bağdat.', [
    P('mohac', 'Belgrad, Rodos, Mohaç', 'MOHAÇ · 1526', w=820),
    P('harita', 'Sınırlar', 'OSMANLI SINIRLARI', w=900),
    TG('Viyana’dan Basra’ya', 'SINIRLAR', '', 'VİYANA → BASRA'),
], year=1530)
SC('board', 'Ama Kanuni Viyana’yı', [
    P('viyana', 'Ama Kanuni', 'VİYANA · 1529', w=880),
    ST('Viyana’yı alamadı', 'VİYANA', 'alamadı', 140),
    P('rodos', 'Fatih de Belgrad’ı', 'RODOS', w=760),
    BD('İkisinin de yenilgileri', 'İKİSİNİN DE YENİLGİSİ VAR', red=True, size=56),
], year=1529.8)
SC('dark', 'Sen olsan hangisi', [
    TI('Sen olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('Bin yıllık bir şehri', 'ŞEHRİ ALAN GENÇ Mİ,\nDÜNYAYI YÖNETEN Mİ?', 100),
], boom=True)
# ---- GÖLGELER ----
SC('board', 'Fatih’in gölgesinde', [
    DC('kardeş katline', ['KANUNNÂME', 'FATİH SULTAN MEHMED', '15. YÜZYIL'], 'KARDEŞ KATLİ', keyAt='kardeş katline'),
    P('kanunname', 'onun kanunnamesiyle', 'KANUNNÂME', w=700),
], year=1477)
SC('board', 'Kanuni’nin gölgesi ise', [
    P('mustafa', 'Şehzade Mustafa’yı', 'ŞEHZADE MUSTAFA', w=760),
    BD('çadırında boğdurdu', 'ÇADIRINDA BOĞDURULDU · 1553', red=True, size=54),
    TG('Pargalı İbrahim’i', 'DOSTU DA', '1536', 'PARGALI İBRAHİM'),
], year=1553.8, boom=True)
SC('dark', 'Büyüklük bazen', [
    TI('en sevdiğini kaybetmenin', 'EN SEVDİĞİNİ\nKAYBETMEK', 140, color='#f0754e', font='cond'),
])
SC('board', 'Fatih 49 yaşında', [
    P('turbe', 'Fatih 49 yaşında', 'FATİH TÜRBESİ · 1481', w=760),
    P('zigetvar', 'Kanuni 72 yaşında', 'ZİGETVAR · 1566', w=760),
    TH('turbe', 'zigetvar'),
], year=1566.7)
SC('dark', 'Fatih bir dünyayı', [
    TI('Fatih bir dünyayı', 'FATİH\nBİR DÜNYAYI BİTİRDİ', 120),
    TI('Kanuni o dünyayı', 'KANUNİ\nONU YÖNETTİ', 140, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Sence en büyük', [
    TI('Sence en büyük', 'EN BÜYÜK PADİŞAH?', 110),
    TI('Fatih mi, Kanuni mi?', 'FATİH Mİ, KANUNİ Mİ?', 110, color='#f0754e', font='cond'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
