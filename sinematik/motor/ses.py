import numpy as np, soundfile as sf, subprocess, json, os, sys
from scipy import signal
# Sinematik dosya sesi (genel): python3 sinematik/motor/ses.py <klasör> → <klasör>/build/mix.wav
# Re minör dron + seyrek piyano; kâğıt/raptiye/ip/daktilo/damga efektleri sahnedeki nesnelerden (build/events.json);
# GLITCH anlarında alçak gümleme (sahne glitch=[...] ile silah sesi istenirse SHOT=1 ortam değişkeni).
os.chdir(os.path.abspath(sys.argv[1]))
E = json.load(open('build/events.json'))
SR = 44100; DUR = round(E['end'] * 30) / 30; N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(7)
def lp(x, f): b, a = signal.butter(2, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def hp(x, f): b, a = signal.butter(2, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)
def bp(x, lo, hi): b, a = signal.butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return signal.lfilter(b, a, x)
def place(buf, x, at, g=1.):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
def env(n, a, d): u = np.arange(n) / SR; return np.minimum(1, u / a) * np.exp(-u / d)
def boom(): n = int(3.5 * SR); u = np.arange(n) / SR; return np.sin(2 * np.pi * 38 * u * (1 + .5 * np.exp(-u * 3))) * np.exp(-u * 1.1) + lp(rng.standard_normal(n), 200) * env(n, .003, .25) * .6
def shot():  # tabanca: keskin çatlama + oda yankısı + alçak gümleme
    n = int(2.5 * SR); u = np.arange(n) / SR; x = hp(rng.standard_normal(n), 900) * env(n, .0003, .018) * 3
    x += lp(rng.standard_normal(n), 1800) * env(n, .001, .09) * 1.6
    for d, g in [(.045, .5), (.11, .35), (.19, .22), (.3, .14)]: x[int(d * SR):] += x[:n - int(d * SR)] * g * .6
    return x + boom()[:n] * .7
def paper(): n = int(.5 * SR); return bp(rng.standard_normal(n), 1200, 7000) * env(n, .005, .08) * 1.2 + lp(rng.standard_normal(n), 300) * env(n, .002, .05) * 2
def pin(): n = int(.15 * SR); return hp(rng.standard_normal(n), 2500) * env(n, .0005, .012) * 1.5
def key(): n = int(.08 * SR); return bp(rng.standard_normal(n), 1500, 6000) * env(n, .0004, .01) * 1.6 + lp(rng.standard_normal(n), 400) * env(n, .0005, .015)
def pen(d=.5): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 2500, 8000) * (.5 + .5 * np.sin(2 * np.pi * 18 * u)) * np.sin(np.pi * u / d) * .5
def string(d=.7): n = int(d * SR); u = np.arange(n) / SR; return bp(rng.standard_normal(n), 3000, 9000) * np.sin(np.pi * u / d) ** 2 * .35
def stamp(): n = int(.6 * SR); return lp(rng.standard_normal(n), 500) * env(n, .001, .06) * 2.5 + boom()[:n] * .4
def air(d=1.0): n = int(d * SR); k = np.linspace(0, 1, n); return bp(rng.standard_normal(n), 250, 2500) * np.sin(np.pi * k) ** 2 * .6
def tick_roll(d):
    n = int(d * SR); out = np.zeros(n)
    for k in range(30): place(out, key(), d * (1 - (1 - k / 30) ** 2), .5)
    return out
def clock():  # saat tiktakları (10 Kasım koridoru)
    n = int(.06 * SR); return bp(rng.standard_normal(n), 2000, 7000) * env(n, .0003, .006) * 1.2
sfx = np.zeros(N)
for st, kd in zip(E['s'][1:], E['kinds'][1:]): place(sfx, air(1.0), st - .2, .3)
for o in E['o']:
    T, ty = o.get('t0'), o['type']
    if T is None or T < 0: continue
    if ty in ('polaroid', 'doc', 'tag'): place(sfx, paper(), T, .6); place(sfx, pin(), T + .32, .5)
    if ty == 'band': place(sfx, paper(), T, .3)
    if ty == 'thread': place(sfx, string(), T, .6)
    if ty == 'counter' and (o.get('dur') or 2) > .5: place(sfx, tick_roll(o.get('dur') or 2), T, .45)
    if ty == 'counter': place(sfx, boom()[:int(1.2 * SR)], T + (o.get('dur') or 2), .3)
    if ty == 'route': place(sfx, air(1.4), T, .35)
    if o.get('key'):
        for k in range(len(o['key'])): place(sfx, key(), o['keyT'] + k * o.get('keyDur', .8) / len(o['key']) + rng.random() * .01, .6)
    for f in ('circleT', 'tStrike', 'crossT'):
        if o.get(f) is not None: place(sfx, pen(.45), o[f], .5)
    if o.get('stamp'): place(sfx, stamp(), o['stamp']['t'], .6)
for b in E['b']: place(sfx, boom(), b, .45)
for g0, g1, pw in E['g']: place(sfx, shot() if os.environ.get('SHOT') else boom()[:int(1.5 * SR)], g0, .9 if os.environ.get('SHOT') else .4)
# müzik: re minör dron, akor değişimleri; seyrek piyano melodisi
chords = [[73.4, 146.8, 174.6, 220.0], [58.3, 116.5, 174.6, 233.1], [65.4, 130.8, 164.8, 196.0], [55.0, 110.0, 164.8, 220.0]]
mus = np.zeros(N); L = 8.0
for i, c0 in enumerate(np.arange(0, DUR, L)):
    ch = chords[i % 4]; n = int((L + 3) * SR); u = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * u + np.sin(2 * np.pi * .07 * u) * 1.5) for f, a in zip(ch, [.5, .35, .2, .14]))
    x *= np.minimum(1, u / 2.5) * np.minimum(1, np.maximum(0, (L + 3 - u) / 3))
    place(mus, x, c0, 1)
mus = lp(mus, 900)
pia = np.zeros(N); notes = [293.7, 349.2, 440.0, 392.0, 349.2, 329.6, 293.7, 261.6, 293.7, 220.0]
for i, tt in enumerate(np.arange(6, DUR - 4, 3.2)):
    f = notes[i % len(notes)]; n = int(3.0 * SR); u = np.arange(n) / SR
    tone = (np.sin(2 * np.pi * f * u) + .3 * np.sin(2 * np.pi * 2 * f * u) + .1 * np.sin(2 * np.pi * 3 * f * u)) * np.exp(-u * 1.3) * np.minimum(1, u / .008)
    place(pia, tone, tt, .5)
pia = lp(pia, 2600)
# yoğunluk: kanca güçlü, sıcak bölümlerde yumuşak, 10 Kasım'da sessizleşip silahla kopar, kapanışta yükselir
inten = np.interp(t, [0, 2, 5, DUR * .35, DUR * .45, DUR * .7, DUR - 8, DUR - 2, DUR], [1.1, 1.1, .75, .85, .7, .9, .75, .95, .4])
mus = mus / np.max(np.abs(mus)) * inten * np.interp(t, [0, .5, DUR - 2, DUR], [0, 1, 1, 0])
pia = pia / np.max(np.abs(pia)) * inten
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'build/voice.mp3', '-ar', str(SR), '-ac', '1', 'build/vo.wav'], check=True)
vo, _ = sf.read('build/vo.wav'); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .5 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
mix = VO + mus * .16 * duck + pia * .09 * (.5 + .5 * duck) + sfx * .4
mix *= np.interp(t, [0, .02, DUR - .5, DUR], [0, 1, 1, 0]); mix = mix / np.max(np.abs(mix)) * .89
sf.write('build/mix.wav', np.stack([mix, mix], 1), SR); print('ok', DUR)
