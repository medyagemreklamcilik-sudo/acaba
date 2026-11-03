// Kanuni'nin Viyana Seferi · belgesel demo · 9:16 · 1080x1920 · 30 fps · 18,9 sn
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 18.94 };
const LOOK = { tilt: 42, fov: 55, dof: 1.25, focusY: .55, light: [.2, .12], lightPower: .62, bloom: .42, grain: .075, vignette: .7, warm: .07, teal: .38 };
const CANDLE = true;
const WORLD = { lon0: 8, lat0: 52, k: 600, latc: 43, lonMin: 2, lonMax: 42, latMin: 26, latMax: 60, map: { x: -2632, y: -4800, w: 20188, h: 20400 } };
const IMAGES = { kanuni: 'img/kanuni.jpg' };
const C_ = { ist: [28.97, 41.01], edi: [26.56, 41.68], nis: [21.9, 43.32], bel: [20.46, 44.82], buda: [19.04, 47.5], vie: [16.37, 48.21] };
const AP = [[-1, 28.97, 41.01], [2.6, 28.75, 41.12], [4.7, 23.2, 42.75], [6.9, 21.5, 44.05], [8.6, 20.25, 45.2], [11.4, 19.05, 47.3], [12.6, 17.35, 47.95], [18.0, 17.35, 47.95], [18.94, 17.75, 47.7]];
const TUNA = [[20.5, 44.843], [20.353, 44.911], [20.339, 45.038], [20.253, 45.15], [20.045, 45.186], [19.907, 45.259], [19.699, 45.233], [19.475, 45.243], [19.273, 45.278], [19.093, 45.337], [19.005, 45.4], [19.033, 45.502], [18.954, 45.558], [18.894, 45.767], [18.759, 45.935], [18.748, 46.063], [18.859, 46.151], [18.916, 46.271], [18.919, 46.423], [18.874, 46.586], [18.966, 46.685], [18.945, 46.804], [18.928, 47.083], [18.907, 47.26], [18.959, 47.365], [19.06, 47.481]];
const SLOMO = [[9.2, 11.4, .35], [16.72, 18.94, .45]];
const WEATHER = [{ type: 'rain', t0: 8.7, t1: 12.2, power: 1 }, { type: 'snow', t0: 16.5, t1: 19.5, power: 1 }];
const FLASHES = [9.22, 10.7];
const RAYS = t => .9 * (1 - smooth((t - 7.6) / .8)) + .7 * smooth((t - 12.6) / 1.2);
const DARKEN = t => .1 * smooth((t - 8.4) / .6) * (1 - smooth((t - 12.0) / .8)) + .06 * smooth((t - 16.5) / 1);
const OBJECTS = [
  { id: 'kanuni', type: 'print', img: 'kanuni', x: 9900, y: 7400, w: 900, rot: -.07, t0: -1, caption: 'Kanuni Sultan Süleyman' },
  // ordunun ardında akan ışık izi (ordu ile aynı duraklar, aynı zamanlama)
  ...AP.slice(1, 7).map((p, i) => ({ id: 'iz' + i, type: 'route', pts: [[AP[i + 1][1], AP[i + 1][2]], [AP[i + 2][1], AP[i + 2][2]]], t0: AP[i + 1][0], t1: AP[i + 2][0], glow: '#ffae4a', width: 14 })).slice(0, 5),
  { id: 'tunaYazi', type: 'label', text: 'TUNA', lon: 19.55, lat: 45.3, dx: 0, dy: 520, size: 380, align: 'center', style: 'glow', t0: 4.9 },
  { id: 'vieYazi', type: 'label', text: 'VİYANA', sub: '1529', lon: C_.vie[0], lat: C_.vie[1], dx: 0, dy: 760, size: 430, subSize: 300, align: 'center', style: 'glow', t0: 13.0, subT: 13.3 },
  { id: 'ordu', type: 'army', team: 'osm', rows: 4, cols: 5, gap: 175, S: 250, king: true, kingHide: 15.32, t0: -.25, path: AP, ring: { t: 12.9, dur: 1.0, lon: C_.vie[0], lat: C_.vie[1], r: 560 }, unring: 17.6, anchor(t) { const c = pathPt(AP, t); return [c.x, c.y]; } },
  { id: 'filo', type: 'fleet', team: 'osm', route: TUNA, t0: 4.75, t1: 8.6, s0: .12, s1: .66, n: 4, spacing: .07, S: 520, side: 0, anchor(t) { return proj(19.9, 45.25); } },
  { id: 'toplar', type: 'cannons', lon: 21.0, lat: 45.85, n: 3, S: 330, t0: 7.9, sink: [10.68, 11.5] },
  { id: 'viyana', type: 'citadel', lon: C_.vie[0], lat: C_.vie[1], R: 380, H: 130, t0: 11.6 },
  { id: 'duman1', type: 'smoke', lon: 16.15, lat: 48.0, S: 420, t0: 13.42, n: 2, spread: 300 },
  { id: 'duman2', type: 'smoke', lon: 16.8, lat: 48.35, S: 360, t0: 13.7, n: 2, spread: 260 },
  { id: 'kral', type: 'king', team: 'osm', S: 620, t0: 15.32, path: [[15.3, 17.08, 47.78], [18.0, 17.08, 47.78], [18.94, 17.38, 47.62]], anchor(t) { const c = pathPt(this.path, t); return [c.x, c.y + 400]; } },
  { id: 'yuzbin', type: 'title', text: '100.000+', y: .19, size: 168, t0: 1.3, t1: 3.9 },
];
const CAMERA = [
  { t: 0.0, x: 9480, y: 6950, z: .56, tilt: 50 },
  { t: 1.3, x: 9380, y: 6880, z: .5, tilt: 48 },
  { t: 2.6, x: 8800, y: 6500, z: .36, tilt: 46 },
  { t: 3.9, x: 7400, y: 5850, z: .22, tilt: 44 },
  { t: 4.9, x: 5900, y: 4700, z: .3, tilt: 42 },
  { t: 6.5, x: 5350, y: 4150, z: .46, tilt: 40 },
  { t: 8.0, x: 5600, y: 3980, z: .36, tilt: 42 },
  { t: 9.2, x: 5720, y: 3730, z: .52, tilt: 48 },
  { t: 11.2, x: 5700, y: 3690, z: .6, tilt: 50 },
  { t: 12.14, x: 4600, y: 3150, z: .27, tilt: 44 },
  { t: 13.0, x: 3720, y: 2520, z: .34, tilt: 40 },
  { t: 14.4, x: 3700, y: 2480, z: .4, tilt: 38 },
  { t: 15.4, x: 3860, y: 2560, z: .5, tilt: 44 },
  { t: 16.8, x: 3990, y: 2620, z: .74, tilt: 52 },
  { t: 18.94, x: 4090, y: 2640, z: .82, tilt: 54 },
];
const BEATS = [
  { t: 0, hero: ['ordu', 'kanuni', 'yuzbin', 'iz0', 'iz1'], mapDim: .18 },
  { t: 4.9, hero: ['filo', 'tunaYazi'], mapDim: .14 },
  { t: 8.04, hero: ['toplar'], mapDim: .28 },
  { t: 12.14, hero: ['viyana', 'ordu', 'duman1', 'duman2', 'vieYazi', 'iz4'], mapDim: .14 },
  { t: 15.32, hero: ['kral'], mapDim: .55 },
];
