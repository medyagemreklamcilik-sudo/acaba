"""Synthesises the background score and sound effects for the video.

Everything is generated procedurally with numpy so there are no licensing
issues: an oud-like Hijaz ostinato (Karplus-Strong), a low drone, frame-drum
percussion and a library of cinematic SFX placed on the scene timeline.
"""
import json, sys
import numpy as np
import wave

SR = 44100
rng = np.random.default_rng(7)


def t_(d):
    return np.arange(int(d * SR)) / SR


def env_exp(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))


def lowpass(x, fc):
    # one-pole low-pass (fast, adequate for noise shaping)
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    # vectorised via lfilter-equivalent recursion using cumulative trick is
    # not exact, so use FFT filtering instead.
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    H = 1 / np.sqrt(1 + (f / fc) ** 4)
    return np.fft.irfft(X * H, len(x))


def bandpass(x, lo, hi):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    H = (1 / np.sqrt(1 + (f / hi) ** 4)) * (1 / np.sqrt(1 + (lo / np.maximum(f, 1)) ** 4))
    return np.fft.irfft(X * H, len(x))


def reverb(x, decay=1.8, mix=0.3):
    n = int(decay * SR)
    ir = rng.standard_normal(n) * np.exp(-np.arange(n) / (decay / 6.9 * SR))
    ir = lowpass(ir, 6000)
    ir /= np.sqrt(np.sum(ir ** 2))
    L = len(x) + n
    y = np.fft.irfft(np.fft.rfft(x, L) * np.fft.rfft(ir, L), L)
    out = np.zeros(L)
    out[: len(x)] += x * (1 - mix)
    out += y * mix
    return out


def norm(x, peak=0.9):
    m = np.max(np.abs(x)) or 1
    return x / m * peak


# ---------------------------------------------------------------- SFX
def sfx_impact():
    d = 3.0
    t = t_(d)
    f = 30 + 60 * np.exp(-t * 8)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(len(t), 0.9)
    click = lowpass(rng.standard_normal(len(t)), 900) * env_exp(len(t), 0.05)
    sub = np.sin(2 * np.pi * 42 * t) * env_exp(len(t), 1.4) * 0.6
    return norm(reverb(body + click * 1.5 + sub, 2.5, 0.25))


def sfx_hit():
    d = 1.2
    t = t_(d)
    f = 50 + 90 * np.exp(-t * 20)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(len(t), 0.25)
    click = bandpass(rng.standard_normal(len(t)), 200, 3000) * env_exp(len(t), 0.02)
    return norm(reverb(body + click, 1.2, 0.2))


def sfx_whoosh(d=0.7, up=True):
    n = int(d * SR)
    x = rng.standard_normal(n)
    out = np.zeros(n)
    # sweep a band through the noise in chunks
    chunks = 24
    for i in range(chunks):
        a, b = i * n // chunks, (i + 1) * n // chunks
        p = i / chunks
        fc = 300 + (4000 if up else 2500) * (p if up else 1 - p)
        seg = bandpass(x, fc * 0.6, fc * 1.6)[a:b]
        out[a:b] = seg
    e = np.sin(np.pi * np.linspace(0, 1, n)) ** 2
    return norm(reverb(out * e, 0.8, 0.2))


def sfx_riser(d=2.2):
    t = t_(d)
    p = t / d
    f = 120 * (2 ** (p * 4))
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.3
    noise = rng.standard_normal(len(t))
    out = np.zeros(len(t))
    chunks = 30
    n = len(t)
    for i in range(chunks):
        a, b = i * n // chunks, (i + 1) * n // chunks
        fc = 400 + 7000 * (i / chunks) ** 2
        out[a:b] = bandpass(noise, fc * 0.5, fc * 1.5)[a:b]
    e = p ** 2.2
    return norm((tone + out * 0.8) * e)


def sfx_reverse_cymbal(d=1.6):
    n = int(d * SR)
    x = bandpass(rng.standard_normal(n), 3000, 14000) * env_exp(n, 0.5)
    return norm(x[::-1])


def sfx_bell():
    d = 4.0
    t = t_(d)
    out = np.zeros(len(t))
    for ratio, amp, tau in [(1, 1, 2.5), (2.0, 0.6, 1.8), (2.76, 0.5, 1.2), (5.4, 0.3, 0.6), (8.9, 0.2, 0.3)]:
        out += amp * np.sin(2 * np.pi * 196 * ratio * t) * env_exp(len(t), tau)
    return norm(reverb(out, 3.0, 0.35))


def sfx_shimmer():
    d = 2.5
    t = t_(d)
    out = np.zeros(len(t))
    for i, f in enumerate([1174.7, 1568, 1760, 2349.3, 2637]):
        st = int(i * 0.07 * SR)
        e = np.zeros(len(t))
        e[st:] = env_exp(len(t) - st, 0.8)
        out += np.sin(2 * np.pi * f * t) * e * 0.4
    return norm(reverb(out, 2.5, 0.5))


def sfx_paper():
    d = 0.9
    n = int(d * SR)
    out = np.zeros(n)
    for _ in range(14):
        st = rng.integers(0, n - 4000)
        ln = rng.integers(800, 4000)
        out[st:st + ln] += bandpass(rng.standard_normal(ln), 1500, 9000) * env_exp(ln, 0.015) * rng.uniform(0.3, 1)
    return norm(out)


def sfx_quill(d=1.4):
    n = int(d * SR)
    x = bandpass(rng.standard_normal(n), 2500, 8000)
    am = (np.sin(2 * np.pi * 9 * t_(d)) > 0.2).astype(float) * (0.5 + 0.5 * rng.random(n) ** 3)
    am = lowpass(am, 60)
    return norm(x * am)


def sfx_chains():
    d = 1.5
    t = t_(d)
    out = np.zeros(len(t))
    for _ in range(9):
        st = rng.integers(0, int(0.9 * SR))
        n = len(t) - st
        tt = np.arange(n) / SR
        f0 = rng.uniform(2500, 5200)
        c = sum(np.sin(2 * np.pi * f0 * r * tt) * a for r, a in [(1, 1), (1.47, 0.6), (2.09, 0.4)])
        out[st:] += c * env_exp(n, 0.04) * rng.uniform(0.4, 1)
    return norm(reverb(out, 0.9, 0.25))


def sfx_heartbeat():
    d = 1.4
    out = np.zeros(int(d * SR))
    for st, a in [(0.0, 1), (0.28, 0.75)]:
        tt = t_(0.35)
        th = np.sin(2 * np.pi * (45 + 30 * np.exp(-tt * 30)) * tt) * env_exp(len(tt), 0.07) * a
        i = int(st * SR)
        out[i:i + len(th)] += th
    return norm(out)


def sfx_thunder():
    d = 4.0
    n = int(d * SR)
    x = lowpass(rng.standard_normal(n), 350)
    e = env_exp(n, 1.2) * (1 + 0.6 * lowpass(rng.standard_normal(n), 4))
    crack = bandpass(rng.standard_normal(n), 800, 6000) * env_exp(n, 0.08)
    return norm(reverb(x * e + crack * 0.5, 2.0, 0.3))


def sfx_sword():
    d = 1.6
    t = t_(d)
    out = np.zeros(len(t))
    for f, a in [(3150, 1), (4720, 0.7), (6300, 0.5), (8400, 0.3)]:
        out += a * np.sin(2 * np.pi * f * t) * env_exp(len(t), 0.5)
    sw = sfx_whoosh(0.35)
    out[: len(sw)] += sw * 0.8
    return norm(reverb(out, 1.5, 0.3))


def sfx_murmur(d=3.2):
    n = int(d * SR)
    out = np.zeros(n)
    for _ in range(10):
        f = rng.uniform(250, 900)
        x = bandpass(rng.standard_normal(n), f * 0.8, f * 1.4)
        am = lowpass(np.clip(rng.standard_normal(n), 0, None), 5)
        out += x * am
    e = np.minimum(1, np.minimum(t_(d) / 0.6, (d - t_(d)) / 0.8))
    return norm(reverb(out * e, 1.2, 0.4))


def sfx_glitch():
    d = 0.4
    n = int(d * SR)
    out = np.zeros(n)
    pos = 0
    while pos < n:
        ln = rng.integers(400, 2400)
        kind = rng.integers(0, 3)
        tt = np.arange(min(ln, n - pos)) / SR
        if kind == 0:
            seg = np.sign(np.sin(2 * np.pi * rng.uniform(200, 1500) * tt))
        elif kind == 1:
            seg = rng.standard_normal(len(tt))
        else:
            seg = np.zeros(len(tt))
        out[pos:pos + len(tt)] = seg * 0.5
        pos += ln
    return norm(out, 0.7)


def sfx_pop():
    tt = t_(0.25)
    f = 900 * np.exp(-tt * 18) + 300
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(len(tt), 0.04))


def sfx_popcorn(d=2.6, seed=3):
    """Patlamış mısır: rastgele kısa, tok patlamalar."""
    rng = np.random.default_rng(seed)
    out = np.zeros(int(SR * d))
    t = 0.05
    while t < d - 0.08:
        n = int(SR * 0.035)
        burst = rng.standard_normal(n) * env_exp(n, 0.006)
        burst = bandpass(burst, 600 + rng.random() * 900, 3500 + rng.random() * 2500)
        i = int(t * SR)
        out[i:i + n] += burst * (0.4 + 0.6 * rng.random())
        t += rng.exponential(0.09 if t < d * 0.6 else 0.16)
    return norm(out, 0.8)


def sfx_shutter():
    n = int(0.3 * SR)
    x = bandpass(rng.standard_normal(n), 2000, 9000)
    e = np.zeros(n)
    for st in (0, int(0.07 * SR)):
        e[st:] += env_exp(n - st, 0.012)
    return norm(x * e)


SFX = {
    "impact": sfx_impact, "hit": sfx_hit, "whoosh": sfx_whoosh, "riser": sfx_riser,
    "revcym": sfx_reverse_cymbal, "bell": sfx_bell, "shimmer": sfx_shimmer, "paper": sfx_paper,
    "quill": sfx_quill, "chains": sfx_chains, "heartbeat": sfx_heartbeat, "thunder": sfx_thunder,
    "sword": sfx_sword, "murmur": sfx_murmur, "glitch": sfx_glitch, "pop": sfx_pop, "shutter": sfx_shutter, "popcorn": sfx_popcorn,
}


# ---------------------------------------------------------------- music
HIJAZ = [0, 1, 4, 5, 7, 8, 10, 12]  # D hijaz: D Eb F# G A Bb C D


def ks_pluck(freq, d, bright=0.6):
    n = int(d * SR)
    p = int(SR / freq)
    buf = rng.uniform(-1, 1, p)
    buf = lowpass(np.concatenate([buf, np.zeros(16)]), 2000 + 6000 * bright)[:p]
    out = np.empty(n)
    decay = 0.996
    for i in range(0, n, p):
        seg = buf
        out[i:i + p] = seg[: min(p, n - i)]
        buf = decay * 0.5 * (buf + np.roll(buf, -1))
    return out * env_exp(n, 1.5)


def drum_dum():
    tt = t_(0.6)
    f = 55 + 70 * np.exp(-tt * 25)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(len(tt), 0.18) + \
        lowpass(rng.standard_normal(len(tt)), 600) * env_exp(len(tt), 0.01) * 0.3


def drum_tek():
    tt = t_(0.2)
    return bandpass(rng.standard_normal(len(tt)), 1500, 7000) * env_exp(len(tt), 0.025) * 0.5 + \
        np.sin(2 * np.pi * 420 * tt) * env_exp(len(tt), 0.03) * 0.3


def build_music(total, sections):
    """sections: list of (start, end, intensity 0..3)."""
    n = int(total * SR)
    L = np.zeros(n); R = np.zeros(n)
    base = 73.42  # D2
    tt = np.arange(n) / SR
    # drone: D + A with slow beating, lowpassed saw-ish
    drone = np.zeros(n)
    for f, a in [(base, 1), (base * 1.5, 0.5), (base * 2, 0.35), (base * 1.005, 0.6)]:
        for h in range(1, 6):
            drone += a / h * np.sin(2 * np.pi * f * h * tt + h)
    drone = lowpass(drone, 500) * (0.7 + 0.3 * np.sin(2 * np.pi * 0.07 * tt))
    inten = np.zeros(n)
    for s, e, lvl in sections:
        inten[int(s * SR):int(e * SR)] = lvl
    inten_s = lowpass(inten, 1.5)
    drone_env = np.clip(0.55 + 0.15 * inten_s, 0, 1)
    L += drone * drone_env * 0.18; R += drone * drone_env * 0.18

    bpm = 92
    beat = 60 / bpm
    # maqsum-like pattern on 8 eighth-notes: D T . T D . T .
    pat = ["D", "T", None, "T", "D", None, "T", None]
    dum, tek = drum_dum(), drum_tek()
    melody = [0, 1, 2, 1, 0, 1, 3, 2, 4, 3, 2, 1, 2, 1, 0, -1]
    k = 0
    t = 0.0
    while t < total:
        lvl = inten[min(int(t * SR), n - 1)]
        step = int(round(t / (beat / 2)))
        sym = pat[step % 8]
        if lvl >= 2 and sym:
            smp = dum if sym == "D" else tek
            i = int(t * SR)
            seg = smp[: max(0, min(len(smp), n - i))]
            g = 0.55 if sym == "D" else 0.35
            if lvl >= 3: g *= 1.25
            L[i:i + len(seg)] += seg * g; R[i:i + len(seg)] += seg * g * 0.9
        if lvl >= 1 and step % 2 == 0:
            deg = melody[k % len(melody)]
            k += 1
            semis = HIJAZ[deg % 7] + 12 * (deg // 7)
            f = base * 4 * 2 ** (semis / 12)
            pl = ks_pluck(f, 1.2, 0.5) * (0.22 if lvl >= 2 else 0.16)
            i = int(t * SR)
            seg = pl[: max(0, min(len(pl), n - i))]
            pan = 0.35 + 0.3 * ((k * 37) % 10) / 10
            L[i:i + len(seg)] += seg * (1 - pan); R[i:i + len(seg)] += seg * pan
        t += beat / 2
    L = reverb(L, 2.2, 0.28)[:n]; R = reverb(R, 2.4, 0.28)[:n]
    fade = np.minimum(1, (total - tt) / 2.0)
    return np.stack([L * fade, R * fade], 1)


def write_wav(path, x):
    x = np.clip(x, -1, 1)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())


def main(spec_path, music_out, sfx_out):
    spec = json.load(open(spec_path))
    total = spec["duration"]
    music = build_music(total, spec["music"])
    write_wav(music_out, norm(music, 0.8))
    n = int(total * SR)
    sfx = np.zeros((n, 2))
    cache = {}
    for ev in spec["sfx"]:
        name, at, gain = ev["name"], ev["t"], ev.get("gain", 0.5)
        if name not in cache:
            cache[name] = SFX[name]()
        s = cache[name]
        i = int(at * SR)
        if ev.get("pre"):  # align the end of the sample (risers) to `at`
            i -= len(s)
        a = max(i, 0)
        seg = s[a - i: a - i + max(0, min(len(s) - (a - i), n - a))]
        pan = ev.get("pan", 0.5)
        sfx[a:a + len(seg), 0] += seg * gain * (1 - pan) * 2 ** 0.5
        sfx[a:a + len(seg), 1] += seg * gain * pan * 2 ** 0.5
    write_wav(sfx_out, sfx * 0.7)


if __name__ == "__main__":
    main(*sys.argv[1:])
