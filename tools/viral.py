"""/viral boru hattı. Her video bir klasör: videolar/<YYYY-MM-DD>-<konu>/

  python3 tools/viral.py voice  <klasör>            tts.txt -> build/voice.mp3, script.txt, aligned.json
  python3 tools/viral.py stills <klasör> t1,t2,...  önizleme kareleri -> build/stills/
  python3 tools/viral.py render <klasör>            müzik+sfx+mix, render, encode -> <klasör>/video.mp4

Harita videoları için klasörde mapdata.py varsa engine/map/run_map.py kullanılır.
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS, ENGINE = os.path.join(ROOT, "tools"), os.path.join(ROOT, "engine")
PY = sys.executable


def run(cmd, **kw):
    print("+", " ".join(cmd) if isinstance(cmd, list) else cmd, flush=True)
    subprocess.run(cmd, check=True, **kw)


def duration(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True, check=True).stdout)


def voice(d):
    b = os.path.join(d, "build"); os.makedirs(b, exist_ok=True)
    mp3 = os.path.join(b, "voice.mp3")
    if not os.path.exists(mp3):
        run([PY, os.path.join(TOOLS, "tts.py"), os.path.join(d, "tts.txt"), mp3])
    run([PY, os.path.join(TOOLS, "strip_tags.py"), os.path.join(d, "tts.txt"), os.path.join(d, "script.txt")])
    run([PY, os.path.join(TOOLS, "transcribe.py"), mp3, os.path.join(b, "words.json")])
    run([PY, os.path.join(TOOLS, "align.py"), os.path.join(b, "words.json"), os.path.join(d, "script.txt"),
         os.path.join(b, "aligned.json")])
    print(f"süre: {duration(mp3):.2f} sn")


def renderer(d):
    return os.path.join(ENGINE, "map", "run_map.py") if os.path.exists(os.path.join(d, "mapdata.py")) \
        else os.path.join(ENGINE, "render.py")


def env(d):
    e = dict(os.environ, VIDEO_DIR=os.path.abspath(d))
    e["PYTHONPATH"] = os.pathsep.join([os.path.abspath(d), ENGINE])
    return e


def stills(d, ts):
    out = os.path.join(d, "build", "stills"); os.makedirs(out, exist_ok=True)
    run([PY, renderer(d), out, "1", ts], env=env(d))


def render(d, workers="4"):
    d = os.path.abspath(d); b = os.path.join(d, "build"); out = os.path.join(b, "out"); os.makedirs(out, exist_ok=True)
    e = env(d)
    spec = os.path.join(b, "spec.json")
    run([PY, "-c", f"import json,scenes;json.dump(scenes.spec(),open({spec!r},'w'))"], env=e, cwd=d)
    run([PY, os.path.join(ENGINE, "music.py"), spec, os.path.join(b, "music.wav"), os.path.join(b, "sfx.wav")], env=e)
    dur = json.load(open(spec))["duration"]
    fc = ("[0:a]aresample=44100,pan=stereo|c0=c0|c1=c0,highpass=f=70,acompressor=threshold=-18dB:ratio=3:attack=5:release=80,"
          f"apad=whole_dur={dur}[v];[v]asplit=2[vm][vk];[1:a]volume=0.28[m];"
          "[m][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[md];[2:a]volume=0.8[s];"
          "[vm][md][s]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(b, "voice.mp3"), "-i", os.path.join(b, "music.wav"),
         "-i", os.path.join(b, "sfx.wav"), "-filter_complex", fc, "-map", "[out]", "-ar", "44100", "-c:a", "pcm_s16le",
         os.path.join(b, "mix.wav")])
    for f in os.listdir(out):
        if f.startswith("seg"):
            os.remove(os.path.join(out, f))
    run([PY, renderer(d), out, workers], env=e)
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(out, "segs.txt"), "-c", "copy",
         os.path.join(out, "raw.mp4")])
    # ~3.5 Mbps: 2 dk ≈ 55 MB, GitHub 100 MB sınırının altında kalır
    kbps = min(3500, int(88_000 * 8 / dur) - 160)
    enc = ["-c:v", "libx264", "-preset", "slow", "-b:v", f"{kbps}k", "-passlogfile", os.path.join(out, "p2")]
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(out, "raw.mp4")] + enc + ["-pass", "1", "-an", "-f", "null", "/dev/null"])
    final = os.path.join(d, "video.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(out, "raw.mp4"), "-i", os.path.join(b, "mix.wav")] + enc +
        ["-maxrate", f"{kbps * 2}k", "-bufsize", f"{kbps * 2 + 2000}k", "-pass", "2", "-pix_fmt", "yuv420p",
         "-profile:v", "high", "-level", "4.2", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
         "-tag:v", "avc1", "-shortest", final])
    # kapak: 1. saniyedeki kare
    run(["ffmpeg", "-v", "error", "-y", "-ss", "1.0", "-i", final, "-frames:v", "1", "-q:v", "2", os.path.join(d, "kapak.jpg")])
    print(f"{final}: {os.path.getsize(final) / 1e6:.1f} MB, {duration(final):.2f} sn")


if __name__ == "__main__":
    cmd, d = sys.argv[1], sys.argv[2]
    {"voice": lambda: voice(d), "stills": lambda: stills(d, sys.argv[3]),
     "render": lambda: render(d, *sys.argv[3:4])}[cmd]()
