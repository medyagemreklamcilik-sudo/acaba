# Cariye uzun video · müzik (bölüm bölüm ruh hâli) + SFX + seslendirme miksi
import numpy as np, soundfile as sf, json, re, subprocess, unicodedata
from scipy import signal
SR = 44100
src = open('web/words.js', encoding='utf8').read()
WORDS = json.loads(re.search(r'const WORDS=(\[.*?\]);', src, re.S).group(1)); PT = json.loads(re.search(r'const PT=(\[.*?\]);', src).group(1))
SP, DUR = json.load(open('build/spans.json'))
def norm(s): return re.sub(r'[^\w]', '', s.replace('I', 'ı').replace('İ', 'i').lower()).replace('_', '')
def wt(w, t0=0):
    q = norm(w)
    for x in WORDS:
        if x['s'] >= t0 - .01 and norm(x['w']).startswith(q): return x['s']
    print('MISS', w, t0); return t0
N = int(DUR * SR); t = np.arange(N) / SR
rng = np.random.default_rng(7)
def T(n): return np.arange(n) / SR
def place(buf, x, at, g=1.0):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if 0 <= i < len(buf): buf[i:j] += x[:j - i] * g
def bp(x, lo, hi, o=2): b, a = signal.butter(o, [lo / (SR / 2), min(hi / (SR / 2), .99)], 'band'); return signal.lfilter(b, a, x)
def lp(x, f, o=2): b, a = signal.butter(o, f / (SR / 2), 'low'); return signal.lfilter(b, a, x)
def hp(x, f, o=2): b, a = signal.butter(o, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)
def smooth(keys):  # [(t, v)] -> eğri
    ts, vs = zip(*keys); return np.interp(t, ts, vs)

# ---------- SFX ----------
def whoosh(d=.35):
    n = int(d * SR); x = rng.standard_normal(n); k = np.linspace(0, 1, n)
    return (bp(x, 250, 1200) * (1 - k) + bp(x, 1500, 6000) * k) * np.sin(np.pi * k) ** 1.5 * 1.4
def thud(f0=70, d=.35, g=1):
    n = int(d * SR); tt = T(n); f = f0 * (1 + 1.5 * np.exp(-tt * 30))
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 12) + lp(rng.standard_normal(n), 900) * np.exp(-tt * 40) * .6) * g
def chime(f=1760, d=1.2):
    n = int(d * SR); tt = T(n); return (np.sin(2 * np.pi * f * tt) + .5 * np.sin(2 * np.pi * f * 2.01 * tt) + .3 * np.sin(2 * np.pi * f * 3 * tt)) * np.exp(-tt * 4) * np.minimum(1, tt / .003) * .5
def heartbeat():
    o = np.zeros(int(.8 * SR)); place(o, thud(55, .3, .8), 0); place(o, thud(50, .3, .6), .22); return o
def kilit():
    o = np.zeros(int(1.2 * SR)); n = int(.06 * SR); tt = T(n)
    for k, at in enumerate([0, .18, .5]):
        c = hp(rng.standard_normal(n), 1800) * np.exp(-tt * 70) + np.sin(2 * np.pi * (1400 - k * 300) * tt) * np.exp(-tt * 60) * .6
        place(o, c, at, .9)
    place(o, thud(80, .5, .8), .5); return o
def kirilma():
    n = int(1.0 * SR); tt = T(n); o = hp(rng.standard_normal(n), 2500) * np.exp(-tt * 9) * .8
    for k in range(14):
        f = rng.uniform(2500, 7000); m = int(.25 * SR); u = T(m); place(o, np.sin(2 * np.pi * f * u) * np.exp(-u * rng.uniform(20, 50)) * .35, rng.uniform(0, .35))
    place(o, thud(140, .25, .6), 0); return o
def sikke():
    n = int(.6 * SR); tt = T(n); return sum(np.sin(2 * np.pi * f * tt) * np.exp(-tt * d) for f, d in [(3150, 9), (4480, 12), (6300, 16)]) * .3 * np.minimum(1, tt / .001)
def kagit(d=.5):
    n = int(d * SR); tt = T(n); return bp(rng.standard_normal(n), 1800, 7000) * (.5 + .5 * np.sin(2 * np.pi * 23 * tt)) * np.sin(np.pi * tt / d) * .5
def tik():
    n = int(.05 * SR); tt = T(n); return hp(rng.standard_normal(n), 3000) * np.exp(-tt * 200) * .7 + np.sin(2 * np.pi * 2200 * tt) * np.exp(-tt * 150) * .4
def dalga(d):
    n = int(d * SR); tt = T(n); x = lp(rng.standard_normal(n), 650, 2); return x * (.35 + .65 * np.sin(2 * np.pi * tt / 5.5) ** 2) * .6
def dere(d):
    n = int(d * SR); x = bp(rng.standard_normal(n), 1500, 6000); m = lp(np.abs(rng.standard_normal(n)), 8); return x * (m / m.max()) * 1.2
def rise(d=2.5):
    n = int(d * SR); tt = T(n); return (bp(rng.standard_normal(n), 600, 5000) * (tt / d) ** 2) * .5

sfx = np.zeros(N)
# kesme geçişleri: hafif whoosh (bölüm başları daha güçlü)
for i, (a, b) in enumerate(SP[1:], 1): place(sfx, whoosh(.32), a - .18, .12)
for k in [1, 8, 13, 19, 26, 30, 33, 36, 45, 48]: place(sfx, whoosh(.5), PT[k] - .3, .25)
for k in [8, 13, 19, 26, 30, 33]: place(sfx, chime(880 if k % 2 else 1175, 1.6), PT[k] + .05, .12)  # saat geçişleri
# kanca
place(sfx, thud(45, 1.0, 1.0), 0.05, .35); place(sfx, heartbeat(), wt('güneş') - .2, .45); place(sfx, heartbeat(), wt('kendi') - .3, .5)
place(sfx, thud(40, .8, 1.0), wt('kendi', 8) + .4, .55)
place(sfx, rise(1.0), PT[1] - 1.0, .4); place(sfx, thud(38, 1.4, 1.2), PT[1], .55); place(sfx, chime(1320, 2), PT[1] + .1, .2)
# köy, dere
place(sfx, dere(PT[3] - wt('akşamları', 23)), wt('akşamları', 23), .05)
# alınış
place(sfx, thud(40, 1.4, 1.2), PT[3] + .1, .5)
for k in range(10): place(sfx, thud(75 + (k % 3) * 8, .14, .5), PT[3] + .8 + k * .3, .22)
place(sfx, thud(35, 1.2, 1.3), wt('cariyelik', 37), .6)
# gemi, satış, kapı kilidi
place(sfx, dalga(wt('gemi', 60) - PT[4]), PT[4], .22)
place(sfx, thud(55, .5, .9), wt('satıldın', 57), .5)
place(sfx, kilit(), wt('kapısında', 57) - .1, .5)
place(sfx, thud(45, .8, 1.0), wt('insanların', 69), .45)
# isim
place(sfx, kagit(.4), wt('mariam', 84) + .05, .4); place(sfx, chime(1568, 1.5), wt('gülnihal', 82), .2)
for k in range(6): place(sfx, tik(), PT[7] + .25 + k * .35, .4)
# şafak
for w in ['acemi', 'cariye', 'kalfa', 'usta', 'haznedar']: place(sfx, thud(120, .18, .5), wt(w, PT[11]), .35)
place(sfx, thud(50, .6, .9), PT[12], .4)
# sabah
place(sfx, thud(40, .9, 1.0), wt('padişah', PT[13] + 8), .5)
place(sfx, thud(40, .9, 1.0), wt('cariyeydi', PT[14]), .55); place(sfx, chime(1175, 2), wt('cariyeydi', PT[14]) + .1, .18)
for k in range(3): place(sfx, kagit(.35), PT[18] + 1 + k * 2.4, .3)
# öğle
for k in range(6): place(sfx, sikke(), wt('ulufe', PT[23]) - 1.5 + .9 + k * .25 + 0.0, .35)
# ikindi: fincan
td = wt('fincan', PT[27]); place(sfx, rise(1.6), td, .35); place(sfx, kirilma(), td + 1.6, .9)
place(sfx, heartbeat(), wt('herkes', PT[27]), .5); place(sfx, heartbeat(), wt('herkes', PT[27]) + 1, .5)
for k in range(int((PT[29] - PT[28]) * 2)): place(sfx, tik(), PT[28] + k * .5, .3)
place(sfx, thud(38, 1.0, 1.1), wt('bu', PT[29] + 3), .5); place(sfx, thud(40, .8, 1.0), wt('düşmanını', PT[29]), .55)
# akşam
for w in ['gözde', 'ikbal', 'haseki', 'valide']: place(sfx, thud(110, .2, .5), wt(w, PT[30]), .35); place(sfx, chime(1046, 1), wt(w, PT[30]), .1)
place(sfx, thud(40, .9, 1.0), wt('istisnaydı', PT[31]), .5); place(sfx, thud(38, 1.0, 1.1), wt('efsane', PT[32]), .6)
# gece, yıllar
place(sfx, kagit(.6), wt('yastığının', PT[33]), .3)
for k in range(9): place(sfx, kagit(.3), PT[36] + k * .7, .2)
place(sfx, thud(45, .8, 1.0), wt('kalfa', PT[37]), .45)
for w in ['birincisi', 'ikincisi', 'üçüncüsü']: place(sfx, thud(90, .3, .6), wt(w, PT[39]), .4)
place(sfx, kilit(), wt('çeyiz', PT[40]), .25); place(sfx, chime(1568, 1.5), wt('çeyiz', PT[40]) + .3, .15)
for k in range(4): place(sfx, kagit(.4), PT[43] + k * 2.4, .3)
# final
place(sfx, dalga(wt('artık', PT[45]) - PT[45]), PT[45], .2)
for w in ['evi', 'odası']: place(sfx, chime(1318, 1.2), wt(w, PT[45] + 3), .2)
place(sfx, chime(1760, 2.5), wt('kendisi', PT[45]), .2)
place(sfx, chime(1046, 3), wt('uzatıyor', PT[46]), .18)
place(sfx, thud(35, 1.6, 1.3), wt('kadar', PT[48]) - .1, .55)
place(sfx, thud(45, .9, 1.0), wt('kimi', PT[48]), .4)
for w in ['sarayın', 'özgürlüğünü']: place(sfx, thud(100, .25, .6), wt(w, PT[50]), .35)
place(sfx, chime(1318, 3), wt('yorumlara', PT[50]), .2)

# ---------- MÜZİK: D hicaz modunda dron + pad + ud-vari pluck ----------
def hz(semi): return 146.83 * 2 ** (semi / 12)   # D3
HICAZ = [0, 1, 4, 5, 7, 8, 10, 12]; PENT = [0, 2, 4, 7, 9, 12]
def pad(semis, amp):
    x = np.zeros(N)
    for s in semis:
        f = hz(s); x += np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .13 * t) * 2) + .5 * np.sin(2 * np.pi * f * 1.003 * t) + .25 * np.sin(2 * np.pi * f * 2 * t)
    return lp(x, 1400) * amp
def pluck_note(f, d=1.6):
    n = int(d * SR); p = max(2, int(SR / f)); buf = rng.uniform(-1, 1, p); o = np.empty(n)
    for i in range(n): j = i % p; o[i] = buf[j]; buf[j] = .5 * (buf[j] + buf[(j + 1) % p]) * .996
    return lp(o, 3500) * np.minimum(1, T(n) / .002)
cache = {}
def pl(semi):
    if semi not in cache: cache[semi] = pluck_note(hz(semi))
    return cache[semi]
# bölüm planı: (başlangıç, mod, yoğunluk 0..1, parlaklık)
SEC = [(0, 'dark', 0, 0), (PT[1], 'hicaz', .35, 1), (PT[2], 'pent', .7, 1), (PT[3], 'dark', 0, 0), (PT[4], 'dark', .1, 0), (PT[5], 'hicaz', .3, 0),
       (PT[8], 'hicaz', .25, 0), (PT[13], 'hicaz', .55, 1), (PT[19], 'hicaz', .7, 1), (PT[26], 'tense', .2, 0), (PT[30], 'hicaz', .6, 1),
       (PT[33], 'hicaz', .15, 0), (PT[36], 'pent', .45, 1), (PT[42], 'hicaz', .3, 0), (PT[45], 'pent', .7, 1), (PT[48], 'dark', .15, 0),
       (PT[49], 'hicaz', .4, 1), (PT[50], 'pent', .5, 1), (DUR, 'end', 0, 0)]
mus = np.zeros(N)
drone = np.sin(2 * np.pi * 73.4 * t) * .6 + np.sin(2 * np.pi * 110 * t) * .3 + .2 * np.sign(np.sin(2 * np.pi * 73.6 * t))
drone = lp(drone, 500) * (.7 + .3 * np.sin(2 * np.pi * t / 9))
mus += drone * .5
hic = pad([0, 7, 13], .12); pen = pad([0, 4, 9], .12); dark = pad([-12, -5, 1], .14)
wH = np.zeros(N); wP = np.zeros(N); wD = np.zeros(N); wT = np.zeros(N)
for (a, m, dens, br), (b, *_r) in zip(SEC[:-1], SEC[1:]):
    i, j = int(a * SR), int(b * SR)
    {'hicaz': wH, 'pent': wP, 'dark': wD, 'tense': wT}[m][i:j] = 1
    # pluck melodisi
    scale = PENT if m == 'pent' else HICAZ
    if dens > 0:
        step = lerp = None; k = a + .5; prev = 3
        while k < b - 1:
            prev = int(np.clip(prev + rng.integers(-2, 3), 0, len(scale) - 1)); semi = scale[prev] + (12 if br and rng.random() < .3 else 0)
            place(mus, pl(semi), k, .22 * (.6 + .4 * rng.random()))
            if rng.random() < .25: place(mus, pl(scale[max(0, prev - 2)]), k + .25, .12)
            k += (60 / 76) * (2 if dens < .3 else 1 if dens < .6 else .5) * rng.choice([1, 1, 2])
# geçişleri yumuşat
for w in (wH, wP, wD, wT): w[:] = lp(w, 1.5, 1)
tense = lp(np.sin(2 * np.pi * 73.4 * 1.5 * t) * (np.sin(2 * np.pi * 2 * t) > .7), 600) * .3
mus += hic * wH + pen * wP + dark * wD * 1.2 + (dark * .8 + tense) * wT
# davul nabzı (kanca + ikindi)
for k in np.arange(PT[26], PT[30], 60 / 76): place(mus, thud(60, .25, .5), k, .25)
mus *= smooth([(0, 0), (.6, 1), (DUR - 3, 1), (DUR, 0)])
mus /= np.max(np.abs(mus))

# ---------- MİKS ----------
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'build/voice.mp3', '-ac', '1', '-ar', str(SR), 'audio/vo.wav'], check=True)
vo, _ = sf.read('audio/vo.wav'); vo = hp(vo, 80)
e = lp(np.abs(signal.hilbert(vo)), 20); vo = vo * np.where(e > .15, (.15 / np.maximum(e, 1e-6)) ** .4, 1.0); vo = vo / np.max(np.abs(vo)) * .9
VO = np.zeros(N); VO[:min(N, len(vo))] = vo[:N]
duck = 1 - .6 * np.clip(lp(np.abs(VO), 5) / .05, 0, 1)
end = smooth([(0, 1), (PT[50] + 10.6, 1), (PT[50] + 11.5, 1.8), (DUR, 1.8)])  # konuşma bitince müzik yükselir (end screen)
mix = VO + mus * .16 * duck * end + sfx * .6
mix *= smooth([(0, 1), (DUR - 1.5, 1), (DUR, 0)])
mix = mix / np.max(np.abs(mix)) * .89
sf.write('audio/mix.wav', np.stack([mix, mix], 1), SR)
print('ok', DUR, 'rms dB', 20 * np.log10(np.sqrt(np.mean(mix ** 2))))
