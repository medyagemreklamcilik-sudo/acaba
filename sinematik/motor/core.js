// Sinematik motor v2 · tek dünya, tek kesintisiz kamera, her kare kodla.
// Akış: (1) 2D "düz dünya" tuvali (masa, kabartmalı harita, baskılar, gazeteler, rotalar)
//       (2) WebGL lens: eğik kamera (perspektif), alan derinliği, hareket bulanıklığı, ışık havuzu, parlama, vinyet, gren
//       (3) ekran katmanı: dikilen objeler (bayrak, iğne) ve ekran yazıları
// Sahne dosyası tanımlar: FORMAT {w,h,fps,dur}, WORLD, IMAGES, OBJECTS, CAMERA [{t,x,y,z,tilt,r}], BEATS, LOOK (isteğe bağlı)
'use strict';
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const smooth = t => { t = clamp(t); return t * t * (3 - 2 * t); };
const easeOut = t => 1 - Math.pow(1 - clamp(t), 3);
const easeInOut = t => { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
const backOut = t => { t = clamp(t); const c = 1.7; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); };
const TAU = Math.PI * 2;
function rng(seed) { let s = seed >>> 0 || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 100000) / 100000; }; }
const L = Object.assign({ tilt: 38, fov: 55, dof: 1.0, focusY: .56, light: [.25, .18], lightPower: .55, bloom: .35, grain: .07, vignette: .6, warm: .08, mblur: 1, handheld: 1 }, typeof LOOK === 'object' ? LOOK : {});

// ---------------- kamera: zaman tabanlı Hermite (C1 sürekli) ----------------
function camAt(t) {
  const K = CAMERA, n = K.length, g = (k, key, d) => k[key] == null ? d : k[key];
  const keys = ['x', 'y', 'z', 'tilt', 'r'], def = { tilt: L.tilt, r: 0 };
  if (t <= K[0].t || t >= K[n - 1].t) { const k = t <= K[0].t ? K[0] : K[n - 1]; return { x: k.x, y: k.y, z: k.z, tilt: g(k, 'tilt', L.tilt), r: g(k, 'r', 0) }; }
  let i = 0; while (i < n - 2 && t > K[i + 1].t) i++;
  const a = K[i], b = K[i + 1], h = b.t - a.t, u = (t - a.t) / h, o = {};
  for (const key of keys) {
    const val = k => key === 'z' ? Math.log(k.z) : g(k, key, def[key]);
    const tan = j => (j === 0 || j === n - 1) ? 0 : (val(K[j + 1]) - val(K[j - 1])) / (K[j + 1].t - K[j - 1].t);
    const p0 = val(a), p1 = val(b), m0 = tan(i) * h, m1 = tan(i + 1) * h, u2 = u * u, u3 = u2 * u;
    const v = (2 * u3 - 3 * u2 + 1) * p0 + (u3 - 2 * u2 + u) * m0 + (-2 * u3 + 3 * u2) * p1 + (u3 - u2) * m1;
    o[key] = key === 'z' ? Math.exp(v) : v;
  }
  return o;
}
function handheld(t) { const a = L.handheld, s = (f, p) => Math.sin(t * f + p); return { x: a * (2.6 * s(.9, 1) + 1.3 * s(2.3, 4) + .5 * s(5.1, 2)), y: a * (2.0 * s(1.1, 3) + 1.1 * s(2.9, .5) + .5 * s(4.7, 1)), r: a * .0009 * (s(.7, 2) + .6 * s(1.9, 5)) }; }

// ---------------- perspektif eşleme (JS ve GLSL aynı formül) ----------------
const W = FORMAT.w, H = FORMAT.h, FOC = (H / 2) / Math.tan(L.fov * Math.PI / 360);
function scr2plane(px, py, tiltDeg) { // ekran (merkez orijin, y aşağı) → düz tuval pikseli (merkez orijin, y aşağı) + derinlik s
  const a = tiltDeg * Math.PI / 180, x = px, y = -py, hh = FOC * Math.cos(a), s = hh / (FOC * Math.cos(a) - y * Math.sin(a));
  const X = s * x, Y = -hh * Math.tan(a) + s * (y * Math.cos(a) + FOC * Math.sin(a)); return [X, -Y, s];
}
function plane2scr(X, Yd, tiltDeg) { // düz tuval (merkez orijin) → ekran; ölçek = 1/s
  const a = tiltDeg * Math.PI / 180, hh = FOC * Math.cos(a), T = -Yd + hh * Math.tan(a), y = FOC * (T * Math.cos(a) - hh * Math.sin(a)) / (hh * Math.cos(a) + T * Math.sin(a)), s = hh / (FOC * Math.cos(a) - y * Math.sin(a));
  return [X / s, -y, 1 / s];
}
// düz tuval boyutu: en büyük eğimde ekranın köşelerini kapsasın
const MAXT = Math.max(...CAMERA.map(k => k.tilt == null ? L.tilt : k.tilt));
const CORN = [[-W / 2, -H / 2], [W / 2, -H / 2], [-W / 2, H / 2], [W / 2, H / 2]].map(([x, y]) => scr2plane(x, y, MAXT));
const FW = Math.ceil(Math.max(...CORN.map(c => Math.abs(c[0]))) * 2 + 80), FTOP = Math.ceil(-Math.min(...CORN.map(c => c[1])) + 40), FBOT = Math.ceil(Math.max(...CORN.map(c => c[1])) + 40);
const FH = FTOP + FBOT, FCX = FW / 2, FCY = FTOP; // düz tuvalde kamera merkezi

// ---------------- dünya ----------------
function proj(lon, lat) { const w = WORLD; return [(lon - w.lon0) * w.k * Math.cos(w.latc * Math.PI / 180), (w.lat0 - lat) * w.k]; }
const TEX = {}, IMG = {}; let GEO = null, CURZ = 1, CURT = 0;
function makeTextures() {
  const mk = (w, h, f) => { const c = document.createElement('canvas'); c.width = w; c.height = h; f(c.getContext('2d'), w, h); return c; };
  TEX.paper = mk(1024, 1024, (g, w, h) => {
    g.fillStyle = '#e3d0a4'; g.fillRect(0, 0, w, h); const R = rng(7);
    const id = g.getImageData(0, 0, w, h); for (let i = 0; i < id.data.length; i += 4) { const v = (R() - .5) * 20; id.data[i] += v; id.data[i + 1] += v; id.data[i + 2] += v * .8; } g.putImageData(id, 0, 0);
    g.globalAlpha = .07; for (let k = 0; k < 900; k++) { g.strokeStyle = R() > .5 ? '#6a5030' : '#fff3d6'; g.lineWidth = .6 + R(); g.beginPath(); const x = R() * w, y = R() * h, an = R() * TAU, l = 8 + R() * 30; g.moveTo(x, y); g.lineTo(x + Math.cos(an) * l, y + Math.sin(an) * l); g.stroke(); }
    g.globalAlpha = .06; for (let k = 0; k < 50; k++) { const x = R() * w, y = R() * h, r = 40 + R() * 180, gr = g.createRadialGradient(x, y, 0, x, y, r); gr.addColorStop(0, '#7a5a2a'); gr.addColorStop(1, 'rgba(122,90,42,0)'); g.fillStyle = gr; g.fillRect(x - r, y - r, r * 2, r * 2); }
  });
  TEX.news = mk(512, 512, (g, w, h) => { g.fillStyle = '#e9dfc6'; g.fillRect(0, 0, w, h); const R = rng(11); const id = g.getImageData(0, 0, w, h); for (let i = 0; i < id.data.length; i += 4) { const v = (R() - .5) * 16; id.data[i] += v; id.data[i + 1] += v; id.data[i + 2] += v; } g.putImageData(id, 0, 0); });
  TEX.wood = mk(2048, 1024, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, '#3a2414'); gr.addColorStop(1, '#24150b'); g.fillStyle = gr; g.fillRect(0, 0, w, h); const R = rng(3);
    for (let k = 0; k < 300; k++) { const y = R() * h, al = .05 + R() * .09; g.strokeStyle = `rgba(${R() > .5 ? '110,70,38' : '12,7,3'},${al})`; g.lineWidth = 1 + R() * 5; g.beginPath(); g.moveTo(0, y); for (let x = 0; x <= w; x += 64) g.lineTo(x, y + Math.sin(x * .004 + k) * 12 + Math.sin(x * .013 + k * 2) * 4); g.stroke(); }
  });
}
function polyPath(ctx, pts) { ctx.beginPath(); pts.forEach(([lo, la], i) => { const [x, y] = proj(lo, la); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }); }
function drawDesk(ctx) { ctx.save(); ctx.fillStyle = ctx.createPattern(TEX.wood, 'repeat'); ctx.fillRect(-30000, -30000, 70000, 70000); ctx.restore(); }
function drawMap(ctx) {
  const M = WORLD.map, x0 = M.x, y0 = M.y, w = M.w, h = M.h, pat = ctx.createPattern(TEX.paper, 'repeat');
  ctx.save();
  ctx.shadowColor = 'rgba(0,0,0,.7)'; ctx.shadowBlur = 160; ctx.shadowOffsetY = 50; ctx.fillStyle = '#d8c497'; ctx.fillRect(x0, y0, w, h); ctx.shadowColor = 'transparent';
  ctx.beginPath(); ctx.rect(x0, y0, w, h); ctx.clip();
  ctx.fillStyle = pat; ctx.fillRect(x0, y0, w, h);
  ctx.fillStyle = 'rgba(70,96,104,.42)'; ctx.fillRect(x0, y0, w, h);                         // deniz
  for (const [lw, al] of [[110, .05], [60, .07], [26, .1]]) { ctx.lineWidth = lw; ctx.strokeStyle = `rgba(40,55,50,${al})`; for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.stroke(); } }
  ctx.save(); ctx.beginPath(); for (const p of GEO.land) { p.forEach(([lo, la], i) => { const [x, y] = proj(lo, la); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }); ctx.closePath(); } ctx.clip();
  ctx.fillStyle = pat; ctx.fillRect(x0, y0, w, h); ctx.fillStyle = 'rgba(226,198,140,.35)'; ctx.fillRect(x0, y0, w, h);
  if (IMG.__relief && IMG.__relief.naturalWidth) { const R = RELIEF, [ax, ay] = proj(R.lon0, R.lat1), [bx, by] = proj(R.lon1, R.lat0); ctx.globalCompositeOperation = 'multiply'; ctx.globalAlpha = L.relief == null ? .85 : L.relief; ctx.drawImage(IMG.__relief, ax, ay, bx - ax, by - ay); ctx.globalCompositeOperation = 'overlay'; ctx.globalAlpha = .35; ctx.drawImage(IMG.__relief, ax, ay, bx - ax, by - ay); ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over'; }
  ctx.restore();
  for (const p of GEO.lakes) { polyPath(ctx, p); ctx.closePath(); ctx.fillStyle = 'rgba(70,96,104,.5)'; ctx.fill(); }
  ctx.lineWidth = 3; ctx.strokeStyle = 'rgba(80,60,30,.13)';
  for (let lo = Math.ceil(WORLD.lonMin / 2) * 2; lo <= WORLD.lonMax; lo += 2) { polyPath(ctx, [[lo, WORLD.latMax], [lo, WORLD.latMin]]); ctx.stroke(); }
  for (let la = Math.ceil(WORLD.latMin / 2) * 2; la <= WORLD.latMax; la += 2) { polyPath(ctx, [[WORLD.lonMin, la], [WORLD.lonMax, la]]); ctx.stroke(); }
  ctx.lineJoin = 'round'; ctx.lineWidth = 5; ctx.strokeStyle = 'rgba(55,38,20,.85)'; for (const p of GEO.land) { polyPath(ctx, p); ctx.closePath(); ctx.stroke(); }
  ctx.lineCap = 'round'; for (const r of GEO.rivers) { polyPath(ctx, r.p); ctx.lineWidth = r.r <= 2 ? 9 : 5; ctx.strokeStyle = 'rgba(50,80,96,.55)'; ctx.stroke(); }
  const v = ctx.createRadialGradient(x0 + w / 2, y0 + h / 2, Math.min(w, h) * .35, x0 + w / 2, y0 + h / 2, Math.max(w, h) * .72); v.addColorStop(0, 'rgba(80,45,15,0)'); v.addColorStop(1, 'rgba(80,45,15,.6)'); ctx.fillStyle = v; ctx.fillRect(x0, y0, w, h);
  ctx.restore();
  ctx.save(); ctx.strokeStyle = 'rgba(60,38,20,.7)'; ctx.lineWidth = 10; ctx.strokeRect(x0 + 60, y0 + 60, w - 120, h - 120); ctx.lineWidth = 3; ctx.strokeRect(x0 + 90, y0 + 90, w - 180, h - 180); ctx.restore();
}

// ---------------- vuruşlar: tek kahraman ----------------
function inHero(b, id) { return !b.hero || b.hero.includes(id) || (b.keep || []).includes(id) ? 1 : 0; }
function heroLevel(id, t) { const F = .45; for (let i = BEATS.length - 1; i >= 0; i--) if (t >= BEATS[i].t) { const p = i > 0 ? inHero(BEATS[i - 1], id) : inHero(BEATS[i], id); return lerp(p, inHero(BEATS[i], id), smooth((t - BEATS[i].t) / F)); } return 1; }
function mapDimAt(t) { const F = .5; for (let i = BEATS.length - 1; i >= 0; i--) if (t >= BEATS[i].t) { const p = i > 0 ? (BEATS[i - 1].mapDim || 0) : (BEATS[i].mapDim || 0); return lerp(p, BEATS[i].mapDim || 0, smooth((t - BEATS[i].t) / F)); } return 0; }
const fadeOut = (lv, t) => (1 - lv) * clamp((mapDimAt(t) - .12) / .48); // kahraman anında geri çekilenleri iyice söndür

// ---------------- düz dünya objeleri ----------------
function cityDot(ctx, o, t, lv) { const [x, y] = proj(o.lon, o.lat), a = smooth((t - (o.t0 ?? -9)) / .4) * (.25 + .75 * lv); if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.arc(x, y, o.r || 26, 0, TAU); ctx.fillStyle = '#5a1810'; ctx.fill(); ctx.lineWidth = 8; ctx.strokeStyle = '#f2e6c8'; ctx.stroke(); ctx.restore(); }
function routePts(o) { const P = o.pts.map(([lo, la]) => proj(lo, la)); if (!o.curve) return P; const out = []; for (let i = 0; i < P.length - 1; i++) { const p0 = P[Math.max(0, i - 1)], p1 = P[i], p2 = P[i + 1], p3 = P[Math.min(P.length - 1, i + 2)]; for (let k = 0; k < 12; k++) { const u = k / 12, u2 = u * u, u3 = u2 * u; out.push([.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * u + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * u2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * u3), .5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * u + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * u2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * u3)]); } } out.push(P[P.length - 1]); return out; }
function routeDraw(ctx, o, t, lv) {
  const u = clamp((t - o.t0) / (o.t1 - o.t0)); if (u <= 0) return;
  const P = o._P || (o._P = routePts(o)); let tot = 0; const Ls = []; for (let i = 1; i < P.length; i++) { const d = Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]); Ls.push(d); tot += d; }
  let rem = easeInOut(u) * tot; const path = [P[0]];
  for (let i = 1; i < P.length && rem > 0; i++) { const k = Math.min(1, rem / Ls[i - 1]); path.push([lerp(P[i - 1][0], P[i][0], k), lerp(P[i - 1][1], P[i][1], k)]); rem -= Ls[i - 1]; }
  const tip = path[path.length - 1], al = (.22 + .78 * lv) * (1 - .75 * fadeOut(lv, t));
  ctx.save(); ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  const line = () => { ctx.beginPath(); ctx.moveTo(...path[0]); for (const p of path) ctx.lineTo(...p); ctx.stroke(); };
  if (o.glow) { ctx.globalAlpha = al * .9; ctx.shadowColor = o.glow; ctx.shadowBlur = 60; ctx.strokeStyle = o.glow; ctx.lineWidth = Math.max((o.width || 22) * 1.6, 9 / CURZ); line(); ctx.shadowBlur = 0; ctx.strokeStyle = '#fff6d8'; ctx.lineWidth = Math.max((o.width || 22) * .45, 3 / CURZ); line(); }
  else { ctx.globalAlpha = al; if (o.dash) ctx.setLineDash(o.dash.map(d => d * Math.max(1, 1 / (CURZ * 2.2)))); ctx.strokeStyle = o.color || '#9a1c14'; ctx.lineWidth = Math.max(o.width || 22, 7 / CURZ); ctx.shadowColor = 'rgba(60,10,5,.35)'; ctx.shadowBlur = 10; line(); ctx.setLineDash([]); }
  if (u < 1) { ctx.globalAlpha = al; ctx.beginPath(); ctx.arc(tip[0], tip[1], Math.max(o.width || 22, 7 / CURZ) * 1.1, 0, TAU); ctx.fillStyle = o.glow ? '#fff6d8' : (o.color || '#9a1c14'); if (o.glow) { ctx.shadowColor = o.glow; ctx.shadowBlur = 80; } ctx.fill(); }
  ctx.restore();
}
function region(ctx, o, t, lv) { // parlayan bölge sınırı (ref: Persia haritası, kırmızı Türkiye sınırı)
  const u = clamp((t - o.t0) / (o.dur || 1.2)); if (u <= 0) return; const al = (.25 + .75 * lv) * (1 - .8 * fadeOut(lv, t));
  ctx.save(); polyPath(ctx, o.pts); ctx.closePath();
  ctx.globalAlpha = al * easeOut(u) * (o.fillA ?? .18); ctx.fillStyle = o.fill || '#c4561c'; ctx.fill();
  let len = 0; for (let i = 1; i < o.pts.length; i++) { const a = proj(...o.pts[i - 1]), b = proj(...o.pts[i]); len += Math.hypot(b[0] - a[0], b[1] - a[1]); }
  ctx.setLineDash([len, len]); ctx.lineDashOffset = len * (1 - easeInOut(u)); ctx.globalAlpha = al; ctx.lineJoin = 'round';
  ctx.shadowColor = o.glow || '#ff8a2a'; ctx.shadowBlur = 50; ctx.strokeStyle = o.color || '#8a1810'; ctx.lineWidth = o.width || 20; ctx.stroke(); ctx.shadowBlur = 0; ctx.strokeStyle = o.inner || '#ffb060'; ctx.lineWidth = (o.width || 20) * .3; ctx.stroke();
  ctx.restore();
}
function inkLabel(ctx, o, t, lv) {
  const u = clamp((t - o.t0) / (o.dur || .55)); if (u <= 0) return;
  const [x, y] = o.lon != null ? proj(o.lon, o.lat) : [o.x, o.y];
  ctx.save(); ctx.globalAlpha = (.16 + .84 * lv) * (1 - .85 * fadeOut(lv, t)); ctx.font = `700 ${o.size}px Cinzel`; ctx.textBaseline = 'alphabetic';
  const tw = ctx.measureText(o.text).width, lx = (o.align === 'center' ? x - tw / 2 : o.align === 'right' ? x - tw : x) + (o.dx || 0), ly = y + (o.dy || 0);
  ctx.beginPath(); ctx.rect(lx - 60, ly - o.size * 1.4, (tw + 120) * easeOut(u), o.size * 2.8 + (o.subSize || 0) * 1.6); ctx.clip(); ctx.textAlign = 'left';
  if (o.style === 'glow') { ctx.shadowColor = o.glowColor || '#ff9a3a'; ctx.shadowBlur = o.size * .5; ctx.fillStyle = o.color || '#ffcf86'; ctx.fillText(o.text, lx, ly); ctx.shadowBlur = o.size * .2; ctx.fillText(o.text, lx, ly); ctx.shadowBlur = 0; }
  else { ctx.lineJoin = 'round'; ctx.lineWidth = o.size * .14; ctx.strokeStyle = 'rgba(242,230,200,.85)'; ctx.strokeText(o.text, lx, ly); ctx.fillStyle = o.color || '#3a1a0c'; ctx.fillText(o.text, lx, ly); }
  if (o.sub) { const su = clamp((t - (o.subT ?? o.t0 + .3)) / .45); if (su > 0) { ctx.globalAlpha *= easeOut(su); ctx.font = `italic 600 ${o.subSize}px "Playfair Display"`; const sx = lx + (o.subDx || 0), sy = ly + o.subSize * 1.15; if (o.style === 'glow') { ctx.shadowColor = o.glowColor || '#ff9a3a'; ctx.shadowBlur = o.subSize * .4; ctx.fillStyle = o.subColor || '#ffcf86'; ctx.fillText(o.sub, sx, sy); } else { ctx.lineWidth = o.subSize * .14; ctx.strokeText(o.sub, sx, sy); ctx.fillStyle = o.subColor || '#9a1c14'; ctx.fillText(o.sub, sx, sy); } } }
  ctx.restore();
}
function penCircle(ctx, o, t, lv) {
  const u = clamp((t - o.t0) / (o.dur || .5)); if (u <= 0) return; const [x, y] = o.lon != null ? proj(o.lon, o.lat) : [o.x, o.y];
  ctx.save(); ctx.globalAlpha = (.35 + .65 * lv) * (1 - .8 * fadeOut(lv, t)); ctx.lineCap = 'round'; ctx.strokeStyle = o.color || '#b3140c'; ctx.lineWidth = o.width || 18; ctx.beginPath();
  const a0 = -2.2, span = TAU * 1.08 * easeInOut(u); for (let k = 0; k <= 80; k++) { const a = a0 + span * k / 80, w = 1 + .04 * Math.sin(a * 3 + 1); const px = x + Math.cos(a) * o.rx * w, py = y + Math.sin(a) * o.ry * w * (1 + .05 * k / 80); k ? ctx.lineTo(px, py) : ctx.moveTo(px, py); }
  ctx.stroke(); ctx.restore();
}
function dropAnim(o, t) { const u = clamp((t - o.t0) / (o.dur || .7)); return { u, e: easeOut(u), lift: 1 - easeOut(u) }; }
function paperShadow(ctx, lift, base = .6) { ctx.shadowColor = `rgba(0,0,0,${base - .25 * lift})`; ctx.shadowBlur = 40 + 160 * lift; ctx.shadowOffsetX = 18 + 70 * lift; ctx.shadowOffsetY = 26 + 100 * lift; }
function printObj(ctx, o, t, lv) {
  const im = IMG[o.img]; if (!im || !im.naturalWidth) return; const { u, e, lift } = dropAnim(o, t); if (u <= 0) return;
  const sc = lerp(1.18, 1, e), bw = o.w * .04, h = o.w * im.naturalHeight / im.naturalWidth;
  ctx.save(); ctx.translate(o.x, o.y); ctx.rotate((o.rot || 0) + lift * .05); ctx.scale(sc, sc); ctx.globalAlpha = clamp(u * 4);
  const W2 = o.w + bw * 2, H2 = h + bw * 2 + (o.caption ? bw * 2.6 : 0);
  paperShadow(ctx, lift); ctx.fillStyle = '#f1e8d4'; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2); ctx.shadowColor = 'transparent';
  ctx.drawImage(im, -o.w / 2, -H2 / 2 + bw, o.w, h);
  if (o.tone) { ctx.fillStyle = o.tone; ctx.fillRect(-o.w / 2, -H2 / 2 + bw, o.w, h); }
  if (o.fx) o.fx(ctx, t, -o.w / 2, -H2 / 2 + bw, o.w, h);
  if (o.caption) { ctx.font = `600 ${bw * 1.7}px Caveat`; ctx.fillStyle = '#2a1a10'; ctx.textAlign = 'center'; ctx.fillText(o.caption, 0, H2 / 2 - bw * .9); }
  const pg = ctx.createLinearGradient(-W2 / 2, -H2 / 2, W2 / 2, H2 / 2); pg.addColorStop(0, 'rgba(255,255,255,.1)'); pg.addColorStop(.5, 'rgba(255,255,255,0)'); pg.addColorStop(1, 'rgba(0,0,0,.1)'); ctx.fillStyle = pg; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2);
  if (lv < 1) { ctx.fillStyle = `rgba(10,6,4,${.6 * (1 - lv)})`; ctx.fillRect(-W2 / 2, -H2 / 2, W2, H2); }
  ctx.restore();
}
function newspaper(ctx, o, t, lv) { // gazete kupürü: gerçek başlık + fotoğraf, gövde metni yumuşak gri çizgiler (kural 3)
  const { u, e, lift } = dropAnim(o, t); if (u <= 0) return; const w = o.w, h = o.h || w * 1.3, R = rng(o.seed || 9);
  ctx.save(); ctx.translate(o.x, o.y); ctx.rotate((o.rot || 0) + lift * .06); const sc = lerp(1.15, 1, e); ctx.scale(sc, sc); ctx.globalAlpha = clamp(u * 4);
  paperShadow(ctx, lift, .55); ctx.beginPath(); const jag = (x0, y0, x1, y1, n) => { for (let i = 0; i <= n; i++) ctx.lineTo(lerp(x0, x1, i / n) + (R() - .5) * w * .006, lerp(y0, y1, i / n) + (R() - .5) * w * .006); };
  ctx.moveTo(-w / 2, -h / 2); jag(-w / 2, -h / 2, w / 2, -h / 2, 30); jag(w / 2, -h / 2, w / 2, h / 2, 40); jag(w / 2, h / 2, -w / 2, h / 2, 30); jag(-w / 2, h / 2, -w / 2, -h / 2, 40); ctx.closePath();
  ctx.fillStyle = ctx.createPattern(TEX.news, 'repeat'); ctx.fill(); ctx.shadowColor = 'transparent'; ctx.save(); ctx.clip();
  ctx.fillStyle = 'rgba(160,120,60,.18)'; ctx.fillRect(-w / 2, -h / 2, w, h);
  const m = w * .06, top = -h / 2 + m; ctx.fillStyle = '#1e1610'; ctx.textAlign = 'center';
  ctx.font = `700 ${w * .13}px ${o.rtl ? 'Amiri' : 'Cinzel'}`; ctx.fillText(o.masthead || '', 0, top + w * .12);
  ctx.fillRect(-w / 2 + m, top + w * .16, w - 2 * m, w * .006); ctx.fillRect(-w / 2 + m, top + w * .175, w - 2 * m, w * .002);
  let y = top + w * .22;
  if (o.headline) { ctx.font = `700 ${w * (o.hSize || .075)}px ${o.rtl ? 'Amiri' : 'Cinzel'}`; ctx.fillText(o.headline, 0, y + w * .07); y += w * .11; }
  const im = IMG[o.img], ph = im && im.naturalWidth ? (w - 2 * m) * .62 * im.naturalHeight / im.naturalWidth : 0, pw = (w - 2 * m) * .62, px = o.rtl ? w / 2 - m - pw : -w / 2 + m;
  if (ph) { ctx.save(); ctx.filter = 'grayscale(1) contrast(1.15) sepia(.35)'; ctx.drawImage(im, px, y, pw, ph); ctx.restore(); ctx.strokeStyle = '#1e1610'; ctx.lineWidth = w * .004; ctx.strokeRect(px, y, pw, ph); }
  ctx.fillStyle = 'rgba(40,30,20,.28)'; const colX = o.rtl ? -w / 2 + m : px + pw + m * .6, colW = w - 2 * m - pw - m * .6;
  for (let ly = y; ly < h / 2 - m; ly += w * .028) { const inPhoto = ly < y + ph + m * .4; const x0 = inPhoto ? colX : -w / 2 + m, ww = inPhoto ? colW : w - 2 * m; ctx.fillRect(x0, ly, ww * (.86 + R() * .14), w * .009); }
  const cg = ctx.createLinearGradient(-w / 2, -h / 2, w / 2, h / 2); cg.addColorStop(0, 'rgba(255,240,210,.15)'); cg.addColorStop(.6, 'rgba(0,0,0,0)'); cg.addColorStop(1, 'rgba(60,40,10,.25)'); ctx.fillStyle = cg; ctx.fillRect(-w / 2, -h / 2, w, h);
  if (lv < 1) { ctx.fillStyle = `rgba(10,6,4,${.6 * (1 - lv)})`; ctx.fillRect(-w / 2, -h / 2, w, h); }
  ctx.restore(); ctx.restore();
}
function compass(ctx, o, t) { const r = o.r; ctx.save(); ctx.translate(o.x, o.y); ctx.shadowColor = 'rgba(0,0,0,.6)'; ctx.shadowBlur = 60; ctx.shadowOffsetX = 30; ctx.shadowOffsetY = 40; ctx.beginPath(); ctx.arc(0, 0, r, 0, TAU); const g = ctx.createRadialGradient(-r * .3, -r * .3, r * .1, 0, 0, r); g.addColorStop(0, '#e8c87a'); g.addColorStop(1, '#7a5420'); ctx.fillStyle = g; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.beginPath(); ctx.arc(0, 0, r * .84, 0, TAU); ctx.fillStyle = '#efe4c8'; ctx.fill(); ctx.strokeStyle = '#3a2810'; ctx.lineWidth = r * .02; for (let k = 0; k < 32; k++) { const a = k / 32 * TAU, l = k % 8 ? .06 : .12; ctx.beginPath(); ctx.moveTo(Math.cos(a) * r * .8, Math.sin(a) * r * .8); ctx.lineTo(Math.cos(a) * r * (.8 - l), Math.sin(a) * r * (.8 - l)); ctx.stroke(); } const na = (o.rot || .3) + Math.sin(t * 1.3) * .05; ctx.rotate(na); ctx.beginPath(); ctx.moveTo(0, -r * .7); ctx.lineTo(r * .08, 0); ctx.lineTo(0, r * .7); ctx.lineTo(-r * .08, 0); ctx.closePath(); ctx.fillStyle = '#9a1c14'; ctx.fill(); ctx.beginPath(); ctx.moveTo(0, r * .7); ctx.lineTo(r * .08, 0); ctx.lineTo(-r * .08, 0); ctx.fillStyle = '#2a2a2a'; ctx.fill(); ctx.beginPath(); ctx.arc(0, 0, r * .05, 0, TAU); ctx.fillStyle = '#d9b25a'; ctx.fill(); ctx.rotate(-na); const gl = ctx.createLinearGradient(-r, -r, r, r); gl.addColorStop(0, 'rgba(255,255,255,.35)'); gl.addColorStop(.4, 'rgba(255,255,255,0)'); ctx.beginPath(); ctx.arc(0, 0, r * .84, 0, TAU); ctx.fillStyle = gl; ctx.fill(); ctx.restore(); }
function magnifier(ctx, o, t, lv, flat) { // haritanın üstünde duran büyüteç; altındaki dünyayı büyütür
  const p = o.path ? pathAt(o.path, t) : [o.x, o.y]; const a = smooth((t - (o.t0 ?? -9)) / .6); if (a <= 0) return; const r = o.r, mag = o.mag || 1.7;
  const m = ctx.getTransform(), sx = m.a * p[0] + m.c * p[1] + m.e, sy = m.b * p[0] + m.d * p[1] + m.f, sr = r * Math.hypot(m.a, m.b);
  ctx.save(); ctx.globalAlpha = a; ctx.shadowColor = 'rgba(0,0,0,.55)'; ctx.shadowBlur = 80; ctx.shadowOffsetX = 50; ctx.shadowOffsetY = 70; ctx.beginPath(); ctx.arc(p[0], p[1], r * 1.06, 0, TAU); ctx.fillStyle = 'rgba(0,0,0,.01)'; ctx.fill(); ctx.shadowColor = 'transparent';
  ctx.save(); ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, TAU); ctx.clip(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.drawImage(flat.snap, sx - sr / mag, sy - sr / mag, 2 * sr / mag, 2 * sr / mag, sx - sr, sy - sr, 2 * sr, 2 * sr); ctx.restore();
  const hl = ctx.createRadialGradient(p[0] - r * .4, p[1] - r * .45, r * .05, p[0], p[1], r); hl.addColorStop(0, 'rgba(255,255,240,.45)'); hl.addColorStop(.35, 'rgba(255,255,240,.05)'); hl.addColorStop(1, 'rgba(0,0,0,.18)'); ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, TAU); ctx.fillStyle = hl; ctx.fill();
  ctx.lineWidth = r * .09; ctx.strokeStyle = '#b08a3a'; ctx.stroke(); ctx.lineWidth = r * .03; ctx.strokeStyle = '#f0d890'; ctx.beginPath(); ctx.arc(p[0], p[1], r * .97, 0, TAU); ctx.stroke();
  const ha = o.handle ?? .8; ctx.translate(p[0] + Math.cos(ha) * r * 1.04, p[1] + Math.sin(ha) * r * 1.04); ctx.rotate(ha); ctx.fillStyle = '#b08a3a'; ctx.fillRect(0, -r * .07, r * .22, r * .14); ctx.fillStyle = '#4a2a14'; ctx.beginPath(); ctx.moveTo(r * .2, -r * .09); ctx.lineTo(r * 1.1, -r * .11); ctx.quadraticCurveTo(r * 1.2, 0, r * 1.1, r * .11); ctx.lineTo(r * .2, r * .09); ctx.fill();
  ctx.restore();
}
function pathAt(path, t) { if (t <= path[0][0]) return [path[0][1], path[0][2]]; for (let i = 0; i < path.length - 1; i++) if (t <= path[i + 1][0]) { const u = easeInOut((t - path[i][0]) / (path[i + 1][0] - path[i][0])); return [lerp(path[i][1], path[i + 1][1], u), lerp(path[i][2], path[i + 1][2], u)]; } const l = path[path.length - 1]; return [l[1], l[2]]; }
const FLAT = { city: cityDot, route: routeDraw, region, label: inkLabel, circle: penCircle, print: printObj, newspaper, compass };

// ---------------- ekran katmanı (dik duran objeler, ekran yazıları) ----------------
function flagScr(ctx, o, t, P) { // dikilen bayrak (ref: ahşap piyonlar/bayraklar)
  const u = clamp((t - o.t0) / .5); if (u <= 0) return; const [x, y, k] = P(o.lon, o.lat), s = (o.s || 1) * k * Math.min(1.6, CURZ * 1.6) * 260;
  const rise = backOut(u), hgt = s * rise;
  ctx.save(); ctx.translate(x, y); ctx.globalAlpha = clamp(u * 3) * (o.alpha ?? 1);
  ctx.beginPath(); ctx.ellipse(s * .08, 0, s * .16, s * .05, 0, 0, TAU); ctx.fillStyle = 'rgba(0,0,0,.35)'; ctx.fill();
  ctx.beginPath(); ctx.ellipse(0, 0, s * .1, s * .035, 0, 0, TAU); ctx.fillStyle = '#5a3a1a'; ctx.fill();
  ctx.fillStyle = '#3a2614'; ctx.fillRect(-s * .012, -hgt, s * .024, hgt);
  const fw = s * .42, fh = s * .26, wave = Math.sin(t * 4 + x * .01) * s * .02; ctx.beginPath(); ctx.moveTo(s * .012, -hgt); ctx.quadraticCurveTo(fw * .5, -hgt + wave, fw, -hgt + s * .02); ctx.lineTo(fw, -hgt + fh); ctx.quadraticCurveTo(fw * .5, -hgt + fh + wave, s * .012, -hgt + fh * .95); ctx.closePath();
  const g = ctx.createLinearGradient(0, -hgt, fw, -hgt + fh); g.addColorStop(0, o.color || '#b3141a'); g.addColorStop(1, '#6a0a0e'); ctx.fillStyle = g; ctx.fill();
  if (o.crescent !== false) { ctx.beginPath(); ctx.arc(fw * .45, -hgt + fh * .5, fh * .24, 0, TAU); ctx.fillStyle = '#f2e6c8'; ctx.fill(); ctx.beginPath(); ctx.arc(fw * .52, -hgt + fh * .5, fh * .2, 0, TAU); ctx.fillStyle = o.color || '#a5121a'; ctx.fill(); }
  ctx.restore();
}
function pinScr(ctx, o, t, P) { const u = clamp((t - o.t0) / .4); if (u <= 0) return; const [x, y, k] = P(o.lon, o.lat), s = (o.s || 1) * k * 90, yy = y - (1 - backOut(u)) * s * 2; ctx.save(); ctx.globalAlpha = clamp(u * 3); const gl = ctx.createRadialGradient(x, y, 0, x, y, s * 1.6); gl.addColorStop(0, 'rgba(255,150,60,.55)'); gl.addColorStop(1, 'rgba(255,150,60,0)'); ctx.fillStyle = gl; ctx.fillRect(x - s * 2, y - s * 2, s * 4, s * 4); ctx.beginPath(); ctx.moveTo(x, yy); ctx.bezierCurveTo(x - s * .6, yy - s * .7, x - s * .45, yy - s * 1.35, x, yy - s * 1.35); ctx.bezierCurveTo(x + s * .45, yy - s * 1.35, x + s * .6, yy - s * .7, x, yy); ctx.fillStyle = '#c4161c'; ctx.fill(); ctx.beginPath(); ctx.arc(x, yy - s * .95, s * .18, 0, TAU); ctx.fillStyle = '#fff'; ctx.fill(); ctx.restore(); }
function titleScr(ctx, o, t) { // ekrana yazılan büyük kahraman kelime (anlatıcının söylediğini belgede göstermiyorsak)
  const a = smooth((t - o.t0) / .35) * (1 - smooth((t - (o.t1 ?? 99)) / .4)); if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.textAlign = 'center'; ctx.font = `700 ${o.size}px ${o.font || 'Cinzel'}`; const y = o.y * H, sc = lerp(1.08, 1, easeOut((t - o.t0) / .6));
  ctx.translate(W / 2, y); ctx.scale(sc, sc); ctx.shadowColor = 'rgba(0,0,0,.8)'; ctx.shadowBlur = 40; ctx.fillStyle = o.color || '#f6e7c4'; ctx.fillText(o.text, 0, 0); ctx.shadowColor = o.glow || 'rgba(255,170,80,.6)'; ctx.shadowBlur = 30; ctx.fillText(o.text, 0, 0);
  if (o.sub) { ctx.font = `italic 600 ${o.subSize || o.size * .45}px "Playfair Display"`; ctx.shadowColor = 'rgba(0,0,0,.8)'; ctx.shadowBlur = 30; ctx.fillStyle = o.subColor || '#e8a860'; ctx.fillText(o.sub, 0, (o.subSize || o.size * .45) * 1.4); }
  ctx.restore();
}
const SCR = { flag: flagScr, pin: pinScr, title: titleScr };

// ---------------- tuvaller ----------------
const out = document.getElementById('c'); out.width = W; out.height = H; const octx = out.getContext('2d');
const flat = document.createElement('canvas'); flat.width = FW; flat.height = FH; const fctx = flat.getContext('2d');
const snap = document.createElement('canvas'); snap.width = FW; snap.height = FH; flat.snap = snap;
const glc = document.createElement('canvas'); glc.width = W; glc.height = H;
const gl = glc.getContext('webgl2', { preserveDrawingBuffer: true, antialias: false, premultipliedAlpha: false });
const VS = `#version 300 es
in vec2 p; out vec2 uv; void main(){ uv = p * .5 + .5; gl_Position = vec4(p, 0., 1.); }`;
const FS = `#version 300 es
precision highp float; in vec2 uv; out vec4 o; uniform sampler2D tex; uniform vec2 scr, fsz, fc; uniform float foc, tilt, dof, focusY, bloom, grain, vig, warm, seed, lpow; uniform vec2 vel, lpos;
vec3 plane(vec2 px){ float a = tilt, x = px.x, y = -px.y, hh = foc * cos(a), s = hh / (foc * cos(a) - y * sin(a)); float X = s * x, Y = -hh * tan(a) + s * (y * cos(a) + foc * sin(a)); return vec3(X, -Y, s); }
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
void main(){
  vec2 px = vec2(uv.x - .5, .5 - uv.y) * scr; vec3 P = plane(px); vec2 t = (fc + P.xy) / fsz;
  float sF = plane(vec2(0., (focusY - .5) * scr.y)).z; float blur = dof * abs(log(P.z / sF)) * 26.;
  float lod = log2(max(1., blur)); vec3 c = vec3(0.); float n = 0.;
  for (int i = 0; i < 9; i++) { float k = float(i) / 8. - .5; vec2 off = vel * k / fsz; float ang = float(i) * 2.399 + seed; vec2 j = vec2(cos(ang), sin(ang)) * blur * .5 * sqrt(float(i) / 9.) / fsz; c += textureLod(tex, t + off + j, lod).rgb; n += 1.; }
  c /= n;
  vec3 b = textureLod(tex, t, 5.5).rgb; c += max(b - .55, 0.) * bloom * 2.2 + b * bloom * .12;
  vec2 q = uv - vec2(lpos.x, 1. - lpos.y); float lp = exp(-dot(q * vec2(scr.x / scr.y, 1.), q * vec2(scr.x / scr.y, 1.)) * 2.2); c *= mix(1. - lpow * .55, 1. + lpow * .45, lp);
  c = mix(c, c * vec3(1.06, 1.0, .9), warm * 4.); c = c * c * (3. - 2. * c) * .35 + c * .65;
  vec2 v = uv - .5; c *= 1. - vig * smoothstep(.25, .85, length(v * vec2(scr.x / scr.y, 1.) * 1.1));
  c += (h21(uv * scr + seed * 17.) - .5) * grain; o = vec4(c, 1.);
}`;
function sh(type, src) { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) console.log('GLSL', gl.getShaderInfoLog(s)); return s; }
const prog = gl.createProgram(); gl.attachShader(prog, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, FS)); gl.linkProgram(prog); gl.useProgram(prog);
const vb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, vb); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW); const loc = gl.getAttribLocation(prog, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
const tx = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tx); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
const U = n => gl.getUniformLocation(prog, n);

function viewFlat(ctx, cam, hh) { ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.translate(FCX + hh.x, FCY + hh.y); ctx.rotate((cam.r || 0) + hh.r); ctx.scale(cam.z, cam.z); ctx.translate(-cam.x, -cam.y); }
function drawFlat(t, cam, hh) {
  CURZ = cam.z; CURT = t; fctx.setTransform(1, 0, 0, 1, 0, 0); fctx.fillStyle = '#120c08'; fctx.fillRect(0, 0, FW, FH);
  viewFlat(fctx, cam, hh); drawDesk(fctx);
  for (const o of OBJECTS) if (o.type === 'compass' || o.under) { viewFlat(fctx, cam, hh); (FLAT[o.type] || (() => { }))(fctx, o, t, 1); }
  viewFlat(fctx, cam, hh); drawMap(fctx);
  const md = mapDimAt(t); if (md > 0) { fctx.save(); fctx.setTransform(1, 0, 0, 1, 0, 0); fctx.fillStyle = `rgba(12,8,5,${md})`; fctx.fillRect(0, 0, FW, FH); fctx.restore(); }
  const list = OBJECTS.filter(o => FLAT[o.type] && o.type !== 'compass' && !o.under).map(o => [o, heroLevel(o.id, t)]).sort((a, b) => a[1] - b[1]);
  for (const [o, lv] of list) { viewFlat(fctx, cam, hh); FLAT[o.type](fctx, o, t, lv); }
  const mags = OBJECTS.filter(o => o.type === 'magnifier'); if (mags.length) { const s = snap.getContext('2d'); s.drawImage(flat, 0, 0); for (const o of mags) { viewFlat(fctx, cam, hh); magnifier(fctx, o, t, 1, flat); } }
}
function lens(t, cam, vel, f) {
  gl.viewport(0, 0, W, H); gl.bindTexture(gl.TEXTURE_2D, tx); gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, flat); gl.generateMipmap(gl.TEXTURE_2D);
  gl.uniform2f(U('scr'), W, H); gl.uniform2f(U('fsz'), FW, FH); gl.uniform2f(U('fc'), FCX, FCY); gl.uniform1f(U('foc'), FOC); gl.uniform1f(U('tilt'), cam.tilt * Math.PI / 180);
  gl.uniform1f(U('dof'), L.dof); gl.uniform1f(U('focusY'), L.focusY); gl.uniform1f(U('bloom'), L.bloom); gl.uniform1f(U('grain'), L.grain); gl.uniform1f(U('vig'), L.vignette); gl.uniform1f(U('warm'), L.warm); gl.uniform1f(U('seed'), f * .618 % 1 * 10);
  const flick = typeof CANDLE !== 'undefined' && CANDLE ? 1 + .06 * Math.sin(t * 9.1) + .04 * Math.sin(t * 23.7) : 1; gl.uniform1f(U('lpow'), L.lightPower * flick); gl.uniform2f(U('lpos'), L.light[0], L.light[1]); gl.uniform2f(U('vel'), vel[0] * L.mblur, vel[1] * L.mblur);
  gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
}
function renderFrame(f) {
  const t = f / FORMAT.fps, cam = camAt(t), hh = handheld(t), c2 = camAt(t + 1 / FORMAT.fps);
  const vel = [(c2.x - cam.x) * cam.z * .5, (c2.y - cam.y) * cam.z * .5]; const zv = Math.log(c2.z / cam.z) * 400; const vv = [vel[0], vel[1] + zv];
  drawFlat(t, cam, hh); lens(t, cam, vv, f);
  octx.setTransform(1, 0, 0, 1, 0, 0); octx.drawImage(glc, 0, 0);
  const P = (lon, lat) => { const [wx, wy] = proj(lon, lat), dx = wx - cam.x, dy = wy - cam.y, c = Math.cos((cam.r || 0) + hh.r), s = Math.sin((cam.r || 0) + hh.r); const fx = (dx * c - dy * s) * cam.z + hh.x, fy = (dx * s + dy * c) * cam.z + hh.y; const [sx, sy, k] = plane2scr(fx, fy, cam.tilt); return [W / 2 + sx, H / 2 + sy, k]; };
  for (const o of OBJECTS) if (SCR[o.type]) { const lv = heroLevel(o.id, t); octx.save(); octx.globalAlpha = .35 + .65 * lv; SCR[o.type](octx, o, t, P); octx.restore(); }
}
window.READY = (async () => {
  GEO = window.GEOJS; makeTextures();
  const all = Object.assign({}, IMAGES, typeof RELIEF === 'object' && L.relief !== 0 ? { __relief: RELIEF.src } : {});
  await Promise.all(Object.entries(all).map(([k, src]) => new Promise(r => { const i = new Image(); i.onload = i.onerror = () => r(); i.src = src; IMG[k] = i; })));
  for (const ff of ['700 80px Cinzel', 'italic 600 80px "Playfair Display"', '600 80px Caveat', '700 80px Amiri']) await document.fonts.load(ff);
  return true;
})();
window.renderFrame = renderFrame; window.TOTAL = Math.round(FORMAT.dur * FORMAT.fps); window.grab = (q = .93) => out.toDataURL('image/jpeg', q);
