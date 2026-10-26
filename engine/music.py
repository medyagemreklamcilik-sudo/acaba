"""Modern trailer-style score for the slavery short; SFX reused from audio.py."""
import json, sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "proj"))
import audio as A

SR = A.SR
rng = np.random.default_rng(21)


def saw(f, n):
    t = np.arange(n) / SR
    return 2 * ((t * f) % 1.0) - 1


def build(total, sections):
    n = int(total * SR)
    L = np.zeros(n); R = np.zeros(n)
    inten = np.zeros(n)
    for s, e, lv in sections:
        inten[int(s * SR):int(e * SR)] = lv
    bpm = 96; beat = 60 / bpm
    # chord pads: Dm Bb Gm A  (one chord per bar)
    chords = [[50, 53, 57], [46, 50, 53], [43, 46, 50], [45, 49, 52]]
    bar = beat * 4
    t = 0.0; k = 0
    env_len = int(bar * SR)
    att = np.minimum(1, np.arange(env_len) / (0.4 * SR)); rel = np.minimum(1, (env_len - np.arange(env_len)) / (0.3 * SR))
    while t < total:
        i = int(t * SR)
        seg = min(env_len, n - i)
        lv = inten[min(i, n - 1)]
        pad = np.zeros(env_len)
        for m in chords[k % 4]:
            f = 440 * 2 ** ((m - 69) / 12)
            pad += saw(f, env_len) * 0.5 + saw(f * 1.006, env_len) * 0.5
        pad = A.lowpass(pad, 700 + 500 * lv) * att * rel * (0.07 + 0.02 * lv)
        # sub bass pulse on 8ths
        bass = np.zeros(env_len)
        if lv >= 1:
            f = 440 * 2 ** ((chords[k % 4][0] - 24 - 69) / 12)
            tt = np.arange(env_len) / SR
            gate = np.exp(-((tt % (beat / 2)) / 0.12))
            bass = np.sin(2 * np.pi * f * tt) * gate * (0.22 if lv >= 2 else 0.14)
        L[i:i + seg] += (pad + bass)[:seg]; R[i:i + seg] += (pad * 0.95 + bass)[:seg]
        t += bar; k += 1
    # drums
    kick_t = np.arange(int(0.5 * SR)) / SR
    kick = np.sin(2 * np.pi * np.cumsum(45 + 110 * np.exp(-kick_t * 30)) / SR) * np.exp(-kick_t * 7)
    hat = A.bandpass(rng.standard_normal(int(0.06 * SR)), 6000, 15000) * np.exp(-np.arange(int(0.06 * SR)) / (0.012 * SR))
    clap = A.bandpass(rng.standard_normal(int(0.25 * SR)), 900, 4000) * np.exp(-np.arange(int(0.25 * SR)) / (0.05 * SR))
    taiko_t = np.arange(int(1.2 * SR)) / SR
    taiko = np.sin(2 * np.pi * np.cumsum(60 + 40 * np.exp(-taiko_t * 12)) / SR) * np.exp(-taiko_t * 3.5)
    taiko = A.reverb(taiko + A.lowpass(rng.standard_normal(len(taiko_t)), 400) * np.exp(-taiko_t * 20) * 0.4, 1.5, 0.3)[:len(taiko_t)]
    step = beat / 4; s_ = 0; t = 0.0
    while t < total:
        i = int(t * SR); lv = inten[min(i, n - 1)]
        def put(x, g, pan=0.5):
            seg = x[:max(0, min(len(x), n - i))]
            L[i:i + len(seg)] += seg * g * (1 - pan) * 1.4; R[i:i + len(seg)] += seg * g * pan * 1.4
        pos = s_ % 16
        if lv >= 2 and pos in (0, 8, 10):
            put(kick, 0.55)
        if lv >= 3 and pos in (4, 12):
            put(clap, 0.35)
        if lv >= 2 and pos % 2 == 0:
            put(hat, 0.18 if pos % 4 else 0.1, 0.6 + 0.2 * ((s_ // 2) % 2))
        if lv >= 3 and pos == 0 and (s_ // 16) % 2 == 0:
            put(taiko, 0.6)
        if lv == 1 and pos == 0 and (s_ // 16) % 2 == 0:
            put(taiko, 0.35)
        t += step; s_ += 1
    L = A.reverb(L, 1.6, 0.2)[:n]; R = A.reverb(R, 1.8, 0.2)[:n]
    tt = np.arange(n) / SR
    fade = np.minimum(1, (total - tt) / 1.2)
    return np.stack([L * fade, R * fade], 1)


def _pen():
    return A.sfx_quill(0.45) * 0.8


def _type():
    n = int(1.6 * SR); out = np.zeros(n)
    for k in range(26):
        i = int(k * 0.058 * SR + rng.uniform(0, 0.01) * SR)
        ln = int(0.03 * SR)
        click = A.bandpass(rng.standard_normal(ln), 1500, 7000) * np.exp(-np.arange(ln) / (0.004 * SR))
        out[i:i + ln] += click[: max(0, min(ln, n - i))]
    return A.norm(out)


A.SFX["pen"] = _pen
A.SFX["type"] = _type

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    m = build(spec["duration"], spec["music"])
    A.write_wav(sys.argv[2], A.norm(m, 0.8))
    # sfx
    total = spec["duration"]; n = int(total * SR); sfx = np.zeros((n, 2)); cache = {}
    for ev in spec["sfx"]:
        nm = ev["name"]
        if nm not in cache:
            cache[nm] = A.SFX[nm]()
        x = cache[nm]; i = int(ev["t"] * SR) - (len(x) if ev.get("pre") else 0)
        a = max(i, 0); seg = x[a - i: a - i + max(0, min(len(x) - (a - i), n - a))]
        sfx[a:a + len(seg)] += seg[:, None] * ev.get("gain", 0.5)
    A.write_wav(sys.argv[3], sfx * 0.7)
