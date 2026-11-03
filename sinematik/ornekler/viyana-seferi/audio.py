# Belgesel ses tasarımı: dron + savaş davulu, Tuna suyu, gök gürültüsü + yağmur (slow-mo'da boğuk), kuşatma vuruşu, kar rüzgârı
import numpy as np, soundfile as sf
from scipy import signal
SR = 44100; DUR = 568 / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(9)
def lp(x, f, o=2): b, a = signal.butter(o, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def hp(x, f, o=2): b, a = signal.butter(o, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)
def bp(x, lo, hi): b, a = signal.butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return signal.lfilter(b, a, x)
def place(buf, x, at, g=1.):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
env = lambda pts: np.interp(t, [p[0] for p in pts], [p[1] for p in pts])
def drum(f0=55, d=.9, g=1.):
    n = int(d * SR); u = np.arange(n) / SR; f = f0 * (1 + 1.2 * np.exp(-u * 18))
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-u * 5) + lp(rng.standard_normal(n), 500) * np.exp(-u * 30) * .5) * g
def braam(d=3.5):
    n = int(d * SR); u = np.arange(n) / SR; x = sum(np.sign(np.sin(2 * np.pi * f * u)) * a for f, a in [(36.7, .6), (55, .4), (73.4, .25), (36.9, .3)])
    return lp(x, 380) * np.minimum(1, u / .05) * np.exp(-u * .7) * .8
def thunder(d=3.0):
    n = int(d * SR); u = np.arange(n) / SR; x = lp(rng.standard_normal(n), 220, 3) * (np.exp(-u * 1.4) + .5 * np.exp(-((u - .35) ** 2) / .02)) * 3
    return x + hp(rng.standard_normal(n), 2000) * np.exp(-u * 25) * .4
def boom(): n = int(2.2 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 38 * u * (1 + .5 * np.exp(-u * 4))) * np.exp(-u * 2.2) + lp(rng.standard_normal(n), 300) * np.exp(-u * 6) * .6
def whoosh(d=1.1): n = int(d * SR); k = np.linspace(0, 1, n); x = rng.standard_normal(n); return (bp(x, 150, 700) * (1 - k) + bp(x, 700, 3500) * k) * np.sin(np.pi * k) ** 2 * 1.1
def tick(): n = int(.25 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 1760 * u) * np.exp(-u * 30) * .3 + hp(rng.standard_normal(n), 3000) * np.exp(-u * 80) * .3
# dron: D frig / hicaz renkli koyu pad
pad = sum(a * np.sin(2 * np.pi * f * t + 2 * np.sin(2 * np.pi * .05 * t + f)) for f, a in [(73.4, .5), (77.8, .12), (110, .3), (146.8, .18), (155.6, .06), (220, .07)])
pad = lp(pad, 1100) * env([(0, .0), (.8, 1), (8, 1), (9.2, .6), (12, .7), (13.4, 1.1), (16.5, .8), (DUR - .6, .9), (DUR, 0)])
# davul: yürüyüş (0-8 sn), kuşatmada yoğun
dr = np.zeros(N)
for k, bt in enumerate(np.arange(.0, 8.0, .48)): place(dr, drum(52 if k % 2 == 0 else 70, .8, 1 if k % 4 == 0 else .55), bt)
for k, bt in enumerate(np.arange(12.2, 15.3, .32)): place(dr, drum(60, .6, .7 if k % 2 else 1), bt)
sfx = np.zeros(N)
place(sfx, braam(4), 0.0, .6); place(sfx, tick(), 1.3, .6)
place(sfx, whoosh(1.2), 2.4, .3); place(sfx, whoosh(1.2), 11.8, .35)
# Tuna: su + kürek + gıcırtı
water = bp(rng.standard_normal(N), 300, 1800) * (.6 + .4 * np.sin(2 * np.pi * t * .35)) * env([(4.6, 0), (5.2, 1), (8.3, 1), (8.9, 0)]) * .18
for k, bt in enumerate(np.arange(5.0, 8.4, .7)): place(sfx, bp(rng.standard_normal(int(.3 * SR)), 400, 1500) * np.hanning(int(.3 * SR)) * .4, bt)
# yağmur + gök gürültüsü (slow-mo boyunca boğuk)
rain_raw = bp(rng.standard_normal(N), 900, 9000); rain_slow = lp(rain_raw, 1400)
slo = env([(9.0, 0), (9.5, 1), (11.2, 1), (11.7, 0)])
rain = (rain_raw * (1 - slo) + rain_slow * slo * 1.6) * env([(8.5, 0), (9.2, .9), (12.0, .9), (12.6, 0)]) * .22
place(sfx, thunder(3.2), 9.22, .9); place(sfx, thunder(2.5), 10.7, .6)
place(sfx, lp(rng.standard_normal(int(1.2 * SR)), 180) * np.hanning(int(1.2 * SR)) * 1.5, 10.68, .7)   # çamur
# kuşatma
place(sfx, braam(4.5), 13.42, .9); place(sfx, boom(), 13.6, .5); place(sfx, boom(), 14.3, .35); place(sfx, boom(), 14.9, .3)
# kar: rüzgâr uğultusu, sessizleşen dünya
wind = bp(rng.standard_normal(N), 180, 1400) * (.55 + .45 * np.sin(2 * np.pi * t * .23) * np.sin(2 * np.pi * t * .61)) * env([(16.2, 0), (17.0, 1), (DUR, 1)]) * .3
place(sfx, braam(3), 18.04, .5)
vo, sr = sf.read('build/vo.wav'); vo = vo if vo.ndim == 1 else vo.mean(1); vo = hp(vo, 70); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .55 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
bed = (pad / np.max(np.abs(pad))) * .16 + dr * .22 + water + rain + wind
mix = VO + bed * duck + sfx * .5 * (1 - .3 * (duck < .7))
mix *= env([(0, 0), (.02, 1), (DUR - .4, 1), (DUR, 0)]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', round(DUR, 3))
