// "Bir tarafta onlar, diğer tarafta biz" — dosya stili, dikey. Mekânlar: split (üst ONLAR / alt BİZ), dark, board, map.
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 6180 / 30 };
const WORLD = { lon0: 20, lat0: 46, k: 600, latc: 30 };
const IMAGES = { fbsk: 'img/fbsk.jpg', ayvatoglu: 'img/ayvatoglu.jpg', zenbilci: 'img/zenbilci.jpg', pazar: 'img/pazar.jpg', pazar2: 'img/pazar2.jpg', kepenk: 'img/kepenk.jpg' };
const OBJECTS = [], SPACES = [];
function SC(t, s, ox, cam, objs, zm = 1) { SPACES.push({ t, s, cam: cam.map(([tt, x, y, z]) => ({ t: tt, x: x + ox, y, z: z * zm })) }); for (const o of objs) OBJECTS.push(Object.assign(o, { space: s }, o.x != null ? { x: o.x + ox } : {})); }
const FB_CENSOR = [0.40, 0.215, 0.68, 0.275];
const TL = v => Math.round(v).toLocaleString('tr-TR') + ' TL';
const GLITCH = [[0, .6, 1], [2.78, 3.05, .8], [61.7, 62.0, .6], [90.34, 90.6, .6], [99.9, 100.2, .5], [200.78, 201.0, .5]];

// 1) split: 2,17 milyar / ay sonu / lüks / emekli, asgari ücret, gençler
SC(0, 'split', 0, [[0, 0, -1150, .66], [2.9, 0, -1000, .6], [3.5, 0, -880, .58], [4.5, 0, 0, .32], [5.6, 0, 950, .6], [9.0, 0, 1050, .6]], [
  { id: 'fb', type: 'polaroid', img: 'fbsk', crop: [.12, 0, .76, .7], censor: FB_CENSOR, censorT: .3, x: 0, y: -1250, w: 760, rot: -.02, t0: 0, dur: .5, name: 'FATMA BETÜL SAYAN KAYA', nameT: .6, nameSize: 38 },
  { id: 'c217', type: 'counter', from: 0, to: 2170000000, fmt: TL, x: 0, y: -720, size: 150, t0: .86, dur: 1.92, sub: 'SORUŞTURMA DOSYASINDAKİ HİSSE SATIŞI', subSize: 30 },
  { id: 'fis', type: 'doc', x: -170, y: 950, w: 640, h: 820, rot: -.04, t0: 3.64, seed: 4, head: ['MARKET FİŞİ'], rowsBefore: 5, key: 'TOPLAM: ?', keySize: 70, keyT: 4.5, keyDur: .5, rowsAfter: 4 },
  { id: 'aysonu', type: 'tag', x: 300, y: 1350, w: 620, rot: .07, t0: 4.5, small: 'TAKVİM', big: 'AY SONU' },
  { id: 'milyonlar', type: 'band', text: 'MİLYONLARCA İNSAN', x: 0, y: 420, size: 80, t0: 6.9, red: true },
], 1.3);
SC(8.5, 'split', 2500, [[8.1, 0, -1000, .6], [12.4, 0, -1100, .6], [13.4, 0, -80, .31], [14.4, 0, 850, .58], [18.5, 0, 1000, .58], [21.4, 0, 1250, .58]], [
  { id: 'car', type: 'car', x: 0, y: -950, w: 1150, t0: 10.78 },
  { id: 'luks', type: 'title', text: 'LÜKS HAYATLAR', x: 0, y: -1500, size: 140, t0: 11.84, color: '#ffe1a0' },
  { id: 'emekli', type: 'polaroid', img: 'pazar', crop: [.1, 0, .8, 1], x: -250, y: 780, w: 560, rot: -.05, t0: 14.14, name: 'EMEKLİ', nameT: 14.5 },
  { id: 'kira', type: 'doc', x: 280, y: 1020, w: 520, h: 640, rot: .05, t0: 16.84, seed: 7, head: ['KİRA MAKBUZU'], rowsBefore: 4, rowsAfter: 3, stamp: { text: 'ÖDENEMEDİ', t: 18.22, x: 0, y: .1, rot: -.15 } },
  { id: 'asgari', type: 'band', text: 'ASGARİ ÜCRET', x: 280, y: 640, size: 60, t0: 16.84, pin: true },
  { id: 'gencler', type: 'band', text: 'GENÇLER', x: -280, y: 1500, size: 70, t0: 19.32, pin: true },
  { id: 'gelecek', type: 'strike', text: 'GELECEK', x: 120, y: 1720, size: 150, t0: 19.88, tStrike: 20.62 },
], 1.3);
// 2) karanlık: zoruna gidiyor / şahsi malı değil / vatana ihanet
SC(21.9, 'dark', 20000, [[21.5, 0, -300, .6], [27.0, 0, 250, .58], [32.6, 0, 1000, .56], [36.6, 0, 1350, .56], [41.6, 0, 1950, .58]], [
  { id: 'zor', type: 'title', text: 'ZORUNA\nGİDİYOR', x: 0, y: -380, size: 190, lh: 1.05, t0: 24.98, t1: 26.3, fadeDur: .35 },
  { id: 'kaynak2', type: 'title', text: 'KAYNAKLAR\nSERVET\nALIN TERİ', x: 0, y: -420, size: 140, lh: 1.15, t0: 26.92, lineT: [26.92, 28.5, 29.34], dur: .6 },
  { id: 'sahsi', type: 'title', text: 'KİMSENİN\nŞAHSİ MALI\nDEĞİLDİR', x: 0, y: 180, size: 170, lh: 1.08, rule: 260, t0: 30.2, lineT: [30.54, 31.18, 31.98] },
  { id: 'makam', type: 'strike', text: 'MAKAM', x: 0, y: 1000, size: 130, t0: 33.02, tStrike: 35.5 },
  { id: 'mevki', type: 'strike', text: 'MEVKİ', x: 0, y: 1180, size: 130, t0: 33.8, tStrike: 35.74 },
  { id: 'siyasi', type: 'strike', text: 'SİYASİ GÖRÜŞ', x: 0, y: 1360, size: 130, t0: 34.46, tStrike: 36.14 },
  { id: 'ihanet', type: 'title', text: 'VATANA\nİHANETTİR', x: 0, y: 1900, size: 190, lh: 1.05, t0: 39.62, color: '#e2493a' },
], 1.15);
// 3) pano: sabahın köründe, maaş eriyor
SC(41.25, 'board', 40000, [[40.9, 0, -700, .6], [46.0, 0, -350, .6], [50.0, 0, 300, .58], [54.0, 0, 550, .58]], [
  { id: 'saat', type: 'counter', from: 0, to: 1, fmt: () => '05:30', x: 0, y: -750, size: 260, t0: 43.76, dur: .3, solid: '#f1efe8', glow: 'rgba(0,0,0,.6)', sub: 'SABAHIN KÖRÜ', subSize: 40 },
  { id: 'bordro', type: 'doc', x: 0, y: -120, w: 900, h: 640, rot: .02, t0: 48.24, seed: 11, head: ['MAAŞ BORDROSU'], rowsBefore: 3, key: 'NET ÖDENEN', keySize: 74, keyT: 48.5, keyDur: .5, rowsAfter: 2 },
  { id: 'maas', type: 'meter', x: 0, y: 380, w: 860, h: 110, label: 'MAAŞ', t0: 48.8, keys: [{ t: 48.8, v: 1 }, { t: 51.06, v: .55 }, { t: 51.98, v: .22 }, { t: 52.7, v: 0 }] },
  { id: 'kiraB', type: 'band', text: 'KİRA', x: -320, y: 720, size: 80, t0: 51.06, red: true, pin: true },
  { id: 'faturaB', type: 'band', text: 'FATURA', x: 0, y: 860, size: 80, t0: 51.98, red: true, pin: true },
  { id: 'borcB', type: 'band', text: 'BORÇ', x: 320, y: 720, size: 80, t0: 52.7, red: true, pin: true },
  { id: 'sk', type: 'thread', from: 'bordro', to: 'kiraB', t0: 51.06, dur: .5, sag: .05 },
  { id: 'sf', type: 'thread', from: 'bordro', to: 'faturaB', t0: 51.98, dur: .5, sag: .05 },
  { id: 'sb', type: 'thread', from: 'bordro', to: 'borcB', t0: 52.7, dur: .5, sag: .05 },
], 1.3);
// 4) split: hisse satışları, milyonluk arabalar
SC(53.4, 'split', 5000, [[53.0, 0, -1750, .58], [57.0, 0, -1800, .56], [61.8, 0, -1750, .56]], [
  { id: 'hisse', type: 'chart', x: -420, y: -1550, w: 840, h: 520, t0: 55.04, dur: 1.6, pts: [[0, .05], [.12, .1], [.22, .08], [.35, .2], [.45, .18], [.58, .38], [.7, .35], [.82, .7], [1, 1]] },
  { id: 'hisseT', type: 'title', text: 'HİSSE SATIŞLARI', x: 0, y: -2180, size: 120, t0: 56.14, color: '#ffe1a0' },
], 1.25);
// 5) pano: Fatma Betül Sayan Kaya dosyası
SC(61.5, 'board', 60000, [[61.1, -100, -500, .6], [63.6, 0, -250, .56], [66.2, 0, 450, .58], [70.0, 0, 600, .58], [74.6, 0, 1250, .6], [80.0, 0, 1320, .62]], [
  { id: 'fb2', type: 'polaroid', img: 'fbsk', crop: [.12, 0, .76, .7], censor: FB_CENSOR, censorT: 61.75, x: -270, y: -430, w: 520, rot: -.05, t0: 61.7, name: 'F. B. SAYAN KAYA', nameT: 62.1, nameSize: 30 },
  { id: 'kupur', type: 'doc', x: 270, y: -380, w: 560, h: 720, rot: .04, t0: 62.88, seed: 23, head: ['HABER', 'FON SORUŞTURMASI'], rowsBefore: 3, key: 'HİSSE SATIŞI', keySize: 52, keyT: 63.2, keyDur: .5, rowsAfter: 5 },
  { id: 'sfk', type: 'thread', from: 'fb2', to: 'kupur', t0: 63.3, dur: .6, sag: .1 },
  { id: 'kaynak', type: 'region', text: 'KAYNAK: BİRGÜN, T24, NTV, SÖZCÜ', x: 0, y: 70, size: 30, alpha: .75, t0: 63.5 },
  { id: 'c163', type: 'counter', from: 0, to: 163000000, fmt: TL, x: 0, y: 330, size: 120, t0: 64.34, dur: 1.1, sub: 'YATIRIM', subSize: 30, solid: '#f1efe8', glow: 'rgba(0,0,0,.6)' },
  { id: 'c217b', type: 'counter', from: 163000000, to: 2170000000, fmt: TL, x: 0, y: 720, size: 140, t0: 66.98, dur: 1.8, sub: 'HİSSE SATIŞI', subSize: 32 },
  { id: 'kat', type: 'band', text: '×13', x: 380, y: 520, size: 90, red: true, rot: -.06, t0: 68.8 },
  { id: 'nasil', type: 'doc', x: 0, y: 1300, w: 900, h: 440, rot: -.02, t0: 74.52, seed: 31, pin: true, head: [], rowsBefore: 1, key: 'NASIL DÖNÜYOR?', keySize: 84, keyT: 77.18, keyDur: 1.6, circleT: 78.7, rowsAfter: 1 },
], 1.3);
// 6) split: rakamlar / pazarda domates, peynir
SC(79.6, 'split', 0, [[79.2, 0, -1050, .58], [81.1, 0, -900, .56], [82.1, 0, 250, .31], [83.2, 0, 1400, .58], [87.4, 0, 1550, .58]], [
  { id: 'domates', type: 'strike', text: 'DOMATES', x: 0, y: 1750, size: 130, t0: 83.38, tStrike: 85.54 },
  { id: 'peynir', type: 'strike', text: 'PEYNİR', x: 0, y: 1920, size: 130, t0: 84.34, tStrike: 85.86 },
], 1.3);
// 7) pano: Kürşat Ayvatoğlu
SC(87.2, 'board', 80000, [[86.8, 0, -500, .6], [91.0, 0, -350, .58], [94.2, 0, 650, .6], [98.8, 0, 820, .6]], [
  { id: 'ayv', type: 'polaroid', img: 'ayvatoglu', crop: [.5, 0, .48, 1], censor: [0.645, 0.24, 0.79, 0.32], censorT: 88.1, x: 0, y: -420, w: 760, rot: .03, t0: 87.64, name: 'KÜRŞAT AYVATOĞLU', nameT: 90.34, color: true },
  { id: 'pudra', type: 'doc', x: 0, y: 720, w: 900, h: 760, rot: -.03, t0: 92.34, seed: 41, head: ['HABER', 'LÜKS ARAÇTA ÇEKİLEN GÖRÜNTÜLER'], rowsBefore: 2, key: '"PUDRA ŞEKERİ"', keySize: 92, keyT: 94.4, keyDur: .8, circleT: 95.2, rowsAfter: 3 },
  { id: 'itiraf', type: 'region', text: 'SONRAKİ İFADESİNDE KOKAİN KULLANDIĞINI KABUL ETTİ (2021)', x: 0, y: 1160, size: 26, alpha: .8, t0: 95.3 },
  { id: 'silinmedi', type: 'band', text: 'SİLİNMEDİ', x: 280, y: 1330, size: 90, red: true, rot: -.05, t0: 97.56 },
], 1.3);
// 8) pano: milletvekilinin oğlu, karar, adalet
SC(98.4, 'board', 100000, [[98.0, 0, -500, .6], [103.0, 0, -250, .6], [108.6, 0, 300, .56], [112.6, 0, 700, .56], [119.5, 0, 1550, .55], [126.0, 0, 1950, .56], [127.8, 0, 2050, .57]], [
  { id: 'karar', type: 'doc', x: 120, y: -330, w: 1000, h: 1150, rot: .02, t0: 98.62, seed: 51, head: ['KARAR', 'OSMANİYE 4. AĞIR CEZA'], rowsBefore: 3, redact: [1], key: '25 KG 850 GR ESRAR', keySize: 72, keyT: 102.46, keyDur: 1.6, circleT: 104.2, rowsAfter: 5, stamp: { text: '11 YIL 8 AY', t: 107.36, x: .05, y: .3, rot: -.1 } },
  { id: 'zen', type: 'polaroid', img: 'zenbilci', crop: [.18, .08, .66, .72], censor: [0.345, 0.435, 0.645, 0.51], censorT: 100.1, x: -300, y: 520, w: 520, rot: -.05, t0: 99.9, name: 'VEKİLİN OĞLU', nameT: 100.3, color: true },
  { id: 'sz', type: 'thread', from: 'zen', to: 'karar', t0: 100.6, dur: .6, sag: .1 },
  { id: 'sahsidir', type: 'band', text: 'SUÇ ŞAHSİDİR', x: 260, y: 820, size: 80, t0: 113.2, pin: true },
  { id: 'terazi', type: 'scale', x: 0, y: 1350, w: 900, t0: 119.0, left: 'İMKÂN', right: 'ADALET', leftColor: '#ffe1a0', tilt: [{ t: 120.5, a: -.24, dur: 2.2 }] },
  { id: 'adalet', type: 'title', text: 'ADALET?', x: 0, y: 2400, size: 200, t0: 125.3 },
], 1.25);
// 9) pano: peki biz ne yapıyoruz?
SC(127.2, 'board', 120000, [[126.8, 0, -1100, .6], [130.4, 0, -560, .6], [133.4, 0, -20, .6], [136.6, 0, 560, .6], [139.6, 0, 1220, .6], [143.0, 0, 1550, .6], [146.6, 0, 2150, .6], [150.6, 0, 2250, .6]], [
  { id: 'pekibiz', type: 'title', text: 'PEKİ BİZ?', x: 0, y: -1150, size: 210, t0: 127.66, color: '#fff3dd' },
  { id: 'emekli2', type: 'polaroid', img: 'pazar2', crop: [.1, 0, .8, 1], x: -230, y: -620, w: 560, rot: -.04, t0: 129.22, name: 'EMEKLİ', nameT: 129.6 },
  { id: 'ucuz', type: 'band', text: 'EN UCUZ ÜRÜN', x: 290, y: -500, size: 64, red: true, t0: 130.5, pin: true },
  { id: 'isci', type: 'tag', x: 240, y: -40, w: 640, rot: .06, t0: 131.94, small: 'İŞÇİ', big: 'AY SONU' },
  { id: 'esnaf', type: 'polaroid', img: 'kepenk', x: -230, y: 520, w: 560, rot: .04, t0: 135.68, name: 'ESNAF', nameT: 136.0 },
  { id: 'siftah', type: 'band', text: 'SİFTAH YOK', x: 290, y: 680, size: 70, red: true, t0: 136.1, pin: true },
  { id: 'cv', type: 'doc', x: 230, y: 1300, w: 560, h: 640, rot: -.03, t0: 138.52, seed: 61, head: ['ÖZGEÇMİŞ'], rowsBefore: 5, rowsAfter: 3, stamp: { text: 'İŞ YOK', t: 139.28, x: 0, y: .05, rot: -.12 } },
  { id: 'genc2', type: 'band', text: 'GENÇLER', x: -280, y: 1200, size: 74, t0: 138.52, pin: true },
  { id: 'hayat', type: 'strike', text: 'HAYAT', x: -250, y: 1560, size: 110, t0: 141.16, tStrike: 142.62 },
  { id: 'senet', type: 'doc', x: -200, y: 2050, w: 620, h: 520, rot: .03, t0: 143.74, seed: 71, head: ['BORÇ SENEDİ'], rowsBefore: 1, key: 'SANAL KUMAR', keySize: 66, keyT: 144.46, keyDur: .8, rowsAfter: 2 },
  { id: 'aile', type: 'band', text: 'AİLE', x: 320, y: 2350, size: 100, red: true, t0: 146.66, pin: true },
  { id: 'ssa', type: 'thread', from: 'senet', to: 'aile', t0: 147.2, dur: .7, sag: .12 },
], 1.3);
// 10) split, iki taraf aynı kadrede
SC(150.3, 'split', 7500, [[149.9, 0, -150, .46], [156.2, 0, -60, .46], [162.4, 0, 60, .46]], [
  { id: 'car2', type: 'car', x: 0, y: -1100, w: 1500, t0: 150.82 },
  { id: 'kart', type: 'doc', x: 0, y: 950, w: 940, h: 560, rot: -.03, t0: 153.44, seed: 81, pin: true, head: ['OTOBÜS KARTI'], rowsBefore: 0, key: 'BAKİYE YETERSİZ', keySize: 66, keyT: 154.8, keyDur: .7, rowsAfter: 1 },
  { id: 'milyarlar', type: 'counter', from: 0, to: 1, fmt: () => 'MİLYARLAR', x: 0, y: -1750, size: 230, t0: 157.24, dur: .3 },
  { id: 'sepet', type: 'band', text: 'SEPET KÜÇÜLÜYOR', x: 0, y: 1550, size: 110, red: true, t0: 160.6 },
], 1.15);
// 11) karanlık: neden hep aynı insanlar
SC(162.0, 'dark', 140000, [[161.6, 0, -500, .58], [167.4, 0, 150, .55], [174.3, 0, 650, .56]], [
  { id: 'neden', type: 'title', text: 'NEDEN HEP\nAYNI İNSANLAR?', x: 0, y: -620, size: 140, lh: 1.1, t0: 165.94 },
  { id: 'terazi2', type: 'scale', x: 0, y: 150, w: 1000, t0: 164.4, left: 'ONLAR', right: 'BİZ', leftDots: 1, rightDots: 160, tilt: [{ t: 166.6, a: .26, dur: 1.6 }] },
  { id: 'hayatta', type: 'title', text: 'SADECE\nHAYATTA KALMAK', x: 0, y: 1320, size: 130, lh: 1.1, t0: 172.02 },
], 1.15);
// 12) karanlık: istemiyoruz / istiyoruz / adalet
SC(173.9, 'dark', 160000, [[173.5, 0, -650, .6], [179.4, 0, -250, .58], [185.4, 0, 350, .58], [191.4, 0, 850, .56], [195.0, 0, 1000, .57]], [
  { id: 'xluks', type: 'strike', text: 'LÜKS', x: 0, y: -760, size: 140, t0: 174.86, tStrike: 175.16 },
  { id: 'xmilyar', type: 'strike', text: 'MİLYAR', x: 0, y: -560, size: 140, t0: 176.42, tStrike: 176.94 },
  { id: 'xayr', type: 'strike', text: 'AYRICALIK', x: 0, y: -360, size: 140, t0: 177.98, tStrike: 178.6 },
  { id: 'gecin', type: 'title', text: 'GEÇİNEBİLMEK', x: 0, y: 160, size: 140, t0: 181.06, color: '#ffd9a0' },
  { id: 'gelec', type: 'title', text: 'GELECEK', x: 0, y: 400, size: 140, t0: 184.24, color: '#ffd9a0' },
  { id: 'pazarh', type: 'title', text: 'HESAPSIZ PAZAR', x: 0, y: 640, size: 110, t0: 187.62, color: '#ffd9a0' },
  { id: 'adalet2', type: 'counter', from: 0, to: 1, fmt: () => 'ADALET', x: 0, y: 1150, size: 300, t0: 193.28, dur: .3, sub: 'HERKES İÇİN', subSize: 50 },
], 1.15);
// 13) harita: bu ülke hepimizin
SC(194.6, 'map', 0, [[194.2, 7900, 4600, .115], [200.4, 7900, 4700, .105]], [
  { id: 'iller', type: 'lights', pts: ILLER, t0: 195.3, step: .035 },
  { id: 'hepimiz', type: 'title', text: 'BU ÜLKE\nHEPİMİZİN', x: 7900, y: 8700, size: 1250, lh: 1.05, t0: 198.14 },
]);
// 14) split final: onlar / biz
SC(199.9, 'split', 10000, [[199.5, 0, -250, .48], [206.0, 0, 250, .5]], [
  { id: 'onlar', type: 'counter', from: 0, to: 1, fmt: () => 'ONLAR', x: 0, y: -900, size: 230, t0: 200.5, dur: .3 },
  { id: 'biz', type: 'counter', from: 0, to: 1, fmt: () => 'BİZ', x: 0, y: 1000, size: 460, t0: 202.9, dur: .3, solid: '#ffffff', glow: 'rgba(255,255,255,.7)' },
], 1.1);
const CAMERA = SPACES[0].cam;
const BEATS = [
  [0, ['fb', 'c217'], .1], [3.64, ['fis', 'aysonu'], .1], [6.9, ['fis', 'aysonu', 'milyonlar'], .1], [8.64, ['car', 'luks'], .1],
  [13.24, ['emekli'], .1], [16.84, ['kira', 'asgari'], .1], [19.32, ['gencler', 'gelecek'], .1],
  [22.12, ['zor'], .2], [26.5, ['kaynak2'], .2], [30.4, ['sahsi'], .2], [33.02, ['makam', 'mevki', 'siyasi'], .2], [39.62, ['ihanet'], .2],
  [41.38, ['saat'], .2], [48.24, ['bordro', 'maas'], .2], [51.06, ['maas', 'kiraB', 'faturaB', 'borcB', 'sk', 'sf', 'sb'], .2],
  [53.56, ['hisse', 'hisseT', 'car'], .1],
  [61.7, ['fb2', 'kupur', 'sfk', 'kaynak'], .25], [64.34, ['c163'], .25], [66.98, ['c217b', 'kat'], .25], [71.94, ['nasil'], .25],
  [79.86, ['c217', 'fb'], .1], [81.46, ['fis', 'domates', 'peynir'], .1],
  [87.28, ['ayv'], .25], [92.34, ['pudra', 'itiraf'], .25], [96.36, ['pudra', 'silinmedi'], .25],
  [98.62, ['karar', 'zen', 'sz'], .25], [111.06, ['sahsidir', 'zen'], .25], [116.28, ['terazi', 'adalet'], .25],
  [127.4, ['pekibiz'], .25], [129.22, ['emekli2', 'ucuz'], .25], [131.94, ['isci'], .25], [135.68, ['esnaf', 'siftah'], .25], [138.52, ['cv', 'genc2', 'hayat'], .25], [143.74, ['senet', 'aile', 'ssa'], .25],
  [150.6, ['car2'], .1], [153.44, ['kart'], .1], [156.5, ['milyarlar'], .1], [158.5, ['sepet', 'kart'], .1],
  [162.32, ['neden', 'terazi2'], .2], [167.86, ['terazi2', 'hayatta'], .2],
  [174.1, ['xluks', 'xmilyar', 'xayr'], .2], [179.8, ['gecin', 'gelec', 'pazarh'], .2], [190.52, ['adalet2'], .2],
  [194.78, ['iller', 'hepimiz'], .05], [200.14, ['onlar'], .1], [202.12, ['biz'], .1],
].map(([t, hero, mapDim]) => ({ t, hero, mapDim }));

// --- Ek cümle: "Eski Aile Bakanı ... tutuklandı." 71.742 sn'ye eklendi; sonrası kaydırılır.
const SHIFT_AT = 71.742, SHIFT = 5.598, sh = v => (v != null && v >= SHIFT_AT ? v + SHIFT : v);
FORMAT.dur = 6348 / 30;
for (const o of OBJECTS) {
  for (const k of ['t0', 't1', 'keyT', 'circleT', 'tStrike', 'nameT', 'censorT']) if (o[k] != null) o[k] = sh(o[k]);
  if (o.stamp) o.stamp.t = sh(o.stamp.t); if (o.lineT) o.lineT = o.lineT.map(sh); if (o.tilt) o.tilt.forEach(k => k.t = sh(k.t)); if (o.keys) o.keys.forEach(k => k.t = sh(k.t));
}
for (const sp of SPACES) { sp.t = sh(sp.t); sp.cam.forEach(k => k.t = sh(k.t)); }
for (const b of BEATS) b.t = sh(b.t);
for (const g of GLITCH) { g[0] = sh(g[0]); g[1] = sh(g[1]); }
// eklenen anda kamera kupüre döner, damga iner
{ const sc = SPACES.find(x => x.t === 61.5), z = 1.3; sc.cam.splice(4, 0, { t: 72.4, x: 60000, y: -220, z: .56 * z }, { t: 76.9, x: 60000, y: -160, z: .58 * z }); sc.cam.sort((a, b) => a.t - b.t);
  const k = OBJECTS.find(o => o.id === 'kupur'); k.stamp = { text: 'TUTUKLANDI', t: 76.0, x: 0, y: .3, rot: -.12, size: 92 };
  OBJECTS.push({ id: 'suclama', type: 'band', text: 'SUÇ ÖRGÜTÜ ÜYELİĞİ', x: 60000 + 260, y: 150, size: 60, red: true, rot: -.03, t0: 74.6, space: 'board' });
  BEATS.push({ t: 71.9, hero: ['kupur', 'fb2', 'sfk', 'suclama'], mapDim: .25 }); BEATS.sort((a, b) => a.t - b.t); }
// --- Final: "Tuna Nehri" türküsünden dörtlükler (Cavit okur, 212.0 sn'de başlar; okuma %92 hıza yavaşlatıldı)
{ const T0 = 212.0, k = v => T0 + v / 0.92;
  FORMAT.dur = 6942 / 30;
  SPACES.push({ t: 211.4, s: 'dark', cam: [{ t: 211.0, x: 300000, y: -260, z: .66 }, { t: 220.0, x: 300000, y: -120, z: .68 }, { t: 231.4, x: 300000, y: 120, z: .7 }] });
  OBJECTS.push(
    { id: 'kita1', type: 'title', space: 'dark', text: 'OLUR MU BÖYLE OLUR MU?\nEVLAT BABAYI VURUR MU?\nSİZİ VATAN HAİNLERİ,\nBU VATAN SİZE KALIR MI?', x: 300000, y: -560, size: 96, lh: 1.45, track: .06, t0: k(0), lineT: [k(0), k(2.94), k(5.02), k(6.42)], dur: .7, t1: k(8.0), fadeDur: .45 },
    { id: 'kita2', type: 'title', space: 'dark', text: 'OLAMAZ BÖYLE OLAMAZ,\nEVLAT BABAYI VURAMAZ!\nCAN BEDENDEN ÇIKMAYINCA,', x: 300000, y: -420, size: 96, lh: 1.45, track: .06, t0: k(8.34), lineT: [k(8.34), k(10.34), k(12.18)], dur: .7 },
    { id: 'kalamaz', type: 'title', space: 'dark', text: 'BU VATAN SİZE KALAMAZ...', x: 300000, y: 260, size: 104, track: .06, t0: k(13.82), dur: .9, color: '#e2493a' },
    { id: 'turku', type: 'region', space: 'dark', text: 'TUNA NEHRİ AKMAM DİYOR · TÜRKÜ', x: 300000, y: 620, size: 34, alpha: .6, t0: k(1.0) });
  BEATS.push({ t: 211.6, hero: ['kita1', 'turku'], mapDim: .2 }, { t: k(8.2), hero: ['kita2', 'turku'], mapDim: .2 }, { t: k(13.7), hero: ['kita2', 'kalamaz', 'turku'], mapDim: .2 });
  BEATS.sort((a, b) => a.t - b.t); }
