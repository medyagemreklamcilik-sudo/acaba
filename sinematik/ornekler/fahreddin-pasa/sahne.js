// Fahreddin Paşa · Çöl Kaplanı — ilk 10 sn demo · 9:16 · 1080x1920 · 30 fps
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 10.4 };
const WORLD = { lon0: 20, lat0: 46, k: 600, latc: 30, lonMin: 22, lonMax: 50, latMin: 14, latMax: 44 };
WORLD.map = { x: 1039, y: 1200, w: 14549, h: 18000 };
const IMAGES = { pasa: 'img/pasa.jpg', agamemnon: 'img/agamemnon.jpg', vahdettin: 'img/vahdettin.jpg', medine: 'img/medine.jpg' };
const P = { med: [39.61, 24.47], ist: [28.97, 41.01], lim: [25.25, 39.9] };
const OBJECTS = [
  { id: 'c_med', type: 'city', lon: P.med[0], lat: P.med[1], t0: -1, r: 40 },
  { id: 'emir', type: 'route', pts: [P.ist, [30.5, 39.0], [33.5, 36.0], [36.2, 32.5], [38.3, 28.5], P.med], t0: 4.5, t1: 5.8, dash: [70, 50], width: 26 },
  { id: 'pasa', type: 'print', img: 'pasa', x: 11450, y: 12050, w: 1000, rot: -.04, t0: -1 },
  { id: 'kaplan', type: 'label', text: 'ÇÖL KAPLANI', x: 11450, y: 13420, size: 190, align: 'center', color: '#5a1408', t0: 1.84, dur: .6 },
  { id: 'agamemnon', type: 'print', img: 'agamemnon', x: 9950, y: 10450, w: 1000, rot: .05, t0: 3.3, dur: .8 },
  { id: 'mondros', type: 'label', text: 'MONDROS', sub: '30 EKİM 1918', x: 9950, y: 11220, size: 190, subSize: 150, align: 'center', t0: 3.56, subT: 3.85 },
  { id: 'vahdettin', type: 'print', img: 'vahdettin', x: 11350, y: 9750, w: 850, rot: -.05, t0: 6.2, dur: .8 },
  { id: 'vahLbl', type: 'label', text: 'VAHDETTİN', x: 11350, y: 10850, size: 170, align: 'center', t0: 6.45 },
  { id: 'medineFoto', type: 'print', img: 'medine', x: 10150, y: 13850, w: 1150, rot: .04, t0: 8.7, dur: .8 },
  { id: 'circ', type: 'circle', lon: P.med[0], lat: P.med[1], rx: 210, ry: 170, t0: 9.86, dur: .5 },
  { id: 'lblMed', type: 'label', text: 'MEDİNE', lon: P.med[0], lat: P.med[1], dx: 0, dy: -250, size: 210, align: 'center', t0: 9.0 },
];
const CAMERA = [
  { t: 0.0, x: 11450, y: 12050, z: .8 },
  { t: 1.8, x: 11430, y: 12300, z: .64 },
  { t: 2.7, x: 11300, y: 12350, z: .6 },
  { t: 3.5, x: 10650, y: 11400, z: .5 },
  { t: 4.4, x: 10050, y: 10850, z: .46 },
  { t: 5.6, x: 10500, y: 10500, z: .4 },
  { t: 6.8, x: 11250, y: 10250, z: .46 },
  { t: 7.8, x: 11150, y: 10500, z: .44 },
  { t: 9.2, x: 10300, y: 12250, z: .46 },
  { t: 10.4, x: 10220, y: 12550, z: .5 },
];
const BEATS = [
  { t: 0, hero: ['pasa', 'kaplan'], mapDim: .3 },
  { t: 3.24, hero: ['agamemnon', 'mondros'], mapDim: .2 },
  { t: 4.5, hero: ['emir', 'c_med'], mapDim: .1 },
  { t: 6.2, hero: ['vahdettin', 'vahLbl'], mapDim: .25 },
  { t: 8.32, hero: ['medineFoto', 'c_med', 'circ', 'lblMed'], mapDim: .2 },
];
