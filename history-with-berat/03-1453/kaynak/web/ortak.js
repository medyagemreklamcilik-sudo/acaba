// History with Berat · 02 · The real Dracula (stick figure)
const LOGO = new Image(); LOGO.src = 'logo.jpg';
const RADU = PAL.blue, VLADC = PAL.red;
const MEHMED = { cols: ['#2e7d4f', '#2e7d4f'], hat: 'none', belt: false, vest: '#e8b93a' };
const DRACUL = { cols: ['#1f4a2a', '#1f4a2a'], hat: 'none', belt: false, vest: '#d9a83a' };

// ---------- yardımcılar ----------
function sc(ctx) { ctx.setTransform(1, 0, 0, 1, 0, 0); }
function etiket(ctx, str, x, y, size, ap, { col = '#ffd23a', bg = '#1b1820', rot = -.06, w = null } = {}) {
  if (ap <= 0) return; ctx.save(); sc(ctx); ctx.translate(x, y); ctx.rotate(rot); const k = lerp(1.7, 1, easeOut(clamp(ap))); ctx.scale(k, k); ctx.globalAlpha = clamp(ap * 2);
  ctx.font = `700 ${size}px Poppins`; const tw = w || ctx.measureText(str).width + size * .9;
  rrect(ctx, -tw / 2, -size * .78, tw, size * 1.5, size * .2); ctx.fillStyle = bg; ctx.fill(); ctx.lineWidth = size * .09; ctx.strokeStyle = col; ctx.stroke();
  text(ctx, str, 0, size * .05, size, col, INK, 0, 'Poppins', 700); ctx.restore();
}
function buyukYazi(ctx, str, x, y, size, ap, col = '#fff') { if (ap <= 0) return; ctx.save(); sc(ctx); ctx.globalAlpha = clamp(ap * 2); ctx.translate(x, y); const k = .7 + .3 * backOut(clamp(ap)); ctx.scale(k, k); text(ctx, str, 0, 0, size, col, INK, size * .12, 'Poppins', 700); ctx.restore(); }
function kid(ctx, x, y, s, cols, o = {}) {
  drawStick(ctx, Object.assign({ x, y, s, cols, hat: 'none', belt: false, shadow: false }, o));
  const hr = .19 * s, lean = o.lean || 0, hx = x + Math.sin(lean) * .765 * s, hy = y - Math.cos(lean) * .765 * s;
  ctx.save(); ctx.translate(hx, hy); ctx.rotate(lean); ctx.beginPath(); ctx.ellipse(0, -hr * .78, hr * .95, hr * .45, 0, Math.PI, 0); fillStroke(ctx, '#4a3424', .02 * s); ctx.restore();
}
function mehmed(ctx, x, y, s, o = {}) { drawStick(ctx, C(MEHMED, Object.assign({ x, y, s, shadow: false }, o))); drawTurban(ctx, x, y - .765 * s, s); }
function dracul(ctx, x, y, s, o = {}) { // baba Vlad II Dracul: taç + bıyık
  drawStick(ctx, C(DRACUL, Object.assign({ x, y, s, shadow: false }, o)));
  const lean = o.lean || 0, hx = x + Math.sin(lean) * .765 * s, hy = y - Math.cos(lean) * .765 * s, r = .19 * s;
  ctx.save(); ctx.translate(hx, hy); ctx.rotate(lean);
  ctx.beginPath(); ctx.moveTo(-r * .85, -r * .6); for (let i = 0; i <= 4; i++) { ctx.lineTo(-r * .85 + i * r * .425, -r * (i % 2 ? 1.1 : 1.45)); } ctx.lineTo(r * .85, -r * .6); ctx.closePath(); fillStroke(ctx, '#e3b23c', .014 * s);
  ctx.beginPath(); ctx.moveTo(0, r * .28); ctx.quadraticCurveTo(-r * .5, r * .2, -r * .6, r * .55); ctx.quadraticCurveTo(-r * .3, r * .42, 0, r * .4); ctx.quadraticCurveTo(r * .3, r * .42, r * .6, r * .55); ctx.quadraticCurveTo(r * .5, r * .2, 0, r * .28); fillStroke(ctx, '#2a1a12', .01 * s);
  ctx.restore();
}
function gunduz(ctx, cam, t, { zemin = '#7aa04a', ufuk = 1180 } = {}) {
  applyCam(ctx, cam, .05); drawSky(ctx, '#4aa6ea', '#fbe6c0', -300, ufuk);
  applyCam(ctx, cam, .12); drawCloud(ctx, 160 + t * 8, 300, 110, 1); drawCloud(ctx, 820 + t * 5, 200, 80, 2);
  applyCam(ctx, cam, .3); ctx.fillStyle = '#5f8a3e'; ctx.beginPath(); ctx.moveTo(-400, ufuk); ctx.quadraticCurveTo(200, ufuk - 160, 700, ufuk - 60); ctx.quadraticCurveTo(1100, ufuk - 140, 1500, ufuk); ctx.lineTo(1500, 2600); ctx.lineTo(-400, 2600); ctx.fill();
  applyCam(ctx, cam, 1); ctx.fillStyle = zemin; ctx.fillRect(-600, ufuk, 2300, 1800);
}
function at(ctx, x, y, s, t, kos = 1, renk = '#7a4a2a') { // y = toynak hizası
  const g = Math.sin(t * 14) * kos;
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  for (const [lx, ph] of [[-.32, 0], [-.22, 2], [.25, 1], [.35, 3]]) { const a = Math.sin(t * 14 + ph) * .5 * kos; line(ctx, lx, -.45, lx + Math.sin(a) * .25, -.02, .05, INK); }
  ellipse(ctx, 0, -.55, .45, .2, g * .03); fillStroke(ctx, renk, .02);
  ctx.beginPath(); ctx.moveTo(.32, -.62); ctx.lineTo(.5, -.95); ctx.lineTo(.62, -.9); ctx.lineTo(.45, -.55); ctx.closePath(); fillStroke(ctx, renk, .02);
  ellipse(ctx, .64, -.93, .14, .08, .5); fillStroke(ctx, renk, .02); circle(ctx, .66, -.97, .018); ctx.fillStyle = INK; ctx.fill();
  ctx.beginPath(); ctx.moveTo(.45, -.98); ctx.quadraticCurveTo(.3, -.85 + g * .03, .36, -.66); ctx.lineWidth = .05; ctx.strokeStyle = '#2a1a12'; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(-.44, -.6); ctx.quadraticCurveTo(-.65, -.55 + g * .05, -.62, -.3); ctx.lineWidth = .05; ctx.stroke();
  ctx.restore();
}
function cadir(ctx, x, y, s, renk = '#f2ece0', ic = '#b3202c') { ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.beginPath(); ctx.moveTo(-1, 0); ctx.lineTo(-.85, -.7); ctx.quadraticCurveTo(0, -1.25, .85, -.7); ctx.lineTo(1, 0); ctx.closePath(); fillStroke(ctx, renk, .025); ctx.beginPath(); ctx.moveTo(-.18, 0); ctx.lineTo(0, -.6); ctx.lineTo(.18, 0); ctx.closePath(); fillStroke(ctx, '#1a1010', .02); for (let i = -1; i <= 1; i++) { ctx.beginPath(); ctx.moveTo(i * .5, -.85 + Math.abs(i) * .12); ctx.lineTo(i * .55, -.05); ctx.lineWidth = .04; ctx.strokeStyle = ic; ctx.stroke(); } line(ctx, 0, -1.04, 0, -1.4, .03); ctx.beginPath(); ctx.moveTo(0, -1.4); ctx.lineTo(.3, -1.3); ctx.lineTo(0, -1.22); ctx.fillStyle = '#c4161c'; ctx.fill(); ctx.restore(); }
function sancak(ctx, x, y, s, t, renk = '#c4161c', hilal = true) { line(ctx, x, y, x, y - 1.3 * s, .03 * s, '#4a3020'); const w = .7 * s, h = .45 * s, top = y - 1.28 * s; ctx.beginPath(); ctx.moveTo(x, top); for (let i = 0; i <= 10; i++) { const u = i / 10; ctx.lineTo(x + u * w, top + Math.sin(u * 5 - t * 6) * .04 * s * u); } for (let i = 10; i >= 0; i--) { const u = i / 10; ctx.lineTo(x + u * w, top + h + Math.sin(u * 5 - t * 6) * .04 * s * u); } ctx.closePath(); fillStroke(ctx, renk, .015 * s); if (hilal) { circle(ctx, x + w * .42, top + h / 2, h * .28); ctx.fillStyle = '#fff'; ctx.fill(); circle(ctx, x + w * .48, top + h / 2, h * .23); ctx.fillStyle = renk; ctx.fill(); } }
function kaziklar(ctx, cam, t, n = 60) { applyCam(ctx, cam, .4); for (let i = 0; i < n; i++) { const x = -200 + (i * 37) % 1500, b = 1060 + ((i * 53) % 90), h = 260 + (i * 29) % 160; line(ctx, x, b, x + Math.sin(i) * 6, b - h, 7, '#14080c'); } }
function sehir(ctx, cam) { // Konstantinopolis silüeti
  applyCam(ctx, cam, .3); ctx.fillStyle = '#5a4a6a';
  for (const [x, r] of [[540, 190], [300, 110], [780, 120], [140, 80], [930, 85]]) { ctx.fillRect(x - r, 980 - r * .4, r * 2, r * .5 + 120); ctx.beginPath(); ctx.arc(x, 980 - r * .4, r, Math.PI, 0); ctx.fill(); }
  for (const x of [380, 700]) { ctx.fillRect(x - 14, 560, 28, 440); ctx.beginPath(); ctx.moveTo(x - 18, 560); ctx.lineTo(x, 470); ctx.lineTo(x + 18, 560); ctx.fill(); }
  applyCam(ctx, cam, .55); ctx.fillStyle = '#8a7a6a'; ctx.fillRect(-300, 1080, 1700, 160); for (let i = 0; i < 16; i++) { ctx.fillRect(-300 + i * 110, 1040, 60, 50); }
  for (let i = 0; i < 5; i++) { ctx.fillStyle = '#7a6a5a'; ctx.fillRect(-100 + i * 300, 1000, 120, 240); }
}
function logoKart(ctx, lt, t, outro) {
  sc(ctx); const g = ctx.createRadialGradient(540, 820, 50, 540, 900, 1100); g.addColorStop(0, '#3a2a1a'); g.addColorStop(1, '#0d0a08'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  for (let i = 0; i < 14; i++) { const a = i / 14 * TAU + t * .2; ctx.save(); ctx.translate(540, 760); ctx.rotate(a); ctx.fillStyle = 'rgba(255,210,58,.06)'; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(1400, -90); ctx.lineTo(1400, 90); ctx.fill(); ctx.restore(); }
  const p = backOut(clamp(lt / .45)), r = 250 * p;
  if (r > 1) { ctx.save(); circle(ctx, 540, 760, r + 18); ctx.fillStyle = '#ffd23a'; ctx.fill(); circle(ctx, 540, 760, r); ctx.clip(); if (LOGO.complete && LOGO.naturalWidth) ctx.drawImage(LOGO, 540 - r, 760 - r, r * 2, r * 2); ctx.restore(); }
  buyukYazi(ctx, 'HISTORY WITH BERAT', 540, 1120, 76, (lt - .25) / .3, '#ffd23a');
  if (outro) etiket(ctx, 'FOLLOW', 540, 1560, 80, (lt - 1.0) / .25, { col: '#fff', bg: '#c4161c', rot: 0 });
}

