# Seslendirme + sessiz sinematik alt katman (dron, kâğıt, kalem, yağmur, rüzgâr)
import numpy as np, soundfile as sf
from scipy import signal
SR = 44100; DUR = 449 / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(4)
def lp(x, f): b, a = signal.butter(2, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def bp(x, lo, hi): b, a = signal.butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return signal.lfilter(b, a, x)
def place(buf, x, at, g=1.):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
def env(n, a, d): u = np.arange(n) / SR; return np.minimum(1, u / a) * np.exp(-u / d)
def whoosh(d=.9):
    n = int(d * SR); k = np.linspace(0, 1, n); x = rng.standard_normal(n)
    return (bp(x, 200, 900) * (1 - k) + bp(x, 900, 4000) * k) * np.sin(np.pi * k) ** 2 * 1.2
def paper(): n = int(.5 * SR); return bp(rng.standard_normal(n), 1200, 7000) * env(n, .005, .08) * 1.2 + lp(rng.standard_normal(n), 300) * env(n, .002, .05) * 2
def pen(d=.55): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 2500, 8000) * (.5 + .5 * np.sin(2 * np.pi * 18 * u)) * np.sin(np.pi * u / d) * .5
def boom(): n = int(2.5 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 42 * u * (1 + .4 * np.exp(-u * 3))) * np.exp(-u * 1.6) * .9
# dron: D minör, yavaş nefes alan pad
mus = sum(a * np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .07 * t) * 2) for f, a in [(73.4, .5), (110, .3), (146.8, .2), (174.6, .12), (220, .08)])
mus = lp(mus, 900) * (0.55 + .45 * np.sin(2 * np.pi * t / 7.5 - 1.2) ** 2)
mus *= np.interp(t, [0, 1.2, DUR - 1.5, DUR], [0, 1, 1, .2])
sfx = np.zeros(N)
place(sfx, boom(), 0.0, .6)
for w in [2.3, 3.6, 5.8, 7.0, 10.6]: place(sfx, whoosh(1.0), w - .3, .22)
place(sfx, pen(.7), 4.17, .25); place(sfx, pen(.6), 5.74, .25); place(sfx, pen(.6), 6.72, .25); place(sfx, pen(.55), 8.98, .5); place(sfx, pen(.6), 10.9, .25)
place(sfx, boom(), 8.98, .35)
place(sfx, paper(), 12.6, .7)
rain = bp(rng.standard_normal(N), 1500, 9000) * np.interp(t, [13.2, 13.7, 14.0, 14.5], [0, 1, 1, .25]) * .25
wind = bp(rng.standard_normal(N), 200, 1200) * (0.6 + .4 * np.sin(2 * np.pi * t * .7)) * np.interp(t, [13.9, 14.4, DUR], [0, 1, 1]) * .35
vo, sr = sf.read('build/vo.wav'); vo = vo if vo.ndim == 1 else vo.mean(1); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .5 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
mix = VO + (mus / np.max(np.abs(mus))) * .14 * duck + sfx * .5 + rain + wind
mix *= np.interp(t, [0, .02, DUR - .3, DUR], [0, 1, 1, 0]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', DUR)
