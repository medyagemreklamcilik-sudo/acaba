# Kösem Sultan: yarım asır imparatorluğu yöneten kadın. Uzun video (yatay, sinematik dosya). Kaynaklar README'de.
BASLIK = 'Kösem Sultan: yarım asır imparatorluğu yöneten kadın. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1585, 1655], 5, 1651.67
# ---- KANCA ----
SC('board', '2 Eylül 1651 gecesi, Topkapı', [
    P('kosem_g2', '2 Eylül 1651 gecesi', 'KÖSEM SULTAN (TEMSİLİ)', w=760, crop=[.3, 0, 1, .6], shift=-1.2),
    TI('2 Eylül 1651 gecesi', 'HAREMDE\nBİR GECE', 150, j=1, shift=-1.2, font='cond'),
    BD('Silahlı adamlar', 'SİLAHLI ADAMLAR KORİDORDA', red=True, size=54),
], lead=.0, year=1651.67)
SC('dark', 'Onu bir odada', [
    P('olum', 'Onu bir odada', 'TEMSİLİ GRAVÜR', w=900),
    TI('o gece öldürdüler', 'O GECE\nÖLDÜRDÜLER', 130, color='#f0754e', font='cond'),
], year=1651.67, boom=True)
SC('board', 'Bu kadın, Osmanlı’yı', [
    TI('Kösem Sultan’dı', 'KÖSEM SULTAN', 160, font='cond'),
    CT('Altı padişah gördü', 0, 6, 'v => Math.round(v) + " PADİŞAH"', 150, dur=.8, sub='YARIM ASIR'),
    TG('İkisinin annesi', 'ANNE · BÜYÜKANNE', '', 'IV. MURAD · İBRAHİM · IV. MEHMED'),
], year=1640)
SC('dark', 'Bir taraf ona', [
    TI('devleti ayakta tutan', 'DEVLETİ AYAKTA\nTUTAN KADIN', 110),
    TI('iktidar hırsı', 'İKTİDAR HIRSI', 150, color='#f0754e', font='cond'),
    TI('gerçek Kösem kimdi', 'GERÇEK KÖSEM\nKİMDİ?', 110),
], boom=True)
# ---- KÖKEN ----
SC('board', 'Kösem’in çocukluğu', [
    TG('Ortodoks papazın kızıydı', 'RİVAYET', '', 'PAPAZ KIZI · BOSNA'),
    ST('kanıtlayan bir belge', 'BELGE', 'belge yok', 120),
], year=1589)
SC('board', 'Ölümünde altmış iki', [
    CT('1589 civarında', 1580, 1589, 'v => Math.round(v)', 200, dur=.8, sub='DOĞUM (TAHMİNİ)'),
    P('harem', 'Saraya genç bir kız', 'TOPKAPI HAREMİ', w=860),
    TI('Ay yüzlü', 'MAHPEYKER\n“AY YÜZLÜ”', 120, color='#f0754e', font='cond'),
], year=1589)
SC('dark', '“Kösem” ise bir lakaptı', [
    TI('pürüzsüz, kılsız cildinden', 'PÜRÜZSÜZ TEN?', 120),
    TI('sürünün önünde giden koç', 'SÜRÜNÜN ÖNÜNDEKİ\nKOÇ', 120, color='#f0754e', font='cond'),
    TI('Yani lider.', 'LİDER', 190, font='cond'),
])
SC('board', 'Genç Sultan Birinci Ahmed', [
    P('ahmed1', 'Genç Sultan Birinci Ahmed', 'I. AHMED', w=700),
    BD('en gözde hasekisi', 'EN GÖZDE HASEKİ', red=True, size=62),
], year=1605)
SC('board', '1612’de bir oğul doğurdu', [
    TG('Murad.', 'OĞUL', '1612', 'MURAD'),
    TG('İbrahim.', 'OĞUL', '1615', 'İBRAHİM'),
    TI('görmezden gelemiyordu', 'GÖRMEZDEN\nGELİNEMEZ', 110, color='#f0754e'),
], year=1612.5)
SC('board', 'Bazı tarihçilere göre Kösem', [
    ST('kardeş katli', 'KARDEŞ KATLİ', 'fiilen sona erdi', 120),
    DC('Kösem’in de bunda', ['TARİHÇİLER', 'TDV İSLÂM ANS.', 'KÖSEM SULTAN'], 'NİSPİ PAYI', keyAt='payı olduğu'),
], year=1617)
SC('dark', 'Belki de ilk büyük', [
    TI('bir annenin korkusundan', 'BİR ANNENİN\nKORKUSU', 150, color='#f0754e', font='cond'),
])
# ---- ESKİ SARAY ----
SC('board', '1617’de Sultan Ahmed', [
    P('turbe', 'Sultan Ahmed, henüz', 'I. AHMED TÜRBESİ', w=820),
    CT('yirmi yedi yaşında', 0, 27, 'v => Math.round(v) + " YAŞINDA"', 150, dur=.8, sub='1617'),
], year=1617.9, boom=True)
SC('board', 'Kösem’in oğulları çok küçüktü.', [
    P('mustafa1', 'Ahmed’in kardeşi Mustafa', 'I. MUSTAFA', w=640),
    P('genc_osman2', 'Genç Osman çıktı', 'GENÇ OSMAN', w=640),
    TH('mustafa1', 'genc_osman2'),
], year=1618)
SC('board', 'Kösem, Eski Saray’a', [
    P('eskisaray', 'Eski Saray’a gönderildi', 'ESKİ SARAY', w=900),
    CT('yaklaşık altı yıl', 0, 6, 'v => Math.round(v) + " YIL"', 170, dur=.8, sub='BEKLEYİŞ'),
], year=1619)
SC('board', 'Bu yıllarda imparatorluk', [
    BD('kendi yeniçerileri', 'GENÇ OSMAN BOĞULDU', red=True, size=60),
    P('yedikule', 'Yedikule’de boğuldu', 'YEDİKULE · 1622', w=900),
    TI('çökmenin eşiğindeydi', 'ÇÖKÜŞÜN\nEŞİĞİNDE', 130, color='#f0754e', font='cond'),
], year=1622.4, boom=True)
SC('dark', 'Sen Kösem olsan, bu kaosta', [
    TI('Sen Kösem olsan', 'SEN KÖSEM\nOLSAN?', 170, color='#f0754e'),
    TI('Bekler miydin', 'BEKLER MİYDİN,\nHAREKETE Mİ GEÇERDİN?', 100),
], boom=True)
# ---- VALİDE ----
SC('board', '10 Eylül 1623’te sıra', [
    TG('10 Eylül 1623’te', 'CÜLUS', '1623', '10 EYLÜL'),
    P('murad_genc', 'Dördüncü Murad olarak', 'IV. MURAD', w=700),
], year=1623.7)
SC('board', 'Kösem özel bir törenle', [
    P('harem_koridor', 'Topkapı’ya döndü', 'TOPKAPI', w=860),
    BD('Valide Sultan’dı', 'VALİDE SULTAN', red=True, size=66),
    TI('devleti fiilen o', 'DEVLETİ O\nYÖNETİYORDU', 120, color='#f0754e', font='cond'),
], year=1623.7)
SC('board', 'Sadrazamlarla yazışıyor', [
    DC('Sadrazamlarla yazışıyor', ['TEZKİRE', 'VALİDE SULTAN', '1620’LER'], 'KENDİ PARASIYLA', keyAt='kendi parasını'),
    P('bagdat', 'Bağdat’ın kaybı', 'BAĞDAT', w=760),
], year=1625)
SC('dark', 'Bir kadının devleti', [
    CT('yaklaşık dokuz yıl', 0, 9, 'v => Math.round(v) + " YIL"', 200, dur=.8, sub='BİR KADININ YÖNETİMİ'),
])
SC('board', 'Ama Murad büyüyordu.', [
    P('murad4', 'Ama Murad büyüyordu', 'IV. MURAD', w=700),
    TG('1632’de yeniçeriler', 'İSYAN', '1632', 'SARAY BASILDI'),
    TI('korkunun padişahı', 'KORKUNUN\nPADİŞAHI', 130, color='#f0754e', font='cond'),
], year=1632.3, boom=True)
SC('board', 'İçkiyi, tütünü', [
    P('kahvehane', 'kahvehaneleri yasakladı', 'KAHVEHANE', w=860),
    BD('tebdil-i kıyafetle', 'GECE TEBDİL-İ KIYAFET', red=True, size=56),
], year=1633)
SC('dark', 'Ve Kösem’in en büyük', [
    TI('en büyük acısı', 'EN BÜYÜK ACI', 150, color='#f0754e', font='cond'),
    TG('1635’te Bayezid', 'İDAM', '1635', 'BAYEZİD · SÜLEYMAN'),
    TG('1638’de Kasım', 'İDAM', '1638', 'KASIM'),
], year=1635.6, boom=True)
SC('dark', 'Kasım, Kösem’in kendi', [
    TI('kendi oğluydu', 'KENDİ OĞLUYDU', 150, color='#f0754e', font='cond'),
], glitch=[('kendi oğluydu', .3, .7)])
SC('board', 'Kösem bu ölümleri', [
    P('ibrahim', 'bir oğlunu kurtardı', 'İBRAHİM', w=700),
    TI('aciz ve zavallı', '“ÂCİZ VE\nZAVALLI”', 130, font='cond'),
], year=1638)
SC('dark', 'Bir anne, oğlunu', [
    TI('dünyanın gözünde küçültmek', 'KURTARMAK İÇİN\nKÜÇÜLTMEK', 120, color='#f0754e', font='cond'),
])
# ---- İBRAHİM ----
SC('board', '1640’ta Dördüncü Murad', [
    CT('yirmi yedi yaşında', 0, 27, 'v => Math.round(v) + " YAŞINDA"', 140, dur=.7, sub='IV. MURAD ÖLDÜ'),
    BD('hayatta kalan tek erkeği', 'HANEDANIN TEK ERKEĞİ', red=True, size=58),
    P('ibrahim', 've İbrahim tahta çıktı', 'SULTAN İBRAHİM', w=700),
], year=1640.1)
SC('board', 'Kösem yeniden güç kazandı', [
    TI('erkek evlat sahibi', 'ERKEK EVLAT\nŞART', 130, font='cond'),
    TG('tek bir adama', 'HANEDAN', '1', 'TEK ADAM: İBRAHİM'),
], year=1641)
SC('board', 'Bunu başardı.', [
    P('mehmed4', 'birçok oğlu oldu', 'İBRAHİM’İN OĞLU MEHMED', w=640),
    ST('beklediği padişah', 'İYİ PADİŞAH', 'padişah olmadı', 120),
], year=1642)
SC('board', 'İsrafı, öfkesi', [
    TI('devleti sarstı', 'DEVLET\nSARSILDI', 140, color='#f0754e', font='cond'),
    BD('bir bahçe köşküne', 'ANNESİNİ UZAKLAŞTIRDI', red=True, size=56),
    TG('Rodos’a sürmek', 'RİVAYET', '', 'RODOS’A SÜRGÜN?'),
], year=1645)
SC('board', '1648 yazında devlet adamları', [
    P('yeniceri', 'yeniçeri ağaları', 'YENİÇERİ AĞALARI', w=640),
    DC('tahttan indirilecekti', ['KARAR', 'DEVLET ERKÂNI', '1648'], 'VALİDE ONAYI ŞART', keyAt='Valide Sultan’ın'),
], year=1648.5)
SC('board', 'Kösem önce direndi.', [
    P('mehmed4b', 'torunu, altı yaşındaki', 'IV. MEHMED', w=640),
    TG('8 Ağustos 1648’de', 'CÜLUS', '1648', '8 AĞUSTOS'),
], year=1648.6)
SC('dark', 'On gün sonra İbrahim', [
    TI('boğduruldu', 'İBRAHİM\nBOĞDURULDU', 150, color='#f0754e', font='cond'),
    TI('parmağı olduğunu', 'KÖSEM’İN\nPARMAĞI?', 110),
], year=1648.63, boom=True)
SC('dark', 'Sen olsan, devleti kurtarmak', [
    TI('Sen olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('kendi oğlunun tahttan', 'OĞLUNU\nFEDA EDER MİYDİN?', 110),
], boom=True)
# ---- TURHAN ----
SC('board', 'Kösem artık “büyük valide”', [
    TI('büyük valide', 'BÜYÜK VALİDE', 140, font='cond'),
    P('turhan', 'Turhan Sultan.', 'TURHAN SULTAN (TEMSİLİ)', w=640, crop=[.12, .1, .88, .58]),
], year=1648.7)
SC('board', 'Turhan yirmili yaşlarındaydı.', [
    TG('üç bin akçe', 'KÖSEM', '3000', 'AKÇE / GÜN'),
    TG('iki bin akçeydi', 'TURHAN', '2000', 'AKÇE / GÜN'),
    BD('Haremin yönetimi', 'HAREM HÂLÂ KÖSEM’DE', red=True, size=58),
], year=1649)
SC('board', 'Saray ikiye bölündü.', [
    P('yeniceri', 'yeniçeri ağaları vardı', 'KÖSEM’İN YANINDA', w=640),
    P('agasi', 'harem ağaları', 'TURHAN’IN YANINDA', w=640),
    TH('yeniceri', 'agasi'),
], year=1650)
SC('board', 'Kâtip Çelebi’nin anlattığına', [
    DC('bir plan yaptı', ['PLAN', 'KÂTİP ÇELEBİ’YE GÖRE', '1651'], 'MEHMED İNECEK', keyAt='tahttan indirilecek'),
    BD('Turhan’ın da öldürülmesi', 'TURHAN DA ÖLECEKTİ', red=True, size=58),
], year=1651.5)
SC('dark', 'Kösem yeniçeri ağalarına', [
    TI('gizli mektuplar', 'GİZLİ\nMEKTUPLAR', 140),
    TI('sırlar uzun süre saklanmaz', 'SIR SAKLANMAZ', 130, color='#f0754e', font='cond'),
])
SC('board', 'Kösem’in hizmetindeki', [
    TG('Meleki Kadın', 'İHBAR', '', 'MELEKİ KADIN'),
    CT('on dört ağa', 0, 14, 'v => Math.round(v) + " AĞA"', 150, dur=.7, sub='KARAR: ÖLÜM'),
], year=1651.6)
SC('board', '2 Eylül 1651 gecesi, Ramazan', [
    TG('2 Eylül 1651', 'RAMAZAN 16', '1651', '2 EYLÜL'),
    P('harem', 'Kösem’in dairesine girdi', 'HAREM', w=860),
], year=1651.67, boom=True)
SC('dark', 'Kösem kaçmaya çalıştı.', [
    P('olum2', 'bir dolabın üzerinde', 'TEMSİLİ GRAVÜR', w=900),
    TI('perde kordonuyla', 'PERDE KORDONU', 120, color='#f0754e', font='cond'),
], year=1651.67, glitch=[('saç örgüsüyle', .3, .7)])
SC('dark', 'Yarım asır sarayı', [
    TI('bir gecede öldü', 'BİR GECEDE', 170, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'Cenazesi Sultanahmet', [
    P('sultanahmet', 'Sultanahmet Camii’nin', 'SULTANAHMET', w=900),
    BD('Turhan artık', 'TURHAN TEK HÂKİM', red=True, size=62),
], year=1651.7)
# ---- MİRAS ----
SC('board', 'Kösem’in ardından kalan', [
    P('valide_han', 'Büyük Valide Han’da', 'BÜYÜK VALİDE HAN', w=820),
    CT('yirmi sandık', 0, 20, 'v => Math.round(v) + " SANDIK"', 170, dur=.9, sub='ALTIN VE MÜCEVHER'),
], year=1651.7)
SC('board', 'Ama Kösem’i sadece', [
    P('cinili', 'Çinili Camii’yi', 'ÇİNİLİ CAMİİ · 1640', w=820),
    TG('Büyük Valide Han’ı', 'VAKIF', '1651', 'BÜYÜK VALİDE HAN'),
], year=1640)
SC('board', 'Hapishanelerdeki borçluların', [
    TI('borçlarını ödedi', 'BORÇLARI\nÖDEDİ', 130, font='cond'),
    P('mekke', 'hacılara su', 'MEKKE · HACILARA SU', w=820),
], year=1645)
SC('dark', 'Yani aynı kadın', [
    TI('oğullarının ölümüne', 'OĞULLARININ\nÖLÜMÜ', 120),
    TI('binlerce yoksulu', 'BİNLERCE\nYOKSUL', 140, color='#f0754e', font='cond'),
])
SC('board', 'Turhan Sultan ise', [
    P('koprulu', 'Köprülü Mehmed Paşa’yı', 'KÖPRÜLÜ MEHMED PAŞA', w=640),
    P('yenicami', 'Yeni Cami’yi', 'YENİ CAMİ', w=760),
    TH('koprulu', 'yenicami'),
], year=1656)
SC('dark', 'Kösem’in bir zamanlar', [
    TI('onu öldürten gelini', 'ONU EN İYİ\nANLAYAN: GELİNİ', 110, color='#f0754e', font='cond'),
])
SC('dark', 'Sen de belki', [
    TI('zamanla benzediğini', 'KAVGA ETTİĞİNE\nBENZEMEK', 120),
])
SC('board', 'Şimdi Kösem’e bir bütün', [
    TG('Doğruları:', 'DOĞRULAR', '+', 'DEVLETİ TUTTU'),
    BD('Hanedanın soyunu', 'HANEDANI SÜRDÜRDÜ', red=True, size=58),
], year=1640)
SC('board', 'Yanlışları: İktidarı', [
    TG('Yanlışları:', 'YANLIŞLAR', '−', 'İKTİDARI BIRAKMADI'),
    ST('İbrahim’in tahttan', 'OĞUL', 'razı oldu', 120),
    TI('gelinini öldürtmeye', 'GELİNİNİ\nÖLDÜRTMEK', 120, color='#f0754e', font='cond'),
], year=1651)
SC('dark', 'Kösem Sultan yarım asır', [
    TI('hep kazandı', 'HEP KAZANDI', 150),
    TI('Sadece bir kez kaybetti', 'BİR KEZ KAYBETTİ', 130, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Peki sen ne düşünüyorsun?', [
    TI('devleti kurtaran', 'DEVLETİ KURTARAN MI,\nHIRSIN KURBANI MI?', 100),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
