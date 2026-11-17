# Enver Paşa uzun video (yatay, sinematik dosya). Kaynaklar README'de.
BASLIK = 'Enver Paşa: Harbiye’den Belcuvan’a. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1880, 1925], 5, 1922.6
# ---- KANCA ----
SC('board', 'Kırk yaşındaydı.', [
    P('enver', 'Kırk yaşındaydı', 'ENVER PAŞA', w=760, crop=[0, 0, 1, .7], shift=-1.2),
    TI('Kırk yaşındaydı', 'KILIÇLA\nMAKİNELİ TÜFEĞE', 100, j=1, shift=-1.2),
    BD('Kızıl Ordu’nun', 'KIZIL ORDU · 1922', red=True, size=56),
], lead=.0, year=1922.6)
SC('dark', 'O gün Kurban Bayramıydı.', [
    TI('O gün Kurban', 'KURBAN BAYRAMI', 110),
    TI('Çegan adında', 'ÇEGAN TEPESİ · TACİKİSTAN', 64, color='#f0754e'),
    TI('Osmanlı İmparatorluğu’nu Birinci', 'İMPARATORLUĞU\nSAVAŞA SOKAN ADAM', 90, lineAt=[0, 'Birinci Dünya']),
    TI('Enver Paşa.', 'ENVER PAŞA', 170, color='#f0754e'),
], year=1922.6, boom=True)
SC('board', 'Bir yanda "Hürriyet', [
    P('enverniyazi', 'Bir yanda', '“HÜRRİYET KAHRAMANI”', w=860),
    P('sarikamis4', 'öbür yanda', '“İMPARATORLUĞU BATIRAN ADAM”', w=860),
    TH('enverniyazi', 'sarikamis4'),
    TI('Peki gerçek Enver', 'GERÇEK ENVER\nHANGİSİ?', 110, color='#f0754e'),
], year=1914)
# ---- ÇOCUKLUK ----
SC('board', 'Enver, 1881’de', [
    TG('Enver, 1881’de', 'DİVANYOLU', '1881', 'İSTANBUL'),
    P('enversivil', 'Babası Ahmed Bey', 'MEMUR ÇOCUĞU', w=700),
    TH('tag1', 'enversivil'),
    BD('ne paşa vardı', 'NE PAŞA NE SARAY', size=56),
], year=1881)
SC('board', 'Enver askerliği seçti.', [
    P('envergenc', 'Enver askerliği', 'HARBİYE · KURMAY SUBAY', w=700),
    TG('az konuşan', 'AZ KONUŞAN', 'ÇOK', 'ÇALIŞAN'),
    BD('kendinden çok emin', 'KENDİNDEN ÇOK EMİN', red=True, size=56),
], year=1902)
SC('dark', 'İlk görev yeri Makedonya’ydı.', [
    TI('İlk görev yeri', 'MAKEDONYA', 160),
    TI('Bulgar ve Rum', 'ÇETELERLE DAĞ DAĞ', 90, color='#f0754e'),
    TI('gizli bir cemiyete', 'GİZLİ CEMİYET', 120),
    TI('İttihat ve Terakki.', 'İTTİHAT VE TERAKKİ', 120, color='#f0754e'),
], year=1906)
# ---- 1908 ----
SC('dark', '24 Haziran 1908', [
    TI('24 Haziran', '24 HAZİRAN 1908', 120),
    TI('Enver dağa çıktı', 'DAĞA ÇIKTI', 200, color='#f0754e'),
], glitch=[('Enver dağa', .3, .7)], boom=True, year=1908.48)
SC('board', 'Birkaç hafta önce Resneli', [
    P('niyazi', 'Birkaç hafta önce', 'RESNELİ NİYAZİ BEY', w=700),
    P('abdulhamid', 'Sultan İkinci Abdülhamid’i', 'II. ABDÜLHAMİD', w=760),
    TH('niyazi', 'abdulhamid'),
    TG('otuz yıldır', 'MEŞRUTİYET', '30', 'YIL ASKIDA'),
], year=1908.45)
SC('board', 'Ve başardılar.', [
    P('hurriyet', 'Ve başardılar', 'MEŞRUTİYET İLAN EDİLDİ · TEMMUZ 1908', w=760),
    P('enverniyazi', 'Duvarlara iki genç', 'NİYAZİ VE ENVER', w=900),
    TH('hurriyet', 'enverniyazi'),
    TI('Hürriyet kahramanları', '“HÜRRİYET\nKAHRAMANLARI”', 100, color='#f0754e'),
], year=1908.56)
SC('dark', 'Henüz yirmi altı', [
    CT('yirmi altı', 0, 26, 'v => Math.round(v) + " YAŞINDA"', 170, dur=.9),
    TI('bütün imparatorluk', 'HERKES ONU TANIYORDU', 80, color='#f0754e'),
])
# ---- BERLİN ----
SC('board', 'Ödülü, Berlin’de', [
    TG('Ödülü, Berlin’de', 'ASKERÎ ATAŞE', 'BERLİN', '1909-1911'),
    P('kayzer', 'Kayzer’in gösterişine', 'KAYZER II. WILHELM', w=760),
    TH('tag1', 'kayzer'),
    BD('Bu hayranlık', 'BU HAYRANLIK KADER OLACAKTI', red=True, size=52),
], year=1909.2)
# ---- TRABLUSGARP ----
SC('board', '1911’de İtalya', [
    TG('1911’de İtalya', 'TRABLUSGARP', '1911', 'İTALYA SALDIRDI'),
    P('trablus', 'Enver, bir grup', 'ENVER · LİBYA ÇÖLÜ', w=760),
    TH('tag1', 'trablus'),
    P('mkderne', 'Mustafa Kemal.', 'BİNBAŞI MUSTAFA KEMAL', w=760),
    TH('trablus', 'mkderne'),
], year=1911.8)
SC('dark', 'Enver çölde Arap', [
    P('trablus2', 'Enver çölde', None, w=900),
    TI('gerilla savaşı', 'GERİLLA SAVAŞI', 120, color='#f0754e'),
    TI('geri çağrıldı', 'GERİ ÇAĞRILDI', 110),
], year=1912)
# ---- BALKAN ----
SC('board', 'Ve Balkan Savaşı', [
    P('balkan', 'Ve Balkan Savaşı', 'BALKAN SAVAŞI · 1912', w=960),
    BD('birkaç hafta içinde', 'BİRKAÇ HAFTADA ÇÖKÜŞ', red=True, size=58),
    TG('Çatalca’ya kadar', 'BULGAR ORDUSU', 'ÇATALCA', 'İSTANBUL’UN KAPISI'),
    BD('Edirne kuşatıldı.', 'EDİRNE KUŞATMADA', size=56),
], year=1912.85)
# ---- BABIALİ ----
SC('dark', '23 Ocak 1913.', [
    TI('23 Ocak', '23 OCAK 1913', 120),
    TI('Babıali’yi bastı', 'BABIALİ BASKINI', 150, color='#f0754e'),
], glitch=[('Babıali’yi bastı', .25, .6)], boom=True, year=1913.06)
SC('board', 'Hükümet binasına silahlı', [
    P('babiali', 'Hükümet binasına', 'LE PETIT JOURNAL · 1913', w=760),
    P('nazim', 'Harbiye Nazırı Nazım', 'NAZIM PAŞA · VURULDU', w=700),
    TH('babiali', 'nazim'),
    P('kamil', 'Sadrazam Kâmil Paşa', 'KÂMİL PAŞA · İSTİFA', w=700),
    ST('silah zoruyla', 'HÜKÜMET', 'silah zoruyla istifa', 110),
    BD('Bu bir darbeydi', 'BU BİR DARBEYDİ', red=True, size=70),
], year=1913.06)
SC('dark', 'Sen o gün Babıali’de', [
    TI('Sen o gün', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('Vatan elden gidiyor', '“VATAN ELDEN GİDİYOR”', 90),
    TI('bu yolun sonunun', 'YOKSA BU YOLUN\nSONU MU?', 100, color='#f0754e'),
])
# ---- EDİRNE ----
SC('board', 'Birkaç ay sonra, Bulgaristan', [
    TG('22 Temmuz', 'EDİRNE', '1913', '22 TEMMUZ'),
    P('edirne', 'Osmanlı birlikleri Edirne’ye', 'EDİRNE’YE GİRİŞ', w=760),
    TH('tag1', 'edirne'),
    TI('Edirne fatihi', '“EDİRNE FATİHİ”', 110, color='#f0754e'),
], year=1913.55)
SC('board', 'Sonrası baş döndürücü', [
    P('enver2', 'Sonrası baş döndürücü', 'ENVER PAŞA · HARBİYE NAZIRI', w=720),
    CT('otuz iki', 0, 32, 'v => Math.round(v) + " YAŞINDA NAZIR"', 110, dur=.9),
    P('dugun', 'Naciye Sultan’la', 'NACİYE SULTAN İLE · 1914', w=720),
    TH('enver2', 'dugun'),
    BD('sarayın damadıydı', 'MEMUR ÇOCUĞU → SARAY DAMADI', red=True, size=52),
], year=1914.1)
# ---- İTTİFAK ----
SC('dark', 'Ama asıl büyük karar', [
    TI('Ama asıl büyük', 'ASIL BÜYÜK KARAR', 120, color='#f0754e'),
])
SC('board', 'Ağustos 1914.', [
    DC('2 Ağustos’ta', ['GİZLİ İTTİFAK', 'OSMANLI - ALMANYA', '2 AĞUSTOS 1914'], 'ALMANYA İLE SAVAŞA', keyAt='gizli bir ittifak', h=880,
       stamp=dict(text='GİZLİ', t='gizli bir ittifak', x=.1, y=.3, rot=-.1)),
    P('enverkayzer', 'Berlin’e hayran', 'ENVER VE KAYZER', w=860),
    TH('doc1', 'enverkayzer'),
    P('goeben', 'Alman amiralin', 'YAVUZ (GOEBEN) · KARADENİZ', w=860),
    BD('Osmanlı artık savaştaydı', 'OSMANLI SAVAŞTA · EKİM 1914', red=True, size=56),
], year=1914.6)
SC('dark', 'Enver’e göre bu', [
    TI('imparatorluğun son', 'SON ŞANS', 180, color='#f0754e'),
    TI('Orta Asya’ya kadar', 'TURAN HAYALİ', 130),
])
# ---- SARIKAMIŞ ----
SC('map', 'Ve bu hayalin ilk sınavı', [
    RT('Kafkasya’daki karlı', ['erzurum', [42.59, 40.33]], 1.2),
    GD('Aralık 1914.', [42.59, 40.33], 'SARIKAMIŞ', square=True),
], cam=[(-.4, 'erzurum', .2), ('Aralık 1914.', [42.59, 40.33], .3)], year=1914.95)
SC('board', 'Enver, Sarıkamış’taki Rus', [
    P('sarikamis', 'Enver, Sarıkamış’taki', 'SARIKAMIŞ · ARALIK 1914', w=720),
    P('dag', 'Allahuekber Dağları’nı', 'ALLAHUEKBER DAĞLARI', w=960),
    TH('sarikamis', 'dag'),
    BD('eksi otuz derece', 'EKSİ 30 DERECE', red=True, size=70),
    P('sarikamis2', 'kışlık elbisesi', 'KIŞLIK ELBİSE YOK', w=900),
], year=1914.97)
SC('dark', 'Genelkurmay kayıtlarına göre', [
    P('sarikamis3', 'Genelkurmay kayıtlarına', None, w=1000),
    CT('yaklaşık altmış bin', 0, 60000, 'v => Math.round(v/1000) + " BİN KAYIP"', 120, dur=1.2, sub='GENELKURMAY KAYITLARI'),
    TI('soğuktan, hastalıktan', 'SOĞUK · HASTALIK · AÇLIK', 70, color='#f0754e'),
], year=1915.0)
SC('dark', 'Enver Ocak 1915’te', [
    TI('Enver Ocak', 'İSTANBUL’A DÖNDÜ', 120),
    TI('Yenilginin hesabını', 'HESAP SORULMADI', 120, color='#f0754e'),
    TI('Çünkü hesap soracak', 'HESAP SORACAK\nKİŞİ DE OYDU', 100),
], year=1915.03)
SC('dark', 'Peki bu kadar büyük', [
    TI('neden durmadı', 'NEDEN DURMADI?', 150, color='#f0754e'),
])
# ---- ÇANAKKALE, RAKİPLİK ----
SC('board', 'Belki de duramazdı.', [
    P('canakkale', 'Çanakkale’de, Irak’ta', 'ÇANAKKALE · IRAK · FİLİSTİN · KAFKASYA', w=860),
    TG('Başkomutan Vekili', 'BAŞKOMUTAN VEKİLİ', '4', 'CEPHE'),
    TH('canakkale', 'tag1'),
], year=1915.3)
SC('board', 'Çanakkale’de zafer', [
    P('mk', 'Libya’dan tanıdığı', 'MUSTAFA KEMAL', w=700),
    P('enverpelerin', 'İki adam aynı', 'ENVER', w=700),
    TH('mk', 'enverpelerin'),
    BD('birbirlerini hiç sevmediler', 'BİRBİRLERİNİ HİÇ SEVMEDİLER', red=True, size=52),
    TG('Almanlara körü körüne', 'MUSTAFA KEMAL’İN ELEŞTİRİSİ', 'SARIKAMIŞ', 'ALMAN BAĞLILIĞI'),
], year=1916)
SC('board', '1918 yazında Enver’in', [
    P('nuri', '1918 yazında', 'NURİ PAŞA · KAFKAS İSLAM ORDUSU', w=640),
    P('baku', 'Bakü’ye girdi', 'BAKÜ · EYLÜL 1918', w=900),
    TH('nuri', 'baku'),
    BD('Turan hayali', 'TURAN HAYALİ GERÇEK Mİ?', size=56),
], year=1918.7)
SC('board', 'Ama birkaç hafta sonra', [
    P('agamemnon', '30 Ekim 1918’de', 'AGAMEMNON ZIRHLISI · MONDROS', w=900),
    DC('Mondros Mütarekesi', ['MONDROS', '30 EKİM 1918', 'MÜTAREKE'], 'SAVAŞ KAYBEDİLDİ', keyAt='savaşı kaybetmişti', h=880),
    TH('agamemnon', 'doc1'),
], year=1918.83)
# ---- KAÇIŞ ----
SC('dark', '1 Kasım 1918 gecesi', [
    TI('1 Kasım', '1 KASIM 1918 GECESİ', 100),
    P('talat', 'Enver, Talat ve Cemal', 'TALAT · ENVER · CEMAL', w=760),
    TI('Alman gemisine', 'BİR ALMAN GEMİSİYLE\nKAÇIŞ', 90, color='#f0754e'),
], year=1918.84, boom=True)
SC('board', 'Arkalarında yıkılmış', [
    P('istanbul1918', 'Arkalarında yıkılmış', 'İŞGAL ALTINDA İSTANBUL', w=920),
    DC('divan-ı harp', ['DİVAN-I HARP', 'İSTANBUL', '1919'], 'GIYABEN İDAM', keyAt='gıyabında idam', h=880,
       stamp=dict(text='İDAM', t='idam kararı verdi', x=.1, y=.3, rot=-.1)),
    TH('istanbul1918', 'doc1'),
], year=1919.5)
SC('dark', 'Sen bu üç paşanın', [
    TI('Sen bu üç', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('kaçar mıydın', 'KAÇAR MIYDIN?', 120),
    TI('kalıp hesabını', 'KALIP HESAP\nVERİR MİYDİN?', 110, color='#f0754e'),
])
# ---- MOSKOVA, BATUM ----
SC('board', 'Enver Berlin’e gitti.', [
    TG('Enver Berlin’e', 'BERLİN', '→', 'MOSKOVA'),
    P('moskova', 'Bolşeviklere yanaştı', 'MOSKOVA · 1920', w=900),
    TH('tag1', 'moskova'),
    P('bakukongre', 'Doğu Halkları', 'BAKÜ · DOĞU HALKLARI KONGRESİ', w=900),
], year=1920.6)
SC('dark', 'Planı neydi?', [
    TI('Planı neydi', 'PLANI?', 180, color='#f0754e'),
    TI('Kurtuluş Savaşı’nın başına', 'KURTULUŞ SAVAŞI’NIN\nBAŞINA GEÇMEK', 90, lineAt=[0, 'başına geçmek']),
])
SC('board', 'Ama Anadolu’da artık', [
    P('sakarya', 'Ankara’da Mustafa Kemal', 'MUSTAFA KEMAL · ANKARA', w=860),
    BD('Enver’in gelmesini istemiyordu', 'ENVER İSTENMİYORDU', red=True, size=60),
    TG('Sarıkamış’ı', 'HALKIN HAFIZASI', 'SARIKAMIŞ', 'MONDROS · KAÇIŞ'),
], year=1921)
SC('board', 'Temmuz 1921.', [
    P('batum', 'Enver, sınırın', 'BATUM · TEMMUZ 1921', w=900),
    TG('Bazı tarihçilere göre', 'BAZI TARİHÇİLERE GÖRE', 'SAKARYA', 'SONUCUNU BEKLEDİ'),
    TI('Mustafa Kemal yenilirse', 'MUSTAFA KEMAL\nYENİLİRSE?', 100, color='#f0754e'),
], year=1921.55)
SC('dark', 'Ama Mustafa Kemal yenilmedi.', [
    TI('Sakarya kazanıldı', 'SAKARYA KAZANILDI', 120, color='#f0754e'),
    TI('sonsuza kadar kapandı', 'KAPI KAPANDI', 160),
], year=1921.7, boom=True)
# ---- TÜRKİSTAN ----
SC('board', 'Enver yüzünü doğuya', [
    P('buhara', 'Ekim 1921’de Buhara’ya', 'BUHARA · EKİM 1921', w=760),
    TG('Bolşevikler onu', 'GÖREV', '', 'DİRENİŞİ YATIŞTIR'),
    TH('buhara', 'tag1'),
], year=1921.8)
SC('board', 'Ama Enver orada taraf', [
    TI('taraf değiştirdi', 'TARAF DEĞİŞTİRDİ', 120, color='#f0754e'),
    P('basmaci', 'Basmacılara katıldı', 'BASMACILAR', w=900),
    P('enverbuhara', 'Kendine büyük unvanlar', 'ENVER · BUHARA 1922', w=700),
    TH('basmaci', 'enverbuhara'),
    BD('Halife damadı', 'MÜHÜRDE: “HALİFE DAMADI”', red=True, size=54),
], year=1922.2)
SC('dark', 'Ama elinde ne düzenli', [
    TI('Ama elinde', 'NE ORDU NE CEPHANE', 90, color='#f0754e'),
    P('kizilordu', 'Karşısında ise Kızıl', None, w=1000),
], year=1922.4)
# ---- ÖLÜM ----
SC('dark', '4 Ağustos 1922.', [
    TI('4 Ağustos', '4 AĞUSTOS 1922', 120),
    TI('Kurban Bayramı', 'KURBAN BAYRAMI', 120, color='#f0754e'),
    TI('Kızıl Ordu’nun baskınına', 'BAYRAM NAMAZINDA BASKIN', 74),
], year=1922.59, boom=True)
SC('board', 'Enver yanındaki bir avuç', [
    P('enverbuhara2', 'Enver yanındaki', 'BELCUVAN · ÇEGAN TEPESİ', w=760),
    TG('Anlatılanlara göre', 'ANLATILANLARA GÖRE', 'KILIÇ', 'SON HÜCUM'),
    CT('Kırk yaşındaydı', 0, 40, 'v => Math.round(v) + " YAŞINDA"', 150, dur=.8),
    BD('Âbıderya köyünde', 'ÂBIDERYA KÖYÜNE GÖMÜLDÜ', red=True, size=54),
], year=1922.59)
SC('board', 'Aynı günlerde, binlerce', [
    P('sakarya', 'Mustafa Kemal Büyük', 'MUSTAFA KEMAL · BÜYÜK TAARRUZ', w=860),
    TG('Üç hafta sonra', 'AFYON', '26', 'AĞUSTOS 1922'),
    TH('sakarya', 'tag1'),
], year=1922.65)
SC('dark', 'Biri kurduğu hayalin', [
    TI('Biri kurduğu', 'BİRİ HAYALİN PEŞİNDE ÖLDÜ', 70),
    TI('Öbürü, elindeki', 'ÖBÜRÜ GERÇEKLİKTEN\nDEVLET KURDU', 90, color='#f0754e', lineAt=[0, 'yeni bir devlet']),
])
SC('board', 'Enver’in naaşı tam', [
    CT('yetmiş dört yıl', 0, 74, 'v => Math.round(v) + " YIL SONRA"', 120, dur=1.0),
    P('tabut', '1996’da Türkiye’ye', 'NAAŞ İSTANBUL’DA · 1996', w=900),
    P('abide', 'Abide-i Hürriyet’e', 'ABİDE-İ HÜRRİYET', w=860),
    TH('tabut', 'abide'),
], year=1996)
# ---- KAPANIŞ ----
SC('dark', 'Peki tarih Enver’i', [
    TI('Peki tarih', 'TARİH ONU\nNASIL HATIRLAMALI?', 110, color='#f0754e'),
])
SC('board', 'Bazıları için o, cesaretiyle', [
    P('enver', 'Bazıları için o, cesaretiyle', 'KAHRAMAN', w=700, crop=[0, 0, 1, .7]),
    P('sarikamis4', 'Bazıları için ise', 'FELAKET', w=860),
    TH('enver', 'sarikamis4'),
    TI('Belki ikisi de', 'BELKİ İKİSİ DE', 110, color='#f0754e'),
])
SC('dark', 'Bazen insan, hayallerine', [
    TI('Bazen insan', 'HAYALİN BEDELİNİ', 110),
    TI('peşinden gelenler öder', 'PEŞİNDEN GELENLER\nÖDER', 120, color='#f0754e'),
])
SC('dark', 'Enver, imparatorluğu kurtarmak', [
    HT('enver', 'Enver, imparatorluğu', crop=[.1, .02, .8, .6], w=1000),
    TI('imparatorluğun sonunu', 'SONU YAKLAŞTIRDI', 110, color='#f0754e'),
])
SC('dark', 'Sence Enver Paşa', [
    TI('Kahraman mı', 'KAHRAMAN MI?', 150),
    TI('felaket mi', 'FELAKET Mİ?', 150, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
