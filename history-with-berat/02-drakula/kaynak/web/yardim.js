// "Tahta çıktığı gece, 19 kardeşini boğdurttu." · 4.5 s hook sample
const SULTAN = { cols: ['#6c3fb0', '#6c3fb0'], hat: 'none', belt: false, vest: '#e8b93a' };
const PRINCE_COLS = [PAL.red, PAL.blue, PAL.green, PAL.navy, PAL.yellow, PAL.purple];
const C = (base, extra) => Object.assign({}, base, extra);
const handheld = (t, a = 4) => shake(t * .35, a, 1, 2);

// ---- props ----
function drawTurban(ctx, x, y, s, tilt = 0) {
  // y = head centre in world coords, s = figure scale
  const hr = .19 * s;
  ctx.save(); ctx.translate(x, y); ctx.rotate(tilt);
  const top = -hr * .55;
  ctx.beginPath(); ctx.ellipse(0, top - hr * .35, hr * 1.12, hr * .78, 0, Math.PI, 0); ctx.lineTo(hr * 1.1, top + hr * .05);
  ctx.quadraticCurveTo(0, top + hr * .32, -hr * 1.1, top + hr * .05); ctx.closePath(); fillStroke(ctx, '#fbf8f1', .017 * s);
  for (let i = -2; i <= 2; i++) { ctx.beginPath(); ctx.moveTo(i * hr * .38 - hr * .3, top + hr * .1); ctx.quadraticCurveTo(i * hr * .38, top - hr * .5, i * hr * .38 + hr * .35, top - hr * .95); ctx.lineWidth = .008 * s; ctx.strokeStyle = 'rgba(60,40,40,.35)'; ctx.stroke(); }
  // jewel + plume
  circle(ctx, 0, top - hr * .25, hr * .16); fillStroke(ctx, '#d8312b', .012 * s);
  ctx.beginPath(); ctx.moveTo(0, top - hr * .35); ctx.quadraticCurveTo(hr * .35, top - hr * 1.3, hr * .1, top - hr * 1.9); ctx.quadraticCurveTo(-hr * .15, top - hr * 1.2, 0, top - hr * .35); fillStroke(ctx, '#1d1a24', .01 * s);
  ctx.restore();
}
function drawFez(ctx, x, y, s, tilt = 0) {
  const hr = .19 * s; ctx.save(); ctx.translate(x, y); ctx.rotate(tilt);
  ctx.beginPath(); ctx.moveTo(-hr * .62, -hr * .62); ctx.lineTo(-hr * .45, -hr * 1.25); ctx.lineTo(hr * .45, -hr * 1.25); ctx.lineTo(hr * .62, -hr * .62); ctx.closePath(); fillStroke(ctx, '#c42a2a', .02 * s);
  line(ctx, 0, -hr * 1.25, hr * .55, -hr * .95, .02 * s, '#1d1a24'); ctx.restore();
}
function drawThrone(ctx, x, y, s) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  // steps
  rrect(ctx, -330, -40, 660, 60, 8); fillStroke(ctx, '#7a2230', 6);
  rrect(ctx, -270, -95, 540, 60, 8); fillStroke(ctx, '#8e2a38', 6);
  // back
  ctx.beginPath(); ctx.moveTo(-170, -95); ctx.lineTo(-170, -520); ctx.quadraticCurveTo(0, -700, 170, -520); ctx.lineTo(170, -95); ctx.closePath(); fillStroke(ctx, '#e3b23c', 7);
  ctx.beginPath(); ctx.moveTo(-120, -260); ctx.lineTo(-120, -490); ctx.quadraticCurveTo(0, -610, 120, -490); ctx.lineTo(120, -260); ctx.closePath(); fillStroke(ctx, '#b4232f', 5);
  circle(ctx, 0, -590, 22); fillStroke(ctx, '#fff3c4', 5);
  // seat + arms
  rrect(ctx, -210, -280, 420, 70, 14); fillStroke(ctx, '#c42a37', 6);
  rrect(ctx, -230, -360, 50, 270, 12); fillStroke(ctx, '#e3b23c', 6);
  rrect(ctx, 180, -360, 50, 270, 12); fillStroke(ctx, '#e3b23c', 6);
  rrect(ctx, -180, -215, 360, 120, 10); fillStroke(ctx, '#d9a632', 6);
  ctx.restore();
}
function palaceBG(ctx, t, cam, night = 1) {
  applyCam(ctx, cam, .2);
  const g = ctx.createLinearGradient(0, -300, 0, 2200); g.addColorStop(0, '#141834'); g.addColorStop(1, '#2a1f3d'); ctx.fillStyle = g; ctx.fillRect(-1500, -1500, 4080, 5000);
  // tiled wall pattern
  ctx.save(); ctx.globalAlpha = .12; for (let i = -6; i < 16; i++) for (let j = -4; j < 18; j++) { const x = i * 120 + (j % 2) * 60, y = j * 120; ctx.beginPath(); ctx.moveTo(x, y - 40); ctx.lineTo(x + 40, y); ctx.lineTo(x, y + 40); ctx.lineTo(x - 40, y); ctx.closePath(); ctx.fillStyle = '#8fb3ff'; ctx.fill(); } ctx.restore();
  // arched windows with moon
  applyCam(ctx, cam, .35);
  for (const wx of [170, 910]) {
    ctx.save(); ctx.beginPath(); ctx.moveTo(wx - 110, 900); ctx.lineTo(wx - 110, 420); ctx.quadraticCurveTo(wx, 230, wx + 110, 420); ctx.lineTo(wx + 110, 900); ctx.closePath();
    const sg = ctx.createLinearGradient(0, 260, 0, 900); sg.addColorStop(0, '#0b1030'); sg.addColorStop(1, '#2b3a78'); ctx.fillStyle = sg; ctx.fill(); ctx.clip();
    for (let k = 0; k < 9; k++) { const R = rng(k + wx); circle(ctx, wx - 100 + R() * 200, 300 + R() * 520, 3 + R() * 3); ctx.fillStyle = `rgba(255,255,230,${.5 + .5 * Math.sin(t * 4 + k)})`; ctx.fill(); }
    if (wx > 500) { const mg = ctx.createRadialGradient(wx + 10, 470, 10, wx + 10, 470, 160); mg.addColorStop(0, 'rgba(255,250,215,.7)'); mg.addColorStop(1, 'rgba(255,250,215,0)'); ctx.fillStyle = mg; ctx.fillRect(wx - 200, 300, 400, 400);
      circle(ctx, wx + 10, 470, 60); ctx.fillStyle = '#fff7d6'; ctx.fill(); circle(ctx, wx + 38, 455, 52); ctx.fillStyle = '#16204a'; ctx.fill(); }
    ctx.restore();
    ctx.beginPath(); ctx.moveTo(wx - 110, 900); ctx.lineTo(wx - 110, 420); ctx.quadraticCurveTo(wx, 230, wx + 110, 420); ctx.lineTo(wx + 110, 900); ctx.lineWidth = 16; ctx.strokeStyle = '#e3b23c'; ctx.stroke();
  }
  // floor + carpet
  applyCam(ctx, cam, 1);
  ctx.fillStyle = '#3a1f2b'; ctx.fillRect(-1500, 1180, 4080, 3000);
  ctx.beginPath(); ctx.moveTo(380, 1180); ctx.lineTo(700, 1180); ctx.lineTo(980, 2400); ctx.lineTo(100, 2400); ctx.closePath(); ctx.fillStyle = '#9b2533'; ctx.fill();
  ctx.beginPath(); ctx.moveTo(410, 1180); ctx.lineTo(670, 1180); ctx.lineTo(930, 2400); ctx.lineTo(150, 2400); ctx.closePath(); ctx.lineWidth = 8; ctx.strokeStyle = '#e3b23c'; ctx.stroke();
  // night tint
  ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = `rgba(10,14,40,${.18 * night})`; ctx.fillRect(0, 0, W, H); ctx.restore();
}
function torchGlow(ctx, x, y, t, a = 1) {
  ctx.save(); ctx.globalCompositeOperation = 'lighter'; const r = 260 + Math.sin(t * 17) * 12;
  const g = ctx.createRadialGradient(x, y, 10, x, y, r); g.addColorStop(0, `rgba(255,190,90,${.45 * a})`); g.addColorStop(1, 'rgba(255,140,40,0)'); ctx.fillStyle = g; ctx.fillRect(x - r, y - r, r * 2, r * 2); ctx.restore();
  line(ctx, x, y + 30, x, y + 140, 14, '#5a3a22');
  ctx.beginPath(); ctx.moveTo(x, y - 45 - Math.sin(t * 23) * 8); ctx.quadraticCurveTo(x + 28, y, x, y + 28); ctx.quadraticCurveTo(x - 28, y, x, y - 45 - Math.sin(t * 23) * 8); fillStroke(ctx, '#ffb02e', 5);
}
// sultan on throne (front view, seated)
function sultan(ctx, x, y, s, o = {}) {
  drawStick(ctx, C(SULTAN, Object.assign({ x, y, s, shadow: false,
    legs: { L: [.95, -.95], R: [.95, -.95] }, arms: { L: [.5, -.6], R: [.5, -.6] },
    face: { eyes: 'normal', mouth: 'flat', browAng: .25 } }, o)));
  drawTurban(ctx, x, y - .765 * s, s, o.headTilt || 0);
}
// 19 princes, two rows; fall = 0..1 per prince
function princes(ctx, t, cx, cy, sc, popT, fallT) {
  const rows = cy.rows;
  let k = 0;
  for (const [n, y, s] of rows) {
    const gap = s * (cy.gap || .5);
    for (let i = 0; i < n; i++, k++) {
      const x = cx + (i - (n - 1) / 2) * gap + (n === 9 ? 0 : 0);
      const ap = clamp((t - popT - k * .045) / .22); if (ap <= 0) continue;
      const fp = fallT == null ? 0 : ease(clamp((t - fallT - (k % 7) * .06 - Math.floor(k / 7) * .05) / .35));
      const dir = (k % 2 ? 1 : -1);
      const sq = backOut(ap);
      drawStick(ctx, { x, y, s: s * sq, cols: PRINCE_COLS[k % 6], hat: 'none', belt: false, lean: dir * fp * 1.45, alpha: 1 - fp * .35,
        arms: fp > .1 ? { L: [2.3, .4], R: [2.3, .4] } : { L: [.35, -.15], R: [.35, -.15] },
        face: fp > .4 ? { eyes: 'x', mouth: 'o' } : { eyes: 'wide', mouth: t > (fallT || 99) - .3 ? 'o' : 'flat', look: [Math.sin(k) * .5, -.2] } });
      // fez follows the head (lean rotates around the feet)
      const hx = x + Math.sin(dir * fp * 1.45) * .765 * s * sq, hy = y - Math.cos(dir * fp * 1.45) * .765 * s * sq;
      ctx.save(); ctx.globalAlpha = 1 - fp * .35; drawFez(ctx, hx, hy, s * sq, dir * fp * 1.45); ctx.restore();
    }
  }
}

// ================= Dracula (History with Berat) =================
const VLAD = { cols: ['#6a1424', '#6a1424'], hat: 'none', belt: false, vest: '#d9a83a' };
function drawCape(ctx, x, y, s, t, open = 1) {
  const w = s * (.32 + .12 * open), top = y - .6 * s, bot = y - .02 * s, fl = Math.sin(t * 3) * s * .02;
  ctx.beginPath(); ctx.moveTo(x - s * .12, top); ctx.quadraticCurveTo(x - w, y - .3 * s, x - w - fl, bot); ctx.lineTo(x + w + fl, bot); ctx.quadraticCurveTo(x + w, y - .3 * s, x + s * .12, top); ctx.closePath();
  fillStroke(ctx, '#3a0810', .014 * s);
  ctx.beginPath(); ctx.moveTo(x - s * .1, top + s * .02); ctx.quadraticCurveTo(x - w * .8, y - .3 * s, x - w * .9, bot - s * .01); ctx.lineTo(x + w * .9, bot - s * .01); ctx.quadraticCurveTo(x + w * .8, y - .3 * s, x + s * .1, top + s * .02); ctx.closePath(); ctx.fillStyle = '#b3162a'; ctx.fill();
}
function drawVladHead(ctx, x, y, s) { // y = ayak; uzun siyah saç, bıyık, mücevherli şapka
  const hx = x, hy = y - .765 * s, r = .19 * s;
  ctx.save(); ctx.fillStyle = '#16121a';
  for (const sg of [-1, 1]) { ctx.beginPath(); ctx.moveTo(hx + sg * r * .7, hy - r * .6); ctx.quadraticCurveTo(hx + sg * r * 1.35, hy + r * .4, hx + sg * r * 1.05, hy + r * 1.55); ctx.lineTo(hx + sg * r * .78, hy + r * 1.45); ctx.quadraticCurveTo(hx + sg * r * .98, hy + r * .3, hx + sg * r * .62, hy - r * .2); ctx.closePath(); fillStroke(ctx, '#16121a', .012 * s); }
  // bıyık
  ctx.beginPath(); ctx.moveTo(hx, hy + r * .28); ctx.quadraticCurveTo(hx - r * .45, hy + r * .2, hx - r * .62, hy + r * .62); ctx.quadraticCurveTo(hx - r * .38, hy + r * .42, hx, hy + r * .42); ctx.quadraticCurveTo(hx + r * .38, hy + r * .42, hx + r * .62, hy + r * .62); ctx.quadraticCurveTo(hx + r * .45, hy + r * .2, hx, hy + r * .28); fillStroke(ctx, '#16121a', .01 * s);
  // şapka
  ctx.beginPath(); ctx.moveTo(hx - r * 1.0, hy - r * .55); ctx.lineTo(hx - r * .9, hy - r * 1.55); ctx.quadraticCurveTo(hx, hy - r * 1.8, hx + r * .9, hy - r * 1.55); ctx.lineTo(hx + r * 1.0, hy - r * .55); ctx.closePath(); fillStroke(ctx, '#7a1426', .014 * s);
  rrect(ctx, hx - r * 1.08, hy - r * .78, r * 2.16, r * .32, r * .1); fillStroke(ctx, '#d9a83a', .012 * s);
  for (let i = 0; i < 7; i++) { circle(ctx, hx - r * .8 + i * r * .27, hy - r * .62, r * .07); ctx.fillStyle = '#fff6e8'; ctx.fill(); }
  circle(ctx, hx, hy - r * 1.05, r * .2); fillStroke(ctx, '#d81e2e', .01 * s); circle(ctx, hx - r * .06, hy - r * 1.11, r * .06); ctx.fillStyle = 'rgba(255,255,255,.7)'; ctx.fill();
  ctx.beginPath(); ctx.moveTo(hx + r * .1, hy - r * 1.2); ctx.quadraticCurveTo(hx + r * .9, hy - r * 2.3, hx + r * .3, hy - r * 2.7); ctx.quadraticCurveTo(hx + r * .25, hy - r * 2.0, hx - r * .05, hy - r * 1.25); fillStroke(ctx, '#f4efe4', .01 * s);
  ctx.restore();
}
function vlad(ctx, x, y, s, t, o = {}) {
  drawCape(ctx, x, y, s, t, o.cape ?? 1);
  drawStick(ctx, C(VLAD, Object.assign({ x, y, s, shadow: false, face: { eyes: 'normal', mouth: 'flat', browAng: .35 } }, o)));
  drawVladHead(ctx, x, y, s);
}
function drawBork(ctx, x, y, s, tilt = 0) { // yeniçeri börkü
  const hr = .19 * s; ctx.save(); ctx.translate(x, y); ctx.rotate(tilt);
  ctx.beginPath(); ctx.moveTo(-hr * .75, -hr * .6); ctx.lineTo(-hr * .65, -hr * 1.9); ctx.quadraticCurveTo(-hr * .4, -hr * 2.6, -hr * 1.4, -hr * 2.4); ctx.quadraticCurveTo(-hr * 2.2, -hr * 1.6, -hr * 2.1, -hr * .5); ctx.lineTo(-hr * 1.6, -hr * .6); ctx.quadraticCurveTo(-hr * 1.6, -hr * 1.6, -hr * .9, -hr * 2.0); ctx.lineTo(hr * .65, -hr * 1.9); ctx.lineTo(hr * .75, -hr * .6); ctx.closePath(); fillStroke(ctx, '#f6f2ea', .02 * s);
  rrect(ctx, -hr * .8, -hr * .8, hr * 1.6, hr * .28, hr * .08); fillStroke(ctx, '#d9a83a', .015 * s);
  rrect(ctx, -hr * .14, -hr * 1.7, hr * .28, hr * .9, hr * .06); fillStroke(ctx, '#d9a83a', .012 * s);
  ctx.restore();
}
function yeniceri(ctx, x, y, s, o = {}) {
  drawStick(ctx, C({ cols: ['#2a5aa8', '#2a5aa8'], hat: 'none', belt: false }, Object.assign({ x, y, s, shadow: false, face: { eyes: 'normal', mouth: 'flat', browAng: .2 } }, o)));
  const lean = o.lean || 0; drawBork(ctx, x + Math.sin(lean) * .765 * s, y - Math.cos(lean) * .765 * s, s, lean);
}
function nightCastle(ctx, cam, t, red = 0) {
  applyCam(ctx, cam, .05);
  const g = ctx.createLinearGradient(0, -200, 0, 1700); g.addColorStop(0, mix('#120a24', '#3a0610', red)); g.addColorStop(1, mix('#3a2a5a', '#b3202a', red)); ctx.fillStyle = g; ctx.fillRect(-800, -800, 2700, 3600);
  applyCam(ctx, cam, .1);
  const mg = ctx.createRadialGradient(780, 420, 40, 780, 420, 360); mg.addColorStop(0, 'rgba(255,245,215,.55)'); mg.addColorStop(1, 'rgba(255,245,215,0)'); ctx.fillStyle = mg; ctx.fillRect(400, 40, 760, 760);
  circle(ctx, 780, 420, 150); ctx.fillStyle = red > .5 ? '#ffb0a0' : '#fff3d6'; ctx.fill();
  applyCam(ctx, cam, .3);
  ctx.fillStyle = '#0c0812';
  ctx.beginPath(); ctx.moveTo(-300, 1250); ctx.quadraticCurveTo(300, 820, 900, 900); ctx.quadraticCurveTo(1200, 960, 1500, 1250); ctx.lineTo(1500, 2400); ctx.lineTo(-300, 2400); ctx.fill();
  for (const [x, w, h] of [[300, 90, 420], [430, 220, 260], [640, 110, 520], [780, 160, 300]]) { ctx.fillRect(x - w / 2, 900 - h, w, h + 60); for (let k = 0; k < 4; k++) ctx.fillRect(x - w / 2 + k * w / 3.5, 900 - h - 30, w / 7, 32); }
  ctx.beginPath(); ctx.moveTo(640 - 70, 900 - 520); ctx.lineTo(640, 900 - 650); ctx.lineTo(640 + 70, 900 - 520); ctx.fill();
  for (const [x, y] of [[620, 520], [450, 700], [780, 680]]) { ctx.fillStyle = '#ffcf6a'; ctx.fillRect(x, y, 16, 26); ctx.fillStyle = '#0c0812'; }
  applyCam(ctx, cam, .6);
  for (let i = 0; i < 7; i++) { const bx = (i * 173 + t * (90 + i * 20)) % 1300 - 100, by = 260 + (i * 97) % 380 + Math.sin(t * 3 + i) * 30, f = Math.sin(t * 22 + i) * 18;
    ctx.beginPath(); ctx.moveTo(bx - 34, by - f); ctx.quadraticCurveTo(bx - 14, by - 8, bx, by + 6); ctx.quadraticCurveTo(bx + 14, by - 8, bx + 34, by - f); ctx.lineTo(bx, by - 4); ctx.closePath(); ctx.fillStyle = '#08060c'; ctx.fill(); }
}

