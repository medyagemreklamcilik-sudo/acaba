// Belgesel modülü (core.js'ten sonra yüklenir): satranç taşı ordular, gemiler, toplar, minyatür kale,
// duman/ateş, ekran yağmuru/karı, ışık huzmeleri, toz, slow motion.
'use strict';
// ---------------- slow motion: SLOMO = [[t0, t1, hız], ...]  → animasyon zamanı ----------------
function rateAt(t) { let r = 1; for (const [a, b, k] of (typeof SLOMO !== 'undefined' ? SLOMO : [])) { const e = .35, u = smooth((t - a) / e) * (1 - smooth((t - b) / e)); r = Math.min(r, lerp(1, k, u)); } return r; }
const _AT = []; (function () { let a = 0; for (let i = 0; i <= Math.ceil(FORMAT.dur * 120) + 240; i++) { _AT.push(a); a += rateAt(i / 120) / 120; } })();
function animT(t) { const i = t * 120, j = Math.max(0, Math.min(_AT.length - 2, Math.floor(i))); return lerp(_AT[j], _AT[j + 1], i - j); }

const tmp = document.createElement('canvas'); tmp.width = W / 2; tmp.height = H / 2; const tctx = tmp.getContext('2d');
const tmp2 = document.createElement('canvas'); tmp2.width = W / 2; tmp2.height = H / 2; const t2 = tmp2.getContext('2d');
function withDof(ctx, info, k, draw) { // derinliğe göre bulanıklık: yarım çözünürlükte çiz + bulanıklaştır (hızlı)
  const b = info.dofPx(k); if (b < 1.2) { draw(ctx); return; }
  tctx.setTransform(.5, 0, 0, .5, 0, 0); tctx.clearRect(0, 0, W, H); draw(tctx);
  t2.setTransform(1, 0, 0, 1, 0, 0); t2.clearRect(0, 0, W / 2, H / 2); t2.filter = `blur(${(b / 2).toFixed(1)}px)`; t2.drawImage(tmp, 0, 0); t2.filter = 'none';
  ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.imageSmoothingQuality = 'high'; ctx.drawImage(tmp2, 0, 0, W, H); ctx.restore();
}
const SOFT = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const g = c.getContext('2d'), gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(.5, 'rgba(255,255,255,.5)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); return c; })();
const TEAM = {
  osm: { lit: '#d4473a', mid: '#8e1a14', dark: '#2c0605', trim: '#d9a84a', spec: 'rgba(255,220,200,.55)' },
  hab: { lit: '#fbf6ea', mid: '#cfc5ae', dark: '#6e6352', trim: '#a8a090', spec: 'rgba(255,255,255,.7)' },
  bronz: { lit: '#e2b060', mid: '#9a6a28', dark: '#3a2408', trim: '#f0d08a', spec: 'rgba(255,240,200,.6)' },
};
// profil: [yükseklik oranı, yarı genişlik oranı]
const PROF = {
  pawn: [[0, .42], [.06, .42], [.09, .36], [.14, .3], [.19, .22], [.5, .13], [.56, .25], [.61, .25], [.64, .15], [.7, .13]],
  king: [[0, .44], [.05, .44], [.08, .38], [.13, .31], [.18, .23], [.55, .15], [.6, .27], [.64, .27], [.67, .18], [.7, .16]],
  rook: [[0, .44], [.06, .44], [.1, .36], [.16, .3], [.22, .26], [.62, .24], [.66, .32], [.82, .32]],
};
function piece(ctx, x, y, S, kind, team, lean = 0, alpha = 1) {
  const C = TEAM[team]; const pr = PROF[kind] || PROF.pawn; ctx.save(); ctx.globalAlpha *= alpha;
  ctx.save(); ctx.translate(x + S * .3, y + S * .02); ctx.scale(1, .26); const shg = ctx.createRadialGradient(0, 0, 0, 0, 0, S * .62); shg.addColorStop(0, 'rgba(0,0,0,.5)'); shg.addColorStop(.6, 'rgba(0,0,0,.3)'); shg.addColorStop(1, 'rgba(0,0,0,0)'); ctx.fillStyle = shg; ctx.fillRect(-S * .62, -S * .62, S * 1.24, S * 1.24); ctx.restore();
  ctx.translate(x, y); ctx.rotate(lean);
  const g = ctx.createLinearGradient(-S * .45, 0, S * .45, 0); g.addColorStop(0, C.lit); g.addColorStop(.38, C.mid); g.addColorStop(1, C.dark);
  ctx.beginPath(); pr.forEach(([h, w], i) => { i ? ctx.lineTo(-w * S, -h * S) : ctx.moveTo(-w * S, -h * S); }); for (let i = pr.length - 1; i >= 0; i--) ctx.lineTo(pr[i][1] * S, -pr[i][0] * S); ctx.closePath(); ctx.fillStyle = g; ctx.fill();
  ctx.lineWidth = Math.max(1, S * .012); ctx.strokeStyle = 'rgba(0,0,0,.35)'; ctx.stroke();
  // taban diski ve kenar parlaması
  ctx.beginPath(); ctx.ellipse(0, -S * .06, S * .41, S * .07, 0, 0, TAU); ctx.fillStyle = C.mid; ctx.fill(); ctx.beginPath(); ctx.ellipse(0, -S * .07, S * .36, S * .05, 0, Math.PI, TAU); ctx.strokeStyle = C.spec; ctx.lineWidth = S * .015; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(-pr[4][1] * S * .8, -pr[4][0] * S); ctx.lineTo(-pr[5][1] * S * .7, -pr[5][0] * S); ctx.strokeStyle = C.spec; ctx.lineWidth = S * .03; ctx.lineCap = 'round'; ctx.stroke();
  if (team === 'osm') { ctx.beginPath(); ctx.ellipse(0, -S * .6, S * .26, S * .045, 0, 0, TAU); ctx.fillStyle = C.trim; ctx.fill(); }
  const top = pr[pr.length - 1][0] * S;
  if (kind === 'pawn') { const r = S * .17, cy = -top - r * .82, rg = ctx.createRadialGradient(-r * .4, cy - r * .4, r * .1, 0, cy, r); rg.addColorStop(0, C.lit); rg.addColorStop(.5, C.mid); rg.addColorStop(1, C.dark); ctx.beginPath(); ctx.arc(0, cy, r, 0, TAU); ctx.fillStyle = rg; ctx.fill(); ctx.beginPath(); ctx.arc(-r * .35, cy - r * .35, r * .22, 0, TAU); ctx.fillStyle = C.spec; ctx.fill(); }
  if (kind === 'king') {
    if (team === 'osm') { // kavuk / sarık + hilal
      const cy = -top - S * .2;
      ctx.beginPath(); ctx.moveTo(-S * .1, cy - S * .2); ctx.quadraticCurveTo(0, cy - S * .36, S * .1, cy - S * .2); ctx.lineTo(S * .09, cy); ctx.lineTo(-S * .09, cy); ctx.closePath(); ctx.fillStyle = '#a5121a'; ctx.fill();   // kavuk tepesi
      const rg = ctx.createRadialGradient(-S * .12, cy - S * .06, S * .02, 0, cy, S * .34); rg.addColorStop(0, '#fffaf0'); rg.addColorStop(.55, '#ddd2bc'); rg.addColorStop(1, '#6e6250');
      ctx.beginPath(); ctx.ellipse(0, cy + S * .02, S * .33, S * .19, 0, 0, TAU); ctx.fillStyle = rg; ctx.fill();
      for (let k = -3; k <= 3; k++) { ctx.beginPath(); ctx.moveTo(k * S * .09 - S * .07, cy + S * .17); ctx.quadraticCurveTo(k * S * .09 + S * .02, cy + S * .02, k * S * .09 + S * .1, cy - S * .14); ctx.strokeStyle = 'rgba(110,90,66,.4)'; ctx.lineWidth = S * .014; ctx.stroke(); }
      ctx.beginPath(); ctx.ellipse(0, cy - S * .02, S * .05, S * .06, 0, 0, TAU); ctx.fillStyle = '#d9a84a'; ctx.fill(); ctx.beginPath(); ctx.arc(0, cy - S * .02, S * .025, 0, TAU); ctx.fillStyle = '#1e7a4a'; ctx.fill();   // mücevher
      ctx.beginPath(); ctx.moveTo(-S * .01, cy - S * .06); ctx.quadraticCurveTo(S * .08, cy - S * .3, S * .02, cy - S * .48); ctx.quadraticCurveTo(-S * .02, cy - S * .28, -S * .03, cy - S * .07); ctx.fillStyle = '#1a1410'; ctx.fill();   // sorguç
    } else { const cy = -top - S * .08; ctx.beginPath(); ctx.moveTo(-S * .2, cy + S * .06); for (let i = 0; i <= 4; i++) ctx.lineTo(-S * .2 + i * S * .1, cy - (i % 2 ? S * .05 : S * .14)); ctx.lineTo(S * .2, cy + S * .06); ctx.closePath(); ctx.fillStyle = C.trim; ctx.fill(); ctx.fillRect(-S * .015, cy - S * .3, S * .03, S * .18); ctx.fillRect(-S * .07, cy - S * .25, S * .14, S * .03); }
  }
  if (kind === 'rook') { ctx.fillStyle = C.mid; for (let i = 0; i < 3; i++) { ctx.fillRect(-S * .32 + i * S * .24, -top - S * .1, S * .16, S * .1); } ctx.beginPath(); ctx.ellipse(0, -top, S * .32, S * .05, 0, 0, TAU); ctx.fillStyle = C.dark; ctx.fill(); }
  ctx.restore();
}
function pathPt(path, at) { // path: [[t, lon, lat], ...] → dünya koordinatı + yön
  const q = path; let i = 0; while (i < q.length - 2 && at > q[i + 1][0]) i++; const a = q[i], b = q[i + 1], u = easeInOut(clamp((at - a[0]) / (b[0] - a[0])));
  const A = proj(a[1], a[2]), B = proj(b[1], b[2]); return { x: lerp(A[0], B[0], u), y: lerp(A[1], B[1], u), dir: Math.atan2(B[1] - A[1], B[0] - A[0]), moving: at > a[0] && at < b[0] };
}
// ordu: satranç taşı formasyonu. o.path [[t,lon,lat]], o.rows, o.cols, o.gap (dünya), o.S (taş yüksekliği dünya), o.ring {t, lon, lat, r} (kuşatma halkası)
function armyScr(ctx, o, t, P, info, lv) {
  const at = info.at, rise = i => backOut(clamp((t - o.t0 - i * .035) / .45));
  const c = pathPt(o.path, t); const n = o.rows * o.cols; const pts = [];
  const ringK = o.ring ? easeInOut(clamp((t - o.ring.t) / (o.ring.dur || 1.0))) * (1 - (o.unring ? easeInOut(clamp((t - o.unring) / 1.2)) : 0)) : 0;
  for (let r = 0; r < o.rows; r++) for (let q = 0; q < o.cols; q++) {
    const i = r * o.cols + q, ox = (q - (o.cols - 1) / 2) * o.gap, oy = (r - (o.rows - 1) / 2) * o.gap * .9, d = (o.face ?? c.dir) + Math.PI / 2;
    let wx = c.x + ox * Math.cos(d) - oy * Math.sin(d), wy = c.y + ox * Math.sin(d) + oy * Math.cos(d);
    if (ringK > 0) { const [cx, cy] = proj(o.ring.lon, o.ring.lat), a = i / n * TAU + .3; wx = lerp(wx, cx + Math.cos(a) * o.ring.r, ringK); wy = lerp(wy, cy + Math.sin(a) * o.ring.r * .85, ringK); }
    const hop = c.moving ? Math.abs(Math.sin(at * 7 + i * 1.3)) * o.S * .05 : 0;
    const isK = o.king && i === Math.floor(o.cols / 2); if (isK && o.kingHide != null && t >= o.kingHide) continue; pts.push({ wx, wy, i, hop, kind: isK ? 'king' : 'pawn' });
  }
  if (o.king && o.kingSolo) pts.length = 0;
  const [, , k0] = info.Pw(c.x, c.y);
  withDof(ctx, info, k0, g => {
    const sp = pts.map(p => { const [x, y, k] = info.Pw(p.wx, p.wy); return { ...p, x, y, k }; }).sort((a, b) => a.y - b.y);
    for (const p of sp) { const a = rise(p.i); if (a <= 0) continue; const S = o.S * info.cam.z * p.k * (p.kind === 'king' ? 1.35 : 1) * a; piece(g, p.x, p.y - p.hop * info.cam.z * p.k, S, p.kind, o.team, (o.lean || 0) * Math.sin(at * 3 + p.i), clamp(a * 2)); }
  });
}
function kingScr(ctx, o, t, P, info) { // tek büyük kral taşı (Kanuni), isteğe bağlı yol boyunca döner/geri çekilir
  const at = info.at, a = backOut(clamp((t - o.t0) / .5)); if (a <= 0) return; const c = o.path ? pathPt(o.path, t) : { x: proj(o.lon, o.lat)[0], y: proj(o.lon, o.lat)[1] };
  const [x, y, k] = info.Pw(c.x, c.y); withDof(ctx, info, k, g => piece(g, x, y, o.S * info.cam.z * k * a, o.kind || 'king', o.team, (o.lean || 0), 1));
}
// gemi filosu: o.route [[lon,lat]...], o.t0, o.t1 (filonun ilerlemesi), o.n, o.spacing (0-1 rota oranı), o.S
function shipDraw(g, x, y, S, ang, team, at, i) {
  g.save(); g.translate(x, y);
  const ca = Math.cos(ang), sa = Math.sin(ang) * .55; // perspektifte basık
  // dümen suyu
  g.globalAlpha *= .7; g.strokeStyle = 'rgba(235,245,255,.55)'; g.lineWidth = Math.max(1, S * .03); for (const sd of [-1, 1]) { g.beginPath(); g.moveTo(-ca * S * .6, -sa * S * .6); g.quadraticCurveTo(-ca * S * 1.3 + sd * sa * S * .3, -sa * S * 1.3 - sd * ca * S * .2, -ca * S * 2.1 + sd * sa * S * .6, -sa * S * 2.1 - sd * ca * S * .45); g.stroke(); } g.globalAlpha /= .7;
  // gövde
  g.save(); g.rotate(Math.atan2(sa, ca)); const len = S * Math.hypot(ca, sa) * 1.2, wid = S * .28;
  g.beginPath(); g.moveTo(-len * .55, -wid * .2); g.quadraticCurveTo(0, -wid * .6, len * .6, -wid * .05); g.lineTo(len * .62, wid * .1); g.quadraticCurveTo(0, wid * .7, -len * .55, wid * .25); g.closePath();
  const hg = g.createLinearGradient(0, -wid, 0, wid); hg.addColorStop(0, '#9a5a2a'); hg.addColorStop(1, '#3a1e0a'); g.fillStyle = hg; g.fill(); g.strokeStyle = '#1a0e06'; g.lineWidth = Math.max(1, S * .015); g.stroke();
  for (let k = 0; k < 7; k++) { const ox = -len * .4 + k * len * .13, sw = Math.sin(at * 6 + k * .5 + i) * wid * .25; g.beginPath(); g.moveTo(ox, wid * .2); g.lineTo(ox - wid * .3 + sw, wid * .95); g.moveTo(ox, -wid * .2); g.lineTo(ox - wid * .3 + sw, -wid * .9); g.strokeStyle = 'rgba(60,40,20,.8)'; g.lineWidth = Math.max(1, S * .012); g.stroke(); }
  g.restore();
  // direk ve latin yelken (dik)
  g.fillStyle = '#4a2c14'; g.fillRect(-S * .012, -S * .95, S * .024, S * .95);
  g.beginPath(); g.moveTo(-S * .5, -S * .25); g.quadraticCurveTo(-S * .05, -S * .55, S * .35, -S * 1.05); g.quadraticCurveTo(S * .15, -S * .6, S * .08, -S * .22); g.closePath(); const sg = g.createLinearGradient(-S * .5, 0, S * .4, 0); sg.addColorStop(0, '#fff6e4'); sg.addColorStop(1, '#bfb090'); g.fillStyle = sg; g.fill(); g.strokeStyle = 'rgba(60,40,20,.5)'; g.lineWidth = Math.max(1, S * .01); g.stroke();
  g.beginPath(); g.moveTo(0, -S * .95); g.lineTo(S * .22, -S * .9); g.lineTo(0, -S * .84); g.fillStyle = team === 'osm' ? '#c4161c' : '#e8e0d0'; g.fill();
  g.restore();
}
function fleetScr(ctx, o, t, P, info) {
  const u0 = clamp((t - o.t0) / (o.t1 - o.t0)); const app = smooth((t - o.t0) / .6); if (app <= 0) return;
  const R = o._R || (o._R = (() => { const P2 = o.route.map(([lo, la]) => proj(lo, la)); const L2 = [0]; for (let i = 1; i < P2.length; i++) L2.push(L2[i - 1] + Math.hypot(P2[i][0] - P2[i - 1][0], P2[i][1] - P2[i - 1][1])); return { P2, L2 }; })());
  const at = info.at, tot = R.L2[R.L2.length - 1];
  const where = s => { s = clamp(s) * tot; let i = 0; while (i < R.L2.length - 2 && s > R.L2[i + 1]) i++; const k = (s - R.L2[i]) / (R.L2[i + 1] - R.L2[i] || 1), A = R.P2[i], B = R.P2[i + 1]; return [lerp(A[0], B[0], k), lerp(A[1], B[1], k), Math.atan2(B[1] - A[1], B[0] - A[0])]; };
  const ships = []; for (let i = 0; i < o.n; i++) { const s = (o.s0 || 0) + u0 * (o.s1 - (o.s0 || 0)) - i * o.spacing; if (s < 0) continue; const [wx, wy, a] = where(s); const off = (i % 2 ? 1 : -1) * (o.side || 60); ships.push({ wx: wx - Math.sin(a) * off, wy: wy + Math.cos(a) * off, a, i }); }
  if (!ships.length) return; const mid = ships[Math.floor(ships.length / 2)]; const [, , km] = info.Pw(mid.wx, mid.wy);
  withDof(ctx, info, km, g => { g.globalAlpha = app; const sp = ships.map(s => { const [x, y, k] = info.Pw(s.wx, s.wy); const [x2, y2] = info.Pw(s.wx + Math.cos(s.a) * 50, s.wy + Math.sin(s.a) * 50); return { ...s, x, y, k, sa: Math.atan2(y2 - y, x2 - x) }; }).sort((a, b) => a.y - b.y); for (const s of sp) shipDraw(g, s.x, s.y + Math.sin(at * 2 + s.i) * 2, o.S * info.cam.z * s.k, s.sa, o.team || 'osm', at, s.i); });
}
// toplar çamura gömülür: o.lon,lat, o.n, o.S, o.sink [t0,t1]
function cannonScr(ctx, o, t, P, info) {
  const a = smooth((t - o.t0) / .5); if (a <= 0) return; const [cx, cy] = proj(o.lon, o.lat); const [, , k0] = info.Pw(cx, cy);
  withDof(ctx, info, k0, g => {
    g.globalAlpha = a; const sk = easeInOut(clamp((t - o.sink[0]) / (o.sink[1] - o.sink[0])));
    const [mx, my, mk] = info.Pw(cx, cy); const MS = o.S * info.cam.z * mk; g.save(); g.translate(mx, my); g.scale(1, .32); g.beginPath(); g.arc(0, 0, MS * 2.6 * (.4 + .6 * clamp(sk * 2 + .3)), 0, TAU); const mg = g.createRadialGradient(-MS * .6, -MS * .6, MS * .2, 0, 0, MS * 2.6); mg.addColorStop(0, '#5a4026'); mg.addColorStop(.7, '#2e2012'); mg.addColorStop(1, 'rgba(46,32,18,0)'); g.fillStyle = mg; g.fill(); g.restore();
    const list = []; for (let i = 0; i < o.n; i++) { const ang = i / o.n * TAU + .8, wx = cx + Math.cos(ang) * o.S * 1.1, wy = cy + Math.sin(ang) * o.S * .6; const [x, y, k] = info.Pw(wx, wy); list.push({ x, y, k, i }); }
    list.sort((p, q) => p.y - q.y);
    for (const p of list) { const S = o.S * info.cam.z * p.k, dn = sk * S * (.45 + .1 * (p.i % 2)), tip = sk * (.25 + .1 * p.i % 3);
      g.save(); g.beginPath(); g.rect(p.x - S * 2, p.y - S * 3, S * 4, S * 3 + S * .05); g.clip(); g.translate(p.x, p.y + dn); g.rotate(-.25 + tip);
      for (const sx of [-.45, .35]) { g.beginPath(); g.arc(sx * S, -S * .18, S * .22, 0, TAU); g.fillStyle = '#4a2e14'; g.fill(); g.strokeStyle = '#1a1006'; g.lineWidth = S * .04; g.stroke(); }
      const bg = g.createLinearGradient(0, -S * .6, 0, -S * .15); bg.addColorStop(0, TEAM.bronz.lit); bg.addColorStop(.5, TEAM.bronz.mid); bg.addColorStop(1, TEAM.bronz.dark);
      g.beginPath(); g.moveTo(-S * .7, -S * .55); g.lineTo(S * .8, -S * .48); g.lineTo(S * .8, -S * .28); g.lineTo(-S * .7, -S * .2); g.closePath(); g.fillStyle = bg; g.fill(); g.beginPath(); g.ellipse(S * .8, -S * .38, S * .05, S * .11, 0, 0, TAU); g.fillStyle = '#1a1006'; g.fill();
      g.restore(); }
  });
}
// minyatür kale (Viyana): o.lon,lat, o.R (dünya yarıçapı), o.H (sur yüksekliği dünya), o.towers
function citadelScr(ctx, o, t, P, info) {
  const a = smooth((t - o.t0) / .7); if (a <= 0) return; const [cx, cy] = proj(o.lon, o.lat); const [, , k0] = info.Pw(cx, cy);
  withDof(ctx, info, k0, g => {
    g.globalAlpha = a; const N = 48, ring = []; for (let i = 0; i <= N; i++) { const an = i / N * TAU; const [x, y, k] = info.Pw(cx + Math.cos(an) * o.R, cy + Math.sin(an) * o.R * .9); ring.push({ x, y, k, an }); }
    const hh = p => o.H * info.cam.z * p.k;
    const seg = (i, front) => { const p = ring[i], q = ring[i + 1]; const isF = Math.sin((p.an + q.an) / 2) > 0; if (isF !== front) return; const sh = .55 + .45 * Math.cos((p.an + q.an) / 2 + 2.3); g.beginPath(); g.moveTo(p.x, p.y); g.lineTo(q.x, q.y); g.lineTo(q.x, q.y - hh(q)); g.lineTo(p.x, p.y - hh(p)); g.closePath(); const c = Math.round(120 + 90 * sh); g.fillStyle = `rgb(${c},${c - 14},${c - 34})`; g.fill(); g.strokeStyle = 'rgba(40,30,20,.5)'; g.lineWidth = 1; g.stroke(); for (let m = 0; m < 3; m++) { const u = (m + .5) / 3, x = lerp(p.x, q.x, u), y = lerp(p.y, q.y, u) - hh(p), w = Math.abs(q.x - p.x) / 7; g.fillRect(x - w / 2, y - hh(p) * .15, w, hh(p) * .15); } };
    const tower = i => { const p = ring[i]; const tw = hh(p) * .55, th = hh(p) * 1.6; const tg = g.createLinearGradient(p.x - tw, 0, p.x + tw, 0); tg.addColorStop(0, '#d8c8a8'); tg.addColorStop(1, '#6a5a44'); g.fillStyle = tg; g.fillRect(p.x - tw, p.y - th, tw * 2, th); g.beginPath(); g.moveTo(p.x - tw * 1.2, p.y - th); g.lineTo(p.x, p.y - th - tw * 1.8); g.lineTo(p.x + tw * 1.2, p.y - th); g.closePath(); g.fillStyle = '#6a2a1a'; g.fill(); };
    for (let i = 0; i < N; i++) seg(i, false); for (let i = 0; i < N; i += 6) if (Math.sin(ring[i].an) <= 0) tower(i);
    // iç şehir + Stephansdom kulesi
    const [x0, y0, kk] = info.Pw(cx, cy); const B = o.H * info.cam.z * kk;
    for (let j = 0; j < 9; j++) { const R2 = rng(j + 3), bx = x0 + (R2() - .5) * o.R * info.cam.z * kk * 1.2, by = y0 + (R2() - .5) * o.R * info.cam.z * kk * .5, bw = B * (.5 + R2() * .4), bh = B * (.6 + R2() * .6); g.fillStyle = '#b8a888'; g.fillRect(bx - bw / 2, by - bh, bw, bh); g.beginPath(); g.moveTo(bx - bw * .6, by - bh); g.lineTo(bx, by - bh - bw * .5); g.lineTo(bx + bw * .6, by - bh); g.fillStyle = '#7a3420'; g.fill(); }
    const sx = x0 + B * .2, sy = y0; g.fillStyle = '#c8b898'; g.fillRect(sx - B * .35, sy - B * 1.4, B * .7, B * 1.4); g.beginPath(); g.moveTo(sx - B * .3, sy - B * 1.4); g.lineTo(sx, sy - B * 3.6); g.lineTo(sx + B * .3, sy - B * 1.4); g.closePath(); const sg = g.createLinearGradient(sx - B * .3, 0, sx + B * .3, 0); sg.addColorStop(0, '#e8d8b8'); sg.addColorStop(1, '#5a4a34'); g.fillStyle = sg; g.fill();
    for (let i = 0; i < N; i++) seg(i, true); for (let i = 0; i < N; i += 6) if (Math.sin(ring[i].an) > 0) tower(i);
  });
}
// duman sütunu + ateş parıltısı: o.lon,lat, o.t0, o.n
function smokeScr(ctx, o, t, P, info) {
  const a = smooth((t - o.t0) / .8) * (1 - smooth((t - (o.t1 ?? 99)) / 1)); if (a <= 0) return; const at = info.at; const [bx, by] = proj(o.lon, o.lat);
  for (let s = 0; s < (o.n || 1); s++) { const R2 = rng(s + 31), wx = bx + (R2() - .5) * (o.spread || 0), wy = by + (R2() - .5) * (o.spread || 0) * .6; const [x, y, k] = info.Pw(wx, wy); const S = (o.S || 300) * info.cam.z * k;
    ctx.save(); ctx.globalCompositeOperation = 'lighter'; const fl = .7 + .3 * Math.sin(at * 17 + s) * Math.sin(at * 7.3 + s * 2); const fg = ctx.createRadialGradient(x, y, 0, x, y, S * .9); fg.addColorStop(0, `rgba(255,170,70,${.75 * a * fl})`); fg.addColorStop(1, 'rgba(255,90,20,0)'); ctx.fillStyle = fg; ctx.fillRect(x - S, y - S, S * 2, S * 2); ctx.restore();
    for (let p = 0; p < 9; p++) { const ph = ((at * .22 + p / 9 + s * .17) % 1), r = S * (.25 + ph * .9), px = x + Math.sin(ph * 5 + p + s) * S * .3 + ph * S * .5, py = y - ph * S * 3.2; ctx.save(); ctx.globalAlpha = a * .7 * Math.sin(ph * Math.PI); const sg = ctx.createRadialGradient(px, py, 0, px, py, r); sg.addColorStop(0, 'rgba(58,52,50,.95)'); sg.addColorStop(1, 'rgba(70,62,58,0)'); ctx.fillStyle = sg; ctx.beginPath(); ctx.arc(px, py, r, 0, TAU); ctx.fill(); ctx.restore(); }
  }
}
Object.assign(SCR, { army: armyScr, king: kingScr, fleet: fleetScr, cannons: cannonScr, citadel: citadelScr, smoke: smokeScr });

// ---------------- ekran efektleri ----------------
window.POSTFX = window.POSTFX || [];
// hava: WEATHER = [{type:'rain'|'snow', t0, t1, power}]
POSTFX.push((ctx, t, info) => {
  for (const w of (typeof WEATHER !== 'undefined' ? WEATHER : [])) {
    const a = smooth((t - w.t0) / .5) * (1 - smooth((t - w.t1) / .6)) * (w.power ?? 1); if (a <= 0) continue; const at = info.at, R = rng(w.type === 'rain' ? 13 : 17);
    if (w.type === 'rain') { ctx.fillStyle = `rgba(20,28,40,${.14 * a})`; ctx.fillRect(0, 0, W, H); ctx.strokeStyle = `rgba(210,225,245,${.5 * a})`; ctx.lineCap = 'round';
      for (let i = 0; i < 520; i++) { const z = .3 + R() * .7, len = 40 + 90 * z, sp = 2600 * z, x = ((R() * W * 1.3 + at * sp * .25) % (W * 1.3)) - W * .15, y = ((R() * H + at * sp) % (H + 200)) - 100; ctx.lineWidth = .8 + 2.2 * z; ctx.globalAlpha = .4 + .6 * z; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x - len * .25, y - len); ctx.stroke(); }
      ctx.globalAlpha = 1; for (let i = 0; i < 40; i++) { const ph = (at * 1.6 + R()) % 1, x = R() * W, y = H * (.55 + R() * .45); ctx.beginPath(); ctx.ellipse(x, y, 4 + ph * 26, (4 + ph * 26) * .3, 0, 0, TAU); ctx.strokeStyle = `rgba(220,230,250,${.4 * a * (1 - ph)})`; ctx.lineWidth = 1.5; ctx.stroke(); } }
    else { ctx.fillStyle = `rgba(200,215,235,${.1 * a})`; ctx.fillRect(0, 0, W, H); for (let i = 0; i < 230; i++) { const z = R(), r = z > .93 ? 26 + 30 * R() : 3 + 9 * z, sp = 60 + 160 * z, x = ((R() * W + Math.sin(at * .9 + i) * 50 * z + at * 25 * z) % W), y = ((R() * H + at * sp) % (H + 80)) - 40; ctx.globalAlpha = a * (z > .93 ? .35 : .45 + .55 * z); ctx.drawImage(SOFT, x - r, y - r, r * 2, r * 2); } ctx.globalAlpha = 1; }
  }
});
// ışık huzmeleri + toz (ref: satranç sahnesi)
POSTFX.push((ctx, t, info) => {
  const pw = typeof RAYS === 'function' ? RAYS(t) : (typeof RAYS === 'number' ? RAYS : 0); if (pw <= 0) return; const at = info.at;
  const lx = L.light[0] * W - W * .15, ly = -H * .08; ctx.save(); ctx.globalCompositeOperation = 'screen';
  for (let i = 0; i < 7; i++) { const a = .5 + i * .13 + Math.sin(at * .2 + i) * .03, w = .05 + (i % 3) * .025; ctx.beginPath(); ctx.moveTo(lx, ly); ctx.lineTo(lx + Math.cos(a - w) * H * 2.2, ly + Math.sin(a - w) * H * 2.2); ctx.lineTo(lx + Math.cos(a + w) * H * 2.2, ly + Math.sin(a + w) * H * 2.2); ctx.closePath(); const g = ctx.createLinearGradient(lx, ly, lx + Math.cos(a) * H * 1.6, ly + Math.sin(a) * H * 1.6); g.addColorStop(0, `rgba(255,214,150,${.16 * pw})`); g.addColorStop(1, 'rgba(255,214,150,0)'); ctx.fillStyle = g; ctx.fill(); }
  const R = rng(41); for (let i = 0; i < 70; i++) { const x = (R() * W + Math.sin(at * .3 + i) * 30 + at * 6) % W, y = (R() * H + Math.cos(at * .25 + i) * 40 - at * 10 + H) % H, r = .8 + R() * 2.4; const dx = x - lx, dy = y - ly, inRay = Math.max(0, 1 - Math.abs(Math.atan2(dy, dx) - .82) * 2.2); ctx.globalAlpha = pw * (.2 + .8 * inRay) * (.4 + .6 * Math.sin(at * 2 + i) ** 2); ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fillStyle = '#ffe6b8'; ctx.fill(); }
  ctx.restore();
});
// şimşek / flaş: FLASHES = [t, ...]
POSTFX.push((ctx, t) => { for (const f of (typeof FLASHES !== 'undefined' ? FLASHES : [])) { const d = t - f; if (d < 0 || d > .5) continue; const a = (d < .06 ? 1 : d < .12 ? .3 : d < .18 ? .8 : Math.max(0, 1 - (d - .18) / .32)) * .55; ctx.fillStyle = `rgba(225,235,255,${a})`; ctx.fillRect(0, 0, W, H); } });
// sinema kenar yazısı / harf aralığı geniş başlık için letterbox istenirse: LETTERBOX = oran
POSTFX.push((ctx) => { if (typeof LETTERBOX === 'undefined' || !LETTERBOX) return; const h = H * LETTERBOX; ctx.fillStyle = '#000'; ctx.fillRect(0, 0, W, h); ctx.fillRect(0, H - h, W, h); });
