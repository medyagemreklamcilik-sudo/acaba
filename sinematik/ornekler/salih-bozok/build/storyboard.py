# Salih Bozok storyboard: SC(mekân, başlangıç ifadesi, [nesneler]) sırayla, metindeki akışla.
# 'at' = nesnenin düştüğü kelime grubu (metinden birebir); sayı = önceki nesneden saniye sonra.
F = 'v => String(Math.round(v))'
# ---- KANCA ----
SC('dark', 'Bir paşa tabancasını', [
    HT('salih', 'Bir paşa', crop=[.08, .02, .84, .62], w=1150, shift=-1.3, rev=.7),
    TI('tetiği çekti', 'TETİĞİ ÇEKTİ', 190),
], glitch=[('tetiği çekti', .35, .8)], lead=.0, year=1938.86)
SC('dark', 'O sabah, 10 Kasım', [
    RG('O sabah', '10 KASIM 1938 · DOLMABAHÇE', 54, alpha=.6),
    P('ataturk', 'O sabah', 'ATATÜRK', w=900, crop=[0, 0, 1, .8], j=1, shift=.25, brackets=dict(t=7.2, r=[.25, .05, .5, .45])),
    CT('50 yıllık', 0, 50, 'v => Math.round(v) + " YIL"', 220, dur=1.1, sub='EN YAKIN ARKADAŞ', subSize=40),
], boom=True)
SC('board', 'Ama kurşun hedefini', [
    P('tabanca', 'Ama kurşun', crop=[0, .05, 1, .9]),
    BD('hedefini bulmadı', 'HEDEFİNİ BULMADI', red=True),
    P('salih', 'Salih Paşa', 'SALİH BOZOK', crop=[0, 0, 1, .92]),
    TH('tabanca', 'salih'),
    TG('üç yıl daha', 'ATATÜRK’SÜZ', '3 YIL', 'DAHA'),
])
SC('dark', 'Peki bir insan', [
    TI('neden ölmek', 'NEDEN?', 260),
    TI('Selanik’e.', 'SELANİK', 200, color='#f0754e', j=0),
])
# ---- SELANİK ----
SC('map', 'Yıl 1881.', [
    GD('Selanik, Osmanlı’nın', 'selanik', 'SELANİK · 1881', square=True),
], cam=[(-.4, 'selanik', .1), ('Selanik, Osmanlı’nın', 'selanik', .2), ('en renkli', 'selanik', .45)], year=1881)
SC('board', 'Limanda buharlı', [
    P('selanik', 'Limanda buharlı', 'SELANİK LİMANI', w=900, crop=[0, .08, 1, .84]),
    BD('Türkçe,', 'TÜRKÇE', size=66), BD('Rumca,', 'RUMCA', size=66), BD('Ladino,', 'LADİNO', size=66), BD('Bulgarca,', 'BULGARCA', size=66), BD('Arnavutça', 'ARNAVUTÇA', size=66),
], year=1881)
SC('board', 'Bu şehirde, aynı yıl', [
    TG('aynı mahallede', 'SELANİK', '1881', 'İKİ ÇOCUK'),
    P('mkgenc', 'Birinin adı Mustafa', 'MUSTAFA', crop=[0, 0, 1, .62]),
    P('salih', 'Ötekinin adı Salih', 'SALİH', crop=[0, 0, 1, .7]),
    TH('mkgenc', 'salih'),
    BD('uzaktan bir akrabalık', 'UZAKTAN AKRABA'),
    P('selanikev', 'aynı sokaklarda büyüyor', 'AYNI SOKAKLAR', w=860),
])
SC('board', 'Mahallede bir çocuk daha', [
    P('nuri', 'Nuri.', 'NURİ', crop=[0, 0, .52, .86]),
    BD('bir yaş küçük', 'BİR YAŞ KÜÇÜK'),
    TG('Bu üç çocuk,', 'DOSYA', '3', 'ÇOCUK'),
    TH('nuri', 'tag1'),
    BD('bir imparatorluğun yıkılışını', 'BİR İMPARATORLUK YIKILACAK', red=True),
    BD('bir cumhuriyetin doğuşunu', 'BİR CUMHURİYET DOĞACAK'),
])
SC('board', 'Mustafa’nın çocukluğu kolay', [
    BD('Babası Ali Rıza', 'ALİ RIZA EFENDİ †', size=86, x=0, y=0, j=0),
    P('zubeyde', 'Annesi Zübeyde Hanım', 'ZÜBEYDE HANIM', crop=[0, .04, 1, .8]),
    DC('askeri rüştiyenin', ['SINAV', 'SELANİK ASKERİ RÜŞTİYESİ'], 'KAZANDI.', keyAt='kazanıyor.'),
    TH('zubeyde', 'doc1'),
], year=1893)
SC('dark', 'Okulda bir matematik', [
    RG('Okulda bir matematik', 'MATEMATİK ÖĞRETMENİ', 52, alpha=.6),
    TI('ikinci bir isim', 'MUSTAFA', 150),
    TI('Kemal.', 'KEMAL', 300, color='#f0754e'),
    BD('Olgun, kusursuz', 'OLGUN · KUSURSUZ', size=70),
])
SC('board', 'Salih de aynı yolu', [
    TG('Selanik Askeri Rüştiyesi', 'ÖNCE', 'RÜŞTİYE', 'SELANİK'),
    P('manastir', 'Manastır Askeri İdadisi', 'MANASTIR ASKERİ İDADİSİ', w=900),
    TH('tag1', 'manastir'),
    BD('aynı yatakhanelerde', 'AYNI YATAKHANE'), BD('aynı sabah talimlerinde', 'AYNI TALİM'),
], year=1896)
SC('map', 'Manastır, sarp dağların', [
    RT('Manastır, sarp', ['selanik', 'manastir'], 1.4),
    GD('sarp dağların', 'manastir', 'MANASTIR', square=True),
], cam=[(-.4, 'selanik', .25, 0, 0), ('sarp dağların', 'manastir', .32), ('garnizon şehri', 'manastir', .4)])
SC('dark', 'Burada genç öğrenciler', [
    RG('Burada genç', 'MANASTIR · İDADİ', 52, alpha=.55),
    TI('şiir,', 'ŞİİR', 150, j=0), TI('tarih', 'TARİH', 150), TI('hürriyet fikirleriyle', 'HÜRRİYET', 200, color='#f0754e'),
    BD('Gece yatakhanede', 'GECE · FISILTIYLA', size=64),
])
# ---- İSTANBUL / HARBİYE ----
SC('map', 'Sonra İstanbul.', [
    RT('Sonra İstanbul.', ['manastir', 'selanik', 'istanbul'], 1.6),
    GD('Harbiye.', 'istanbul', 'İSTANBUL · HARBİYE', square=True),
], cam=[(-.4, 'manastir', .2), (.9, 'selanik', .14, 2500, 0), ('Harbiye.', 'istanbul', .3)], year=1899)
SC('board', 'Osmanlı’nın en iyi subaylarının', [
    P('harbiye', 'Osmanlı’nın en iyi', 'MEKTEB-İ HARBİYE', w=900),
    TG('1903’te teğmen', 'SALİH', '1903', 'TEĞMEN'),
    P('mkgenc2', 'Mustafa ise', 'MUSTAFA KEMAL', crop=[0, 0, 1, .7]),
    TG('1905’te kurmay', 'MUSTAFA', '1905', 'KURMAY YÜZBAŞI'),
    TH('tag2', 'mkgenc2'),
], year=1903)
SC('dark', 'Burada yollar ayrılabilirdi', [
    P('subaylar', 'Burada yollar', None, w=1200, j=0),
    ST('imparatorluğun iki ayrı', 'İKİ AYRI UÇ', 'Ama ayrılmıyor.', 120, j=1),
    TI('Ama ayrılmıyor.', 'AYRILMIYORLAR', 150, color='#f0754e'),
])
SC('board', 'Salih genç bir subay', [
    P('jandarma', 'jandarmaya veriliyor', 'JANDARMA', crop=[0, 0, 1, .85]),
    BD('Makedonya dağlarında', 'MAKEDONYA'), BD('eşkıya kovalıyor', 'EŞKIYA', red=True),
    P('jandarma2', 'Balkanlar o yıllarda', 'BALKANLAR', w=880),
    BD('Köyler basılıyor', 'KÖYLER BASILIYOR'), BD('yollar kesiliyor', 'YOLLAR KESİLİYOR'), BD('her gün bir çatışma', 'HER GÜN ÇATIŞMA', red=True),
], year=1904)
SC('board', 'Sonra Selanik’e dönüyor', [
    DC('Türk subay okulunda', ['TAYİN', 'SELANİK', 'SUBAY OKULU'], 'ÖĞRETMEN', keyAt='öğretmenlik', h=1050),
    P('salih', 'Artık genç subayları', 'SALİH BEY', crop=[0, 0, 1, .7]),
    TH('salih', 'doc1'),
])
SC('dark', 'Selanik bu sırada', [
    P('hurriyet', '1908’de Hürriyet', None, w=1000, crop=[0, .05, 1, .7]),
    TI('Hürriyet burada', 'HÜRRİYET · 1908', 140, color='#f0754e'),
    P('hurriyet2', 'Meydanlar dolup', 'SELANİK · 1908', w=1100, crop=[0, .2, 1, .8], j=0),
], year=1908)
SC('board', 'Bir yıl sonra İstanbul’da', [
    TG('bir isyan çıkıyor', 'İSTANBUL', '1909', 'İSYAN'),
    BD('Hareket Ordusu.', 'HAREKET ORDUSU', size=90, red=True),
    P('hareket', 'Hareket Ordusu.', None, w=900, crop=[.04, 0, .92, .9]),
    P('mkgenc', 'kurmay başkanlarından', 'KURMAY BAŞKANI: MUSTAFA KEMAL', crop=[0, 0, 1, .62]),
    TH('tag1', 'hareket'), TH('hareket', 'mkgenc'),
], year=1909, boom=True)
SC('dark', 'Ordu İstanbul’a giriyor', [
    P('abdulhamid', 'Ordu İstanbul’a', 'II. ABDÜLHAMİD', w=820, crop=[0, 0, 1, .85]),
    CT('otuz üç yıldır', 0, 33, 'v => Math.round(v) + " YIL"', 200, dur=1.0, sub='TAHTTA', subSize=40),
    ST('tahttan indiriliyor', 'TAHT', 'indiriliyor.', 150, j=1),
])
SC('map', 'Sonra eski padişah', [
    RT('bir trenle', ['istanbul', [27.5, 41.1], [25.5, 40.95], 'selanik'], 1.8, dash=True),
    GD('Alatini Köşkü’nde', 'selanik', 'ALATİNİ KÖŞKÜ', square=True),
], cam=[(-.4, 'istanbul', .2), ('bir trenle', 'istanbul', .16, -1600, 0), ('Alatini Köşkü’nde', 'selanik', .32)])
SC('board', 'Ve köşkün muhafızlığını', [
    P('alatini', 'Ve köşkün', 'ALATİNİ KÖŞKÜ', w=880),
    P('salih', 'genç Salih.', 'MUHAFIZ: SALİH', crop=[0, 0, 1, .7]),
    TH('salih', 'alatini'),
])
SC('dark', 'Düşünsene:', [
    TI('Düşünsene:', 'DÜŞÜNSENE', 120, color='#f0754e'),
    TI('Arkadaşının da içinde', 'ARKADAŞIN:\nTAHTI İNDİREN\nORDUDA', 130, lineAt=['Arkadaşının', 'bir padişahı', 'tahtından']),
    TI('Ve sen,', 'SEN:\nKAPISINDA\nNÖBETTE', 130, color='#f0754e', lineAt=['Ve sen,', 'padişahın kapısında', 'nöbet']),
])
# ---- 1912 ----
SC('board', 'Sonra 1912 geliyor', [
    TG('1912 geliyor', 'BALKAN SAVAŞI', '1912'),
    P('balkan', 'geri çekiliyor', 'GERİ ÇEKİLİŞ', w=900),
    DC('tek bir büyük savaş', ['TESLİM', 'SELANİK', 'KASIM 1912'], 'YUNAN ORDUSUNA', keyAt='Yunan ordusuna', stamp=dict(text='TESLİM', t='teslim ediliyor.', x=.1, y=.3, rot=-.12), h=1050),
    P('teslim', 'teslim ediliyor.', 'SELANİK · 1912', w=900),
], year=1912, boom=True)
SC('board', 'Mustafa’nın, Salih’in ve Nuri’nin', [
    P('selanikev', 'doğduğu şehir', 'SELANİK', w=860),
    BD('başka bir ülkenin', 'ARTIK BAŞKA BİR ÜLKE', red=True),
    P('balkan3', 'Aileler göç', 'GÖÇ YOLLARI', w=900),
    P('zubeyde', 'Zübeyde Hanım ve kızı', 'ZÜBEYDE HANIM', crop=[0, .04, 1, .8]),
    BD('İstanbul’a sığınıyor', 'İSTANBUL’A SIĞINDI'),
    TH('balkan3', 'zubeyde'),
])
SC('map', 'Üç arkadaşın çocukluğu', [
    GD('Üç arkadaşın', 'selanik', 'SELANİK', square=True, crossT_at='siliniyor.'),
], cam=[(-.4, 'selanik', .14), ('bir haritanın', 'selanik', .3), ('siliniyor.', 'selanik', .38)])
SC('dark', 'Mustafa Kemal o şehre', [
    TI('bir daha hiç', 'BİR DAHA\nHİÇ DÖNEMEDİ', 170, lineAt=['bir daha', 'dönemeyecek.']),
    TI('Sen doğduğun', 'SEN OLSAN?', 200, color='#f0754e', j=0),
    BD('ne hissederdin?', 'NE HİSSEDERDİN?', size=70),
])
# ---- BÜYÜK SAVAŞ ----
SC('board', '1914’te Birinci Dünya', [
    TG('1914’te Birinci', 'BİRİNCİ DÜNYA SAVAŞI', '1914'),
    P('canakkale', 'Çanakkale’de duyuluyor', 'ÇANAKKALE · 1915', w=900, crop=[0, 0, 1, .82]),
    BD('Anafartalar’da,', 'ANAFARTALAR'), BD('Conkbayırı’nda,', 'CONKBAYIRI'),
    BD('durdurulamaz denilen', 'DURDURULAMAZ DENİLEN ORDU DURDU', red=True, size=62),
], year=1915)
SC('map', 'Sonra Doğu’ya gidiyor', [
    RT('Sonra Doğu’ya', ['istanbul', 'ankara', 'sivas', 'diyarbakir', 'mus'], 2.0),
    GD('Muş’u', 'mus', 'MUŞ', square=True, dy=-45), GD('Bitlis’i', 'bitlis', 'BİTLİS', dy=55),
    RT('Suriye’de,', ['mus', 'diyarbakir', 'halep'], 1.4),
    GD('Yedinci Ordu’nun', 'halep', '7. ORDU', square=True),
], cam=[(-.4, 'istanbul', .14, 3000, 0), ('Muş’u', 'mus', .2, 2300, 0), ('İkinci Ordu’nun', 'mus', .16, -1000, 600), ('Yedinci Ordu’nun', 'halep', .2)], year=1916)
SC('dark', 'Ve yanına bir başyaver', [
    P('suriye', 'Ve yanına', 'MUSTAFA KEMAL PAŞA', w=880, crop=[0, 0, 1, .7]),
    BD('başyaver istiyor', 'BAŞYAVER ARANIYOR', size=70),
    HT('salih', 'Salih’i.', crop=[.08, .02, .84, .62], w=1100, j=0, shift=-.7, rev=.6),
    TI('Salih’i.', 'SALİH', 220, color='#f0754e'),
], year=1917, boom=True)
SC('board', 'Yaver ne demek?', [
    TI('Yaver ne demek?', 'YAVER\nNE DEMEK?', 150, x=0),
    BD('Komutanın gölgesi', 'KOMUTANIN GÖLGESİ', size=90, red=True),
    P('suriyeg', 'Gece yatana kadar', None, w=900),
    BD('Mektuplarını taşıyan', 'MEKTUP'), BD('kapısını bekleyen', 'KAPI'), BD('yorgunluğunu gören', 'YORGUNLUK'), BD('öfkesini dinleyen', 'ÖFKE'), BD('sırrını tutan', 'SIR', red=True),
])
SC('dark', 'Salih Bey bu gölge', [
    P('yuruyus', 'Salih Bey bu gölge', None, w=1000, crop=[0, 0, 1, .9]),
    TI('ömrünün sonuna', 'ÖMRÜNÜN\nSONUNA KADAR', 150, color='#f0754e', lineAt=['ömrünün', 'hiç bırakmıyor.']),
])
# ---- MİLLİ MÜCADELE ----
SC('board', '1918’de savaş kaybediliyor', [
    TG('1918’de savaş', 'YENİLGİ', '1918'),
    DC('Mondros imzalanıyor', ['MÜTAREKE', 'MONDROS', '30 EKİM 1918'], 'İMZALANDI.', keyAt='imzalanıyor.', h=1000),
    P('isgal', 'düşman donanması', 'İŞGAL ALTINDA İSTANBUL', w=900),
], year=1918)
SC('map', 'Mustafa Kemal Anadolu’ya', [
    RT('Samsun’dan', ['istanbul', [31, 41.9], 'samsun'], 1.0, dash=True), GD('Samsun’dan', 'samsun', 'SAMSUN', dy=-50),
    RT('Amasya’ya,', ['samsun', 'amasya'], .8), GD('Amasya’ya,', 'amasya', 'AMASYA', dy=50),
    RT('Erzurum’dan', ['amasya', 'erzurum'], .9), GD('Erzurum’dan', 'erzurum', 'ERZURUM'),
    RT('Sivas’a.', ['erzurum', 'sivas'], .8), GD('Sivas’a.', 'sivas', 'SİVAS', dy=60),
    RT('sonunda Ankara.', ['sivas', 'ankara'], 1.0), GD('sonunda Ankara.', 'ankara', 'ANKARA', square=True),
], cam=[(-.4, 'istanbul', .16, 2000, 0), ('Samsun’dan', 'samsun', .16, 0, 400), ('Erzurum’dan', 'erzurum', .14, -2000, 300), ('sonunda Ankara.', 'ankara', .22)], year=1919)
SC('board', '23 Nisan 1920’de', [
    P('ankara', '23 Nisan', '23 NİSAN 1920 · ANKARA', w=900),
    P('meclis', 'yeni bir meclis', 'BÜYÜK MİLLET MECLİSİ', w=860),
    TG('Meclis Başkanlığı', 'SALİH BEY', 'YAVER', 'MECLİS BAŞKANLIĞI'),
    TH('tag1', 'meclis'),
], year=1920.3)
SC('board', 'Ama sadece kapı', [
    P('yozgat', 'Yozgat’ta', 'YOZGAT', w=760),
    BD('Çapanoğlu isyanı', 'ÇAPANOĞLU İSYANI', red=True, size=84),
    BD('genç meclisi tehdit', 'MECLİSE TEHDİT'),
    P('salih', 'Salih Bey de var.', 'SALİH BEY', crop=[0, 0, 1, .7]),
    TH('salih', 'yozgat'),
], year=1920.5)
SC('board', 'Sonra Sakarya.', [
    P('sakarya', 'Sonra Sakarya.', 'SAKARYA · 1921', w=900, crop=[0, .1, 1, .8]),
    BD('Büyük Taarruz.', 'BÜYÜK TAARRUZ', red=True, size=84),
    P('izmir', 'Ordular İzmir’e', 'İZMİR · 1922', w=900),
    TG('1923’te Cumhuriyet', 'CUMHURİYET', '1923'),
    P('cumhuriyet', 'Cumhurbaşkanı oluyor', None, w=900),
    BD('Cumhurbaşkanlığı Yaveri.', 'CUMHURBAŞKANLIĞI YAVERİ: SALİH BEY', size=60),
], year=1921.6)
SC('board', 'Aynı yıl Yozgat’tan', [
    DC('Yozgat’tan milletvekili', ['MAZBATA', 'TBMM', 'YOZGAT MEBUSU'], 'SALİH BEY', keyAt='seçiliyor.', h=1000),
    BD('isyanın şehrinden', 'İSYANIN ŞEHRİNDEN'),
    BD('Bilecik’ten.', 'SONRA BİLECİK'),
    CT('On sekiz yıl', 0, 18, 'v => Math.round(v) + " YIL"', 230, dur=1.1, sub='MECLİSTE', subSize=40),
    P('isbank', 'İş Bankası’nın', 'TÜRKİYE İŞ BANKASI · KURUCU', w=880),
], year=1923.5)
SC('board', '1934’te Soyadı Kanunu', [
    TG('Soyadı Kanunu', 'SOYADI KANUNU', '1934'),
    BD('soyadı: Atatürk.', 'ATATÜRK', size=96),
    BD('aldığı soyadı ise', 'BOZOK', size=110, red=True),
    P('yozgat2', 'Yozgat’ın eski adı', 'BOZOK = YOZGAT', w=900),
], year=1934.5)
SC('board', 'Bu arada üç arkadaş', [
    P('salih', 'Bu arada üç', 'SALİH BOZOK', crop=[0, 0, 1, .7]),
    P('nuri', 'Nuri’nin kız kardeşi', 'NURİ', crop=[0, 0, .52, .86]),
    BD('Dürriye Hanım’la', 'KIZ KARDEŞİ DÜRRİYE İLE EVLENDİ', size=60),
    TH('salih', 'nuri'),
    BD('artık akraba', 'ARTIK AKRABA', red=True),
    BD('Conker’i alıyor', 'NURİ CONKER'),
])
SC('board', 'Çankaya’nın uzun akşamları', [
    P('cankaya', 'Çankaya’nın uzun', 'ÇANKAYA SOFRASI', w=950),
    P('sofra', 'eski Selanik günleri', 'K. ATATÜRK · 1935', w=920),
    P('dortlu', 'en zor gecelerinde', 'ÇANKAYA KÖŞKÜ', w=950),
    BD('hep aynı: Salih', 'HEP AYNI YÜZ: SALİH', red=True),
    TH('cankaya', 'dortlu'),
], year=1935)
SC('dark', 'Senin de böyle bir arkadaşın', [
    TI('Senin de böyle', 'SENİN DE\nBÖYLE BİR\nARKADAŞIN\nVAR MI?', 150, lineAt=['Senin de', 'böyle bir', 'arkadaşın', 'var mı?']),
    BD('hiç gitmemiş biri', 'HİÇ GİTMEMİŞ BİRİ', size=70, red=True),
])
# ---- SON YILLAR ----
SC('board', '1937’de ilk yara', [
    TG('ilk yara', 'İLK YARA', '1937'),
    P('nuri', 'Nuri Conker ölüyor', 'NURİ CONKER †', crop=[0, 0, .52, .86]),
    BD('üç çocuktan biri', 'ÜÇ ÇOCUKTAN BİRİ YOK', red=True),
    P('ikili', 'çocukluk arkadaşının ardından', None, w=950),
    BD('çok sarsılıyor', 'SARSILDI'),
], year=1937)
SC('board', 'Ve aynı yıllarda Atatürk’ün', [
    BD('alarm vermeye', 'ALARM', red=True, size=110, x=0, y=0, j=0),
    BD('Burnu kanıyor', 'BURUN KANAMASI', j=1), BD('vücudu kaşınıyor', 'KAŞINTI', j=1),
    DC('Paris’ten gelen', ['TEŞHİS', 'PROF. FIESSINGER', '1938'], 'KARACİĞER SİROZU', keyAt='karaciğer sirozu.', h=1000),
    BD('dinlenmeyi reddediyor', 'DİNLENMEYİ REDDETTİ'),
    TG('Aklında Hatay', 'AKLINDA', 'HATAY'),
], year=1938.3)
SC('board', 'Salih Bey ise yanından', [
    P('salih', 'Salih Bey ise', 'SALİH BEY', crop=[0, 0, 1, .7]),
    P('savarona', 'Savarona yatında', 'SAVARONA · YAZ 1938', w=950, crop=[0, .1, 1, .8]),
    P('dolma', 'Sonbahar Dolmabahçe’de', 'DOLMABAHÇE · SONBAHAR', w=950),
    TH('salih', 'savarona'), TH('savarona', 'dolma'),
    BD('her gün o kapının', 'HER GÜN O KAPIDA', red=True),
], year=1938.6)
SC('dark', 'Arkadaşının her gün biraz', [
    HT('ataturk', 'Arkadaşının her gün', crop=[.15, 0, .7, .55], w=1100),
    BD('Kilo verişini', 'KİLO', size=64, j=1), BD('sararan yüzünü', 'SARARAN YÜZ', size=64, j=1), BD('uzayan uykularını', 'UZAYAN UYKULAR', size=64, j=1),
    TI('fısıltıya dönüşünü', 'FISILTI', 170, color='#f0754e', j=1),
])
SC('dark', 'Sen elli yıllık arkadaşının', [
    TI('Sen elli yıllık', 'ELLİ YILLIK\nARKADAŞIN', 160, lineAt=['Sen elli', 'arkadaşının']),
    TI('ne yapardın?', 'SEN NE YAPARDIN?', 130, color='#f0754e'),
])
SC('board', 'Ekim ayında Atatürk', [
    DC('ilk kez komaya', ['SAĞLIK BÜLTENİ', 'EKİM 1938'], 'KOMA', keyAt='komaya giriyor.', h=950),
    BD('Herkes umutlanıyor', 'UMUT'),
    DC('Gazetelerde her gün', ['SAĞLIK BÜLTENİ', 'KASIM 1938'], 'YENİDEN KOMA', keyAt='yeniden komaya', h=950, stamp=dict(text='8 KASIM', t='8 Kasım', x=.12, y=.28, rot=-.1)),
    BD('Bu sefer uyanmıyor', 'BU SEFER UYANMADI', red=True),
], year=1938.8)
SC('dark', 'Dolmabahçe’nin koridorlarında', [
    P('oda', 'Dolmabahçe’nin koridorlarında', 'DOLMABAHÇE', w=1050),
    BD('Kimse konuşmuyor', 'SESSİZLİK', size=70),
    BD('Herkes saate bakıyor', 'SAAT', size=70, red=True),
])
SC('dark', '10 Kasım 1938. Sabah.', [
    RG('10 Kasım 1938.', '10 KASIM 1938 · SABAH', 54, alpha=.65, x=0, y=-300),
    CT('Saat dokuzu beş', 0, 1, 'v => "09:05"', 330, dur=.3, sub='', y=0),
    TI('kalbi duruyor.', 'KALBİ DURDU', 140, color='#f0754e'),
], year=1938.86, boom=True)
SC('dark', 'Salih Bey odaya giriyor', [
    HT('salih', 'Salih Bey odaya', crop=[.08, .02, .84, .62], w=1150),
    TI('son kez bakıyor', 'SON KEZ', 150, color='#f0754e'),
])
SC('dark', 'Sonra sessizce odadan', [
    TI('Sonra sessizce', 'KAPI', 200),
    P('tabanca', 'bir silah sesi', None, w=1000, crop=[0, .05, 1, .9], j=0),
], glitch=[('bir silah sesi', .45, 1.0)], boom=True)
SC('board', 'Salih Bey tabancasını kendi', [
    DC('Salih Bey tabancasını', ['VAKA', 'DOLMABAHÇE', '10 KASIM 1938'], 'GÖĞSÜNE ATEŞ ETTİ', keyAt='tetiği çekmiş.', h=1000),
    BD('Anlatılanlara göre', 'ANLATILANLARA GÖRE', size=64),
])
SC('dark', 'son sözü şuydu', [
    TI('son sözü', '“BAŞKOMUTAN\nYAVERSİZ\nGİDEMEZ!”', 150, lineAt=['Başkomutan', 'yaversiz', 'gidemez!']),
], boom=True)
SC('board', 'Onu yerde kanlar içinde', [
    P('salih', 'Onu yerde', 'SALİH BOZOK', crop=[0, 0, 1, .7]),
    TG('hastaneye kaldırıyorlar', 'ACİL', 'HASTANE'),
    BD('çok az bir farkla', 'KALBİ ÇOK AZ FARKLA ISKALADI', red=True, size=60),
])
SC('dark', 'Salih Bey yaşıyor.', [
    TI('Salih Bey yaşıyor.', 'YAŞIYOR', 220),
    TI('Ama artık bir yarası', 'AMA BİR YARASI VAR', 110, color='#f0754e'),
    BD('sadece göğsündeki değil', 'SADECE GÖĞSÜNDE DEĞİL', size=64),
])
SC('dark', 'Bazen insan, birini', [
    TI('Bazen insan,', 'BAZEN İNSAN,\nBİRİNİ KAYBEDİNCE\nKENDİNDEN DE\nBİR PARÇA\nKAYBEDER.', 120, lineAt=['Bazen insan,', 'birini kaybedince', 'kendinden de', 'bir parça', 'kaybeder.']),
])
# ---- CENAZE ----
SC('board', 'Atatürk’ün cenazesi', [
    P('cenaze', 'Atatürk’ün cenazesi', 'SON YOLCULUK', w=950),
    P('kapi', 'Bütün İstanbul', 'DOLMABAHÇE · KASIM 1938', w=950),
    BD('Trenle Ankara’ya', 'TRENLE ANKARA’YA'),
    P('cenaze2', 'Milyonlarca insan', 'MİLYONLAR', w=950),
    TH('cenaze', 'cenaze2'),
], year=1938.88)
SC('board', 'İyileşiyor ama eskisi', [
    P('salih', 'İyileşiyor ama', 'SALİH BOZOK', crop=[0, 0, 1, .7]),
    P('meclisic', 'meclise geliyor', 'MECLİS', w=950),
    BD('artık yok', 'O ADAM ARTIK YOK', red=True),
], year=1939)
SC('dark', 'Arkadaşının yokluğunda üç', [
    CT('üç yıl yaşıyor', 0, 3, 'v => Math.round(v) + " YIL"', 260, dur=.9, sub='ONSUZ', subSize=44),
    TI('en uzun üç', 'HAYATININ\nEN UZUN\nÜÇ YILI', 140, lineAt=['hayatının', 'en uzun', 'üç yılı.']),
])
SC('board', '25 Nisan 1941’de', [
    TG('25 Nisan', '25 NİSAN', '1941', 'SUADİYE'),
    BD('Altmış yaşında', '60 YAŞINDA'),
    DC('Vasiyeti çok açık', ['VASİYET', 'SALİH BOZOK'], 'CEBECİ ŞEHİTLİĞİ', keyAt='Cebeci Askeri', h=1000),
    P('cebeci', 'Nuri Conker’in yanına', 'NURİ CONKER’İN MEZARI', w=820, crop=[0, .1, 1, .62]),
    TH('doc1', 'cebeci'),
], year=1941.3)
SC('board', 'Selanik’in o mahallesinden', [
    BD('üç çocuktan ikisi', 'İKİSİ YAN YANA', x=0, y=0, size=90),
    P('cebeci2', 'yan yana yatıyor', 'CEBECİ · ANKARA', w=950),
    P('anitkabir', 'Anıtkabir’de', 'ANITKABİR', w=950),
    BD('şehre tepeden', 'ÜÇÜNCÜSÜ: ANITKABİR', red=True),
    TH('cebeci2', 'anitkabir'),
], year=1941.3)
SC('board', 'Yıllar sonra oğlu', [
    P('kitapA', 'oğlu Cemil Bozok', 'CEMİL S. BOZOK', w=700),
    BD('Hep Atatürk’ün Yanında', '“HEP ATATÜRK’ÜN YANINDA”', size=62),
    P('kitapB', 'Gazeteci Can Dündar', 'CAN DÜNDAR', w=700),
    P('veda', '2010’da beyaz', 'FİLM · 2010', w=720),
    BD('tek bir kelimeydi', 'VEDA', red=True, size=120),
    TH('kitapA', 'kitapB'), TH('kitapB', 'veda'),
])
# ---- KAPANIŞ ----
SC('dark', 'Tarih kitapları savaşları', [
    TI('Tarih kitapları', 'SAVAŞLAR\nANTLAŞMALAR\nDEVRİMLER', 120, lineAt=['savaşları,', 'antlaşmaları,', 'devrimleri']),
    TI('büyük adamların arkasında', 'VE ARKALARINDA\nADINI DUYMADIĞIMIZ\nİNSANLAR', 100, color='#f0754e', lineAt=['büyük adamların', 'adını pek', 'insanlar durur.'], j=0),
])
SC('dark', 'Salih Bozok bir ordu', [
    ST('bir ordu kurmadı', 'ORDU KURMADI', 'Bir devlet', 120),
    ST('Bir devlet kurmadı', 'DEVLET KURMADI', 'Ama kurulan', 120),
    HT('salih', 'Ama kurulan', crop=[.08, .02, .84, .62], w=1150, j=0),
    TI('elli yıl boyunca', '50 YIL · TEK BİR KİŞİ', 100, color='#f0754e'),
], boom=True)
SC('dark', 'Atatürk’ün en uzun yolculuğunda', [
    P('yuruyus', 'Atatürk’ün en uzun', None, w=1000, crop=[0, 0, 1, .9]),
    TI('yaversiz gitmesine', 'YAVERSİZ\nGİTMESİNE\nRAZI OLMADI', 140, color='#f0754e', lineAt=['yaversiz', 'gitmesine', 'razı olmadı.']),
])
SC('dark', 'Sence sadakat', [
    TI('Sence sadakat', 'SADAKAT', 220),
    TI('kendi hayatından', 'HAYATINDAN\nVAZGEÇMEK Mİ?', 120, lineAt=['kendi hayatından', 'vazgeçmek']),
    TI('Yoksa asıl sadakat', 'YAŞAMAYA\nDEVAM ETMEK Mİ?', 120, color='#f0754e', lineAt=['Yoksa asıl', 'yaşamaya devam']),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
