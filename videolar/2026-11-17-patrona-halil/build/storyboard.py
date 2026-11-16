# Patrona Halil ve Lale Devri (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Patrona Halil: padişah indiren tellak. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1715, 1735], 5, 1730.7
# ---- KANCA ----
SC('board', 'Eski bir hamam tellağı', [
    P('patrona', 'Eski bir hamam', 'PATRONA HALİL', w=880, crop=[.1, 0, .8, .7], shift=-1.2),
    TI('Eski bir hamam', 'PADİŞAHI\nTAHTTAN İNDİRDİ', 120, x=0, j=1, shift=-1.2),
    BD('Adı Patrona Halil’di.', 'ESKİ BİR HAMAM TELLAĞI', red=True, size=60),
    TG('İsyanı, koca bir', 'BİR DÖNEM', '1730', 'BİRKAÇ GÜNDE BİTTİ'),
], lead=.0, year=1730.7)
SC('dark', 'Ama asıl şaşırtıcı', [
    TI('Ama asıl şaşırtıcı', 'O DÖNEMİN ADI', 140, color='#f0754e'),
    TI('o döneme verdiğimiz', 'O ZAMAN\nHİÇ YOKTU', 150, lineAt=[0, 'hiç kullanılmamış']),
], glitch=[('Ama asıl', .3, .7)])
# ---- SARAY ----
SC('board', 'Sultan Üçüncü Ahmed', [
    P('ahmed', 'Sultan Üçüncü Ahmed', 'SULTAN III. AHMED', w=760),
    TG('ve damadı', 'DAMAT', '', 'PADİŞAHIN KIZI FATMA SULTAN'),
    P('ibrahim', 'Sadrazam Nevşehirli', 'NEVŞEHİRLİ İBRAHİM PAŞA', w=760),
    TH('ahmed', 'ibrahim'),
], year=1718.5)
SC('board', 'İstanbul’u bahçeler', [
    P('sadabad', 'İstanbul’u bahçeler', 'SADABAD · KÂĞITHANE', w=920),
    P('senlik', 'köşkler ve eğlencelerle', 'ŞENLİKLER · LEVNİ', w=900),
    TH('sadabad', 'senlik'),
    P('lale', 'Bazı lale soğanları', 'LALE', w=760),
    BD('servet değerinde', 'SERVET DEĞERİNDE SOĞANLAR', red=True, size=58),
], year=1722)
# ---- SOKAK ----
SC('dark', 'Ama sarayın dışında', [
    P('pazar', 'Ama sarayın dışında', None, w=1050),
    TI('başka bir İstanbul', 'BAŞKA BİR\nİSTANBUL', 140, color='#f0754e'),
])
SC('board', 'Pahalılık, ağır vergiler', [
    TG('Pahalılık', 'PAHALILIK', '', 'AĞIR VERGİLER'),
    P('tebriz', 'İran cephesinden', 'TEBRİZ · İRAN CEPHESİ', w=920),
    TH('tag1', 'tebriz'),
    ST('Tebriz kaybedilmişti.', 'TEBRİZ', 'Tebriz kaybedilmişti.', 140),
], year=1730.5)
SC('dark', 'Sen o günlerde', [
    TI('Sen o günlerde', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('sarayın eğlencesine', 'EĞLENCEYE Mİ\nKIZARDIN?', 120),
    TI('kaybedilen savaşa', 'SAVAŞA MI?', 140, color='#f0754e'),
], boom=True)
# ---- İSYAN ----
SC('board', '28 Eylül 1730.', [
    TG('28 Eylül', '28 EYLÜL', '1730', 'BAYEZİD'),
    P('isyan2', 'Patrona Halil, bir avuç', 'İSYAN BAYRAĞI', w=820),
    TH('tag1', 'isyan2'),
    BD('İsyancılar tek şey', 'TEK İSTEK:', size=64),
    TI('İbrahim Paşa’nın başını.', 'İBRAHİM PAŞA’NIN\nBAŞI', 110, x=0),
], year=1730.74, boom=True)
SC('dark', 'Padişah, tahtını kurtarmak', [
    P('isyan', 'Padişah, tahtını', None, w=1050),
    TI('kendi damadını boğdurdu', 'KENDİ DAMADINI\nBOĞDURDU', 120, color='#f0754e', lineAt=[0, 'boğdurdu']),
    TI('Yetmedi.', 'YETMEDİ.', 170),
])
SC('board', 'Birkaç gün sonra', [
    P('ahmed', 'Birkaç gün sonra', 'III. AHMED', w=760),
    ST('o da tahttan', 'TAHT', 'tahttan indi.', 150),
    P('patrona2', 'Patrona Halil iki ay', 'İSTANBUL’UN GERÇEK HÂKİMİ', w=820),
    CT('iki ay boyunca', 0, 2, 'v => Math.round(v) + " AY"', 200, dur=.7),
    P('mahmud', 'Sonra yeni padişah', 'SULTAN I. MAHMUD', w=740),
    TH('patrona2', 'mahmud'),
    BD('orada öldürttü.', 'SARAYDA ÖLDÜRÜLDÜ · KASIM 1730', red=True, size=52),
], year=1730.9)
# ---- LALE DEVRİ ADI ----
SC('dark', 'Peki "Lale Devri"', [
    P('lalemin', 'Peki "Lale Devri"', None, w=1050),
    TI('Lale Devri', '“LALE DEVRİ”', 150, color='#f0754e'),
    CT('yaklaşık 180 yıl', 0, 180, 'v => Math.round(v) + " YIL SONRA"', 130, dur=1.0),
    TI('tarihçiler tarafından', 'TARİHÇİLER\nKOYDU', 130),
], year=1913)
SC('dark', 'Bazen bir düzeni', [
    TI('Bazen bir düzeni', 'DÜŞMAN DEĞİL', 150),
    TI('sofradakilerle', 'SOFRA İLE SOKAK\nARASINDAKİ MESAFE', 100, color='#f0754e', lineAt=[0, 'arasındaki mesafedir']),
])
SC('dark', 'Lale bahçeleri', [
    HT('patrona', 'Lale bahçeleri', crop=[.3, .05, .45, .4], w=1000),
    TI('bir tellağın öfkesine', 'BİR TELLAĞIN\nÖFKESİ', 130, color='#f0754e'),
])
SC('dark', 'Sence suçlu israf', [
    TI('Sence suçlu', 'İSRAF MI?', 150),
    TI('savaş mı', 'SAVAŞ MI?', 150, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
