// Demo: Kanuni'nin seferleri ve Viyana (15 sn, 21:9, 3840x1646, 30 fps)
const FORMAT = { w: 3840, h: 1646, fps: 30, dur: 14.964 };
const WORLD = { lon0: 8, lat0: 52, k: 600, latc: 43, lonMin: 10, lonMax: 33, latMin: 34, latMax: 51 };
WORLD.map = { x: 877, y: 600, w: 11409, h: 10200 }; WORLD.lonMax = 36;
const IMAGES = { kanuni: 'img/kanuni.jpg', meldeman: 'img/meldeman.jpg' };
const P = { ist: [28.97, 41.01], bel: [20.46, 44.82], rod: [28.22, 36.43], moh: [18.68, 45.99], buda: [19.04, 47.5], vie: [16.37, 48.21] };

function havaFx(ctx, t, x, y, w, h) { // Viyana baskısının üstünde yağmur, sonra kar
  const yag = smooth((t - 13.3) / .5) * (1 - smooth((t - 14.0) / .5)), kar = smooth((t - 14.0) / .5);
  if (yag + kar <= 0) return;
  ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip();
  ctx.fillStyle = `rgba(25,35,55,${.4 * Math.max(yag, kar)})`; ctx.fillRect(x, y, w, h);
  const R = rng(5);
  if (yag > 0) { ctx.strokeStyle = `rgba(235,242,255,${yag})`; ctx.lineWidth = 6; ctx.beginPath(); for (let i = 0; i < 420; i++) { const px = x + R() * w * 1.2, sp = .8 + R() * .5, py = y + ((R() * h + t * 2600 * sp) % (h + 160)) - 80; ctx.moveTo(px, py); ctx.lineTo(px - 26, py + 120); } ctx.stroke(); }
  if (kar > 0) { ctx.fillStyle = `rgba(255,255,255,${.85 * kar})`; for (let i = 0; i < 220; i++) { const r = 3 + R() * 7, px = x + ((R() * w + Math.sin(t * 1.3 + i) * 40) % w), py = y + ((R() * h + t * (90 + R() * 80)) % h); ctx.beginPath(); ctx.arc(px, py, r, 0, TAU); ctx.fill(); } }
  ctx.restore();
}

const pr = (lo, la) => proj(lo, la);
const OBJECTS = [
  { id: 'c_ist', type: 'city', lon: P.ist[0], lat: P.ist[1], t0: -1 },
  { id: 'kanuni', type: 'print', img: 'kanuni', x: 10150, y: 6150, w: 1100, rot: -.05, t0: -1, caption: 'Kanuni Sultan Süleyman' },
  { id: 'r1', type: 'route', pts: [P.ist, [26.56, 41.68], [23.32, 42.7], [21.9, 43.32], P.bel], t0: 3.85, t1: 4.6 },
  { id: 'c_bel', type: 'city', lon: P.bel[0], lat: P.bel[1], t0: 4.5 },
  { id: 'belgrad', type: 'label', text: 'BELGRAD', sub: '1521', lon: P.bel[0], lat: P.bel[1], dx: 90, dy: -70, size: 300, subSize: 230, t0: 4.17, subT: 4.55 },
  { id: 'r2', type: 'route', pts: [P.ist, [26.4, 40.2], [26.1, 39.0], [26.9, 37.6], P.rod], t0: 5.5, t1: 6.3, dash: [60, 46] },
  { id: 'c_rod', type: 'city', lon: P.rod[0], lat: P.rod[1], t0: 6.2, r: 34 },
  { id: 'rodos', type: 'label', text: 'RODOS', sub: '1522', lon: P.rod[0], lat: P.rod[1], dx: -200, dy: -150, size: 620, subSize: 380, align: 'right', t0: 5.74, subT: 6.05 },
  { id: 'r3', type: 'route', pts: [P.bel, [19.9, 45.3], P.moh], t0: 6.75, t1: 7.4 },
  { id: 'c_moh', type: 'city', lon: P.moh[0], lat: P.moh[1], t0: 7.3 },
  { id: 'mohac', type: 'label', text: 'MOHAÇ', sub: '1526', lon: P.moh[0], lat: P.moh[1], dx: -300, dy: -90, size: 300, subSize: 230, align: 'right', t0: 6.72, subT: 7.2 },
  { id: 'saat', type: 'label', text: '2 SAAT', lon: P.moh[0], lat: P.moh[1], dx: -300, dy: 490, size: 230, color: '#9a1c14', align: 'right', t0: 8.13 },
  { id: 'circ', type: 'circle', lon: P.moh[0], lat: P.moh[1], rx: 260, ry: 200, t0: 8.98, dur: .55 },
  { id: 'r4', type: 'route', pts: [P.moh, P.buda, [17.9, 47.85], P.vie], t0: 10.3, t1: 11.3 },
  { id: 'c_vie', type: 'city', lon: P.vie[0], lat: P.vie[1], t0: 11.2, r: 34 },
  { id: 'viyana', type: 'label', text: 'VİYANA', sub: '1529', lon: P.vie[0], lat: P.vie[1], dx: 110, dy: -60, size: 340, subSize: 240, t0: 10.9, subT: 11.1 },
  { id: 'meldeman', type: 'print', img: 'meldeman', x: 2350, y: 2750, w: 1500, rot: .035, t0: 12.55, dur: .8, fx: havaFx, tone: 'rgba(150,110,60,.16)' },
];
const CAMERA = [
  { t: 0.0, x: 10150, y: 6120, z: 1.12 },
  { t: 1.6, x: 9900, y: 6200, z: .78 },
  { t: 2.9, x: 8300, y: 5800, z: .42 },
  { t: 3.85, x: 6700, y: 4950, z: .38 },
  { t: 4.6, x: 5750, y: 4300, z: .6 },
  { t: 5.4, x: 5950, y: 4750, z: .52 },
  { t: 6.25, x: 7150, y: 6950, z: .26 },
  { t: 6.95, x: 5600, y: 5000, z: .29 },
  { t: 7.75, x: 4600, y: 3650, z: .6 },
  { t: 9.1, x: 4620, y: 3620, z: .68 },
  { t: 10.25, x: 4450, y: 3250, z: .62 },
  { t: 11.1, x: 3800, y: 2450, z: .5 },
  { t: 12.0, x: 3150, y: 2550, z: .5 },
  { t: 13.1, x: 2520, y: 2720, z: .78 },
  { t: 14.964, x: 2370, y: 2740, z: 1.0 },
];
const BEATS = [
  { t: 0, hero: ['kanuni', 'c_ist'], mapDim: .3 },
  { t: 3.85, hero: ['r1', 'c_bel', 'belgrad', 'c_ist'], mapDim: .12 },
  { t: 5.56, hero: ['r2', 'c_rod', 'rodos', 'c_ist'], mapDim: .12 },
  { t: 6.72, hero: ['r3', 'c_moh', 'mohac', 'saat', 'circ'], mapDim: .12 },
  { t: 10.3, hero: ['r4', 'c_vie', 'viyana'], mapDim: .12 },
  { t: 12.57, hero: ['meldeman'], mapDim: .6 },
];
