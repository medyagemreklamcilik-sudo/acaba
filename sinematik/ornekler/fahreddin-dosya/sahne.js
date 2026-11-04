// Fahreddin Paşa: Çöl Kaplanı, "dosya" stili, tam metin (143.9 sn, 9:16).
// Üç ayrı mekân: 'dark' (karanlık stüdyo), 'board' (mantar pano), 'map' (koyu harita). Pano haritanın üstünde değil;
// mekânlar arası geçiş yumuşak kararmayla. Kelime zamanları build/aligned.json'dan.
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 4316 / 30 };
const WORLD = { lon0: 20, lat0: 46, k: 600, latc: 30 };
const IMAGES = {}; for (const k of ['pasa', 'pasa2', 'pasa3', 'pasa4', 'yasli', 'vahdettin', 'vahdettin2', 'askerler', 'toplanma', 'kapi', 'subaylar', 'kubbe', 'emanet', 'mondros', 'mezar', 'yorgun']) IMAGES[k] = `img/${k}.jpg`;
const OBJECTS = [], SPACES = [];
const LL = (lo, la) => ({ lon: lo, lat: la });
const MED = [39.61, 24.47], IST = [28.97, 41.01];
// sahne: zaman, mekân, ofset, kamera anahtarları (yerel), nesneler (yerel)
function SC(t, s, ox, cam, objs) {
  SPACES.push({ t, s, cam: cam.map(([tt, x, y, z]) => ({ t: tt, x: x + ox, y, z })) });
  for (const o of objs) OBJECTS.push(Object.assign(o, { space: s }, o.x != null ? { x: o.x + ox } : {}));
}
// 1) karanlık: nokta portre + ÇÖL KAPLANI
SC(0, 'dark', 0, [[0, 0, -200, .68], [1.7, 0, 0, .63], [3.6, 0, 350, .58]], [
  { id: 'pasa', type: 'halftone', img: 'pasa', crop: [.08, 0, .84, .56], x: 0, y: -150, w: 1150, cols: 70, t0: -.35, rev: 1.3, glow: [.64, .2] },
  { id: 'kaplan', type: 'title', text: 'ÇÖL\nKAPLANI', x: 0, y: 880, size: 300, lh: 1.0, rule: 420, t0: 1.84 },
]);
// 2) pano: 1918 / telgraf / Vahdettin
SC(3.1, 'board', 0, [[2.6, 9750, 10150, .6], [4.4, 10080, 10250, .56], [5.5, 10500, 10600, .72], [6.5, 10020, 10900, .6], [8.7, 10150, 11100, .57]], [
  { id: 'tag', type: 'tag', x: 9560, y: 10300, w: 720, rot: -.07, t0: 3.24, small: 'DOSYA', big: '1918', sub: 'MONDROS' },
  { id: 'telgraf', type: 'doc', x: 10560, y: 10700, w: 1000, h: 1350, rot: .03, t0: 4.45, seed: 8, head: ['TELGRAF', 'HARBİYE NEZARETİ', 'MEDİNE MUHAFIZINA'], rowsBefore: 4, redact: [1, 102], key: 'TESLİM OLUNUZ.', keySize: 82, keyT: 4.62, keyDur: .7, circleT: 4.95, rowsAfter: 6 },
  { id: 'vah', type: 'polaroid', img: 'vahdettin', crop: [.12, .02, .76, .5], x: 9650, y: 11300, w: 720, rot: -.04, t0: 6.2, name: 'VAHDETTİN', nameT: 6.5 },
  { id: 's1', type: 'thread', from: 'tag', to: 'telgraf', t0: 4.75, dur: .7, sag: .12 },
  { id: 's2', type: 'thread', from: 'vah', to: 'telgraf', t0: 6.95, dur: .7, sag: .1 },
]);
// 3) harita: Medine
SC(8.25, 'map', 0, [[7.8, 10190, 12700, .55], [10.9, 10190, 12950, .6]], [
  { id: 'med', type: 'glowdot', ...LL(...MED), t0: 8.45, label: 'MEDİNE', size: 95, square: true, crossT: 9.86 },
]);
// 4) karanlık: düşman değil, kendi askerleri
SC(10.4, 'dark', 20000, [[10.0, 0, -200, .55], [12.7, 0, 100, .54], [15.6, 0, 250, .56]], [
  { id: 'asker', type: 'polaroid', img: 'askerler', x: 0, y: 0, w: 1300, rot: -.02, t0: 10.5, dur: .8, brackets: { t: 13.98, r: [.02, .22, .5, .72] } },
  { id: 'dusman', type: 'strike', text: 'DÜŞMAN', x: 0, y: -690, size: 170, t0: 12.0, tStrike: 12.5 },
  { id: 'kendi', type: 'title', text: 'KENDİ\nASKERLERİ', x: 0, y: 750, size: 230, lh: 1.02, t0: 12.88 },
]);
// 5) pano: Ömer Fahreddin, Soyadı Kanunu, Türkkan imzası
SC(15.15, 'board', 40000, [[14.7, -150, -300, .6], [17.6, -100, -150, .55], [19.4, 150, -250, .56], [21.2, -150, 450, .62], [25.0, -120, 300, .56]], [
  { id: 'pasaP', type: 'polaroid', img: 'pasa', x: -200, y: 80, w: 860, rot: .02, t0: 15.24, brackets: { t: 20.14, r: [.0, .855, 1, .14] } },
  { id: 'adBand', type: 'band', text: 'ÖMER FAHREDDİN', x: -200, y: -860, size: 70, rot: -.02, t0: 15.74, pin: true },
  { id: 't1934', type: 'tag', x: 470, y: -520, w: 720, rot: .07, t0: 18.2, small: 'SOYADI KANUNU', big: '1934' },
  { id: 's3', type: 'thread', from: 't1934', to: 'pasaP', t0: 20.2, dur: .7, sag: .12 },
]);
// 6) harita: Medine Müdafii, kuşatma, kesilen demiryolu
SC(24.5, 'map', 0, [[24.1, 10190, 12000, .34], [27.0, 10190, 12450, .31], [29.4, 9950, 11300, .2], [31.8, 9800, 10900, .18]], [
  { id: 'mudafi', type: 'title', text: 'MEDİNE\nMÜDAFİİ', x: 10190, y: 10950, size: 330, lh: 1.0, t0: 24.9, t1: 27.4, fadeDur: .6 },
  { id: 'ring', type: 'ring', ...LL(...MED), r0: 2800, r1: 1150, t0: 28.9, dur: 1.6, t1: 31.6 },
  { id: 'hat', type: 'route', pts: [[36.29, 33.51], [35.93, 31.95], [35.73, 30.19], [36.57, 28.38], [37.95, 26.79], MED], t0: 29.9, t1: 30.6, dash: true, hide: 31.6 },
  { id: 'xm', type: 'xmark', ...LL(36.4, 29.3), s: 70, t0: 30.55, t1: 31.6 },
]);
// 7) pano: erzak, hastalık, rivayet: çekirge
SC(31.3, 'board', 60000, [[30.9, 0, -650, .6], [32.6, -60, -350, .6], [34.0, 50, 150, .58], [36.3, 0, 850, .56], [39.4, 60, 1300, .6], [44.4, 40, 1450, .62]], [
  { id: 'rapor', type: 'doc', x: 0, y: -720, w: 1000, h: 1150, rot: -.02, t0: 31.3, seed: 3, head: ['DURUM RAPORU', 'MEDİNE MUHAFIZLIĞI'], rowsBefore: 3, redact: [0], key: 'ERZAK TÜKENDİ.', keySize: 80, keyT: 31.62, keyDur: .6, circleT: 31.95, rowsAfter: 5 },
  { id: 'kapi', type: 'polaroid', img: 'kapi', crop: [0, .05, 1, .7], x: -300, y: 380, w: 720, rot: -.05, t0: 32.9, name: 'MEDİNE GARNİZONU', nameT: 33.3 },
  { id: 'rivayet', type: 'tag', x: 420, y: 200, w: 640, rot: .08, t0: 34.62, small: 'ANLATILANLARA GÖRE', big: 'RİVAYET' },
  { id: 'pasa2', type: 'polaroid', img: 'pasa2', crop: [0, 0, 1, .72], x: -120, y: 1300, w: 760, rot: .03, t0: 35.6 },
  { id: 's4', type: 'thread', from: 'rivayet', to: 'pasa2', t0: 36.1, dur: .7, sag: .1 },
  { id: 'cekirge', type: 'band', text: 'ÇEKİRGE', x: 330, y: 1820, size: 90, rot: -.04, t0: 39.78, red: true, pin: true },
]);
// 8) karanlık: Mescid-i Nebevî önünde yemin
SC(44.0, 'dark', 80000, [[43.6, 0, -420, .6], [48.5, 0, -220, .56], [50.2, 0, 230, .56], [53.4, 0, 380, .6]], [
  { id: 'toplanma', type: 'polaroid', img: 'toplanma', x: 0, y: -560, w: 1250, rot: -.015, t0: 44.18, name: 'MESCİD-İ NEBEVÎ', nameT: 45.76 },
  { id: 'yaRes', type: 'title', text: '“YA RESULALLAH,\nBİZ SENİ\nBIRAKMAYIZ!”', x: 0, y: 520, size: 150, lh: 1.15, t0: 49.96, lineT: [49.96, 51.54, 52.04] },
]);
// 9) pano: tahliye emri, Paşa okur
SC(53.0, 'board', 100000, [[52.6, 50, -350, .6], [54.6, 120, -250, .68], [56.4, 80, 100, .6], [58.6, -200, 650, .62], [61.6, -180, 760, .64]], [
  { id: 'tahliye', type: 'doc', x: 100, y: -300, w: 1000, h: 1300, rot: -.02, t0: 53.22, seed: 12, head: ['TELGRAF', 'İSTANBUL', 'MEDİNE MUHAFIZINA'], rowsBefore: 4, redact: [2, 101], key: 'MEDİNE TAHLİYE EDİLECEK.', keySize: 60, keyT: 54.64, keyDur: 1.0, circleT: 55.72, rowsAfter: 6 },
  { id: 'pasa3', type: 'polaroid', img: 'pasa3', crop: [.22, 0, .56, 1], x: -300, y: 760, w: 820, rot: .04, t0: 56.74, name: 'FAHREDDİN PAŞA', nameT: 57.1 },
  { id: 's5', type: 'thread', from: 'tahliye', to: 'pasa3', t0: 57.6, dur: .7, sag: .1 },
]);
// 10) karanlık: bayrak sözü
SC(61.2, 'dark', 120000, [[60.8, 0, -40, .58], [65.6, 0, 60, .62]], [
  { id: 'bayrak', type: 'title', text: '“TÜRK BAYRAĞINI\nKENDİ ELİMLE\nİNDİREMEM.”', x: 0, y: -150, size: 150, lh: 1.2, t0: 61.44, lineT: [62.40, 63.38, 64.14], dur: .6 },
]);
// 11) harita: kutsal emanetler İstanbul'a, Paşa kalır
SC(65.2, 'map', 0, [[64.8, 10190, 12600, .36], [67.0, 8800, 10500, .22], [70.0, 7400, 8200, .16], [72.0, 7500, 8400, .16], [74.2, 9300, 11200, .25]], [
  { id: 'emanet', type: 'polaroid', img: 'emanet', crop: [0, .05, 1, .7], x: 6300, y: 11500, w: 2900, rot: -.03, t0: 66.3, dur: .8, name: 'KUTSAL EMANETLER', nameT: 66.9, nameSize: 160, t1: 73.8 },
  { id: 'hat2', type: 'route', pts: [MED, [37.95, 26.79], [36.57, 28.38], [35.73, 30.19], [35.93, 31.95], [36.29, 33.51], [37.16, 36.2], [35.32, 37.0], [32.48, 37.87], [30.52, 39.78], IST], t0: 69.6, t1: 71.4, hide: 73.8 },
  { id: 'band2000', type: 'band', text: '2.000 ASKER', x: 6200, y: 6400, size: 480, rot: -.03, t0: 69.24, red: true, t1: 73.8 },
  { id: 'ist', type: 'glowdot', ...LL(...IST), t0: 70.9, label: 'İSTANBUL', size: 95, square: true, t1: 73.8 },
]);
// 12) karanlık: 1918, Mondros
SC(73.5, 'dark', 140000, [[73.1, 0, -250, .6], [75.8, 0, 0, .56], [78.0, 0, 450, .58]], [
  { id: 'y1918', type: 'title', text: '1918', x: 0, y: -280, size: 360, rule: 380, track: .2, t0: 74.26 },
  { id: 'otuz', type: 'region', text: '30 EKİM', x: 0, y: -90, size: 70, alpha: .55, t0: 76.56 },
  { id: 'mondros', type: 'polaroid', img: 'mondros', x: 0, y: 700, w: 1150, rot: .02, t0: 76.0, name: 'MONDROS', nameT: 76.56 },
]);
// 13) pano: tebliğ, Vahdettin, azil, ret
SC(77.6, 'board', 160000, [[77.2, 0, -450, .62], [79.4, 0, -320, .66], [81.4, -230, 420, .58], [83.4, 230, 560, .58], [84.8, 0, -200, .6], [86.2, 0, -280, .62]], [
  { id: 'teblig', type: 'doc', x: 0, y: -420, w: 1000, h: 1250, rot: .02, t0: 77.88, seed: 21, head: ['TEBLİĞ', 'MÜTAREKE HÜKÜMLERİ'], rowsBefore: 3, redact: [1, 103], key: 'MEDİNE TESLİM EDİLECEK.', keySize: 62, keyT: 78.1, keyDur: .9, rowsAfter: 6, stamp: { text: 'REDDEDİLDİ', t: 84.5, x: .05, y: .3, rot: -.13 } },
  { id: 'vah2', type: 'polaroid', img: 'vahdettin2', crop: [.05, .02, .9, .62], x: -330, y: 640, w: 700, rot: -.05, t0: 80.88, name: 'VAHDETTİN', nameT: 81.3 },
  { id: 's6', type: 'thread', from: 'vah2', to: 'teblig', t0: 81.6, dur: .7, sag: .1 },
  { id: 'azil', type: 'tag', x: 430, y: 560, w: 640, rot: .07, t0: 83.04, small: 'EMİR', big: 'AZİL' },
]);
// 14) karanlık: rüya
SC(85.8, 'dark', 180000, [[85.4, 0, -300, .55], [92.0, 0, 180, .6], [93.4, 0, 260, .6]], [
  { id: 'kubbe', type: 'polaroid', img: 'ravza', crop: [0, .12, 1, .62], x: 0, y: -220, w: 1150, rot: -.02, t0: 86.0, dur: 1.0, pin: false },
  { id: 'olma', type: 'title', text: '“TESLİM OLMA.”', x: 0, y: 900, size: 175, t0: 91.2 },
]);
// 15) pano: cevap telgrafı, yorgun askerler, son ana kadar
SC(92.9, 'board', 200000, [[92.5, 0, -650, .6], [95.2, 0, -500, .68], [97.3, -50, 200, .56], [99.6, 80, 520, .58], [102.2, 150, 640, .58], [104.0, 80, 1300, .58], [106.5, 60, 1450, .6]], [
  { id: 'cevap', type: 'doc', x: 0, y: -620, w: 1000, h: 1200, rot: -.02, t0: 93.16, seed: 31, head: ['TELGRAF', 'MEDİNE MUHAFIZI', 'FAHREDDİN'], rowsBefore: 4, redact: [2], key: 'DÜŞMANA TESLİM ETMEM.', keySize: 64, keyT: 95.5, keyDur: 1.3, circleT: 96.4, rowsAfter: 5 },
  { id: 'yorgun', type: 'polaroid', img: 'yorgun', x: -260, y: 560, w: 900, rot: .03, t0: 97.76 },
  { id: 'ac', type: 'band', text: 'AÇ', x: 400, y: 330, size: 90, rot: -.05, t0: 100.26, pin: true },
  { id: 'hasta', type: 'band', text: 'HASTA', x: 420, y: 560, size: 90, rot: .04, t0: 100.88, pin: true },
  { id: 'yorgunB', type: 'band', text: 'YORGUN', x: 390, y: 790, size: 90, rot: -.02, t0: 101.88, pin: true },
  { id: 'pasa4', type: 'polaroid', img: 'pasa4', crop: [0, 0, 1, .72], x: 80, y: 1500, w: 760, rot: -.03, t0: 102.7 },
  { id: 's7', type: 'thread', from: 'yorgun', to: 'pasa4', t0: 103.4, dur: .7, sag: .1 },
]);
// 16) karanlık: yakalanış, teslim
SC(106.1, 'dark', 220000, [[105.7, 0, -300, .6], [111.7, 0, 100, .58]], [
  { id: 'tarih', type: 'region', text: '10 OCAK 1919', x: 0, y: -960, size: 80, alpha: .6, t0: 106.88 },
  { id: 'subaylar', type: 'polaroid', img: 'subaylar', x: 0, y: -200, w: 1250, rot: -.02, t0: 106.26 },
  { id: 'esir', type: 'band', text: 'ESİR', x: 0, y: 650, size: 150, red: true, t0: 110.16 },
]);
// 17) harita: 72 gün, 2 yıl 7 ay, Mısır, Malta
SC(111.3, 'map', 0, [[110.9, 10190, 12300, .3], [117.0, 10190, 12600, .28], [118.4, 9200, 11800, .2], [121.9, 3700, 9400, .075]], [
  { id: 'g72', type: 'title', text: '72 GÜN', x: 10190, y: 11500, size: 420, t0: 112.84, t1: 113.95, fadeDur: .35 },
  { id: 'g27', type: 'title', text: '2 YIL\n7 AY', x: 10190, y: 11300, size: 400, lh: 1.0, t0: 114.2, t1: 117.8, fadeDur: .5 },
  { id: 'r1', type: 'route', pts: [MED, [38.06, 24.09], [36.5, 25.6], [34.5, 27.6], [32.9, 29.3], [32.55, 29.97], [31.24, 30.04]], t0: 118.6, t1: 119.5 },
  { id: 'misir', type: 'glowdot', ...LL(31.24, 30.04), t0: 118.9, label: 'MISIR', size: 95 },
  { id: 'r2', type: 'route', pts: [[31.24, 30.04], [29.92, 31.2], [25, 33.6], [19, 35.2], [14.51, 35.9]], t0: 119.6, t1: 120.7, dash: true },
  { id: 'malta', type: 'glowdot', ...LL(14.51, 35.9), t0: 119.98, label: 'MALTA', size: 95, square: true },
]);
// 18) pano: 1948, mezar
SC(121.75, 'board', 240000, [[121.2, -200, -300, .6], [124.0, 100, 200, .58], [126.2, 0, 650, .57], [128.2, -120, 1300, .6], [130.0, -120, 1350, .62]], [
  { id: 'yasli', type: 'polaroid', img: 'yasli', crop: [0, 0, 1, .7], x: -250, y: -300, w: 820, rot: -.03, t0: 121.82, name: 'F. TÜRKKAN', nameT: 122.2 },
  { id: 't1948', type: 'tag', x: 420, y: 520, w: 720, rot: .07, t0: 122.58, small: 'DOSYA', big: '1948' },
  { id: 'mezar', type: 'polaroid', img: 'mezar', crop: [0, .3, .62, .7], x: -150, y: 1350, w: 950, rot: .02, t0: 126.08, name: 'AŞİYAN, İSTANBUL', nameT: 126.64 },
  { id: 's8', type: 'thread', from: 't1948', to: 'mezar', t0: 126.9, dur: .7, sag: .1 },
]);
// 19) karanlık: kitabe, son, soru
SC(129.6, 'dark', 260000, [[129.2, 0, -220, .58], [133.4, 0, -150, .6], [137.4, 0, -100, .64], [140.0, 0, 350, .6], [143.9, 0, 450, .6]], [
  { id: 'kitabe', type: 'title', text: '“BİRİNCİ CİHAN\nHARBİNDE\nMEDİNE’NİN\nKAHRAMAN MÜDAFİİ”', x: 0, y: -440, size: 135, lh: 1.25, t0: 129.88, lineT: [129.88, 130.56, 131.32, 132.04], t1: 133.3, fadeDur: .5 },
  { id: 'pasaSon', type: 'halftone', img: 'pasa', crop: [.08, 0, .84, .56], x: 0, y: -150, w: 1150, cols: 70, t0: 133.64, rev: 1.2, glow: [.64, .2] },
  { id: 'emir', type: 'title', text: 'EMİR Mİ?', x: 0, y: 900, size: 190, t0: 138.54 },
  { id: 'medmi', type: 'title', text: 'MEDİNE Mİ?', x: 0, y: 1140, size: 190, t0: 141.34, color: '#f0754e' },
  { id: 'yorum', type: 'band', text: 'YORUMLARA YAZ', x: 0, y: 1430, size: 70, red: true, t0: 143.06 },
]);
const CAMERA = SPACES[0].cam;
const BEATS = [
  [0, ['pasa'], .3], [1.84, ['pasa', 'kaplan'], .3], [3.24, ['tag'], .3], [4.5, ['telgraf', 's1'], .3], [6.2, ['vah', 's2'], .3],
  [8.32, ['med'], .05], [10.46, ['asker'], .2], [12.0, ['asker', 'dusman'], .2], [12.88, ['asker', 'kendi'], .2],
  [15.24, ['pasaP', 'adBand'], .25], [18.2, ['t1934'], .25], [20.14, ['pasaP', 's3'], .25],
  [24.9, ['mudafi'], .45], [25.88, ['med'], .1], [29.08, ['med', 'ring'], .1], [30.24, ['hat', 'xm'], .1],
  [31.62, ['rapor'], .25], [32.96, ['kapi'], .25], [34.62, ['rivayet'], .25], [35.68, ['pasa2', 's4'], .25], [39.78, ['pasa2', 'cekirge'], .25],
  [44.18, ['toplanma'], .2], [49.96, ['yaRes'], .3], [53.22, ['tahliye'], .25], [56.74, ['pasa3', 's5'], .25], [61.44, ['bayrak'], .2],
  [65.12, ['med', 'emanet'], .1], [69.24, ['hat2', 'band2000', 'ist'], .1], [72.48, ['med'], .1],
  [73.66, ['y1918'], .2], [76.0, ['mondros', 'otuz'], .2], [77.88, ['teblig'], .25], [80.88, ['vah2', 's6'], .25], [83.04, ['azil'], .25], [84.34, ['teblig'], .25],
  [85.92, ['kubbe'], .2], [91.2, ['kubbe', 'olma'], .2], [93.16, ['cevap'], .25], [97.76, ['yorgun'], .25], [100.26, ['yorgun', 'ac', 'hasta', 'yorgunB'], .25], [102.7, ['pasa4', 's7'], .25],
  [106.26, ['subaylar', 'tarih'], .2], [110.16, ['subaylar', 'esir'], .2],
  [111.48, ['g72', 'g27', 'med'], .45], [118.6, ['r1', 'r2', 'misir', 'malta', 'med'], .05],
  [121.82, ['yasli'], .25], [122.58, ['t1948'], .25], [126.08, ['mezar', 's8'], .25],
  [129.88, ['kitabe'], .2], [133.64, ['pasaSon'], .2], [137.76, ['emir', 'medmi', 'yorum'], .25],
].map(([t, hero, mapDim]) => ({ t, hero, mapDim }));
const TIMELINE = { t0: .6, t1: 121.0, years: [1916, 1917, 1918, 1919, 1920], keys: [{ t: 0, v: 1916.45 }, { t: 3.24, v: 1918.83, dur: 1.3 }, { t: 10.46, v: 1919.03, dur: 1.0 }, { t: 25.88, v: 1916.45, dur: 1.4 }, { t: 53.22, v: 1918.5, dur: 1.3 }, { t: 73.66, v: 1918.83, dur: 1.0 }, { t: 106.26, v: 1919.03, dur: 1.0 }] };
