import numpy as np, soundfile as sf, json
from scipy import signal
SR = 44100
import json as _j, os as _os
WARP = _j.load(open('audio/warp.json')) if _os.path.exists('audio/warp.json') else None
def toNew(x):
    if not WARP: return x
    A = WARP['anchors']
    if x <= A[0][0]: return x - A[0][0] + A[0][1]
    for i in range(len(A) - 1):
        if x <= A[i + 1][0]: k = (x - A[i][0]) / (A[i + 1][0] - A[i][0]); return A[i][1] + k * (A[i + 1][1] - A[i][1])
    return x - A[-1][0] + A[-1][1]
DUR = 79.6
N = int(DUR * SR)
rng = np.random.default_rng(3)
def T(n): return np.arange(n) / SR
def env(n, a=.005, d=.2, curve=4):
    t = T(n); e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) * curve / max(d, 1e-4)); return e
def place(buf, x, at, g=1.0):
    i = int(toNew(at) * SR); j = min(len(buf), i + len(x))
    if i < 0 or i >= len(buf): return
    buf[i:j] += x[:j - i] * g
def bp(x, lo, hi, order=2):
    b, a = signal.butter(order, [lo / (SR / 2), min(hi / (SR / 2), .99)], 'band'); return signal.lfilter(b, a, x)
def lp(x, f, order=2):
    b, a = signal.butter(order, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def hp(x, f, order=2):
    b, a = signal.butter(order, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)

# ---------------- SFX ----------------
def whoosh(dur=.35, up=True):
    n = int(dur * SR); x = rng.standard_normal(n); t = T(n)
    lo, hi = bp(x, 250, 1200), bp(x, 1500, 6000); k = np.linspace(0, 1, n) if up else np.linspace(1, 0, n)
    e = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.5
    return (lo * (1 - k) + hi * k) * e * 1.6
def thud(f0=70, dur=.35, g=1):
    n = int(dur * SR); t = T(n); f = f0 * (1 + 1.5 * np.exp(-t * 30))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 12)
    x += lp(rng.standard_normal(n), 900) * np.exp(-t * 40) * .6
    return x * g
def clang(f0=520, dur=1.0):
    n = int(dur * SR); t = T(n); x = np.zeros(n)
    for k, (r, a, d) in enumerate([(1, 1, 5), (2.76, .6, 7), (5.4, .4, 10), (8.9, .25, 14), (1.5, .5, 6)]):
        x += a * np.sin(2 * np.pi * f0 * r * t + k) * np.exp(-t * d)
    x += hp(rng.standard_normal(n), 2000) * np.exp(-t * 60) * .8
    return x * .5 + thud(90, dur, .7)[:n]
def pluck(f, dur=.5, bright=.5):
    n = int(dur * SR); p = int(SR / f); buf = rng.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = bright * buf[i % p] + (1 - bright) * .5 * (buf[i % p] + buf[(i + 1) % p]) * .996 if False else .5 * (buf[i % p] + buf[(i + 1) % p]) * .995
    return out
def chime(f=1760, dur=.8):
    n = int(dur * SR); t = T(n)
    return (np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.01 * t) + .3 * np.sin(2 * np.pi * f * 3 * t)) * np.exp(-t * 6) * np.minimum(1, t / .003) * .5
def sparkle_sfx():
    out = np.zeros(int(.7 * SR))
    for i, f in enumerate([2093, 2637, 3136, 4186]): place(out, chime(f, .5) * .5, i * .05)
    return out
def tick(): n = int(.04 * SR); t = T(n); return hp(rng.standard_normal(n), 3000) * np.exp(-t * 200) * .8 + np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 150) * .4
def pop(f=600):
    n = int(.12 * SR); t = T(n); fr = f * (1 + 2 * t * 10); return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t * 40)
def boing(f=220, dur=.5):
    n = int(dur * SR); t = T(n); fr = f * (1 + .35 * np.sin(2 * np.pi * 9 * t) * np.exp(-t * 3)) * (1 + t)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t * 5) * .6
def tweet():
    out = np.zeros(int(1.2 * SR))
    for i in range(4):
        n = int(.1 * SR); t = T(n); fr = 3200 + 900 * np.sin(2 * np.pi * 30 * t)
        place(out, np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.sin(np.pi * t / .1) * .25, i * .25)
    return out
def scribble(dur=.18):
    n = int(dur * SR); t = T(n); return bp(rng.standard_normal(n), 1500, 6000) * (0.5 + .5 * np.sin(2 * np.pi * 30 * t)) * np.sin(np.pi * t / dur) * .5
def riser(dur=2.8):
    n = int(dur * SR); t = T(n); f = 200 * (2 ** (t / dur * 2.5))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * .3 + bp(rng.standard_normal(n), 800, 5000) * .3 * (t / dur)
    return x * (t / dur) ** 2
def waves(dur):
    n = int(dur * SR); t = T(n); x = lp(rng.standard_normal(n), 700, 2)
    return x * (0.5 + .5 * np.sin(2 * np.pi * t / 4.5) ** 2) * .5
def heartbeat():
    out = np.zeros(int(.8 * SR)); place(out, thud(55, .3, .8), 0); place(out, thud(50, .3, .6), .22); return out
sfx = np.zeros(N)
def gok(dur=1.6):
    n = int(dur * SR); t = T(n); return lp(rng.standard_normal(n), 400) * (np.exp(-t * 2.2) + .6 * np.exp(-((t - .25) ** 2) / .01)) * 2.5
for w in [1.18, 3.9, 8.4, 12.5, 17.3, 20.2, 24.3, 28.6, 31.9, 35.2, 38.1, 40.9, 44.8, 59.9, 66.6, 70.9]: place(sfx, whoosh(.36), w - .2, .3)
place(sfx, thud(45, 1.0, 1.0), 0.0, .45); place(sfx, gok(), 0.66, .6)
place(sfx, heartbeat(), 1.6, .45); place(sfx, heartbeat(), 2.5, .5)
place(sfx, clang(900, .9) * .6, 5.0, .3); place(sfx, thud(40, 1.3, 1.3), 6.8, .9); place(sfx, clang(160, 1.5), 6.8, .4)
place(sfx, sparkle_sfx(), 8.5, .3)
place(sfx, thud(60, .5, .8), 12.6, .5); place(sfx, boing(260, .4), 17.5, .3); place(sfx, pop(520), 18.4, .3); place(sfx, pop(640), 18.5, .3)
place(sfx, chime(1320, .8), 25.2, .2); place(sfx, thud(110, .2, .5), 26.25, .3); place(sfx, clang(700, .6), 27.8, .3)
place(sfx, thud(50, .8, 1.0), 36.25, .6); place(sfx, chime(1100, 1.0), 34.0, .2)
place(sfx, gok(2.0), 38.2, .35); place(sfx, thud(55, .5, .8), 41.0, .5)
for k in range(8): place(sfx, thud(80 + (k % 3) * 10, .15, .5), 41.2 + k * .35, .25)
place(sfx, heartbeat(), 45.5, .5); place(sfx, heartbeat(), 46.6, .55); place(sfx, boing(420, .3), 47.9, .35)
place(sfx, thud(40, 1.0, 1.2), 49.8, .7)
for k in range(10): place(sfx, thud(70, .12, .5), 51.1 + k * .38, .3)
place(sfx, thud(35, 1.6, 1.4), 55.0, .8); place(sfx, gok(2.5), 55.2, .5)
for k in range(10): place(sfx, tick() * .5, 57.4 + k * .09)
place(sfx, sparkle_sfx(), 62.3, .3); place(sfx, thud(50, .6, .9), 68.6, .6); place(sfx, gok(), 68.7, .4)
place(sfx, pop(560), 71.6, .35); place(sfx, pop(480), 72.6, .35); place(sfx, pop(700), 73.5, .3)
place(sfx, sparkle_sfx(), 75.1, .35); place(sfx, pop(620), 76.1, .35)
t = T(N); music = np.zeros(N)
for f, a in [(55, .5), (82.4, .35), (110, .25), (130.8, .18)]: music += a * np.sin(2 * np.pi * f * t) + a * .25 * np.sign(np.sin(2 * np.pi * f * 1.002 * t))
puls = .6 + .4 * (np.sin(2 * np.pi * t * 1.0) > .9)
music = lp(music, 700) * np.clip(t / .8, 0, 1) * puls
music *= np.where((t > 8.4) & (t < 12.5), .5, 1) * np.where(t > 75, .5, 1)
music /= np.max(np.abs(music))
# ---------------- VO + mix ----------------
vo, vsr = sf.read('audio/vo.wav')
if vo.ndim > 1: vo = vo.mean(1)
vo = signal.resample_poly(vo, SR, vsr)
vo = hp(vo, 90)
# gentle compression
envv = np.abs(signal.hilbert(vo)); envv = lp(envv, 20)
gain = np.where(envv > .15, (.15 / np.maximum(envv, 1e-6)) ** .4, 1.0); vo = vo * gain
vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
# duck music under VO
venv = lp(np.abs(VO), 6); vtrack = np.clip(venv / .05, 0, 1)
duck = 1 - .55 * vtrack
mixL = VO * 1.0 + music * .22 * duck + sfx * .7
mixR = mixL.copy()
out = np.stack([mixL, mixR], 1)
fade = np.ones(N); fl = int(.5 * SR); fade[-fl:] = np.linspace(1, 0, fl); out *= fade[:, None]
pk = np.max(np.abs(out)); out = out / pk * .89
sf.write('audio/mix.wav', out, SR)
print('done', out.shape, 'rms dB', 20 * np.log10(np.sqrt(np.mean(out ** 2))))
