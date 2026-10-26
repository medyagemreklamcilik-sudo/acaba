# acaba.nolurdu

Dikey (1080x1920) tarih videoları, video motoru ve `/viral` skill'i.

- `takvim.md` — günlük içerik takvimi (her gün 16:00, tüm platformlar)
- `videolar/<tarih>-<konu>/` — her videonun klasörü: `video.mp4`, `kapak.jpg`, `tts.txt` (ElevenLabs metni), `script.txt`, `scenes.py`, `aciklama.txt`, `README.md` (kaynaklar)
- `engine/` — renderer (`render.py`), müzik/SFX (`music.py`, `audio.py`), harita motoru (`map/`), fontlar, örnek sahne dosyaları
- `tools/` — seslendirme (`tts.py`), transkripsiyon/hizalama, görsel arama, boru hattı (`viral.py`)
- `.claude/skills/viral/SKILL.md` — `/viral` komutunun adımları

Eski videolar (Hürrem, Köle, Atatürk dindar, Hürrem–Kösem, Koyun, Hocalar, Osmanlı haritası) `medyagemreklamcilik-sudo/esradavetiye` deposunda.

Kurulum: `./setup.sh`. ElevenLabs anahtarı `ELEVENLABS_API_KEY` ortam değişkeninden okunur (depoya yazılmaz).
