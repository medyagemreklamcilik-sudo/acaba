// Fahreddin Paşa, "dosya" stili demo (ilk 15 sn). Kelime zamanları build/aligned.json'dan.
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 15.1 };
const WORLD = { lon0: 20, lat0: 46, k: 600, latc: 30 };
const IMAGES = { pasa: 'img/pasa.jpg', vahdettin: 'img/vahdettin.jpg', askerler: 'img/askerler.jpg' };
const BOARDS = [{ x: 8850, y: 9900, w: 2700, h: 2300 }];
const OBJECTS = [
  { id: 'pasa', type: 'halftone', img: 'pasa', crop: [.08, 0, .84, .56], x: 10190, y: 8300, w: 1150, cols: 70, t0: -.35, rev: 1.3, glow: [.64, .2] },
  { id: 'kaplan', type: 'title', text: 'ÇÖL\nKAPLANI', x: 10190, y: 9330, size: 300, lh: 1.0, rule: 420, t0: 1.84 },
  { id: 'tag', type: 'tag', x: 9560, y: 10300, w: 720, rot: -.07, t0: 3.24, small: 'DOSYA', big: '1918', sub: 'MONDROS' },
  { id: 'telgraf', type: 'doc', x: 10560, y: 10700, w: 1000, h: 1350, rot: .03, t0: 4.45, seed: 8, head: ['TELGRAF', 'HARBİYE NEZARETİ', 'MEDİNE MUHAFIZINA'], rowsBefore: 4, redact: [1, 102], key: 'TESLİM OLUNUZ.', keySize: 82, keyT: 4.62, keyDur: .7, circleT: 4.95, rowsAfter: 6 },
  { id: 'vah', type: 'polaroid', img: 'vahdettin', crop: [.12, .02, .76, .5], x: 9650, y: 11300, w: 720, rot: -.04, t0: 6.2, name: 'VAHDETTİN', nameT: 6.5 },
  { id: 's1', type: 'thread', from: 'tag', to: 'telgraf', t0: 4.75, dur: .7, sag: .12 },
  { id: 's2', type: 'thread', from: 'vah', to: 'telgraf', t0: 6.95, dur: .7, sag: .1 },
  { id: 'med', type: 'glowdot', lon: 39.61, lat: 24.47, t0: 8.45, label: 'MEDİNE', size: 170, square: true, crossT: 9.86 },
  { id: 'asker', type: 'polaroid', img: 'askerler', x: 10190, y: 14250, w: 1300, rot: -.02, t0: 10.5, dur: .8, brackets: { t: 13.98, r: [.02, .22, .5, .72] } },
  { id: 'dusman', type: 'strike', text: 'DÜŞMAN', x: 10190, y: 13560, size: 170, t0: 12.0, tStrike: 12.5 },
  { id: 'kendi', type: 'title', text: 'KENDİ\nASKERLERİ', x: 10190, y: 15000, size: 230, lh: 1.02, t0: 12.88 },
];
const CAMERA = [
  { t: 0, x: 10190, y: 8250, z: .68 }, { t: 1.7, x: 10190, y: 8450, z: .63 }, { t: 2.4, x: 10180, y: 8850, z: .58 },
  { t: 4.4, x: 10080, y: 10200, z: .56 }, { t: 5.5, x: 10500, y: 10600, z: .72 }, { t: 6.5, x: 10020, y: 10900, z: .6 },
  { t: 9.1, x: 10190, y: 12350, z: .48 }, { t: 10.7, x: 10190, y: 13350, z: .52 }, { t: 12.7, x: 10190, y: 14050, z: .54 }, { t: 15.1, x: 10190, y: 14330, z: .56 },
];
const BEATS = [
  { t: 0, hero: ['pasa'], mapDim: .82 }, { t: 1.84, hero: ['pasa', 'kaplan'], mapDim: .8 },
  { t: 3.24, hero: ['tag'], mapDim: .3 }, { t: 4.5, hero: ['telgraf', 's1'], mapDim: .3 }, { t: 6.2, hero: ['vah', 's2'], mapDim: .3 },
  { t: 8.32, hero: ['med'], mapDim: .05 }, { t: 10.46, hero: ['asker'], mapDim: .35 }, { t: 12.0, hero: ['asker', 'dusman'], mapDim: .4 },
  { t: 12.88, hero: ['asker', 'kendi'], mapDim: .45 },
];
const TIMELINE = { t0: .6, years: [1916, 1917, 1918, 1919, 1920], keys: [{ t: 0, v: 1916.45 }, { t: 3.24, v: 1918.83, dur: 1.3 }, { t: 10.46, v: 1919.03, dur: 1.0 }] };
