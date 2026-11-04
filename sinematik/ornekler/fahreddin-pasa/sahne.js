// Fahreddin Paşa · Çöl Kaplanı — ilk 10 sn demo · 9:16 · 1080x1920 · 30 fps
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 10.4 };
const WORLD = { lon0: 20, lat0: 46, k: 600, latc: 30, lonMin: 22, lonMax: 50, latMin: 14, latMax: 44 };
WORLD.map = { x: 1039, y: 1200, w: 14549, h: 18000 };
const IMAGES = { pasa: 'img/pasa.jpg', agamemnon: 'img/agamemnon.jpg', vahdettin: 'img/vahdettin.jpg', medine: 'img/medine.jpg' };
const P = { med: [39.61, 24.47], ist: [28.97, 41.01], lim: [25.25, 39.9] };
const OBJECTS = [
  { id: 'c_med', type: 'city', lon: P.med[0], lat: P.med[1], t0: -1, r: 40 },
  { id: 'c_ist', type: 'city', lon: P.ist[0], lat: P.ist[1], t0: -1, r: 40 },
  { id: 'pasa', type: 'print', img: 'pasa', x: 11250, y: 11000, w: 1000, rot: -.04, t0: -1 },
  { id: 'kaplan', type: 'label', text: 'ÇÖL KAPLANI', x: 11250, y: 12330, size: 190, align: 'center', color: '#5a1408', t0: 1.84, dur: .6 },
  { id: 'agamemnon', type: 'print', img: 'agamemnon', x: 3500, y: 4350, w: 1350, rot: .05, t0: 3.3, dur: .7 },
  { id: 'mondros', type: 'label', text: 'MONDROS', sub: '30 EKİM 1918', x: 3500, y: 5300, size: 200, subSize: 140, align: 'center', t0: 3.56, subT: 3.8 },
  { id: 'emir', type: 'route', pts: [P.ist, [30.5, 39.0], [33.5, 36.0], [36.2, 32.5], [38.3, 28.5], P.med], t0: 4.5, t1: 5.6, dash: [70, 50], width: 26 },
  { id: 'vahdettin', type: 'print', img: 'vahdettin', x: 6200, y: 2700, w: 1000, rot: -.05, t0: 6.2, dur: .7 },
  { id: 'vahLbl', type: 'label', text: 'VAHDETTİN', x: 6200, y: 3780, size: 170, align: 'center', t0: 6.4 },
  { id: 'medineFoto', type: 'print', img: 'medine', x: 10150, y: 13850, w: 1150, rot: .04, t0: 8.7, dur: .7 },
  { id: 'circ', type: 'circle', lon: P.med[0], lat: P.med[1], rx: 210, ry: 170, t0: 9.86, dur: .5 },
  { id: 'lblMed', type: 'label', text: 'MEDİNE', lon: P.med[0], lat: P.med[1], dx: 0, dy: -250, size: 210, align: 'center', t0: 9.0 },
];
const CAMERA = [
  { t: 0.0, x: 11250, y: 11000, z: .84 },
  { t: 1.8, x: 11240, y: 11400, z: .66 },
  { t: 3.0, x: 11000, y: 11200, z: .5 },
  { t: 4.3, x: 3600, y: 4600, z: .44 },
  { t: 5.6, x: 7300, y: 8150, z: .16 },
  { t: 6.8, x: 5800, y: 3100, z: .42 },
  { t: 7.5, x: 6000, y: 3500, z: .34 },
  { t: 9.1, x: 10150, y: 13450, z: .5 },
  { t: 10.4, x: 10170, y: 13380, z: .56 },
];
const BEATS = [
  { t: 0, hero: ['pasa', 'kaplan'], mapDim: .3 },
  { t: 3.24, hero: ['agamemnon', 'mondros'], mapDim: .2 },
  { t: 4.5, hero: ['emir', 'c_ist', 'c_med'], mapDim: .1 },
  { t: 6.2, hero: ['vahdettin', 'vahLbl', 'c_ist'], mapDim: .25 },
  { t: 8.32, hero: ['medineFoto', 'c_med', 'circ', 'lblMed'], mapDim: .2 },
];
