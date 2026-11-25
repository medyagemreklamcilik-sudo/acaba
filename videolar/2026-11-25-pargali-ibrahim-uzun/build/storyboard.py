# Pargalı İbrahim: Kanuni'nin en yakın dostu. Uzun video (yatay, sinematik dosya). Kaynaklar README'de.
BASLIK = 'Pargalı İbrahim Paşa: Kanuni’nin en yakın dostu. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1490, 1540], 5, 1536.2
# ---- KANCA ----
SC('board', 'Bir Ramazan gecesi', [
    P('ibrahim', 'Bir Ramazan gecesi', 'PARGALI İBRAHİM PAŞA', w=760, crop=[.05, .05, .95, .85], shift=-1.2),
    TI('Bir Ramazan gecesi', 'İFTARDAN SONRA\nBOĞDURULDU', 130, j=1, shift=-1.2, font='cond'),
    BD('en yakın dostunu', 'EN YAKIN DOSTU · 1536', red=True, size=56),
], lead=.0, year=1536.2)
SC('board', 'Sabah olduğunda', [
    P('topkapi', 'Sabah olduğunda', 'TOPKAPI SARAYI', w=960),
    BD('Boğularak öldürülmüştü', 'BOĞULARAK ÖLDÜRÜLDÜ', red=True, size=62),
], year=1536.2, boom=True)
SC('board', 'Onu öldürten', [
    P('kanuni', 'Onu öldürten', 'KANUNİ SULTAN SÜLEYMAN', w=720, crop=[0, 0, 1, .8]),
    TI('kardeşim', '“KARDEŞİM”', 150, font='cond'),
], year=1536.2)
SC('board', 'Ölen adam, Pargalı', [
    P('ibrahim_b', 'Ölen adam', 'PARGALI İBRAHİM', w=640),
    TG('Bir balıkçı çocuğu', 'BALIKÇI ÇOCUĞU', '', 'KÖLE'),
    CT('on üç yıl', 0, 13, 'v => Math.round(v) + " YIL"', 160, dur=.9, sub='SADRAZAM'),
], year=1530)
SC('dark', 'Peki bir köle nasıl', [
    TI('Peki bir köle', 'KÖLEDEN\nSADRAZAMA', 140),
    TI('neden padişahın emriyle', 'NEDEN BOĞULDU?', 150, color='#f0754e', font='cond'),
    TI('Hırslarını, kibrini', 'HIRS · KİBİR · SÖZLER', 90),
], boom=True)
# ---- PARGA ----
SC('board', 'Hikâye, bugün Yunanistan’da', [
    P('parga3', 'küçük bir sahil kasabasında', 'PARGA, BUGÜN', w=900),
    TG('Parga.', 'VENEDİK’E BAĞLI', 'PARGA', 'EPİR'),
], year=1495)
SC('board', 'İbrahim 1495 civarında', [
    P('parga', 'İbrahim 1495', 'PARGA KALESİ', w=900),
    TG('Babasının bir balıkçı', 'BABASI', '1495', 'BALIKÇI / GEMİCİ'),
    TI('Ben Pargalıyım', '“BEN PARGALIYIM”', 110, color='#f0754e'),
], year=1495)
SC('board', 'Çocukken nasıl esir', [
    CT('altı yaşındayken', 0, 6, 'v => Math.round(v) + " YAŞINDA"', 130, dur=.6, sub='ESİR'),
    P('gemi', 'korsanlar onu kaçırdı', 'KORSANLAR', w=900),
    BD('köle olarak sattı', 'KÖLE OLARAK SATILDI', red=True, size=60),
], year=1501)
SC('board', 'Bir rivayete göre Manisa’da', [
    P('esir', 'bir dul kadına', 'ESİR PAZARI', w=900),
    ST('Tarihçiler bu hikâyelerin', 'KESİN BİLGİ', 'şüpheyle bakıyor', 110),
], year=1505)
SC('board', 'Kesin olan şu', [
    P('manisa', 'İbrahim gençliğinde Manisa’daydı', 'MANİSA', w=820),
    P('kanuni2', 'Şehzade Süleyman.', 'ŞEHZADE SÜLEYMAN', w=640),
    TH('manisa', 'kanuni2'),
], year=1513)
SC('board', 'İbrahim sıradan bir', [
    TG('birkaç dil konuşuyordu', 'DİLLER', '', 'TARİH MERAKI'),
    P('calgi', 'iyi bir müzisyendi', 'MÜZİSYEN', w=820),
    BD('Şehzadeye çalgı', 'ŞEHZADEYE ÇALGI ÇALDI', red=True, size=56),
], year=1515)
SC('dark', 'İki genç arasında', [
    TI('efendi ile köleden', 'EFENDİ VE KÖLE\nDEĞİL', 110),
    TI('dostluk doğdu', 'DOST', 200, color='#f0754e', font='cond'),
])
SC('dark', 'Belki sen de hayatında', [
    TI('Her şeyi paylaştığın', 'SENİ SENDEN\nİYİ BİLEN BİRİ', 110),
    TI('en büyük acıyı', 'EN BÜYÜK ACI', 140, color='#f0754e', font='cond'),
])
# ---- YÜKSELİŞ ----
SC('board', '1520’de Yavuz Sultan', [
    TG('1520’de Yavuz', 'TAHT', '1520', 'SÜLEYMAN 26 YAŞINDA'),
    P('kanuni3', 'Süleyman yirmi altı', 'SULTAN SÜLEYMAN', w=700),
    TH('tag1', 'kanuni3'),
], year=1520.75)
SC('board', 'Süleyman tahta çıkar', [
    P('saray', 'At Meydanı’nda', 'İBRAHİM PAŞA SARAYI', w=960),
    TI('birkaç yüz metre', 'PADİŞAHA\nBİRKAÇ YÜZ METRE', 100, color='#f0754e'),
], year=1521)
SC('board', 'İbrahim hızla yükseldi.', [
    TG('Belgrad seferinde', 'BELGRAD', '1521', 'KAPI AĞASI'),
    P('has_oda', 'has odabaşı', 'HAS ODA', w=900),
    BD('Padişahı uyurken', 'PADİŞAHIN EN YAKINI', red=True, size=60),
], year=1522)
SC('board', 'Venedik raporlarına göre', [
    P('venedik', 'Venedik raporlarına', 'VENEDİK', w=900),
    DC('aynı sofrada', ['RAPOR', 'VENEDİK ELÇİSİ', '1520’LER'], 'AYNI SOFRADA', keyAt='aynı sofrada'),
    TI('kıskanıyordu', 'SARAY\nKISKANIYORDU', 110, color='#f0754e'),
], year=1522)
SC('dark', 'Ve 27 Haziran 1523’te', [
    TI('27 Haziran 1523’te', '27 HAZİRAN 1523', 130, color='#f0754e', font='cond'),
    TI('Yerine İbrahim’i atadı', 'SADRAZAM\nİBRAHİM', 150),
], year=1523.5, boom=True)
SC('board', 'Bu, Osmanlı geleneğine', [
    ST('Osmanlı geleneğine', 'TEAMÜL', 'tamamen aykırıydı', 140),
    P('divan', 'imparatorluğun en yüksek', 'DİVAN-I HÜMAYUN', w=900),
    TG('Yaşı otuz bile', 'YAŞ', '<30', 'VEZİR-İ AZAM'),
], year=1523.5)
SC('board', 'Bir rivayete göre İbrahim', [
    DC('Süleyman’a bir ricada', ['RİVAYET', 'İBRAHİM’İN RİCASI', '1523'], 'YÜKSELEN DÜŞER', keyAt='yükselen düşer'),
    TI('asla öldürmeyeceğine', 'SENİ ASLA\nÖLDÜRMEYECEĞİM', 110, color='#f0754e', font='cond'),
], year=1523.5)
SC('dark', 'Bu hikâye gerçek mi', [
    TI('Bu hikâye gerçek mi', 'GERÇEK Mİ?', 160),
    TI('tüylerini diken', 'SONUNU BİLİYORUZ', 110, color='#f0754e'),
])
# ---- MISIR ----
SC('board', 'Saraydaki herkes bu', [
    TG('ikinci vezir Ahmed Paşa', 'RAKİP', '', 'AHMED PAŞA'),
    BD('kendi hakkı sayıyordu', 'SADRAZAMLIK BENİM HAKKIM', red=True, size=54),
], year=1523.6)
SC('board', 'Mısır’a varınca', [
    P('kahire', 'Mısır’a varınca', 'KAHİRE', w=960),
    TI('Kendini sultan ilan', 'KENDİNİ SULTAN\nİLAN ETTİ', 110, font='cond'),
    BD('başı İstanbul’a', 'BAŞI İSTANBUL’A GÖNDERİLDİ', red=True, size=54),
], year=1524.1, boom=True)
SC('board', 'Bu kez Süleyman', [
    P('ibrahim_oval', 'İbrahim Kahire’de', 'İBRAHİM PAŞA', w=620),
    DC('yeni bir kanunname', ['KANUNNÂME-İ MISIR', 'İBRAHİM PAŞA', '1525'], 'YENİ DÜZEN', keyAt='yeni bir kanunname'),
], year=1525)
SC('dark', 'Burada İbrahim’in en güçlü', [
    ST('padişahın gözdesi', 'GÖZDE', 'Sadece padişahın gözdesi değildi', 150),
    TI('yetenekli bir yöneticiydi', 'YETENEKLİ\nBİR YÖNETİCİ', 130, color='#f0754e', font='cond'),
])
SC('board', 'İbrahim’in evliliği de', [
    TG('Hatice Sultan’la', 'İDDİA 1', '', 'HATİCE SULTAN'),
    TG('Muhsine Hatun', 'İDDİA 2', '', 'MUHSİNE HATUN'),
    P('dugun', 'büyük bir düğün', 'AT MEYDANI ŞENLİĞİ', w=820),
], year=1524.4)
# ---- MOHAÇ ----
SC('dark', '1526 yazında İbrahim', [
    TI('ilk büyük sınavına', 'İLK BÜYÜK SINAV', 120),
    TI('Macaristan.', 'MACARİSTAN', 170, color='#f0754e', font='cond'),
], year=1526.6)
SC('board', 'Osmanlı ordusu, Mohaç', [
    P('mohac', 'Mohaç ovasında', 'MOHAÇ · SÜLEYMANNÂME', w=820),
    TG('29 Ağustos 1526', 'MOHAÇ', '1526', '29 AĞUSTOS'),
    BD('bir bataklıkta boğuldu', 'KRAL LAJOS BOĞULDU', red=True, size=58),
], year=1526.66, boom=True)
SC('board', 'Zaferin planında İbrahim’in', [
    P('mohac2', 'Zaferin planında', 'MOHAÇ', w=820),
    P('budin', 'Budin’e girdi', 'BUDİN', w=900),
    TH('mohac2', 'budin'),
], year=1526.7)
SC('board', 'İbrahim Budin’den İstanbul’a', [
    P('budin2', 'çok özel bir ganimet', 'BUDİN SARAYI', w=900),
    TI('Herkül, Apollon ve Diana', 'HERKÜL · APOLLON\nDİANA', 110, color='#f0754e', font='cond'),
], year=1526.8)
SC('board', 'Ve bu heykelleri', [
    P('atmeydani', 'kendi sarayının önüne', 'AT MEYDANI', w=960),
    P('heykel', 'diktirdi', 'BRONZ HEYKEL (TEMSİLİ)', w=520),
    TH('atmeydani', 'heykel'),
], year=1527)
SC('board', 'İstanbul halkı şaşırdı.', [
    TI('eski Yunan tanrılarının', 'PAŞANIN KAPISINDA\nTANRI HEYKELLERİ', 100),
    BD('gizlice Hristiyan', '“GİZLİCE HRİSTİYAN”', red=True, size=60),
], year=1527, glitch=[('Söylentiler yayıldı', .3, .6)])
SC('board', 'Figani adında genç', [
    DC('bir beyit yazdı', ['BEYİT', 'ŞAİR FİGANİ', '1530’LAR'], 'PUT DİKTİ', keyAt='bir beyit yazdı'),
    TI('Dünyaya iki İbrahim', '“DÜNYAYA İKİ\nİBRAHİM GELDİ”', 100, color='#f0754e'),
], year=1530)
SC('dark', 'Biri, putları kıran', [
    TI('putları kıran', 'PUT KIRAN', 140),
    TI('putları kapısına', 'PUT DİKEN', 160, color='#f0754e', font='cond'),
])
SC('dark', 'Figani bu beyti', [
    TI('hayatıyla ödedi', 'İDAM EDİLDİ', 170, color='#f0754e', font='cond'),
], boom=True, glitch=[('idam edildi', .3, .7)])
SC('dark', 'Sen olsan, seni eleştiren', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('affeder miydin', 'AFFEDER MİYDİN,\nSUSTURUR MUYDUN?', 110),
], boom=True)
SC('dark', 'İbrahim’in kibri', [
    HT('ibrahim', 'İbrahim’in kibri', crop=[.1, .05, .9, .85], w=900),
    TI('büyümeye başladı', 'KİBİR BÜYÜYOR', 130, color='#f0754e', font='cond'),
])
# ---- SERASKER / VİYANA ----
SC('board', '1529’da Süleyman', [
    TG('olağanüstü bir unvan', 'UNVAN', '1529', 'SERASKER'),
    P('ibrahim_at', 'ordunun başkomutanı', 'SERASKER İBRAHİM', w=700),
    BD('sıradan bir serasker', 'SIRADAN DEĞİL', red=True, size=60),
], year=1529.4)
SC('board', 'Anlatıldığına göre beratta', [
    DC('beratta', ['BERAT', 'SULTAN SÜLEYMAN', '1529'], 'SÖZÜ = PADİŞAHIN SÖZÜ', keyAt='padişahın sözü sayılacağı'),
    TI('en büyük yetkiydi', 'EN BÜYÜK YETKİ', 120, color='#f0754e', font='cond'),
], year=1529.4)
SC('map', 'Aynı yıl ordu Viyana’ya', [
    RT('Viyana’ya yürüdü', ['istanbul', [19.04, 47.5], [16.37, 48.21]], 2.0),
    GD('Habsburg imparatorluğunun', [16.37, 48.21], 'VİYANA', square=True),
], cam=[(-.4, 'istanbul', .2), ('Viyana’ya yürüdü', [19.04, 47.5], .25), ('Habsburg imparatorluğunun', [16.37, 48.21], .3)], year=1529.6)
SC('board', 'Ama bu kez işler', [
    P('viyana', 'Yağmurlar yolları', 'VİYANA KUŞATMASI · 1529', w=960),
    TG('Kuşatma Eylül sonunda', 'KUŞATMA', '1529', 'EYLÜL - EKİM'),
    ST('Viyana düşmedi', 'VİYANA', 'Viyana düşmedi', 160),
], year=1529.8, boom=True)
SC('dark', 'Osmanlı’nın Avrupa’daki', [
    TI('ilk kez burada durmuştu', 'İLK KEZ DURDU', 140, color='#f0754e', font='cond'),
    TI('ordunun başında İbrahim', 'BAŞINDA İBRAHİM', 110),
])
SC('board', 'Ama İbrahim bu yenilgiyi', [
    P('viyana2', 'Ama İbrahim', 'VİYANA', w=860),
    TI('hiç sarsılmadı', 'İTİBARI\nSARSILMADI', 120, font='cond'),
], year=1529.9)
# ---- 1533: KENDİ SÖZLERİ ----
SC('dark', 'Şimdi, İbrahim’in kendi ağzından', [
    TI('kendi ağzından', 'KENDİ AĞZINDAN', 150, color='#f0754e', font='cond'),
    TI('en iyi anlatan belgeler', 'BELGELER', 130),
], boom=True)
SC('board', '1533 baharında, Habsburg', [
    P('ferdinand', 'Ferdinand’ın iki elçisi', 'FERDİNAND', w=640),
    TG('27 Mayıs’ta', 'ELÇİLER', '1533', '27 MAYIS'),
    P('elci', 'İbrahim’in huzuruna', 'ELÇİ KABULÜ (TEMSİLİ)', w=860),
    TH('ferdinand', 'elci'),
], year=1533.4)
SC('board', 'Elçiler, bu görüşmeleri', [
    DC('Latince olarak', ['RELATIO', 'ZARA · SCHEPPER', '1533'], 'LATİNCE RAPOR', keyAt='Bu rapor bugün'),
    BD('inanılmaz bir özgüvenle', 'İNANILMAZ ÖZGÜVEN', red=True, size=58),
], year=1533.4)
SC('board', 'Elçilerin raporuna göre İbrahim', [
    DC('Bu büyük imparatorluğu', ['ELÇİ RAPORU', 'İBRAHİM PAŞA', '1533'], 'SE IMPERIUM REGERE', keyAt='ben yönetiyorum'),
    TI('Her şey benim elimde', '“HER ŞEY\nBENİM ELİMDE”', 130, color='#f0754e', font='cond'),
], year=1533.4)
SC('dark', 'Ve devam etti', [
    TI('Ben ne verirsem', '“BEN NE VERİRSEM\nVERİLMİŞ OLUR”', 110),
    TI('verilmiş sayılmaz', '“VERMEDİĞİM\nVERİLMEZ”', 130, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Düşün. Bunu söyleyen', [
    ST('Bunu söyleyen padişah', 'PADİŞAH', 'padişah değil', 170),
    TI('Padişahın veziri.', 'VEZİR', 180, color='#f0754e', font='cond'),
])
SC('board', 'Görüşmenin bir yerinde', [
    P('fransa', 'Fransa kralının', 'FRANSA KRALI FRANÇOIS', w=640),
    TG('bir yakutu gösterdi', 'YAKUT', '', 'KRALIN PARMAĞINDAN'),
    TH('fransa', 'tag1'),
], year=1533.4)
SC('board', 'Ferdinand’ın abisi', [
    P('sarlken', 'Şarlken hakkında', 'ŞARLKEN (KARL V)', w=640),
    DC('Barış yaparsak', ['ELÇİ RAPORU', 'İBRAHİM PAŞA', '1533'], 'KARL İMPARATOR KALIR', keyAt='imparator olarak kalmaya'),
    TI('iki dudağı arasındaydı', 'TAÇ ONUN\nDUDAKLARINDA', 100, color='#f0754e'),
], year=1533.4)
SC('board', 'Elçiler bu sözlerin', [
    BD('gösteriş olabileceğini', 'GÖSTERİŞ Mİ?', red=True, size=64),
    TG('padişahın kâtibi', 'ODADA', '', 'PADİŞAHIN KÂTİBİ'),
], year=1533.4)
SC('dark', 'Ama bir sorun vardı', [
    TI('padişaha ulaşabilirdi', 'PADİŞAH DUYARSA?', 130, color='#f0754e', font='cond'),
    TI('ne kadar süre sevebilirdi', 'NE KADAR\nSEVEBİLİRDİ?', 120),
], boom=True)
SC('board', 'İbrahim’in Avrupa’da başka', [
    P('venedik', 'Alvise Gritti', 'GRİTTİ’NİN VENEDİK’İ', w=900),
    TG('bankeri ve tercümanıydı', 'ALVİSE GRİTTİ', '', 'BANKER · TERCÜMAN'),
], year=1533.4)
SC('board', 'İbrahim, Habsburglarla ve', [
    P('tugra', 'mektuplaşıyordu', 'OSMANLI DİPLOMASİSİ', w=860),
    TI('padişahla birlikte', 'PADİŞAHLA\nBİRLİKTE YÖNETEN', 100, color='#f0754e'),
], year=1533.5)
# ---- IRAKEYN ----
SC('map', '1533 sonbaharında İbrahim', [
    RT('doğuya yürüdü', ['istanbul', 'erzurum', [46.29, 38.08], [44.37, 33.31]], 2.4),
    GD('Safevi İranı’ydı', [46.29, 38.08], 'TEBRİZ', square=True),
], cam=[(-.4, 'istanbul', .2), ('doğuya yürüdü', 'erzurum', .25), ('Safevi İranı’ydı', [46.29, 38.08], .3)], year=1533.8)
SC('board', 'Bu seferde İbrahim', [
    DC('serasker sultan', ['BELGE', 'İBRAHİM PAŞA', '1534'], 'SERASKER SULTAN', keyAt='serasker sultan'),
    TI('Sultan.', 'SULTAN', 200, color='#f0754e', font='cond'),
    BD('yalnızca padişah', 'YALNIZ HANEDANA AİT', red=True, size=56),
], year=1534, boom=True)
SC('board', '1534 Ağustos’unda Tebriz’e', [
    P('tebriz', 'Tebriz’e girdi', 'TEBRİZ · MATRAKÇI NASUH', w=820),
    P('bagdat', 'Bağdat’ı aldılar', 'BAĞDAT · MATRAKÇI NASUH', w=820),
    TH('tebriz', 'bagdat'),
], year=1534.6)
SC('dark', 'Ama bu sefer sırasında', [
    TI('ölümcül bir hata', 'ÖLÜMCÜL HATA', 160, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Ordunun defterdarı İskender', [
    TG('İskender Çelebi', 'DEFTERDAR', '', 'İSKENDER ÇELEBİ'),
    P('altin', 'en zengin ve', 'HAZİNE', w=640),
    BD('büyük bir düşmanlık', 'BÜYÜK DÜŞMANLIK', red=True, size=60),
], year=1534.8)
SC('board', 'İbrahim, İskender Çelebi’yi', [
    ST('yolsuzlukla suçladı', 'GÖREV', 'görevinden aldırdı', 130),
    TI('Bağdat’ta idam ettirdi', 'BAĞDAT’TA\nİDAM', 140, color='#f0754e', font='cond'),
], year=1535.2, boom=True)
SC('board', 'Anlatılanlara göre İskender', [
    DC('ölmeden önce', ['SON SÖZ', 'İSKENDER ÇELEBİ', '1535'], 'İBRAHİM HAİNDİR', keyAt='hainlik peşinde'),
], year=1535.2)
SC('dark', 'Sen Süleyman olsan', [
    TI('Sen Süleyman olsan', 'SEN SÜLEYMAN\nOLSAN?', 150, color='#f0754e'),
    TI('son sözüne inanır', 'İNANIR MIYDIN?', 120),
], boom=True)
SC('board', 'Tarihçi Celalzade Mustafa', [
    P('suleymanname', 'Tarihçi Celalzade', 'SÜLEYMANNÂME', w=760),
    TI('daha kibirli', 'DAHA SERT\nDAHA KİBİRLİ', 120, font='cond'),
], year=1535.5)
SC('board', 'Sarayda ise bir başka', [
    P('hurrem', 'Hürrem Sultan.', 'HÜRREM SULTAN', w=620),
    P('mustafa', 'Şehzade Mustafa’ya', 'ŞEHZADE MUSTAFA', w=620),
    TH('hurrem', 'mustafa'),
    BD('Hürrem’in oğlu değildi', 'HÜRREM’İN OĞLU DEĞİL', red=True, size=56),
], year=1535.6)
SC('dark', 'Birçok kişi, İbrahim’in', [
    TI('Hürrem’in parmağı', 'HÜRREM Mİ?', 160, color='#f0754e', font='cond'),
    ST('kanıtlayan bir belge', 'BELGE', 'belge yok', 130),
    TI('Süleyman’ın kendi kararı', 'SÜLEYMAN’IN\nKENDİ KARARI', 110),
])
# ---- SON ----
SC('dark', 'Ve 1536 Mart’ı geldi.', [
    TI('1536 Mart’ı geldi', 'MART 1536', 180, color='#f0754e', font='cond'),
], year=1536.2, boom=True)
SC('board', 'İbrahim o günlerde Fransa', [
    P('fransa', 'Fransa ile önemli', 'FRANSA ANTLAŞMASI', w=620),
    TI('padişahın verdiği sözü', 'VERİLEN SÖZ', 120, font='cond'),
], year=1536.1)
SC('board', '14 Mart 1536 akşamı', [
    TG('14 Mart 1536', 'RAMAZAN 22', '14 MART', '1536'),
    P('topkapi', 'onu iftara çağırdı', 'TOPKAPI SARAYI', w=900),
    BD('gece sarayda kaldı', 'GECE SARAYDA KALDI', red=True, size=60),
], year=1536.2)
SC('dark', 'Sabah, İbrahim’in cesedi', [
    HT('ibrahim_b', 'Sabah, İbrahim’in', crop=[.1, .05, .9, .8], w=900),
    TI('Boğularak öldürülmüştü', 'BOĞULDU', 170, color='#f0754e', font='cond'),
    TI('boğuşma izleri', 'BOĞUŞMA İZLERİ', 90),
], boom=True, glitch=[('boğuşma izleri', .3, .7)])
SC('board', 'Peki Süleyman’ın verdiği söz', [
    TI('verdiği söz ne oldu', 'YA YEMİN?', 140, font='cond'),
    DC('din alimine danıştı', ['RİVAYET', 'FETVA', '1536'], 'UYKU ÖLÜMÜN KARDEŞİ', keyAt='Uyku, ölümün kardeşidir'),
], year=1536.2)
SC('dark', 'Bu hikâyenin de gerçek', [
    TI('bir belge yok', 'BELGE YOK', 150),
    TI('bir dostun dostu', 'DOST DOSTU\nNASIL ÖLDÜRÜR?', 120, color='#f0754e', font='cond'),
])
SC('board', 'İbrahim’in cesedi, sessizce', [
    P('mezar', 'Galata’da, Tersane’nin', 'GALATA · CANFEDA (TEMSİLİ)', w=700),
    TG('Bütün serveti devlete', 'MÜSADERE', '1536', 'SERVET · SARAY'),
    TH('mezar', 'tag1'),
], year=1536.25)
SC('dark', 'Kimseden korkmayan adamın', [
    TI('mezarının yeri bile', 'MEZARI BİLE\nBİLİNMİYOR', 130, color='#f0754e', font='cond'),
])
SC('board', 'Halk ona öldükten sonra', [
    ST('Makbul İbrahim', 'MAKBUL', 'padişahın sevdiği', 150),
    TI('Maktul İbrahim', 'MAKTUL', 190, color='#f0754e', font='cond'),
], year=1536.3, boom=True)
SC('dark', 'Şimdi İbrahim’in hayatına', [
    TI('Doğruları ve yanlışlarıyla', 'DOĞRULAR\nYANLIŞLAR', 140),
])
SC('board', 'Doğruları: Mısır’ı yeniden', [
    TG('Doğruları:', 'DOĞRULAR', '+', 'MISIR · MOHAÇ'),
    P('kanuni_min', 'Avrupa diplomasisini', 'KANUNİ VE DİVANI', w=760),
    CT('On üç yıl boyunca', 0, 13, 'v => Math.round(v) + " YIL"', 140, dur=.9, sub='FİİLEN YÖNETTİ'),
], year=1530)
SC('board', 'Yanlışları: Kendini padişahla', [
    TG('Yanlışları:', 'YANLIŞLAR', '−', 'KİBİR'),
    TI('Her şey benim elimde', '“HER ŞEY\nBENİM ELİMDE”', 100, color='#f0754e'),
    TI('Kendine “sultan”', 'SULTAN', 140, font='cond'),
    BD('gücünün nereden geldiğini', 'GÜCÜNÜN KAYNAĞINI UNUTTU', red=True, size=54),
], year=1534)
SC('dark', 'Çünkü İbrahim’in bütün', [
    TI('tek bir adamın sevgisine', 'TEK BİR ADAMIN\nSEVGİSİ', 120),
    TI('geriye hiçbir şey kalmadı', 'HİÇBİR ŞEY KALMADI', 110, color='#f0754e', font='cond'),
])
SC('board', 'Pargalı bir balıkçı çocuğu', [
    P('parga2', 'Pargalı bir balıkçı', 'PARGA', w=640),
    P('ibrahim', 'ikinci adamı oldu', 'İKİNCİ ADAM', w=640, crop=[.05, .05, .95, .85]),
    TH('parga2', 'ibrahim'),
    BD('birinci adam olmaya', 'BİRİNCİ OLMAK İSTEDİ', red=True, size=58),
], year=1536)
SC('dark', 'İbrahim’i bir padişah', [
    TI('İbrahim’i bir padişah', 'ONU BİR PADİŞAH\nYÜKSELTTİ', 110),
    TI('kendi kibri oldu', 'KİBRİ BİTİRDİ', 150, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Peki sen ne düşünüyorsun?', [
    TI('Hürrem miydi', 'HÜRREM Mİ,\nKİBRİ Mİ?', 130),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
