# Yaşar Nuri Öztürk: kendi sözleriyle (sinematik dosya, dikey). Sözler kaynaklı ve tarihli; README'de kaynak listesi.
BASLIK = 'Yaşar Nuri Öztürk: dört söz, iki tarafın öfkesi. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1995, 2020], 5, 2008.95
# ---- KANCA ----
SC('board', 'Türban, rahibe kıyafetidir.', [
    P('yno', 'Türban, rahibe', 'YAŞAR NURİ ÖZTÜRK', w=820, crop=[0, 0, 1, .72], shift=-1.2),
    TI('Türban, rahibe', '“TÜRBAN, RAHİBE\nKIYAFETİDİR.”', 120, x=0, j=1, shift=-1.2),
    BD('canlı yayında', 'CANLI YAYIN · ARALIK 2008', red=True, size=60),
], lead=.0, year=2008.95)
SC('dark', 'Dindarlar ayağa kalktı.', [
    TI('Dindarlar ayağa', 'DİNDARLAR\nAYAĞA KALKTI', 150, lineAt=['Dindarlar', 'ayağa kalktı.']),
    TI('laiklerin de hedefindeydi', 'LAİKLER DE', 150, color='#f0754e'),
    HT('yno', 'Adı Yaşar Nuri', crop=[.1, .02, .8, .55], w=1100, j=0),
    TI('Yaşar Nuri Öztürk’tü.', 'YAŞAR NURİ ÖZTÜRK', 120),
])
# ---- KİMDİ ----
SC('board', 'Dokuz yaşında hafız', [
    TG('Dokuz yaşında', '9 YAŞINDA', 'HAFIZ'),
    P('medrese', 'On yıl medrese', '10 YIL MEDRESE', w=880),
    TH('tag1', 'medrese'),
    P('medrese2', 'On iki yıl imamlık', '12 YIL İMAM VE VAİZ', w=880),
    BD('Hukuk ve ilahiyat', 'HUKUK + İLAHİYAT'),
    P('ilahiyat', 'İstanbul Üniversitesi', 'KURUCU DEKAN · 1993', w=880),
    TH('medrese2', 'ilahiyat'),
], year=1995)
SC('dark', 'Yani dini sokaktan', [
    P('kutuphane', 'Yani dini', None, w=1050),
    TI('kaynağından öğrenmişti', 'KAYNAĞINDAN', 150, color='#f0754e'),
    TI('Kendi sözleri.', 'KENDİ SÖZLERİ', 160, j=0),
])
# ---- DÖRT SÖZ ----
SC('board', 'Birinci söz.', [
    TG('Birinci söz.', 'SÖZ', '1', 'HÜRRİYET · 1998'),
    DC('bir gazete yazısında', ['HÜRRİYET', '16 OCAK 1998', 'ANADİLDE İBADET'], 'SERBESTLİK ALANI', keyAt='serbestlik alanı', h=1050),
    TI('Kur’an bu konuyu', '“KUR’AN BU KONUYU\nSERBESTLİK ALANI\nİÇİNDE BIRAKMIŞTIR.”', 82, x=0, j=1, lineAt=[0, 'serbestlik alanı', 'içinde bırakmıştır.']),
    TH('tag1', 'doc1'),
    P('mushaf2', 'Yüzyıllardır Arapça', 'ARAPÇA KILINAN NAMAZ', w=900),
    BD('kırmızı çizgiydi', 'KIRMIZI ÇİZGİ', red=True, size=90),
], year=1998)
SC('board', 'İkinci söz.', [
    TG('İkinci söz.', 'SÖZ', '2', 'HÜRRİYET · 2008'),
    DC('Kendini İslam dünyası', ['HÜRRİYET', '11 TEMMUZ 2008', '“İSLAM DÜNYASI”NA'], 'KUR’AN’IN DİNİ DEĞİL', keyAt='Kur’an’ın getirdiği', h=1050),
    TI('Yaşadığını iddia', '“YAŞADIĞINI İDDİA ETTİĞİ DİN,\nKUR’AN’IN GETİRDİĞİ\nDİN DEĞİLDİR.”', 72, x=0, j=1, lineAt=[0, 'Kur’an’ın getirdiği', 'din değildir.']),
    TH('tag1', 'doc1'),
    P('kitap', 'adını İslam', 'KUR’AN’DAKİ İSLAM', w=760),
], year=2008.5)
SC('board', 'Üçüncü söz, en çok', [
    TG('Üçüncü söz', 'EN ÇOK SES GETİREN', '3', 'TV · ARALIK 2008'),
    P('ynotv', 'Türban tartışmasının', 'CANLI YAYIN', w=900),
    TH('tag1', 'ynotv'),
    TI('Türban rahibe kıyafeti.', '“TÜRBAN RAHİBE\nKIYAFETİ.”', 120, x=0),
    BD('Çarşaf ise', '“ÇARŞAF DİNDE DEĞİL, GELENEKTE”', size=54),
], year=2008.95)
SC('dark', 'Sen olsan, bu sözü', [
    TI('Sen olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('Kızar mıydın', 'KIZAR MIYDIN?', 130),
    TI('Kur’an’ı açıp', 'AÇIP BAKAR MIYDIN?', 120, color='#f0754e'),
])
SC('board', 'Dördüncü söz.', [
    TG('Dördüncü söz.', 'SÖZ', '4', 'TV · 2015'),
    P('yno2', 'halk için', None, w=900),
    BD('Raiye, sürü', 'RAİYE = SÜRÜ', red=True, size=96),
    DC('Hakkında halkı', ['SORUŞTURMA', 'İSTANBUL', '2015'], 'KİN VE DÜŞMANLIĞA TAHRİK', keyAt='kin ve düşmanlığa', h=1000,
       stamp=dict(text='SORUŞTURMA', t='soruşturma açıldı.', x=.1, y=.3, rot=-.1)),
    BD('Savunması kısaydı', '“OSMANLI DÜZENİNDE HALK RAİYEDİR”', size=50),
    TH('tag1', 'yno2'),
], year=2015.4)
# ---- İKİ TARAF ----
SC('dark', 'Bir taraf ona', [
    TI('Bir taraf ona', '“DİNİ\nDEĞİŞTİRİYOR”', 160, color='#f0754e', lineAt=['Bir taraf', 'dini değiştiriyor']),
    BD('suikast planladıklarını', 'SUİKAST PLANI · 1999', red=True, size=70),
], year=1999)
SC('board', 'Öbür taraf, bir ilahiyatçının', [
    TI('Öbür taraf', '“İLAHİYATÇI SİYASETE\nGİRMESİN”', 88, x=0),
    P('siyaset', 'Milletvekili oldu', 'TBMM · 2002', w=900),
    TG('kendi partisini kurdu', 'KENDİ PARTİSİ', 'HYP', '2005'),
    BD('siyaseti bıraktı', 'SİYASETİ BIRAKTI · 2009'),
], year=2002)
SC('dark', 'Mide kanserine yenildi.', [
    P('cenaze', 'Mide kanserine', '22 HAZİRAN 2016', w=1050),
    TI('Kendi doğum gününde.', 'DOĞUM GÜNÜNDE', 140, color='#f0754e'),
], year=2016.47)
SC('dark', 'Bugün sözleri hâlâ', [
    HT('yno', 'Bugün sözleri', crop=[.1, .02, .8, .55], w=1100),
    TI('Kur’an’ı aç ve', 'KUR’AN’I AÇ,\nKENDİN OKU', 150, color='#f0754e', lineAt=['Kur’an’ı aç', 'kendin oku.']),
])
SC('dark', 'Bazen en çok kızdığımız', [
    TI('Bazen en çok', 'EN ÇOK KIZDIĞIMIZ İNSAN', 100),
    TI('en rahatsız edici', 'EN RAHATSIZ\nEDİCİ SORUYU\nSORAN KİŞİDİR', 130, color='#f0754e', lineAt=['en rahatsız', 'soruyu', 'soran kişidir.']),
])
SC('dark', 'Sence Yaşar Nuri', [
    TI('dini savundu', 'DİNİ SAVUNDU MU?', 120),
    TI('yoksa değiştirmeye', 'DEĞİŞTİRMEYE Mİ\nÇALIŞTI?', 120, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
