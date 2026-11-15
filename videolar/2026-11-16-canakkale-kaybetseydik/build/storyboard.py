# Çanakkale geçilseydi ne olurdu? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Çanakkale geçilseydi? Mustafa Kemal ve gizli pazarlık. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1914, 1918], 1, 1915.2
# ---- KANCA ----
SC('board', 'Çanakkale geçilseydi ne olurdu?', [
    P('mk', 'Çanakkale geçilseydi', 'MUSTAFA KEMAL · 1915', w=880, crop=[.25, 0, .55, .42], shift=-1.2),
    TI('Çanakkale geçilseydi', 'ÇANAKKALE\nGEÇİLSEYDİ?', 140, x=0, j=1, shift=-1.2),
    BD('İstanbul haftalar', 'İSTANBUL HAFTALAR İÇİNDE DÜŞERDİ', red=True, size=52),
    TG('Ve bugün herkesin', 'O İSİM', '?', 'HİÇ DUYULMAZDI'),
], lead=.0, year=1915.2)
SC('dark', 'Ama asıl şok edici', [
    TI('Ama asıl şok', 'ASIL ŞOK', 170, color='#f0754e'),
    TI('İstanbul’un çoktan', 'İSTANBUL ÇOKTAN\nSÖZ VERİLMİŞTİ', 120, lineAt=[0, 'söz verilmiş']),
], glitch=[('Ama asıl', .3, .7)])
# ---- DONANMA ----
SC('board', 'İngiliz ve Fransız donanması', [
    P('filo', 'İngiliz ve Fransız', 'İTİLAF DONANMASI', w=900),
    P('zirhli', 'dünyanın en güçlü', 'DÜNYANIN EN GÜÇLÜ ZIRHLILARI', w=880),
    TH('filo', 'zirhli'),
], year=1915.1)
SC('map', 'Hedef: İstanbul.', [
    RT('Hedef', [[25.7, 39.85], 'canakkale', 'istanbul'], 1.4),
    GD('İstanbul.', 'istanbul', 'İSTANBUL', square=True),
], cam=[(-.4, 'canakkale', .2), ('İstanbul.', 'istanbul', .3)])
# ---- GİZLİ PAZARLIK ----
SC('board', 'Ama gizli bir pazarlık', [
    DC('Ama gizli bir', ['GİZLİ ANLAŞMA', 'İSTANBUL', 'MART-NİSAN 1915'], 'İSTANBUL VE BOĞAZLAR RUSYA’YA', keyAt='Rusya’ya vermeyi', h=1050,
       stamp=dict(text='GİZLİ', t='Aynı aylarda', x=.1, y=.3, rot=-.1)),
    P('nikola', 'Aynı aylarda', 'ÇAR II. NİKOLA', w=760),
    TH('doc1', 'nikola'),
    P('churchill', 'savaş kazanılırsa', 'CHURCHILL · İNGİLİZ BAHRİYE NAZIRI', w=760),
], year=1915.2)
SC('dark', 'Yani Çanakkale düşseydi', [
    P('istanbul', 'Yani Çanakkale', None, w=1050),
    TI('İstanbul bir Rus', 'İSTANBUL:\nBİR RUS ŞEHRİ?', 130, color='#f0754e', lineAt=[0, 'Rus şehri']),
])
SC('dark', 'Sen o gün siperde', [
    TI('Sen o gün', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('geri çekilir miydin?', 'GERİ ÇEKİLİR\nMİYDİN?', 130),
], boom=True)
# ---- HESAP ----
SC('board', 'Karşı tarafın hesabı', [
    TG('Karşı tarafın hesabı', 'HESAP', '1', 'BOĞAZ AÇILIRSA'),
    P('rusasker', 'Rusya’ya silah', 'RUS ORDUSUNA SİLAH + BUĞDAY', w=800),
    TH('tag1', 'rusasker'),
    BD('Rus Devrimi’ni geciktirir', 'RUS DEVRİMİ GECİKİR?', size=64),
    CT('savaşı iki yıl', 0, 2, 'v => Math.round(v) + " YIL KISA SAVAŞ?"', 120, dur=.8),
], year=1915.3)
# ---- GERÇEK ----
SC('dark', 'Peki gerçekte ne oldu?', [
    TI('Peki gerçekte', 'GERÇEKTE\nNE OLDU?', 160),
])
SC('board', '18 Mart 1915’te', [
    TG('18 Mart', '18 MART', '1915', 'BOĞAZ HAREKÂTI'),
    P('nusret', 'Nusret adında', 'NUSRET MAYIN GEMİSİ', w=900),
    TH('tag1', 'nusret'),
    P('bouvet', 'üç büyük zırhlıyı', 'BOUVET BATIYOR', w=900),
    CT('üç büyük', 0, 3, 'v => Math.round(v) + " ZIRHLI BATTI"', 120, dur=.6),
], year=1915.21, boom=True)
SC('board', 'Sonra kara savaşı', [
    P('anzac', 'Sonra kara', 'KARA SAVAŞI · NİSAN 1915', w=900),
    P('mksiper', 'Ve Conkbayırı’nda', 'CONKBAYIRI', w=860),
    TH('anzac', 'mksiper'),
    P('mkanafarta', 'Anafartalar’da', 'ANAFARTALAR GRUP KOMUTANI', w=900),
    TI('Mustafa Kemal.', 'MUSTAFA KEMAL', 120, x=0),
], year=1915.6)
SC('dark', 'Sekiz ay sürdü.', [
    P('siper', 'Sekiz ay', None, w=1050),
    CT('Sekiz ay', 0, 8, 'v => Math.round(v) + " AY"', 220, dur=.7),
    TI('İki tarafta', 'YARIM MİLYONDAN\nFAZLA KAYIP', 110, color='#f0754e'),
], year=1916.0)
# ---- KAPANIŞ ----
SC('dark', 'Bazen bir hayatı', [
    TI('Bazen bir hayatı', 'KÜÇÜK BİR AN', 150),
    P('mayin', 'Herkes dev gemilere', None, w=1000),
    TI('sonucu bir gece', 'SONUCU BİR GECE\nDÖKÜLEN MAYINLAR\nBELİRLEDİ', 100, color='#f0754e', lineAt=[0, 'dökülen mayınlar', 'belirledi.']),
])
SC('dark', 'Çanakkale bir savaşı', [
    P('mksiper', 'Çanakkale bir savaşı', None, w=1000, crop=[0, 0, .8, .62]),
    TI('bir milletin kaderini', 'BİR MİLLETİN\nKADERİNİ DEĞİŞTİRDİ', 110, color='#f0754e'),
])
SC('dark', 'Sence Çanakkale geçilseydi', [
    TI('Sence Çanakkale', 'GEÇİLSEYDİ\nTÜRKİYE OLUR MUYDU?', 100),
    TI('Evet mi', 'EVET Mİ, HAYIR MI?', 110, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
