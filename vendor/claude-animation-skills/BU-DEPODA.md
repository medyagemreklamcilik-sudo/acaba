# Bu depodaki kurulum notları (acaba)

Kaynak: https://github.com/artemnovitckii/claude-animation-skills (MIT). Skiller `.claude/skills/` altına bağlantı olarak eklendi.

Bulut makinesinde (Linux, GPU yok) çalıştırma:
- Paketler: `cd vendor/claude-animation-skills/kit && npm install --no-audit --no-fund` (node_modules depoda yok). GSAP: `kit/vendor/gsap.min.js` yoksa `kit/setup.sh` içindeki curl satırı.
- `playwright install` ÇALIŞTIRMA; makinedeki hazır Chromium'u kullan: `CHROME=/opt/pw-browsers/chromium`.
- zach-d-films: `GL=swiftshader` (yazılım WebGL, kare başı ~3-6 sn). `render.mjs` CHROME değişkenini okuyacak şekilde düzenlendi; `index.html`'e Türkçe harfler için Montserrat latin-ext eklendi.
- stick-figure: `make.sh` İngilizce ses/hizalama modellerini (Kokoro, Parakeet) bekler. Türkçe için: ses = ElevenLabs Cavit Pancar (`tools/tts.py`), kelime zamanları = `tools/transcribe.py` (faster-whisper); `audio/words_new.json` + `web/words.js` + `web/warp.js` (`window.WARP=null;`) elle yazılır, sonra `node engine/tools/render.js segments ...` ve ffmpeg ile birleştirilir.
- Python: `pip install scipy soundfile` (audio.py için).
