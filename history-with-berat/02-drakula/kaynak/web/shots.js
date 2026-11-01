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

const SHOTS = [];
const S = (start, end, draw, tr = 'whip') => SHOTS.push({ start, end, tr, draw });

// ===== 0 · KANCA =====
S(0, 1.18, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.12 - lt * .08 };
  nightCastle(ctx, cam, t); applyCam(ctx, cam, 1); ctx.fillStyle = '#0c0812'; ctx.fillRect(-400, 1240, 1900, 1200);
  vlad(ctx, 540, 1235, 620, t, { arms: { L: [.5, -.3], R: [.5, -.3] }, face: { eyes: 'smug', mouth: lt > .7 ? 'smirk' : 'flat', look: [0, .2] } });
  if ((lt > .66 && lt < .74) || (lt > .8 && lt < .84)) { sc(ctx); ctx.fillStyle = 'rgba(220,225,255,.55)'; ctx.fillRect(0, 0, W, H); }
});
S(1.18, 3.9, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 980 + hh[1], z: 1.0 + lt * .05 };
  palaceBG(ctx, t, cam, .6); applyCam(ctx, cam, 1); torchGlow(ctx, 110, 760, t, .8); torchGlow(ctx, 970, 760, t, .8);
  drawThrone(ctx, 540, 1060, .62); sultan(ctx, 540, 1060 - 280 * .62 + .3 * 330, 330, { face: { eyes: 'smug', mouth: 'smirk', browAng: .1 } });
  yeniceri(ctx, 170, 1240, 300, { arms: { L: [.3, -.2], R: [.3, -.2] } }); yeniceri(ctx, 910, 1240, 300, { flip: -1, arms: { L: [.3, -.2], R: [.3, -.2] } });
  const cx = lerp(-150, 0, easeOut(clamp(lt / .5)));
  kid(ctx, 450 + cx, 1235, 210, VLADC, { arms: { L: [.6, -1.2], R: [.6, -1.2] }, face: { eyes: 'normal', mouth: 'flat', browAng: .4, look: [0, -.4] } });
  kid(ctx, 630 + cx, 1235, 210, RADU, { arms: { L: [.6, -1.2], R: [.6, -1.2] }, face: { eyes: 'wide', mouth: 'frown', browAng: -.2, look: [0, -.4] } });
  etiket(ctx, 'HOSTAGES', 540, 360, 92, (lt - .8) / .2);
});
S(3.9, 8.4, (ctx, lt, t) => {
  const hit = t >= 6.8 ? Math.max(0, 1 - (t - 6.8) / .45) : 0, sh = shake(t, 22 * hit, 2.2, 5), red = clamp((t - 6.6) / .3);
  const cam = { x: 540 + sh[0], y: kf(t, [[3.9, 1000], [6.7, 1040], [6.9, 1080]]) + sh[1], z: kf(t, [[3.9, 1.05], [6.7, 1.18], [6.85, 1.0, easeOut], [8.4, .96]]) };
  nightCastle(ctx, cam, t, red); applyCam(ctx, cam, 1); ctx.fillStyle = mix('#140c18', '#2a0a10', red); ctx.fillRect(-400, 1240, 1900, 1200);
  for (let i = 0; i < 6; i++) { const f = ease(clamp((t - 6.85 - i * .04) / .35)); yeniceri(ctx, 150 + i * 160 + f * (i < 3 ? -60 : 60), 1180 - (i % 2) * 40, 170, { lean: (i < 3 ? -1 : 1) * f * 1.2, arms: f > .1 ? { L: [2.4, .3], R: [2.4, .3] } : { L: [.3, -.2], R: [.3, -.2] }, face: f > .2 ? { eyes: 'wide', mouth: 'o' } : { eyes: 'normal', mouth: 'flat' } }); }
  const dr = ease(clamp((t - 4.9) / .6)), up = ease(clamp((t - 6.55) / .25));
  vlad(ctx, 540, 1600, 760, t, { cape: 1 + up * .4, arms: { L: [.5, -.4], R: [lerp(.3, 2.1, Math.max(dr * .6, up)), lerp(-.2, -.35, up)] }, face: { eyes: 'smug', mouth: up > .3 ? 'grin' : 'smirk', look: [0, .1] },
    prop: (c, k, p, ang, side) => { if (k !== 'R' || dr <= 0) return; c.save(); c.translate(p[0], p[1]); c.rotate(-ang * side); c.beginPath(); c.moveTo(-.018, 0); c.lineTo(.018, 0); c.lineTo(.014, .55 * dr); c.lineTo(0, .6 * dr); c.lineTo(-.014, .55 * dr); c.closePath(); c.fillStyle = '#e8ecf2'; c.fill(); c.lineWidth = .005; c.strokeStyle = INK; c.stroke(); c.fillStyle = '#d9a83a'; c.fillRect(-.05, -.008, .1, .016); c.restore(); } });
  if (hit > 0) { sc(ctx); ctx.globalAlpha = hit * .5; ctx.fillStyle = '#ff2a2a'; ctx.fillRect(0, 0, W, H); ctx.globalAlpha = 1; }
});
// ===== 1 · I'M BERAT =====
S(8.4, 12.5, (ctx, lt, t) => logoKart(ctx, lt, t, false));
// ===== 2 · 1442: baba boyun eğer, bedel iki oğul =====
S(12.5, 17.3, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1080 + hh[1], z: 0.32 + 1.0 + lt * .03 };
  palaceBG(ctx, t, cam, 0); applyCam(ctx, cam, 1); drawThrone(ctx, 700, 1100, .7);
  sultan(ctx, 700, 1100 - 280 * .7 + .3 * 370, 370, { face: { eyes: 'smug', mouth: 'smirk', look: [-.6, .2] } });
  const bow = ease(clamp((lt - 1.2) / .5));
  dracul(ctx, 250, 1240, 380, { spine: undefined, lean: bow * .35, arms: { L: [.3 + bow * .6, -.4], R: [.3 + bow * .6, -.4] }, face: { eyes: 'normal', mouth: 'flat', look: [.6, 0] } });
  buyukYazi(ctx, '1442', 540, 330, 190, (lt - .1) / .3, '#ffd23a');
  etiket(ctx, 'VLAD II DRACUL', 260, 760, 46, (lt - 1.6) / .25, { col: '#fff', bg: '#1f4a2a', rot: -.03 });
});
S(17.3, 20.2, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1080 + hh[1], z: 0.3 + 1.08 - lt * .03 };
  palaceBG(ctx, t, cam, 0); applyCam(ctx, cam, 1); drawThrone(ctx, 760, 1100, .62);
  sultan(ctx, 760, 1100 - 280 * .62 + .3 * 330, 330, { arms: { L: [.5, -.6], R: { ik: [-.42, -.42] } }, flip: 1, face: { eyes: 'normal', mouth: 'grin', look: [-.6, .4] } });
  dracul(ctx, 200, 1240, 360, { lean: .25, face: { eyes: 'normal', mouth: 'frown', browAng: -.3, look: [.6, .3] } });
  const g = backOut(clamp((t - 18.4) / .3));
  if (g > 0) { kid(ctx, 390, 1240, 210 * g, VLADC, { face: { eyes: 'normal', mouth: 'frown', browAng: .3 } }); kid(ctx, 540, 1240, 210 * g, RADU, { face: { eyes: 'wide', mouth: 'o' } }); }
  buyukYazi(ctx, '?', 540, 420, 260, (t - 17.5) / .25, '#ffd23a');
});
// ===== 3 · saraya gönderildiler =====
S(20.2, 24.3, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0] + lt * 30, y: 1100 + hh[1], z: 0.22 + 1.0 };
  gunduz(ctx, cam, t, { zemin: '#c8b07a' });
  applyCam(ctx, cam, .5); // saray kapısı
  ctx.fillStyle = '#e8dcc0'; ctx.fillRect(560, 700, 520, 520); ctx.fillStyle = '#b3202c'; ctx.beginPath(); ctx.moveTo(560, 700); ctx.lineTo(820, 560); ctx.lineTo(1080, 700); ctx.fill();
  ctx.fillStyle = '#3a2a1a'; ctx.beginPath(); ctx.moveTo(740, 1220); ctx.lineTo(740, 930); ctx.arc(820, 930, 80, Math.PI, 0); ctx.lineTo(900, 1220); ctx.fill();
  sancak(ctx, 620, 700, 200, t); sancak(ctx, 1020, 700, 200, t);
  applyCam(ctx, cam, 1); const x0 = 120 + lt * 120;
  kid(ctx, x0, 1300, 220, VLADC, { ...YURU_POZ(t), face: { eyes: 'normal', mouth: 'flat', browAng: .35 } });
  kid(ctx, x0 + 150, 1300, 210, RADU, { ...YURU_POZ(t + .3), face: { eyes: 'normal', mouth: 'smile' } });
  yeniceri(ctx, x0 - 170, 1300, 300, { ...YURU_POZ(t + .1) });
  etiket(ctx, 'THE OTTOMAN COURT', 540, 330, 64, (lt - .3) / .25);
});
function YURU_POZ(t, sp = 8) { return { legs: { L: [Math.sin(t * sp) * .5 + .05, -Math.max(0, Math.sin(t * sp + 1)) * .7], R: [-Math.sin(t * sp) * .5 + .05, -Math.max(0, -Math.sin(t * sp + 1)) * .7] }, arms: { L: [.3 - Math.sin(t * sp) * .5, -.3], R: [.3 + Math.sin(t * sp) * .5, -.3] }, bob: -Math.abs(Math.sin(t * sp)) * .01 }; }
// ===== 4 · eğitim: Türkçe, binicilik, savaş =====
S(24.3, 26.2, (ctx, lt, t) => {
  const cam = { x: 540, y: 1080, z: 0.25 + 1.02 + lt * .04 }; palaceBG(ctx, t, cam, 0); applyCam(ctx, cam, 1);
  rrect(ctx, 300, 520, 520, 330, 14); fillStroke(ctx, '#20402a', 10);
  ctx.save(); ctx.strokeStyle = '#f4efe0'; ctx.lineWidth = 9; ctx.lineCap = 'round'; const n = Math.floor(clamp(lt / 1.2) * 5);
  for (let i = 0; i < n; i++) { const x = 760 - i * 95; ctx.beginPath(); ctx.moveTo(x, 600); ctx.quadraticCurveTo(x - 40, 700, x - 10, 760); ctx.stroke(); if (i % 2) { ctx.beginPath(); ctx.arc(x - 30, 640, 7, 0, 7); ctx.stroke(); } } ctx.restore();
  drawStick(ctx, { x: 880, y: 1240, s: 360, cols: ['#2c3a5a', '#2c3a5a'], hat: 'none', belt: false, shadow: false, arms: { L: [.3, -.2], R: { ik: [-.45, -.75] } }, face: { eyes: 'normal', mouth: 'smile' } }); drawTurban(ctx, 880, 1240 - .765 * 360, 360);
  kid(ctx, 330, 1300, 220, VLADC, { face: { eyes: 'normal', mouth: 'flat', look: [.5, -.4] } }); kid(ctx, 520, 1300, 210, RADU, { face: { eyes: 'happy', mouth: 'smile' } });
  etiket(ctx, 'TURKISH', 540, 330, 84, (lt - .9) / .2);
}, 'cut');
S(26.2, 27.1, (ctx, lt, t) => {
  const cam = { x: 540 + lt * 60, y: 1080, z: 0.3 + 1.0 }; gunduz(ctx, cam, t, { zemin: '#9ab060' }); applyCam(ctx, cam, 1);
  const x = 200 + lt * 380; at(ctx, x, 1320, 420, t); kid(ctx, x + 10, 1320 - .5 * 420, 200, VLADC, { legs: { L: [.9, -.6], R: [.9, -.6] }, arms: { L: [1.2, -.5], R: [1.2, -.5] }, face: { eyes: 'wide', mouth: 'grin' } });
  etiket(ctx, 'HORSE RIDING', 540, 330, 70, lt / .15);
}, 'cut');
S(27.1, 28.6, (ctx, lt, t) => {
  const hit = Math.max(0, 1 - Math.abs(lt - .7) / .12), sh = shake(t, 10 * hit, 3, 2), cam = { x: 540 + sh[0], y: 1080 + sh[1], z: 0.3 + 1.05 };
  gunduz(ctx, cam, t, { zemin: '#c8b07a' }); applyCam(ctx, cam, 1);
  const sw = Math.sin(lt * 9) * .6;
  kid(ctx, 380, 1300, 260, VLADC, { arms: { L: [.4, -.3], R: [1.6 + sw, -.3] }, face: { eyes: 'normal', mouth: 'teeth', browAng: .5 }, prop: (c, k, p, ang, side) => { if (k !== 'R') return; c.save(); c.translate(p[0], p[1]); c.rotate(-ang * side); c.fillStyle = '#c8a070'; c.fillRect(-.012, 0, .024, .45); c.restore(); } });
  yeniceri(ctx, 700, 1300, 340, { flip: -1, arms: { L: [.4, -.3], R: [1.4 - sw, -.4] }, face: { eyes: 'normal', mouth: 'smile' }, prop: (c, k, p, ang, side) => { if (k !== 'R') return; c.save(); c.translate(p[0], p[1]); c.rotate(-ang * side); c.fillStyle = '#c8a070'; c.fillRect(-.012, 0, .024, .4); c.restore(); } });
  if (hit > 0) burst(ctx, 540, 900, 70 * hit, 9, '#ffd23a');
  etiket(ctx, 'THE ART OF WAR', 540, 330, 70, lt / .15);
});
// ===== 5 · iki kardeş ayrışır =====
S(28.6, 31.9, (ctx, lt, t) => {
  const cam = { x: 540, y: 1120, z: 0.25 + 1.0 + lt * .03 }; gunduz(ctx, cam, t, { zemin: '#8aa858' }); applyCam(ctx, cam, 1);
  ctx.fillStyle = '#d8c090'; ctx.beginPath(); ctx.moveTo(440, 2000); ctx.lineTo(500, 1240); ctx.lineTo(580, 1240); ctx.lineTo(640, 2000); ctx.fill();
  const ay = ease(clamp((lt - .8) / 1.4));
  for (const s of [-1, 1]) { ctx.beginPath(); ctx.moveTo(540, 1240); ctx.quadraticCurveTo(540 + s * 150, 1150, 540 + s * 420, 1180); ctx.lineWidth = 60; ctx.strokeStyle = '#d8c090'; ctx.stroke(); }
  kid(ctx, 540 - ay * 300, 1400, 280, VLADC, { flip: 1, face: { eyes: 'normal', mouth: 'frown', browAng: .5, look: [-.5, 0] } });
  kid(ctx, 540 + ay * 300, 1400, 270, RADU, { face: { eyes: 'happy', mouth: 'smile', look: [.5, 0] } });
});
S(31.9, 35.2, (ctx, lt, t) => {
  const cam = { x: 540, y: 1110, z: 0.25 + 1.05 - lt * .03 }; palaceBG(ctx, t, cam, 0); applyCam(ctx, cam, 1); torchGlow(ctx, 110, 760, t, .6); torchGlow(ctx, 970, 760, t, .6);
  const laf = Math.sin(t * 9) > .3;
  kid(ctx, 380, 1300, 300, RADU, { arms: { L: [.3, -.2], R: [.3, -.2] }, face: { eyes: 'happy', mouth: laf ? 'grin' : 'smile' } });
  mehmed(ctx, 690, 1300, 330, { arms: { L: { ik: [.35, -.55] }, R: [.3, -.2] }, flip: -1, face: { eyes: 'happy', mouth: laf ? 'smile' : 'grin' } });
  etiket(ctx, 'MEHMED II', 690, 720, 60, (t - 34.0) / .2, { col: '#fff', bg: '#2e7d4f' });
  // köşede Vlad kıskanç bakar
  kid(ctx, 980, 1500, 200, VLADC, { flip: -1, face: { eyes: 'smug', mouth: 'frown', look: [-.6, -.2] } });
});
S(35.2, 38.1, (ctx, lt, t) => {
  const boom = Math.max(0, 1 - Math.abs(lt - 1.05) / .2), sh = shake(t, 14 * boom, 3, 4), cam = { x: 540 + sh[0], y: 1000 + sh[1], z: 1.12 - lt * .04 };
  applyCam(ctx, cam, .05); drawSky(ctx, '#e88a3a', '#ffd9a0', -300, 1100); applyCam(ctx, cam, .1); drawSun(ctx, 540, 640, 110, t, .9);
  sehir(ctx, cam); applyCam(ctx, cam, 1); ctx.fillStyle = '#4a3a2a'; ctx.fillRect(-400, 1240, 1900, 1200);
  for (let i = 0; i < 3; i++) sancak(ctx, 200 + i * 340, 1250, 360 * clamp((lt - .3 - i * .15) / .4), t + i, '#c4161c');
  if (boom > 0) burst(ctx, 540, 1000, 200 * boom, 12, '#fff2b0');
  etiket(ctx, 'CONSTANTINOPLE 1453', 540, 330, 58, (lt - .5) / .2);
});
// ===== 6 · Vlad unutmadı =====
S(38.1, 40.9, (ctx, lt, t) => {
  const cam = { x: 540, y: 1060, z: 0.12 + 1.0 + lt * .08 }; sc(ctx); ctx.fillStyle = '#0d0b14'; ctx.fillRect(0, 0, W, H);
  applyCam(ctx, cam, 1); rrect(ctx, 230, 380, 620, 760, 20); ctx.fillStyle = '#2a3a6a'; ctx.fill();
  circle(ctx, 640, 560, 70); ctx.fillStyle = '#e8ecff'; ctx.fill();
  for (let i = 0; i < 12; i++) { const y = ((t * 900 + i * 137) % 900) + 300; line(ctx, 260 + i * 50, y, 250 + i * 50, y + 40, 3, 'rgba(180,200,255,.5)'); }
  kid(ctx, 540, 1400, 380, VLADC, { arms: { L: [.2, -.1], R: [.2, -.1] }, face: { eyes: 'smug', mouth: 'flat', browAng: .55, look: [0, .3] } });
  for (let i = 0; i < 6; i++) { rrect(ctx, 250 + i * 116, 360, 26, 820, 10); fillStroke(ctx, '#3a3a44', 6); }
  rrect(ctx, 230, 360, 620, 30, 8); fillStroke(ctx, '#3a3a44', 6); rrect(ctx, 230, 1150, 620, 30, 8); fillStroke(ctx, '#3a3a44', 6);
  etiket(ctx, 'PRISONER', 540, 260, 84, (lt - 1.6) / .2, { col: '#ff4a4a' });
});
// ===== 7 · 1462 savaşı, gece baskını =====
S(40.9, 44.8, (ctx, lt, t) => {
  const cam = { x: 540 + lt * 40, y: 1000, z: 1.0 }; gunduz(ctx, cam, t, { zemin: '#6a7a3a' }); applyCam(ctx, cam, 1);
  for (let i = 0; i < 5; i++) { const x = 120 + i * 120 + lt * 260; at(ctx, x, 1300 + (i % 2) * 40, 300, t + i * .3); drawStick(ctx, { x: x + 8, y: 1300 + (i % 2) * 40 - 150, s: 150, cols: PAL.red, hat: 'none', belt: false, shadow: false, legs: { L: [.9, -.6], R: [.9, -.6] }, face: { eyes: 'normal', mouth: 'teeth', browAng: .4 } }); }
  const x = 760 + lt * 120; at(ctx, x, 1420, 460, t, 1, '#1a1210');
  vlad(ctx, x + 10, 1420 - .5 * 460, 300, t, { legs: { L: [.9, -.6], R: [.9, -.6] }, arms: { L: [.6, -.5], R: [2.3, -.2] }, face: { eyes: 'smug', mouth: 'teeth' } });
  buyukYazi(ctx, '1462', 540, 330, 190, (lt - .1) / .3, '#ffd23a');
});
S(44.8, 49.7, (ctx, lt, t) => {
  const cam = { x: 540, y: 1000, z: kf(lt, [[0, 1.0], [3.0, 1.12], [3.2, 1.3, easeOut]]) };
  sc(ctx); const g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#070a1c'); g.addColorStop(1, '#1a2040'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  applyCam(ctx, cam, .1); circle(ctx, 860, 300, 60); ctx.fillStyle = '#e8ecff'; ctx.fill();
  applyCam(ctx, cam, 1); ctx.fillStyle = '#1a1a14'; ctx.fillRect(-400, 1180, 1900, 1200);
  for (let i = 0; i < 5; i++) cadir(ctx, 60 + i * 230, 1180 - (i % 2) * 30, 150, '#a8a8b8', '#6a1a24');
  const big = 1 + (lt > 3.1 ? .0 : 0); cadir(ctx, 640, 1330, 330, '#d8d0c0', '#b3202c');
  if (lt > 3.1) { mehmed(ctx, 640, 1330, 220, { arms: { L: [2.4, .3], R: [2.4, .3] }, face: { eyes: 'wide', mouth: 'o' } }); etiket(ctx, 'KILL THE SULTAN', 540, 330, 60, (lt - 3.1) / .2, { col: '#ff4a4a' }); }
  const vx = lerp(-120, 330, ease(clamp(lt / 3)));
  vlad(ctx, vx, 1440, 300, t, { ...YURU_POZ(t, 10), arms: { L: [.6, -.5], R: [2.6, -.2] }, face: { eyes: 'smug', mouth: 'smirk' }, prop: (c, k, p, ang, side) => { if (k !== 'R') return; c.save(); c.translate(p[0], p[1]); c.rotate(-ang * side); c.fillStyle = '#5a3a20'; c.fillRect(-.012, -.05, .024, .25); c.restore(); } });
  torchGlow(ctx, vx + 140, 1080, t, 1);
});
S(49.7, 51.0, (ctx, lt, t) => {
  const cam = { x: 540, y: 1000, z: 1.0 }; sc(ctx); ctx.fillStyle = '#120a10'; ctx.fillRect(0, 0, W, H); applyCam(ctx, cam, 1); ctx.fillStyle = '#1a1a14'; ctx.fillRect(-400, 1180, 1900, 1200);
  cadir(ctx, 760, 1260, 300, '#d8d0c0', '#b3202c');
  ctx.save(); ctx.globalCompositeOperation = 'lighter'; for (let i = 0; i < 5; i++) { const y = 1100 - ((t * 400 + i * 90) % 300); circle(ctx, 700 + Math.sin(i * 3 + t * 5) * 80, y, 40 + i * 6); ctx.fillStyle = 'rgba(255,120,30,.35)'; ctx.fill(); } ctx.restore();
  vlad(ctx, 600 - lt * 500, 1450, 300, t, { ...YURU_POZ(t, 14), flip: -1, face: { eyes: 'wide', mouth: 'o' } });
  etiket(ctx, 'FAILED', 540, 420, 130, lt / .15, { col: '#ff4a4a', bg: '#1b1820', rot: -.12 });
}, 'cut');
// ===== 8 · kazıklar ormanı =====
S(51.0, 55.0, (ctx, lt, t) => {
  const cam = { x: 540 + lt * 20, y: 1000, z: 1.0 }; gunduz(ctx, cam, t, { zemin: '#7a6a4a' }); applyCam(ctx, cam, 1);
  for (let r = 0; r < 2; r++) for (let i = 0; i < 6; i++) yeniceri(ctx, -200 + i * 170 + lt * 140 + r * 60, 1250 + r * 160, 230 + r * 40, { ...YURU_POZ(t + i * .2 + r) , face: { eyes: 'normal', mouth: 'flat' } });
  sancak(ctx, -60 + lt * 140, 1250, 380, t);
}, 'cut');
S(55.0, 59.9, (ctx, lt, t) => {
  const cam = { x: 540, y: 1000, z: kf(lt, [[0, 1.15], [4.9, 1.0]]) };
  applyCam(ctx, cam, .05); const g = ctx.createLinearGradient(0, -200, 0, 1300); g.addColorStop(0, '#2a0508'); g.addColorStop(1, '#c43a2a'); ctx.fillStyle = g; ctx.fillRect(-800, -800, 2700, 3600);
  applyCam(ctx, cam, .2); circle(ctx, 540, 640, 150); ctx.fillStyle = '#ff9a7a'; ctx.fill();
  applyCam(ctx, cam, .4); ctx.fillStyle = '#14080c'; ctx.beginPath(); ctx.moveTo(-300, 1100); ctx.quadraticCurveTo(540, 980, 1400, 1100); ctx.lineTo(1400, 2400); ctx.lineTo(-300, 2400); ctx.fill();
  kaziklar(ctx, cam, t, 70);
  applyCam(ctx, cam, 1); ctx.fillStyle = '#0c0608'; ctx.fillRect(-400, 1300, 1900, 1200);
  for (let i = 0; i < 4; i++) yeniceri(ctx, 170 + i * 250, 1520, 320, { flip: i % 2 ? -1 : 1, face: { eyes: 'wide', mouth: 'o' }, arms: i % 2 ? { L: [2.6, .2], R: [2.6, .2] } : { L: [.3, -.2], R: [.3, -.2] } });
  const n = Math.round(20000 * easeOut(clamp((t - 57.4) / .9)));
  if (t > 57.3) buyukYazi(ctx, n.toLocaleString('en-US'), 540, 360, 180, (t - 57.3) / .3, '#fff');
});
// ===== 9 · tahtı Radu aldı =====
S(59.9, 65.2, (ctx, lt, t) => {
  const cam = { x: 540, y: 1040, z: 0.12 + 1.02 + lt * .03 }; palaceBG(ctx, t, cam, .3); applyCam(ctx, cam, 1);
  drawThrone(ctx, 540, 1200, .8); sancak(ctx, 860, 1250, 420, t);
  const otur = ease(clamp((t - 62.0) / .5));
  if (t > 61.7) drawStick(ctx, { x: lerp(300, 540, otur), y: 1200 - 280 * .8 + .3 * 340 * otur + (1 - otur) * (280 * .8 - .3 * 340) + 0, s: 340, cols: RADU, hat: 'none', belt: false, shadow: false, legs: otur > .8 ? { L: [.95, -.95], R: [.95, -.95] } : undefined, face: { eyes: 'happy', mouth: 'grin' } });
  if (t > 61.7) { const x = lerp(300, 540, otur), y = 1200 - 280 * .8 + .3 * 340 * otur + (1 - otur) * (280 * .8 - .3 * 340); drawTurban(ctx, x, y - .765 * 340, 340); }
  etiket(ctx, 'RADU', 540, 330, 100, (t - 62.3) / .2, { col: '#fff', bg: '#2f63c9' });
  if (lt < 1.8) { buyukYazi(ctx, '?', 540, 600, 300, lt / .2, '#ffd23a'); }
});
// ===== 10 · aynı çocukluk, iki son =====
S(65.2, 66.6, (ctx, lt, t) => {
  const cam = { x: 540, y: 1120, z: 0.35 + 1.0 }; palaceBG(ctx, t, cam, 0); applyCam(ctx, cam, 1);
  kid(ctx, 420, 1350, 300, VLADC, { face: { eyes: 'normal', mouth: 'smile' } }); kid(ctx, 660, 1350, 290, RADU, { face: { eyes: 'normal', mouth: 'smile' } });
  etiket(ctx, 'SAME CHILDHOOD', 540, 330, 66, lt / .2);
}, 'cut');
S(66.6, 70.9, (ctx, lt, t) => {
  const cam = { x: 540, y: 1000, z: 1.0 }; sc(ctx);
  ctx.fillStyle = '#2a4a8a'; ctx.fillRect(0, 0, W / 2, H); ctx.fillStyle = '#2a0a12'; ctx.fillRect(W / 2, 0, W / 2, H);
  ctx.fillStyle = '#fff'; ctx.fillRect(W / 2 - 4, 0, 8, H);
  applyCam(ctx, cam, 1);
  const a = backOut(clamp(lt / .3)), b = backOut(clamp((t - 68.6) / .3));
  if (a > 0) { sancak(ctx, 330, 1300, 340, t); drawStick(ctx, { x: 270, y: 1300, s: 330 * a, cols: RADU, hat: 'none', belt: false, shadow: false, face: { eyes: 'happy', mouth: 'grin' } }); drawTurban(ctx, 270, 1300 - .765 * 330 * a, 330 * a); }
  if (b > 0) vlad(ctx, 810, 1300, 340 * b, t, { face: { eyes: 'smug', mouth: 'smirk' } });
  etiket(ctx, 'OTTOMAN ALLY', 270, 330, 50, lt / .2, { col: '#fff', bg: '#1b3a7a' });
  etiket(ctx, 'DRACULA', 810, 330, 70, (t - 69.6) / .2, { col: '#ff4a4a' });
});
// ===== 11 · kahraman mı, canavar mı =====
S(70.9, 75.0, (ctx, lt, t) => {
  const cam = { x: 540, y: 1000, z: 1.0 + lt * .03 }; nightCastle(ctx, cam, t, .4); applyCam(ctx, cam, 1); ctx.fillStyle = '#140c18'; ctx.fillRect(-400, 1240, 1900, 1200);
  vlad(ctx, 540, 1480, 520, t, { face: { eyes: 'smug', mouth: 'smirk', look: [Math.sin(t * 2) * .6, 0] } });
  etiket(ctx, 'HERO?', 270, 420, 80, (t - 71.6) / .2, { col: '#fff', bg: '#2f63c9', rot: -.1 });
  etiket(ctx, 'MONSTER?', 790, 520, 80, (t - 72.6) / .2, { col: '#fff', bg: '#c4161c', rot: .08 });
  if (t > 73.5) { const p = backOut(clamp((t - 73.5) / .3)); sc(ctx); ctx.save(); ctx.translate(540, 1680); ctx.scale(p, p); rrect(ctx, -300, -80, 600, 150, 40); ctx.fillStyle = '#fff'; ctx.fill(); ctx.beginPath(); ctx.moveTo(-180, 60); ctx.lineTo(-230, 130); ctx.lineTo(-120, 65); ctx.fill(); text(ctx, 'COMMENT BELOW', 0, 0, 52, '#1b1820', INK, 0, 'Poppins', 700); ctx.restore(); }
});
// ===== 12 · kapanış =====
S(75.0, 79.6, (ctx, lt, t) => logoKart(ctx, lt, t, true), 'cut');
