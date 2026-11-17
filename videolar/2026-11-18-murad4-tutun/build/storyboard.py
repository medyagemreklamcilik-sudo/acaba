# IV. Murad'ın tütün yasağı (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'IV. Murad: tütün yasağı ve içki. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1620, 1645], 5, 1633.7
# ---- KANCA ----
SC('board', 'Tütün içeni idam ettiren', [
    P('murad', 'Tütün içeni', 'SULTAN IV. MURAD', w=860, crop=[0, 0, 1, .62], shift=-1.2),
    TI('Tütün içeni', 'TÜTÜN İÇENİ\nİDAM ETTİRDİ', 120, x=0, j=1, shift=-1.2),
    BD('kendisi içkiden öldü', 'KENDİSİ İÇKİDEN ÖLDÜ', red=True, size=64),
    TG('Onun döneminde', 'BİR NEFES', 'TÜTÜN', 'BİR CAN'),
], lead=.0, year=1633.7)
SC('dark', 'Ama bu yasağı başlatan', [
    TI('Ama bu yasağı', 'YASAĞI BAŞLATAN', 120),
    TI('bir yangındı', 'BİR YANGIN', 180, color='#f0754e'),
], glitch=[('bir yangındı', .2, .6)])
# ---- YANGIN ----
SC('board', '1633’te İstanbul’da', [
    TG('1633’te', 'CİBALİ', '1633', 'BÜYÜK YANGIN'),
    P('yangin', 'büyük bir yangın', 'İSTANBUL YANIYOR', w=920),
    TH('tag1', 'yangin'),
    BD('Binlerce ev', 'BİNLERCE EV KÜL OLDU', red=True, size=62),
], year=1633.67, boom=True)
SC('board', 'Saray, kahvehaneleri', [
    P('kahvehane', 'kahvehaneleri ve tütün', 'KAHVEHANE', w=920),
    P('tiryaki', 'tütün içilen meclisleri', 'TÜTÜN MECLİSİ', w=820),
    TH('kahvehane', 'tiryaki'),
    BD('isyan fısıldandığı', 'İSYAN FISILTISI', red=True, size=70),
], year=1633.7)
SC('board', 'Murad önce kahvehaneleri', [
    P('murad2', 'Murad önce', 'IV. MURAD', w=760),
    ST('kapattı', 'KAHVEHANE', 'kapattı.', 130),
    DC('Sonra tütünü ve içkiyi', ['FERMAN', 'İSTANBUL', '1633'], 'TÜTÜN + İÇKİ YASAK', keyAt='yasakladı', h=950,
       stamp=dict(text='YASAK', t='yasakladı', x=.1, y=.3, rot=-.1)),
    TH('murad2', 'doc1'),
], year=1633.75)
# ---- GECE ----
SC('dark', 'Rivayete göre geceleri', [
    P('gece', 'Rivayete göre', None, w=1000),
    TI('kılık değiştirip', 'KILIK DEĞİŞTİRİP\nSOKAKTA', 120, color='#f0754e'),
    TI('orada cezalandırıyordu', 'ORADA CEZA', 140),
])
SC('board', 'Bazı kaynaklara göre bu yasak', [
    TG('Bazı kaynaklara göre', 'BAZI KAYNAKLARA GÖRE', 'BİNLERCE', 'ÖLÜ?'),
    P('muradmin', 'Seferde bile', 'SEFERDE BİLE', w=820),
    TH('tag1', 'muradmin'),
    BD('askerler idam edildi', 'TÜTÜN İÇEN ASKER: İDAM', red=True, size=60),
], year=1635)
SC('dark', 'Sen o günlerde', [
    TI('Sen o günlerde', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('bir nefes tütün için', 'BİR NEFES İÇİN\nCANINI RİSKE\nATAR MIYDIN?', 110, lineAt=[0, 'canını riske', 'atar mıydın']),
], boom=True)
# ---- DİRENİŞ ----
SC('board', 'Ama insanlar vazgeçmedi.', [
    P('tiryaki2', 'Ama insanlar', 'VAZGEÇMEDİLER', w=880),
    P('katip', 'Dönemin büyük âlimi', 'KÂTİP ÇELEBİ (TEMSİLİ)', w=740, crop=[0, 0, 1, .7]),
    TH('tiryaki2', 'katip'),
    DC('yasakların insanları', ['KÂTİP ÇELEBİ', 'MÎZÂNÜ’L-HAK', 'TÜTÜN BAHSİ'], 'YASAK VAZGEÇİRMEDİ', keyAt='vazgeçiremediğini', h=900),
], year=1637)
# ---- İRONİ ----
SC('dark', 'Ve en ironik kısım', [
    TI('Ve en ironik', 'EN İRONİK KISIM', 130, color='#f0754e'),
    HT('murad', 'Murad’ın kendisi', crop=[.2, .05, .6, .4], w=1000),
])
SC('board', 'Anlatılanlara göre genç padişahı', [
    TG('Anlatılanlara göre', 'RİVAYET', 'BEKRİ', 'MUSTAFA'),
    P('muradmin2', 'genç padişahı içkiyle', 'GENÇ PADİŞAH', w=820),
    TH('tag1', 'muradmin2'),
    TI('kendi yasakladığı', 'KENDİ YASAĞINA\nDÜŞTÜ', 120, x=0),
], year=1638)
SC('dark', '1640’ta, daha yirmi', [
    P('murad', '1640’ta', None, w=900, crop=[0, 0, 1, .62]),
    CT('yirmi yedi', 0, 27, 'v => Math.round(v) + " YAŞINDA"', 160, dur=.8),
    TI('Ölümünde içkinin', 'İÇKİNİN PAYI?', 120, color='#f0754e'),
], year=1640.1)
# ---- KAPANIŞ ----
SC('dark', 'Bazen insan, başkalarında', [
    TI('Bazen insan', 'EN ÇOK CEZALANDIRDIĞIN ŞEY', 80),
    TI('kendinde olduğunu', 'KENDİNDEDİR', 160, color='#f0754e'),
])
SC('dark', 'Murad tütünü yasakladı.', [
    P('cubuk', 'Murad tütünü', None, w=1000),
    TI('Ama tütün', 'TÜTÜN,\nMURAD’DAN\nUZUN YAŞADI', 120, color='#f0754e', lineAt=[0, 'Murad’dan', 'uzun yaşadı']),
])
SC('dark', 'Sence bu yasak', [
    TI('bir gereklilik', 'GEREKLİLİK Mİ?', 130),
    TI('yoksa zulüm', 'ZULÜM MÜ?', 160, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
