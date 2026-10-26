"""ElevenLabs seslendirme: Cavit Pancar sesi, Eleven v4 (ses etiketleri [dramatic], [whispers]... desteklenir).

Kullanım: python3 tools/tts.py <tts.txt> <çıktı.mp3>
Anahtar: ELEVENLABS_API_KEY ortam değişkeni ya da depo kökündeki .env (git'e girmez).
"""
import json, os, sys, urllib.error, urllib.request

VOICE = "Y2T2O1csKPgWgyuKcU0a"  # Cavit Pancar - Epic Powerful Historical
MODEL = "eleven_v4"


def key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    env = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    if not k and os.path.exists(env):
        for line in open(env):
            if line.startswith("ELEVENLABS_API_KEY="):
                k = line.split("=", 1)[1].strip()
    if not k:
        sys.exit("ELEVENLABS_API_KEY yok: ortam değişkeni olarak ekle ya da .env dosyasına yaz.")
    return k


def main(src, out):
    text = open(src).read().strip()
    body = json.dumps({"text": text, "model_id": MODEL}).encode()
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_192"
    req = urllib.request.Request(url, data=body, headers={"xi-api-key": key(), "Content-Type": "application/json"})
    try:
        data = urllib.request.urlopen(req, timeout=600).read()
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs hata {e.code}: {e.read()[:400]}")
    open(out, "wb").write(data)
    print(f"{out}: {len(data) // 1024} KB, {len(text)} karakter")


if __name__ == "__main__":
    main(*sys.argv[1:3])
