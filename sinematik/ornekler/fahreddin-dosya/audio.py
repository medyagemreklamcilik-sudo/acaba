import numpy as np, soundfile as sf, subprocess, json
from scipy import signal
SR = 44100; DUR = 4316 / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(4)
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
def stamp(): n = int(.6 * SR); return lp(rng.standard_normal(n), 500) * env(n, .001, .06) * 2.5 + boom()[:n] * .4
def air(d=1.0): n = int(d * SR); k = np.linspace(0, 1, n); return bp(rng.standard_normal(n), 250, 2500) * np.sin(np.pi * k) ** 2 * .6
E = json.load(open('build/events.json'))
sfx = np.zeros(N)
for st in E['s'][1:]: place(sfx, air(1.0), st - .5, .35)
for o in E['o']:
    T, ty = o['t0'], o['type']
    if ty in ('polaroid', 'doc', 'tag'): place(sfx, paper(), T, .6); place(sfx, pin(), T + .32, .5)
    if ty == 'band': place(sfx, paper(), T, .35)
    if ty == 'thread': place(sfx, string(), T, .6)
    if ty == 'halftone': place(sfx, air(1.6), max(0, T), .3)
    if ty == 'xmark': place(sfx, pen(.35), T, .6)
    if ty == 'glowdot': place(sfx, pin(), T, .3)
    if o.get('key'):
        for k in range(len(o['key'])): place(sfx, key(), o['keyT'] + k * o.get('keyDur', .8) / len(o['key']) + rng.random() * .01, .7)
    for f in ('circleT', 'crossT', 'tStrike'):
        if o.get(f) is not None: place(sfx, pen(.5), o[f], .5)
    if o.get('stamp'): place(sfx, stamp(), o['stamp']['t'], .6)
for b in [0.0, 1.84, 10.46, 12.88, 24.9, 49.96, 61.44, 74.26, 91.2, 106.26, 110.16, 112.84, 129.88, 133.64, 135.82]: place(sfx, boom(), b, .45)
# karanlık belgesel dronu: D minör; bölümlere göre yoğunluk
mus = sum(a * np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .05 * t) * 2) for f, a in [(36.7, .5), (73.4, .45), (110, .25), (146.8, .12), (174.6, .08), (220, .05)])
inten = np.interp(t, [0, 30, 44, 53, 61, 73, 86, 97, 106, 121, 129, 137, DUR], [.8, .9, .8, 1, 1.1, .8, .7, .9, 1.1, .7, .8, 1.0, .5])
mus = lp(mus, 750) * (1 + .25 * np.sin(2 * np.pi * .5 * t)) * inten * np.interp(t, [0, 1.0, DUR - 1.2, DUR], [0, 1, 1, .3])
tick = np.zeros(N)
for s in np.arange(0.5, DUR, 1.0): place(tick, key(), s, .2)
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'build/voice.mp3', '-t', str(DUR), '-ar', str(SR), '-ac', '1', 'build/vo.wav'], check=True)
vo, _ = sf.read('build/vo.wav'); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .5 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
mix = VO + (mus / np.max(np.abs(mus))) * .16 * duck + tick * .25 * duck + sfx * .45
mix *= np.interp(t, [0, .02, DUR - .5, DUR], [0, 1, 1, 0]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', DUR)
