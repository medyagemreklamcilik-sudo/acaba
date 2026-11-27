# Kösem mi, Turhan mı? Sarayda gelin-kaynana savaşı (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Kösem mi, Turhan mı? 1651. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1600, 1690], 15, 1651.67
# ---- KANCA ----
SC('board', 'Kösem Sultan’ı kendi gelini', [
    P('turhan', 'Kösem Sultan’ı', 'TURHAN SULTAN (TEMSİLİ)', w=1000, crop=[.12, .1, .88, .58], shift=-1.2),
    TI('Kösem Sultan’ı', 'KÖSEM’İ GELİNİ Mİ\nBOĞDURDU?', 135, x=0, j=1, shift=-1.2, font='cond'),
    BD('mi boğdurdu', 'TOPKAPI · 1651', red=True, size=60),
], lead=.0, year=1651.67)
SC('board', 'Biri imparatorluğu', [
    P('kosem', 'yarım asır yöneten', 'KÖSEM SULTAN (TEMSİLİ)', w=760),
    P('turhan2', 'genç bir anne', 'TURHAN SULTAN (TEMSİLİ)', w=700),
    TH('kosem', 'turhan2'),
    TI('Kösem mi güçlüydü', 'KÖSEM Mİ,\nTURHAN MI?', 140, x=0, color='#f0754e', font='cond'),
], year=1640)
SC('board', 'Kösem, iki padişahın', [
    P('murad4', 'Dördüncü Murad', 'IV. MURAD', w=700),
    P('ibrahim', 've İbrahim', 'SULTAN İBRAHİM', w=700),
    TH('murad4', 'ibrahim'),
    BD('devleti o yönetti', 'DEVLETİ O YÖNETTİ', red=True, size=60),
], year=1623.7)
SC('board', 'İbrahim tahttan indirilince', [
    CT('altı yaşındaki', 0, 6, 'v => Math.round(v) + " YAŞINDA"', 170, dur=.6, sub='PADİŞAH'),
    P('mehmed4', 'Dördüncü Mehmed geçti', 'IV. MEHMED', w=760),
    TG('büyük valide', 'KÖSEM', '1648', 'BÜYÜK VALİDE'),
], year=1648.6)
SC('board', 'Ama küçük padişahın', [
    P('turhan', 'Turhan Sultan.', 'ANNE: TURHAN', w=760, crop=[.12, .1, .88, .58]),
    ST('kaynanasına bırakmak', 'KAYNANA', 'bırakmak istemiyordu', 130),
], year=1650)
SC('board', 'Saray ikiye bölündü.', [
    P('yeniceri', 'Kösem ve yeniçeri ağaları', 'KÖSEM: YENİÇERİ AĞALARI', w=700),
    P('agasi', 'Turhan ve harem ağaları', 'TURHAN: HAREM AĞALARI', w=700),
    TH('yeniceri', 'agasi'),
], year=1651)
SC('board', 'Anlatılanlara göre Kösem', [
    DC('bir plan yaptı', ['PLAN', 'KÖSEM SULTAN', '1651'], 'PADİŞAH DEĞİŞECEK', keyAt='bir plan yaptı'),
    BD('başka bir şehzadeyi', 'YERİNE BAŞKA ŞEHZADE', red=True, size=56),
], year=1651.6)
SC('dark', 'Sen Turhan olsan', [
    TI('Sen Turhan olsan', 'SEN TURHAN\nOLSAN?', 170, color='#f0754e'),
    TI('oğlunu kurtarmak', 'OĞLUNU NASIL\nKURTARIRDIN?', 115),
], boom=True)
SC('board', 'Plan Turhan’a sızdı.', [
    TG('2 Eylül 1651', 'GECE', '1651', '2 EYLÜL'),
    P('harem', 'harem ağası', 'TOPKAPI HAREMİ', w=900),
    BD('dairesine girdi', 'SÜLEYMAN AĞA VE ADAMLARI', red=True, size=56),
], year=1651.67, boom=True)
SC('dark', 'Anlatılanlara göre Kösem bir dolaba', [
    P('olum', 'bir dolaba saklandı', 'KÖSEMİN ÖLÜMÜ · TEMSİLİ', w=1000),
    TI('perde kordonuyla', 'PERDE KORDONU', 120, color='#f0754e', font='cond'),
    CT('Altmış yaşını', 0, 60, 'v => Math.round(v) + "+ YAŞINDA"', 150, dur=.8),
], year=1651.67, boom=True, glitch=[('boğuldu', .3, .7)])
SC('board', 'Turhan o geceden sonra', [
    CT('otuz yıl', 0, 30, 'v => Math.round(v) + " YIL"', 170, dur=.9, sub='EN GÜÇLÜ KADIN'),
    P('koprulu', 'Köprülü Mehmed Paşa’yı', 'KÖPRÜLÜ MEHMED PAŞA · 1656', w=700),
    P('yenicami', 'Yeni Cami’yi', 'YENİ CAMİ · 1665', w=760),
    TH('koprulu', 'yenicami'),
], year=1656)
SC('dark', 'Gelin ile kaynana', [
    TI('her evde olur', 'HER EVDE\nOLUR', 140),
    TI('bir imparatorluk aldı', 'KAZANAN\nİMPARATORLUK ALDI', 115, color='#f0754e', font='cond'),
])
SC('dark', 'Kösem yarım asır', [
    HT('turhan', 'Kösem yarım asır', crop=[.12, .1, .88, .55], w=1000),
    TI('son geceyi kazanan', 'SON GECEYİ\nTURHAN KAZANDI', 120, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Sence hangisi güçlüydü?', [
    TI('Sence hangisi', 'KÖSEM Mİ,\nTURHAN MI?', 150),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
