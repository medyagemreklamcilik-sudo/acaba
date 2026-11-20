# Yıldırım Ankara Savaşı'nı kazansaydı? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Yıldırım Bayezid ve Timur: Ankara 1402. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1390, 1460], 10, 1402.57
# ---- KANCA ----
SC('board', 'Yıldırım Bayezid o savaşı', [
    P('bayezid', 'Yıldırım Bayezid', 'YILDIRIM BAYEZİD', w=1000, crop=[.05, .05, .9, .7], shift=-1.2),
    TI('Yıldırım Bayezid', 'KAZANSAYDI?', 180, x=0, j=1, shift=-1.2, font='cond'),
    BD('İstanbul elli yıl', 'İSTANBUL 50 YIL ERKEN DÜŞERDİ', red=True, size=52, shift=-1.2),
], lead=.0, year=1402.57)
SC('board', 'Bayezid, İstanbul’u yıllardır', [
    P('istanbul', 'İstanbul’u yıllardır', 'KUŞATILAN KONSTANTİNOPOLİS', w=960),
    P('manuel', 'Şehir teslim olmanın', 'İMPARATOR MANUEL II', w=560),
    TH('istanbul', 'manuel'),
    BD('teslim olmanın eşiğindeydi', 'TESLİMİN EŞİĞİNDE', red=True, size=60),
], year=1400)
SC('dark', 'Ama doğudan biri geldi', [
    P('timur', 'Ama doğudan', None, w=780),
    TI('Timur.', 'TİMUR', 200, color='#f0754e', font='cond'),
], year=1402, boom=True)
# ---- SAVAŞ ----
SC('board', '28 Temmuz 1402.', [
    TG('28 Temmuz', 'ANKARA', '1402', 'ÇUBUK OVASI'),
    P('ova', 'Çubuk Ovası', 'ÇUBUK OVASI', w=920),
    TH('tag1', 'ova'),
    P('savas', 'İki dev ordu', 'ANKARA SAVAŞI', w=800),
], year=1402.57)
SC('board', 'Savaşın ortasında', [
    P('tatar', 'Bayezid’in saflarındaki', 'TATAR SÜVARİLERİ', w=760),
    ST('taraf değiştirdi', 'SADAKAT', 'taraf değiştirdi.', 140),
    TG('Çünkü eski beyleri', 'ESKİ BEYLER', '', 'TİMUR’UN YANINDA'),
    TH('tatar', 'tag1'),
], year=1402.57, boom=True)
SC('board', 'Bayezid yanında kalan', [
    P('yeniceri', 'yeniçerilerle akşama', 'SON YENİÇERİLER', w=820),
    TI('Sonunda esir düştü.', 'ESİR DÜŞTÜ', 160, x=0, font='cond'),
], year=1402.57)
SC('dark', 'Sen Bayezid olsan', [
    TI('Sen Bayezid olsan', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('affeder miydin', 'AFFEDER\nMİYDİN?', 150),
], boom=True)
# ---- ESARET ----
SC('board', 'Anlatılanlara göre Timur', [
    P('kafes', 'demir bir kafeste', 'DEMİR KAFES?', w=900),
    BD('büyük ihtimalle efsane', 'BÜYÜK İHTİMALLE EFSANE', size=56),
    TG('Akşehir’de', 'AKŞEHİR', '1403', 'ESARETTE ÖLDÜ'),
    TH('kafes', 'tag1'),
], year=1403.2)
SC('dark', 'Osmanlı neredeyse dağıldı.', [
    TI('neredeyse dağıldı', 'OSMANLI DAĞILDI', 120, color='#f0754e'),
    CT('on bir yıl', 0, 11, 'v => Math.round(v) + " YIL"', 200, dur=.8, sub='KARDEŞ SAVAŞI'),
], year=1410)
# ---- YA OLSAYDI ----
SC('dark', 'Peki Yıldırım kazansaydı?', [
    TI('Peki Yıldırım', 'YA KAZANSAYDI?', 150, color='#f0754e', font='cond'),
])
SC('board', 'Bazı tarihçilere göre İstanbul', [
    P('istanbul2', 'İstanbul 1453’ü', 'İSTANBUL', w=760),
    ST('1453’ü beklemeden', '1453', 'beklemeden düşerdi.', 170),
    BD('Kuşatılan şehri kurtaran', 'ŞEHRİ TİMUR KURTARDI', red=True, size=60),
    P('fatih', 'Belki "Fatih"', '“FATİH” KİM OLURDU?', w=560),
], year=1453)
SC('board', 'Bazı tarihçilere göre bu yenilgi', [
    P('hisar', 'devleti Balkanlara', 'YENİDEN KURULUŞ', w=920),
    TI('daha sağlam kuruldu', 'DAHA SAĞLAM?', 130, x=0, color='#f0754e'),
], year=1413)
# ---- KAPANIŞ ----
SC('dark', 'Bazen en büyük yenilgi', [
    TI('Bazen en büyük', 'EN BÜYÜK YENİLGİ', 130),
    TI('saf değiştirmesinden', 'YANINDAKİNİN\nSAF DEĞİŞTİRMESİ', 110, color='#f0754e', lineAt=[0, 'saf değiştirmesinden']),
])
SC('dark', 'Yıldırım’ı Timur değil', [
    HT('bayezid', 'Yıldırım’ı Timur', crop=[.15, .25, .75, .5], w=1000),
    TI('kendi saflarındaki ihanet', 'İHANET YENDİ', 150, color='#f0754e'),
])
SC('dark', 'Sence Yıldırım kazansaydı', [
    TI('İstanbul elli yıl önce', 'İSTANBUL 50 YIL\nÖNCE DÜŞER MİYDİ?', 100),
    TI('Evet mi', 'EVET Mİ, HAYIR MI?', 110, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
