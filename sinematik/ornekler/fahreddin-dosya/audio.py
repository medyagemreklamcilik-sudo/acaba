import numpy as np, soundfile as sf, subprocess
from scipy import signal
SR = 44100; DUR = 453 / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(4)
def lp(x, f): b, a = signal.butter(2, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def hp(x, f): b, a = signal.butter(2, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)
def bp(x, lo, hi): b, a = signal.butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return signal.lfilter(b, a, x)
def place(buf, x, at, g=1.):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
def env(n, a, d): u = np.arange(n) / SR; return np.minimum(1, u / a) * np.exp(-u / d)
def boom(): n = int(3.5 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 38 * u * (1 + .5 * np.exp(-u * 3))) * np.exp(-u * 1.1) + lp(rng.standard_normal(n), 200) * env(n, .003, .25) * .6
def paper(): n = int(.5 * SR); return bp(rng.standard_normal(n), 1200, 7000) * env(n, .005, .08) * 1.2 + lp(rng.standard_normal(n), 300) * env(n, .002, .05) * 2
def pin(): n = int(.15 * SR); return hp(rng.standard_normal(n), 2500) * env(n, .0005, .012) * 1.5 + np.sin(2 * np.pi * 1800 * np.arange(n) / SR) * env(n, .0005, .02) * .4
def key(): n = int(.08 * SR); return bp(rng.standard_normal(n), 1500, 6000) * env(n, .0004, .01) * 1.6 + lp(rng.standard_normal(n), 400) * env(n, .0005, .015)
def pen(d=.5): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 2500, 8000) * (.5 + .5 * np.sin(2 * np.pi * 18 * u)) * np.sin(np.pi * u / d) * .5
def string(d=.7): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 3000, 9000) * np.sin(np.pi * u / d) ** 2 * .35
def rise(d): n = int(d * SR); k = np.linspace(0, 1, n); return bp(rng.standard_normal(n), 300, 3000) * k ** 2 * .5
# karanlık belgesel dronu (D minör, alçak puls)
mus = sum(a * np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .05 * t) * 2) for f, a in [(36.7, .5), (73.4, .45), (110, .25), (146.8, .12), (174.6, .08)])
mus = lp(mus, 700) * (1 + .25 * np.sin(2 * np.pi * .5 * t)) * np.interp(t, [0, 1.0, DUR - .8, DUR], [0, 1, 1, .4])
tick = np.zeros(N)
for s in np.arange(0.5, DUR, 1.0): place(tick, key(), s, .25)
sfx = np.zeros(N)
place(sfx, boom(), 0.0, .7); place(sfx, boom(), 1.84, .5); place(sfx, boom(), 10.46, .45); place(sfx, boom(), 12.88, .4)
for p_ in [3.24, 4.45, 6.2, 10.5]: place(sfx, paper(), p_, .7); place(sfx, pin(), p_ + .32, .6)
for k in range(14): place(sfx, key(), 4.62 + k * .05 + rng.random() * .01, .8)
place(sfx, pen(.55), 4.95, .5); place(sfx, string(), 4.75, .6); place(sfx, string(), 6.95, .6)
place(sfx, pen(.45), 9.86, .5); place(sfx, pen(.35), 12.5, .6); place(sfx, rise(1.2), 9.3, .4); place(sfx, pin(), 13.98, .5)
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'build/voice.mp3', '-t', str(DUR), '-ar', str(SR), '-ac', '1', 'build/vo.wav'], check=True)
vo, _ = sf.read('build/vo.wav'); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .5 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
mix = VO + (mus / np.max(np.abs(mus))) * .16 * duck + tick * .3 * duck + sfx * .5
mix *= np.interp(t, [0, .02, DUR - .35, DUR], [0, 1, 1, 0]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', DUR)
