"""Overlay timeline for the Ottoman map video (narration seconds)."""

DURATION = 216.2
CX = 507
IMAGES = {}
FACES = {}
SCENES = [dict(t=0.0, mode="plate", bg=None, _end=DURATION)]

RED = (255, 45, 45)
YEL = (255, 214, 10)

OVERLAYS = [
    dict(type="mapui", t0=0.0, t1=DURATION + 1),
    dict(type="title", t0=0.0, t1=2.9, lines=["KÜÇÜK BİR BEYLİKTEN", "ÜÇ KITAYA"], y=330, size=100),
    dict(type="kinetic", t0=0.3, t1=2.9, text="1683", y=560, size=130),
    dict(type="kinetic", t0=3.0, t1=5.4, text="SONRA…", y=330, size=130, style="red"),
    dict(type="kinetic", t0=4.4, t1=5.4, text="1923", y=560, size=130),
    dict(type="counter", t0=5.54, t1=8.7, **{"from": 1, "to": 36}, fmt="{} PADİŞAH", dur=0.9, y=330, size=130),
    dict(type="counter", t0=6.90, t1=8.7, **{"from": 0, "to": 623}, fmt="{} YIL", dur=0.9, y=500, size=110),
    dict(type="title", t0=8.78, t1=11.5, lines=["İŞTE OSMANLI'NIN", "HARİTASI"], y=330, size=100),
    dict(type="stamp", t0=48.46, t1=50.6, text="ANKARA 1402", y=1110, size=100),
    dict(type="kinetic", t0=56.06, t1=56.95, text="YENİDEN BİRLİK", y=1110, size=90),
    dict(type="stamp", t0=65.74, t1=67.3, text="FETİH", y=1110, size=120, color=(130, 255, 150), rot=-6),
    dict(type="kinetic", t0=80.56, t1=81.4, text="×2", y=1110, size=150),
    dict(type="kinetic", t0=91.08, t1=92.35, text="ZİRVE", y=1110, size=130),
    dict(type="kinetic", t0=121.84, t1=123.5, text="EN GENİŞ SINIRLAR", y=1110, size=90),
    dict(type="stamp", t0=125.96, t1=128.7, text="DÖNÜM NOKTASI", y=1110, size=96),
    dict(type="stamp", t0=135.02, t1=136.9, text="İLK BÜYÜK KAYIP", y=1110, size=96),
    dict(type="stamp", t0=161.40, t1=163.5, text="BERLİN 1878", y=1110, size=100),
    dict(type="stamp", t0=179.36, t1=181.9, text="BALKAN BOZGUNU", y=1110, size=96),
    dict(type="stamp", t0=193.62, t1=195.6, text="SEVR 1920", y=1110, size=110),
    dict(type="stamp", t0=200.20, t1=202.0, text="SALTANAT KALDIRILDI", y=900, size=84),
    dict(type="kinetic", t0=202.06, t1=204.9, text="623 YIL\nSONA ERDİ", y=840, size=110, style="black"),
    dict(type="kinetic", t0=209.36, t1=210.9, text="TÜRKİYE\nCUMHURİYETİ", y=1100, size=110, style="red"),
    dict(type="kinetic", t0=211.0, t1=DURATION + 1, text="ÇÖKÜŞ NE ZAMAN\nBAŞLADI?", y=380, size=100, style="black"),
    dict(type="cta", t0=214.1, t1=DURATION + 1, y=1250),
]

NO_CAPTIONS = [(0.0, 2.9), (214.0, DURATION + 1)]
BLUR_CAPS = []


def CAPTION_Y(t):
    return 1440


PUNCH = []
SHAKE = [48.46, 124.48, 179.36]
FLASH = [(65.74, 0.25)]

MUSIC = [(0, 11.6, 2), (11.6, 47.0, 2), (47.0, 53.7, 1), (53.7, 119.8, 3), (119.8, 128.8, 1),
         (128.8, 190.3, 2), (190.3, 205.0, 0), (205.0, 211.0, 3), (211.0, DURATION, 1)]

import mapdata as _MD

SFX = [dict(name="impact", t=0.0, gain=0.8), dict(name="glitch", t=2.98, gain=0.35), dict(name="hit", t=4.3, gain=0.4),
       dict(name="hit", t=11.64, gain=0.45), dict(name="impact", t=48.46, gain=0.55), dict(name="impact", t=65.74, gain=0.6),
       dict(name="riser", t=119.78, gain=0.3, pre=True), dict(name="impact", t=124.48, gain=0.6),
       dict(name="hit", t=135.02, gain=0.45), dict(name="hit", t=161.40, gain=0.45), dict(name="impact", t=179.36, gain=0.5),
       dict(name="hit", t=193.62, gain=0.45), dict(name="bell", t=200.2, gain=0.4), dict(name="riser", t=209.36, gain=0.3, pre=True),
       dict(name="impact", t=209.36, gain=0.55), dict(name="pop", t=214.1, gain=0.4)]
for _op in _MD.OPS:
    if _op[3]:
        SFX.append(dict(name="pop" if _op[1] != "sub" else "hit", t=_op[0], gain=0.22 if _op[1] != "sub" else 0.3))
for _s in _MD.SULTANS:
    SFX.append(dict(name="whoosh", t=_s[0] - 0.12, gain=0.18))


def spec():
    return {"duration": DURATION, "music": MUSIC, "sfx": SFX}


if __name__ == "__main__":
    import json, sys
    json.dump(spec(), open(sys.argv[1], "w"))
