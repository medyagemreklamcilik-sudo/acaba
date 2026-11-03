window.ciz = () => {
  const c = document.getElementById('c'); c.width = W; c.height = H; const ctx = c.getContext('2d'); const t = 1.3;
  const cam = { x: 540, y: 1000, z: 1.0 };
  tepe(ctx, cam, t); applyCam(ctx, cam, 1); ctx.fillStyle = '#5f8a3e'; ctx.beginPath(); ctx.moveTo(-500, 1700); ctx.quadraticCurveTo(540, 700, 1600, 1700); ctx.lineTo(1600, 2600); ctx.lineTo(-500, 2600); ctx.fill();
  const hy = x => hillY(x, 1700, 700);
  for (let i = 0; i < 7; i++) { const x = 120 + i * 140; kutuk(ctx, x, hy(x) + 5, 22, 130); }
  kadirga(ctx, 470, hy(470) - 40, 1.15, t, { rot: Math.atan2(hy(490) - hy(450), 40), oars: 0 });
  for (let i = 0; i < 3; i++) { const x = 820 + i * 95; yeniceri(ctx, x, hy(x) + 10, 230, { lean: .5, arms: { L: [1.4, -.2], R: [1.4, -.2] }, legs: { L: [.4, -.3], R: [-.4, -.3] }, face: { eyes: 'wide', mouth: 'o' } }); }
  sc(ctx); ctx.save(); ctx.textAlign = 'center';
  text(ctx, 'HE CARRIED', 540, 250, 130, '#fff', INK, 18, 'Poppins', 700);
  text(ctx, 'HIS NAVY', 540, 400, 130, '#fff', INK, 18, 'Poppins', 700);
  text(ctx, 'OVER A HILL', 540, 550, 130, '#ffd23a', INK, 18, 'Poppins', 700);
  ctx.restore();
  etiket(ctx, '1453', 540, 1420, 110, 1, { col: '#fff', bg: '#c4161c', rot: -.06 });
};
