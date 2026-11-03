// node render.js <klasör> stills 1.5,4.2   |  node render.js <klasör> range f0 f1 out.mp4
const { chromium } = require('playwright'); const { spawn } = require('child_process'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]), mode = process.argv[3];
  const browser = await chromium.launch({ ...(process.env.CHROME ? { executablePath: process.env.CHROME } : {}), args: ['--allow-file-access-from-files', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const fmt = JSON.parse(fs.readFileSync(path.join(dir, 'format.json')));
  const page = await browser.newPage({ viewport: { width: fmt.w, height: fmt.h } });
  page.on('console', m => console.log('[page]', m.text())); page.on('pageerror', e => console.log('[err]', e.message));
  await page.goto('file://' + path.join(dir, 'index.html')); await page.evaluate(() => window.READY);
  if (mode === 'stills') {
    fs.mkdirSync(path.join(dir, 'stills'), { recursive: true });
    for (const t of process.argv[4].split(',').map(Number)) { const d = await page.evaluate(f => { renderFrame(f); return grab(.9); }, Math.round(t * fmt.fps)); fs.writeFileSync(path.join(dir, 'stills', `s_${t.toFixed(2)}.jpg`), Buffer.from(d.split(',')[1], 'base64')); }
  } else {
    const f0 = +process.argv[4], f1 = +process.argv[5], outF = process.argv[6];
    const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fmt.fps), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', String(fmt.fps), outF], { stdio: ['pipe', 'inherit', 'inherit'] });
    const t0 = Date.now();
    for (let f = f0; f < f1; f++) { const d = await page.evaluate(f => { renderFrame(f); return grab(.94); }, f); if (!ff.stdin.write(Buffer.from(d.split(',')[1], 'base64'))) await new Promise(r => ff.stdin.once('drain', r)); if ((f - f0) % 30 === 0) console.log(`kare ${f}/${f1} ${((Date.now() - t0) / 1000).toFixed(0)} sn`); }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();
