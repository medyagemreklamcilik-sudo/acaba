# Osmanlı matbaayı neden geç aldı? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Osmanlı ve matbaa: 270 yıllık gecikme. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1450, 1750], 50, 1455
# ---- KANCA ----
SC('board', 'Avrupa kitap basarken', [
    P('bayezid', 'Avrupa kitap basarken', 'II. BAYEZİD', w=1000, crop=[.1, .08, .85, .62], shift=-1.2),
    TI('Avrupa kitap basarken', 'MATBAAYI\nYASAKLADI MI?', 160, x=0, j=1, shift=-1.2, font='cond'),
    BD('270 yıl bekledi', '270 YIL GECİKME', red=True, size=62),
], lead=.0, year=1455)
SC('board', 'Bir padişah mı', [
    P('gutenberg', 'Bir padişah mı', 'GUTENBERG MATBAASI', w=820, crop=[0, 0, 1, .9]),
    TI('yasakladı?', 'SUÇLU PADİŞAH MI?', 120, x=0, color='#f0754e', font='cond'),
], year=1455)
SC('board', 'Sana anlatılan hikâye', [
    DC('İkinci Bayezid bir fermanla', ['FERMAN', 'II. BAYEZİD', '1485 (?)'], 'MATBAA YASAK', keyAt='matbaayı yasakladı'),
    BD('İddiaya göre cezası ölümdü', 'CEZASI: ÖLÜM (İDDİA)', red=True, size=60),
], year=1485)
SC('dark', 'Ama o fermanı', [
    TI('Ama o fermanı', 'O FERMAN', 150),
    TI('kimse bulamadı', 'HİÇ BULUNAMADI', 140, color='#f0754e', font='cond'),
], boom=True)
SC('board', 'İddia, 1584’te', [
    P('thevet', 'bir Fransız rahibin', 'ANDRÉ THEVET, 1584', w=820, crop=[.05, .02, .9, .72]),
    ST('Osmanlı arşivinde', 'ARŞİVDE BELGE', 'böyle bir belge yok', 120),
], year=1584)
# ---- MATBAA ZATEN VARDI ----
SC('board', 'Üstelik İstanbul’da matbaa', [
    TG('matbaa zaten vardı', 'İSTANBUL', '1493', 'MATBAA ZATEN VAR'),
    P('ibrani', 'Yahudiler 1493’te', 'İBRANİCE BASKI, 1493', w=760),
    P('ermeni', 'Ermeniler 1567’de', 'ERMENİCE BASKI, 1567', w=760),
    TH('ibrani', 'ermeni'),
], year=1493)
SC('board', 'Basmayan Müslümanlardı.', [
    BD('Basmayan Müslümanlardı.', 'BASMAYAN: MÜSLÜMANLAR', red=True, size=62),
    P('harfler', 'Arap harfleri', 'BİTİŞİK HARFLER', w=820),
    P('hat2', 'Hattatlar ise', 'HAT SANATI', w=860),
    TH('harfler', 'hat2'),
], year=1600)
SC('dark', 'Sen olsan, ekmeğini', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('işsiz bırakır mıydın', 'HATTATLARI\nİŞSİZ BIRAKIR\nMIYDIN?', 120),
], boom=True)
# ---- MÜTEFERRİKA ----
SC('board', '1727’de Müslüman olmuş', [
    TG('Müslüman olmuş bir Macar', 'KOLOJVAR', '1727', 'MACAR ASILLI'),
    P('muteferrika', 'İbrahim Müteferrika', 'İBRAHİM MÜTEFERRİKA (BÜST)', w=760, crop=[0, 0, 1, .6]),
    BD('ilk Türk matbaasını', 'İLK TÜRK MATBAASI', red=True, size=62),
], year=1727)
SC('board', 'Şeyhülislam fetva verdi', [
    DC('fetva verdi', ['FETVA', 'ŞEYHÜLİSLAM', 'YENİŞEHİRLİ ABDULLAH'], 'İZİN VERİLDİ', keyAt='fetva verdi'),
    BD('dinî kitaplar basılmayacaktı', 'DİNÎ KİTAP YOK', red=True, size=66),
], year=1727)
SC('board', 'Müteferrika ölene kadar', [
    CT('17 kitap', 0, 17, 'v => Math.round(v) + " KİTAP"', 220, dur=1.0, sub='1729-1747'),
    P('harita', 'Bazıları yıllarca', 'MÜTEFERRİKA BASKISI', w=900),
], year=1747)
SC('board', 'Bugün de öyle değil mi?', [
    P('vankulu', 'Yeni bir şey', 'VANKULU LÜGATI, 1729', w=820),
    TI('buna gerek yok', '“BUNA\nGEREK YOK”', 140, x=0, font='cond'),
], year=1747)
SC('dark', 'Osmanlı’yı geciktiren', [
    HT('bayezid', 'Osmanlı’yı geciktiren', crop=[.1, .08, .8, .55], w=1000),
    ST('bir yasak değildi', 'YASAK', 'bir yasak değildi', 160),
    TI('bir alışkanlıktı', 'BİR ALIŞKANLIK', 140, color='#f0754e', font='cond'),
], boom=True)
SC('dark', 'Sence suçlu kim?', [
    TI('Sence suçlu kim?', 'SUÇLU KİM?', 160),
    TI('Hattatlar mı', 'HATTATLAR MI,\nULEMA MI?', 110, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
