# Mimar Sinan'ın kayıp kafatası (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Mimar Sinan: 1935, açılan mezar ve kayıp kafatası. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1500, 2020], 100, 1935.6
# ---- KANCA ----
SC('board', 'Mimar Sinan’ın mezarı açıldı.', [
    P('sinan', 'Mimar Sinan’ın', 'MİMAR SİNAN (TEMSİLİ)', w=1000, crop=[.05, 0, .9, .62], shift=-1.2),
    TI('Mimar Sinan’ın', 'MEZARI AÇILDI', 170, x=0, j=1, shift=-1.2, font='cond'),
    BD('Ve kafatası bir daha', 'KAFATASI GERİ DÖNMEDİ', red=True, size=62),
], lead=.0, year=1935.6)
SC('board', 'Süleymaniye’yi yapan', [
    P('suleymaniye', 'Süleymaniye’yi yapan', 'SÜLEYMANİYE', w=920),
    ST('hâlâ kayıp', 'KAFATASI', 'hâlâ kayıp.', 140),
], year=1557)
SC('dark', 'Ama asıl soru şu', [
    TI('Ama asıl soru', 'ASIL SORU', 150, color='#f0754e'),
    TI('Bir mimarın mezarını', 'MEZARI NEDEN\nAÇARSINIZ?', 130, lineAt=[0, 'neden açarsınız']),
], glitch=[('neden açarsınız', .25, .6)])
# ---- 1935 ----
SC('board', '1935 yazı.', [
    TG('1935 yazı', 'TÜRK TARİH KURUMU', '1935', 'İSTANBUL HEYETİ'),
    P('ttk', 'Türk Tarih Kurumu’ndan', 'TÜRK TARİH KURUMU · 1930’LAR', w=900),
    TH('tag1', 'ttk'),
    P('afet', 'Heyette Afet İnan', 'AFET İNAN', w=760),
    BD('antropolog Şevket Aziz', 'ANTROPOLOG ŞEVKET AZİZ KANSU', size=50),
], year=1935.58)
SC('dark', 'Süleymaniye’deki küçük türbeye', [
    P('turbeeski', 'Süleymaniye’deki küçük', None, w=1000),
    TI('mezarı açtılar', 'MEZAR AÇILDI', 150, color='#f0754e'),
], year=1935.58, boom=True)
SC('board', 'Amaç, Sinan’ın kafatasını', [
    P('olcum', 'Amaç, Sinan’ın', 'KAFATASI ÖLÇÜMÜ', w=880),
    P('cizim', 'O yıllarda kafatasının', '1930’LAR ANTROPOLOJİSİ', w=800),
    TH('olcum', 'cizim'),
    BD('bir ırkın bilimsel', '“IRKIN BİLİMSEL KANITI”', red=True, size=56),
], year=1935.6)
# ---- KÖKEN ----
SC('board', 'Çünkü Sinan’ın kökeni', [
    P('agirnas', 'Kayserili bir Hristiyan', 'AĞIRNAS · KAYSERİ', w=880),
    P('devsirme', 'devşirme olarak saraya', 'DEVŞİRME', w=760),
    TH('agirnas', 'devsirme'),
    TG('Bir taraf onu Türk', 'KÖKEN TARTIŞMASI', 'TÜRK?', 'RUM? ERMENİ?'),
], year=1512)
SC('dark', 'Sen olsan, bir dâhinin', [
    TI('Sen olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('kanıtlamak için mezarını', 'MEZARINI\nAÇAR MIYDIN?', 140, lineAt=[0, 'açar mıydın']),
], boom=True)
# ---- SONUÇ VE KAYIP ----
SC('board', 'Kansu ölçümü orada', [
    DC('Kansu ölçümü', ['ÖLÇÜM RAPORU', 'SÜLEYMANİYE', '1935'], '“TÜRK IRKINA UYGUN”', keyAt='Türk ırkına', h=980,
       stamp=dict(text='SONUÇ', t='Türk ırkına', x=.1, y=.3, rot=-.1)),
    TI('Türk ırkına uygun', '“TÜRK IRKINA\nUYGUN TİPTE”', 100, x=0, j=1),
], year=1935.6)
SC('board', 'Kafatası, açılacak bir', [
    P('koleksiyon', 'açılacak bir antropoloji', 'ANTROPOLOJİ MÜZESİ?', w=820),
    TG('Kansu’ya teslim', 'TESLİM', 'KANSU', 'ŞEVKET AZİZ'),
    TH('koleksiyon', 'tag1'),
    ST('Ama o müze', 'MÜZE', 'hiç açılmadı.', 150),
], year=1936)
SC('dark', 'Ve kafatası bir daha mezara', [
    P('turbe', 'Ve kafatası', None, w=1000),
    TI('mezara dönmedi', 'MEZARA DÖNMEDİ', 130, color='#f0754e'),
], year=1936)
SC('board', 'Bir fakültede mi', [
    P('dtcf', 'Bir fakültede mi', 'BİR FAKÜLTEDE Mİ?', w=880),
    P('raf', 'bir koleksiyonda mı', 'BİR KOLEKSİYONDA MI?', w=880),
    TH('dtcf', 'raf'),
    TI('Kimse bilmiyor.', 'KİMSE\nBİLMİYOR', 130, x=0),
    BD('hükümet arama', 'YILLAR SONRA: “ARAMA BAŞLAYACAK”', red=True, size=48),
], year=2010)
# ---- KAPANIŞ ----
SC('dark', 'Bazen bir insanı kim', [
    TI('Bazen bir insanı', 'KİM OLDUĞU İÇİN DEĞİL', 90),
    TI('bizim ne olduğumuzu', 'BİZİ KANITLAMAK İÇİN', 100, color='#f0754e'),
])
SC('dark', 'Sinan bize taştan', [
    P('selimiye', 'Sinan bize taştan', None, w=1000),
    TI('Biz onun kafatasını', 'KAFATASINI BİLE\nKORUYAMADIK', 110, color='#f0754e', lineAt=[0, 'koruyamadık']),
])
SC('dark', 'Sence mezarı açmak', [
    TI('bilim miydi', 'BİLİM Mİ?', 150),
    TI('saygısızlık mı', 'SAYGISIZLIK MI?', 130, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
