# Lozan'ın "gizli maddeleri" efsanesi (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Lozan’ın gizli maddeleri: efsane ve belgeler. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1920, 2025], 15, 1923.56
# ---- KANCA ----
SC('board', 'İsmet Paşa Lozan’da', [
    P('ismet', 'İsmet Paşa Lozan’da', 'İSMET PAŞA', w=1000, crop=[.08, .05, .92, .6], shift=-1.2),
    TI('İsmet Paşa Lozan’da', 'GİZLİ MADDE\nİMZALADI MI?', 150, x=0, j=1, shift=-1.2, font='cond'),
    BD('Yıllarca anlatıldı', 'LOZAN 2023’TE BİTECEK?', red=True, size=58),
], lead=.0, year=1923.56)
SC('dark', 'Türkiye madenlerini', [
    TI('madenlerini çıkaramayacak', '“MADENLER\nYASAK”', 140, color='#f0754e', font='cond'),
])
SC('dark', '2023 geldi ve geçti.', [
    CT('2023 geldi', 2020, 2023, 'v => Math.round(v)', 260, dur=.8, sub='GELDİ VE GEÇTİ'),
    TI('Hiçbir şey olmadı.', 'HİÇBİR ŞEY\nOLMADI', 140, color='#f0754e', font='cond'),
], year=2023, boom=True)
SC('board', 'Çünkü Lozan’da gizli madde yok.', [
    ST('gizli madde yok', 'GİZLİ MADDE', 'gizli madde yok', 150),
    P('imza', 'Antlaşma 24 Temmuz', 'LOZAN · 24 TEMMUZ 1923', w=900),
    DC('tam metni yayımlandı', ['LOZAN SULH MUAHEDENAMESİ', 'TBMM ONAYI', '23 AĞUSTOS 1923'], 'TAM METİN YAYIMLANDI', keyAt='tam metni yayımlandı'),
    CT('143 madde', 0, 143, 'v => Math.round(v) + " MADDE"', 170, dur=1.0, sub='HEPSİ AÇIK'),
], year=1923.56, boom=True)
SC('board', 'Metinde bir bitiş tarihi', [
    ST('bitiş tarihi de yok', 'BİTİŞ TARİHİ', 'bitiş tarihi de yok', 140),
    TI('süresizdir', 'SÜRESİZ', 190, color='#f0754e', font='cond'),
], year=1923.56)
SC('board', 'Peki madenler?', [
    P('raman', 'Türkiye ilk petrolünü', 'RAMAN · 1940', w=900),
    TG('1940’ta Raman’da', 'İLK PETROL', '1940', 'RAMAN'),
    P('bor', 'bor, krom, altın', 'BOR MADENİ', w=860),
    BD('Lozan engel olsaydı', 'ENGEL OLSAYDI ÇIKARILAMAZDI', red=True, size=52),
], year=1940)
SC('dark', 'Sen olsan, yüz yıllık', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('bir mesaja inanır', 'OKUMADAN\nİNANIR MIYDIN?', 120),
], boom=True)
SC('board', 'Peki bu efsane nereden', [
    P('sevr', 'Sevr’le karıştırılmasından', 'SEVR HARİTASI · 1920', w=900),
    TI('gerçek eksiklerinden', 'GERÇEK\nEKSİKLER', 130, x=0, font='cond'),
], year=1920.6)
SC('board', 'Çünkü Lozan’da gerçekten', [
    TG('Musul çözülemeden', 'MUSUL', '1926', 'IRAK’A GEÇTİ'),
    P('curzon', 'İngiltere’nin kontrolündeki', 'LORD CURZON (İNGİLTERE)', w=640),
    BD('Batı Trakya ve On İki Ada', 'BATI TRAKYA · ON İKİ ADA', red=True, size=56),
], year=1926)
SC('board', 'Boğazlar da uluslararası', [
    P('bogaz', 'Boğazlar da', 'BOĞAZLAR', w=900),
    P('ulus', '1936’da Montrö', 'MONTRÖ · 1936', w=760, crop=[0, 0, 1, .6]),
    TH('bogaz', 'ulus'),
    BD('açıkça değiştirildi', 'AÇIKÇA DEĞİŞTİRİLDİ', red=True, size=60),
], year=1936.5)
SC('dark', 'Bazen gerçek, uydurmadan', [
    TI('daha az heyecanlıdır', 'GERÇEK\nDAHA SIKICI', 130),
    TI('daha hızlı yayılır', 'UYDURMA\nDAHA HIZLI', 140, color='#f0754e', font='cond'),
])
SC('dark', 'Lozan’ın sırrı yoktu.', [
    HT('ismet', 'Lozan’ın sırrı yoktu.', crop=[.08, .05, .92, .55], w=1000),
    ST('sırrı yoktu', 'SIR', 'sırrı yoktu', 150),
    TI('okunmamış sayfaları', 'OKUNMAMIŞ\nSAYFALAR', 130, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Sence Lozan bir zafer', [
    TI('Sence Lozan', 'ZAFER Mİ,\nEKSİK BARIŞ MI?', 120),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
