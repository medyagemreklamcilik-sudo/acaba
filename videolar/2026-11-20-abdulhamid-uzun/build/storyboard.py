# II. Abdülhamid uzun video (yatay, sinematik dosya). Kaynaklar README'de.
BASLIK = 'II. Abdülhamid: Kızıl Sultan mı, Ulu Hakan mı? "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1840, 1920], 10, 1905.55
# ---- KANCA ----
SC('board', 'Cuma namazından çıkıyordu.', [
    P('ah', 'Cuma namazından', 'II. ABDÜLHAMİD', w=760, crop=[0, 0, 1, .7], shift=-1.2),
    TI('Cuma namazından', 'BOMBA\nPATLADI', 150, j=1, shift=-1.2, font='cond'),
    BD('Tam o sırada', 'YILDIZ CAMİİ · 1905', red=True, size=56),
], lead=.0, year=1905.55)
SC('board', 'Birkaç saniye sonra', [
    P('bomba', 'Birkaç saniye sonra', 'YILDIZ SUİKASTI', w=760),
    CT('Onlarca kişi', 0, 26, 'v => Math.round(v) + " ÖLÜ"', 140, dur=.8),
    TI('o birkaç saniyelik', 'BİRKAÇ SANİYE\nONU KURTARDI', 100, color='#f0754e'),
], year=1905.55, boom=True)
SC('dark', 'Tarih 21 Temmuz 1905’ti.', [
    TI('Tarih 21 Temmuz', '21 TEMMUZ 1905', 110),
    TI('otuz üç yıl', 'OTUZ ÜÇ YIL', 150, color='#f0754e'),
    TI('Sultan İkinci Abdülhamid’di', 'SULTAN II. ABDÜLHAMİD', 100),
])
SC('board', 'Bir taraf ona', [
    P('karikatur', 'Bir taraf ona', '“KIZIL SULTAN”', w=640),
    P('ahoturan', 'Öbür taraf', '“ULU HAKAN”', w=700),
    TH('karikatur', 'ahoturan'),
    TI('Peki gerçek Abdülhamid', 'GERÇEK ABDÜLHAMİD\nKİMDİ?', 100, color='#f0754e'),
], year=1900)
# ---- ÇOCUKLUK ----
SC('board', 'Abdülhamid 1842’de', [
    TG('Abdülhamid 1842’de', 'ÇIRAĞAN', '1842', 'İSTANBUL'),
    P('ciragan', 'Dolmabahçe’nin hemen', 'ÇIRAĞAN', w=900),
    TH('tag1', 'ciragan'),
    P('abdulmecid', 'Babası Sultan Abdülmecid’di', 'BABASI SULTAN ABDÜLMECİD', w=640),
], year=1842.7)
SC('dark', 'Ama çocukluğu mutlu', [
    TI('Annesi Tirimüjgan', 'ANNESİ TİRİMÜJGAN', 90),
    CT('on yaşındayken', 0, 10, 'v => Math.round(v) + " YAŞINDA"', 150, dur=.7, sub='ANNESİZ KALDI'),
    TI('yalnız büyüdü', 'YALNIZ BÜYÜDÜ', 120, color='#f0754e'),
], year=1853)
SC('board', 'Kardeşlerinden farklıydı.', [
    P('ahgenc', 'Kardeşlerinden farklıydı', 'ŞEHZADE ABDÜLHAMİD', w=700),
    TG('at binmeyi', 'AT · SİLAH', '', 'MARANGOZLUK'),
    P('marangoz', 'Evet, marangozluk', 'SARAY MARANGOZHANESİ', w=560),
    TH('ahgenc', 'marangoz'),
], year=1860)
SC('dark', '1867’de amcası', [
    P('abdulaziz', '1867’de amcası', None, w=800),
    TI('Paris’i, Londra’yı', 'PARİS · LONDRA · VİYANA', 80),
    TI('ne kadar geride', 'NE KADAR GERİDE?', 110, color='#f0754e'),
], year=1867.5)
# ---- 1876 ----
SC('dark', '1876 yılı', [
    TI('1876 yılı', '1876', 220, color='#f0754e', font='cond'),
], year=1876.4, boom=True)
SC('board', 'Mayıs ayında Sultan Abdülaziz', [
    P('abdulaziz', 'Mayıs ayında', 'SULTAN ABDÜLAZİZ · DARBE', w=640),
    BD('bilekleri kesik', 'BİLEKLERİ KESİK BULUNDU', red=True, size=54),
    P('murad5', 'Beşinci Murad', 'V. MURAD · SİNİR KRİZLERİ', w=640),
    TH('abdulaziz', 'murad5'),
    CT('doksan üç gün', 0, 93, 'v => Math.round(v) + " GÜN"', 140, dur=.8),
], year=1876.4)
SC('board', 'Ve 31 Ağustos 1876’da', [
    P('ahoval', 'Ve 31 Ağustos', 'II. ABDÜLHAMİD · 34 YAŞINDA', w=640),
    TG('31 Ağustos', 'TAHTA ÇIKIŞ', '1876', '31 AĞUSTOS'),
    TI('bir söz vermişti', 'BİR SÖZ\nVERMİŞTİ', 110, color='#f0754e'),
], year=1876.66)
SC('board', 'Sadrazam Mithat Paşa', [
    P('mithat', 'Sadrazam Mithat Paşa', 'MİTHAT PAŞA', w=640),
    P('kanun', '23 Aralık 1876’da', 'KANUN-İ ESASİ · 23 ARALIK 1876', w=560),
    TH('mithat', 'kanun'),
    P('meclis', 'ilk kez seçilmiş', 'MECLİS-İ MEBUSAN · 1877', w=880),
], year=1876.98)
# ---- 93 HARBİ ----
SC('dark', 'Ama bu bahar uzun', [
    TI('Ama bu bahar', 'BAHAR UZUN SÜRMEDİ', 110, color='#f0754e'),
])
SC('board', '1877’de Rusya', [
    P('harb93', '1877’de Rusya', '93 HARBİ · 1877-78', w=900),
    BD('Yeşilköy’e kadar', 'RUSLAR YEŞİLKÖY’DE', red=True, size=60),
    P('muhacir', 'Yüz binlerce Müslüman', 'MUHACİRLER · İSTANBUL', w=900),
    TH('harb93', 'muhacir'),
], year=1877.5)
SC('board', 'Meclis’te mebuslar', [
    DC('13 Şubat 1878’de', ['İRADE', 'YILDIZ', '13 ŞUBAT 1878'], 'MECLİS TATİL', keyAt='Meclis tatil edildi', h=880,
       stamp=dict(text='TATİL', t='Meclis tatil edildi', x=.1, y=.3, rot=-.1)),
    CT('tam otuz yıl', 0, 30, 'v => Math.round(v) + " YIL"', 160, dur=.9),
], year=1878.12)
SC('board', 'Anayasanın babası', [
    P('mithat', 'Anayasanın babası', 'MİTHAT PAŞA · SÜRGÜN', w=640),
    TG('Taif’te zindana', 'TAİF', '1884', 'ZİNDANDA ÖLDÜ'),
    TH('mithat', 'tag1'),
    BD('Kimilerine göre boğduruldu', 'BOĞDURULDU MU?', red=True, size=60),
], year=1884)
SC('dark', 'Sen Abdülhamid olsan', [
    TI('Sen Abdülhamid olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('meclisi açık tutar', 'MECLİSİ AÇIK MI TUTARDIN', 80),
    TI('bütün yetkiyi', 'YOKSA BÜTÜN YETKİYİ\nELİNE Mİ ALIRDIN?', 90, color='#f0754e'),
])
# ---- YILDIZ ----
SC('board', 'Abdülhamid, Dolmabahçe’yi', [
    P('yildiz', 'Yıldız Sarayı’na', 'YILDIZ SARAYI', w=900),
    TI('tek bir adamın', 'TEK BİR ADAMIN\nMASASI', 100, color='#f0754e'),
], year=1880)
SC('board', 'Yıldız, bir sarayın', [
    DC('yüzlerce jurnal', ['JURNAL', 'YILDIZ', 'GİZLİ'], 'İHBAR MEKTUBU', keyAt='ihbar mektubu', h=860),
    TG('Sansür o kadar', 'SANSÜR', '“BURUN”', 'BİLE YASAK?'),
    TH('doc1', 'tag1'),
], year=1890)
SC('dark', 'Paranoyak mıydı?', [
    TI('Paranoyak mıydı', 'PARANOYAK MIYDI?', 120, color='#f0754e'),
    TI('Bir amcası', 'AMCA: ÖLÜ BULUNDU', 80),
    TI('Bir ağabeyi', 'AĞABEY: AKLINI YİTİRDİ', 80),
    TI('suikast korkusuyla', 'SUİKAST KORKUSU', 110, color='#f0754e'),
])
# ---- ESERLER ----
SC('dark', 'Peki bu otuz yılda', [
    TI('Peki bu otuz', 'NE YAPTI?', 180, color='#f0754e'),
])
SC('board', 'Abdülhamid okullar açtı.', [
    P('mekteb', 'Abdülhamid okullar açtı', 'HAMİDİYE MEKTEPLERİ', w=640),
    P('mulkiye', 'Mülkiye, Tıbbiye', 'MÜLKİYE · TIBBİYE · DARÜLFÜNUN', w=880),
    TH('mekteb', 'mulkiye'),
    BD('Mustafa Kemal de dahil', 'MUSTAFA KEMAL DE BU OKULLARDA', red=True, size=48),
], year=1890)
SC('board', 'İmparatorluğu telgraf', [
    P('telgraf', 'İmparatorluğu telgraf', 'TELGRAF · YEMEN’DEN BASRA’YA', w=880),
    P('darulaceze', 'Darülaceze’yi açtı', 'DARÜLACEZE · 1896', w=880),
    TH('telgraf', 'darulaceze'),
], year=1896)
SC('board', 'Ve en büyük projesi', [
    TI('Hicaz Demiryolu', 'HİCAZ DEMİRYOLU', 110, font='cond'),
    P('hicaz', 'Şam’dan Medine’ye', 'ŞAM → MEDİNE', w=900),
    TG('bağışlarıyla', 'PARA', 'BAĞIŞ', 'DÜNYA MÜSLÜMANLARI'),
    TH('hicaz', 'tag1'),
    P('hicaz2', '1908’de tren', 'MEDİNE · 1908', w=900),
], year=1905)
SC('board', 'Bir de pek bilinmeyen', [
    TG('Polisiye romanlara', 'POLİSİYE', 'SHERLOCK', 'HOLMES'),
    P('album', 'Ve fotoğrafa', 'ABDÜLHAMİD ALBÜMLERİ', w=880),
    TH('tag1', 'album'),
    BD('Osmanlı geri değil', '“OSMANLI GERİ DEĞİL”', red=True, size=56),
], year=1893)
# ---- KARANLIK YÜZ ----
SC('dark', 'Ama bu tablonun', [
    TI('karanlık bir yüzü', 'KARANLIK YÜZ', 150, color='#f0754e'),
])
SC('board', '1881’de devletin', [
    P('duyun', '1881’de devletin', 'DÜYUN-I UMUMİYE · 1881', w=900),
    BD('yabancı alacaklıların', 'GELİRLER YABANCI ALACAKLILARDA', red=True, size=48),
], year=1881.97)
SC('board', 'Ve 1890’larda Doğu', [
    TG('Ve 1890’larda', 'DOĞU ANADOLU', '1890’LAR', 'ERMENİ OLAYLARI'),
    P('karikatur', 'Avrupa basını', 'AVRUPA BASINI', w=640),
    TH('tag1', 'karikatur'),
    TI('Kızıl Sultan.', '“KIZIL SULTAN”', 120, color='#f0754e', font='cond'),
], year=1895)
SC('dark', 'Abdülhamid’in politikası ise', [
    TI('Halifeliği öne', 'HALİFELİK', 160),
    TI('Halifeniz burada', '“HALİFENİZ BURADA”', 100, color='#f0754e'),
], year=1898)
# ---- SUİKAST ----
SC('dark', 'Ve sonra, o cuma', [
    TI('o cuma günü', 'O CUMA', 190, color='#f0754e', font='cond'),
], year=1905.55)
SC('board', '21 Temmuz 1905.', [
    P('cami', 'Yıldız Camii’nin önüne', 'YILDIZ (HAMİDİYE) CAMİİ', w=900),
    BD('saatli bombalı', 'SAATLİ BOMBALI ARABA', red=True, size=56),
    TG('Şeyhülislam’la', 'BİRKAÇ', 'DAKİKA', 'SOHBET'),
    TH('cami', 'tag1'),
    P('bomba2', 'Bomba hesaplanan', 'PATLAMA', w=880),
], year=1905.55, boom=True)
SC('dark', 'Ve anlatılanlara göre', [
    P('ahayakta', 'bombanın gürültüsü', None, w=560),
    TI('sakince saraya', 'SAKİNCE SARAYA DÖNDÜ', 90, color='#f0754e'),
])
# ---- 1908 ----
SC('board', 'Ama Yıldız’ın duvarları', [
    TG('İttihat ve Terakki', 'SELANİK', 'İTTİHAT', 'VE TERAKKİ'),
    P('mesrutiyet', '23 Temmuz 1908’de', 'MEŞRUTİYET · 23 TEMMUZ 1908', w=900),
    TH('tag1', 'mesrutiyet'),
    TI('padişahın zamanı', 'ZAMANI DOLMUŞTU', 110, color='#f0754e'),
], year=1908.56)
SC('board', 'Nisan 1909’da İstanbul’da', [
    P('mart31', 'Nisan 1909’da', '31 MART VAKASI', w=900),
    P('hareket', 'Hareket Ordusu', 'HAREKET ORDUSU', w=820),
    TH('mart31', 'hareket'),
    BD('hiçbir zaman kanıtlanamadı', 'İDDİA KANITLANAMADI', size=56),
], year=1909.3)
SC('board', '27 Nisan 1909’da', [
    DC('27 Nisan 1909’da', ['HAL’ FETVASI', 'MECLİS-İ UMUMÎ', '27 NİSAN 1909'], 'TAHTTAN İNDİRİLDİ', keyAt='tahttan indirildi', h=880,
       stamp=dict(text='HAL’', t='tahttan indirildi', x=.1, y=.3, rot=-.1)),
    P('alatini', 'Selanik’te, Alatini', 'ALATİNİ KÖŞKÜ · SELANİK', w=900),
    TH('doc1', 'alatini'),
], year=1909.32)
SC('board', 'Orada yine marangozluk', [
    P('marangoz', 'Orada yine', 'MARANGOZLUK', w=520),
    P('beylerbeyi', 'Beylerbeyi Sarayı’na', 'BEYLERBEYİ SARAYI · 1912', w=900),
    TH('marangoz', 'beylerbeyi'),
    TG('Balkanlar gitti', 'BALKANLAR', 'LİBYA', 'DÜNYA SAVAŞI'),
], year=1912.84)
SC('dark', '10 Şubat 1918’de', [
    P('cenaze', '10 Şubat 1918’de', None, w=900),
    CT('Yetmiş beş', 0, 75, 'v => Math.round(v) + " YAŞINDA"', 140, dur=.9),
    TI('imparatorluğun çöküşünü', 'ÇÖKÜŞÜ GÖRMEDİ', 100, color='#f0754e'),
], year=1918.11)
# ---- KAPANIŞ ----
SC('dark', 'Peki tarih Abdülhamid’i', [
    TI('Peki tarih', 'TARİH ONU\nNASIL HATIRLAMALI?', 110, color='#f0754e'),
])
SC('board', 'Bazıları için o, Ulu', [
    P('ahoturan', 'Bazıları için o, Ulu', '“ULU HAKAN”', w=700),
    P('karikatur', 'Bazıları için ise', '“KIZIL SULTAN”', w=640),
    TH('ahoturan', 'karikatur'),
    TI('Belki ikisi de', 'BELKİ İKİSİ DE', 110, color='#f0754e'),
])
SC('dark', 'Bazen insan, kaybetmekten', [
    TI('kaybetmekten o kadar', 'KAYBETME KORKUSU', 120),
    TI('korktuğu şeyi kendisi', 'KORKTUĞUNU\nKENDİSİ BÜYÜTÜR', 110, color='#f0754e'),
])
SC('dark', 'Abdülhamid imparatorluğu otuz', [
    HT('ah', 'Abdülhamid imparatorluğu', crop=[.1, .02, .8, .6], w=1000),
    TI('kendi korkusundan', 'KORKUSUNDAN\nKURTULAMADI', 110, color='#f0754e'),
])
SC('dark', 'Sence İkinci Abdülhamid', [
    TI('Kızıl Sultan mı', 'KIZIL SULTAN MI?', 140),
    TI('Ulu Hakan mı', 'ULU HAKAN MI?', 140, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
