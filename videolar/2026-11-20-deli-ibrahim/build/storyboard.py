# Deli İbrahim gerçekten deli miydi? (sinematik dosya, dikey). Kaynaklar README'de.
BASLIK = 'Sultan İbrahim: deli mi, kafesin kurbanı mı? "dosya" stili'
TL_YEARS, TL_EVERY, TL_START = [1610, 1650], 10, 1640.1
# ---- KANCA ----
SC('board', 'Padişah olduğunu söylediler.', [
    P('ibrahim', 'Padişah olduğunu', 'SULTAN İBRAHİM', w=1000, crop=[.12, .1, .76, .62], shift=-1.2),
    TI('Padişah olduğunu', 'KAPIYI AÇMADI', 170, x=0, j=1, shift=-1.2, font='cond'),
    BD('O ise kapıyı', 'PADİŞAH OLDUN DEDİLER', red=True, size=58, shift=-1.2),
], lead=.0, year=1640.1)
SC('dark', 'Çünkü yıllardır o kapının', [
    P('kapi', 'Çünkü yıllardır', None, w=1000),
    TI('öldürülmeyi bekliyordu', 'ÖLÜMÜ BEKLİYORDU', 110, color='#f0754e'),
], year=1630)
SC('board', 'Adı Sultan İbrahim’di.', [
    P('ibrahimmin', 'Adı Sultan', 'SULTAN İBRAHİM', w=880),
    TI('Deli İbrahim', '“DELİ İBRAHİM”', 140, x=0, font='cond'),
    TG('Ama gerçekten', 'GERÇEKTEN', 'DELİ', 'MİYDİ?'),
], year=1640.1)
# ---- KAFES ----
SC('board', 'İbrahim gençliğini Kafes', [
    P('kafes', 'İbrahim gençliğini', 'KAFES · TOPKAPI', w=920),
    BD('Şehzadelerin kilitli', 'ŞEHZADELER KİLİT ALTINDA', red=True, size=56),
    P('murad', 'Ağabeyi Dördüncü Murad', 'AĞABEYİ IV. MURAD', w=760),
    TH('kafes', 'murad'),
    TG('kardeşlerini birer birer', 'KARDEŞLER', '3', 'ÖLDÜRÜLDÜ'),
], year=1635)
SC('dark', 'Her kapı açıldığında', [
    P('harem', 'Her kapı', None, w=900),
    TI('sıranın kendisine', 'SIRA BENDE Mİ?', 130, color='#f0754e'),
], year=1638)
SC('board', 'Anlatılanlara göre Murad', [
    DC('Anlatılanlara göre', ['RİVAYET', 'TOPKAPI', '1640'], 'İBRAHİM DE ÖLDÜRÜLSÜN', keyAt='öldürülmesini emretti', h=950,
       stamp=dict(text='EMİR', t='öldürülmesini emretti', x=.1, y=.3, rot=-.1)),
    P('kosem', 'Onu annesi Kösem', 'KÖSEM SULTAN (TEMSİLİ)', w=760),
    TH('doc1', 'kosem'),
], year=1640.1)
# ---- TAHT ----
SC('board', '1640’ta Murad öldü.', [
    TG('1640’ta', 'MURAD', '1640', 'ÖLDÜ'),
    P('ibrahim3', 'Görevliler kapıya', '“PADİŞAH OLDUNUZ”', w=800),
    TH('tag1', 'ibrahim3'),
    BD('bir tuzak olduğunu', 'TUZAK SANDI', red=True, size=74),
    TI('cesedini görünce', 'CESEDİ GÖRÜNCE\nAÇTI', 110, x=0, font='cond'),
], year=1640.1, boom=True)
SC('dark', 'Sen yıllarca ölümü', [
    TI('Sen yıllarca', 'SEN OLSAN?', 200, color='#f0754e'),
    TI('normal kalabilir', 'NORMAL\nKALABİLİR MİYDİN?', 120, lineAt=[0, 'kalabilir miydin']),
], boom=True)
# ---- TUHAFLIKLAR ----
SC('board', 'Tahttaki yılları tuhaflıklarla', [
    P('kaftan', 'Samur kürke', 'SAMUR KÜRK', w=760),
    TG('amber kokusuna', 'AMBER', 'SAMUR', 'SERVET'),
    TH('kaftan', 'tag1'),
    DC('Bazı tarihçilere göre', ['BAZI TARİHÇİLERE GÖRE', 'BAŞ AĞRILARI', 'SİNİR KRİZLERİ'], 'HASTA MIYDI?', keyAt='sinir krizleri', h=900),
], year=1645)
# ---- SON ----
SC('board', '1648’de yeniçeriler', [
    P('yeniceri', '1648’de yeniçeriler', 'YENİÇERİ VE ULEMA AYAKLANDI', w=900),
    P('kosem', 'Annesi Kösem Sultan bile', 'KÖSEM: RAZI OLDU', w=700),
    TH('yeniceri', 'kosem'),
    BD('tahttan indirilmesine', 'OĞLUNUN TAHTTAN İNMESİNE RAZI', red=True, size=48),
], year=1648.6)
SC('dark', 'Fetva verildi.', [
    TI('Fetva verildi', 'FETVA', 200, color='#f0754e', font='cond'),
    CT('otuz iki yaşında', 0, 32, 'v => Math.round(v) + " YAŞINDA"', 160, dur=.8),
    TI('boğduruldu', 'BOĞDURULDU', 140),
], year=1648.63, boom=True)
# ---- KAPANIŞ ----
SC('dark', 'Bazen bir insanı deli', [
    TI('Bazen bir insanı', 'DELİ YAPAN', 140),
    TI('büyüdüğü kafestir', 'BÜYÜDÜĞÜ KAFESTİR', 110, color='#f0754e'),
])
SC('dark', 'Tarih onu "deli"', [
    HT('ibrahim', 'Tarih onu', crop=[.2, .15, .6, .45], w=1000),
    TI('hayatta kalmaya', 'HAYATTA KALMAYA\nÇALIŞAN BİR ÇOCUK', 100, color='#f0754e', lineAt=[0, 'çalışan bir çocuktu']),
])
SC('dark', 'Sence Sultan İbrahim', [
    TI('deli miydi', 'DELİ Mİ?', 160),
    TI('kafesin kurbanı', 'KAFESİN KURBANI MI?', 110, color='#f0754e'),
    BD('Yorumlara yaz.', 'YORUMLARA YAZ', red=True, size=74),
])
