# Kanuni'nin ölümü 48 gün saklandı (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Kanuni Sultan Süleyman: Zigetvar 1566. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1560, 1570], 2, 1566.68
# ---- KANCA ----
SC('board', 'Padişah ölmüştü.', [
    P('kanuni', 'Padişah ölmüştü.', 'KANUNİ SULTAN SÜLEYMAN', w=1000, crop=[.12, .02, .8, .62], shift=-1.2),
    TI('Padişah ölmüştü.', 'PADİŞAH\nÖLMÜŞTÜ', 170, x=0, j=1, shift=-1.2, font='cond'),
    BD('Ama ordu ona', 'ORDU ZAFER MÜJDESİ GETİRDİ', red=True, size=54),
], lead=.0, year=1566.68)
SC('board', 'Kanuni Sultan Süleyman, ölümünü', [
    TG('haftalarca', 'GİZLİ', '1566', 'HAFTALARCA'),
    P('cadir', 'bir çadırda yattı', 'OTAĞ-I HÜMAYUN', w=960),
    TH('cadir', 'tag1'),
], year=1566.68)
SC('dark', 'Bu sırrı kim sakladı', [
    TI('Bu sırrı kim', 'KİM SAKLADI?', 170, color='#f0754e', font='cond'),
    TI('neden sakladı?', 'NEDEN?', 150),
], boom=True)
# ---- ZİGETVAR ----
SC('board', 'Macaristan, Zigetvar kalesi.', [
    P('kale', 'Zigetvar kalesi', 'ZİGETVAR KUŞATMASI', w=900),
    TG('72 yaşındaki', 'KANUNİ', '72', 'SON SEFER'),
    P('kanuni_min', 'son seferindeydi', 'SULTAN SÜLEYMAN', w=560),
    TH('kale', 'tag1'),
], year=1566.6)
SC('dark', 'Kale düşmek üzereyken', [
    HT('kanuni_prof', 'padişah bir gece', crop=[.3, .05, .45, .9], w=1000),
    TI('çadırında öldü', 'BİR GECE ÖLDÜ', 140, color='#f0754e', font='cond'),
], year=1566.68, boom=True)
SC('board', 'Bunu bilen yalnızca', [
    BD('yalnızca birkaç kişi', 'BİLEN: BİRKAÇ KİŞİ', size=60),
    P('sokullu', 'Sadrazam Sokullu', 'SOKULLU MEHMED PAŞA', w=900, crop=[.05, .05, .9, .7]),
    ST('hepsine yemin ettirdi', 'KONUŞMAK', 'yemin ettirdi', 140),
], year=1566.68)
# ---- SIR ----
SC('board', 'Padişahın iç organları', [
    P('kazi', 'iç organları', 'ZİGETVAR, BUGÜN: KAZI', w=620),
    P('otag', 'çadırın altına gömüldü', 'ÇADIRIN ALTINA', w=920),
    BD('Bedeni mumyalandı', 'BEDENİ MUMYALANDI', red=True, size=62),
    TH('otag', 'kazi'),
], year=1566.68)
SC('board', 'Yatağına ise bir adam', [
    TI('bir adam yatırıldı', 'YATAĞINDA\nBAŞKASI', 150, x=0, font='cond'),
    TG('sadece hasta', 'ORDUYA GÖRE', '', 'PADİŞAH HASTA'),
], year=1566.68, glitch=[('bir adam', .3, .7)])
SC('dark', 'Sen Sokullu’nun yerinde', [
    TI('Sen Sokullu’nun', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('gerçeği söyler miydin', 'GERÇEĞİ\nSÖYLER MİYDİN?', 130),
], boom=True)
SC('board', 'Zigetvar düştü.', [
    P('kale2', 'Zigetvar düştü.', 'ZİGETVAR DÜŞTÜ', w=900),
    ST('artık yaşamayan', 'ZAFER', 'yaşamayan bir padişaha', 140),
], year=1566.69, boom=True)
SC('board', 'Sokullu, gizlice Kütahya’daki', [
    P('selim', 'Şehzade Selim’e', 'ŞEHZADE SELİM', w=860, crop=[.05, .02, .9, .7]),
    DC('haber yolladı', ['GİZLİ MEKTUP', 'SOKULLU’DAN', 'KÜTAHYA’YA'], 'BABAN ÖLDÜ', keyAt='haber yolladı'),
    BD('isyan etmesinden', 'İSYAN KORKUSU', red=True, size=64),
    TH('selim', 'doc1'),
], year=1566.7)
SC('dark', 'Kaynaklara göre sır', [
    CT('42 ile 48', 0, 48, 'v => Math.round(v) + " GÜN"', 230, dur=1.2, sub='42-48 GÜN SAKLANDI'),
    TI('Selim orduya', 'SONRA AÇIKLANDI', 110, color='#f0754e'),
], year=1566.8)
SC('board', 'Bazen en büyük sorumluluk', [
    TI('kimseye söyleyemediğin', 'SÖYLEYEMEDİĞİN\nHABER', 110, x=0, color='#f0754e'),
    P('araba', 'tek başına taşımaktır', 'SON YOLCULUK', w=820),
], year=1566.8)
SC('dark', 'Kanuni’yi son seferinde', [
    HT('kanuni', 'Kanuni’yi son', crop=[.15, .05, .7, .5], w=1000),
    TI('bir sır taşıdı', 'ONU BİR SIR\nTAŞIDI', 150, color='#f0754e', font='cond'),
])
SC('dark', 'Sence Sokullu doğru mu', [
    TI('Sence Sokullu', 'SOKULLU\nDOĞRU MU YAPTI?', 110),
    TI('yanlış mı?', 'DOĞRU MU, YANLIŞ MI?', 100, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
