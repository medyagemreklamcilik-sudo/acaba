// History with Berat · 03 · 1453: He carried his navy over a hill (stick figure)
const BYZ = { cols: ['#7a2a9a', '#7a2a9a'], hat: 'none', belt: false };
const BYZ_SOL = { cols: ['#2f63c9', '#f6f1e8'], hat: 'none', belt: true };
const URBAN = { cols: ['#6b5a44', '#6b5a44'], hat: 'none', belt: true };
const norm = s => s.toLowerCase().replace(/[^a-z0-9]/g, '');
function wt(word, t0 = 0) { const q = norm(word); const w = WORDS.find(w => w.s >= t0 - .01 && norm(w.w).startsWith(q)); if (!w) console.log('WT MISS', word, t0); return w ? w.s : t0; }

// ---------- props ----------
function helmet(ctx, x, y, s, lean = 0, col = '#b8c2cc') { const hr = .19 * s, hx = x + Math.sin(lean) * .765 * s, hy = y - Math.cos(lean) * .765 * s; ctx.save(); ctx.translate(hx, hy); ctx.rotate(lean); ctx.beginPath(); ctx.arc(0, -hr * .15, hr * 1.05, Math.PI, 0); ctx.lineTo(hr * 1.05, -hr * .05); ctx.lineTo(-hr * 1.05, -hr * .05); ctx.closePath(); fillStroke(ctx, col, .015 * s); line(ctx, 0, -hr * 1.2, 0, -hr * 1.55, .02 * s); ctx.beginPath(); ctx.ellipse(0, -hr * 1.6, hr * .18, hr * .32, 0, 0, TAU); fillStroke(ctx, '#c4161c', .01 * s); ctx.restore(); }
function bizAsker(ctx, x, y, s, o = {}) { drawStick(ctx, C(BYZ_SOL, Object.assign({ x, y, s, shadow: false, face: { eyes: 'normal', mouth: 'flat' } }, o))); helmet(ctx, x, y, s, o.lean || 0); }
function crown(ctx, hx, hy, r, s) { ctx.beginPath(); ctx.moveTo(-r * .9, -r * .55); ctx.lineTo(-r * .9, -r * 1.25); ctx.lineTo(-r * .45, -r * 1.0); ctx.lineTo(0, -r * 1.45); ctx.lineTo(r * .45, -r * 1.0); ctx.lineTo(r * .9, -r * 1.25); ctx.lineTo(r * .9, -r * .55); ctx.closePath(); fillStroke(ctx, '#e3b23c', .014 * s); for (const k of [-.5, 0, .5]) { circle(ctx, k * r, -r * .78, r * .1); ctx.fillStyle = k ? '#2f63c9' : '#c4161c'; ctx.fill(); } }
function konstantin(ctx, x, y, s, t, o = {}) {
  const robe = o.robe ?? 1;
  drawStick(ctx, C(o.armor ? { cols: ['#8a96a3', '#8a96a3'], hat: 'none', belt: true } : BYZ, Object.assign({ x, y, s, shadow: false, face: { eyes: 'normal', mouth: 'flat', browAng: .2 } }, o)));
  if (robe > 0) { ctx.save(); ctx.globalAlpha = robe; const w = s * .34; ctx.beginPath(); ctx.moveTo(x - s * .1, y - .6 * s); ctx.quadraticCurveTo(x - w, y - .3 * s, x - w, y - .02 * s); ctx.lineTo(x + w, y - .02 * s); ctx.quadraticCurveTo(x + w, y - .3 * s, x + s * .1, y - .6 * s); ctx.closePath(); fillStroke(ctx, '#5a1a7a', .014 * s); ctx.fillStyle = '#e3b23c'; ctx.fillRect(x - s * .03, y - .58 * s, s * .06, .56 * s); ctx.restore(); }
  const r = .19 * s, lean = o.lean || 0, hx = x + Math.sin(lean) * .765 * s, hy = y - Math.cos(lean) * .765 * s;
  ctx.save(); ctx.translate(hx, hy); ctx.rotate(lean); ctx.beginPath(); ctx.moveTo(-r * .55, r * .35); ctx.quadraticCurveTo(0, r * 1.25, r * .55, r * .35); ctx.quadraticCurveTo(0, r * .7, -r * .55, r * .35); fillStroke(ctx, '#5a3a22', .01 * s); if (o.crown !== false) crown(ctx, 0, 0, r, s); ctx.restore();
}
function urban(ctx, x, y, s, o = {}) { drawStick(ctx, C(URBAN, Object.assign({ x, y, s, shadow: false }, o))); const r = .19 * s, hy = y - .765 * s; ctx.beginPath(); ctx.ellipse(x, hy - r * .8, r * 1.05, r * .55, 0, Math.PI, 0); fillStroke(ctx, '#3a2a1a', .014 * s); ctx.beginPath(); ctx.moveTo(x - r * .4, hy + r * .3); ctx.quadraticCurveTo(x, hy + r * 1.2, x + r * .4, hy + r * .3); fillStroke(ctx, '#8a6a4a', .01 * s); }
function topDev(ctx, x, y, s, ang = -.06, fire = 0, t = 0) { // dev bombard, y = zemin
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  rrect(ctx, -320, -70, 640, 70, 10); fillStroke(ctx, '#7a4a2a', 6); for (const wx of [-250, 250]) { circle(ctx, wx, -10, 60); fillStroke(ctx, '#5a3a22', 6); circle(ctx, wx, -10, 14); ctx.fillStyle = INK; ctx.fill(); }
  ctx.save(); ctx.translate(-40, -150); ctx.rotate(ang);
  rrect(ctx, -300, -90, 620, 180, 40); fillStroke(ctx, '#8a7a5a', 7);
  for (const bx of [-220, -80, 60, 200]) { rrect(ctx, bx, -100, 34, 200, 8); fillStroke(ctx, '#6a5a3a', 5); }
  ellipse(ctx, 330, 0, 40, 110); fillStroke(ctx, '#6a5a3a', 7); ellipse(ctx, 336, 0, 24, 80); ctx.fillStyle = '#120c08'; ctx.fill();
  if (fire > 0) { ctx.globalAlpha = clamp(1 - fire); burst(ctx, 420 + fire * 120, 0, 120 + fire * 260, 12, '#ffcf3a', 7); burst(ctx, 420 + fire * 120, 0, 70 + fire * 150, 10, '#ff6a2a', 3); ctx.globalAlpha = 1; puff(ctx, 520 + fire * 300, -40, 90 + fire * 160, t, '#d8d0c4', 4, clamp(1.3 - fire)); }
  ctx.restore(); ctx.restore();
}
function surlar(ctx, x0, base, w, h, o = {}) { // Theodosius surları: taş + tuğla şeritler, burçlar
  const stone = o.stone || '#cdb88e', brick = o.brick || '#b4573a', dark = o.dark || 0;
  ctx.save();
  rrect(ctx, x0, base - h, w, h + 400, 6); fillStroke(ctx, mix(stone, '#1a1418', dark), 6);
  ctx.save(); ctx.beginPath(); ctx.rect(x0, base - h, w, h + 400); ctx.clip(); ctx.fillStyle = mix(brick, '#1a1418', dark); for (let k = 0; k < 6; k++) ctx.fillRect(x0, base - h + 60 + k * 110, w, 22); ctx.restore();
  for (let i = 0; i < Math.floor(w / 70); i++) { rrect(ctx, x0 + 8 + i * 70, base - h - 46, 44, 50, 4); fillStroke(ctx, mix(stone, '#1a1418', dark), 5); }
  for (const tx of (o.towers || [])) { rrect(ctx, tx - 90, base - h - 170, 180, h + 570, 8); fillStroke(ctx, mix(stone, '#1a1418', dark), 6); ctx.fillStyle = mix(brick, '#1a1418', dark); for (let k = 0; k < 6; k++) ctx.fillRect(tx - 88, base - h - 100 + k * 110, 176, 20); for (let j = 0; j < 3; j++) { rrect(ctx, tx - 84 + j * 62, base - h - 214, 44, 50, 4); fillStroke(ctx, mix(stone, '#1a1418', dark), 5); } rrect(ctx, tx - 20, base - h - 110, 40, 70, 18); ctx.fillStyle = '#1a1418'; ctx.fill(); }
  ctx.restore();
}
function kubbeler(ctx, cam, red = 0) { // Ayasofya + şehir silüeti
  applyCam(ctx, cam, .25); ctx.fillStyle = mix('#7d6a8a', '#3a1a20', red);
  ctx.fillRect(330, 760, 420, 300); ctx.beginPath(); ctx.arc(540, 760, 170, Math.PI, 0); ctx.fill(); for (const x of [380, 700]) { ctx.beginPath(); ctx.arc(x, 800, 70, Math.PI, 0); ctx.fill(); }
  for (const [x, r] of [[140, 90], [940, 100], [250, 60], [840, 70]]) { ctx.fillRect(x - r, 900, r * 2, 200); ctx.beginPath(); ctx.arc(x, 900, r, Math.PI, 0); ctx.fill(); }
  line(ctx, 540, 590, 540, 520, 8, mix('#7d6a8a', '#3a1a20', red));
}
function kadirga(ctx, x, y, s, t, o = {}) { // Osmanlı kadırgası, y = omurga
  ctx.save(); ctx.translate(x, y); ctx.rotate(o.rot || 0); ctx.scale(s * (o.flip || 1), s);
  for (let i = 0; i < 7; i++) { const ox = -200 + i * 60, a = Math.sin(t * 5 + i * .4) * (o.oars ?? 1) * .3; line(ctx, ox, -30, ox + Math.sin(a) * 50 - 30, 70, 6, '#6a4a2a'); }
  ctx.beginPath(); ctx.moveTo(-300, -80); ctx.lineTo(300, -80); ctx.quadraticCurveTo(370, -110, 400, -150); ctx.lineTo(330, -10); ctx.quadraticCurveTo(0, 20, -260, -10); ctx.quadraticCurveTo(-330, -40, -300, -80); ctx.closePath(); fillStroke(ctx, o.hull || '#8a3a22', 6);
  ctx.fillStyle = '#e2b04a'; ctx.fillRect(-280, -70, 590, 14);
  line(ctx, -10, -80, -10, -420, 10, '#6a4a2a');
  ctx.beginPath(); ctx.moveTo(-190, -150); ctx.lineTo(170, -440); ctx.quadraticCurveTo(120, -250, -10, -150); ctx.closePath(); fillStroke(ctx, '#f4ead4', 5);
  line(ctx, -10, -420, -10, -470, 5); ctx.beginPath(); ctx.moveTo(-10, -470); for (let i = 0; i <= 6; i++) ctx.lineTo(-10 + i * 14, -470 + Math.sin(i - t * 6) * 4); for (let i = 6; i >= 0; i--) ctx.lineTo(-10 + i * 14, -430 + Math.sin(i - t * 6) * 4); ctx.closePath(); fillStroke(ctx, o.flag || '#c4161c', 3);
  if (!o.flag) { circle(ctx, 30, -450, 9); ctx.fillStyle = '#fff'; ctx.fill(); circle(ctx, 34, -450, 7); ctx.fillStyle = '#c4161c'; ctx.fill(); }
  ctx.restore();
}
function kutuk(ctx, x, y, r, len = 120, shine = 1) { ctx.save(); ctx.translate(x, y); rrect(ctx, -len / 2, -r, len, r * 2, r); fillStroke(ctx, '#8a5a32', 5); ctx.fillStyle = `rgba(255,240,180,${.35 * shine})`; ctx.fillRect(-len / 2 + 10, -r * .6, len - 20, r * .3); ellipse(ctx, len / 2, 0, r * .45, r); fillStroke(ctx, '#c49a6a', 4); ctx.restore(); }
function zincir(ctx, x0, x1, y, t, s = 1) { const n = Math.floor((x1 - x0) / (60 * s)); for (let i = 0; i < n; i++) { const x = x0 + i * 60 * s, yy = y + Math.sin(i * .4 + t) * 6; ctx.save(); ctx.translate(x, yy); if (i % 2) { ellipse(ctx, 0, 0, 40 * s, 22 * s); ctx.lineWidth = 12 * s; ctx.strokeStyle = INK; ctx.stroke(); ctx.lineWidth = 7 * s; ctx.strokeStyle = '#7a8088'; ctx.stroke(); } else { ctx.fillStyle = '#7a8088'; ctx.fillRect(-40 * s, -6 * s, 80 * s, 12 * s); ctx.lineWidth = 4; ctx.strokeStyle = INK; ctx.strokeRect(-40 * s, -6 * s, 80 * s, 12 * s); } ctx.restore(); if (i % 6 === 3) { rrect(ctx, x - 50 * s, yy - 26 * s, 100 * s, 30 * s, 10 * s); fillStroke(ctx, '#8a5a32', 4); } } }
function deniz(ctx, cam, t, ufuk = 1100, gece = 0) { applyCam(ctx, cam, .05); drawSky(ctx, mix('#4aa6ea', '#0e1430', gece), mix('#fbe6c0', '#2a2a5a', gece), -300, ufuk); applyCam(ctx, cam, .2); drawSea(ctx, ufuk, t, 2600, gece ? ['#2a3a6a', '#1a2a5a', '#0e1a3a'] : ['#7fd3e0', '#18a3c0', '#0d7fa6']); }
function tepe(ctx, cam, t, { gece = 0, sabah = 0 } = {}) { applyCam(ctx, cam, .05); drawSky(ctx, mix(sabah ? '#ff9a5a' : '#4aa6ea', '#0e1430', gece), mix(sabah ? '#ffd9a0' : '#fbe6c0', '#2a2a5a', gece), -300, 1300); applyCam(ctx, cam, .12); if (!gece) { drawCloud(ctx, 200 + t * 8, 280, 100, 1); drawCloud(ctx, 850 + t * 5, 200, 70, 2); } }
function kirmizi(ctx, a) { if (a <= 0) return; sc(ctx); ctx.globalAlpha = a; ctx.fillStyle = '#ff2a2a'; ctx.fillRect(0, 0, W, H); ctx.globalAlpha = 1; }
function flas(ctx, a) { if (a <= 0) return; sc(ctx); ctx.fillStyle = `rgba(255,255,255,${clamp(a)})`; ctx.fillRect(0, 0, W, H); }

function hillY(x, base, ctrl) { const u = clamp((x + 500) / 2100); return base - 2 * u * (1 - u) * (base - ctrl); }
const SHOTS = [];
const S = (start, end, draw, tr = 'whip') => SHOTS.push({ start, end, tr, draw });

// ===== 0 · KANCA =====
S(0, 2.86, (ctx, lt, t) => { // dünyanın en güçlü surları, minicik ordu
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: kf(lt, [[0, 1.35], [2.8, 1.0]]) };
  tepe(ctx, cam, t); kubbeler(ctx, cam); applyCam(ctx, cam, .6); surlar(ctx, -300, 1100, 1700, 420, { towers: [120, 540, 960] });
  applyCam(ctx, cam, 1); ctx.fillStyle = '#9a8a5a'; ctx.fillRect(-600, 1180, 2300, 1400);
  for (let i = 0; i < 9; i++) yeniceri(ctx, 60 + i * 120, 1240, 110, { arms: { L: [.3, -.2], R: [1.6, -1.0] }, face: { eyes: 'wide', mouth: 'o', look: [0, -.6] } });
  buyukYazi(ctx, 'STRONGEST WALLS', 540, 330, 92, lt / .3, '#ffd23a');
});
S(2.86, 4.48, (ctx, lt, t) => { // 21 yaşındaki padişah
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1060 + hh[1], z: 1.1 - lt * .05 };
  palaceBG(ctx, t, cam, .3); applyCam(ctx, cam, 1);
  mehmed(ctx, 540, 1560, 760, { arms: { L: [.5, -.4], R: [1.2, -1.6] }, face: { eyes: 'smug', mouth: 'smirk', look: [.3, -.1] } });
  buyukYazi(ctx, '21', 540, 360, 260, (t - wt('21-year-old')) / .25, '#ffd23a'); etiket(ctx, 'YEARS OLD', 540, 520, 56, (t - wt('21-year-old') - .2) / .25);
});
S(4.48, 7.24, (ctx, lt, t) => { // gemi tepenin üstünde: kanca görüntüsü
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 + lt * .04 };
  tepe(ctx, cam, t); applyCam(ctx, cam, .4); ctx.fillStyle = '#5f8a3e'; ctx.beginPath(); ctx.moveTo(-500, 1250); ctx.quadraticCurveTo(540, 560, 1600, 1250); ctx.lineTo(1600, 2600); ctx.lineTo(-500, 2600); ctx.fill();
  const u = clamp(lt / 2.6), px = lerp(-80, 760, u), py = hillY(px, 1250, 560);
  const ang = Math.atan2(hillY(px + 20, 1250, 560) - hillY(px - 20, 1250, 560), 40);
  for (let i = 0; i < 5; i++) { const lx = px - 200 + i * 110, ly = hillY(lx, 1250, 560); kutuk(ctx, lx, ly + 10, 16, 110); }
  kadirga(ctx, px, py - 30, .75, t, { rot: ang, oars: 0 });
  for (let i = 0; i < 3; i++) { const fx = px + 260 + i * 90, fy = hillY(fx, 1250, 560); yeniceri(ctx, fx, fy, 150, { lean: .5, arms: { L: [1.4, -.2], R: [1.4, -.2] }, legs: { L: [Math.sin(t * 8 + i) * .5, -.3], R: [-Math.sin(t * 8 + i) * .5, -.3] }, face: { eyes: 'normal', mouth: 'o' } }); }
  buyukYazi(ctx, 'OVER A HILL?!', 540, 330, 100, (t - wt('over', 5)) / .25, '#ffd23a');
});
// ===== 1 · I'M BERAT =====
S(7.24, 11.9, (ctx, lt, t) => logoKart(ctx, lt, t, false));
// ===== 2 · bin yıl dayanan surlar =====
S(11.9, 14.7, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0] + lt * 20, y: 1000 + hh[1], z: 1.05 };
  tepe(ctx, cam, t); kubbeler(ctx, cam); applyCam(ctx, cam, .55); surlar(ctx, -300, 1150, 1700, 300, { towers: [200, 880] });
  applyCam(ctx, cam, 1); deniz(ctx, { x: 540, y: 1000, z: 1 }, t, 1600);
  buyukYazi(ctx, 'CONSTANTINOPLE', 540, 330, 96, lt / .3, '#fff');
}, 'cut');
S(14.7, 17.95, (ctx, lt, t) => { // ordular surlara çarpıp sekiyor
  const hit = Math.max(0, 1 - ((lt % 1.0) / .3)), sh = shake(t, 10 * hit, 2, 1), cam = { x: 540 + sh[0], y: 1000 + sh[1], z: 1.0 };
  tepe(ctx, cam, t); applyCam(ctx, cam, .7); surlar(ctx, -200, 1180, 1500, 620, { towers: [300, 820] });
  applyCam(ctx, cam, 1); ctx.fillStyle = '#9a8a5a'; ctx.fillRect(-600, 1180, 2300, 1400);
  for (let i = 0; i < 4; i++) { const ph = (lt * 1.0 + i * .25) % 1, x = 1000 - ph * 650, fall = clamp((ph - .75) / .25); drawStick(ctx, { x: x + fall * 120, y: 1240, s: 200, cols: [[PAL.red, PAL.green, PAL.navy, PAL.yellow][i][0], [PAL.red, PAL.green, PAL.navy, PAL.yellow][i][0]], hat: 'none', belt: false, shadow: false, lean: fall * 1.3, arms: { L: [1.5, -.2], R: [1.5, -.2] }, legs: { L: [Math.sin(t * 10 + i) * .5, -.3], R: [-Math.sin(t * 10 + i) * .5, -.3] }, face: fall > .3 ? { eyes: 'x', mouth: 'o' } : { eyes: 'wide', mouth: 'grin' } }); }
  buyukYazi(ctx, '1,000 YEARS', 540, 330, 120, (t - wt('thousand', 12)) / .25, '#ffd23a'); etiket(ctx, 'NEVER BROKEN', 540, 500, 56, (t - wt('stopped')) / .25);
});
S(17.95, 19.94, (ctx, lt, t) => { sc(ctx); ctx.fillStyle = '#120c10'; ctx.fillRect(0, 0, W, H); const z = 1 + lt * .08; ctx.save(); ctx.translate(540, 820); ctx.scale(z, z); text(ctx, '1453', 0, 0, 300, '#ffd23a', INK, 30, 'Poppins', 700); ctx.restore(); }, 'cut');
// ===== 3 · canavar: Urban'ın topu =====
S(19.94, 22.6, (ctx, lt, t) => { // Mehmed ordusuyla geliyor
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 + lt * .04 };
  gunduz(ctx, cam, t, { zemin: '#b8a070' }); applyCam(ctx, cam, .5); for (let i = 0; i < 5; i++) cadir(ctx, 100 + i * 220, 1120, 90 + (i % 2) * 20);
  applyCam(ctx, cam, 1); for (let i = 0; i < 6; i++) yeniceri(ctx, 120 + i * 170, 1240 - (i % 2) * 30, 150, { arms: { L: [.3, -.2], R: [.3, -.2] } });
  at(ctx, 540, 1250, 330, t, .3, '#f2ece0'); mehmed(ctx, 560, 1250 - 330 * .45, 230, { legs: { L: [.9, -.9], R: [.9, -.9] }, face: { eyes: 'smug', mouth: 'smirk' } });
  sancak(ctx, 860, 1240, 380, t); etiket(ctx, 'MEHMED II', 540, 360, 70, (lt - .2) / .25, { col: '#fff', bg: '#2e7d4f' });
});
S(22.6, 26.2, (ctx, lt, t) => { // dev top ortaya çıkıyor
  const rev = easeOut(clamp(lt / .8)), hh = handheld(t, 2), cam = { x: 540 + hh[0] + lerp(-200, 0, rev), y: 1050 + hh[1], z: lerp(1.6, 1.0, rev) };
  gunduz(ctx, cam, t, { zemin: '#b8a070' }); applyCam(ctx, cam, 1);
  topDev(ctx, 470, 1240, 1.05, -.06);
  urban(ctx, 920, 1240, 300, { flip: -1, arms: { L: [.3, -.2], R: [1.8, -.6] }, face: { eyes: 'happy', mouth: 'grin', look: [-.6, 0] } });
  for (let i = 0; i < 3; i++) yeniceri(ctx, 120 + i * 90, 1240, 130, { face: { eyes: 'wide', mouth: 'o', look: [.5, -.4] } });
  buyukYazi(ctx, 'A MONSTER', 540, 330, 120, (t - wt('monster')) / .25, '#ff4a3a'); etiket(ctx, 'URBAN · HUNGARIAN ENGINEER', 700, 520, 44, (t - wt('urban', 25)) / .25);
});
S(26.2, 28.5, (ctx, lt, t) => { // twist
  const cam = { x: 540, y: 1000, z: 1.0 + lt * .1 }; sc(ctx); ctx.fillStyle = '#1a1220'; ctx.fillRect(0, 0, W, H);
  for (let i = 0; i < 12; i++) { const a = i / 12 * TAU + t * .4; ctx.save(); ctx.translate(540, 900); ctx.rotate(a); ctx.fillStyle = 'rgba(255,210,58,.07)'; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(1400, -100); ctx.lineTo(1400, 100); ctx.fill(); ctx.restore(); }
  urban(ctx, 540, 1400, 640, { arms: { L: [.4, -.2], R: [1.6, -2.2] }, face: { eyes: 'smug', mouth: 'smirk', look: [.4, -.2] } });
  buyukYazi(ctx, 'THE TWIST', 540, 360, 130, (t - wt('twist')) / .25, '#ffd23a');
}, 'cut');
S(28.5, 32.6, (ctx, lt, t) => { // Bizans'a teklif, parası yok
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 };
  palaceBG(ctx, t, cam, 0); applyCam(ctx, cam, 1);
  konstantin(ctx, 740, 1240, 380, t, { flip: -1, arms: lt > 2.6 ? { L: [1.2, -1.6], R: [1.2, -1.6] } : { L: [.3, -.2], R: [.3, -.2] }, face: lt > 2.6 ? { eyes: 'normal', mouth: 'frown', browAng: -.4 } : { eyes: 'happy', mouth: 'smile' } });
  urban(ctx, 300, 1240, 300, { arms: { L: [.3, -.2], R: { ik: [.45, -.5] } }, face: { eyes: 'happy', mouth: 'grin', look: [.6, 0] } });
  sc(ctx); rrect(ctx, 390, 760, 200, 140, 10); fillStroke(ctx, '#f4ead2', 5); line(ctx, 410, 800, 570, 800, 5); topDev(ctx, 490, 880, .18, -.06);
  if (lt > 2.6) { const k = clamp((lt - 2.6) / .4); ctx.save(); ctx.translate(840, 1000); ctx.rotate(.4); ellipse(ctx, 0, 0, 60 * k, 40 * k); fillStroke(ctx, '#c49a6a', 5); ctx.restore(); for (let i = 0; i < 3; i++) { ctx.globalAlpha = clamp(1 - (lt - 2.8 - i * .2)); circle(ctx, 870 + i * 20, 1060 + (lt - 2.6) * 120 + i * 20, 6); ctx.fillStyle = '#8a8a8a'; ctx.fill(); ctx.globalAlpha = 1; } }
  etiket(ctx, 'BYZANTINES', 740, 360, 64, (lt - .3) / .25, { col: '#fff', bg: '#5a1a7a' });
  if (t > wt('couldnt', 30)) etiket(ctx, 'NO MONEY', 540, 560, 96, (t - wt('couldnt', 30)) / .2, { col: '#fff', bg: '#c4161c', rot: -.08 });
});
// ===== 4 · top surları yıkıyor, gece yeniden örülüyor =====
S(32.6, 34.92, (ctx, lt, t) => {
  const f = clamp((t - wt('smashed')) / .9), hit = t > wt('smashed') ? Math.max(0, 1 - (t - wt('smashed')) / .5) : 0, sh = shake(t, 26 * hit, 2.2, 3);
  const cam = { x: 540 + sh[0], y: 1000 + sh[1], z: 1.0 };
  tepe(ctx, cam, t); applyCam(ctx, cam, .8); surlar(ctx, 560, 1240, 900, 700, { towers: [900] });
  if (f > 0) { ctx.save(); ctx.globalCompositeOperation = 'destination-out'; circle(ctx, 720, 860, 160 * clamp(f * 2)); ctx.fill(); ctx.restore(); for (let i = 0; i < 9; i++) { const R = rng(i + 3); rrect(ctx, 720 + (R() - .5) * 80 + f * (R() - .3) * 500, 860 + f * f * 600 * R(), 50, 40, 6); fillStroke(ctx, '#cdb88e', 4); } }
  applyCam(ctx, cam, 1); ctx.fillStyle = '#9a8a5a'; ctx.fillRect(-600, 1240, 2300, 1400);
  topDev(ctx, 170, 1240, .7, -.1, f, t);
  flas(ctx, hit * .6); buyukYazi(ctx, 'BOOM', 540, 360, 170, (t - wt('smashed')) / .2, '#ff4a3a');
});
S(34.92, 37.9, (ctx, lt, t) => { // gece tamir
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.05 };
  tepe(ctx, cam, t, { gece: 1 }); applyCam(ctx, cam, .1); circle(ctx, 820, 300, 90); ctx.fillStyle = '#fff3d6'; ctx.fill();
  applyCam(ctx, cam, .8); surlar(ctx, 100, 1240, 900, 640, { towers: [], dark: .45 });
  const fill = clamp(lt / 2.6); ctx.save(); ctx.globalCompositeOperation = 'destination-out'; circle(ctx, 560, 900, 170 * (1 - fill)); ctx.fill(); ctx.restore();
  applyCam(ctx, cam, 1); ctx.fillStyle = '#2a2430'; ctx.fillRect(-600, 1240, 2300, 1400);
  for (let i = 0; i < 4; i++) { const x = 300 + i * 160, up = Math.sin(t * 6 + i) > 0; bizAsker(ctx, x, 1240, 210, { arms: { L: [up ? 2.4 : 1.2, -.3], R: [up ? 2.4 : 1.2, -.3] }, face: { eyes: 'normal', mouth: 'o' } }); sc(ctx); }
  applyCam(ctx, cam, 1); for (let i = 0; i < 4; i++) { const x = 300 + i * 160, y = 1240 - 210 * (Math.sin(t * 6 + i) > 0 ? 1.15 : .95); rrect(ctx, x - 28, y - 20, 56, 40, 6); fillStroke(ctx, '#cdb88e', 4); }
  torchGlow(ctx, 160, 1000, t, .8);
  buyukYazi(ctx, 'EVERY NIGHT', 540, 330, 110, (t - wt('every', 34)) / .25, '#ffd23a'); etiket(ctx, 'REBUILT', 540, 490, 60, (t - wt('rebuilt')) / .25);
});
// ===== 5 · Haliç ve zincir =====
S(37.9, 42.72, (ctx, lt, t) => {
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.05 - lt * .02 };
  deniz(ctx, cam, t, 900); applyCam(ctx, cam, .3); ctx.fillStyle = '#7d8a5a'; ctx.fillRect(-500, 760, 520, 200); ctx.fillRect(1000, 760, 600, 200); kubbeler(ctx, { x: cam.x + 300, y: cam.y + 120, z: .7 });
  applyCam(ctx, cam, 1); const k = clamp((t - wt('chain')) / .8); zincir(ctx, -100, lerp(-100, 1200, Math.max(k, t > wt('locked') ? .3 : 0)), 1050, t * 2, 1.2);
  buyukYazi(ctx, 'GOLDEN HORN', 540, 330, 100, (t - wt('golden')) / .25, '#ffd23a'); etiket(ctx, 'IRON CHAIN', 540, 1150, 70, (t - wt('chain')) / .25, { col: '#fff', bg: '#4a4a52' });
});
S(42.72, 44.98, (ctx, lt, t) => { // gemiler zincire çarpıyor
  const bump = Math.max(0, Math.sin(lt * 4)) * 20, cam = { x: 540, y: 1000, z: 1.0 };
  deniz(ctx, cam, t, 800); applyCam(ctx, cam, 1);
  for (let i = 0; i < 2; i++) kadirga(ctx, 300 + i * 420 - bump, 1100 + i * 40, .6, t, { flip: 1 });
  zincir(ctx, -100, 1200, 1150, t * 2, 1.4);
  buyukYazi(ctx, 'NO WAY IN', 540, 360, 120, (t - wt('no', 42)) / .25, '#ff4a3a');
});
S(44.98, 47.88, (ctx, lt, t) => { // Mehmed düşünüyor
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.1 + lt * .05 };
  palaceBG(ctx, t, cam, .3); applyCam(ctx, cam, 1);
  mehmed(ctx, 540, 1600, 760, { arms: { L: [.5, -.4], R: { ik: [.12, -.66] } }, face: { eyes: lt > 1.6 ? 'wide' : 'smug', mouth: lt > 1.6 ? 'grin' : 'flat', look: [.4, -.4] } });
  if (lt > 1.4) { const k = backOut(clamp((lt - 1.4) / .3)); sc(ctx); circle(ctx, 820, 420, 90 * k); fillStroke(ctx, '#ffe14d', 7); rrect(ctx, 800, 500, 40 * k, 50 * k, 8); fillStroke(ctx, '#b8b8b8', 5); burst(ctx, 820, 420, 160 * k, 12, 'rgba(255,225,77,.35)', 2); }
  buyukYazi(ctx, 'NO ONE EXPECTED', 540, 330, 92, (t - wt('expected')) / .25, '#ffd23a');
});
// ===== 6 · gemiler karadan =====
S(47.88, 51.08, (ctx, lt, t) => { // yağlı kütükler diziliyor
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 };
  tepe(ctx, cam, t); applyCam(ctx, cam, .5); ctx.fillStyle = '#5f8a3e'; ctx.beginPath(); ctx.moveTo(-500, 1240); ctx.quadraticCurveTo(540, 700, 1600, 1240); ctx.lineTo(1600, 2600); ctx.lineTo(-500, 2600); ctx.fill();
  applyCam(ctx, cam, 1);
  const n = Math.floor(clamp(lt / 2.6) * 9); for (let i = 0; i < n; i++) { const x = 60 + i * 120, y = hillY(x, 1240, 700) - 16; kutuk(ctx, x, y, 18, 110, 1); }
  for (let i = 0; i < 3; i++) { const x = 200 + i * 300; yeniceri(ctx, x, hillY(x, 1240, 700) + 40, 170, { lean: .3, arms: { L: [1.1, -.5], R: [1.1, -.5] } }); sc(ctx); applyCam(ctx, cam, 1); ctx.fillStyle = '#3a2a1a'; ctx.fillRect(x + 20, hillY(x, 1240, 700) - 50, 60, 30); }
  buyukYazi(ctx, 'GREASED LOGS', 540, 330, 104, (t - wt('greased')) / .25, '#ffd23a'); etiket(ctx, 'GALATA', 540, 490, 60, (t - wt('galata')) / .25, { col: '#fff', bg: '#2e7d4f' });
});
S(51.08, 54.12, (ctx, lt, t) => { // 70 gemi karadan
  const hh = handheld(t, 3), cam = { x: 540 + hh[0] + lt * 30, y: 1000 + hh[1], z: .95 };
  tepe(ctx, cam, t); applyCam(ctx, cam, .4); ctx.fillStyle = '#5f8a3e'; ctx.beginPath(); ctx.moveTo(-500, 1250); ctx.quadraticCurveTo(540, 600, 1600, 1250); ctx.lineTo(1600, 2600); ctx.lineTo(-500, 2600); ctx.fill();
  const hill = x => hillY(x, 1250, 600);
  for (let k = 0; k < 4; k++) { const px = ((lt * 260 + k * 420) % 1700) - 300, py = hill(px), sl = Math.atan2(hill(px + 20) - hill(px - 20), 40); kadirga(ctx, px, py - 10, .42, t + k, { rot: sl, oars: 0 }); for (let j = 0; j < 2; j++) yeniceri(ctx, px + 160 + j * 60, hill(px + 160 + j * 60), 100, { lean: .55, arms: { L: [1.4, -.2], R: [1.4, -.2] }, legs: { L: [Math.sin(t * 9 + j) * .5, -.3], R: [-Math.sin(t * 9 + j) * .5, -.3] } }); }
  sc(ctx); const c = Math.round(lerp(0, 70, easeOut(clamp((t - wt('seventy')) / .8)))); if (t > wt('seventy') - .1) buyukYazi(ctx, `~${c} SHIPS`, 540, 330, 120, (t - wt('seventy')) / .25, '#ffd23a');
  etiket(ctx, 'OVER LAND', 540, 500, 64, (t - wt('over', 52)) / .25);
});
S(54.12, 59.6, (ctx, lt, t) => { // sabah: filo limanın içinde
  const hh = handheld(t, 2), z = kf(lt, [[0, 1.0], [2.2, 1.0], [2.8, 1.25, easeOut]]), cam = { x: 540 + hh[0], y: 1000 + hh[1], z };
  applyCam(ctx, cam, .05); drawSky(ctx, '#ff9a5a', '#ffe0a0', -300, 1000); applyCam(ctx, cam, .1); drawSun(ctx, 200, 900, 120, t, .6);
  applyCam(ctx, cam, .2); drawSea(ctx, 1000, t, 2600); applyCam(ctx, cam, .5);
  for (let i = 0; i < 4; i++) kadirga(ctx, 120 + i * 250, 1090 + (i % 2) * 30, .35, t + i);
  applyCam(ctx, cam, 1); surlar(ctx, -200, 1500, 1500, 260, { towers: [] });
  for (let i = 0; i < 3; i++) bizAsker(ctx, 300 + i * 240, 1260, 240, { flip: 1, arms: lt > 2.2 ? { L: [2.4, .3], R: [2.4, .3] } : { L: [.3, -.2], R: [.3, -.2] }, face: lt > 2.2 ? { eyes: 'wide', mouth: 'o', browAng: -.3 } : { eyes: 'half', mouth: 'flat' } });
  if (lt > 2.2) { sc(ctx); for (const x of [300, 540, 780]) { buyukYazi(ctx, '!', x, 830, 120, (lt - 2.2) / .2, '#ff4a3a'); } }
  buyukYazi(ctx, 'INSIDE THE HARBOR', 540, 330, 86, (t - wt('inside')) / .25, '#ffd23a');
});
// ===== 7 · 53 gün, son saldırı =====
S(59.6, 64.68, (ctx, lt, t) => {
  const hh = handheld(t, 4), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 + lt * .03 };
  tepe(ctx, cam, t, { gece: .7 }); applyCam(ctx, cam, .7); surlar(ctx, -200, 1240, 1500, 620, { towers: [250, 850], dark: .3 });
  applyCam(ctx, cam, 1); ctx.fillStyle = '#3a2a24'; ctx.fillRect(-600, 1240, 2300, 1400);
  for (let i = 0; i < 3; i++) { const lx = 160 + i * 340; line(ctx, lx, 1240, lx + 120, 640, 12, '#6a4a2a'); line(ctx, lx + 40, 1240, lx + 160, 640, 12, '#6a4a2a'); for (let r = 0; r < 8; r++) line(ctx, lx + r * 15, 1240 - r * 75, lx + 40 + r * 15, 1240 - r * 75, 8, '#6a4a2a'); const cl = ((lt * .4 + i * .3) % 1); yeniceri(ctx, lx + 20 + cl * 110, 1240 - cl * 560, 150, { arms: { L: [2.2, -.2], R: [2.0, -.3] }, legs: { L: [Math.sin(t * 9) * .5, -.4], R: [-Math.sin(t * 9) * .5, -.4] } }); }
  sancak(ctx, 940, 1240, 300, t);
  sc(ctx); const d = Math.round(lerp(1, 53, clamp((t - wt('fifty-three') + .1) / .8))); if (t > wt('fifty-three') - .1) buyukYazi(ctx, `DAY ${d}`, 540, 330, 130, (t - wt('fifty-three')) / .25, '#ffd23a');
  etiket(ctx, 'MAY 29, 1453', 540, 500, 64, (t - wt('may')) / .25, { col: '#fff', bg: '#c4161c' });
});
// ===== 8 · son imparator =====
S(64.68, 71.76, (ctx, lt, t) => {
  const hh = handheld(t, 3), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 + lt * .02 };
  nightCastle(ctx, cam, t, .5); applyCam(ctx, cam, 1); ctx.fillStyle = '#1a1014'; ctx.fillRect(-400, 1240, 1900, 1200);
  const off = clamp((t - wt('threw')) / .6), ch = clamp((t - wt('charged')) / .6);
  const x = 540 + ch * 260;
  konstantin(ctx, x, 1240, 520, t, { robe: 1 - off, armor: off > .5, arms: ch > 0 ? { L: [.6, -.3], R: [2.6, -.4] } : { L: [.4, -.3], R: [.4, -.3] }, legs: ch > 0 ? { L: [Math.sin(t * 10) * .5, -.3], R: [-Math.sin(t * 10) * .5, -.3] } : undefined, face: { eyes: 'normal', mouth: ch > 0 ? 'o' : 'flat', browAng: .5 },
    prop: (c, k, p, ang, side) => { if (k !== 'R' || ch <= 0) return; c.save(); c.translate(p[0], p[1]); c.rotate(-ang * side); c.beginPath(); c.moveTo(-.016, 0); c.lineTo(.016, 0); c.lineTo(.012, .5); c.lineTo(0, .55); c.lineTo(-.012, .5); c.closePath(); c.fillStyle = '#e8ecf2'; c.fill(); c.lineWidth = .005; c.strokeStyle = INK; c.stroke(); c.restore(); } });
  if (off > 0 && off < 1.6) { applyCam(ctx, cam, 1); ctx.save(); ctx.translate(x - 260 - off * 80, 1240 - 200 + off * 180); ctx.rotate(off * 1.2); ctx.globalAlpha = clamp(1.4 - off); rrect(ctx, -110, -80, 220, 160, 30); fillStroke(ctx, '#5a1a7a', 6); ctx.restore(); }
  etiket(ctx, 'CONSTANTINE XI', 540, 330, 70, (t - wt('constantine')) / .25, { col: '#fff', bg: '#5a1a7a' }); etiket(ctx, 'LAST ROMAN EMPEROR', 540, 470, 48, (t - wt('roman', 64)) / .25);
  etiket(ctx, 'LEGEND', 860, 620, 46, (lt - .1) / .25, { col: '#1b1820', bg: '#ffd23a', rot: .08 });
});
S(71.76, 74.14, (ctx, lt, t) => { // taç yerde
  const cam = { x: 540, y: 1000, z: 1.05 + lt * .05 }; nightCastle(ctx, cam, t, .8); applyCam(ctx, cam, 1); ctx.fillStyle = '#1a1014'; ctx.fillRect(-400, 1240, 1900, 1200);
  ctx.save(); ctx.translate(540, 1200); crown(ctx, 0, 60, 70, 600); ctx.restore(); puff(ctx, 300, 1180, 120, t, '#5a4a52', 2, .6); puff(ctx, 820, 1160, 140, t, '#5a4a52', 5, .6);
  buyukYazi(ctx, 'NEVER FOUND', 540, 360, 120, (t - wt('identified')) / .25, '#fff');
});
// ===== 9 · bin yıl, tek sabah =====
S(74.14, 79.12, (ctx, lt, t) => {
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 + lt * .04 };
  applyCam(ctx, cam, .05); drawSky(ctx, '#ff9a5a', '#ffe0a0', -300, 1100); kubbeler(ctx, cam);
  applyCam(ctx, cam, .25); const fl = clamp((lt - 2.2) / .6); line(ctx, 540, 590, 540, 380, 8); ctx.save(); ctx.translate(540, 400); ctx.scale(1, 1 - fl * 2 > -1 ? 1 : 1);
  if (fl < .5) { rrect(ctx, 0, 0, 220, 140, 6); fillStroke(ctx, '#e3b23c', 5); circle(ctx, 110, 70, 40); ctx.fillStyle = '#1b1820'; ctx.fill(); } else { rrect(ctx, 0, 0, 220, 140, 6); fillStroke(ctx, '#c4161c', 5); circle(ctx, 95, 70, 45); ctx.fillStyle = '#fff'; ctx.fill(); circle(ctx, 112, 70, 37); ctx.fillStyle = '#c4161c'; ctx.fill(); }
  ctx.restore(); flas(ctx, Math.max(0, .6 - Math.abs(fl - .5) * 3));
  buyukYazi(ctx, '1,000 YEARS', 540, 1000, 120, (t - wt('thousand', 74)) / .25, '#ffd23a'); buyukYazi(ctx, '1 MORNING', 540, 1150, 120, (t - wt('single')) / .25, '#ff4a3a');
});
// ===== 10 · dünya değişti: âlimler İtalya'ya, Rönesans =====
function alim(ctx, x, y, s, o = {}) { drawStick(ctx, C({ cols: ['#3a5a8a', '#3a5a8a'], hat: 'none', belt: true }, Object.assign({ x, y, s, shadow: false }, o))); const r = .19 * s, hy = y - .765 * s; ctx.beginPath(); ctx.moveTo(x - r * .6, hy + r * .3); ctx.quadraticCurveTo(x, hy + r * 1.6, x + r * .6, hy + r * .3); fillStroke(ctx, '#e8e4dc', .01 * s); ctx.beginPath(); ctx.ellipse(x, hy - r * .8, r * .95, r * .5, 0, Math.PI, 0); fillStroke(ctx, '#2a2a3a', .014 * s); }
function kitap(ctx, x, y, w, h, renk = '#8a2a2a', rot = 0) { ctx.save(); ctx.translate(x, y); ctx.rotate(rot); rrect(ctx, -w / 2, -h / 2, w, h, 6); fillStroke(ctx, renk, 5); ctx.fillStyle = '#f4ead2'; ctx.fillRect(w / 2 - 10, -h / 2 + 6, 6, h - 12); ctx.fillStyle = '#e3b23c'; ctx.fillRect(-w / 2 + 8, -h * .1, w * .6, 8); ctx.restore(); }
S(79.12, 81.54, (ctx, lt, t) => { // dünya döner
  sc(ctx); const g = ctx.createRadialGradient(540, 820, 50, 540, 900, 1100); g.addColorStop(0, '#1a2a4a'); g.addColorStop(1, '#070a14'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  for (let k = 0; k < 40; k++) { const R = rng(k + 9); circle(ctx, R() * W, R() * 1500, 2 + R() * 3); ctx.fillStyle = `rgba(255,255,230,${.4 + .4 * Math.sin(t * 3 + k)})`; ctx.fill(); }
  const r = 330 * backOut(clamp(lt / .5)); ctx.save(); circle(ctx, 540, 860, r); ctx.fillStyle = '#2f7ac9'; ctx.fill(); ctx.clip();
  for (let i = 0; i < 6; i++) { const x = 540 - r + ((i * 230 + t * 160) % (2 * r + 400)) - 200, y = 860 + Math.sin(i * 2.1) * r * .5; ellipse(ctx, x, y, 110 + (i % 3) * 30, 70 + (i % 2) * 40, i); ctx.fillStyle = '#4fae5a'; ctx.fill(); }
  ctx.restore(); circle(ctx, 540, 860, r); ctx.lineWidth = 10; ctx.strokeStyle = INK; ctx.stroke();
  buyukYazi(ctx, 'THE WORLD', 540, 330, 120, (t - wt('world', 79)) / .25, '#fff'); buyukYazi(ctx, 'CHANGED', 540, 470, 120, (t - wt('changed', 79)) / .25, '#ffd23a');
}, 'whip');
S(81.54, 86.68, (ctx, lt, t) => { // âlimler kitaplarla İtalya'ya
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 };
  deniz(ctx, cam, t, 1000); applyCam(ctx, cam, .3); ctx.fillStyle = '#7d8a5a'; ctx.beginPath(); ctx.moveTo(820, 1010); ctx.quadraticCurveTo(1000, 900, 1300, 960); ctx.lineTo(1300, 1100); ctx.lineTo(820, 1100); ctx.fill();
  applyCam(ctx, cam, 1); const x = lerp(120, 520, clamp(lt / 5));
  kadirga(ctx, x, 1180, .9, t, { hull: '#5a3a22', flag: '#e3b23c' });
  for (let i = 0; i < 3; i++) { const ax = x - 170 + i * 110; alim(ctx, ax, 1110, 150, { arms: { L: [.3, -.2], R: { ik: [.25, -.45] } }, face: { eyes: 'normal', mouth: i === 1 ? 'o' : 'flat', look: [.6, -.1] } }); kitap(ctx, ax + 30, 1110 - 150 * .5, 46, 60, ['#8a2a2a', '#2a5a8a', '#3a7a3a'][i], .2); }
  for (let i = 0; i < 4; i++) kitap(ctx, x + 120 + i * 30, 1085 - i * 14, 70, 22, ['#8a2a2a', '#2a5a8a', '#3a7a3a', '#7a5a2a'][i], 0);
  etiket(ctx, 'GREEK SCHOLARS', 540, 330, 76, (t - wt('greek', 81)) / .25); etiket(ctx, 'ITALY', 900, 760, 64, (t - wt('italy', 82)) / .25, { col: '#fff', bg: '#2e7d4f', rot: .05 });
  etiket(ctx, 'ANCIENT BOOKS', 540, 500, 56, (t - wt('ancient', 84)) / .25, { col: '#1b1820', bg: '#ffd23a' });
});
S(86.68, 92.5, (ctx, lt, t) => { // Rönesans
  const hh = handheld(t, 2), cam = { x: 540 + hh[0], y: 1000 + hh[1], z: 1.0 + lt * .03 };
  applyCam(ctx, cam, .05); drawSky(ctx, '#ff9a5a', '#ffe0a0', -300, 1100); applyCam(ctx, cam, .25); ctx.fillStyle = '#c96a3a';
  ctx.fillRect(380, 820, 320, 300); ctx.beginPath(); ctx.moveTo(400, 820); ctx.quadraticCurveTo(540, 520, 680, 820); ctx.fill(); ctx.fillStyle = '#f2ece0'; ctx.fillRect(520, 560, 40, 60); for (let i = 0; i < 4; i++) { ctx.fillStyle = '#e8dcc0'; ctx.fillRect(400 + i * 90, 900, 30, 220); }
  for (const [x, h] of [[150, 260], [900, 300], [260, 180], [800, 200]]) { ctx.fillStyle = '#d9a070'; ctx.fillRect(x - 60, 1120 - h, 120, h); ctx.fillStyle = '#b04a2a'; ctx.beginPath(); ctx.moveTo(x - 75, 1120 - h); ctx.lineTo(x, 1120 - h - 60); ctx.lineTo(x + 75, 1120 - h); ctx.fill(); }
  applyCam(ctx, cam, 1); ctx.fillStyle = '#b8a070'; ctx.fillRect(-600, 1240, 2300, 1400);
  alim(ctx, 400, 1240, 330, { arms: { L: [1.0, -1.4], R: [1.0, -1.4] }, face: { eyes: 'happy', mouth: 'smile', look: [.5, .3] } });
  const gl = .5 + .5 * Math.sin(t * 4); ctx.save(); ctx.globalCompositeOperation = 'lighter'; const rg = ctx.createRadialGradient(560, 1010, 10, 560, 1010, 260); rg.addColorStop(0, `rgba(255,230,140,${.5 + .2 * gl})`); rg.addColorStop(1, 'rgba(255,200,80,0)'); ctx.fillStyle = rg; ctx.fillRect(300, 750, 520, 520); ctx.restore();
  kitap(ctx, 560, 1010, 150, 100, '#8a2a2a', -.2);
  for (let i = 0; i < 5; i++) { const k = (t * .3 + i / 5) % 1; ctx.save(); ctx.globalAlpha = Math.sin(k * Math.PI); text(ctx, ['α', 'β', 'Ω', 'π', 'Σ'][i], 620 + i * 70, 960 - k * 360, 60, '#ffe9a8', INK, 4, 'Poppins', 700); ctx.restore(); }
  buyukYazi(ctx, 'RENAISSANCE', 540, 330, 116, (t - wt('renaissance', 86)) / .25, '#ffd23a');
  etiket(ctx, 'END OF THE MIDDLE AGES', 540, 500, 54, (t - wt('end', 90)) / .25, { col: '#fff', bg: '#c4161c', rot: -.04 });
}, 'whip');
// ===== 11 · soru + kapanış =====
S(92.5, 97.52, (ctx, lt, t) => {
  sc(ctx); ctx.fillStyle = '#1b2a1e'; ctx.fillRect(0, 0, W / 2, H); ctx.fillStyle = '#2a1a1a'; ctx.fillRect(W / 2, 0, W / 2, H);
  const cam = { x: 540, y: 1000, z: 1 }; applyCam(ctx, cam, 1);
  mehmed(ctx, 270, 1240, 360, { arms: { L: [.5, -.4], R: { ik: [.12, -.66] } }, face: { eyes: 'smug', mouth: 'smirk' } });
  ctx.save(); ctx.beginPath(); ctx.rect(540, 0, 540, 1600); ctx.clip(); surlar(ctx, 600, 1240, 500, 500, { towers: [] }); ctx.restore();
  sc(ctx); ctx.fillStyle = '#fff'; ctx.fillRect(536, 0, 8, H);
  buyukYazi(ctx, 'GENIUS', 270, 420, 104, (t - wt('genius')) / .25, '#ffd23a'); buyukYazi(ctx, 'LUCK', 810, 420, 120, (t - wt('luck')) / .25, '#ff4a3a');
  etiket(ctx, 'COMMENTS', 540, 1560, 70, (t - wt('comments')) / .2, { col: '#fff', bg: '#c4161c', rot: 0 });
});
S(97.52, 103.0, (ctx, lt, t) => logoKart(ctx, lt, t, true), 'cut');
