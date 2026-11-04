import numpy as np, soundfile as sf, subprocess
from scipy import signal
SR = 44100; DUR = 312 / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(4)
def lp(x, f): b, a = signal.butter(2, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def bp(x, lo, hi): b, a = signal.butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return signal.lfilter(b, a, x)
def place(buf, x, at, g=1.):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
def env(n, a, d): u = np.arange(n) / SR; return np.minimum(1, u / a) * np.exp(-u / d)
def whoosh(d=1.0): n = int(d * SR); k = np.linspace(0, 1, n); x = rng.standard_normal(n); return (bp(x, 200, 900) * (1 - k) + bp(x, 900, 4000) * k) * np.sin(np.pi * k) ** 2 * 1.2
def paper(): n = int(.5 * SR); return bp(rng.standard_normal(n), 1200, 7000) * env(n, .005, .08) * 1.2 + lp(rng.standard_normal(n), 300) * env(n, .002, .05) * 2
def pen(d=.5): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 2500, 8000) * (.5 + .5 * np.sin(2 * np.pi * 18 * u)) * np.sin(np.pi * u / d) * .5
def boom(): n = int(3 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 40 * u * (1 + .4 * np.exp(-u * 3))) * np.exp(-u * 1.3) * .9
# hüzünlü dron: D hicaz (D, Eb, F#, A)
mus = sum(a * np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .06 * t) * 2) for f, a in [(73.4, .5), (110, .3), (146.8, .2), (155.6, .1), (185, .08), (220, .07)])
mus = lp(mus, 900) * np.interp(t, [0, 1.0, DUR - .8, DUR], [0, 1, 1, .3])
sfx = np.zeros(N)
place(sfx, boom(), 0.0, .7); place(sfx, boom(), 1.84, .45)
for w in [3.0, 4.6, 6.0, 7.6]: place(sfx, whoosh(1.1), w - .3, .25)
for p in [3.3, 6.2, 8.7]: place(sfx, paper(), p, .7)
place(sfx, pen(.7), 1.84, .3); place(sfx, pen(.5), 9.86, .5)
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'build/voice.mp3', '-t', str(DUR), '-ar', str(SR), '-ac', '1', 'build/vo.wav'], check=True)
vo, _ = sf.read('build/vo.wav'); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .5 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
mix = VO + (mus / np.max(np.abs(mus))) * .15 * duck + sfx * .5
mix *= np.interp(t, [0, .02, DUR - .35, DUR], [0, 1, 1, 0]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', DUR)
