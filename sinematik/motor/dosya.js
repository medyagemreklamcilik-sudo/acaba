// Sinematik motor, "dosya" stili: koyu belgesel haritası + mantar pano, kırmızı ip, dosya etiketi,
// daktilo belge, polaroid + siyah isim bandı, nokta (halftone) portre, ışıyan şehir noktası, zaman çizgisi.
// Tek dünya, tek kesintisiz kamera (core.js ile aynı kamera ve beat mantığı).
// Sahne dosyası: FORMAT, WORLD, IMAGES, OBJECTS, CAMERA, BEATS, isteğe bağlı BOARDS, TIMELINE.
'use strict';
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const smooth = t => { t = clamp(t); return t * t * (3 - 2 * t); };
const easeOut = t => 1 - Math.pow(1 - clamp(t), 3);
const easeInOut = t => { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
const backOut = t => { t = clamp(t); const c = 1.6; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); };
const TAU = Math.PI * 2;
function rng(seed) { let s = seed >>> 0 || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 100000) / 100000; }; }
const MONO = '"IBM Plex Mono"', TYPE = '"Special Elite"', SERIF = '"Cormorant Garamond"', COND = 'Oswald';
const RED = '#c8322a', ORANGE = '#f0754e';

// ---------------- kamera ----------------
function camAt(t, K = CAMERA) {
  const n = K.length;
  if (t <= K[0].t) return { x: K[0].x, y: K[0].y, z: K[0].z, r: K[0].r || 0 };
  if (t >= K[n - 1].t) return { x: K[n - 1].x, y: K[n - 1].y, z: K[n - 1].z, r: K[n - 1].r || 0 };
  let i = 0; while (i < n - 2 && t > K[i + 1].t) i++;
  const a = K[i], b = K[i + 1], h = b.t - a.t, u = (t - a.t) / h;
  const tan = (j, key) => { if (j === 0 || j === n - 1) return 0; const p = K[j - 1], q = K[j + 1], v = key === 'z' ? Math.log(q.z) - Math.log(p.z) : (q[key] || 0) - (p[key] || 0); return v / (q.t - p.t); };
  const H = key => { const p0 = key === 'z' ? Math.log(a.z) : (a[key] || 0), p1 = key === 'z' ? Math.log(b.z) : (b[key] || 0), m0 = tan(i, key) * h, m1 = tan(i + 1, key) * h, u2 = u * u, u3 = u2 * u; return (2 * u3 - 3 * u2 + 1) * p0 + (u3 - 2 * u2 + u) * m0 + (-2 * u3 + 3 * u2) * p1 + (u3 - u2) * m1; };
  return { x: H('x'), y: H('y'), z: Math.exp(H('z')), r: H('r') };
}
function handheld(t, amp = 1) { const s = (f, p) => Math.sin(t * f + p); return { x: amp * (3.2 * s(.9, 1) + 1.6 * s(2.3, 4) + .7 * s(5.1, 2)), y: amp * (2.4 * s(1.1, 3) + 1.3 * s(2.9, .5) + .6 * s(4.7, 1)), r: amp * .0011 * (s(.7, 2) + .6 * s(1.9, 5)) }; }
function applyView(ctx, cam, hh) { ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.translate(FORMAT.w / 2 + hh.x, FORMAT.h / 2 + hh.y); ctx.rotate((cam.r || 0) + hh.r); ctx.scale(cam.z, cam.z); ctx.translate(-cam.x, -cam.y); }
function proj(lon, lat) { const W_ = WORLD; return [(lon - W_.lon0) * W_.k * Math.cos(W_.latc * Math.PI / 180), (W_.lat0 - lat) * W_.k]; }

// ---------------- beat: tek kahraman ----------------
function heroLevel(id, t) {
  const FADE = .45; let lv = 1;
  for (let i = 0; i < BEATS.length; i++) {
    const b = BEATS[i], n = BEATS[i + 1], on = !b.hero || b.hero.includes(id) || (b.keep || []).includes(id) ? 1 : 0;
    if (t >= b.t && (!n || t < n.t)) { const pb = BEATS[i - 1], prev = i > 0 ? (!pb.hero || pb.hero.includes(id) || (pb.keep || []).includes(id) ? 1 : 0) : on; lv = lerp(prev, on, smooth((t - b.t) / FADE)); }
  }
  return lv;
}
function mapDimAt(t) { const FADE = .6; for (let i = BEATS.length - 1; i >= 0; i--) if (t >= BEATS[i].t) { const p = i > 0 ? (BEATS[i - 1].mapDim || 0) : (BEATS[i].mapDim || 0); return lerp(p, BEATS[i].mapDim || 0, smooth((t - BEATS[i].t) / FADE)); } return 0; }
const endOf = o => o.type === 'route' ? o.hide : o.t1;
const fadeOf = (o, t) => endOf(o) != null ? 1 - smooth((t - endOf(o)) / (o.fadeDur || .5)) : 1;

// ---------------- dokular ----------------
const TEX = {}, IMG = {}, GRAY = {}, HALF = {};
function mk(w, h, f) { const c = document.createElement('canvas'); c.width = w; c.height = h; f(c.getContext('2d'), w, h); return c; }
function makeTextures() {
  TEX.cork = mk(512, 512, (g, w, h) => {
    g.fillStyle = '#8c5f37'; g.fillRect(0, 0, w, h); const R = rng(11);
    const cols = ['#5e3c1f', '#a87a4a', '#4a2f17', '#c39463', '#734b29', '#b5875a'];
    for (let k = 0; k < 16000; k++) { g.fillStyle = cols[(R() * cols.length) | 0]; g.globalAlpha = .35 + R() * .5; g.beginPath(); g.ellipse((R() * w), (R() * h), .5 + R() * 1.8, .4 + R() * 1.4, R() * 3, 0, TAU); g.fill(); }
    g.globalAlpha = 1; const id = g.getImageData(0, 0, w, h); for (let i = 0; i < id.data.length; i += 4) { const v = (R() - .5) * 26; id.data[i] += v; id.data[i + 1] += v * .9; id.data[i + 2] += v * .7; } g.putImageData(id, 0, 0);
  });
  TEX.paper = mk(512, 512, (g, w, h) => {
    g.fillStyle = '#ece7da'; g.fillRect(0, 0, w, h); const R = rng(5);
    const id = g.getImageData(0, 0, w, h); for (let i = 0; i < id.data.length; i += 4) { const v = (R() - .5) * 10; id.data[i] += v; id.data[i + 1] += v; id.data[i + 2] += v * .9; } g.putImageData(id, 0, 0);
    g.globalAlpha = .05; for (let k = 0; k < 500; k++) { g.strokeStyle = R() > .5 ? '#8a7a60' : '#ffffff'; g.lineWidth = .5 + R(); g.beginPath(); const x = R() * w, y = R() * h, a = R() * TAU, l = 4 + R() * 18; g.moveTo(x, y); g.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke(); }
  });
  TEX.manila = mk(256, 256, (g, w, h) => { g.fillStyle = '#d8c8a0'; g.fillRect(0, 0, w, h); const R = rng(9), id = g.getImageData(0, 0, w, h); for (let i = 0; i < id.data.length; i += 4) { const v = (R() - .5) * 14; id.data[i] += v; id.data[i + 1] += v; id.data[i + 2] += v * .8; } g.putImageData(id, 0, 0); });
  TEX.hatch = mk(24, 24, (g, w, h) => { g.strokeStyle = 'rgba(190,220,220,.075)'; g.lineWidth = 1.2; for (let k = -1; k <= 1; k++) { g.beginPath(); g.moveTo(k * w, h); g.lineTo(k * w + w, 0); g.stroke(); } });
  TEX.grain = []; for (let k = 0; k < 6; k++) TEX.grain.push(mk(512, 512, (g, w, h) => { const id = g.createImageData(w, h), R = rng(k + 21); for (let i = 0; i < id.data.length; i += 4) { const v = 128 + (R() - .5) * 150; id.data[i] = id.data[i + 1] = id.data[i + 2] = v; id.data[i + 3] = 255; } g.putImageData(id, 0, 0); }));
  const R = rng(77); TEX.dust = Array.from({ length: 46 }, () => ({ x: R(), y: R(), r: 1.5 + R() * 4.5, a: .15 + R() * .5, vx: (R() - .5) * .006, vy: -.004 - R() * .01, p: R() * TAU, warm: R() > .35 }));
}
function loadImages() { return Promise.all(Object.entries(IMAGES).map(([k, src]) => new Promise(r => { const i = new Image(); i.onload = i.onerror = () => r(); i.src = src; IMG[k] = i; }))); }
function prepImages() {
  for (const [k, im] of Object.entries(IMG)) { if (!im.naturalWidth) continue; GRAY[k] = mk(im.naturalWidth, im.naturalHeight, g => { g.filter = 'grayscale(1) contrast(1.18) brightness(1.03)'; g.drawImage(im, 0, 0); }); }
  for (const o of OBJECTS) if (o.type === 'halftone') { // nokta portre: parlaklık ızgarası bir kez örneklenir
    const im = IMG[o.img]; if (!im || !im.naturalWidth) continue; const c = cropOf(o, im), cols = o.cols || 64, rows = Math.round(cols * c[3] / c[2]);
    const s = mk(cols, rows, g => { g.filter = 'grayscale(1) contrast(1.35)'; g.drawImage(im, c[0], c[1], c[2], c[3], 0, 0, cols, rows); });
    const d = s.getContext('2d').getImageData(0, 0, cols, rows).data, R = rng(3), dots = [];
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) { const q = Math.hypot((i / cols - .5) / .5, (j / rows - .45) / .55); let l = d[(j * cols + i) * 4] / 255 * (1 - smooth((q - .55) / .45)); if (o.maxL && l > o.maxL) l *= Math.max(0, 1 - (l - o.maxL) / .1); if (l > .1) dots.push({ i, j, l, d: Math.hypot(i / cols - .5, j / rows - .42) + R() * .25 }); }
    HALF[o.id] = { cols, rows, dots };
  }
}
function cropOf(o, im) { const c = o.crop || [0, 0, 1, 1]; return [c[0] * im.naturalWidth, c[1] * im.naturalHeight, c[2] * im.naturalWidth, c[3] * im.naturalHeight]; }
let GEO = null, CURZ = 1;
function pat(ctx, tex, s) { const p = ctx.createPattern(tex, 'repeat'); p.setTransform(new DOMMatrix().scale(s)); return p; }
function polyPath(ctx, pts) { ctx.beginPath(); pts.forEach(([lo, la], i) => { const [x, y] = proj(lo, la); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }); }
function local(o, lx, ly) { const r = o.rot || 0, c = Math.cos(r), s = Math.sin(r); return [o.x + c * lx - s * ly, o.y + s * lx + c * ly]; }

// ---------------- dünya: koyu harita + panolar ----------------
function drawMap(ctx) {
  ctx.fillStyle = '#0d1416'; ctx.fillRect(-30000, -30000, 80000, 80000);
  ctx.save(); ctx.lineJoin = 'round';
  for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.fillStyle = '#1b2627'; ctx.fill(); ctx.fillStyle = pat(ctx, TEX.hatch, 1.4); ctx.fill(); }
  for (const p of GEO.lakes) { polyPath(ctx, p); ctx.closePath(); ctx.fillStyle = '#0f181a'; ctx.fill(); }
  ctx.strokeStyle = 'rgba(140,190,190,.06)'; ctx.lineWidth = 26 / CURZ; for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.stroke(); }
  ctx.strokeStyle = 'rgba(170,200,196,.42)'; ctx.lineWidth = 2.2 / CURZ; for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.stroke(); }
  ctx.lineCap = 'round'; ctx.strokeStyle = 'rgba(120,160,170,.16)'; ctx.lineWidth = 2 / CURZ; for (const r of GEO.rivers) { polyPath(ctx, r.p); ctx.stroke(); }
  ctx.restore();
}
function drawBoards(ctx) {
  for (const b of (typeof BOARDS !== 'undefined' ? BOARDS : [])) {
    ctx.save(); ctx.shadowColor = 'rgba(0,0,0,.75)'; ctx.shadowBlur = 220; ctx.shadowOffsetY = 60; ctx.fillStyle = '#7a5230'; ctx.fillRect(b.x, b.y, b.w, b.h); ctx.shadowColor = 'transparent';
    ctx.fillStyle = pat(ctx, TEX.cork, 3); ctx.fillRect(b.x, b.y, b.w, b.h);
    const g = ctx.createRadialGradient(b.x + b.w / 2, b.y + b.h * .45, Math.min(b.w, b.h) * .2, b.x + b.w / 2, b.y + b.h / 2, Math.max(b.w, b.h) * .7); g.addColorStop(0, 'rgba(255,220,170,.10)'); g.addColorStop(1, 'rgba(20,10,5,.55)'); ctx.fillStyle = g; ctx.fillRect(b.x, b.y, b.w, b.h);
    ctx.strokeStyle = '#2a1a0e'; ctx.lineWidth = 34; ctx.strokeRect(b.x, b.y, b.w, b.h); ctx.strokeStyle = 'rgba(255,230,190,.08)'; ctx.lineWidth = 4; ctx.strokeRect(b.x + 18, b.y + 18, b.w - 36, b.h - 36);
    ctx.restore();
  }
}

// ---------------- nesneler ----------------
function pinHead(ctx, x, y, r, a = 1) {
  ctx.save(); ctx.globalAlpha *= a; ctx.fillStyle = 'rgba(0,0,0,.45)'; ctx.beginPath(); ctx.ellipse(x + r * .5, y + r * .7, r * 1.05, r * .8, 0, 0, TAU); ctx.fill();
  const g = ctx.createRadialGradient(x - r * .35, y - r * .4, r * .1, x, y, r); g.addColorStop(0, '#ff8d80'); g.addColorStop(.35, '#d3261c'); g.addColorStop(1, '#6a0a06'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill(); ctx.restore();
}
function dropIn(ctx, o, t) { // yerine oturma: hafif büyükten küçülür, gölgesi yaklaşır
  const u = clamp((t - o.t0) / (o.dur || .6)), e = easeOut(u), lift = 1 - e;
  const [x, y] = [o.x, o.y]; ctx.translate(x, y); ctx.rotate((o.rot || 0) + lift * .035); ctx.scale(lerp(1.08, 1, e), lerp(1.08, 1, e)); ctx.globalAlpha *= clamp(u * 3.5);
  return lift;
}
function dimRect(ctx, lv, x, y, w, h) { if (lv < 1) { ctx.fillStyle = `rgba(6,8,9,${.62 * (1 - lv)})`; ctx.fillRect(x, y, w, h); } }
function polaroidGeom(o) { const im = IMG[o.img], c = cropOf(o, im), ph = o.w * c[3] / c[2], bw = o.w * .045, W2 = o.w + bw * 2, H2 = ph + bw + bw * (o.name && !o.tagOnPhoto ? 3.6 : 1.2); return { c, ph, bw, W2, H2 }; }
function polaroid(ctx, o, t, lv) {
  const im = IMG[o.img]; if (!im || !im.naturalWidth || t < o.t0) return; const G = polaroidGeom(o); const { c, ph, bw, W2, H2 } = G; const fa = fadeOf(o, t); if (fa <= 0) return;
  ctx.save(); ctx.globalAlpha = fa; const lift = dropIn(ctx, o, t);
  ctx.shadowColor = `rgba(0,0,0,${.6 - .2 * lift})`; ctx.shadowBlur = 50 + 140 * lift; ctx.shadowOffsetX = 14 + 50 * lift; ctx.shadowOffsetY = 24 + 80 * lift;
  ctx.fillStyle = '#ecebe6'; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2); ctx.shadowColor = 'transparent';
  ctx.drawImage(o.color ? im : (GRAY[o.img] || im), c[0], c[1], c[2], c[3], -o.w / 2, -H2 / 2 + bw, o.w, ph);
  ctx.fillStyle = 'rgba(30,40,40,.08)'; ctx.fillRect(-o.w / 2, -H2 / 2 + bw, o.w, ph);
  const ig = ctx.createLinearGradient(0, -H2 / 2 + bw, 0, -H2 / 2 + bw + ph); ig.addColorStop(0, 'rgba(0,0,0,.16)'); ig.addColorStop(.15, 'rgba(0,0,0,0)'); ig.addColorStop(.85, 'rgba(0,0,0,0)'); ig.addColorStop(1, 'rgba(0,0,0,.14)'); ctx.fillStyle = ig; ctx.fillRect(-o.w / 2, -H2 / 2 + bw, o.w, ph);
  if (o.censor) { // göz bandı: soldan sağa çekilen siyah şerit (orijinal görsel oranlarıyla)
    const cu = clamp((t - (o.censorT != null ? o.censorT : o.t0 + .25)) / .3); if (cu > 0) { const cr = o.crop || [0, 0, 1, 1], [a, b, c2, d2] = o.censor, fx = v => (v - cr[0]) / cr[2], fy = v => (v - cr[1]) / cr[3];
      const X0 = -o.w / 2 + fx(a) * o.w, Y0 = -H2 / 2 + bw + fy(b) * ph, X1 = -o.w / 2 + fx(c2) * o.w, Y1 = -H2 / 2 + bw + fy(d2) * ph; ctx.save(); ctx.fillStyle = '#050505'; ctx.shadowColor = 'rgba(0,0,0,.4)'; ctx.shadowBlur = 6; ctx.fillRect(X0, Y0, (X1 - X0) * easeOut(cu), Y1 - Y0); ctx.restore(); } }
  if (o.name) { // siyah isim bandı (beyaz aralıklı mono harf)
    const nu = clamp((t - (o.nameT || o.t0 + .35)) / .4); if (nu > 0) {
      const fs = o.nameSize || bw * 1.25; ctx.font = `600 ${fs}px ${MONO}`; ctx.letterSpacing = (fs * .14) + 'px'; const tw = ctx.measureText(o.name).width, ph2 = fs * 1.7, px = -W2 / 2 + bw * 1.1, py = -H2 / 2 + bw + ph - ph2 * .55;
      ctx.save(); ctx.globalAlpha *= easeOut(nu); ctx.shadowColor = 'rgba(0,0,0,.4)'; ctx.shadowBlur = 12; ctx.shadowOffsetY = 4; ctx.fillStyle = '#16191b'; ctx.fillRect(px, py, (tw + fs * 1.2) * easeOut(nu), ph2); ctx.shadowColor = 'transparent';
      ctx.beginPath(); ctx.rect(px, py, (tw + fs * 1.2) * easeOut(nu), ph2); ctx.clip(); ctx.fillStyle = '#efefe9'; ctx.textBaseline = 'middle'; ctx.fillText(o.name, px + fs * .6, py + ph2 * .53); ctx.restore();
    }
  }
  if (o.brackets) { const bu = clamp((t - o.brackets.t) / .35); if (bu > 0) { const [bx, by, bw2, bh2] = o.brackets.r, X = -o.w / 2 + bx * o.w, Y = -H2 / 2 + bw + by * ph, Wb = bw2 * o.w, Hb = bh2 * ph, L = Math.min(Wb, Hb) * .2, k = lerp(1.25, 1, easeOut(bu)); ctx.save(); ctx.globalAlpha *= easeOut(bu); ctx.translate(X + Wb / 2, Y + Hb / 2); ctx.scale(k, k); ctx.strokeStyle = ORANGE; ctx.lineWidth = o.w * .006; ctx.beginPath(); for (const [sx, sy] of [[-1, -1], [1, -1], [1, 1], [-1, 1]]) { const cx = sx * Wb / 2, cy = sy * Hb / 2; ctx.moveTo(cx, cy - sy * L); ctx.lineTo(cx, cy); ctx.lineTo(cx - sx * L, cy); } ctx.stroke(); ctx.restore(); } }
  dimRect(ctx, lv, -W2 / 2, -H2 / 2, W2, H2);
  if (o.pin !== false) { const pu = clamp((t - o.t0 - .3) / .25); if (pu > 0) pinHead(ctx, 0, -H2 / 2 + bw * .55, bw * .62 * lerp(1.6, 1, backOut(pu)), clamp(pu * 3)); }
  ctx.restore();
}
function pinOf(o) { // ipin bağlandığı raptiye noktası (dünya koordinatı)
  if (o.type === 'polaroid') { const G = polaroidGeom(o); return local(o, 0, -G.H2 / 2 + G.bw * .55); }
  if (o.type === 'doc') return local(o, o.pinX != null ? o.pinX * o.w : 0, -o.h / 2 + o.w * .035);
  if (o.type === 'tag') return local(o, -o.w / 2 + o.w * .14, 0);
  return [o.x, o.y];
}
function tag(ctx, o, t, lv) { // manila dosya etiketi: delik + raptiye, küçük "DOSYA", büyük yıl
  if (t < o.t0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const w = o.w, h = w * .52;
  ctx.save(); ctx.globalAlpha = fa; const lift = dropIn(ctx, o, t);
  ctx.shadowColor = 'rgba(0,0,0,.55)'; ctx.shadowBlur = 40 + 100 * lift; ctx.shadowOffsetX = 12 + 40 * lift; ctx.shadowOffsetY = 20 + 60 * lift;
  ctx.beginPath(); ctx.moveTo(-w / 2 + h * .32, -h / 2); ctx.lineTo(w / 2, -h / 2); ctx.lineTo(w / 2, h / 2); ctx.lineTo(-w / 2 + h * .32, h / 2); ctx.lineTo(-w / 2, h * .2); ctx.lineTo(-w / 2, -h * .2); ctx.closePath();
  ctx.fillStyle = pat(ctx, TEX.manila, 2); ctx.fill(); ctx.shadowColor = 'transparent';
  const g = ctx.createLinearGradient(-w / 2, 0, w / 2, 0); g.addColorStop(0, 'rgba(80,60,30,.12)'); g.addColorStop(1, 'rgba(255,255,255,.06)'); ctx.fillStyle = g; ctx.fill();
  const hx = -w / 2 + w * .14; ctx.beginPath(); ctx.arc(hx, 0, h * .12, 0, TAU); ctx.fillStyle = '#efe6cc'; ctx.fill(); ctx.lineWidth = h * .03; ctx.strokeStyle = 'rgba(120,100,60,.6)'; ctx.stroke();
  ctx.fillStyle = 'rgba(70,60,45,.55)'; ctx.font = `500 ${h * .11}px ${MONO}`; ctx.letterSpacing = (h * .03) + 'px'; ctx.textBaseline = 'alphabetic'; ctx.fillText(o.small || 'DOSYA', -w / 2 + w * .3, -h * .24);
  ctx.strokeStyle = 'rgba(70,60,45,.35)'; ctx.lineWidth = h * .012; ctx.beginPath(); ctx.moveTo(-w / 2 + w * .3, -h * .18); ctx.lineTo(w / 2 - w * .07, -h * .2); ctx.stroke();
  ctx.fillStyle = '#26221d'; ctx.font = `700 ${h * .5}px ${COND}`; ctx.letterSpacing = '0px'; { const mw = ctx.measureText(o.big).width, fsz = Math.min(h * .5, h * .5 * w * .64 / mw); ctx.font = `700 ${fsz}px ${COND}`; } ctx.fillText(o.big, -w / 2 + w * .28, h * .3);
  if (o.sub) { ctx.fillStyle = RED; ctx.font = `600 ${h * .1}px ${MONO}`; ctx.letterSpacing = (h * .025) + 'px'; ctx.fillText(o.sub, -w / 2 + w * .3, h * .43); }
  dimRect(ctx, lv, -w / 2, -h / 2, w, h); const pu = clamp((t - o.t0 - .3) / .25); if (pu > 0) pinHead(ctx, hx, 0, h * .1 * lerp(1.6, 1, backOut(pu)), clamp(pu * 3));
  ctx.restore();
}
function doc(ctx, o, t, lv) { // daktilo belge: başlık, gri satırlar, karartma, daktiloyla yazılan anahtar cümle + kırmızı daire
  if (t < o.t0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const w = o.w, h = o.h, m = w * .09, R = rng(o.seed || 5);
  ctx.save(); ctx.globalAlpha = fa; const lift = dropIn(ctx, o, t);
  ctx.shadowColor = 'rgba(0,0,0,.6)'; ctx.shadowBlur = 50 + 140 * lift; ctx.shadowOffsetX = 14 + 50 * lift; ctx.shadowOffsetY = 26 + 80 * lift;
  ctx.fillStyle = pat(ctx, TEX.paper, 2); ctx.fillRect(-w / 2, -h / 2, w, h); ctx.shadowColor = 'transparent';
  for (const f of [1 / 3, 2 / 3]) { const y = -h / 2 + h * f, g = ctx.createLinearGradient(0, y - h * .02, 0, y + h * .02); g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(.5, 'rgba(0,0,0,.07)'); g.addColorStop(.51, 'rgba(255,255,255,.25)'); g.addColorStop(1, 'rgba(0,0,0,0)'); ctx.fillStyle = g; ctx.fillRect(-w / 2, y - h * .02, w, h * .04); }
  let y = -h / 2 + m * 1.25; ctx.textBaseline = 'alphabetic'; ctx.fillStyle = '#2a2a28';
  (o.head || []).forEach((s, i) => { const fs = i === 0 ? w * .062 : w * .036; ctx.font = `${fs}px ${TYPE}`; ctx.letterSpacing = (fs * .06) + 'px'; y += fs * 1.25; ctx.fillText(s, -w / 2 + m, y); });
  y += w * .035; ctx.strokeStyle = 'rgba(40,40,38,.55)'; ctx.lineWidth = w * .003; ctx.beginPath(); ctx.moveTo(-w / 2 + m, y); ctx.lineTo(w / 2 - m, y); ctx.stroke(); y += w * .06;
  const row = (yy, k) => { let x = -w / 2 + m; const end = w / 2 - m - (k ? R() * w * .3 : 0); ctx.fillStyle = 'rgba(120,120,115,.42)'; while (x < end) { const L = w * (.03 + R() * .09); ctx.fillRect(x, yy - w * .011, Math.min(L, end - x), w * .016); x += L + w * .018; } };
  const red = new Set(o.redact || []);
  for (let i = 0; i < (o.rowsBefore || 3); i++) { if (red.has(i)) { ctx.fillStyle = '#141414'; ctx.fillRect(-w / 2 + m + w * .2, y - w * .017, w * .32, w * .026); row(y, 1); } else row(y, i === (o.rowsBefore || 3) - 1); y += w * .05; }
  if (o.key) { // anahtar cümle
    const fs = o.keySize || w * .068; ctx.font = `${fs}px ${TYPE}`; ctx.letterSpacing = (fs * .02) + 'px'; y += fs * .9;
    const full = o.key, n = Math.floor(clamp((t - o.keyT) / (o.keyDur || .8)) * full.length + .001), tw = ctx.measureText(full).width, kx = -w / 2 + m + (w - 2 * m - tw) / 2;
    ctx.fillStyle = '#1d1d1b'; ctx.fillText(full.slice(0, n), kx, y);
    if (o.circleT != null) { const cu = clamp((t - o.circleT) / .55); if (cu > 0) { const cx = kx + tw / 2, cy = y - fs * .32, rx = tw / 2 + fs * .55, ry = fs * .85; ctx.save(); ctx.strokeStyle = RED; ctx.lineWidth = w * .007; ctx.lineCap = 'round'; ctx.globalAlpha *= .92; ctx.beginPath(); const a0 = 2.6, sp = TAU * 1.07 * easeInOut(cu); for (let k = 0; k <= 90; k++) { const a = a0 + sp * k / 90, q = 1 + .035 * Math.sin(a * 2 + 1); const px = cx + Math.cos(a) * rx * q, py = cy + Math.sin(a) * ry * q * (1 + .06 * k / 90); k ? ctx.lineTo(px, py) : ctx.moveTo(px, py); } ctx.stroke(); ctx.restore(); } }
    y += fs * .9;
  }
  for (let i = 0; i < (o.rowsAfter || 4); i++) { y += w * .05; if (y > h / 2 - m) break; if (red.has(100 + i)) { ctx.fillStyle = '#141414'; ctx.fillRect(-w / 2 + m + w * .35, y - w * .017, w * .3, w * .026); } row(y, i === (o.rowsAfter || 4) - 1); }
  if (o.stamp) { const su = clamp((t - o.stamp.t) / .22); if (su > 0) { const S = o.stamp, fs = S.size || w * .09; ctx.save(); ctx.translate(S.x * w, S.y * h); ctx.rotate(S.rot || -.08); const k = lerp(1.5, 1, easeOut(su)); ctx.scale(k, k); ctx.globalAlpha *= .78 * clamp(su * 2); ctx.font = `700 ${fs}px ${COND}`; ctx.letterSpacing = (fs * .08) + 'px'; const tw = ctx.measureText(S.text).width; ctx.strokeStyle = RED; ctx.lineWidth = fs * .08; ctx.strokeRect(-tw / 2 - fs * .35, -fs * .82, tw + fs * .7, fs * 1.15); ctx.fillStyle = RED; ctx.textAlign = 'center'; ctx.fillText(S.text, 0, 0); ctx.restore(); } }
  dimRect(ctx, lv, -w / 2, -h / 2, w, h);
  if (o.pin !== false) { const pu = clamp((t - o.t0 - .3) / .25); if (pu > 0) pinHead(ctx, o.pinX != null ? o.pinX * w : 0, -h / 2 + w * .035, w * .028 * lerp(1.6, 1, backOut(pu)), clamp(pu * 3)); }
  ctx.restore();
}
function thread(ctx, o, t, lv) { // kırmızı ip: iki raptiye arası sarkan çizgi, uzayarak gerilir
  const u = clamp((t - o.t0) / (o.dur || .7)); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return;
  const A = OBJ[o.from], B = OBJ[o.to]; if (!A || !B || t < A.t0 || t < B.t0) return; const p = pinOf(A), q = pinOf(B), d = Math.hypot(q[0] - p[0], q[1] - p[1]);
  const cx = (p[0] + q[0]) / 2, cy = (p[1] + q[1]) / 2 + d * (o.sag != null ? o.sag : .1) * lerp(1.6, 1, easeOut(u));
  ctx.save(); ctx.globalAlpha = fa * (.3 + .7 * lv); ctx.lineCap = 'round'; ctx.strokeStyle = '#b8261f'; ctx.lineWidth = o.width || 6; ctx.shadowColor = 'rgba(0,0,0,.5)'; ctx.shadowBlur = 8; ctx.shadowOffsetY = 6;
  ctx.beginPath(); const E = easeInOut(u); for (let k = 0; k <= 40; k++) { const s = E * k / 40, x = (1 - s) * (1 - s) * p[0] + 2 * (1 - s) * s * cx + s * s * q[0], y = (1 - s) * (1 - s) * p[1] + 2 * (1 - s) * s * cy + s * s * q[1]; k ? ctx.lineTo(x, y) : ctx.moveTo(x, y); } ctx.stroke(); ctx.shadowColor = 'transparent';
  pinHead(ctx, p[0], p[1], o.pinR || 22); if (u >= 1) pinHead(ctx, q[0], q[1], o.pinR || 22); ctx.restore();
}
function halftone(ctx, o, t, lv) { // siyah üstünde nokta portre, merkezden dışa açılır
  const H = HALF[o.id]; if (!H || t < o.t0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const cell = o.w / H.cols, x0 = o.x - o.w / 2, y0 = o.y - cell * H.rows / 2, rev = o.rev || 1.1;
  ctx.save(); ctx.globalAlpha = fa * (.25 + .75 * lv);
  if (o.glow) { const [gx, gy] = [x0 + o.glow[0] * o.w, y0 + o.glow[1] * cell * H.rows], gr = o.w * .12, ga = smooth((t - o.t0 - .5) / .8) * (.75 + .25 * Math.sin(t * 2.2)); const g = ctx.createRadialGradient(gx, gy, 0, gx, gy, gr); const gc = o.glowColor || '215,50,35'; g.addColorStop(0, `rgba(${gc},${.75 * ga})`); g.addColorStop(1, `rgba(${gc},0)`); ctx.fillStyle = g; ctx.fillRect(gx - gr, gy - gr, gr * 2, gr * 2); }
  ctx.fillStyle = '#d9dbd6'; const buckets = [[], [], [], []];
  for (const d of H.dots) { const a = clamp((t - o.t0 - d.d * rev) / .35); if (a <= 0) continue; buckets[Math.min(3, (a * 4) | 0)].push(d); }
  buckets.forEach((B, bi) => { if (!B.length) return; ctx.globalAlpha = fa * (.25 + .75 * lv) * (bi + 1) / 4; ctx.beginPath(); for (const d of B) { const r = cell * .5 * Math.sqrt(d.l) * .98, cx = x0 + (d.i + .5 + (d.j % 2) * .5) * cell, cy = y0 + (d.j + .5) * cell; ctx.moveTo(cx + r, cy); ctx.arc(cx, cy, r, 0, TAU); } ctx.fill(); });
  ctx.restore();
}
function glowdot(ctx, o, t, lv) { // ışıyan şehir noktası + mono etiket + kesikli kare + nişangâh
  const u = clamp((t - o.t0) / .5); if (u <= 0) return; const fa = fadeOf(o, t) * (.3 + .7 * lv); if (fa <= 0) return; const [x, y] = proj(o.lon, o.lat), z = CURZ, pulse = 1 + .12 * Math.sin(t * 3.1);
  ctx.save(); ctx.globalAlpha = fa * easeOut(u);
  const gr = 120 / z * pulse, g = ctx.createRadialGradient(x, y, 0, x, y, gr); g.addColorStop(0, 'rgba(255,150,90,.85)'); g.addColorStop(.25, 'rgba(240,100,60,.35)'); g.addColorStop(1, 'rgba(240,90,50,0)'); ctx.globalCompositeOperation = 'lighter'; ctx.fillStyle = g; ctx.fillRect(x - gr, y - gr, gr * 2, gr * 2); ctx.globalCompositeOperation = 'source-over';
  ctx.fillStyle = '#ffd9c2'; ctx.beginPath(); ctx.arc(x, y, 9 / z, 0, TAU); ctx.fill();
  if (o.square) { const s = 46 / z * lerp(1.6, 1, easeOut(u)); ctx.setLineDash([7 / z, 6 / z]); ctx.strokeStyle = 'rgba(240,117,78,.85)'; ctx.lineWidth = 2.2 / z; ctx.strokeRect(x - s, y - s, s * 2, s * 2); ctx.setLineDash([]); }
  if (o.label) { const lu = clamp((t - o.t0 - .2) / .5), fs = o.size / z; ctx.font = `600 ${fs}px ${MONO}`; ctx.letterSpacing = (fs * .16) + 'px'; ctx.textBaseline = 'middle'; const tw = ctx.measureText(o.label).width; const lx = x + (o.dx != null ? o.dx : 70 / z), ly = y + (o.dy || 0); ctx.save(); ctx.beginPath(); ctx.rect(lx - 10, ly - fs, (tw + 40) * easeOut(lu), fs * 2); ctx.clip(); ctx.fillStyle = 'rgba(0,0,0,.45)'; ctx.shadowColor = 'rgba(0,0,0,.8)'; ctx.shadowBlur = 20; ctx.fillStyle = ORANGE; ctx.fillText(o.label, lx, ly); ctx.restore(); }
  if (o.crossT != null) { const cu = clamp((t - o.crossT) / .45); if (cu > 0) { const R = 120 / z * lerp(1.5, 1, easeOut(cu)); ctx.save(); ctx.translate(x, y); ctx.rotate(lerp(-.6, -.2, easeOut(cu))); ctx.globalAlpha *= easeOut(cu); ctx.strokeStyle = RED; ctx.lineWidth = 3.5 / z; ctx.beginPath(); ctx.arc(0, 0, R, 0, TAU * easeInOut(cu)); ctx.stroke(); ctx.beginPath(); for (const [a, b] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { ctx.moveTo(a * R * .55, b * R * .55); ctx.lineTo(a * R * 1.35, b * R * 1.35); } ctx.stroke(); ctx.restore(); } }
  ctx.restore();
}
function region(ctx, o, t, lv) { // soluk, geniş aralıklı bölge adı
  const u = smooth((t - (o.t0 || -9)) / .8); if (u <= 0) return; const [x, y] = o.lon != null ? proj(o.lon, o.lat) : [o.x, o.y];
  ctx.save(); ctx.globalAlpha = u * (o.alpha || .22) * (.4 + .6 * lv) * fadeOf(o, t); ctx.font = `500 ${o.size}px ${MONO}`; ctx.letterSpacing = (o.size * .4) + 'px'; ctx.textAlign = 'center'; ctx.fillStyle = '#cfe0de'; ctx.fillText(o.text, x, y); ctx.restore();
}
function title(ctx, o, t, lv) { // büyük ince serif başlık, iki yanında ince çizgi ve kırmızı uç
  const u = clamp((t - o.t0) / (o.dur || .9)); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const e = easeOut(u), fs = o.size;
  ctx.save(); ctx.globalAlpha = fa * smooth(u * 1.4) * (.2 + .8 * lv); ctx.font = `${o.weight || 500} ${fs}px ${o.font === 'mono' ? MONO : SERIF}`; ctx.letterSpacing = (fs * lerp(.24, o.track != null ? o.track : .12, e)) + 'px'; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
  ctx.shadowColor = 'rgba(0,0,0,.7)'; ctx.shadowBlur = fs * .3; ctx.fillStyle = o.color || '#f1ede4';
  const lines = o.text.split('\n'), lh = fs * (o.lh || 1.02); const A0 = ctx.globalAlpha; lines.forEach((s, i) => { let ee = e; if (o.lineT) { const lu = clamp((t - o.lineT[i]) / (o.dur || .9)); if (lu <= 0) return; ee = easeOut(lu); ctx.globalAlpha = fa * smooth(lu * 1.4) * (.2 + .8 * lv); } ctx.fillText(s, o.x, o.y + i * lh + (1 - ee) * fs * .12); }); ctx.globalAlpha = A0;
  if (o.rule) { const tw = ctx.measureText(lines[0]).width - fs * .12, gap = fs * .3, L = o.rule * easeInOut(clamp((t - o.t0 - .25) / .8)), yy = o.y - fs * .33; ctx.shadowColor = 'transparent';
    for (const s of [-1, 1]) { const a = o.x + s * (tw / 2 + gap); ctx.strokeStyle = 'rgba(230,230,225,.45)'; ctx.lineWidth = fs * .012; ctx.beginPath(); ctx.moveTo(a, yy); ctx.lineTo(a + s * L, yy); ctx.stroke(); ctx.strokeStyle = RED; ctx.lineWidth = fs * .022; ctx.beginPath(); ctx.moveTo(a, yy); ctx.lineTo(a + s * Math.min(L, fs * .22), yy); ctx.stroke(); } }
  ctx.restore();
}
function strike(ctx, o, t, lv) { // mono yazı, söylenince kırmızı çizgiyle üstü çizilir
  const u = clamp((t - o.t0) / .45); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const fs = o.size, su = clamp((t - o.tStrike) / .35);
  ctx.save(); ctx.globalAlpha = fa * easeOut(u) * (.25 + .75 * lv) * (1 - .45 * smooth(su)); ctx.font = `600 ${fs}px ${MONO}`; ctx.letterSpacing = (fs * .1) + 'px'; ctx.textAlign = 'center'; ctx.fillStyle = o.color || '#c4c7c3'; ctx.shadowColor = 'rgba(0,0,0,.7)'; ctx.shadowBlur = fs * .3;
  ctx.fillText(o.text, o.x, o.y); const tw = ctx.measureText(o.text).width; ctx.restore();
  if (su > 0) { ctx.save(); ctx.globalAlpha = fa * (.3 + .7 * lv); ctx.strokeStyle = RED; ctx.lineCap = 'round'; ctx.lineWidth = fs * .075; ctx.beginPath(); const a = o.x - tw / 2 - fs * .15, b = o.x + tw / 2 + fs * .1; ctx.moveTo(a, o.y - fs * .34); ctx.lineTo(lerp(a, b, easeInOut(su)), o.y - fs * .34 - fs * .03 * easeInOut(su)); ctx.stroke(); ctx.restore(); }
}
function band(ctx, o, t, lv) { // tek başına siyah mono bant (etiket)
  const u = clamp((t - o.t0) / .4); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const fs = o.size;
  ctx.save(); ctx.globalAlpha = fa * (.3 + .7 * lv); ctx.translate(o.x, o.y); ctx.rotate(o.rot || 0); ctx.font = `600 ${fs}px ${MONO}`; ctx.letterSpacing = (fs * .14) + 'px'; const tw = ctx.measureText(o.text).width, W = tw + fs * 1.2, H = fs * 1.7;
  ctx.shadowColor = 'rgba(0,0,0,.5)'; ctx.shadowBlur = fs * .4; ctx.shadowOffsetY = fs * .12; ctx.fillStyle = o.bg || '#15181a'; ctx.fillRect(-W / 2, -H / 2, W * easeOut(u), H); ctx.shadowColor = 'transparent';
  if (o.red) { ctx.fillStyle = RED; ctx.fillRect(-W / 2, -H / 2, fs * .14, H); }
  ctx.beginPath(); ctx.rect(-W / 2, -H / 2, W * easeOut(u), H); ctx.clip(); ctx.fillStyle = o.color || '#efefe9'; ctx.textBaseline = 'middle'; ctx.fillText(o.text, -W / 2 + fs * .6, fs * .04);
  ctx.restore(); if (o.pin) { ctx.save(); ctx.globalAlpha = fa; const [px, py] = local(o, 0, -fs * .85); pinHead(ctx, px, py, fs * .22); ctx.restore(); }
}
function route(ctx, o, t, lv) { // ışıyan turuncu rota, ucunda nokta
  const u = clamp((t - o.t0) / (o.t1 - o.t0)); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const z = CURZ;
  const P = o.pts.map(([lo, la]) => proj(lo, la)), L = []; let tot = 0; for (let i = 1; i < P.length; i++) { const d = Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]); L.push(d); tot += d; }
  let rem = easeInOut(u) * tot; const path = [P[0]]; let tip = P[0];
  for (let i = 1; i < P.length && rem > 0; i++) { const k = Math.min(1, rem / L[i - 1]); tip = [lerp(P[i - 1][0], P[i][0], k), lerp(P[i - 1][1], P[i][1], k)]; path.push(tip); rem -= L[i - 1]; }
  ctx.save(); ctx.globalAlpha = fa * (.3 + .7 * lv); ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  const stroke = (w, c) => { ctx.strokeStyle = c; ctx.lineWidth = w / z; ctx.beginPath(); path.forEach((p, i) => i ? ctx.lineTo(...p) : ctx.moveTo(...p)); ctx.stroke(); };
  stroke(18, 'rgba(240,117,78,.12)'); if (o.dash) ctx.setLineDash([16 / z, 12 / z]); stroke(4.5, o.color || ORANGE); ctx.setLineDash([]);
  if (u < 1) { const g = ctx.createRadialGradient(tip[0], tip[1], 0, tip[0], tip[1], 60 / z); g.addColorStop(0, 'rgba(255,170,120,.9)'); g.addColorStop(1, 'rgba(255,120,80,0)'); ctx.fillStyle = g; ctx.fillRect(tip[0] - 60 / z, tip[1] - 60 / z, 120 / z, 120 / z); }
  ctx.restore();
}
function ring(ctx, o, t, lv) { // kuşatma halkası: kesikli kırmızı daire içe doğru daralır, oklar merkeze bakar
  const u = clamp((t - o.t0) / (o.dur || 1.6)); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const [x, y] = proj(o.lon, o.lat), z = CURZ, r = lerp(o.r0, o.r1, easeInOut(u));
  ctx.save(); ctx.globalAlpha = fa * smooth(u * 3) * (.3 + .7 * lv); ctx.strokeStyle = RED; ctx.lineWidth = 3.5 / z; ctx.setLineDash([22 / z, 14 / z]); ctx.lineDashOffset = -t * 40 / z; ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.stroke(); ctx.setLineDash([]);
  const n = o.n || 10; for (let k = 0; k < n; k++) { const a = k / n * TAU + .3, ax = x + Math.cos(a) * r, ay = y + Math.sin(a) * r, L = 70 / z, h = 22 / z; ctx.beginPath(); ctx.moveTo(ax + Math.cos(a) * L, ay + Math.sin(a) * L); ctx.lineTo(ax, ay); ctx.stroke(); ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(ax + Math.cos(a + .5) * h, ay + Math.sin(a + .5) * h); ctx.moveTo(ax, ay); ctx.lineTo(ax + Math.cos(a - .5) * h, ay + Math.sin(a - .5) * h); ctx.stroke(); }
  ctx.restore();
}
function xmark(ctx, o, t, lv) { // kırmızı çarpı (kesilen yol)
  const u = clamp((t - o.t0) / .4); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const [x, y] = proj(o.lon, o.lat), s = (o.s || 70) / CURZ;
  ctx.save(); ctx.globalAlpha = fa * (.3 + .7 * lv); ctx.strokeStyle = RED; ctx.lineCap = 'round'; ctx.lineWidth = 9 / CURZ; const a = clamp(u * 2), b = clamp(u * 2 - 1);
  ctx.beginPath(); ctx.moveTo(x - s, y - s); ctx.lineTo(x - s + 2 * s * easeOut(a), y - s + 2 * s * easeOut(a)); ctx.stroke(); if (b > 0) { ctx.beginPath(); ctx.moveTo(x + s, y - s); ctx.lineTo(x + s - 2 * s * easeOut(b), y - s + 2 * s * easeOut(b)); ctx.stroke(); } ctx.restore();
}
function counter(ctx, o, t, lv) { // altın sayaç: söylenen rakama kadar sayar
  const u = clamp((t - o.t0) / (o.dur || 2)); if (t < o.t0) return; const fa = fadeOf(o, t); if (fa <= 0) return;
  const e = 1 - Math.pow(1 - u, 3), v = o.from + (o.to - o.from) * e, txt = (o.prefix || '') + (o.fmt ? o.fmt(v) : Math.round(v).toLocaleString('tr-TR')) + (o.suffix || '');
  ctx.save(); ctx.globalAlpha = fa * smooth(u * 6) * (.3 + .7 * lv); ctx.translate(o.x, o.y); const pop = u >= 1 ? 1 + .06 * Math.exp(-(t - o.t0 - (o.dur || 2)) * 6) : 1; ctx.scale(pop, pop);
  ctx.font = `700 ${o.size}px ${COND}`; ctx.letterSpacing = (o.size * .02) + 'px'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  const g = ctx.createLinearGradient(0, -o.size / 2, 0, o.size / 2); g.addColorStop(0, o.c1 || '#ffe9a8'); g.addColorStop(.55, o.c2 || '#e3b04b'); g.addColorStop(1, o.c3 || '#9a6a1c');
  ctx.shadowColor = o.glow || 'rgba(255,190,80,.55)'; ctx.shadowBlur = o.size * .35; ctx.fillStyle = 'rgba(0,0,0,.6)'; ctx.fillText(txt, 6, 10); ctx.fillStyle = o.solid || g; ctx.fillText(txt, 0, 0);
  if (o.sub) { ctx.shadowBlur = 0; ctx.font = `600 ${o.subSize || o.size * .28}px ${MONO}`; ctx.letterSpacing = '6px'; ctx.fillStyle = o.subColor || 'rgba(240,230,210,.8)'; ctx.fillText(o.sub, 0, o.size * .78); }
  ctx.restore();
}
function car(ctx, o, t, lv) { // kodla çizilen lüks araba silueti + far ışığı
  const u = clamp((t - o.t0) / .8); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const w = o.w, h = w * .3;
  ctx.save(); ctx.globalAlpha = fa * easeOut(u) * (.3 + .7 * lv); ctx.translate(o.x + (1 - easeOut(u)) * w * .25, o.y); if (o.flip) ctx.scale(-1, 1);
  const body = new Path2D(); body.moveTo(-w * .5, h * .25); body.lineTo(-w * .48, -h * .05); body.quadraticCurveTo(-w * .4, -h * .18, -w * .22, -h * .2); body.quadraticCurveTo(-w * .1, -h * .55, w * .08, -h * .55); body.quadraticCurveTo(w * .22, -h * .55, w * .32, -h * .22); body.quadraticCurveTo(w * .47, -h * .18, w * .5, h * .02); body.lineTo(w * .5, h * .25); body.closePath();
  const gb = ctx.createLinearGradient(0, -h * .6, 0, h * .3); gb.addColorStop(0, '#2a2620'); gb.addColorStop(.5, '#0d0c0a'); gb.addColorStop(1, '#050505'); ctx.fillStyle = gb; ctx.fill(body);
  ctx.strokeStyle = 'rgba(255,215,140,.75)'; ctx.lineWidth = w * .004; ctx.stroke(body); ctx.beginPath(); ctx.moveTo(-w * .2, -h * .2); ctx.quadraticCurveTo(w * .05, -h * .25, w * .3, -h * .21); ctx.strokeStyle = 'rgba(255,215,140,.35)'; ctx.stroke();
  for (const cx of [-w * .3, w * .3]) { ctx.beginPath(); ctx.arc(cx, h * .25, h * .2, 0, TAU); ctx.fillStyle = '#050505'; ctx.fill(); ctx.strokeStyle = 'rgba(255,215,140,.6)'; ctx.lineWidth = w * .006; ctx.stroke(); }
  const fl = .7 + .3 * Math.sin(t * 2); const hx = w * .48, hy = -h * .02; const g = ctx.createRadialGradient(hx, hy, 0, hx, hy, w * .5); g.addColorStop(0, `rgba(255,240,200,${.9 * fl})`); g.addColorStop(.15, `rgba(255,220,150,${.35 * fl})`); g.addColorStop(1, 'rgba(255,200,120,0)');
  ctx.globalCompositeOperation = 'lighter'; ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(hx, hy); ctx.lineTo(hx + w * .9, hy - h * .5); ctx.lineTo(hx + w * .9, hy + h * .6); ctx.closePath(); ctx.fill(); ctx.globalCompositeOperation = 'source-over';
  ctx.restore();
}
function scale(ctx, o, t, lv) { // terazi: kol açısı zamana göre yatar; kefelere yazı/nesne
  const u = clamp((t - o.t0) / .6); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const w = o.w; let ang = 0;
  for (const k of (o.tilt || [])) if (t >= k.t) ang = lerp(ang, k.a, 1); let a0 = 0; for (const k of (o.tilt || [])) { if (t >= k.t) { const p = clamp((t - k.t) / (k.dur || 1.4)); ang = lerp(a0, k.a, easeInOut(p)); a0 = k.a; } }
  ctx.save(); ctx.globalAlpha = fa * easeOut(u) * (.3 + .7 * lv); ctx.translate(o.x, o.y); ctx.strokeStyle = o.color || '#e3b04b'; ctx.fillStyle = o.color || '#e3b04b'; ctx.lineWidth = w * .012; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(0, -w * .05); ctx.lineTo(0, w * .7); ctx.moveTo(-w * .2, w * .7); ctx.lineTo(w * .2, w * .7); ctx.stroke(); ctx.beginPath(); ctx.arc(0, -w * .06, w * .03, 0, TAU); ctx.fill();
  ctx.rotate(ang); ctx.beginPath(); ctx.moveTo(-w / 2, 0); ctx.lineTo(w / 2, 0); ctx.stroke();
  for (const s of [-1, 1]) { const px = s * w / 2; ctx.save(); ctx.translate(px, 0); ctx.rotate(-ang); ctx.lineWidth = w * .005; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(-w * .14, w * .3); ctx.moveTo(0, 0); ctx.lineTo(w * .14, w * .3); ctx.stroke(); ctx.beginPath(); ctx.ellipse(0, w * .3, w * .17, w * .035, 0, 0, Math.PI); ctx.fill();
    const lab = s < 0 ? o.left : o.right; if (lab) { ctx.font = `700 ${w * .07}px ${COND}`; ctx.textAlign = 'center'; ctx.fillStyle = s < 0 ? (o.leftColor || '#ffe1a0') : (o.rightColor || '#dfe8e6'); ctx.fillText(lab, 0, w * .44); }
    const dots = s < 0 ? o.leftDots : o.rightDots; if (dots) { const R = rng(s < 0 ? 3 : 9); ctx.fillStyle = s < 0 ? '#ffd27a' : '#cfe0de'; for (let k = 0; k < dots; k++) { const dx = (R() - .5) * w * .28, dy = w * .26 - R() * w * .1 * Math.min(1, dots / 40); ctx.beginPath(); ctx.arc(dx, dy, w * (dots > 1 ? .008 : .05), 0, TAU); ctx.fill(); } }
    ctx.restore(); }
  ctx.restore();
}
function meter(ctx, o, t, lv) { // eriyen para çubuğu
  if (t < o.t0) return; const fa = fadeOf(o, t); if (fa <= 0) return; let v = o.keys[0].v; for (let i = 1; i < o.keys.length; i++) { const k = o.keys[i]; if (t >= k.t) v = lerp(o.keys[i - 1].v, k.v, easeInOut((t - k.t) / (k.dur || .6))); }
  ctx.save(); ctx.globalAlpha = fa * smooth((t - o.t0) / .4) * (.3 + .7 * lv); ctx.translate(o.x, o.y); ctx.fillStyle = 'rgba(10,12,13,.85)'; ctx.fillRect(-o.w / 2, -o.h / 2, o.w, o.h); ctx.strokeStyle = 'rgba(230,230,225,.6)'; ctx.lineWidth = 6; ctx.strokeRect(-o.w / 2, -o.h / 2, o.w, o.h);
  ctx.fillStyle = v > .3 ? '#5fbf7a' : '#c8322a'; ctx.fillRect(-o.w / 2 + 12, -o.h / 2 + 12, (o.w - 24) * v, o.h - 24);
  ctx.font = `600 ${o.h * .42}px ${MONO}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillStyle = '#f1efe8'; ctx.fillText(o.label + ' ' + Math.round(v * 100) + '%', 0, 2); ctx.restore();
}
function lights(ctx, o, t, lv) { // il ışıkları tek tek yanar
  if (t < o.t0) return; const z = CURZ; ctx.save(); ctx.globalCompositeOperation = 'lighter';
  o.pts.forEach(([lo, la], i) => { const a = clamp((t - o.t0 - i * (o.step || .03)) / .4); if (a <= 0) return; const [x, y] = proj(lo, la), r = 60 / z * (1 + .1 * Math.sin(t * 3 + i)); const g = ctx.createRadialGradient(x, y, 0, x, y, r); g.addColorStop(0, `rgba(255,200,130,${.95 * a})`); g.addColorStop(.25, `rgba(255,150,80,${.45 * a})`); g.addColorStop(1, 'rgba(255,120,60,0)'); ctx.fillStyle = g; ctx.fillRect(x - r, y - r, 2 * r, 2 * r); });
  ctx.restore();
}
function chart(ctx, o, t, lv) { // altın yükselen hisse grafiği (dünya koordinatında)
  const u = clamp((t - o.t0) / (o.dur || 1.6)); if (u <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return; const P = o.pts.map(([a, b]) => [o.x + a * o.w, o.y - b * o.h]); const n = (P.length - 1) * easeInOut(u), k = Math.floor(n), fr = n - k;
  const path = P.slice(0, k + 1); if (k < P.length - 1) path.push([lerp(P[k][0], P[k + 1][0], fr), lerp(P[k][1], P[k + 1][1], fr)]);
  ctx.save(); ctx.globalAlpha = fa * (.3 + .7 * lv); ctx.strokeStyle = 'rgba(255,215,140,.15)'; ctx.lineWidth = 2; for (let i = 0; i <= 4; i++) { const y = o.y - o.h * i / 4; ctx.beginPath(); ctx.moveTo(o.x, y); ctx.lineTo(o.x + o.w, y); ctx.stroke(); }
  const g = ctx.createLinearGradient(0, o.y - o.h, 0, o.y); g.addColorStop(0, 'rgba(240,190,90,.35)'); g.addColorStop(1, 'rgba(240,190,90,0)'); ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(path[0][0], o.y); path.forEach(p => ctx.lineTo(...p)); ctx.lineTo(path[path.length - 1][0], o.y); ctx.closePath(); ctx.fill();
  ctx.strokeStyle = '#f2c46b'; ctx.lineWidth = o.w * .008; ctx.lineJoin = 'round'; ctx.shadowColor = 'rgba(255,190,80,.8)'; ctx.shadowBlur = 30; ctx.beginPath(); path.forEach((p, i) => i ? ctx.lineTo(...p) : ctx.moveTo(...p)); ctx.stroke();
  const tip = path[path.length - 1]; ctx.beginPath(); ctx.arc(tip[0], tip[1], o.w * .015, 0, TAU); ctx.fillStyle = '#fff2c8'; ctx.fill(); ctx.restore();
}
function backdrop(ctx, o, t, lv) { // karanlık sahnelerin arkasında soluk, gri tonlu tam kadraj fotoğraf
  const im = IMG[o.img]; if (!im || !im.naturalWidth) return; const a = smooth((t - o.t0) / (o.dur || 1.2)); if (a <= 0) return; const fa = fadeOf(o, t); if (fa <= 0) return;
  const src = o.color ? im : (GRAY[o.img] || im), r = Math.max(o.w / im.naturalWidth, o.h / im.naturalHeight), dw = im.naturalWidth * r, dh = im.naturalHeight * r, k = 1 + .04 * clamp((t - o.t0) / 12);
  ctx.save(); ctx.beginPath(); ctx.rect(o.x - o.w / 2, o.y - o.h / 2, o.w, o.h); ctx.clip(); ctx.globalAlpha = a * fa * (o.alpha || .32);
  ctx.translate(o.x, o.y); ctx.scale(k, k); ctx.drawImage(src, -dw / 2, -dh / 2, dw, dh); ctx.setTransform(ctx.getTransform());
  ctx.restore(); ctx.save(); const g = ctx.createRadialGradient(o.x, o.y, Math.min(o.w, o.h) * .2, o.x, o.y, Math.max(o.w, o.h) * .62); g.addColorStop(0, 'rgba(10,14,15,0)'); g.addColorStop(1, 'rgba(10,14,15,.95)'); ctx.fillStyle = g; ctx.globalAlpha = a * fa; ctx.fillRect(o.x - o.w / 2, o.y - o.h / 2, o.w, o.h); ctx.restore();
}
const DRAW = { backdrop, chart, counter, car, scale, meter, lights, band, route, ring, xmark, polaroid, tag, doc, thread, halftone, glowdot, region, title, strike };
let OBJ = {};

// ---------------- ekran katmanları ----------------
function drawTimeline(ctx, t) {
  if (typeof TIMELINE === 'undefined') return; const T = TIMELINE, a = smooth((t - (T.t0 || 0)) / .8) * (T.t1 != null ? 1 - smooth((t - T.t1) / .6) : 1); if (a <= 0) return;
  const W = FORMAT.w, y = FORMAT.h - (T.bottom || 170), x0 = 90, x1 = W - 90, [ya, yb] = [T.years[0], T.years[T.years.length - 1]], X = v => lerp(x0, x1, (v - ya) / (yb - ya));
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = 'rgba(220,225,222,.2)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
  ctx.font = `500 24px ${MONO}`; ctx.letterSpacing = '3px'; ctx.textAlign = 'center'; ctx.fillStyle = 'rgba(220,225,222,.32)';
  for (let v = ya; v <= yb + 1e-6; v += 1 / 12) { const yr = Math.abs(v - Math.round(v)) < 1e-6, x = X(v); ctx.strokeStyle = `rgba(220,225,222,${yr ? .35 : .12})`; ctx.beginPath(); ctx.moveTo(x, y - (yr ? 14 : 6)); ctx.lineTo(x, y); ctx.stroke(); if (yr) ctx.fillText(String(Math.round(v)), x, y + 40); }
  let v = T.keys[0].v; for (let i = 1; i < T.keys.length; i++) { const k = T.keys[i]; if (t >= k.t) v = lerp(T.keys[i - 1].v, k.v, easeInOut((t - k.t) / (k.dur || 1.2))); }
  const mx = X(v); ctx.strokeStyle = RED; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(mx, y - 34); ctx.lineTo(mx, y + 10); ctx.stroke(); ctx.fillStyle = RED; ctx.beginPath(); ctx.moveTo(mx - 7, y - 40); ctx.lineTo(mx + 7, y - 40); ctx.lineTo(mx, y - 31); ctx.fill();
  ctx.font = `600 34px ${MONO}`; ctx.letterSpacing = '5px'; ctx.fillStyle = ORANGE; ctx.fillText(T.label ? T.label(v) : String(Math.floor(v + 1e-4)), mx, y - 56);
  ctx.restore();
}
function drawDust(ctx, t, cam) {
  ctx.save(); ctx.globalCompositeOperation = 'lighter';
  for (const d of TEX.dust) { const x = ((d.x + d.vx * t - cam.x * cam.z * .00004) % 1 + 1) % 1 * FORMAT.w, y = ((d.y + d.vy * t - cam.y * cam.z * .00003) % 1 + 1) % 1 * FORMAT.h, a = d.a * (.6 + .4 * Math.sin(t * 1.3 + d.p)) * .5, r = d.r * 2.4; const g = ctx.createRadialGradient(x, y, 0, x, y, r); g.addColorStop(0, d.warm ? `rgba(255,140,90,${a})` : `rgba(200,225,225,${a * .6})`); g.addColorStop(1, 'rgba(0,0,0,0)'); ctx.fillStyle = g; ctx.fillRect(x - r, y - r, r * 2, r * 2); }
  ctx.restore();
}

// ---------------- kare ----------------
const canvas = document.getElementById('c'); canvas.width = FORMAT.w; canvas.height = FORMAT.h; const out = canvas.getContext('2d');
const buf = document.createElement('canvas'); buf.width = FORMAT.w; buf.height = FORMAT.h; const bctx = buf.getContext('2d');
const glowC = document.createElement('canvas'); glowC.width = FORMAT.w / 4; glowC.height = FORMAT.h / 4; const gctx = glowC.getContext('2d');
const SPC = typeof SPACES !== 'undefined' ? SPACES : [{ t: 0, s: 'map', cam: CAMERA }], TR = .8;
const keysOf = sc => sc.cam || CAMERA;
function drawCork(ctx, cam) {
  ctx.fillStyle = pat(ctx, TEX.cork, 3); ctx.fillRect(cam.x - 6000, cam.y - 8000, 12000, 16000);
  const g = ctx.createRadialGradient(cam.x, cam.y - 300, 400, cam.x, cam.y, 4200); g.addColorStop(0, 'rgba(255,215,160,.10)'); g.addColorStop(1, 'rgba(25,12,5,.5)'); ctx.fillStyle = g; ctx.fillRect(cam.x - 6000, cam.y - 8000, 12000, 16000);
}
function drawDark(ctx, cam) {
  ctx.fillStyle = '#0a0e0f'; ctx.fillRect(cam.x - 8000, cam.y - 10000, 16000, 20000);
  ctx.strokeStyle = 'rgba(160,200,200,.035)'; ctx.lineWidth = 1.5 / CURZ; ctx.beginPath(); const G = 420;
  for (let x = Math.floor((cam.x - 3000) / G) * G; x < cam.x + 3000; x += G) { ctx.moveTo(x, cam.y - 4000); ctx.lineTo(x, cam.y + 4000); }
  for (let y = Math.floor((cam.y - 4000) / G) * G; y < cam.y + 4000; y += G) { ctx.moveTo(cam.x - 3000, y); ctx.lineTo(cam.x + 3000, y); } ctx.stroke();
}
function drawSplit(ctx, cam) {
  const X0 = cam.x - 6000, W = 12000; const g = ctx.createLinearGradient(0, -3500, 0, 0); g.addColorStop(0, '#050403'); g.addColorStop(1, '#1d160c'); ctx.fillStyle = g; ctx.fillRect(X0, -9000, W, 9000);
  const sp = ctx.createRadialGradient(cam.x, -900, 100, cam.x, -900, 2600); sp.addColorStop(0, 'rgba(255,200,110,.20)'); sp.addColorStop(1, 'rgba(255,200,110,0)'); ctx.fillStyle = sp; ctx.fillRect(X0, -9000, W, 9000);
  ctx.fillStyle = pat(ctx, TEX.cork, 3); ctx.fillRect(X0, 0, W, 9000); const c = ctx.createLinearGradient(0, 0, 0, 3500); c.addColorStop(0, 'rgba(20,50,58,.35)'); c.addColorStop(1, 'rgba(5,10,12,.6)'); ctx.fillStyle = c; ctx.fillRect(X0, 0, W, 9000);
  ctx.fillStyle = 'rgba(0,0,0,.55)'; ctx.fillRect(X0, 0, W, 60); ctx.strokeStyle = 'rgba(220,40,30,.25)'; ctx.lineWidth = 40 / CURZ; ctx.beginPath(); ctx.moveTo(X0, 0); ctx.lineTo(X0 + W, 0); ctx.stroke(); ctx.strokeStyle = '#d23a2c'; ctx.lineWidth = 5 / CURZ; ctx.stroke();
}
function drawWorld(ctx, t, sc) {
  const sp = sc.s, K = keysOf(sc), cam = camAt(t, K), hh = handheld(t, FORMAT.w / 3840 * 1.4); CURZ = cam.z;
  applyView(ctx, cam, hh); if (sp === 'board') drawCork(ctx, cam); else if (sp === 'dark') drawDark(ctx, cam); else if (sp === 'split') drawSplit(ctx, cam); else drawMap(ctx);
  const md = mapDimAt(t); if (md > 0) { ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = `rgba(4,6,7,${md})`; ctx.fillRect(0, 0, FORMAT.w, FORMAT.h); ctx.restore(); }
  const mine = OBJECTS.filter(o => (o.space || 'map') === sp && (o.t0 == null || t >= o.t0 - .05) && !(endOf(o) != null && t > endOf(o) + (o.fadeDur || .5)));
  const order = mine.filter(o => o.type === 'backdrop').concat(mine.filter(o => o.type !== 'thread' && o.type !== 'backdrop').sort((a, b) => heroLevel(a.id, t) - heroLevel(b.id, t))).concat(mine.filter(o => o.type === 'thread'));
  for (const o of order) { applyView(ctx, cam, hh); DRAW[o.type](ctx, o, t, heroLevel(o.id, t)); }
  ctx.setTransform(1, 0, 0, 1, 0, 0); return cam;
}
function screenSpeed(t, K) { const a = camAt(t, K), b = camAt(t + 1 / FORMAT.fps, K), z = (a.z + b.z) / 2; return Math.hypot((b.x - a.x) * z, (b.y - a.y) * z) + Math.abs(Math.log(b.z / a.z)) * FORMAT.w * .6; }
const bufB = document.createElement('canvas'); bufB.width = FORMAT.w; bufB.height = FORMAT.h; const b2 = bufB.getContext('2d');
function renderSpace(ctx, t, sp, f) { // tek mekân, gerekirse hareket bulanıklığıyla
  const v = screenSpeed(t, keysOf(sp)), n = v > 14 ? Math.min(6, Math.ceil(v / 14)) : 1;
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1; ctx.fillStyle = '#000'; ctx.fillRect(0, 0, FORMAT.w, FORMAT.h);
  if (n === 1) return drawWorld(ctx, t, sp);
  const tmp = mk(FORMAT.w, FORMAT.h, () => {}), tc = tmp.getContext('2d'); let cam;
  for (let k = 0; k < n; k++) { const tt = t + (k / (n - 1) - .5) * .5 / FORMAT.fps; tc.setTransform(1, 0, 0, 1, 0, 0); tc.fillStyle = '#000'; tc.fillRect(0, 0, FORMAT.w, FORMAT.h); cam = drawWorld(tc, tt, sp); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1 / (k + 1); ctx.drawImage(tmp, 0, 0); }
  ctx.globalAlpha = 1; return cam;
}
const gl = document.createElement('canvas'); gl.width = FORMAT.w; gl.height = FORMAT.h; const glc = gl.getContext('2d');
function glitchFx(f, pw) { // kanal kayması + yatay dilim kaydırma + tarama çizgileri
  const R = rng(f * 7919 + 13), W = FORMAT.w, H = FORMAT.h; glc.globalCompositeOperation = 'source-over'; glc.clearRect(0, 0, W, H); glc.drawImage(canvas, 0, 0);
  const n = 3 + Math.floor(R() * 7 * pw); for (let k = 0; k < n; k++) { const y = R() * H, h = 8 + R() * 120 * pw, dx = (R() - .5) * 160 * pw; out.drawImage(gl, 0, y, W, h, dx, y, W, h); }
  const off = 6 + 22 * pw * R(); out.globalCompositeOperation = 'lighter'; out.globalAlpha = .35 * pw; glc.globalCompositeOperation = 'multiply'; glc.fillStyle = '#ff0000'; glc.fillRect(0, 0, W, H); out.drawImage(gl, off, 0);
  glc.globalCompositeOperation = 'source-over'; glc.clearRect(0, 0, W, H); glc.drawImage(canvas, 0, 0); glc.globalCompositeOperation = 'multiply'; glc.fillStyle = '#00ffff'; glc.fillRect(0, 0, W, H); out.drawImage(gl, -off, 0);
  out.globalAlpha = 1; out.globalCompositeOperation = 'source-over'; out.fillStyle = `rgba(255,255,255,${.05 * pw})`; for (let y = 0; y < H; y += 6) out.fillRect(0, y, W, 2);
  if (R() < .35 * pw) { out.fillStyle = `rgba(255,255,255,${.12 * pw})`; out.fillRect(0, R() * H, W, 3 + R() * 10); }
}
function renderFrame(f) {
  const t = f / FORMAT.fps; let i = 0; while (i < SPC.length - 1 && t >= SPC[i + 1].t - TR / 2) i++;
  const inT = i > 0 && t < SPC[i].t + TR / 2; let cam;
  out.setTransform(1, 0, 0, 1, 0, 0); out.globalCompositeOperation = 'source-over'; out.globalAlpha = 1; out.fillStyle = '#000'; out.fillRect(0, 0, FORMAT.w, FORMAT.h);
  if (!inT) cam = renderSpace(out, t, SPC[i], f);
  else { // mekân geçişi: eskisi hafifçe yaklaşıp kararırken yenisi karanlıktan açılır
    const u = clamp((t - (SPC[i].t - TR / 2)) / TR), e = smooth(u);
    renderSpace(bctx, t, SPC[i - 1], f); cam = renderSpace(b2, t, SPC[i], f);
    const W = FORMAT.w, H = FORMAT.h, draw = (c, sc, a) => { out.globalAlpha = a; out.drawImage(c, W / 2 - W * sc / 2, H / 2 - H * sc / 2, W * sc, H * sc); };
    draw(buf, 1 + .06 * e, 1); draw(bufB, 1.05 - .05 * e, e); out.globalAlpha = 1;
    out.fillStyle = `rgba(0,0,0,${.6 * Math.sin(Math.PI * u)})`; out.fillRect(0, 0, W, H);
  }
  out.setTransform(1, 0, 0, 1, 0, 0); out.globalAlpha = 1;
  if (typeof GLITCH !== 'undefined') for (const [g0, g1, pw] of GLITCH) if (t >= g0 && t < g1) glitchFx(f, pw * (1 - .6 * (t - g0) / (g1 - g0)));
  drawDust(out, t, cam);
  gctx.filter = 'blur(12px) brightness(1.15)'; gctx.clearRect(0, 0, glowC.width, glowC.height); gctx.drawImage(canvas, 0, 0, glowC.width, glowC.height); gctx.filter = 'none';
  out.globalCompositeOperation = 'screen'; out.globalAlpha = .26; out.drawImage(glowC, 0, 0, FORMAT.w, FORMAT.h); out.globalAlpha = 1;
  out.globalCompositeOperation = 'soft-light'; out.fillStyle = 'rgba(40,95,105,.22)'; out.fillRect(0, 0, FORMAT.w, FORMAT.h); out.globalCompositeOperation = 'source-over';
  const vg = out.createRadialGradient(FORMAT.w / 2, FORMAT.h * .47, Math.min(FORMAT.w, FORMAT.h) * .32, FORMAT.w / 2, FORMAT.h / 2, Math.hypot(FORMAT.w, FORMAT.h) * .56); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.72)'); out.fillStyle = vg; out.fillRect(0, 0, FORMAT.w, FORMAT.h);
  drawTimeline(out, t);
  out.globalCompositeOperation = 'overlay'; out.globalAlpha = .11; const g = TEX.grain[f % TEX.grain.length]; out.save(); out.translate((f * 131) % 512, (f * 71) % 512); out.fillStyle = out.createPattern(g, 'repeat'); out.fillRect(-512, -512, FORMAT.w + 1024, FORMAT.h + 1024); out.restore(); out.globalAlpha = 1; out.globalCompositeOperation = 'source-over';
}
window.READY = (async () => {
  GEO = window.GEOJS; OBJ = Object.fromEntries(OBJECTS.map(o => [o.id, o]));
  makeTextures(); await loadImages();
  for (const f of [`600 80px ${MONO}`, `500 80px ${MONO}`, `80px ${TYPE}`, `500 80px ${SERIF}`, `700 80px ${COND}`]) await document.fonts.load(f);
  prepImages(); return true;
})();
window.renderFrame = renderFrame; window.TOTAL = Math.round(FORMAT.dur * FORMAT.fps);
window.grab = (q = .93) => canvas.toDataURL('image/jpeg', q);
