import numpy as np, soundfile as sf, subprocess, json
from scipy import signal
SR = 44100; DUR = 6942 / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(5)
def lp(x, f): b, a = signal.butter(2, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def hp(x, f): b, a = signal.butter(2, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)
def bp(x, lo, hi): b, a = signal.butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return signal.lfilter(b, a, x)
def place(buf, x, at, g=1.):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
def env(n, a, d): u = np.arange(n) / SR; return np.minimum(1, u / a) * np.exp(-u / d)
def boom(): n = int(3.5 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 38 * u * (1 + .5 * np.exp(-u * 3))) * np.exp(-u * 1.1) + lp(rng.standard_normal(n), 200) * env(n, .003, .25) * .6
def paper(): n = int(.5 * SR); return bp(rng.standard_normal(n), 1200, 7000) * env(n, .005, .08) * 1.2 + lp(rng.standard_normal(n), 300) * env(n, .002, .05) * 2
def pin(): n = int(.15 * SR); return hp(rng.standard_normal(n), 2500) * env(n, .0005, .012) * 1.5
def key(): n = int(.08 * SR); return bp(rng.standard_normal(n), 1500, 6000) * env(n, .0004, .01) * 1.6 + lp(rng.standard_normal(n), 400) * env(n, .0005, .015)
def pen(d=.5): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 2500, 8000) * (.5 + .5 * np.sin(2 * np.pi * 18 * u)) * np.sin(np.pi * u / d) * .5
def string(d=.7): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 3000, 9000) * np.sin(np.pi * u / d) ** 2 * .35
def stamp(): n = int(.6 * SR); return lp(rng.standard_normal(n), 500) * env(n, .001, .06) * 2.5 + boom()[:n] * .4
def air(d=1.0): n = int(d * SR); k = np.linspace(0, 1, n); return bp(rng.standard_normal(n), 250, 2500) * np.sin(np.pi * k) ** 2 * .6
def glitch(d): n = int(d * SR); x = rng.standard_normal(n); sq = np.sign(np.sin(2 * np.pi * np.repeat(rng.uniform(80, 900, n // 400 + 1), 400)[:n] * np.arange(n) / SR)); return (bp(x, 800, 6000) * .6 + sq * .25) * (rng.random(n // 600 + 1).repeat(600)[:n] > .35)
def tick_roll(d):  # sayaç tıkırtısı: başta hızlı, sona doğru yavaşlar
    n = int(d * SR); out = np.zeros(n)
    for k in range(40): place(out, key(), d * (1 - (1 - k / 40) ** 2), .5)
    return out
E = json.load(open('build/events.json')); sfx = np.zeros(N)
for st in E['s'][1:]: place(sfx, air(1.0), st - .5, .35)
for g0, g1, pw in E['g']: place(sfx, glitch(g1 - g0 + .05), g0, .45 * pw)
for o in E['o']:
    T, ty = o.get('t0'), o['type']
    if T is None: continue
    if ty in ('polaroid', 'doc', 'tag'): place(sfx, paper(), T, .6); place(sfx, pin(), T + .32, .5)
    if ty == 'band': place(sfx, paper(), T, .35)
    if ty == 'thread': place(sfx, string(), T, .6)
    if ty == 'counter' and (o.get('dur') or 2) > .5: place(sfx, tick_roll(o.get('dur') or 2), T, .5)
    if ty == 'counter': place(sfx, boom()[:int(1.2 * SR)], T + (o.get('dur') or 2), .35)
    if o.get('censorT') is not None: place(sfx, pen(.3), o['censorT'], .6)
    if o.get('key'):
        for k in range(len(o['key'])): place(sfx, key(), o['keyT'] + k * o.get('keyDur', .8) / len(o['key']) + rng.random() * .01, .7)
    for f in ('circleT', 'tStrike'):
        if o.get(f) is not None: place(sfx, pen(.45), o[f], .5)
    if o.get('stamp'): place(sfx, stamp(), o['stamp']['t'], .6)
SH = lambda v: v + 5.598 if v >= 71.742 else v
for b in [SH(x) for x in [0.0, 22.12, 39.62, 61.7, 76.0 - 5.598, 107.36, 162.32, 193.28, 200.14, 202.12]]: place(sfx, boom(), b, .45)
# gergin dron (A minör), son bölümde umut veren major geçiş
base = sum(a * np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .05 * t) * 2) for f, a in [(55, .5), (110, .4), (130.8, .18), (164.8, .12), (220, .06)])
hope = sum(a * np.sin(2 * np.pi * f * t) for f, a in [(55, .45), (110, .35), (138.6, .2), (164.8, .14), (220, .08)])
mix_t = np.clip((t - 184.6) / 6, 0, 1)
mus = lp(base * (1 - mix_t) + hope * mix_t, 800) * (1 + .3 * np.sin(2 * np.pi * .5 * t))
inten = np.interp(t, [0, 21.5, 22.3, 25.5, 41, 61] + [SH(x) for x in [98, 127, 150, 162, 174, 190, 200]] + [211.0, 213.0, DUR - 2, DUR], [1, 1, .15, .9, .8, 1, .9, .8, 1, 1.1, .9, 1.2, 1.3, .7, 1.0, 1.0, .5])
mus = mus * inten * np.interp(t, [0, .6, DUR - 1.5, DUR], [0, 1, 1, 0])
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'build/voice.mp3', '-ar', str(SR), '-ac', '1', 'build/vo.wav'], check=True)
vo, _ = sf.read('build/vo.wav'); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
sk, _ = sf.read('build/sarki/sarki_slow.wav'); sk = sk / np.max(np.abs(sk)) * .88; place(VO, sk, 212.0)
place(sfx, boom(), 212.0 + 13.82 / .92, .5); place(sfx, air(1.2), 211.0, .4)
duck = 1 - .5 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
mix = VO + (mus / np.max(np.abs(mus))) * .17 * duck + sfx * .42
mix *= np.interp(t, [0, .02, DUR - .5, DUR], [0, 1, 1, 0]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', DUR)
