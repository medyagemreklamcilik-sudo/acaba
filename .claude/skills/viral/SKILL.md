---
name: viral
description: acaba.nolurdu için uçtan uca dikey tarih videosu üretir ve yayına planlar. Takvimdeki sıradaki konuyu (veya verilen konuyu) araştırır, ElevenLabs seslendirme metnini Cavit Pancar sesiyle seslendirir, gerçek tarihi görselleri bulur, 1080x1920 videoyu render eder, depoya push eder ve Metricool'da 16:00'ya Instagram/TikTok/YouTube/Facebook için planlar. "/viral", "/viral <konu>", "/viral 2026-11-03" veya "sıradaki videoyu hazırla" dendiğinde kullan.
---

# /viral — acaba.nolurdu video hattı

Depo: `medyagemreklamcilik-sudo/acaba` (herkese açık, `main` dalı). Çalışma kökü: `/home/user/acaba`.
Argüman yoksa `takvim.md`'de tarihi **yarın** (Europe/Istanbul) olan ve durumu `bekliyor` olan satırı üret (aynı güne ait EKSTRA satırlar ayrı videodur, onlara bakma); yarına ait `bekliyor` satır yoksa, tarihi yarından sonra olan ilk `bekliyor` satırı üret. Satırda saat yazmıyorsa yayın 16:00'dır. Takvimde hiç `bekliyor` satır kalmadıysa önceki konularla çakışmayan, tartışma yaratacak yeni bir Osmanlı/Cumhuriyet tarihi konusu seç ve takvime ekle.
Otomatik (zamanlanmış) çalıştırmada kullanıcıya hiçbir şey sorma; her kararı kendin ver ve sonunda kısa rapor yaz. Argüman bir tarihse o satırı, serbest metinse o konuyu üret (takvime ekleyerek).

## 0. Hazırlık (her yeni oturumda)
1. `/home/user/acaba` yoksa: `add_repo` (owner `medyagemreklamcilik-sudo`, repo `acaba`, access `push`), sonra `git clone https://github.com/medyagemreklamcilik-sudo/acaba /home/user/acaba`.
2. `cd /home/user/acaba && git pull origin main`.
3. `python3 -c "import faster_whisper"` başarısızsa `./setup.sh`.
4. ElevenLabs anahtarı `ELEVENLABS_API_KEY` ortam değişkeninde ya da `/home/user/acaba/.env` dosyasında olmalı. Yoksa **dur** ve kullanıcıya ortam ayarlarına `ELEVENLABS_API_KEY` eklemesini söyle; anahtarı asla depoya yazma.
5. Metricool: brand id `7651740`, saat dilimi `Europe/Istanbul`.

## 1. Klasör
`videolar/<YYYY-MM-DD>-<kısa-slug>/` (ör. `videolar/2026-11-03-kardes-katli/`). Takvimde Klasör sütununu doldur.

## 2. Araştırma + metin (`tts.txt`)
- Konuyu WebSearch ile araştır; tarih, isim, sayıları en az iki kaynaktan doğrula. Kaynak listesini README'ye yaz.
- Kesin olmayan iddiaları kesin gibi yazma; tartışmalıysa "iddiaya göre", "bazı tarihçilere göre" de ya da soru olarak sor. Etkileşim için tartışma çıkaran **soru** sor, uydurma bilgi verme.
- Uzunluk: 1.600–2.100 karakter (≈1:45–2:15). Dil: sade, konuşma Türkçesi, kısa cümleler.
- Yapı: **ilk cümle kanca** (şok edici bilgi/soru, ilk 1 saniye), 3 saniyede vaat, ana anlatım (isimler, yıllar, somut detaylar), en sonda yorumlarda tartışma çıkaracak soru ("Sizce...? Yorumlara yazın.").
- ElevenLabs "auto-tag" yerine etiketleri sen ekle (Eleven v4 destekler): `[dramatic]`, `[serious]`, `[whispers]`, `[excited]`, `[curious]`, `[pause]`, `[sighs]`. Her 1–3 cümlede bir, abartmadan. Etiketler köşeli parantezde, okunmaz.
- Sayıları ve kısaltmaları yazıyla değil rakamla bırakabilirsin (1453), ama "II. Mehmed" yerine "İkinci Mehmed" yaz ki doğru okunsun.

## 3. Seslendirme + zamanlama
```
python3 tools/viral.py voice videolar/<klasör>
```
`build/voice.mp3` (Cavit Pancar, `eleven_v4`), `script.txt` (etiketsiz metin) ve `build/aligned.json` (kelime zamanları) üretir. Kalan karakter hakkını kontrol etmek için: `GET https://api.elevenlabs.io/v1/user/subscription`.

## 4. Görseller (adı geçen HER kişi ve yer için gerçek tarihi görsel)
- Wikimedia bu ortamdan 429 veriyor; kullanma. Yandex ve Europeana kullan:
  - `tools/ydl.py <klasör>/build/cand jobs.json 8` — jobs: `[["anahtar", "arama sorgusu"], ...]`
  - `tools/eu_dl.py <klasör>/build/cand jobs.json` — jobs: `[["anahtar", "sorgu", 12], ...]`
- `python3 tools/sheet.py sheet.jpg <dosyalar...>` ile kontak sayfası yap, Read ile bak, en iyi, filigransız, gerçek (AI üretimi olmayan) görselleri seç. Kişi portresinin doğru kişi olduğundan emin ol.
- Seçilenleri `videolar/<klasör>/img/` içine kopyala. Kaynak URL'lerini (`build/cand/_index.json`) README'ye yaz.
- Portresi olmayan kişiler için bunu açıkça belirt (ör. "temsili minyatür"), sahte portre kullanma.

## 5. Sahne dosyası (`scenes.py`)
Örnekler: `engine/ornekler/` (`scenes_koyun.py` kalem efektleri, `scenes_hocalar.py` belgesel, `scenes_hurrem_kosem.py` karşılaştırma, `scenes_harita.py` + `mapdata_harita.py` harita). Zamanları `build/aligned.json`'dan al.
- Dosyada: `DURATION` (ses süresi), `CX = 507`, `IMAGES {anahtar: dosya | (dosya, (x0,y0,x1,y1) kırpma)}`, `FACES`, `SCENES`, `OVERLAYS`, `NO_CAPTIONS`, `BLUR_CAPS`, `CAPTION_Y(t)`, `PUNCH`, `SHAKE`, `FLASH`, `MUSIC [(t0,t1,yoğunluk 0-3)]`, `SFX`, `spec()`.
- Sahne modları: `cover` (zoom/focus/from/to/kf), `card` (maxw,maxh,tilt), `split` (imgs), `grid` (tiles,bg), `plate` (bg; sadece yazı arka planı).
- Geçişler (`tr`): pushup, pushdown, pushleft, pushright, bars, iris, diag, zoomblur, spin, glitch, flash, dip. **Çeşitli kullan**, aynı geçişi art arda koyma. Her 2–4 saniyede görsel değişsin.
- Overlay tipleri: title, label, kinetic, counter, arrow, pip, stamp, tagpair, cta, item, source, quote, vs, roster, pencircle, penarrow, penline, pencross, handwrite, finger, people, typewriter, papers.
- Stil kuralları (kullanıcının istekleri):
  - Altyazılar siyah kutu üstünde **sarı** yazı (motor otomatik yapar).
  - Güvenli alan: x 64–950, üst yazılar y≥230, altyazı y≈1235–1440; sağ kenar ve alt 420 px butonlara ayrılmış.
  - İlk 1 saniyede güçlü kanca: büyük `title` + `impact` SFX + hareketli zoom.
  - Bir şeyi göstermek için kalem efektleri: `pencircle`, `penarrow`, `handwrite`.
  - Geçiş SFX'ini az kullan (izleyiciyi bayıyor): sadece önemli anlarda `impact`/`hit`, gerisi sessiz.
  - Yapay zekâ görünümü olmasın: gerçek arşiv görselleri, sade modern tipografi, abartısız renk.
  - Sona `cta` + tartışma sorusu `kinetic` ile.
  - Kaynak gösterilen iddialarda `source` overlay'i kullan.
- **Kapak (zorunlu):** `scenes.py` içine `COVER` ekle. Videonun ilk 2 karesi ve `kapak.jpg` bundan üretilir (TikTok kapağı ilk kareden alır; beyaz flaş/boş kare kapak olmasın). Kullanıcının elle yaptığı kapak tarzı:
  ```python
  COVER = dict(img="fatih", focus=(0.45, 0.32), zoom=1.12,          # yüzü net, büyük bir görsel
               lines=["FATİH İSTANBUL'U", "ALAMASAYDI?"], size=118,   # siyah kutuda sarı, 2 satır, kısa ve soru/şok
               stamp="OSMANLI BİTERDİ?", stamp_y=1050, stamp_size=96, # kırmızı damga: tartışma kışkırtan 1-3 kelime
               bottom="sonuna kadar izle", bottom_y=1330,              # altta sarı küçük çağrı
               marks=[dict(type="pencircle", cx=..., cy=..., rx=..., ry=...)])  # isteğe bağlı: kırmızı daire/ok
  ```
  **Her videonun kapağı kendine özel olmalı** (kullanıcı isteği). Kapak tasarlamadan önce `grep -A4 "COVER" videolar/*/scenes.py` ile son 7 videonun kapaklarına bak ve aynı düzeni, aynı damga/alt yazıyı, aynı başlık rengini art arda kullanma. Konuya göre düzen seç:
  - **Tek yüz** (kişi videoları): `img` + `focus` yüze, büyük başlık, damga.
  - **Karşılaştırma** (X mi Y mi): `imgs=[dict(img=..., focus=...), dict(img=..., focus=...)]` + `marks=[dict(type="vs")]`.
  - **Detay işaretleme** (belge, tablo, mekân): `marks` ile `pencircle` + `penarrow` kırmızı daire/ok, `handwrite` el yazısı not.
  - **Harita/şehir + portre**: arka plan harita (`grade="dark"`), `portraits=[("anahtar", x, y, boyut)]` yuvarlak portre.
  - **Rakam kancası**: başlıkta büyük sayı ("53 GÜN", "623 YIL", "%3").
  - Başlık rengi `style`: `"yellow"` (siyah kutu sarı yazı), `"red"` (kırmızı kutu beyaz yazı), `"white"` (beyaz kutu siyah yazı). Damga rengi `stamp_color`. Alt yazı (`bottom`) her seferinde farklı ve konuya özel olsun ("sonuna kadar izle"yi sürekli tekrarlama); gerekmiyorsa hiç koyma.
  - Kapak metni videodaki kancayla aynı vaadi versin ama birebir aynı cümle olmak zorunda değil; merak boşluğu bıraksın.
  Başlık 3 saniyede okunmalı, en fazla ~16 karakter/satır. Yüz veya ana obje yazıların altında kalmasın. `python3 tools/viral.py cover <klasör>` ile üretip Read ile kontrol et; küçük (360x640) halde de okunur olmalı.
- Önizleme: `python3 tools/viral.py stills videolar/<klasör> 0.5,5,30,60,...` ve kareleri Read ile kontrol et (yazı taşması, yüz kesilmesi, güvenli alan). Sorunları düzelt.

## 6. Render
```
python3 tools/viral.py render videolar/<klasör>
```
(Harita videoları için klasörde `mapdata.py` olması yeterli.) Çıktı: `video.mp4` (1080x1920, ≈3.5 Mbps, < 90 MB) ve `kapak.jpg`. Uzun sürer; arka planda çalıştır, bitince süreyi ve boyutu doğrula, birkaç kare çıkarıp bak.

## 7. Açıklama (`aciklama.txt`)
- **Toplam en fazla 100 karakter, 4 hashtag dahil.** Emoji yok. `#osmanlıtreni` / "osmanlı treni" etiketini KULLANMA (kullanıcı yalnızca tek bir video için istemişti). Merak uyandıran tek cümle + 4 hashtag. Python ile `len()` kontrol et.
- YouTube başlığı (`baslik.txt`): en fazla 70 karakter, kanca gibi.

## 8. Depoya gönder
```
git add videolar/<klasör> takvim.md && git commit -m "<konu> videosu" && git push origin main
```
`img/` ve `build/` .gitignore'da; video, kapak, metinler, scenes.py ve README girer. Push sonrası kontrol:
`curl -sI https://raw.githubusercontent.com/medyagemreklamcilik-sudo/acaba/main/videolar/<klasör>/video.mp4` → 200.

## 9. Metricool'da planla (16:00)
`createScheduledPost` — blogId `7651740`, tarih `<YYYY-MM-DD>T16:00:00+03:00`, info:
```json
{"autoPublish": true, "draft": false, "text": "<aciklama.txt>",
 "media": ["https://raw.githubusercontent.com/medyagemreklamcilik-sudo/acaba/main/videolar/<klasör>/video.mp4"],
 "videoThumbnailUrl": "https://raw.githubusercontent.com/medyagemreklamcilik-sudo/acaba/main/videolar/<klasör>/kapak.jpg",
 "providers": [{"network":"instagram"},{"network":"tiktok"},{"network":"youtube"},{"network":"facebook"}],
 "publicationDate": {"dateTime": "<YYYY-MM-DD>T16:00:00", "timezone": "Europe/Istanbul"},
 "instagramData": {"type": "REEL", "showReelOnFeed": true},
 "tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE", "title": "<aciklama.txt>"},
 "youtubeData": {"title": "<baslik.txt>", "type": "short", "privacy": "public", "madeForKids": false, "category": "EDUCATION", "tags": ["tarih", "osmanlı"]},
 "facebookData": {"type": "REEL"},
 "firstCommentText": "", "hasNotReadNotes": false, "shortener": false, "smartLinkData": {"ids": []}, "descendants": [], "mediaAltText": []}
```
`VIDEO_THUMBNAIL_NOT_APPLICABLE` hatası gelirse `videoThumbnailUrl` olmadan bir kez daha dene (kapak zaten videonun ilk karesi). Başka hata verirse mesajı olduğu gibi kullanıcıya ilet; plan limiti (ücretsiz plan) dolduysa takvimde durumu `hazır` bırak.
Başarılıysa takvimde durumu `planlandı` yap, commit + push.

## 10. Rapor
Kullanıcıya kısa Türkçe özet: konu, süre, yayın tarihi/saati, açıklama, tartışmalı/emin olunmayan noktalar, Metricool planner linki.
