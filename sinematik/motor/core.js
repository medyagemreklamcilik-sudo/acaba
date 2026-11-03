// Sinematik motor: tek dünya, tek kesintisiz kamera. Her kare canvas'ta kodla çizilir.
// Sahne dosyası (sahne.js) şunları tanımlar: FORMAT {w,h,fps,dur}, WORLD, IMAGES, OBJECTS, CAMERA, BEATS.
'use strict';
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const smooth = t => { t = clamp(t); return t * t * (3 - 2 * t); };
const easeOut = t => 1 - Math.pow(1 - clamp(t), 3);
const easeInOut = t => { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
const TAU = Math.PI * 2;
function rng(seed) { let s = seed >>> 0 || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 100000) / 100000; }; }

// ---------------- kamera: zaman tabanlı Hermite (C1 sürekli, hiç ölü durma yok) ----------------
function camAt(t) {
  const K = CAMERA, n = K.length;
  if (t <= K[0].t) return { x: K[0].x, y: K[0].y, z: K[0].z, r: K[0].r || 0 };
  if (t >= K[n - 1].t) return { x: K[n - 1].x, y: K[n - 1].y, z: K[n - 1].z, r: K[n - 1].r || 0 };
  let i = 0; while (i < n - 2 && t > K[i + 1].t) i++;
  const a = K[i], b = K[i + 1], h = b.t - a.t, u = (t - a.t) / h;
  const tan = (j, key) => {
    if (j === 0 || j === n - 1) return 0;                    // ilk ve son anahtarda yumuşak giriş/çıkış
    const p = K[j - 1], q = K[j + 1], v = key === 'z' ? Math.log(q.z) - Math.log(p.z) : (q[key] || 0) - (p[key] || 0);
    return v / (q.t - p.t);
  };
  const H = (key) => {
    const p0 = key === 'z' ? Math.log(a.z) : (a[key] || 0), p1 = key === 'z' ? Math.log(b.z) : (b[key] || 0);
    const m0 = tan(i, key) * h, m1 = tan(i + 1, key) * h, u2 = u * u, u3 = u2 * u;
    return (2 * u3 - 3 * u2 + 1) * p0 + (u3 - 2 * u2 + u) * m0 + (-2 * u3 + 3 * u2) * p1 + (u3 - u2) * m1;
  };
  return { x: H('x'), y: H('y'), z: Math.exp(H('z')), r: H('r') };
}
function handheld(t, amp = 1) { // düşük frekanslı, organik el kamerası
  const s = (f, p) => Math.sin(t * f + p);
  return { x: amp * (3.2 * s(.9, 1) + 1.6 * s(2.3, 4) + .7 * s(5.1, 2)), y: amp * (2.4 * s(1.1, 3) + 1.3 * s(2.9, .5) + .6 * s(4.7, 1)), r: amp * .0011 * (s(.7, 2) + .6 * s(1.9, 5)) };
}
function applyView(ctx, cam, hh) {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.translate(FORMAT.w / 2 + hh.x, FORMAT.h / 2 + hh.y); ctx.rotate((cam.r || 0) + hh.r); ctx.scale(cam.z, cam.z); ctx.translate(-cam.x, -cam.y);
}

// ---------------- dünya: projeksiyon ----------------
function proj(lon, lat) { const W_ = WORLD; return [(lon - W_.lon0) * W_.k * Math.cos(W_.latc * Math.PI / 180), (W_.lat0 - lat) * W_.k]; }

// ---------------- dokular (bir kez üretilir) ----------------
const TEX = {};
function makeTextures() {
  const mk = (w, h, f) => { const c = document.createElement('canvas'); c.width = w; c.height = h; f(c.getContext('2d'), w, h); return c; };
  TEX.paper = mk(1024, 1024, (g, w, h) => {
    g.fillStyle = '#e8d9b5'; g.fillRect(0, 0, w, h); const R = rng(7);
    const id = g.getImageData(0, 0, w, h); for (let i = 0; i < id.data.length; i += 4) { const v = (R() - .5) * 18; id.data[i] += v; id.data[i + 1] += v; id.data[i + 2] += v * .8; } g.putImageData(id, 0, 0);
    g.globalAlpha = .07; for (let k = 0; k < 900; k++) { g.strokeStyle = R() > .5 ? '#7a6040' : '#fff6dd'; g.lineWidth = .6 + R(); g.beginPath(); const x = R() * w, y = R() * h, a = R() * TAU, l = 8 + R() * 30; g.moveTo(x, y); g.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke(); }
    g.globalAlpha = .05; for (let k = 0; k < 40; k++) { const x = R() * w, y = R() * h, r = 40 + R() * 160; const gr = g.createRadialGradient(x, y, 0, x, y, r); gr.addColorStop(0, '#8a6a3a'); gr.addColorStop(1, 'rgba(138,106,58,0)'); g.fillStyle = gr; g.fillRect(x - r, y - r, r * 2, r * 2); }
  });
  TEX.wood = mk(2048, 1024, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, '#2a1a10'); gr.addColorStop(1, '#1c110a'); g.fillStyle = gr; g.fillRect(0, 0, w, h); const R = rng(3);
    for (let k = 0; k < 260; k++) { const y = R() * h, a = .04 + R() * .08; g.strokeStyle = `rgba(${R() > .5 ? '90,60,35' : '10,6,3'},${a})`; g.lineWidth = 1 + R() * 4; g.beginPath(); g.moveTo(0, y); for (let x = 0; x <= w; x += 64) g.lineTo(x, y + Math.sin(x * .004 + k) * 10 + Math.sin(x * .013 + k * 2) * 4); g.stroke(); }
  });
  TEX.grain = []; for (let k = 0; k < 6; k++) TEX.grain.push(mk(512, 512, (g, w, h) => { const id = g.createImageData(w, h), R = rng(k + 21); for (let i = 0; i < id.data.length; i += 4) { const v = 128 + (R() - .5) * 150; id.data[i] = id.data[i + 1] = id.data[i + 2] = v; id.data[i + 3] = 255; } g.putImageData(id, 0, 0); }));
}

// ---------------- vuruş (beat) yönetimi: tek kahraman, gerisi geri çekilir ----------------
function beatAt(t) { let b = BEATS[0]; for (const x of BEATS) if (t >= x.t) b = x; return b; }
function heroLevel(id, t) { // 1 = kahraman/normal, 0 = tamamen geri çekilmiş
  const FADE = .45; let lv = 1;
  for (let i = 0; i < BEATS.length; i++) {
    const b = BEATS[i], n = BEATS[i + 1], on = !b.hero || b.hero.includes(id) || (b.keep || []).includes(id) ? 1 : 0;
    if (t >= b.t && (!n || t < n.t)) {
      const prev = i > 0 ? (!BEATS[i - 1].hero || BEATS[i - 1].hero.includes(id) || (BEATS[i - 1].keep || []).includes(id) ? 1 : 0) : on;
      lv = lerp(prev, on, smooth((t - b.t) / FADE));
    }
  }
  return lv;
}
function mapDimAt(t) { const FADE = .5; for (let i = BEATS.length - 1; i >= 0; i--) if (t >= BEATS[i].t) { const p = i > 0 ? (BEATS[i - 1].mapDim || 0) : (BEATS[i].mapDim || 0); return lerp(p, BEATS[i].mapDim || 0, smooth((t - BEATS[i].t) / FADE)); } return 0; }

// ---------------- çizim parçaları ----------------
const IMG = {};
function loadImages() { return Promise.all(Object.entries(IMAGES).map(([k, src]) => new Promise(r => { const i = new Image(); i.onload = i.onerror = () => r(); i.src = src; IMG[k] = i; }))); }
let GEO = null, CURZ = 1;
function polyPath(ctx, pts) { ctx.beginPath(); pts.forEach(([lo, la], i) => { const [x, y] = proj(lo, la); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }); }
function drawDesk(ctx) { ctx.save(); const p = ctx.createPattern(TEX.wood, 'repeat'); ctx.fillStyle = p; ctx.fillRect(-20000, -20000, 50000, 50000); ctx.restore(); }
function drawMap(ctx, t, z) {
  const M = WORLD.map, [x0, y0] = [M.x, M.y], w = M.w, h = M.h;
  ctx.save();
  // kâğıdın masaya düşen gölgesi
  ctx.shadowColor = 'rgba(0,0,0,.6)'; ctx.shadowBlur = 140; ctx.shadowOffsetY = 40; ctx.fillStyle = '#e3d2ab'; ctx.fillRect(x0, y0, w, h); ctx.shadowColor = 'transparent';
  ctx.beginPath(); ctx.rect(x0, y0, w, h); ctx.clip();
  const pat = ctx.createPattern(TEX.paper, 'repeat'); ctx.fillStyle = pat; ctx.fillRect(x0, y0, w, h);
  // deniz tonu
  ctx.fillStyle = 'rgba(96,124,132,.34)'; ctx.fillRect(x0, y0, w, h);
  // kıyı halkaları (eski harita dalga çizgileri)
  for (const [lw, a] of [[90, .05], [50, .07], [22, .1]]) { ctx.lineWidth = lw; ctx.strokeStyle = `rgba(70,80,70,${a})`; for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.stroke(); } }
  // kara
  for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.fillStyle = pat; ctx.fill(); ctx.fillStyle = 'rgba(236,214,166,.42)'; ctx.fill(); }
  for (const p of GEO.lakes) { polyPath(ctx, p); ctx.closePath(); ctx.fillStyle = 'rgba(120,140,140,.25)'; ctx.fill(); }
  // ızgara
  ctx.lineWidth = 3; ctx.strokeStyle = 'rgba(90,70,40,.12)';
  for (let lo = Math.ceil(WORLD.lonMin / 2) * 2; lo <= WORLD.lonMax; lo += 2) { polyPath(ctx, [[lo, WORLD.latMax], [lo, WORLD.latMin]]); ctx.stroke(); }
  for (let la = Math.ceil(WORLD.latMin / 2) * 2; la <= WORLD.latMax; la += 2) { polyPath(ctx, [[WORLD.lonMin, la], [WORLD.lonMax, la]]); ctx.stroke(); }
  // kıyı çizgisi
  ctx.lineJoin = 'round'; ctx.lineWidth = 5; ctx.strokeStyle = 'rgba(70,50,30,.85)'; for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.stroke(); }
  // nehirler
  ctx.lineCap = 'round'; for (const r of GEO.rivers) { polyPath(ctx, r.p); ctx.lineWidth = r.n === 'Danube' || r.n === 'Donau' ? 9 : 5; ctx.strokeStyle = 'rgba(60,90,110,.55)'; ctx.stroke(); }
  // yanık kenar
  const v = ctx.createRadialGradient(x0 + w / 2, y0 + h / 2, Math.min(w, h) * .35, x0 + w / 2, y0 + h / 2, Math.max(w, h) * .72); v.addColorStop(0, 'rgba(90,55,20,0)'); v.addColorStop(1, 'rgba(90,55,20,.55)'); ctx.fillStyle = v; ctx.fillRect(x0, y0, w, h);
  ctx.restore();
  // çift çerçeve
  ctx.save(); ctx.strokeStyle = 'rgba(70,45,25,.7)'; ctx.lineWidth = 10; ctx.strokeRect(x0 + 60, y0 + 60, w - 120, h - 120); ctx.lineWidth = 3; ctx.strokeRect(x0 + 90, y0 + 90, w - 180, h - 180); ctx.restore();
}
function cityDot(ctx, o, t, lv) { const [x, y] = proj(o.lon, o.lat), a = smooth((t - (o.t0 || -9)) / .4) * lv; if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.arc(x, y, o.r || 26, 0, TAU); ctx.fillStyle = '#5a1810'; ctx.fill(); ctx.lineWidth = 8; ctx.strokeStyle = '#f2e6c8'; ctx.stroke(); ctx.restore(); }
function routeDraw(ctx, o, t, lv) {
  const u = clamp((t - o.t0) / (o.t1 - o.t0)); if (u <= 0) return;
  const P = o.pts.map(([lo, la]) => proj(lo, la)); const L = []; let tot = 0; for (let i = 1; i < P.length; i++) { const d = Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]); L.push(d); tot += d; }
  let rem = easeInOut(u) * tot;
  ctx.save(); ctx.globalAlpha = .22 + .78 * lv; ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.strokeStyle = o.color || '#9a1c14'; ctx.lineWidth = Math.max(o.width || 22, 7 / CURZ); if (o.dash) ctx.setLineDash(o.dash);
  ctx.shadowColor = 'rgba(60,10,5,.35)'; ctx.shadowBlur = 10;
  ctx.beginPath(); ctx.moveTo(...P[0]); let tip = P[0];
  for (let i = 1; i < P.length && rem > 0; i++) { const k = Math.min(1, rem / L[i - 1]); tip = [lerp(P[i - 1][0], P[i][0], k), lerp(P[i - 1][1], P[i][1], k)]; ctx.lineTo(...tip); rem -= L[i - 1]; }
  ctx.stroke(); ctx.setLineDash([]);
  if (u < 1) { ctx.beginPath(); ctx.arc(tip[0], tip[1], (o.width || 22) * .9, 0, TAU); ctx.fillStyle = o.color || '#9a1c14'; ctx.fill(); }
  ctx.restore();
}
function inkLabel(ctx, o, t, lv) { // haritaya mürekkeple yazılan büyük etiket (soldan sağa açılır)
  const u = clamp((t - o.t0) / (o.dur || .55)); if (u <= 0) return;
  const [x, y] = o.lon != null ? proj(o.lon, o.lat) : [o.x, o.y];
  ctx.save(); ctx.globalAlpha = .16 + .84 * lv; ctx.font = `700 ${o.size}px Cinzel`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic';
  const tw = ctx.measureText(o.text).width, lx = (o.align === 'center' ? x - tw / 2 : o.align === 'right' ? x - tw : x) + (o.dx || 0), ly = y + (o.dy || 0);
  ctx.beginPath(); ctx.rect(lx - 40, ly - o.size * 1.3, (tw + 80) * easeOut(u), o.size * 2.6 + (o.subSize || 0) * 1.6); ctx.clip();
  ctx.lineJoin = 'round'; ctx.lineWidth = o.size * .14; ctx.strokeStyle = 'rgba(242,230,200,.85)'; ctx.strokeText(o.text, lx + (o.align === 'center' ? tw / 2 : o.align === 'right' ? tw : 0), ly);
  ctx.fillStyle = o.color || '#3a1a0c'; ctx.fillText(o.text, lx + (o.align === 'center' ? tw / 2 : o.align === 'right' ? tw : 0), ly);
  if (o.sub) { const su = clamp((t - (o.subT || o.t0 + .3)) / .45); if (su > 0) { ctx.globalAlpha *= easeOut(su); ctx.font = `italic 600 ${o.subSize}px "Playfair Display"`; ctx.lineWidth = o.subSize * .14; ctx.strokeText(o.sub, lx + (o.align === 'center' ? tw / 2 : o.align === 'right' ? tw : 0), ly + o.subSize * 1.15); ctx.fillStyle = o.subColor || '#9a1c14'; ctx.fillText(o.sub, lx + (o.align === 'center' ? tw / 2 : o.align === 'right' ? tw : 0), ly + o.subSize * 1.15); } }
  ctx.restore();
}
function penCircle(ctx, o, t, lv) { // kelime söylenirken elle çizilen daire
  const u = clamp((t - o.t0) / (o.dur || .5)); if (u <= 0) return; const [x, y] = o.lon != null ? proj(o.lon, o.lat) : [o.x, o.y];
  ctx.save(); ctx.globalAlpha = .35 + .65 * lv; ctx.lineCap = 'round'; ctx.strokeStyle = o.color || '#b3140c'; ctx.lineWidth = o.width || 18; ctx.beginPath();
  const a0 = -2.2, span = TAU * 1.08 * easeInOut(u); for (let k = 0; k <= 80; k++) { const a = a0 + span * k / 80, w = 1 + .04 * Math.sin(a * 3 + 1); const px = x + Math.cos(a) * o.rx * w, py = y + Math.sin(a) * o.ry * w * (1 + .05 * k / 80); k ? ctx.lineTo(px, py) : ctx.moveTo(px, py); }
  ctx.stroke(); ctx.restore();
}
function printObj(ctx, o, t, lv) { // fiziksel baskı: düşer, gölgesi oturur, hafif döner
  const im = IMG[o.img]; if (!im || !im.naturalWidth) return; const u = clamp((t - o.t0) / (o.dur || .7)); if (u <= 0) return;
  const e = easeOut(u), sc = lerp(1.18, 1, e), lift = 1 - e, bw = o.w * .04, h = o.w * im.naturalHeight / im.naturalWidth;
  ctx.save(); ctx.translate(o.x, o.y); ctx.rotate((o.rot || 0) + lift * .05); ctx.scale(sc, sc); ctx.globalAlpha = clamp(u * 4);
  ctx.shadowColor = `rgba(0,0,0,${.55 - .25 * lift})`; ctx.shadowBlur = 40 + 160 * lift; ctx.shadowOffsetX = 18 + 60 * lift; ctx.shadowOffsetY = 26 + 90 * lift;
  const W2 = o.w + bw * 2, H2 = h + bw * 2 + (o.caption ? bw * 2.6 : 0);
  ctx.fillStyle = '#f3ecdc'; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2); ctx.shadowColor = 'transparent';
  ctx.drawImage(im, -o.w / 2, -H2 / 2 + bw, o.w, h);
  if (o.tone) { ctx.fillStyle = o.tone; ctx.fillRect(-o.w / 2, -H2 / 2 + bw, o.w, h); }
  if (o.fx) o.fx(ctx, t, -o.w / 2, -H2 / 2 + bw, o.w, h);
  if (o.caption) { ctx.font = `600 ${bw * 1.7}px Caveat`; ctx.fillStyle = '#2a1a10'; ctx.textAlign = 'center'; ctx.fillText(o.caption, 0, H2 / 2 - bw * .9); }
  const pg = ctx.createLinearGradient(-W2 / 2, -H2 / 2, W2 / 2, H2 / 2); pg.addColorStop(0, 'rgba(255,255,255,.08)'); pg.addColorStop(.5, 'rgba(255,255,255,0)'); pg.addColorStop(1, 'rgba(0,0,0,.08)'); ctx.fillStyle = pg; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2);
  if (lv < 1) { ctx.fillStyle = `rgba(10,6,4,${.55 * (1 - lv)})`; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2); }
  ctx.restore();
}
const DRAW = { city: cityDot, route: routeDraw, label: inkLabel, circle: penCircle, print: printObj };

// ---------------- kare ----------------
const canvas = document.getElementById('c'); canvas.width = FORMAT.w; canvas.height = FORMAT.h; const out = canvas.getContext('2d');
const buf = document.createElement('canvas'); buf.width = FORMAT.w; buf.height = FORMAT.h; const bctx = buf.getContext('2d');
const glowC = document.createElement('canvas'); glowC.width = FORMAT.w / 4; glowC.height = FORMAT.h / 4; const gctx = glowC.getContext('2d');
function drawWorld(ctx, t) {
  const cam = camAt(t), hh = handheld(t, FORMAT.w / 3840); CURZ = cam.z;
  applyView(ctx, cam, hh); drawDesk(ctx); drawMap(ctx, t, cam.z);
  const md = mapDimAt(t); if (md > 0) { ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = `rgba(12,8,5,${md})`; ctx.fillRect(0, 0, FORMAT.w, FORMAT.h); ctx.restore(); applyView(ctx, cam, hh); }
  const order = OBJECTS.slice().sort((a, b) => heroLevel(a.id, t) - heroLevel(b.id, t));
  for (const o of order) { applyView(ctx, cam, hh); DRAW[o.type](ctx, o, t, heroLevel(o.id, t)); }
  if (typeof OVERLAY === 'function') { ctx.setTransform(1, 0, 0, 1, 0, 0); OVERLAY(ctx, t, cam); }
}
function screenSpeed(t) { const a = camAt(t), b = camAt(t + 1 / FORMAT.fps), z = (a.z + b.z) / 2; return Math.hypot((b.x - a.x) * z, (b.y - a.y) * z) + Math.abs(Math.log(b.z / a.z)) * FORMAT.w * .6; }
function renderFrame(f) {
  const t = f / FORMAT.fps, sp = screenSpeed(t), n = sp > 14 ? Math.min(7, Math.ceil(sp / 14)) : 1;
  out.setTransform(1, 0, 0, 1, 0, 0); out.globalCompositeOperation = 'source-over'; out.globalAlpha = 1; out.fillStyle = '#000'; out.fillRect(0, 0, FORMAT.w, FORMAT.h);
  if (n === 1) { drawWorld(out, t); }
  else { // hareket bulanıklığı: 180° obtüratör, alt kareler toplanır
    for (let k = 0; k < n; k++) { const tt = t + (k / (n - 1) - .5) * .5 / FORMAT.fps; bctx.setTransform(1, 0, 0, 1, 0, 0); bctx.fillStyle = '#000'; bctx.fillRect(0, 0, FORMAT.w, FORMAT.h); drawWorld(bctx, tt); out.setTransform(1, 0, 0, 1, 0, 0); out.globalAlpha = 1 / (k + 1); out.drawImage(buf, 0, 0); }
    out.globalAlpha = 1;
  }
  // yumuşak ışıma
  out.setTransform(1, 0, 0, 1, 0, 0); gctx.filter = 'blur(10px) brightness(1.1)'; gctx.clearRect(0, 0, glowC.width, glowC.height); gctx.drawImage(canvas, 0, 0, glowC.width, glowC.height); gctx.filter = 'none';
  out.globalCompositeOperation = 'screen'; out.globalAlpha = .22; out.drawImage(glowC, 0, 0, FORMAT.w, FORMAT.h); out.globalAlpha = 1; out.globalCompositeOperation = 'source-over';
  // sıcak renk + vinyet
  out.fillStyle = 'rgba(255,170,90,.05)'; out.globalCompositeOperation = 'soft-light'; out.fillRect(0, 0, FORMAT.w, FORMAT.h); out.globalCompositeOperation = 'source-over';
  const vg = out.createRadialGradient(FORMAT.w / 2, FORMAT.h / 2, FORMAT.h * .45, FORMAT.w / 2, FORMAT.h / 2, FORMAT.w * .62); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.55)'); out.fillStyle = vg; out.fillRect(0, 0, FORMAT.w, FORMAT.h);
  // film greni
  out.globalCompositeOperation = 'overlay'; out.globalAlpha = .09; const g = TEX.grain[f % TEX.grain.length]; out.save(); out.translate((f * 131) % 512, (f * 71) % 512); out.fillStyle = out.createPattern(g, 'repeat'); out.fillRect(-512, -512, FORMAT.w + 1024, FORMAT.h + 1024); out.restore(); out.globalAlpha = 1; out.globalCompositeOperation = 'source-over';
}
window.READY = (async () => {
  GEO = window.GEOJS;
  makeTextures(); await loadImages();
  for (const f of ['700 80px Cinzel', 'italic 600 80px "Playfair Display"', '600 80px Caveat']) await document.fonts.load(f);
  return true;
})();
window.renderFrame = renderFrame; window.TOTAL = Math.round(FORMAT.dur * FORMAT.fps);
window.grab = (q = .93) => canvas.toDataURL('image/jpeg', q);
