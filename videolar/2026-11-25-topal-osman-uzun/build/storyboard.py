# Topal Osman ve Ali Şükrü Bey cinayeti: uzun video (yatay, sinematik dosya). Kaynaklar README'de.
BASLIK = 'Topal Osman ve Ali Şükrü Bey: Cumhuriyet’in ilk siyasi cinayeti. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1880, 1925], 5, 1923.25
# ---- KANCA ----
SC('board', 'Ankara, Meclis binasının önü.', [
    P('topal_yuz', 'Ankara, Meclis', 'TOPAL OSMAN', w=760, crop=[.15, 0, .85, .8], shift=-1.2),
    TI('Ankara, Meclis', 'MECLİS’İN ÖNÜNDE\nASILDI', 140, j=1, shift=-1.2, font='cond'),
    BD('ayaklarından asılmış', 'ANKARA · NİSAN 1923', red=True, size=56),
], lead=.0, year=1923.25)
SC('board', 'Saatlerce orada kaldı.', [
    P('meclis', 'Saatlerce orada', 'BİRİNCİ MECLİS BİNASI', w=960),
    TG('Yoldan geçen', 'ULUS', '1923', 'SAATLERCE'),
    TH('meclis', 'tag1'),
], year=1923.25)
SC('board', 'Bu ceset, Mustafa Kemal’in', [
    P('mk', 'Mustafa Kemal’in', 'MUSTAFA KEMAL', w=700, crop=[0, 0, 1, .75]),
    P('topal', 'en sadık adamlarından', 'EN SADIK ADAMI', w=640),
    TH('mk', 'topal'),
    BD('Çankaya’yı koruyan', 'ÇANKAYA MUHAFIZ KOMUTANI', red=True, size=54),
    TI('Topal Osman diye', 'TOPAL OSMAN', 130, font='cond'),
], year=1923.25)
SC('dark', 'Ve birkaç gün önce', [
    TI('Meclis’in en cesur', 'MECLİS’İN EN CESUR\nMUHALİFİ', 110),
    TI('öldürmekle suçlanıyordu', 'CİNAYET', 190, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Öldürülen adam Trabzon', [
    P('ali', 'Öldürülen adam', 'ALİ ŞÜKRÜ BEY', w=760, crop=[0, 0, 1, .8]),
    TG('Trabzon mebusu', 'TRABZON MEBUSU', '1923', 'İKİNCİ GRUP'),
    BD('ilk siyasi cinayeti', 'İLK SİYASİ CİNAYET', red=True, size=62),
], year=1923.24)
SC('dark', 'Yüz yıldır aynı soru', [
    TI('kendi kafasına göre', 'KENDİ BAŞINA MI?', 130),
    TI('emir mi verdi', 'EMİR Mİ ALDI?', 150, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Bu videoda iki adamın', [
    P('ali_bahriye', 'kürsüden korkmayan', 'DENİZCİ', w=640),
    P('topal_b', 'savaş meydanından', 'KAYIKÇI', w=640),
    TH('ali_bahriye', 'topal_b'),
    BD('1923 baharında', 'ANKARA · 1923 BAHARI', red=True, size=56),
], year=1923.2)
# ---- ALİ ŞÜKRÜ ----
SC('board', 'Önce Ali Şükrü Bey.', [
    P('ali_portre', 'Ali Şükrü Bey.', 'ALİ ŞÜKRÜ', w=640),
    TG('1884’te İstanbul’da', 'KASIMPAŞA', '1884', 'İSTANBUL'),
    TH('ali_portre', 'tag1'),
    P('trabzon', 'Trabzon’un Şarlı', 'TRABZON', w=820),
], year=1884)
SC('board', 'On dört yaşında', [
    P('bahriye', 'On dört yaşında', 'HEYBELİADA BAHRİYE MEKTEBİ', w=900),
    CT('Yirmi yaşında', 0, 20, 'v => Math.round(v) + " YAŞINDA"', 120, dur=.7, sub='TEĞMEN'),
    TI('soru soruyordu', 'SORU SORAN\nBİR SUBAY', 100, color='#f0754e'),
], year=1898)
SC('board', '1911’de İngiltere’ye', [
    P('gemi', 'İngiltere’ye gönderildi', 'OSMANLI DONANMASI', w=900),
    TG('deniz hukuku', 'İNGİLTERE', '1911', 'DENİZ HUKUKU'),
    TH('gemi', 'tag1'),
], year=1911)
SC('board', '1914’te Almanya’dan', [
    BD('mayın getirdi', 'ALMANYA’DAN MAYIN', red=True, size=62),
    TI('Çanakkale’de', 'ÇANAKKALE', 130, font='cond'),
    TG('binbaşı rütbesiyle', 'BİNBAŞI', '1914', 'ORDUDAN AYRILDI'),
], year=1914)
SC('board', 'Savaş bitip İstanbul', [
    P('isgal', 'İstanbul işgal', 'İŞGAL ALTINDA İSTANBUL', w=960),
    BD('Gizli direniş', 'KARAKOL CEMİYETİ', red=True, size=60),
    TG('Gündoğdu adında', 'DERGİ', '1919', 'GÜNDOĞDU'),
], year=1919.2)
SC('map', 'Ve sonunda, işgal', [
    RT('Ankara’ya geçti', ['istanbul', 'ankara'], 1.4),
    GD('Ankara’ya geçti', 'ankara', 'ANKARA', square=True),
], cam=[(-.4, 'istanbul', .2), ('Ankara’ya geçti', 'ankara', .3)], year=1920.3)
SC('board', 'Trabzon onu milletvekili', [
    TG('Trabzon onu', 'MEBUS', '1920', 'TRABZON'),
    P('tbmm_acilis', '1920’de açılan', 'TBMM AÇILIŞI · 1920', w=960),
], year=1920.3)
SC('board', 'Mecliste ilk işlerinden', [
    DC('İçkiyi yasaklayan', ['KANUN TEKLİFİ', 'ALİ ŞÜKRÜ (TRABZON)', '1920'], 'İÇKİ YASAĞI', keyAt='İçkiyi yasaklayan'),
    BD('Kanun kabul edildi', 'KABUL EDİLDİ', red=True, size=64),
], year=1920.7)
SC('board', 'Ve bir de önerge verdi', [
    DC('önerge verdi', ['ÖNERGE', 'ALİ ŞÜKRÜ', '29 NİSAN 1920'], 'MUHAFIZ BİRLİĞİ', keyAt='önerge verdi'),
    P('meclis_kart', 'Meclis’i korumak', 'MECLİS', w=760),
], year=1920.33)
SC('dark', 'Hayatına mal olacak', [
    TI('Hayatına mal olacak', 'KENDİ ÖNERGESİ', 120),
    TI('ilk o hayal', 'İLK O İSTEDİ', 150, color='#f0754e', font='cond'),
])
SC('board', 'Ali Şükrü, mecliste tam', [
    CT('yüz seksen üç', 0, 183, 'v => Math.round(v) + " KONUŞMA"', 150, dur=1.0, sub='BİRİNCİ MECLİS'),
    ST('İstiklal Mahkemeleri’ne', 'İSTİKLAL MAHKEMELERİ', 'karşı çıktı', 90),
    P('meclis_ic', 'İkinci Grup’un', 'İKİNCİ GRUP’UN SESİ', w=900),
], year=1921.5)
# ---- TOPAL OSMAN ----
SC('board', 'Şimdi öbür adama', [
    P('topal', 'Topal Osman 1883’te', 'TOPAL OSMAN', w=640),
    TG('Giresun’da doğdu', 'GİRESUN', '1883', 'HACI HÜSEYİN MAH.'),
    P('giresun', 'kayıkçılık yaptı', 'GİRESUN', w=900),
    TH('topal', 'giresun'),
], year=1883)
SC('board', '1912’de Balkan Savaşı', [
    P('balkan', 'Balkan Savaşı başladı', 'BALKAN SAVAŞI · 1912', w=960),
    ST('askerlik bedeli', 'BEDEL ÖDENMİŞTİ', 'gitmek zorunda değildi', 90),
    BD('gönüllü olarak', 'GÖNÜLLÜ GİTTİ', red=True, size=64),
], year=1912.8)
SC('board', 'Çorlu civarında dizinden', [
    P('balkan2', 'Çorlu civarında', 'ÇORLU', w=820),
    TI('Topal Osman.', '“TOPAL”', 180, font='cond'),
], year=1912.9, boom=True)
SC('board', 'Birinci Dünya Savaşı’nda', [
    P('topal_grup', 'gönüllülerle', 'GİRESUN GÖNÜLLÜLERİ', w=960),
    CT('Yüzlerce adamı', 0, 700, 'v => Math.round(v) + " GÖNÜLLÜ"', 110, dur=1.0, sub='BATUM CEPHESİ'),
    BD('körü körüne bağlıydı', 'KÖRÜ KÖRÜNE BAĞLI', red=True, size=60),
], year=1915)
SC('board', 'Savaştan sonra Karadeniz’de', [
    P('milis', 'Pontus devleti', 'KARADENİZ MİLİSLERİ', w=900),
    P('topal_renk', 'Giresun’daki bu milis', 'GİRESUN', w=720),
    TH('milis', 'topal_renk'),
], year=1919.4)
SC('dark', 'Ama Topal Osman’ın efsanesinin', [
    TI('karanlık bir yüzü', 'KARANLIK YÜZÜ', 140, color='#f0754e', font='cond'),
    TI('baskınlar ve sürgünler', 'RUM KÖYLERİ\nBASKINLAR · SÜRGÜNLER', 90),
    TI('Bir taraf için kahraman', 'KAHRAMAN MI,\nKATİL Mİ?', 120),
], boom=True)
SC('map', '1921’de Koçgiri isyanını', [
    RT('Sivas’a gitti', [[38.39, 40.91], 'sivas'], 1.2),
    GD('Sivas’a gitti', 'sivas', 'KOÇGİRİ', square=True),
], cam=[(-.4, [38.39, 40.91], .2), ('Sivas’a gitti', 'sivas', .3)], year=1921.2)
SC('board', 'Aynı yaz Sakarya', [
    P('sakarya', 'Sakarya Savaşı’nda', 'SAKARYA · 1921', w=960),
    TG('47. Alay’ın', '47. ALAY', '1921', 'MANGALTEPE'),
    BD('yarbaylığa yükseldi', 'YARBAY', red=True, size=64),
], year=1921.65)
SC('board', 'Savaştan sonra Mustafa', [
    P('mk2', 'Mustafa Kemal onu', 'MUSTAFA KEMAL', w=660),
    P('cankaya', 'Çankaya’yı koruyan', 'ÇANKAYA KÖŞKÜ', w=900),
    TH('mk2', 'cankaya'),
    BD('muhafız taburunun komutanıydı', 'MUHAFIZ TABURU KOMUTANI', red=True, size=56),
], year=1922.95)
SC('dark', 'Yani Ali Şükrü’nün kurulmasını', [
    HT('topal_yuz', 'Yani Ali Şükrü’nün', crop=[.2, 0, .8, .7], w=900),
    TI('türden bir birliğin', 'KADERİN CİLVESİ', 110, color='#f0754e'),
])
SC('dark', 'Sen olsan, bir adamın', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('kapının önüne nöbetçi', 'KAPINA NÖBETÇİ\nKOYAR MIYDIN?', 110),
], boom=True)
# ---- 1923 ----
SC('board', '1923’ün başında Ankara', [
    P('ankara', 'Ankara gergindi', 'ANKARA · 1923', w=960),
    P('ismet', 'İsmet Paşa Lozan’da', 'İSMET PAŞA · LOZAN', w=760),
    TH('ankara', 'ismet'),
], year=1923)
SC('board', 'Ocak 1923’te Ali Şükrü', [
    P('tan', 'Tan adında', 'TAN GAZETESİ · OCAK 1923', w=760, crop=[0, 0, 1, .6]),
    P('hakimiyet', 'Hâkimiyet-i Milliye’ye', 'HÂKİMİYET-İ MİLLİYE', w=760, crop=[0, 0, 1, .6]),
    TH('tan', 'hakimiyet'),
    BD('muhalefetin sesiydi', 'MUHALEFETİN SESİ', red=True, size=60),
], year=1923.05)
SC('board', 'Mart 1923’te Lozan', [
    DC('gizli oturumlarda', ['GİZLİ CELSE', 'TBMM', 'MART 1923'], 'LOZAN', keyAt='gizli oturumlarda'),
    ST('Musul’un sonraya', 'MUSUL', 'sonraya bırakılmasını', 120),
    TI('görevinin bittiğini', 'HEYETİN GÖREVİ\nBİTMİŞTİR', 100, color='#f0754e'),
], year=1923.17)
SC('board', 'Mecliste hava elektrikliydi.', [
    P('ali', 'Ali Şükrü, artık', 'EN ÇOK KONUŞULAN MUHALİF', w=760, crop=[0, 0, 1, .8]),
], year=1923.2)
# ---- 27 MART ----
SC('dark', '27 Mart 1923 akşamı.', [
    TI('27 Mart 1923', '27 MART 1923', 150, color='#f0754e', font='cond'),
    TI('Merkez Kıraathanesi’ndeydi', 'MERKEZ KIRAATHANESİ', 100),
], year=1923.23, boom=True)
SC('board', 'Kaynaklara göre, Topal', [
    P('kahve', 'Kaynaklara göre', 'KIRAATHANE · ANKARA', w=900),
    TG('Mustafa Kaptan', 'TOPAL OSMAN’IN ADAMI', '', 'MUSTAFA KAPTAN'),
    BD('onunla gitti', 'ONUNLA GİTTİ', red=True, size=64),
], year=1923.23)
SC('dark', 'O geceden sonra', [
    TI('bir daha kimse', 'BİR DAHA\nGÖRÜLMEDİ', 150, color='#f0754e', font='cond'),
], glitch=[('canlı görmedi', .3, .7)])
SC('board', 'Anlatılanlara göre Topal', [
    P('sokak', 'Topal Osman’ın evine', 'ANKARA', w=820),
    BD('boğularak öldürüldü', 'BOĞULARAK ÖLDÜRÜLDÜ', red=True, size=60),
    TI('toprağa gömüldü', 'GİZLİCE\nGÖMÜLDÜ', 120, font='cond'),
], year=1923.23)
SC('dark', 'Sen Ali Şükrü’nün yerinde', [
    TI('Sen Ali Şükrü’nün', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('gider miydin', 'GİDER MİYDİN?', 130),
], boom=True)
SC('board', 'Ertesi gün Ali Şükrü', [
    P('ali_takim', 'Ertesi gün', 'KAYIP MEBUS', w=700),
    CT('Bir gün daha', 1, 5, 'v => Math.round(v) + ". GÜN"', 130, dur=1.4, sub='ALİ ŞÜKRÜ YOK'),
], year=1923.24)
SC('board', '1 Nisan 1923 Pazar', [
    TG('1 Nisan 1923', 'PAZAR', '1 NİSAN', '1923'),
    P('ankara2', 'Dikmen deresinin', 'DİKMEN DERESİ', w=900),
    TH('tag1', 'ankara2'),
    BD('Ali Şükrü Bey oradaydı', 'CESET BULUNDU', red=True, size=66),
], year=1923.25, boom=True)
SC('board', 'Meclis ayağa kalktı.', [
    P('meclis_kalabalik', 'Meclis ayağa kalktı', 'MECLİS AYAKTA', w=960),
    TI('daha yukarıya', 'DAHA YUKARI?', 130, color='#f0754e', font='cond'),
], year=1923.25)
SC('board', 'İşte tam o gün', [
    DC('meclis bir karar', ['KARAR', 'TBMM', '1 NİSAN 1923'], 'SEÇİM YENİLENECEK', keyAt='seçimler yenilenecekti'),
    BD('kendi sonunu', 'BİRİNCİ MECLİS’İN SONU', red=True, size=56),
], year=1923.25)
# ---- BASKIN ----
SC('dark', 'O gece Ankara’da', [
    P('tekce', 'İsmail Hakkı Bey', 'İSMAİL HAKKI (TEKÇE)', w=640, crop=[0, .1, .5, .7]),
    TI('kuşattı', 'KUŞATMA', 150, color='#f0754e', font='cond'),
    TG('Emrin Mustafa', 'EMİR', '', 'MUSTAFA KEMAL'),
], year=1923.25, boom=True)
SC('board', 'Topal Osman’ın adamları', [
    TI('teslim olmadı', 'TESLİM\nOLMADILAR', 130, font='cond'),
    CT('saatlerce sürdü', 0, 2, 'v => "2 NİSAN"', 120, dur=.5, sub='SABAHA KARŞI'),
    BD('kısa sürede öldü', 'TOPAL OSMAN ÖLDÜ', red=True, size=64),
], year=1923.25)
SC('board', '2 Nisan’da Başbakan', [
    P('rauf', 'Başbakan Rauf Bey', 'RAUF BEY (ORBAY)', w=640),
    DC('Katilin Topal Osman', ['TBMM ZABTI', 'RAUF BEY', '2 NİSAN 1923'], 'KATİL: TOPAL OSMAN', keyAt='gereken cezayı'),
], year=1923.25)
SC('dark', 'Ama meclis bununla', [
    TI('mezardan çıkarılıp', 'MEZARDAN\nÇIKARILDI', 130),
    TI('Meclis binasının önünde', 'MECLİS ÖNÜNDE\nASILDI', 140, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Ve videonun başındaki', [
    P('meclis', 'videonun başındaki', 'MECLİS ÖNÜ', w=900),
    P('topal_yuz', 'Kurtuluş Savaşı’nın', 'SAVAŞ KAHRAMANI', w=600, crop=[.15, 0, .85, .8]),
    TH('meclis', 'topal_yuz'),
], year=1923.25)
SC('board', 'Sonra ailesinin isteğiyle', [
    P('giresun2', 'Giresun’a götürüldü', 'GİRESUN', w=820),
    P('mezar_topal', 'Giresun Kalesi’nde', 'GİRESUN KALESİ · MEZAR', w=640),
    TH('giresun2', 'mezar_topal'),
], year=1923.3)
SC('map', 'Ali Şükrü Bey’in cenazesi', [
    RT('İnebolu üzerinden', ['ankara', [33.76, 41.98], [39.72, 41.0]], 2.0),
    GD('Trabzon’a gitti', [39.72, 41.0], 'TRABZON', square=True),
], cam=[(-.4, 'ankara', .2), ('İnebolu üzerinden', [33.76, 41.98], .25), ('Trabzon’a gitti', [39.72, 41.0], .3)], year=1923.27)
SC('board', '10 Nisan’da kalabalık', [
    P('trabzon2', 'limanda karşıladı', 'TRABZON LİMANI', w=900),
    TG('Boztepe’ye gömüldü', 'BOZTEPE', '10 NİSAN', 'TRABZON'),
], year=1923.27)
SC('dark', 'Trabzon’daki cenazede', [
    TI('Topal Osman değildi', 'HEDEF\nTOPAL OSMAN DEĞİLDİ', 110),
    TI('Doğrudan Mustafa Kemal’di', 'MUSTAFA KEMAL', 140, color='#f0754e', font='cond'),
])
# ---- ASIL SORU ----
SC('dark', 'Şimdi asıl soruya', [
    TI('kendi kafasına göre', 'KENDİ KAFASINA\nGÖRE Mİ?', 140, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Bir görüşe göre evet.', [
    TG('Bir görüşe göre evet.', '1. GÖRÜŞ', 'EVET', 'KENDİ BAŞINA'),
    P('topal', 'körü körüne bağlıydı', 'AŞIRI SADAKAT', w=640),
    BD('yakalanmasını emretti', 'YAKALANMASI EMREDİLDİ', red=True, size=58),
], year=1923.25)
SC('board', 'Öbür görüşe göre hayır.', [
    TG('Öbür görüşe göre hayır.', '2. GÖRÜŞ', 'HAYIR', 'SUSTURULDU'),
    P('rizanur', 'Rıza Nur', 'RIZA NUR (ANILAR)', w=640),
    TI('çok şey bildiği', 'ÇOK ŞEY\nBİLİYORDU', 110, color='#f0754e'),
], year=1923.25)
SC('dark', 'Ama Rıza Nur’un da', [
    TI('Anıları tarafsız değildir', 'TARAFSIZ DEĞİL', 120),
    ST('belge bulunamadı', 'CİNAYET EMRİ', 'belge bulunamadı', 120),
])
SC('board', 'Belgelerle bildiğimiz şunlar', [
    DC('Belgelerle bildiğimiz', ['DOSYA', 'ALİ ŞÜKRÜ CİNAYETİ', '1923'], 'AYDINLATILAMADI', keyAt='Belgelerle bildiğimiz'),
    BD('Mustafa Kaptan tutuklandı', 'MUSTAFA KAPTAN TUTUKLANDI', red=True, size=54),
], year=1923.3)
SC('board', 'Bir de sonrası var.', [
    P('cumhuriyet', 'İkinci Grup neredeyse', 'YAŞASIN CUMHURİYET · 1923', w=760, crop=[0, 0, 1, .6]),
    ST('İkinci Grup neredeyse', 'İKİNCİ GRUP', 'tamamen silindi', 110),
    TG('Cumhuriyet ilan edildi', 'CUMHURİYET', '1923', '29 EKİM'),
], year=1923.8)
SC('dark', 'Bazen bir patronu memnun', [
    TI('ondan bile ileri', 'PATRONDAN\nBİLE İLERİ', 140, color='#f0754e', font='cond'),
    TI('böyle birini tanıyorsundur', 'SEN DE TANIYOR\nMUSUN?', 100),
])
SC('board', 'Topal Osman’ın hikâyesi', [
    P('mezar_topal', 'Topal Osman’ın hikâyesi', 'GİRESUN KALESİ', w=640),
    DC('2022’de mecliste', ['KANUN TEKLİFİ', 'TBMM', '2022'], '1923 KARARI KALKSIN', keyAt='kaldırılması için'),
    TI('kahraman mı katil mi', 'KAHRAMAN MI,\nKATİL Mİ?', 110, color='#f0754e'),
], year=1923.3)
SC('dark', 'Ali Şükrü’yü bir ip', [
    TI('Ali Şükrü’yü bir ip', 'ALİ ŞÜKRÜ’YÜ\nBİR İP ÖLDÜRDÜ', 110),
    TI('Topal Osman’ı ise', 'TOPAL OSMAN’I\nBİR SIR', 140, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Peki sen ne düşünüyorsun?', [
    TI('kendi başına mı', 'KENDİ BAŞINA MI,\nEMİR Mİ?', 120),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
