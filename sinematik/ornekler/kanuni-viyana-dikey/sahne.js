// Demo (dikey): Kanuni'nin seferleri ve Viyana · 9:16 · 1080x1920 · 30 fps · 15 sn
const FORMAT = { w: 1080, h: 1920, fps: 30, dur: 14.964 };
const LOOK = { tilt: 38, fov: 55, dof: 1.0, focusY: .55, light: [.22, .16], lightPower: .6, bloom: .35, grain: .07, vignette: .65, warm: .08 };
const CANDLE = true;
const WORLD = { lon0: 8, lat0: 52, k: 600, latc: 43, lonMin: 4, lonMax: 40, latMin: 28, latMax: 58, map: { x: -1756, y: -3600, w: 15797, h: 18000 } };
const IMAGES = { kanuni: 'img/kanuni.jpg', meldeman: 'img/meldeman.jpg' };
const P = { ist: [28.97, 41.01], bel: [20.46, 44.82], rod: [28.22, 36.43], moh: [18.68, 45.99], buda: [19.04, 47.5], vie: [16.37, 48.21] };
function havaFx(ctx, t, x, y, w, h) {
  const yag = smooth((t - 13.3) / .5) * (1 - smooth((t - 14.0) / .5)), kar = smooth((t - 14.0) / .5); if (yag + kar <= 0) return;
  ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); ctx.fillStyle = `rgba(25,35,55,${.4 * Math.max(yag, kar)})`; ctx.fillRect(x, y, w, h); const R = rng(5);
  if (yag > 0) { ctx.strokeStyle = `rgba(235,242,255,${yag})`; ctx.lineWidth = 6; ctx.beginPath(); for (let i = 0; i < 420; i++) { const px = x + R() * w * 1.2, sp = .8 + R() * .5, py = y + ((R() * h + t * 2600 * sp) % (h + 160)) - 80; ctx.moveTo(px, py); ctx.lineTo(px - 26, py + 120); } ctx.stroke(); }
  if (kar > 0) { ctx.fillStyle = `rgba(255,255,255,${.85 * kar})`; for (let i = 0; i < 240; i++) { const r = 4 + R() * 8, px = x + ((R() * w + Math.sin(t * 1.3 + i) * 40) % w), py = y + ((R() * h + t * (90 + R() * 80)) % h); ctx.beginPath(); ctx.arc(px, py, r, 0, TAU); ctx.fill(); } }
  ctx.restore();
}
const OBJECTS = [
  { id: 'pusula', type: 'compass', x: 11250, y: 7250, r: 330, rot: .5 },
  { id: 'c_ist', type: 'city', lon: P.ist[0], lat: P.ist[1], t0: -1 },
  { id: 'kanuni', type: 'print', img: 'kanuni', x: 10150, y: 6150, w: 1100, rot: -.05, t0: -1, caption: 'Kanuni Sultan Süleyman' },
  { id: 'r1', type: 'route', pts: [P.ist, [26.56, 41.68], [23.32, 42.7], [21.9, 43.32], P.bel], curve: true, t0: 3.85, t1: 4.6 },
  { id: 'c_bel', type: 'city', lon: P.bel[0], lat: P.bel[1], t0: 4.5 },
  { id: 'f_bel', type: 'flag', lon: P.bel[0], lat: P.bel[1], t0: 4.57 },
  { id: 'belgrad', type: 'label', text: 'BELGRAD', sub: '1521', lon: P.bel[0], lat: P.bel[1], dx: 0, dy: 380, size: 380, subSize: 280, align: 'center', t0: 4.17, subT: 4.55 },
  { id: 'r2', type: 'route', pts: [P.ist, [26.4, 40.2], [26.1, 39.0], [26.9, 37.6], P.rod], curve: true, t0: 5.5, t1: 6.3, dash: [60, 46] },
  { id: 'c_rod', type: 'city', lon: P.rod[0], lat: P.rod[1], t0: 6.2, r: 40 },
  { id: 'f_rod', type: 'flag', lon: P.rod[0], lat: P.rod[1], t0: 6.25, s: 1.6 },
  { id: 'rodos', type: 'label', text: 'RODOS', sub: '1522', lon: P.rod[0], lat: P.rod[1], dx: 0, dy: 900, size: 950, subSize: 620, align: 'center', t0: 5.74, subT: 6.05 },
  { id: 'r3', type: 'route', pts: [P.bel, [19.9, 45.3], P.moh], curve: true, t0: 6.75, t1: 7.3 },
  { id: 'c_moh', type: 'city', lon: P.moh[0], lat: P.moh[1], t0: 7.2 },
  { id: 'f_moh', type: 'flag', lon: P.moh[0], lat: P.moh[1], t0: 7.25 },
  { id: 'mohac', type: 'label', text: 'MOHAÇ', sub: '1526', lon: P.moh[0], lat: P.moh[1], dx: 0, dy: -620, size: 380, subSize: 280, align: 'center', t0: 6.72, subT: 7.2 },
  { id: 'saat', type: 'label', text: '2 SAAT', lon: P.moh[0], lat: P.moh[1], dx: 0, dy: 640, size: 320, color: '#9a1c14', align: 'center', t0: 8.13 },
  { id: 'circ', type: 'circle', lon: P.moh[0], lat: P.moh[1], rx: 150, ry: 115, t0: 8.98, dur: .55 },
  { id: 'r4', type: 'route', pts: [P.moh, [18.9, 46.8], P.buda, [18.2, 47.75], [17.2, 48.0], P.vie], curve: true, t0: 10.3, t1: 11.3, glow: '#ffae4a', width: 18 },
  { id: 'c_vie', type: 'city', lon: P.vie[0], lat: P.vie[1], t0: 11.2, r: 40 },
  { id: 'viyana', type: 'label', text: 'VİYANA', sub: '1529', lon: P.vie[0], lat: P.vie[1], dx: 0, dy: 600, size: 540, subSize: 380, align: 'center', style: 'glow', t0: 10.9, subT: 11.1 },
  { id: 'meldeman', type: 'print', img: 'meldeman', x: 2300, y: 2900, w: 1500, rot: .035, t0: 12.55, dur: .8, fx: havaFx, tone: 'rgba(150,110,60,.16)' },
  { id: 'lup', type: 'magnifier', r: 270, mag: 1.6, handle: .7, t0: 6.9, path: [[6.9, 5900, 4400], [8.2, 4686, 3606], [10.2, 4700, 3600], [11.4, 6300, 3300]] },
];
const CAMERA = [
  { t: 0.0, x: 10120, y: 6250, z: .74, tilt: 22 },
  { t: 1.6, x: 9900, y: 6200, z: .48, tilt: 30 },
  { t: 2.9, x: 8300, y: 5800, z: .22, tilt: 40 },
  { t: 3.85, x: 6600, y: 5000, z: .21 },
  { t: 4.6, x: 5550, y: 4550, z: .4 },
  { t: 5.4, x: 5750, y: 4950, z: .34 },
  { t: 6.25, x: 7650, y: 8200, z: .16, tilt: 40 },
  { t: 6.95, x: 5600, y: 5300, z: .19 },
  { t: 7.75, x: 4690, y: 3750, z: .38 },
  { t: 9.1, x: 4686, y: 3680, z: .44 },
  { t: 10.25, x: 4500, y: 3450, z: .38 },
  { t: 11.1, x: 3700, y: 2700, z: .3 },
  { t: 12.0, x: 3050, y: 2750, z: .33 },
  { t: 13.1, x: 2380, y: 2930, z: .52, tilt: 28 },
  { t: 14.964, x: 2320, y: 2930, z: .68, tilt: 22 },
];
const BEATS = [
  { t: 0, hero: ['kanuni', 'c_ist', 'pusula'], mapDim: .3 },
  { t: 3.85, hero: ['r1', 'c_bel', 'f_bel', 'belgrad', 'c_ist'], mapDim: .12 },
  { t: 5.56, hero: ['r2', 'c_rod', 'f_rod', 'rodos', 'c_ist'], mapDim: .12 },
  { t: 6.72, hero: ['r3', 'c_moh', 'f_moh', 'mohac', 'saat', 'circ'], mapDim: .12 },
  { t: 10.3, hero: ['r4', 'c_vie', 'viyana'], mapDim: .12 },
  { t: 12.57, hero: ['meldeman'], mapDim: .6 },
];
