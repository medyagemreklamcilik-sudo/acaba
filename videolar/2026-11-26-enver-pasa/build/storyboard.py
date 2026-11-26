# Enver Paşa: kahraman mı, felaket mi? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Enver Paşa: kahraman mı, felaket mi? "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1905, 1925], 5, 1914
# ---- KANCA ----
SC('board', 'Otuz iki yaşında', [
    P('enver', 'Otuz iki yaşında', 'ENVER PAŞA', w=1000, crop=[.12, .05, .88, .6], shift=-1.2),
    TI('Otuz iki yaşında', 'KAHRAMAN MI,\nFELAKET Mİ?', 150, x=0, j=1, shift=-1.2, font='cond'),
    BD('Kızıl Ordu’ya kılıçla', 'KIZIL ORDU’YA KILIÇLA', red=True, size=58),
], lead=.0, year=1914)
SC('dark', 'Enver Paşa kahraman', [
    TI('Enver Paşa kahraman', 'KAHRAMAN MI?', 160),
    TI('imparatorluğun felaketi', 'FELAKET Mİ?', 170, color='#f0754e', font='cond'),
], boom=True)
SC('board', '1908’de bütün ülke', [
    P('hurriyet', 'onun resmini', '“HÜRRİYET KAHRAMANI”', w=900),
    CT('yirmi altı yaşındaydı', 0, 26, 'v => Math.round(v) + " YAŞINDA"', 170, dur=.8, sub='1908'),
], year=1908.5)
SC('board', '1913’te bir avuç adamla', [
    P('babiali', 'Babıâli’yi bastı', 'BABIÂLİ BASKINI · 1913', w=880),
    BD('Harbiye Nazırı vuruldu', 'HARBİYE NAZIRI VURULDU', red=True, size=58),
    ST('hükümet düştü', 'HÜKÜMET', 'hükümet düştü', 150),
], year=1913.07, boom=True)
SC('board', 'Aynı yıl, Balkan Savaşı’nda', [
    P('edirne', 'Edirne’yi geri aldı', 'EDİRNE’Yİ GERİ ALDI', w=820),
    P('naciye', 'padişahın yeğeniyle', 'NACİYE SULTAN İLE', w=760),
    TH('edirne', 'naciye'),
    BD('Harbiye Nazırı oldu', 'HARBİYE NAZIRI · 32 YAŞ', red=True, size=58),
], year=1913.6)
SC('board', 'Sonra hayatının en büyük', [
    P('goeben', 'Almanya’nın yanında', 'YAVUZ (GOEBEN) · 1914', w=900),
    TI('Birinci Dünya Savaşı’na', 'SAVAŞA\nSOKTU', 150, x=0, font='cond'),
], year=1914.8, boom=True)
SC('board', 'Aynı kış Sarıkamış’ta', [
    P('sarikamis', 'karlı dağlardan', 'SARIKAMIŞ · 1914', w=900),
    CT('yaklaşık altmış bin', 0, 60, 'v => Math.round(v) + " BİN"', 200, dur=1.0, sub='GENELKURMAY'),
    BD('soğuktan ve hastalıktan', 'SOĞUK VE HASTALIK', red=True, size=62, y=.78),
], year=1914.97)
SC('dark', 'Sen olsan, böyle bir', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('komutayı bırakır', 'KOMUTAYI\nBIRAKIR MIYDIN?', 120),
], boom=True)
SC('board', 'Enver bırakmadı.', [
    P('enver2', 'Enver bırakmadı.', 'BIRAKMADI', w=820, crop=[.1, .05, .9, .6]),
    ST('imparatorluk çöktü', 'İMPARATORLUK', 'imparatorluk çöktü', 130),
], year=1918)
SC('board', '1918’de bir Alman gemisiyle', [
    P('kacis', 'İstanbul’dan kaçtı', 'ENVER · TALAT · CEMAL', w=900),
    DC('idam kararı', ['DİVAN-I HARP', 'GIYABİ', '1919'], 'İDAM', keyAt='idam kararı'),
], year=1918.84)
SC('board', 'Son durağı Orta Asya', [
    P('asya', 'Orta Asya oldu', 'ENVER, BUHARA', w=820),
    TG('4 Ağustos 1922', 'ÇEGAN', '1922', 'KURBAN BAYRAMI'),
    BD('atıyla saldırdı', 'ATIYLA SALDIRDI · VURULDU', red=True, size=56),
], year=1922.6, boom=True)
SC('dark', 'Bazen en büyük cesaret', [
    TI('durmayı bilmektir', 'DURMAYI\nBİLMEK', 160, color='#f0754e', font='cond'),
])
SC('dark', 'Enver Paşa korkudan', [
    HT('enver', 'Enver Paşa korkudan', crop=[.12, .05, .88, .55], w=1000),
    ST('korkudan değil', 'KORKU', 'korkudan değil', 150),
    TI('hiç durmamaktan', 'HİÇ DURMAMAKTAN', 120, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Sence kahraman mı', [
    TI('Sence kahraman mı', 'KAHRAMAN MI,\nFELAKET Mİ?', 130),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
