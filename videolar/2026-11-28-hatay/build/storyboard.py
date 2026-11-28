# Hatay Türkiye'ye nasıl katıldı? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Hatay 1921-1939: belgeler. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1920, 1940], 5, 1938.86
SC('board', 'Atatürk, Hatay’ı neden', [
    P('ataturk', 'Atatürk, Hatay’ı', 'MUSTAFA KEMAL ATATÜRK', w=1000, crop=[.05, .02, .95, .55], shift=-1.2),
    TI('Atatürk, Hatay’ı', 'HATAY’I\nNEDEN GÖREMEDİ?', 150, x=0, j=1, shift=-1.2, font='cond'),
], lead=.0, year=1938.86)
SC('dark', 'Peki Hatay nasıl', [
    TI('Hatay nasıl bizim', 'HATAY NASIL\nBİZİM OLDU?', 140),
    TI('Tek kurşun atılmadan', 'TEK KURŞUN\nATILMADAN', 150, color='#f0754e', font='cond'),
], boom=True)
SC('board', '1921’de imzalanan Ankara', [
    DC('Ankara Antlaşması’yla', ['ANKARA ANTLAŞMASI', 'TÜRKİYE - FRANSA', '20 EKİM 1921'], 'SURİYE’DE KALDI', keyAt='Fransız yönetimindeki'),
    P('antakya', 'İskenderun ve Antakya', 'ANTAKYA', w=760),
    BD('Türkçe resmi dil', 'TÜRKÇE RESMİ DİL · ÖZEL STATÜ', red=True, size=52),
], year=1921.8)
SC('board', '1936’da Fransa', [
    P('iskenderun', 'Suriye’ye bağımsızlık', 'İSKENDERUN', w=900),
    TI('Suriye’yle birlikte', 'SURİYE’YE\nGİDECEKTİ', 140, color='#f0754e', font='cond'),
], year=1936.7, boom=True)
SC('board', 'Atatürk bunu kabul etmedi.', [
    P('ataturk2', 'Atatürk bunu', 'ATATÜRK · 1937', w=760),
    DC('Anlatılanlara göre', ['SÖZ', 'ATATÜRK', '1936-37'], 'ŞAHSİ MESELEM', keyAt='benim şahsi meselemdir'),
], year=1936.9)
SC('board', 'Mesele Milletler Cemiyeti’ne', [
    P('milletler', 'Milletler Cemiyeti’ne', 'MİLLETLER CEMİYETİ · CENEVRE', w=900),
    TG('1937’de Hatay’a', 'STATÜ', '1937', 'AYRI YÖNETİM'),
], year=1937.4)
SC('dark', 'Sen olsan, hasta', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('savaşı göze alır', 'SAVAŞI GÖZE\nALIR MIYDIN?', 120),
], boom=True)
SC('board', 'Atatürk o günlerde ağır', [
    P('mersin', 'güneye gitti', 'ATATÜRK, MERSİN · 1938', w=900),
    BD('askerleri denetledi', 'MERSİN · ADANA · ASKER', red=True, size=58),
    TI('Mesaj açıktı.', 'MESAJ AÇIK', 150, font='cond'),
], year=1938.4)
SC('board', '2 Eylül 1938’de Hatay', [
    P('hatay_devlet', 'Hatay Devleti kuruldu', 'HATAY DEVLETİ', w=820, crop=[0, 0, 1, .6]),
    P('pul', 'kendi bayrağı', 'HATAY DEVLETİ PULU', w=600),
    TH('hatay_devlet', 'pul'),
], year=1938.67)
SC('dark', 'Ama Atatürk iki ay sonra', [
    HT('ataturk', 'Ama Atatürk', crop=[.05, .02, .95, .5], w=1000),
    TI('10 Kasım 1938’de', '10 KASIM 1938', 150, color='#f0754e', font='cond'),
], year=1938.86, boom=True)
SC('board', '29 Haziran 1939’da Hatay', [
    P('meclis', 'Hatay Meclisi', 'HATAY MECLİSİ · 1939', w=880),
    P('ulus', 'katılma kararı', '“HATAY DEVLETİ TARİHE KARIŞTI”', w=760, crop=[0, 0, 1, .6]),
    TH('meclis', 'ulus'),
    BD('Fransız askerleri çekildi', 'FRANSIZLAR ÇEKİLDİ · TEMMUZ 1939', red=True, size=50),
], year=1939.5)
SC('dark', 'Bazen en çok istediğin', [
    TI('göremezsin', 'GÖREMEZSİN', 150),
    TI('onu başlatan sen', 'AMA SEN\nBAŞLATIRSIN', 130, color='#f0754e', font='cond'),
])
SC('board', 'Hatay’ı bir kurşun değil', [
    P('yasa', 'Hatay’ı bir kurşun', '“YAŞA VAROL ATATÜRK”', w=900),
    ST('bir kurşun değil', 'KURŞUN', 'bir kurşun değil', 140),
    TI('bir inat kazandı', 'BİR İNAT', 170, color='#f0754e', font='cond'),
], year=1939.5, boom=True)
SC('dark', 'Sence Hatay’ı kim', [
    TI('Sence Hatay’ı', 'KİM KAZANDI?', 150),
    TI('Atatürk mü, diplomasi mi?', 'ATATÜRK MÜ,\nDİPLOMASİ Mİ?', 120, color='#f0754e', font='cond'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
