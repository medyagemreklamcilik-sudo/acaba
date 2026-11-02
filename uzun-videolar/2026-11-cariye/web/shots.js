// "Osmanlı Sarayında Bir Cariye Olsaydın" · 16:9 · gerçek görsel + stickman
// Zamanlar: PT[k] = k. paragrafın başlangıcı (words.js), wt('kelime', t0) = t0'dan sonra o kelimenin başladığı an.
const IMG = {};
['harem_kapi', 'altin_yol', 'koridor2', 'tasligi', 'avlu', 'mutfak', 'hunkar', 'valide', 'kubbe', 'hamam', 'valide_tasligi', 'avlu2', 'babussaade',
 'koy', 'koy2', 'koy3', 'deniz_gece', 'deniz_firtina', 'istanbul_gunbatimi', 'carsi', 'istanbul_cami', 'esir_pazari', 'uskudar', 'uskudar2', 'vanmour',
 'kanun', 'muzisyen', 'levni1', 'levni2', 'levni3', 'elizabeth', 'hurrem', 'darussaade', 'nakis1', 'nakis2', 'kandil', 'melling', 'melling2', 'harita']
  .forEach(k => { const i = new Image(); i.src = 'img/' + k + '.jpg'; IMG[k] = i; });
const norm = s => s.toLocaleLowerCase('tr').replace(/[^\p{L}\p{N}]/gu, '');
function wt(word, t0 = 0) { const q = norm(word); const w = WORDS.find(w => w.s >= t0 - .01 && norm(w.w).startsWith(q)); if (!w) console.log('WT MISS', word, t0); return w ? w.s : t0; }
const C = (a, b) => Object.assign({}, a, b);
const sc = ctx => ctx.setTransform(1, 0, 0, 1, 0, 0);

// ---------- arka plan ----------
function bg(ctx, key, lt, dur, o = {}) {
  sc(ctx); const im = IMG[key]; ctx.fillStyle = '#0b0a10'; ctx.fillRect(0, 0, W, H);
  if (!im || !im.naturalWidth) return;
  const u = clamp(lt / Math.max(1, dur)), z = lerp(o.z?.[0] ?? 1.04, o.z?.[1] ?? 1.14, ease(u));
  const p0 = o.p?.[0] ?? [.5, .5], p1 = o.p?.[1] ?? p0, px = lerp(p0[0], p1[0], u), py = lerp(p0[1], p1[1], u);
  const k = Math.max(W / im.naturalWidth, H / im.naturalHeight) * z, iw = im.naturalWidth * k, ih = im.naturalHeight * k;
  const x = clamp(W / 2 - px * iw, W - iw, 0), y = clamp(H / 2 - py * ih, H - ih, 0);
  ctx.save(); if (o.blur || o.bri != null) ctx.filter = `blur(${o.blur || 0}px) brightness(${o.bri ?? 1}) saturate(${o.sat ?? 1})`;
  ctx.drawImage(im, x, y, iw, ih); ctx.restore();
}
const TONES = { koy: ['#f2c86a', .32], soguk: ['#5a7aa8', .55], harem: ['#6a1a2a', .5], altin: ['#ffcf6a', .38], sabah: ['#ffe3b0', .3], gece: ['#1a2a5a', .6], gri: ['#808080', .0] };
function tone(ctx, name, a = 1) { const t = TONES[name]; if (!t || a <= 0) return; sc(ctx); ctx.save(); ctx.globalCompositeOperation = 'soft-light'; ctx.globalAlpha = t[1] * a; ctx.fillStyle = t[0]; ctx.fillRect(0, 0, W, H); ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = .08 * a; ctx.fillRect(0, 0, W, H); ctx.restore(); }
function karart(ctx, a) { if (a <= 0) return; sc(ctx); ctx.fillStyle = `rgba(0,0,0,${clamp(a)})`; ctx.fillRect(0, 0, W, H); }
function flas(ctx, a) { if (a <= 0) return; sc(ctx); ctx.fillStyle = `rgba(255,255,255,${clamp(a)})`; ctx.fillRect(0, 0, W, H); }
function kandilIsigi(ctx, x, y, r, a = 1, t = 0) { sc(ctx); ctx.save(); ctx.globalCompositeOperation = 'lighter'; const f = 1 + Math.sin(t * 13) * .05; const g = ctx.createRadialGradient(x, y, 5, x, y, r * f); g.addColorStop(0, `rgba(255,190,100,${.55 * a})`); g.addColorStop(1, 'rgba(255,150,60,0)'); ctx.fillStyle = g; ctx.fillRect(x - r * 1.2, y - r * 1.2, r * 2.4, r * 2.4); ctx.restore(); }

// ---------- yazılar ----------
function etiket(ctx, str, x, y, size, ap, { col = '#ffd23a', bg = '#16121a', rot = 0, al = 'center' } = {}) {
  if (ap <= 0) return; sc(ctx); ctx.save(); ctx.translate(x, y); ctx.rotate(rot); const k = lerp(1.35, 1, easeOut(clamp(ap))); ctx.scale(k, k); ctx.globalAlpha = clamp(ap * 2.5);
  ctx.font = `700 ${size}px Poppins`; const tw = ctx.measureText(str).width + size * .9; const ox = al === 'left' ? tw / 2 : 0;
  rrect(ctx, -tw / 2 + ox, -size * .75, tw, size * 1.45, size * .18); ctx.fillStyle = bg; ctx.fill(); ctx.lineWidth = size * .07; ctx.strokeStyle = col; ctx.stroke();
  text(ctx, str, ox, size * .05, size, col, INK, 0, 'Poppins', 700); ctx.restore();
}
function damga(ctx, str, x, y, size, ap, col = '#e0262f', rot = -.1) {
  if (ap <= 0) return; sc(ctx); ctx.save(); ctx.translate(x, y); ctx.rotate(rot); const k = lerp(2.2, 1, easeOut(clamp(ap / .6))); ctx.scale(k, k); ctx.globalAlpha = clamp(ap * 3);
  ctx.font = `700 ${size}px Poppins`; const tw = ctx.measureText(str).width + size * .7;
  rrect(ctx, -tw / 2, -size * .72, tw, size * 1.4, size * .12); ctx.lineWidth = size * .11; ctx.strokeStyle = col; ctx.stroke();
  text(ctx, str, 0, size * .05, size, col, INK, 0, 'Poppins', 700); ctx.restore();
}
function baslik(ctx, lines, ap, y = 470, size = 96, col = '#fff') {
  if (ap <= 0) return; sc(ctx); ctx.save(); ctx.globalAlpha = clamp(ap * 2);
  lines.forEach((l, i) => { const a = clamp(ap * 2 - i * .4); ctx.save(); ctx.translate(960, y + i * size * 1.18); const k = .85 + .15 * backOut(a); ctx.scale(k, k); ctx.globalAlpha = a; text(ctx, l, 0, 0, size, i === 0 ? col : '#ffd23a', INK, size * .13, 'Poppins', 700); ctx.restore(); });
  ctx.restore();
}
function hud(ctx, t) { // sağ üst rozetler: yıl + gün saati
  let yil = null;
  if (t >= PT[1] + 1 && t < PT[36]) yil = 'YIL 1598';
  else if (t >= PT[36] && t < PT[38]) yil = 'YIL ' + Math.round(lerp(1598, 1607, clamp((t - PT[36]) / (PT[38] - PT[36]))));
  else if (t >= PT[38] && t < PT[45]) yil = 'YIL 1607';
  const H_ = [[PT[8], PT[13], 'ŞAFAK'], [PT[13], PT[19], 'SABAH'], [PT[19], PT[26], 'ÖĞLE'], [PT[26], PT[30], 'İKİNDİ'], [PT[30], PT[33], 'AKŞAM'], [PT[33], PT[36], 'GECE']];
  const h = H_.find(([a, b]) => t >= a && t < b);
  sc(ctx); ctx.save(); ctx.font = '700 34px Poppins'; let y = 70;
  for (const s of [yil, h && h[2]].filter(Boolean)) { const tw = ctx.measureText(s).width + 40; rrect(ctx, 1860 - tw, y - 30, tw, 60, 30); ctx.fillStyle = s.startsWith('YIL') ? 'rgba(20,16,24,.78)' : 'rgba(255,201,60,.92)'; ctx.fill(); text(ctx, s, 1860 - tw / 2, y + 2, 34, s.startsWith('YIL') ? '#ffd23a' : '#1b1820', INK, 0, 'Poppins', 700); y += 74; }
  if (false) { // gün çizelgesi
    const i = H_.indexOf(h); for (let k = 0; k < 6; k++) { circle(ctx, 1560 + k * 50, y + 8, k === i ? 12 : 7); ctx.fillStyle = k < i ? '#ffd23a' : k === i ? '#ffc93c' : 'rgba(255,255,255,.35)'; ctx.fill(); }
  }
  ctx.restore();
}

// ---------- karakterler ----------
const RENK = { gul: '#86c97a', dil: '#8a5ac9', kalfa: '#7a5230', haz: '#8e1f2c', val: '#e3b23c', anne: '#8a6a48' };
function kadin(ctx, x, y, s, o = {}) {
  const renk = o.renk || RENK.gul, ortu = o.ortu === undefined ? '#ffffff' : o.ortu;
  drawStick(ctx, C({ x, y, s, cols: [renk, renk], hat: 'none', belt: false, shadow: o.shadow ?? false }, o));
  const lean = o.lean || 0;
  ctx.save(); ctx.translate(x, y); ctx.rotate(lean); ctx.scale(s * (o.flip || 1), s); if (o.alpha != null) ctx.globalAlpha = o.alpha;
  ctx.beginPath(); ctx.moveTo(-.13, -.33); ctx.lineTo(.13, -.33); ctx.lineTo(.22, -.03); ctx.quadraticCurveTo(0, .0, -.22, -.03); ctx.closePath(); fillStroke(ctx, renk, .017);
  ctx.save(); ctx.clip(); ctx.fillStyle = 'rgba(255,255,255,.18)'; for (let i = 0; i < 4; i++) ctx.fillRect(-.3, -.3 + i * .08, .6, .018); ctx.restore();
  const hy = -.765, r = .19;
  if (o.val) { ctx.beginPath(); ctx.moveTo(-r * .8, hy - r * .7); ctx.lineTo(-r * .55, hy - r * 2.3); ctx.quadraticCurveTo(0, hy - r * 2.55, r * .55, hy - r * 2.3); ctx.lineTo(r * .8, hy - r * .7); ctx.closePath(); fillStroke(ctx, '#e3b23c', .015); for (let i = 0; i < 5; i++) { circle(ctx, -r * .5 + i * r * .25, hy - r * .95, r * .07); ctx.fillStyle = '#fff6e0'; ctx.fill(); } }
  else if (ortu) {
    ctx.beginPath(); ctx.arc(0, hy, r * 1.16, Math.PI * 1.0, Math.PI * 2.0); ctx.lineTo(r * 1.16, hy + r * 1.3); ctx.quadraticCurveTo(r * 1.0, hy + r * 1.5, r * .82, hy + r * 1.2); ctx.lineTo(r * .9, hy - r * .1);
    ctx.arc(0, hy - r * .05, r * .9, -0.1, Math.PI + 0.1, true); ctx.lineTo(-r * .82, hy + r * 1.2); ctx.quadraticCurveTo(-r * 1.0, hy + r * 1.5, -r * 1.16, hy + r * 1.3); ctx.closePath(); fillStroke(ctx, ortu, .014);
  }
  if (o.anahtar) { line(ctx, .1, -.3, .14, -.2, .012); circle(ctx, .145, -.19, .02); ctx.lineWidth = .01; ctx.strokeStyle = '#d9a83a'; ctx.stroke(); }
  ctx.restore();
}
const gul = (ctx, x, y, s, o = {}) => kadin(ctx, x, y, s, C({ renk: RENK.gul, ortu: '#ffffff' }, o));
const dil = (ctx, x, y, s, o = {}) => kadin(ctx, x, y, s, C({ renk: RENK.dil, ortu: '#e8dcff' }, o));
const kalfa = (ctx, x, y, s, o = {}) => kadin(ctx, x, y, s, C({ renk: RENK.kalfa, ortu: '#efe6d6', anahtar: true }, o));
const haznedar = (ctx, x, y, s, o = {}) => kadin(ctx, x, y, s, C({ renk: RENK.haz, ortu: '#f2d7a0', anahtar: true }, o));
const valide = (ctx, x, y, s, o = {}) => kadin(ctx, x, y, s, C({ renk: RENK.val, val: true }, o));
const anne = (ctx, x, y, s, o = {}) => kadin(ctx, x, y, s, C({ renk: RENK.anne, ortu: '#d8c8a8' }, o));
function erkek(ctx, x, y, s, o = {}) { drawStick(ctx, C({ x, y, s, cols: ['#6a4a30', '#6a4a30'], hat: 'none', belt: true, shadow: false }, o)); const r = .19 * s; ctx.beginPath(); ctx.ellipse(x, y - .765 * s - r * .75, r * .95, r * .45, 0, Math.PI, 0); fillStroke(ctx, '#3a2a1a', .02 * s); }
function padisahSil(ctx, x, y, s, a = 1) { ctx.save(); ctx.globalAlpha = a; drawStick(ctx, { x, y, s, sil: '#0a0810', hat: 'none', belt: false, shadow: false }); const r = .19 * s, hy = y - .765 * s; ctx.beginPath(); ctx.ellipse(x, hy - r * .9, r * 1.1, r * .9, 0, 0, TAU); ctx.fillStyle = '#0a0810'; ctx.fill(); ctx.restore(); }
function uyuyan(ctx, x, y, s, renk = RENK.gul, o = {}) { // yerde yatan (sola doğru)
  kadin(ctx, x, y, s, C({ renk, lean: -Math.PI / 2, face: { eyes: 'normal', blink: o.uyanik ? 0 : 1, mouth: 'flat' }, arms: { L: [.2, -.1], R: [.2, -.1] } }, o));
  sc(ctx); rrect(ctx, x - s * .58, y - s * .2, s * .78, s * .2, s * .07); fillStroke(ctx, o.yorgan || '#c9b48a', 5);
}
function dosek(ctx, x, y, w, h, renk = '#c9b48a') { rrect(ctx, x, y, w, h, 14); fillStroke(ctx, renk, 5); rrect(ctx, x + 8, y + 8, w * .22, h - 16, 10); fillStroke(ctx, '#efe6d6', 4); }
function basortu(ctx, x, y, s, a = 1, rot = 0) { ctx.save(); sc(ctx); ctx.globalAlpha = a; ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s); ctx.beginPath(); ctx.moveTo(-1, -.4); ctx.quadraticCurveTo(0, -.7, 1, -.4); ctx.lineTo(.8, .5); ctx.quadraticCurveTo(0, .75, -.8, .5); ctx.closePath(); fillStroke(ctx, '#fbf8f1', .04); for (let i = 0; i < 3; i++) { ctx.beginPath(); ctx.moveTo(-.6 + i * .5, -.3); ctx.quadraticCurveTo(-.5 + i * .5, .1, -.6 + i * .5, .45); ctx.lineWidth = .02; ctx.strokeStyle = 'rgba(120,110,100,.35)'; ctx.stroke(); } ctx.restore(); }
function fincan(ctx, x, y, s, rot = 0, kirik = 0) {
  ctx.save(); sc(ctx); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  if (kirik <= 0) { ctx.beginPath(); ctx.moveTo(-.5, -.4); ctx.lineTo(.5, -.4); ctx.quadraticCurveTo(.48, .35, 0, .4); ctx.quadraticCurveTo(-.48, .35, -.5, -.4); fillStroke(ctx, '#f6f1e6', .05); ctx.fillStyle = '#2a63c9'; ctx.fillRect(-.45, -.2, .9, .1); ellipse(ctx, 0, .48, .6, .12); fillStroke(ctx, '#d9a83a', .04); }
  else { for (let i = 0; i < 6; i++) { const a = i / 6 * TAU, d = kirik * .9; ctx.save(); ctx.translate(Math.cos(a) * d, .3 + Math.sin(a) * d * .3); ctx.rotate(a * 2 * kirik); ctx.beginPath(); ctx.moveTo(-.15, -.1); ctx.lineTo(.18, -.05); ctx.lineTo(.05, .16); ctx.closePath(); fillStroke(ctx, '#f6f1e6', .03); ctx.restore(); } }
  ctx.restore();
}
function kapi(ctx, x, y, w, h, renk = '#5a3a20', acik = 0, yazi = '', hi = 0) {
  sc(ctx); ctx.save(); rrect(ctx, x - w / 2 - 14, y - h - 14, w + 28, h + 14, 18); fillStroke(ctx, '#d9a83a', 6);
  ctx.fillStyle = `rgba(255,236,180,${.85 * acik})`; ctx.fillRect(x - w / 2, y - h, w, h);
  ctx.save(); ctx.translate(x - w / 2, 0); ctx.scale(1 - acik * .75, 1); rrect(ctx, 0, y - h, w, h, 10); fillStroke(ctx, renk, 6); circle(ctx, w * .85, y - h / 2, 9); ctx.fillStyle = '#d9a83a'; ctx.fill(); ctx.restore();
  if (yazi) etiket(ctx, yazi, x, y + 60, 36, 1, { col: hi ? '#1b1820' : '#ffd23a', bg: hi ? '#ffd23a' : '#16121a' });
  ctx.restore();
}
function merdiven(ctx, steps, n, hi, ap, { x0 = 420, y0 = 900, dx = 230, dy = 120, renk = '#ffd23a', gulAt = -1 } = {}) {
  sc(ctx); steps.forEach((s, i) => { const a = clamp((n - i)); if (a <= 0) return; const x = x0 + i * dx, y = y0 - i * dy, k = backOut(clamp(a)); ctx.save(); ctx.globalAlpha = clamp(a * ap); ctx.translate(x, y); ctx.scale(k, k);
    rrect(ctx, -dx * .48, -40, dx * .96, 80, 14); ctx.fillStyle = i === hi ? renk : 'rgba(22,18,26,.86)'; ctx.fill(); ctx.lineWidth = 4; ctx.strokeStyle = renk; ctx.stroke();
    text(ctx, s, 0, 2, s.length > 12 ? 26 : 32, i === hi ? '#1b1820' : '#fff', INK, 0, 'Poppins', 700); ctx.restore(); });
  if (gulAt >= 0) { const x = x0 + gulAt * dx, y = y0 - gulAt * dy - 42; gul(ctx, x, y, 170, { face: { eyes: 'normal', mouth: 'flat', look: [.4, -.4] } }); }
}
function mektup(ctx, x, y, s, a = 1, rot = 0) { ctx.save(); sc(ctx); ctx.globalAlpha = a; ctx.translate(x, y); ctx.rotate(rot); rrect(ctx, -s, -s * .65, s * 2, s * 1.3, 6); fillStroke(ctx, '#f4ead2', 4); ctx.beginPath(); ctx.moveTo(-s, -s * .65); ctx.lineTo(0, s * .1); ctx.lineTo(s, -s * .65); ctx.lineWidth = 4; ctx.strokeStyle = INK; ctx.stroke(); circle(ctx, 0, s * .1, s * .18); ctx.fillStyle = '#b3202c'; ctx.fill(); ctx.restore(); }
function akce(ctx, x, y, r, a = 1) { ctx.save(); sc(ctx); ctx.globalAlpha = a; circle(ctx, x, y, r); fillStroke(ctx, '#d9d2c0', 4); circle(ctx, x, y, r * .62); ctx.lineWidth = 3; ctx.strokeStyle = '#9a9280'; ctx.stroke(); ctx.restore(); }
function buhar(ctx, t, a = 1) { sc(ctx); ctx.save(); for (let i = 0; i < 14; i++) { const k = (t * .12 + i / 14) % 1, x = 200 + (i * 137) % 1500, y = 1000 - k * 900; ctx.globalAlpha = .18 * a * Math.sin(k * Math.PI); circle(ctx, x + Math.sin(t + i) * 40, y, 90 + k * 160); ctx.fillStyle = '#fff'; ctx.fill(); } ctx.restore(); }
function harfler(ctx, t, a = 1) { sc(ctx); const H_ = ['ا', 'ب', 'ت', 'ج', 'د', 'ر', 'س', 'ع', 'ق', 'ك', 'ل', 'م', 'ن', 'و', 'ه', 'ي']; ctx.save(); ctx.font = '700 80px serif'; for (let i = 0; i < 16; i++) { const k = (t * .08 + i / 16) % 1; ctx.globalAlpha = a * .8 * Math.sin(k * Math.PI); ctx.fillStyle = '#ffe9a8'; ctx.fillText(H_[i], 120 + (i * 211) % 1680, 900 - k * 700); } ctx.restore(); }

const SHOTS = []; const NOCAP = [];
let _sonT = 0;
function S(start, end, draw, o = {}) {
  SHOTS.push({ start, end, tr: o.tr || 'cut', draw(ctx, lt, t) { draw(ctx, lt, t, end - start); if (o.dip) karart(ctx, 1 - clamp(lt / .35)); if (o.flash) flas(ctx, .8 * (1 - clamp(lt / .25))); hud(ctx, t); } });
}
const P = PT;

// ====================== 0 · KANCA (0 – 10.7) ======================
const tGunes = wt('güneş', 0), tOda = wt('kendi', tGunes), tAd = wt('kendi', tOda + .5);
S(0, tGunes, (ctx, lt, t, d) => {
  const z = kf(lt, [[0, 1.0], [.5, 1.0], [2.6, 1.35, easeIn]]);
  bg(ctx, 'harem_kapi', lt, d, { z: [z, z], p: [[.42, .55]] }); tone(ctx, 'harem', 1);
  gul(ctx, 1450, 1010, 320, { face: { eyes: 'wide', mouth: 'o', look: [-.5, -.5] } });
  karart(ctx, 1 - clamp((lt - .35) / .3));
  baslik(ctx, ['BİR GÜNÜN', 'NASIL GEÇERDİ?'], (lt - 1.2) / .4, 230, 84);
});
S(tGunes, tOda, (ctx, lt, t, d) => {
  bg(ctx, 'melling', lt, d, { z: [1.15, 1.25], bri: .45, blur: 2 }); tone(ctx, 'gece', 1); kandilIsigi(ctx, 1500, 300, 420, 1, t);
  for (let i = 0; i < 4; i++) uyuyan(ctx, 420 + i * 400, 900, 230, [RENK.gul, RENK.dil, '#c97a5a', '#5a8ac9'][i], { uyanik: i === 0 && lt > .8 });
  if (lt > 1) kalfa(ctx, 1700, 760, 330, { flip: -1, arms: { L: [.3, -.2], R: [2.2, .2] }, face: { eyes: 'normal', mouth: 'o', browAng: .4 } });
}, { flash: 1 });
S(tOda, tAd, (ctx, lt, t, d) => { // yukarıdan sıra sıra döşekler
  sc(ctx); ctx.fillStyle = '#2a1a22'; ctx.fillRect(0, 0, W, H); ctx.save(); ctx.translate(960, 540); ctx.rotate(lerp(-.05, .03, lt / d)); ctx.scale(1.1 + lt * .03, 1.1 + lt * .03); ctx.translate(-960, -540);
  for (let r = 0; r < 4; r++) for (let c = 0; c < 9; c++) dosek(ctx, 60 + c * 205, 90 + r * 240, 175, 200, ['#c9b48a', '#b8a078', '#d6c49a'][(r + c) % 3]);
  ctx.restore(); kandilIsigi(ctx, 960, 540, 700, .6, t); tone(ctx, 'harem', .8);
  damga(ctx, 'KENDİ ODAN YOK', 960, 540, 90, (lt - .2) / .25);
});
S(tAd, P[1], (ctx, lt, t, d) => { // MARİAM → GÜLNİHAL
  bg(ctx, 'harem_kapi', lt, d, { z: [1.2, 1.3], bri: .35, blur: 4 }); tone(ctx, 'harem', 1);
  sc(ctx); const sh = shake(t, 6, 3, 1); ctx.save(); ctx.translate(sh[0], sh[1]);
  text(ctx, 'MARİAM', 960, 430, 170, '#fbf8f1', INK, 16, 'Poppins', 700);
  const k = clamp((lt - .5) / .4); if (k > 0) { ctx.beginPath(); ctx.moveTo(560, 440); ctx.lineTo(560 + 800 * k, 425); ctx.lineWidth = 22; ctx.strokeStyle = '#e0262f'; ctx.lineCap = 'round'; ctx.stroke(); }
  const g = clamp((lt - 1.0) / .4); if (g > 0) { ctx.globalAlpha = g; text(ctx, 'GÜLNİHAL', 960, 700, 150, '#ffd23a', INK, 14, 'Poppins', 700); }
  ctx.restore();
});
// ====================== 1 · BAŞLIK (10.7 – 23.3) ======================
NOCAP.push([P[1], P[1] + 4.6]);
S(P[1], P[2], (ctx, lt, t, d) => {
  bg(ctx, lt < 6 ? 'babussaade' : 'harem_kapi', lt < 6 ? lt : lt - 6, 6, { z: [1.02, 1.14] }); tone(ctx, 'altin', .8);
  karart(ctx, .35 * clamp(lt / .5) * (1 - clamp((lt - 4.5) / .5)));
  baslik(ctx, ['OSMANLI SARAYINDA', 'BİR CARİYE OLSAYDIN'], clamp(lt / .4) * (1 - clamp((lt - 4.3) / .3)), 440, 104);
  etiket(ctx, 'TOPKAPI SARAYI · 1598', 960, 760, 44, (lt - .8) / .3 * (lt < 4.6 ? 1 : 0));
  if (lt > 6) { gul(ctx, 520, 1060, 260, { face: { eyes: 'normal', mouth: 'flat', look: [.6, -.3] } }); etiket(ctx, 'SAAT SAAT BİR GÜN', 1300, 300, 46, (lt - 6.3) / .3); }
}, { dip: 1 });
// ====================== 2 · KÖY (23.3 – 37) ======================
const tKafkas = wt('kafkas', P[2]), tAnne = wt('annen', P[2]), tDere = wt('akşamları', P[2]), tHayal = wt('en', tDere);
S(P[2], tKafkas + 1.6, (ctx, lt, t, d) => { // harita
  bg(ctx, 'harita', lt, d, { z: [1.0, 1.06], p: [[.6, .45], [.5, .5]] }); tone(ctx, 'koy', .5);
  sc(ctx); const k = clamp((lt - .6) / 1.6); const A = [1371, 450], B = [1200, 424], Cc = [926, 510], D = [651, 570], E = [479, 646];
  ctx.save(); ctx.setLineDash([22, 16]); ctx.lineWidth = 8; ctx.strokeStyle = '#ffd23a'; ctx.beginPath(); ctx.moveTo(...A); ctx.bezierCurveTo(...B, ...Cc, ...D); ctx.lineTo(...E); ctx.stroke(); ctx.restore();
  ctx.save(); ctx.globalCompositeOperation = 'destination-out'; ctx.restore();
  circle(ctx, ...A, 16); ctx.fillStyle = '#e0262f'; ctx.fill(); circle(ctx, ...E, 16); ctx.fill();
  etiket(ctx, 'KAFKASYA', 1470, 380, 40, (lt - .2) / .3); etiket(ctx, 'İSTANBUL', 380, 720, 40, (lt - 1.6) / .3); etiket(ctx, "1.000 KM'DEN FAZLA", 900, 300, 48, (lt - 2.0) / .3);
  karart(ctx, (1 - k) * 0);
});
S(tKafkas + 1.6, tDere, (ctx, lt, t, d) => {
  bg(ctx, 'koy', lt, d, { z: [1.05, 1.18], p: [[.4, .5], [.6, .5]] }); tone(ctx, 'koy', 1);
  anne(ctx, 560, 1000, 300, { arms: { L: [1.4, -1.2], R: [1.4, -1.2] }, face: { eyes: 'happy', mouth: 'smile' } });
  erkek(ctx, 1380, 1000, 300, { arms: { L: [.4, -.2], R: [2.1, .2] }, face: { eyes: 'normal', mouth: 'smile' } });
  gul(ctx, 900 + Math.sin(lt * 3) * 60, 1010, 190, { ...{ legs: { L: [Math.sin(lt * 9) * .5, -.3], R: [-Math.sin(lt * 9) * .5, -.3] } }, face: { eyes: 'happy', mouth: 'grin' } });
  etiket(ctx, 'MARİAM', 900, 640, 40, (lt - .3) / .3);
});
S(tDere, P[3], (ctx, lt, t, d) => {
  bg(ctx, 'koy3', lt, d, { z: [1.1, 1.22], p: [[.5, .65]] }); tone(ctx, 'koy', 1.2); tone(ctx, 'altin', .6);
  anne(ctx, 820, 900, 300, { face: { eyes: 'happy', mouth: 'smile', look: [.5, 0] } }); gul(ctx, 1040, 900, 200, { face: { eyes: 'happy', mouth: 'smile', look: [-.5, -.3] } });
  etiket(ctx, 'HAYALİ: DENİZİ GÖRMEK', 960, 230, 50, (t - tHayal) / .3);
});
// ====================== 3 · ALINIŞ (37 – 57.2) ======================
const tGos = wt('o', P[3] + 1.5), tKole = wt('cariyelik', P[3]), tBas = wt('annenden', P[3]);
S(P[3], tGos, (ctx, lt, t, d) => {
  bg(ctx, 'koy2', lt, d, { z: [1.05, 1.2], sat: .2 }); tone(ctx, 'soguk', 1.2);
  sc(ctx); for (let i = 0; i < 5; i++) { const x = 1250 + i * 110 - lt * 30, y = 420 + (i % 2) * 18; ctx.save(); ctx.translate(x, y); ctx.fillStyle = '#0a0a10'; ellipse(ctx, 0, 0, 48, 20); ctx.fill(); ctx.fillRect(28, -40, 14, 40); ctx.fillRect(-36, 5, 8, 40); ctx.fillRect(30, 5, 8, 40); circle(ctx, 0, -62, 13); ctx.fill(); ctx.fillRect(-6, -52, 12, 30); ctx.restore(); }
  ctx.fillStyle = '#000'; const bar = 110 * clamp(lt / .6); ctx.fillRect(0, 0, W, bar); ctx.fillRect(0, H - bar, W, bar);
}, { tr: 'cut' });
S(tGos, tKole, (ctx, lt, t, d) => {
  bg(ctx, 'koy2', lt, d, { z: [1.2, 1.3], bri: .25, blur: 8, sat: .1 }); tone(ctx, 'soguk', 1);
  baslik(ctx, ['O GÜNÜ', 'GÖSTERMEYECEĞİZ'], lt / .4, 420, 84);
}, { dip: 1 });
const tSav = wt('saraya', tKole);
S(tKole, tSav, (ctx, lt, t, d) => {
  bg(ctx, 'koy2', lt, d, { z: [1.25, 1.35], bri: .3, blur: 6, sat: .1 }); tone(ctx, 'soguk', 1);
  damga(ctx, 'CARİYELİK = KÖLELİK', 960, 480, 96, lt / .3, '#e0262f', -.05);
});
S(tSav, tBas, (ctx, lt, t, d) => {
  bg(ctx, 'koy2', lt, d, { z: [1.1, 1.22], p: [[.6, .5], [.4, .5]], sat: .15, bri: .7 }); tone(ctx, 'soguk', 1.2);
  for (let i = 0; i < 3; i++) kadin(ctx, 1150 + i * 190 - lt * 25, 960, 200, { renk: ['#7a7a8a', '#8a7a6a', '#6a7a8a'][i], ortu: '#cfcfcf', face: { eyes: 'normal', mouth: 'frown', browAng: -.3, look: [-.6, .2] }, legs: { L: [Math.sin(t * 4 + i) * .3, -.2], R: [-Math.sin(t * 4 + i) * .3, -.2] } });
  etiket(ctx, 'SAVAŞ ESİRLERİ', 520, 260, 50, (t - wt('savaşta', tSav)) / .3);
  etiket(ctx, 'KAÇIRILAN ÇOCUKLAR', 520, 380, 50, (t - wt('çocukken', tSav)) / .3);
});
S(tBas, P[4], (ctx, lt, t, d) => {
  bg(ctx, 'koy2', lt, d, { z: [1.2, 1.3], bri: .4, blur: 6, sat: .2 }); tone(ctx, 'soguk', 1.4);
  sc(ctx); drawStick(ctx, { x: 700, y: 1180, s: 900, cols: [RENK.anne, RENK.anne], hat: 'none', belt: false, shadow: false, arms: { L: [.3, -.1], R: { ik: [.55, -.5] } }, face: { eyes: 'normal', mouth: 'frown', browAng: -.3 } });
  const k = easeOut(clamp(lt / 2)); basortu(ctx, lerp(1080, 1180, k), lerp(600, 620, k), 130, 1, -.1);
  drawStick(ctx, { x: 1450, y: 1180, s: 620, cols: [RENK.gul, RENK.gul], hat: 'none', belt: false, shadow: false, flip: -1, arms: { L: [.3, -.1], R: { ik: [.45, -.45] } }, face: { eyes: 'wide', mouth: 'o', browAng: -.3 } });
});
// ====================== 4 · GEMİ, İSTANBUL (57.2 – 69.6) ======================
const tVardi = wt('gemi', P[4] + 3), tKapi = wt('ve', tVardi + 1.5);
S(P[4], tVardi, (ctx, lt, t, d) => {
  const r = Math.sin(t * 1.4) * .02; bg(ctx, 'deniz_gece', lt, d, { z: [1.1, 1.2], p: [[.5, .7]] }); tone(ctx, 'soguk', 1);
  sc(ctx); ctx.save(); ctx.translate(960, 720); ctx.rotate(r); ctx.fillStyle = '#0a0a12'; ctx.beginPath(); ctx.moveTo(-380, 0); ctx.lineTo(380, 0); ctx.lineTo(300, 90); ctx.lineTo(-300, 90); ctx.closePath(); ctx.fill(); ctx.fillRect(-8, -380, 16, 380); ctx.beginPath(); ctx.moveTo(10, -360); ctx.lineTo(260, -80); ctx.lineTo(10, -60); ctx.closePath(); ctx.fill(); ctx.restore();
  etiket(ctx, 'İLK KEZ DENİZ', 960, 220, 50, (lt - 1.5) / .3);
}, { tr: 'whip' });
S(tVardi, tKapi, (ctx, lt, t, d) => { bg(ctx, 'carsi', lt, d, { z: [1.05, 1.2], sat: .4 }); tone(ctx, 'soguk', .7); etiket(ctx, 'İSTANBUL', 960, 230, 56, (lt - .2) / .3); damga(ctx, 'SATILDI', 1400, 760, 90, (t - wt('satıldın', tVardi)) / .3); });
S(tKapi, P[5], (ctx, lt, t, d) => { bg(ctx, 'babussaade', lt, d, { z: [1.0, 1.25], p: [[.5, .55]] }); tone(ctx, 'altin', .6); gul(ctx, 1450, 1010, 260, { face: { eyes: 'wide', mouth: 'o', look: [-.4, -.6] } }); }, { tr: 'whip' });
// ====================== 5 · HEDİYE EDİLEN İNSANLAR (69.6 – 82.8) ======================
S(P[5], P[5] + 6.5, (ctx, lt, t, d) => { bg(ctx, 'esir_pazari', lt, d, { z: [1.05, 1.2], sat: .3 }); tone(ctx, 'soguk', .6); etiket(ctx, 'ESİR PAZARI', 420, 220, 46, (lt - .3) / .3); });
S(P[5] + 6.5, P[6], (ctx, lt, t, d) => { bg(ctx, 'vanmour', lt, d, { z: [1.0, 1.12], p: [[.5, .3], [.5, .45]] }); tone(ctx, 'harem', .5); damga(ctx, 'HEDİYE EDİLEN İNSANLAR', 960, 880, 64, (t - wt('insanların', P[5])) / .3, '#e0262f', -.04); });
// ====================== 6 · İSİM (82.8 – 93.5) ======================
const tFars = wt('sana', P[6]);
S(P[6], P[7], (ctx, lt, t, d) => {
  bg(ctx, 'harem_kapi', lt, d, { z: [1.05, 1.2], bri: .55, blur: 3 }); tone(ctx, 'harem', 1);
  gul(ctx, 360, 1060, 300, { face: { eyes: 'normal', mouth: 'flat', look: [.6, -.2] } });
  sc(ctx); text(ctx, 'MARİAM', 1120, 400, 150, '#fbf8f1', INK, 14, 'Poppins', 700);
  const k = clamp((t - wt('mariam', P[6] + 1)) / .5); if (k > 0) { ctx.beginPath(); ctx.moveTo(780, 410); ctx.lineTo(780 + 690 * k, 395); ctx.lineWidth = 20; ctx.strokeStyle = '#e0262f'; ctx.lineCap = 'round'; ctx.stroke(); }
  const g = clamp((t - wt('gülnihal', P[6])) / .4); if (g > 0) { ctx.globalAlpha = g; text(ctx, 'GÜLNİHAL', 1120, 640, 140, '#ffd23a', INK, 12, 'Poppins', 700); ctx.globalAlpha = 1; etiket(ctx, '"GÜL FİDANI"', 1120, 790, 44, (t - wt('fidanı', P[6])) / .3); }
});
S(P[7], P[8], (ctx, lt, t, d) => { // gün çizelgesi
  sc(ctx); ctx.fillStyle = '#100c14'; ctx.fillRect(0, 0, W, H);
  const L = ['ŞAFAK', 'SABAH', 'ÖĞLE', 'İKİNDİ', 'AKŞAM', 'GECE'];
  L.forEach((l, i) => { const a = clamp((lt - .2 - i * .35) / .3); const x = 260 + i * 280; circle(ctx, x, 540, 26 * backOut(a)); ctx.fillStyle = '#ffd23a'; ctx.fill(); if (i < 5) line(ctx, x + 30, 540, x + 250, 540, 6, `rgba(255,210,58,${a})`); ctx.globalAlpha = a; text(ctx, l, x, 620, 40, '#fff', INK, 0, 'Poppins', 700); ctx.globalAlpha = 1; });
  baslik(ctx, ['HAREMDE BİR GÜN'], lt / .4, 330, 90);
}, { dip: 1 });
// ====================== 7 · ŞAFAK (98 – 153.4) ======================
const tKandil = wt('gece', P[8] + 3);
S(P[8], tKandil, (ctx, lt, t, d) => {
  bg(ctx, 'melling', lt, d, { z: [1.12, 1.2], bri: .5, blur: 2 }); tone(ctx, 'harem', 1.1); kandilIsigi(ctx, 1550, 330, 480, 1, t);
  for (let i = 0; i < 3; i++) uyuyan(ctx, 380 + i * 420, 940, 240, [RENK.gul, RENK.dil, '#c97a5a'][i], { uyanik: i === 0 && lt > 1.2 });
  kalfa(ctx, 1640, 800, 360, { flip: -1, arms: { L: [.3, -.2], R: [2.0, .3] }, face: { eyes: 'normal', mouth: lt % .6 < .3 ? 'o' : 'flat', browAng: .35 } });
  etiket(ctx, 'ACEMİ KOĞUŞU', 330, 200, 44, (lt - .5) / .3);
}, { dip: 1 });
S(tKandil, P[9], (ctx, lt, t, d) => {
  bg(ctx, 'melling2', lt, d, { z: [1.1, 1.2], bri: .4, blur: 3 }); tone(ctx, 'gece', 1); kandilIsigi(ctx, 960, 260, 520, 1.2, t);
  sc(ctx); line(ctx, 960, 0, 960, 200, 4, '#3a2a1a'); ctx.save(); ctx.translate(960, 230); ellipse(ctx, 0, 0, 40, 26); fillStroke(ctx, '#d9a83a', 4); circle(ctx, 0, -20, 12 + Math.sin(t * 15) * 2); ctx.fillStyle = '#ffd27a'; ctx.fill(); ctx.restore();
  kalfa(ctx, 1500, 980, 340, { arms: { L: [.6, -1.6], R: [.6, -1.6] }, face: { eyes: 'normal', mouth: 'flat', look: [-.6, .2] } });
  for (let i = 0; i < 3; i++) uyuyan(ctx, 360 + i * 380, 1010, 210, [RENK.gul, RENK.dil, '#5a8ac9'][i]);
});
S(P[9], P[10], (ctx, lt, t, d) => {
  bg(ctx, 'avlu', lt, d, { z: [1.05, 1.15], bri: .7 }); tone(ctx, 'sabah', 1); tone(ctx, 'soguk', .4);
  for (let i = 0; i < 5; i++) kadin(ctx, 520 + i * 220, 900, 150, { renk: [RENK.gul, RENK.dil, '#c97a5a', '#5a8ac9', '#c9a12a'][i], lean: .25 + Math.sin(lt * .8) * .05, arms: { L: [.8, -.5], R: [.8, -.5] }, alpha: .9, face: { eyes: 'normal', blink: 1, mouth: 'flat' } });
  if (lt > 4.5) { sc(ctx); for (let i = 0; i < 3; i++) dosek(ctx, 300 + i * 500, 1000 - 90, 300, 70 - clamp(lt - 4.5) * 40); }
});
S(P[10], P[11], (ctx, lt, t, d) => { bg(ctx, 'hamam', lt, d, { z: [1.05, 1.2], p: [[.4, .5], [.6, .45]] }); tone(ctx, 'altin', .4); buhar(ctx, t, 1); etiket(ctx, 'HAREM HAMAMI', 380, 220, 46, (lt - .4) / .3); gul(ctx, 1500, 1060, 260, { face: { eyes: 'wide', mouth: 'smile', look: [-.5, -.3] } }); });
const STEPS1 = ['ACEMİ', 'CARİYE', 'KALFA', 'USTA', 'HAZNEDAR USTA'];
S(P[11], P[13], (ctx, lt, t, d) => {
  bg(ctx, 'tasligi', lt, d, { z: [1.1, 1.15], bri: .3, blur: 6 }); tone(ctx, 'harem', 1);
  baslik(ctx, ['HİZMET MERDİVENİ'], lt / .4, 170, 66);
  const t0 = wt('acemi', P[11]); const n = STEPS1.reduce((a, s, i) => t >= wt(s.split(' ')[0].toLowerCase(), t0 - .2) - .1 ? i + 1.0 : a, 0) + (t >= t0 ? 0 : 0);
  merdiven(ctx, STEPS1, t >= t0 ? n + clamp((t - t0) % 1) * 0 : 0, t >= P[12] ? 0 : -1, 1, { x0: 330, y0: 930, dx: 320, dy: 130, gulAt: t >= P[12] ? 0 : -1 });
  if (t >= P[12]) etiket(ctx, 'SEN BURADASIN', 330, 720, 40, (t - P[12]) / .3, { col: '#1b1820', bg: '#ffd23a' });
});
// ====================== 8 · SABAH (153.4 – 246) ======================
const tHakim = wt('ve', P[13] + 8);
S(P[13], tHakim, (ctx, lt, t, d) => {
  bg(ctx, 'tasligi', lt, d, { z: [1.04, 1.14], p: [[.4, .55], [.6, .5]] }); tone(ctx, 'sabah', 1);
  const yur = (i, x0, sp) => { const x = (x0 + lt * sp) % 2200 - 140; return x; };
  [[RENK.dil, 0, 120], ['#c97a5a', 500, 90], [RENK.gul, 1000, 110], ['#5a8ac9', 1500, 100]].forEach(([r, x0, sp], i) => { const x = yur(i, x0, sp); kadin(ctx, x, 980, 230, { renk: r, legs: { L: [Math.sin(t * 7 + i) * .45, -.3], R: [-Math.sin(t * 7 + i) * .45, -.3] }, arms: { L: [.3, -.2], R: [i % 2 ? 1.3 : .3, -.8] } }); if (i % 2) { sc(ctx); rrect(ctx, x + 50, 840, 60, 70, 8); fillStroke(ctx, '#8a6a48', 4); } });
  etiket(ctx, 'SU · ÇAMAŞIR · MUTFAK', 960, 200, 46, (lt - .4) / .3);
});
S(tHakim, P[14], (ctx, lt, t, d) => { bg(ctx, 'koridor2', lt, d, { z: [1.05, 1.2], bri: .6 }); tone(ctx, 'harem', 1); damga(ctx, 'PADİŞAH DEĞİL', 960, 520, 96, (t - wt('padişah', tHakim)) / .3); });
S(P[14], P[15], (ctx, lt, t, d) => {
  bg(ctx, 'valide', lt, d, { z: [1.04, 1.16], p: [[.5, .5], [.55, .45]] }); tone(ctx, 'altin', 1.2);
  sc(ctx); ctx.save(); ctx.globalCompositeOperation = 'lighter'; for (let i = 0; i < 5; i++) { ctx.beginPath(); ctx.moveTo(1380 + i * 60, 0); ctx.lineTo(1000 + i * 120, H); ctx.lineTo(1080 + i * 120, H); ctx.closePath(); ctx.fillStyle = 'rgba(255,220,140,.08)'; ctx.fill(); } ctx.restore();
  valide(ctx, 1300, 860, 260, { face: { eyes: 'smug', mouth: 'smirk' } });
  etiket(ctx, 'VALİDE SAFİYE SULTAN', 1300, 230, 46, (t - wt('safiye', P[14])) / .3);
  damga(ctx, 'BİR ZAMANLAR CARİYEYDİ', 640, 760, 62, (t - wt('cariyeydi', P[14])) / .3, '#ffd23a', -.06);
});
S(P[15], P[16], (ctx, lt, t, d) => {
  bg(ctx, 'altin_yol', lt, d, { z: [1.0, 1.25], p: [[.5, .6]] }); tone(ctx, 'harem', .8);
  padisahSil(ctx, 960, 690, 120, clamp((lt - .6) / .6) * (.6 + .4 * Math.sin(t * 2) ** 2));
  gul(ctx, 360, 1080, 300, { face: { eyes: 'wide', mouth: 'o', look: [.6, -.3] } });
  etiket(ctx, 'ÇOĞU PADİŞAHI HİÇ GÖRMEDİ', 960, 190, 50, (t - wt('haremdeki', P[15])) / .3);
});
S(P[16], P[17], (ctx, lt, t, d) => { bg(ctx, 'darussaade', lt, d, { z: [1.0, 1.1], p: [[.5, .35], [.5, .45]] }); tone(ctx, 'harem', .5); etiket(ctx, 'DARÜSSAADE AĞASI', 1450, 200, 46, (t - wt('darüssaade', P[16])) / .3); });
S(P[17], P[18], (ctx, lt, t, d) => {
  bg(ctx, 'kubbe', lt, d, { z: [1.05, 1.2] }); tone(ctx, 'altin', 1);
  baslik(ctx, ['HAREMİN KALBİ'], (lt - .2) / .4, 260, 84);
  valide(ctx, 960, 900, 230, { face: { eyes: 'smug', mouth: 'smirk' } });
  [[RENK.gul, 520], [RENK.dil, 1400], ['#c97a5a', 700], ['#5a8ac9', 1220]].forEach(([r, x], i) => kadin(ctx, x, 980, 170, { renk: r, face: { eyes: 'normal', mouth: 'flat', look: [x < 960 ? .5 : -.5, -.2] } }));
});
S(P[18], P[19], (ctx, lt, t, d) => {
  sc(ctx); ctx.fillStyle = '#120e16'; ctx.fillRect(0, 0, W, H);
  ctx.save(); ctx.beginPath(); ctx.rect(0, 0, W / 2, H); ctx.clip(); bg(ctx, 'valide', lt, d, { z: [1.2, 1.3], bri: .9 }); tone(ctx, 'altin', 1); valide(ctx, 480, 900, 230, { face: { eyes: 'smug', mouth: 'smile' } }); ctx.restore();
  ctx.save(); sc(ctx); ctx.beginPath(); ctx.rect(W / 2, 0, W / 2, H); ctx.clip(); const im = IMG.elizabeth; if (im.naturalWidth) { const k = W / 2 / im.naturalWidth * 1.05; ctx.drawImage(im, W / 2 + (W / 2 - im.naturalWidth * k) / 2, -lt * 8, im.naturalWidth * k, im.naturalHeight * k); } ctx.restore();
  sc(ctx); ctx.fillStyle = '#fff'; ctx.fillRect(W / 2 - 4, 0, 8, H);
  for (let i = 0; i < 3; i++) { const k = ((lt * .4 + i / 3) % 1); mektup(ctx, lerp(560, 1360, k), 520 - Math.sin(k * Math.PI) * 220, 46, Math.sin(k * Math.PI), (k - .5) * .6); }
  etiket(ctx, 'SAFİYE SULTAN', 480, 200, 42, (lt - .3) / .3); etiket(ctx, 'KRALİÇE I. ELIZABETH', 1440, 200, 42, (lt - .6) / .3);
  if (t > wt('araba', P[18])) etiket(ctx, 'HEDİYE: AT ARABASI', 1440, 820, 40, (t - wt('araba', P[18])) / .3, { col: '#1b1820', bg: '#ffd23a' });
});
// ====================== 9 · ÖĞLE (246 – 314.6) ======================
const tNakis = wt('sonra', P[19] + 4);
S(P[19], tNakis, (ctx, lt, t, d) => { bg(ctx, 'levni1', lt, d, { z: [1.1, 1.2], p: [[.5, .3], [.5, .5]], bri: .55, blur: 2 }); tone(ctx, 'altin', .6); harfler(ctx, t, 1); gul(ctx, 1450, 1010, 300, { arms: { L: [.8, -1.4], R: [.8, -1.4] }, face: { eyes: 'normal', mouth: 'flat', look: [0, .5] } }); etiket(ctx, "OKUMA YAZMA · KUR'AN", 960, 200, 46, (lt - .4) / .3); });
S(tNakis, P[20], (ctx, lt, t, d) => { bg(ctx, lt < 3 ? 'nakis1' : 'nakis2', lt % 3, 3, { z: [1.05, 1.2] }); tone(ctx, 'altin', .5); etiket(ctx, 'NAKIŞ · DİKİŞ · İPEK', 960, 200, 46, (lt - .3) / .3); });
S(P[20], P[21], (ctx, lt, t, d) => {
  sc(ctx); ctx.save(); ctx.beginPath(); ctx.rect(0, 0, W / 2, H); ctx.clip(); bg(ctx, 'muzisyen', lt, d, { z: [1.2, 1.3], p: [[.5, .5]] }); tone(ctx, 'harem', .5); ctx.restore();
  ctx.save(); ctx.beginPath(); ctx.rect(W / 2, 0, W / 2, H); ctx.clip(); sc(ctx); bg(ctx, 'kanun', lt, d, { z: [1.25, 1.3], bri: .5, blur: 3 }); tone(ctx, 'harem', 1); ctx.restore();
  sc(ctx); ctx.fillStyle = '#fff'; ctx.fillRect(W / 2 - 4, 0, 8, H);
  dil(ctx, 1240, 1000, 300, { arms: { L: [1.1, -1.3], R: [.9, -1.6] }, face: { eyes: 'happy', mouth: 'smile' } });
  sc(ctx); ctx.save(); ctx.translate(1240, 860); ctx.rotate(-.5); ellipse(ctx, 0, 0, 70, 52); fillStroke(ctx, '#a0602a', 5); ctx.fillRect(40, -10, 150, 20); ctx.restore();
  gul(ctx, 1640, 1000, 280, { flip: -1, face: { eyes: 'normal', mouth: 'smile', look: [-.6, 0] } });
  etiket(ctx, 'DİLRUBA', 1240, 340, 48, (t - wt('dilruba', P[20])) / .3, { col: '#fff', bg: RENK.dil });
});
S(P[21], P[22], (ctx, lt, t, d) => {
  bg(ctx, 'hunkar', lt, d, { z: [1.1, 1.15], bri: .45, blur: 4 }); tone(ctx, 'altin', .8);
  baslik(ctx, ['SARAY ADABI'], (lt - .2) / .4, 230, 84);
  const L = [['YÜRÜYÜŞ', 'yürüyeceksin'], ['SELAM', 'selam'], ['SUSMAK', 'susacaksın']];
  L.forEach(([l, w], i) => { const a = (t - wt(w, P[21])) / .3; const x = 460 + i * 500; if (a <= 0) return; gul(ctx, x, 900, 260 * backOut(clamp(a)), i === 1 ? { arms: { L: [.3, -.2], R: [2.6, -2.6] } } : i === 2 ? { face: { eyes: 'normal', mouth: 'flat' }, arms: { L: [.3, -.2], R: { ik: [.08, -.72] } } } : { legs: { L: [Math.sin(t * 6) * .3, -.2], R: [-Math.sin(t * 6) * .3, -.2] } }); etiket(ctx, l, x, 960, 40, a); });
});
S(P[22], P[23], (ctx, lt, t, d) => {
  bg(ctx, 'mutfak', lt, d, { z: [1.05, 1.15], bri: .8 }); tone(ctx, 'altin', .6);
  sc(ctx); ellipse(ctx, 960, 900, 360, 90); fillStroke(ctx, '#c9a04a', 6); for (let i = 0; i < 5; i++) { ellipse(ctx, 760 + i * 100, 885, 36, 14); fillStroke(ctx, '#f6f1e6', 3); }
  [[RENK.gul, 560], [RENK.dil, 1360], ['#c97a5a', 760], ['#5a8ac9', 1160]].forEach(([r, x]) => kadin(ctx, x, 1010, 220, { renk: r, face: { eyes: 'happy', mouth: 'smile', look: [x < 960 ? .5 : -.5, .3] } }));
  etiket(ctx, 'YER SOFRASI', 960, 200, 46, (lt - .3) / .3);
});
S(P[23], P[24], (ctx, lt, t, d) => {
  bg(ctx, 'valide_tasligi', lt, d, { z: [1.1, 1.2], bri: .5, blur: 4 }); tone(ctx, 'altin', 1);
  gul(ctx, 760, 1060, 360, { arms: { L: [.3, -.2], R: { ik: [.4, -.5] } }, face: { eyes: 'wide', mouth: 'smile', look: [.5, .2] } });
  for (let i = 0; i < 6; i++) { const k = clamp((lt - .8 - i * .25) / .5); if (k > 0) akce(ctx, 1000 + (i % 3) * 18, lerp(300, 820 - i * 10, easeIn(k)), 34); }
  etiket(ctx, 'ULUFE · GÜNLÜK ÖDENEK', 1300, 220, 46, (t - wt('ulufe', P[23])) / .3);
});
S(P[24], P[25], (ctx, lt, t, d) => { bg(ctx, 'levni2', lt, d, { z: [1.05, 1.2], p: [[.5, .35], [.5, .55]] }); tone(ctx, 'altin', .4); etiket(ctx, 'BAYRAMLIK KUMAŞ', 960, 200, 46, (lt - .3) / .3); etiket(ctx, 'KIDEM = KUMAŞ', 960, 300, 42, (t - wt('kıdemin', P[24])) / .3, { col: '#1b1820', bg: '#ffd23a' }); });
S(P[25], P[26], (ctx, lt, t, d) => { bg(ctx, 'avlu2', lt, d, { z: [1.04, 1.14] }); tone(ctx, 'sabah', .7); etiket(ctx, 'HAREMİN KENDİ HASTANESİ', 960, 200, 46, (lt - .3) / .3); etiket(ctx, 'TOPKAPI HAREMİ · BUGÜN', 330, 960, 30, (lt - .6) / .3); });
// ====================== 10 · İKİNDİ: FİNCAN (314.6 – 354.3) ======================
const tDus = wt('fincan', P[27]), tBak = wt('herkes', P[27]), tGor = wt('ama', P[27]);
S(P[26], tDus, (ctx, lt, t, d) => {
  bg(ctx, 'kubbe', lt, d, { z: [1.1, 1.15], bri: .55, blur: 3 }); tone(ctx, 'harem', .8);
  haznedar(ctx, 1500, 900, 300, { flip: -1, face: { eyes: 'smug', mouth: 'flat' } }); etiket(ctx, 'HAZNEDAR USTA', 1500, 260, 40, (t - wt('haznedar', P[26])) / .3, { col: '#fff', bg: RENK.haz });
  const x = 500 + lt * 60; dil(ctx, x, 980, 280, { arms: { L: [1.3, -1.1], R: [1.3, -1.1] }, legs: { L: [Math.sin(t * 6) * .3, -.2], R: [-Math.sin(t * 6) * .3, -.2] } }); sc(ctx); rrect(ctx, x - 110, 760, 220, 18, 8); fillStroke(ctx, '#c9a04a', 4); for (let i = 0; i < 3; i++) fincan(ctx, x - 60 + i * 60, 735, 34);
  kadin(ctx, x - 300, 980, 260, { renk: '#b33a3a', face: { eyes: 'smug', mouth: 'smirk', look: [.6, 0] } });
}, { tr: 'whip' });
S(tDus, tGor, (ctx, lt, t, d) => { // yavaş çekim: düşer, kırılır, herkes bakar
  bg(ctx, 'kubbe', lt, d, { z: [1.2, 1.24], bri: .5, blur: 4 }); tone(ctx, 'harem', 1);
  const fall = clamp(lt / 1.6), kir = clamp((lt - 1.6) / .5);
  fincan(ctx, 900, lerp(560, 930, easeIn(fall)), 60, fall * 3, kir);
  if (lt > 1.6 && lt < 1.75) flas(ctx, .6);
  dil(ctx, 640, 1000, 300, { face: { eyes: 'wide', mouth: 'o', browAng: -.3 } });
  if (t >= tBak) [[RENK.gul, 1200], ['#5a8ac9', 1460], [RENK.haz, 1720]].forEach(([r, x]) => kadin(ctx, x, 1000, 260, { renk: r, flip: -1, face: { eyes: 'normal', mouth: 'flat', look: [-.8, 0], browAng: .3 } }));
});
S(tGor, P[28], (ctx, lt, t, d) => { // geri sarma: kızı itiyor
  bg(ctx, 'kubbe', lt, d, { z: [1.2, 1.24], bri: .45, blur: 5, sat: .3 }); tone(ctx, 'soguk', .8);
  sc(ctx); ctx.save(); ctx.globalAlpha = .15; ctx.fillStyle = '#fff'; for (let y = 0; y < H; y += 6) ctx.fillRect(0, y, W, 2); ctx.restore();
  dil(ctx, 900, 1000, 300, { arms: { L: [1.3, -1.1], R: [1.3, -1.1] } });
  kadin(ctx, 600, 1000, 290, { renk: '#b33a3a', arms: { L: [.3, -.2], R: { ik: [.5, -.45] } }, face: { eyes: 'smug', mouth: 'smirk' } });
  sc(ctx); circle(ctx, 600, 760, 170 + Math.sin(t * 8) * 6); ctx.lineWidth = 10; ctx.strokeStyle = '#e0262f'; ctx.stroke();
  etiket(ctx, '◀◀ GERİ SAR', 300, 160, 40, 1, { col: '#fff', bg: '#16121a' });
});
S(P[28], P[29], (ctx, lt, t, d) => { // SUS mu KONUŞ mu
  sc(ctx); ctx.fillStyle = '#1a1018'; ctx.fillRect(0, 0, W / 2, H); ctx.fillStyle = '#10141c'; ctx.fillRect(W / 2, 0, W / 2, H);
  gul(ctx, 960, 880, 300, { face: { eyes: 'normal', mouth: 'flat', look: [Math.sin(t * 2) * .8, 0], browAng: -.2 } });
  text(ctx, 'SUS', 480, 420, 170, '#fff', INK, 16, 'Poppins', 700); text(ctx, 'KONUŞ', 1440, 420, 170, '#ffd23a', INK, 16, 'Poppins', 700);
  text(ctx, 'Dilruba cezalandırılır', 480, 600, 40, '#bbb', INK, 0, 'Poppins', 700); text(ctx, 'Düşman kazanırsın', 1440, 600, 40, '#bbb', INK, 0, 'Poppins', 700);
  const s = Math.floor(t * 2) % 2; sc(ctx); circle(ctx, 960, 200, 70); fillStroke(ctx, '#f4ead2', 6); line(ctx, 960, 200, 960 + Math.sin(t * 6.28) * 50, 200 - Math.cos(t * 6.28) * 50, 8);
}, { dip: 1 });
const tSoz = wt('bu', P[29] + 3);
S(P[29], P[30], (ctx, lt, t, d) => {
  bg(ctx, 'kubbe', lt, d, { z: [1.15, 1.25], bri: .5, blur: 4 }); tone(ctx, 'harem', 1);
  if (t < tSoz - .3) { gul(ctx, 600, 1040, 330, { arms: { L: [.3, -.2], R: [1.6, -.4] }, face: { eyes: 'normal', mouth: lt % .5 < .25 ? 'o' : 'flat' } }); haznedar(ctx, 1350, 1040, 330, { flip: -1, face: { eyes: 'smug', mouth: 'flat' } }); }
  else { const z = clamp((t - tSoz + .3) / .4); drawStick(ctx, { x: 960, y: 1700 + 150 * (1 - z), s: 1500, cols: [RENK.haz, RENK.haz], hat: 'none', belt: false, shadow: false, face: { eyes: 'smug', mouth: 'smile' } }); etiket(ctx, '"BU KIZ DOĞRUYU SÖYLÜYOR"', 960, 200, 52, (t - tSoz) / .3); }
  const tDus2 = wt('düşmanını', P[29]) - 2; if (t > tDus2 + 2) { kadin(ctx, 1700, 1060, 240, { renk: '#b33a3a', flip: -1, face: { eyes: 'smug', mouth: 'frown', browAng: .6, look: [-.8, 0] } }); damga(ctx, 'İLK DÜŞMAN', 1500, 520, 70, (t - tDus2 - 2) / .3); }
});
// ====================== 11 · AKŞAM: İKİNCİ MERDİVEN (354.3 – 397.7) ======================
const STEPS2 = ['GÖZDE', 'İKBAL', 'HASEKİ', 'VALİDE SULTAN'];
S(P[30], P[31], (ctx, lt, t, d) => {
  bg(ctx, 'hunkar', lt, d, { z: [1.08, 1.16], bri: .4, blur: 5 }); tone(ctx, 'altin', 1);
  baslik(ctx, ['PADİŞAH MERDİVENİ'], (t - wt('ikinci', P[30])) / .4, 160, 64);
  const t0 = wt('gözde', P[30]); let n = 0; STEPS2.forEach((s, i) => { if (t >= wt(s.split(' ')[0].toLowerCase(), t0 - .2) - .1) n = i + 1; });
  merdiven(ctx, STEPS2, n, n - 1, 1, { x0: 420, y0: 900, dx: 360, dy: 150, renk: '#ffd23a' });
  padisahSil(ctx, 1700, 1060, 220, clamp(lt / 1.5) * .9);
});
S(P[31], P[32], (ctx, lt, t, d) => { bg(ctx, 'hurrem', lt, d, { z: [1.0, 1.12], p: [[.5, .3], [.5, .4]] }); tone(ctx, 'altin', .4); etiket(ctx, 'HÜRREM SULTAN', 960, 200, 48, (t - wt('hürrem', P[31])) / .3); damga(ctx, 'İSTİSNA', 1450, 700, 110, (t - wt('istisnaydı', P[31])) / .3, '#ffd23a', -.12); });
S(P[32], P[33], (ctx, lt, t, d) => {
  bg(ctx, 'hunkar', lt, d, { z: [1.15, 1.2], bri: .45, blur: 4 }); tone(ctx, 'harem', .8);
  const k = clamp(lt / 2.2); sc(ctx); ctx.save(); ctx.translate(lerp(1500, 960, k), lerp(300, 620, easeIn(k))); ctx.rotate(Math.sin(lt * 4) * .4); rrect(ctx, -90, -70, 180, 140, 10); fillStroke(ctx, '#fbf2e0', 5); ctx.fillStyle = '#d9a83a'; ctx.fillRect(-90, 50, 180, 12); ctx.restore();
  damga(ctx, 'EFSANE', 960, 620, 150, (t - wt('efsane', P[32])) / .3, '#e0262f', -.14);
  etiket(ctx, 'MENDİL HİKÂYESİ', 960, 190, 48, (lt - .3) / .3);
});
// ====================== 12 · GECE (397.7 – 435.8) ======================
const tYastik = wt('yastığının', P[33]), tAnneSes = wt('annenin', P[33]);
S(P[33], P[34], (ctx, lt, t, d) => {
  bg(ctx, 'melling', lt, d, { z: [1.2, 1.3], bri: .5, blur: 3 }); tone(ctx, 'gece', 1.1); kandilIsigi(ctx, 1600, 260, 380, lerp(1, .35, clamp(lt / 3)), t);
  uyuyan(ctx, 1100, 760, 380, RENK.gul, { uyanik: true });
  if (t > tYastik) basortu(ctx, 700, 690, 90, clamp((t - tYastik) / .5), -.2);
  if (t > tAnneSes) { sc(ctx); ctx.save(); ctx.globalAlpha = .4 * clamp((t - tAnneSes) / .8); bg(ctx, 'koy3', t - tAnneSes, 6, { z: [1.1, 1.2] }); ctx.restore(); tone(ctx, 'gece', .6); uyuyan(ctx, 1100, 760, 380, RENK.gul, { uyanik: true }); basortu(ctx, 700, 690, 90, 1, -.2); }
}, { dip: 1 });
S(P[34], P[35], (ctx, lt, t, d) => {
  bg(ctx, 'melling2', lt, d, { z: [1.05, 1.15], bri: .5 }); tone(ctx, 'harem', 1.1); kandilIsigi(ctx, 960, 300, 500, 1, t);
  dil(ctx, 600, 1000, 240, { arms: { L: [1.1, -1.3], R: [.9, -1.6] }, face: { eyes: 'happy', mouth: 'smile' } });
  [['#c97a5a', 960], ['#5a8ac9', 1320]].forEach(([r, x]) => kadin(ctx, x, 1000, 230, { renk: r, face: { eyes: 'happy', mouth: 'smile' } }));
  const L = ['ÇERKESÇE', 'GÜRCÜCE', 'RUSÇA', 'LEHÇE', 'İTALYANCA']; L.forEach((l, i) => etiket(ctx, l, 300 + i * 330, 230 + (i % 2) * 90, 36, (t - wt(l.slice(0, 4).toLowerCase(), P[34])) / .3));
});
S(P[35], P[36], (ctx, lt, t, d) => { bg(ctx, 'harem_kapi', lt, d, { z: [1.1, 1.3], bri: .4 }); tone(ctx, 'gece', 1); baslik(ctx, ['BİR GÜN BURADAN', 'ÇIKABİLECEK MİYİM?'], lt / .4, 420, 92); });
NOCAP.push([P[35], P[36]]);
// ====================== 13 · YILLAR, KALFA, ÜÇ KAPI (435.8 – 502) ======================
S(P[36], P[37], (ctx, lt, t, d) => { bg(ctx, 'tasligi', lt, d, { z: [1.0, 1.3] }); tone(ctx, 'sabah', 1); sc(ctx); for (let i = 0; i < 9; i++) { const k = clamp((lt - i * .7) / .5); if (k <= 0 || k >= 1) continue; ctx.save(); ctx.globalAlpha = 1 - k; ctx.translate(960, 520 - k * 200); ctx.rotate(k * .6); rrect(ctx, -140, -170, 280, 340, 10); fillStroke(ctx, '#f4ead2', 5); text(ctx, String(1598 + i), 0, 0, 70, '#1b1820', INK, 0, 'Poppins', 700); ctx.restore(); } gul(ctx, 1500, 1060, 300, { face: { eyes: 'normal', mouth: 'smile' } }); }, { dip: 1 });
S(P[37], P[38], (ctx, lt, t, d) => {
  bg(ctx, 'melling', lt, d, { z: [1.12, 1.2], bri: .55, blur: 2 }); tone(ctx, 'sabah', .8); tone(ctx, 'harem', .5); kandilIsigi(ctx, 1550, 330, 420, .7, t);
  for (let i = 0; i < 3; i++) uyuyan(ctx, 380 + i * 400, 940, 230, ['#c9a12a', '#5ac9a8', '#c97a5a'][i], { uyanik: lt > 1.5 });
  gul(ctx, 1640, 800, 360, { flip: -1, anahtar: true, arms: { L: [.3, -.2], R: [2.0, .3] }, face: { eyes: 'normal', mouth: lt % .6 < .3 ? 'o' : 'smile' } });
  damga(ctx, 'GÜLNİHAL ARTIK KALFA', 960, 220, 62, (t - wt('kalfa', P[37])) / .3, '#ffd23a', -.04);
});
const DOOR = ['SARAYDA KAL', 'BAŞKA SARAY', 'ÇIRAĞ ÇIK'];
const tD = [wt('birincisi', P[39]), wt('ikincisi', P[39]), wt('üçüncüsü', P[39])];
S(P[38], P[40], (ctx, lt, t, d) => {
  sc(ctx); ctx.fillStyle = '#120e16'; ctx.fillRect(0, 0, W, H); tone(ctx, 'altin', .3);
  baslik(ctx, ['9 YIL SONRA', 'ÜÇ KAPI'], lt / .4, 180, 72);
  DOOR.forEach((l, i) => { const a = clamp((lt - .6 - i * .3) / .3); if (a <= 0) return; const hi = t >= tD[i] && (i === 2 || t < tD[i + 1]); sc(ctx); ctx.save(); ctx.globalAlpha = a; kapi(ctx, 480 + i * 480, 780, 230, 360, '#5a3a20', hi ? .35 : 0, l, hi); ctx.restore(); });
  gul(ctx, 1800, 1010, 200, { flip: -1, face: { eyes: 'normal', mouth: 'flat', look: [-.8, -.3] } });
}, { dip: 1 });
S(P[40], P[41], (ctx, lt, t, d) => {
  bg(ctx, 'valide_tasligi', lt, d, { z: [1.1, 1.15], bri: .45, blur: 4 }); tone(ctx, 'altin', 1);
  sc(ctx); const op = clamp((t - wt('çeyiz', P[40])) / .6); ctx.save(); ctx.translate(960, 780); rrect(ctx, -260, -120, 520, 240, 20); fillStroke(ctx, '#7a4a2a', 6); ctx.save(); ctx.translate(0, -120); ctx.rotate(-op * .5); rrect(ctx, -260, -60, 520, 60, 16); fillStroke(ctx, '#8a5a32', 6); ctx.restore(); ctx.fillStyle = '#e3b23c'; ctx.fillRect(-270, -20, 540, 18); if (op > .5) for (let i = 0; i < 5; i++) { circle(ctx, -160 + i * 80, -140 - Math.sin(i + t * 3) * 10, 18); ctx.fillStyle = ['#ffd23a', '#e0262f', '#86c97a', '#fff', '#5a8ac9'][i]; ctx.fill(); } ctx.restore();
  etiket(ctx, 'ÇIRAĞ ÇIKMAK', 960, 220, 56, (t - wt('çırağ', P[40])) / .3); etiket(ctx, 'AZAT + ÇEYİZ + EVLİLİK', 960, 360, 40, (t - wt('evlendirirdi', P[40])) / .3, { col: '#1b1820', bg: '#ffd23a' });
});
S(P[41], P[42], (ctx, lt, t, d) => { bg(ctx, 'istanbul_cami', lt, d, { z: [1.0, 1.12], p: [[.5, .4], [.5, .55]] }); tone(ctx, 'altin', .4); etiket(ctx, 'SARAY ↔ İSTANBUL AİLELERİ', 960, 200, 44, (t - wt('saray', P[41] + 5)) / .3); });
// ====================== 14 · AYRILIK, MEKTUPLAR (502 – 534.8) ======================
S(P[42], P[43], (ctx, lt, t, d) => {
  bg(ctx, 'valide_tasligi', lt, d, { z: [1.1, 1.2], bri: .35, blur: 3 }); tone(ctx, 'gece', 1); kandilIsigi(ctx, 960, 350, 520, .9, t);
  sc(ctx); ctx.save(); ctx.globalAlpha = clamp(lt / .6); kapi(ctx, 1640, 1000, 200, 340, '#5a3a20', .6); ctx.restore();
  gul(ctx, 780, 1040, 330, { arms: { L: [.3, -.2], R: { ik: [.42, -.5] } }, face: { eyes: 'normal', mouth: 'smile', look: [.6, 0] } });
  dil(ctx, 1160, 1040, 330, { flip: -1, arms: { L: [.3, -.2], R: { ik: [.42, -.5] } }, face: { eyes: 'normal', mouth: 'smile', look: [.6, 0] } });
  if (t > wt('mektup', P[42])) mektup(ctx, 970, 560, 50, clamp((t - wt('mektup', P[42])) / .4));
});
S(P[43], P[44], (ctx, lt, t, d) => {
  bg(ctx, 'uskudar2', lt, d, { z: [1.05, 1.15] }); tone(ctx, 'sabah', .8);
  for (let i = 0; i < 4; i++) { const k = clamp((lt - i * 2.4) / 1.2); if (k > 0) mektup(ctx, lerp(1900, 700 + i * 160, easeOut(k)), lerp(200, 560 + (i % 2) * 60, easeOut(k)), 56, 1, (i - 1.5) * .15); }
  gul(ctx, 400, 1060, 300, { face: { eyes: 'happy', mouth: 'smile', look: [.6, -.3] } });
  etiket(ctx, 'DİLRUBA: KALFA', 1500, 300, 40, (t - wt('kalfa', P[43])) / .3, { col: '#fff', bg: RENK.dil }); etiket(ctx, 'DİLRUBA: USTA', 1500, 400, 40, (t - wt('usta', P[43])) / .3, { col: '#fff', bg: RENK.dil });
});
S(P[44], P[45], (ctx, lt, t, d) => {
  sc(ctx); ctx.save(); ctx.beginPath(); ctx.rect(0, 0, W / 2, H); ctx.clip(); bg(ctx, 'uskudar', lt, d, { z: [1.25, 1.35], p: [[.45, .72]] }); tone(ctx, 'sabah', 1); gul(ctx, 480, 1060, 300, { face: { eyes: 'happy', mouth: 'smile' } }); ctx.restore();
  ctx.save(); ctx.beginPath(); ctx.rect(W / 2, 0, W / 2, H); ctx.clip(); bg(ctx, 'hunkar', lt, d, { z: [1.2, 1.3], bri: .55 }); tone(ctx, 'altin', 1); merdiven(ctx, ['KALFA', 'USTA', 'HAZNEDAR'], 3, 1, 1, { x0: 1160, y0: 900, dx: 260, dy: 140 }); dil(ctx, 1420, 720, 170, {}); ctx.restore();
  sc(ctx); ctx.fillStyle = '#fff'; ctx.fillRect(W / 2 - 4, 0, 8, H);
  etiket(ctx, 'HANGİSİ DAHA ŞANSLIYDI?', 960, 160, 50, (t - wt('hangisi', P[44])) / .3);
});
// ====================== 15 · ÜSKÜDAR, FİNAL (534.8 – 629) ======================
const tEv = wt('artık', P[45]), tAdi = wt('ve', tEv + 1);
S(P[45], tEv, (ctx, lt, t, d) => {
  bg(ctx, 'uskudar', lt, d, { z: [1.05, 1.15], p: [[.3, .6], [.6, .6]] }); tone(ctx, 'sabah', 1);
  sc(ctx); const x = lerp(1500, 600, lt / d), y = 830 + Math.sin(t * 2) * 6; ctx.save(); ctx.translate(x, y); ctx.beginPath(); ctx.moveTo(-170, 0); ctx.quadraticCurveTo(0, 50, 190, -20); ctx.lineTo(160, 30); ctx.quadraticCurveTo(0, 70, -150, 30); ctx.closePath(); fillStroke(ctx, '#7a4a2a', 5); ctx.restore();
  gul(ctx, x, y + 4, 150, { face: { eyes: 'happy', mouth: 'smile' } }); etiket(ctx, 'ÜSKÜDAR', 1500, 220, 52, (t - wt('üsküdar', P[45])) / .3);
}, { tr: 'whip' });
S(tEv, P[46], (ctx, lt, t, d) => {
  bg(ctx, 'uskudar2', lt, d, { z: [1.1, 1.2], bri: .5, blur: 3 }); tone(ctx, 'sabah', 1);
  gul(ctx, 500, 1060, 330, { face: { eyes: 'happy', mouth: 'grin' } });
  const L = [['KENDİ EVİ', 'evi'], ['KENDİ ODASI', 'odası'], ['KENDİ ADI', 'adı']];
  L.forEach(([l, w], i) => { const a = (t - wt(w, tEv - 1)) / .3; if (a <= 0) return; etiket(ctx, l + '  ' + (i < 2 || t > tAdi + 3 ? '✔' : '…'), 1250, 360 + i * 150, 54, a, { col: '#1b1820', bg: '#ffd23a' }); });
});
S(P[46], P[47], (ctx, lt, t, d) => {
  bg(ctx, 'istanbul_gunbatimi', lt, d, { z: [1.02, 1.12] }); tone(ctx, 'sabah', 1);
  sc(ctx); ctx.lineWidth = 60; ctx.strokeStyle = '#3a2416'; ctx.strokeRect(30, 30, W - 60, H - 60); ctx.fillStyle = '#3a2416'; ctx.fillRect(W / 2 - 15, 0, 30, H);
  gul(ctx, 700, 1060, 380, { arms: { L: [.3, -.2], R: { ik: [.4, -.45] } }, face: { eyes: 'happy', mouth: 'smile', look: [.6, .3] } });
  const tKiz = wt('yanına', P[46]); if (t > tKiz) kadin(ctx, 1080, 1060, 220 * backOut(clamp((t - tKiz) / .5)), { renk: '#ffb3c6', ortu: null, face: { eyes: 'happy', mouth: 'smile', look: [-.6, -.3] } });
  const tVer = wt('uzatıyor', P[46]); if (t > tVer - 2.5) basortu(ctx, lerp(830, 980, clamp((t - tVer + 2.5) / 2.5)), 720, 80, 1, -.15);
}, { dip: 1 });
S(P[47], P[48], (ctx, lt, t, d) => { bg(ctx, 'tasligi', lt, d, { z: [1.02, 1.18], p: [[.3, .5], [.7, .5]] }); tone(ctx, 'sabah', .5); etiket(ctx, 'TOPKAPI HAREMİ · BUGÜN', 960, 200, 46, (lt - .4) / .3); etiket(ctx, 'KURGUSAL BİR HİKÂYE · GERÇEK BİLGİLER', 960, 330, 34, (t - wt('kurgusal', P[47])) / .3, { col: '#fff', bg: '#16121a' }); });
S(P[48], P[49], (ctx, lt, t, d) => {
  bg(ctx, 'koy2', lt, d, { z: [1.05, 1.2], sat: .1 }); tone(ctx, 'soguk', .6);
  baslik(ctx, ['1909'], lt / .3 * (t < wt('hükümet', P[48]) ? 1 : 0), 300, 170);
  const tAile = wt('uzak', P[48]); if (t > tAile) for (let i = 0; i < 5; i++) { const x = (lt - (tAile - P[48])) * 70 + 200 + i * 130; drawStick(ctx, { x, y: 1000, s: 200, sil: '#1a1418', shadow: false, legs: { L: [Math.sin(t * 5 + i) * .4, -.2], R: [-Math.sin(t * 5 + i) * .4, -.2] } }); }
  if (t > wt('hükümet', P[48])) etiket(ctx, '"KIZLARINIZI GELİP ALABİLİRSİNİZ"', 960, 220, 46, (t - wt('hükümet', P[48])) / .3);
  const tTan = wt('kimi', P[48]); damga(ctx, 'KİMİ TANIDI · KİMİ TANIYAMADI', 1100, 720, 54, (t - tTan) / .3, '#ffd23a', -.04);
}, { dip: 1 });
S(P[49], P[50], (ctx, lt, t, d) => { bg(ctx, lt < d / 2 ? 'hunkar' : 'harem_kapi', lt % (d / 2), d / 2, { z: [1.04, 1.14] }); tone(ctx, lt < d / 2 ? 'altin' : 'sabah', 1); if (lt > d / 2) { sc(ctx); const a = clamp((lt - d / 2) / 2); ctx.save(); ctx.globalCompositeOperation = 'lighter'; const g = ctx.createRadialGradient(960, 560, 20, 960, 560, 700); g.addColorStop(0, `rgba(255,236,190,${.6 * a})`); g.addColorStop(1, 'rgba(255,236,190,0)'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); ctx.restore(); } });
const SON = P[50] + 22;
S(P[50], SON, (ctx, lt, t, d) => {
  sc(ctx); ctx.fillStyle = '#120e16'; ctx.fillRect(0, 0, W, H);
  ctx.save(); ctx.beginPath(); ctx.rect(0, 0, W * .55, H); ctx.clip(); bg(ctx, 'hunkar', lt, d, { z: [1.1, 1.2], bri: .6 }); tone(ctx, 'altin', 1); ctx.restore();
  gul(ctx, 520, 1060, 300, { face: { eyes: 'normal', mouth: 'flat', look: [Math.sin(t * 1.5) * .8, -.2] } });
  etiket(ctx, 'SARAYIN İHTİŞAMI MI?', 520, 300, 50, (t - wt('sarayın', P[50])) / .3); etiket(ctx, 'ÖZGÜRLÜK MÜ?', 520, 430, 58, (t - wt('özgürlüğünü', P[50])) / .3, { col: '#1b1820', bg: '#ffd23a' });
  etiket(ctx, 'YORUMLARA YAZ', 520, 640, 46, (t - wt('yorumlara', P[50])) / .3, { col: '#fff', bg: '#e0262f' });
  const fade = 1 - clamp((t - 629.6) / .6);
  if (fade > 0) { sc(ctx); ctx.save(); ctx.globalAlpha = fade * clamp(lt / .6);
    kapi(ctx, 1290, 760, 220, 340, '#5a3a20', .15 + .1 * Math.sin(t * 2), '', 0); kapi(ctx, 1640, 760, 220, 340, '#5a3a20', .55 + .15 * Math.sin(t * 2 + 1), '', 0); ctx.restore();
    etiket(ctx, 'SARAY', 1290, 830, 40, fade * clamp((t - wt('sarayın', P[50])) / .3)); etiket(ctx, 'ÖZGÜRLÜK', 1640, 830, 40, fade * clamp((t - wt('özgürlüğünü', P[50])) / .3), { col: '#1b1820', bg: '#ffd23a' });
    etiket(ctx, 'HANGİ KAPIYI SEÇERDİN?', 1465, 260, 46, fade * clamp((t - wt('hangi', P[50])) / .3)); }
}, { dip: 1 });
window.NOCAP = NOCAP;
