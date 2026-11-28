# Sokullu Mehmed Paşa'yı kim öldürdü? (sinematik dosya + LTX canlandırma, dikey). Kaynaklar README'de.
# LTX klipleri boş 'dark' sahnelerin üstüne ffmpeg ile bindirilir (build/ltx_bindir.py).
BASLIK = 'Sokullu Mehmed Paşa: 12 Ekim 1579. "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1500, 1590], 15, 1579.78
# ---- KANCA ----
SC('board', 'Sokullu Mehmed Paşa’yı', [
    P('sokullu', 'Sokullu Mehmed Paşa’yı', 'SOKULLU MEHMED PAŞA', w=1000, crop=[.18, .2, .86, .68], shift=-1.2),
    TI('Sokullu Mehmed Paşa’yı', 'BİR DİLEKÇE\nÖLDÜRDÜ', 160, x=0, j=1, shift=-1.2, font='cond'),
], lead=.0, year=1579.78)
SC('board', 'Üç padişaha sadrazamlık', [
    CT('Üç padişaha', 0, 3, 'v => Math.round(v) + " PADİŞAH"', 170, dur=.6, sub='SADRAZAM'),
    P('katil', 'dervişin hançeriyle', 'SOKULLU’NUN KATLİ (GRAVÜR)', w=900, crop=[0, 0, 1, .5]),
    TI('kim gönderdi', 'KİM GÖNDERDİ?', 140, color='#f0754e', font='cond'),
], year=1579.78, boom=True)
SC('board', 'Sokullu, Bosna’da bir köyde', [
    P('visegrad', 'Bosna’da bir köyde', 'VİŞEGRAD, BOSNA', w=860),
    P('devsirme', 'Devşirme olarak', 'DEVŞİRME', w=700),
    TH('visegrad', 'devsirme'),
    CT('on dört yıl', 0, 14, 'v => Math.round(v) + " YIL"', 170, dur=.8, sub='SADRAZAM'),
], year=1520)
SC('dark', 'Kanuni’nin ölümünü Zigetvar’da', [], year=1566.68)   # LTX: zigetvar
SC('board', 'Don ile Volga’yı', [
    P('volga', 'Don ile Volga’yı', 'DON - VOLGA KANALI', w=900),
], year=1569)
SC('board', 'Ama yeni padişah', [
    P('murad3', 'Üçüncü Murad', 'III. MURAD', w=760, crop=[.1, .05, .9, .7]),
    TI('onu sevmiyordu', 'SEVMİYORDU', 150, color='#f0754e', font='cond'),
], year=1574.9, boom=True)
SC('board', 'Sokullu’nun adamları', [
    ST('görevden alındı', 'ADAMLARI', 'görevden alındı', 130),
    P('budin', '1578’de Budin', 'BUDİN · 1578', w=880),
    BD('akrabası idam edildi', 'AKRABASI İDAM EDİLDİ', red=True, size=60),
    TI('yalnız kalıyordu', 'YALNIZ', 180, font='cond'),
], year=1578)
SC('dark', 'Sen olsan, etrafındaki', [
    TI('Sen olsan,', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('görevini bırakır', 'GÖREVİ\nBIRAKIR MIYDIN?', 120),
], boom=True)
SC('dark', '12 Ekim 1579’da', [], year=1579.78)   # LTX: dervis
SC('dark', 'Dilekçeyi uzatır gibi', [], year=1579.78)   # LTX: hancer
SC('board', 'Katil, tımarı azaltılan', [
    P('katil', 'Katil, tımarı', 'KATİL: BİR BOŞNAK', w=900, crop=[0, 0, 1, .5]),
    TG('tımarı azaltılan', 'GÖRÜNÜŞTE', '', 'TIMARI AZALTILMIŞ'),
    TI('burada bitmiyor', 'AMA BİTMİYOR', 130, color='#f0754e', font='cond'),
], year=1579.78)
SC('board', 'Bazı tarihçilere göre arkada', [
    P('dervis', 'Hamzavî tarikatı', 'HAMZAVÎLER?', w=640),
    P('murad3b', 'padişahın kendisi', 'III. MURAD?', w=640),
    TH('dervis', 'murad3b'),
], year=1579.8)
SC('dark', 'Bazen en büyük tehlike', [
    TI('küçük bir ricayla', 'KÜÇÜK BİR\nRİCAYLA GELEN', 140, color='#f0754e', font='cond'),
])
SC('dark', 'Sokullu’yu bir hançer', [], year=1579.8)   # LTX: gravur
SC('dark', 'Sence kim gönderdi?', [
    TI('Sence kim gönderdi?', 'KİM GÖNDERDİ?', 150),
    TI('Hamzavîler mi', 'HAMZAVÎLER Mİ,\nPADİŞAH MI?', 120, color='#f0754e', font='cond'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
