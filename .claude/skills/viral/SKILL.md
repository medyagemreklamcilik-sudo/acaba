---
name: viral
description: acaba.nolurdu için uçtan uca dikey tarih videosu üretir ve yayına planlar. Takvimdeki sıradaki konuyu (veya verilen konuyu) araştırır, ElevenLabs seslendirme metnini Cavit Pancar sesiyle seslendirir, gerçek tarihi görselleri bulur, 1080x1920 videoyu render eder, depoya push eder ve Metricool'da her platformu kendi zirve saatine (Facebook 12:00, YouTube 16:00, TikTok 18:00, Instagram 20:00) planlar. "/viral", "/viral <konu>", "/viral 2026-11-03" veya "sıradaki videoyu hazırla" dendiğinde kullan.
---

# /viral — acaba.nolurdu video hattı

Depo: `medyagemreklamcilik-sudo/acaba` (herkese açık, `main` dalı). Çalışma kökü: `/home/user/acaba`.
Argüman yoksa `takvim.md`'de tarihi **yarın** (Europe/Istanbul) olan ve durumu `bekliyor` olan satırı üret (aynı güne ait EKSTRA satırlar ayrı videodur, onlara bakma); yarına ait `bekliyor` satır yoksa, tarihi yarından sonra olan ilk `bekliyor` satırı üret. Satırda saat yazmıyorsa her platform kendi zirve saatinde yayınlanır (bkz. adım 9); satırda saat yazıyorsa (EKSTRA) dört platform o saatte tek paylaşım olarak gider. Takvimde hiç `bekliyor` satır kalmadıysa önceki konularla çakışmayan, tartışma yaratacak yeni bir Osmanlı/Cumhuriyet tarihi konusu seç ve takvime ekle.
**Kullanıcının kalıcı kararları (15 Kasım 2026):**
- Video sohbetlerinde (otomatik ya da elle) kullanıcıya **hiçbir şey sorma**; her kararı kendin ver, sonunda kısa Türkçe rapor yaz.
- Metricool için bütün onaylar verili (plan yükseltildi, limit yok): planla, güncelle, biriken videoları kuyruğa koy.
- **Yeni videoların hepsi `/sinematik` "dosya" stilinde** (mantar pano, ip, polaroid, belge, harita; 9:16). Görüntü adımı aşağıdaki 5-6'daki sinematik hattıdır; eski `scenes.py` motoru yalnızca sinematik hat bozulursa yedektir.
- Bir gün video hazırlanamazsa boş geçme: eski güçlü bir videoyu (ör. `ogrenimler.md` tablolarındaki en iyiler) aynı saatlerde yeniden paylaş (öğrenim 37). Argüman bir tarihse o satırı, serbest metinse o konuyu üret (takvime ekleyerek).

## 0. Hazırlık (her yeni oturumda)
1. `/home/user/acaba` yoksa: `add_repo` (owner `medyagemreklamcilik-sudo`, repo `acaba`, access `push`), sonra `git clone https://github.com/medyagemreklamcilik-sudo/acaba /home/user/acaba`.
2. `cd /home/user/acaba && git pull origin main`.
3. `python3 -c "import faster_whisper"` başarısızsa `./setup.sh`.
4. ElevenLabs anahtarı `ELEVENLABS_API_KEY` ortam değişkeninde ya da `/home/user/acaba/.env` dosyasında olmalı. Yoksa **dur** ve kullanıcıya ortam ayarlarına `ELEVENLABS_API_KEY` eklemesini söyle; anahtarı asla depoya yazma.
5. Metricool: brand id `7651740`, saat dilimi `Europe/Istanbul`.

## 1. Klasör
`videolar/<YYYY-MM-DD>-<kısa-slug>/` (ör. `videolar/2026-11-03-kardes-katli/`). Takvimde Klasör sütununu doldur.

## 2. Araştırma + metin (`tts.txt`)
- **Önce `ogrenimler.md`'yi oku** ve oradaki derslere uy (kanca, süre, kart süresi, ikinci merak boşluğu). Bu dosya gerçek izleyici verisinden (`/analiz`) gelir ve bu bölümdeki genel kurallarla çelişirse `ogrenimler.md` kazanır.
- Konuyu WebSearch ile araştır; tarih, isim, sayıları en az iki kaynaktan doğrula. Kaynak listesini README'ye yaz.
- Kesin olmayan iddiaları kesin gibi yazma; tartışmalıysa "iddiaya göre", "bazı tarihçilere göre" de ya da soru olarak sor. Etkileşim için tartışma çıkaran **soru** sor, uydurma bilgi verme.
- **Uzunluk: en fazla 1.300 karakter (etiketsiz metin, ≈80-90 sn).** Taşarsa kes: önce biyografi/kronoloji cümleleri, uzun alıntılar (orijinalden en fazla bir kısa cümle, sade hâliyle) ve 3'ten fazla öğeli isim listeleri gider. Uzun video ya da EKSTRA sinematik video bu sınırın dışındadır. Dil: sade, konuşma Türkçesi, kısa cümleler.
- **İzlet / yorumlat / paylaştır kontrolü (her metinde zorunlu):**
  - *Ortada taraf tutturan an:* 30-40. saniye civarına (≈ metnin %35-45'i) izleyiciyi doğrudan içine çeken tek bir cümle koy: "Sen o gece İbrahim'in yerinde olsan saraya gider miydin?", "Sen olsan emri dinler miydin?" Cevabı videonun devamında gelmesin; merakı da diri tutar.
  - *Kendini görmek / "tam ben" hissi:* en az bir cümlede olayı izleyicinin bugünkü hayatına bağla (en yakın arkadaşın sırtından vurması, patronun emri, kardeş kıskançlığı, ailenin baskısı). Kısa ve tek cümle; ders verme.
  - *Paylaşım repliği:* videonun son anlatım cümlesi, kapaktaki vaatle aynı, tek başına alıntılanabilecek kısa bir replik olsun ("Teslim olan Medine'ydi, Çöl Kaplanı değil."). Ekranda büyük yazıyla da görünür.
  - *Söylenecek bir şey:* kapanış sorusu tek kelimeyle cevaplanabilecek iki seçenekli olsun ("Hürrem mi, kibri mi?"); yorumu kolaylaştır.
- Yapı: **ilk cümle kanca** (şok edici bilgi/soru, ilk 1 saniye), 3 saniyede vaat, ana anlatım (isimler, yıllar, somut detaylar), en sonda yorumlarda tartışma çıkaracak soru ("Sizce...? Yorumlara yazın.").
- **KANCA KURALI (kullanıcı isteği, kesin):** Video ASLA tarih/yer ile açılmaz ("27 Ocak 1595, İstanbul..." YOK, fısıltıyla tarih okumak YOK). İlk cümle olayın en şok edici gerçeği ya da en çok tartışılan sorusu olur; tarih ve yer ikinci-üçüncü cümlede gelir. İlk kelime `[dramatic]` veya `[curious]` ile, `[whispers]` ile değil.
  - Örnek kancalar (kullanıcının beğendikleri): "Bir gecede 19 kardeşini öldürttü." · "Atatürk vatan haini mi?" · "Atatürk hocaları astı mı?" · "Şehzade Mustafa isyan etseydi ne olurdu?" · "Hürrem mi güçlüydü, Kösem mi?" · "Kösem Sultan nasıl öldürüldü?"
  - Kalıplar: şok eylem ("Kendi oğlunu boğdurttu."), suçlama sorusu ("X hain miydi?"), karşılaştırma ("X mi, Y mi?"), "ya ... olsaydı?", gizem ("Mezar taşında yanlış tarih yazıyor.").
  - Ekrandaki ilk `title` overlay'i de bu kanca cümlesi olur (tarih değil); kapak başlığı kancayla aynı vaadi verir.
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

## 5. Sinematik sahne (`build/storyboard.py`) — varsayılan
Motor: `sinematik/motor/dosya.js`; derleyici `sinematik/motor/derle.py`; hat `sinematik/motor/uret.sh`. Örnekler: `sinematik/ornekler/yasar-nuri-dosya/build/storyboard.py` (2:15, dört söz), `sinematik/ornekler/salih-bozok/build/storyboard.py` (11 dk, harita dahil).
Klasör yine `videolar/<YYYY-MM-DD>-<slug>/` (Metricool raw URL'leri aynı kalır). Görseller `img/<anahtar>.jpg` (yalnız .jpg, ≤1600 px).
`build/storyboard.py` sahneleri metindeki sırayla, kelimeye bağlı yazar. Zaman = `build/aligned.json`'da o kelime grubunun başlangıcı (birebir metinden kopyala; noktalama ve kesme işareti önemsiz):
```python
BASLIK = 'Konu: kısa açıklama'; TL_YEARS, TL_EVERY, TL_START = [1600, 1650], 10, 1622.4   # alttaki yıl şeridi
SC('board', 'Sahnenin ilk kelimeleri', [            # mekân: 'board' (mantar pano), 'dark' (karanlık), 'map' (harita)
    P('osman', 'kelime grubu', 'İSİM BANDI', w=820, crop=[0,0,1,.72], shift=-1.2),   # polaroid (shift<0: ilk karede hazır)
    TI('kelime', '“BÜYÜK\nBAŞLIK”', 120, x=0, j=1, lineAt=[0, 'ikinci satır kelimesi']),  # başlık; j=1 öncekiyle aynı kadraj
    TG('kelime', 'KÜÇÜK', '1622', 'ALT SATIR'),     # manila etiket
    DC('kelime', ['BAŞLIK', 'KAYNAK', 'TARİH'], 'DAKTİLO ANAHTAR', keyAt='kelime', stamp=dict(text='DAMGA', t='kelime', x=.1, y=.3, rot=-.1)),
    BD('kelime', 'SİYAH BANT', red=True, size=80),   # ebeveyninin altına iner
    TH('osman', 'tag1'),                             # kırmızı ip (görsel anahtarı / tag1 / doc1)
    HT('osman', 'kelime', crop=[.1,.02,.8,.55], w=1100),  # nokta portre (dark)
    CT('kelime', 0, 17, 'v => Math.round(v) + " YAŞINDA"', 220, dur=1.0, sub='ALT'),  # sayaç
    ST('kelime', 'ÜSTÜ ÇİZİLEN', 'çizilecek kelime', 120),
], year=1622.4, glitch=[('kelime', .35, .8)], boom=True)
SC('map', 'kelime', [RT('kelime', ['istanbul', 'ankara'], 1.2), GD('kelime', 'ankara', 'ANKARA', square=True)],
   cam=[(-.4, 'istanbul', .2), ('kelime', 'ankara', .3)])    # şehirler: derle.py içindeki PL sözlüğü (yoksa [lon, lat])
```
Kurallar (öğrenimlerden): **ilk sahne `board` + net yüzlü polaroid (shift=-1.2) + kanca yazısı (shift=-1.2), karanlıktan yavaş açılış yok** (öğrenim 30, 32); her cümlenin tek kahramanı; ortadaki "sen olsan?" `dark` sahnede büyük yazı; sözler/alıntılar `DC` belge + altında tam metin `TI`; kamera derleyicide otomatik (odak + pano sonu geri çekilme).
Kontrol: `bash sinematik/motor/uret.sh videolar/<klasör> stills` → `videolar/<klasör>/stills/_sayfa.jpg`'yi Read ile incele (yazı taşması, boş pano, yüzü örten yazı); storyboard'u düzelt, yeniden `stills`.
- **Kapak (zorunlu):** `kapak.json` (dosya stili; `bg: cork|dark`, `photo`, `crop`, `name`, `title[2]`, `title_red`, `stamp` ≤16 karakter; `motor/kapak.py` dokümanına bak). Son 7 videonun kapaklarıyla aynı düzeni art arda kullanma. `uret.sh final` kapağı ilk 2 kareye gömer.

## 6. Render
`bash sinematik/motor/uret.sh videolar/<klasör> final` (90 sn ≈ 5-7 dk; yarıda kalırsa aynı komut kaldığı yerden sürer) → `video.mp4` (< 90 MB) + `kapak.jpg`. Arka planda çalıştır. Bitince 3-4 kare çıkarıp bak (ilk kare kapak, ikinci saniyede yüz + kanca).
Yedek (sinematik hat bozulursa): eski motor `scenes.py` + `python3 tools/viral.py render videolar/<klasör>` (örnekler `engine/ornekler/`, `videolar/2026-11-1*/scenes.py`).

## 7. Açıklama (`aciklama.txt`)
- **İlk yorum (`ilk_yorum.txt`, zorunlu):** iki seçenekli soru + paylaşım çağrısı, konuya özel; ör. "Hürrem mi bitirdi, kibri mi? 1 ya da 2 yaz. Bunu en yakın arkadaşına gönder, o ne derdi?" Metricool'da `firstCommentText` olarak dört paylaşımın hepsine eklenir.
- **Toplam en fazla 100 karakter, 4 hashtag dahil.** Emoji yok. `#osmanlıtreni` / "osmanlı treni" etiketini KULLANMA (kullanıcı yalnızca tek bir video için istemişti). Merak uyandıran tek cümle + 4 hashtag. Python ile `len()` kontrol et.
- YouTube başlığı (`baslik.txt`): en fazla 70 karakter, kanca gibi.

## 8. Depoya gönder
```
git add videolar/<klasör> takvim.md && git add -f videolar/<klasör>/build/storyboard.py && git commit -m "<konu> videosu" && git push origin main
```
`img/` ve `build/` .gitignore'da; video, kapak, metinler, sahne.js, storyboard.py (-f ile) ve README girer. Push sonrası kontrol:
`curl -sI https://raw.githubusercontent.com/medyagemreklamcilik-sudo/acaba/main/videolar/<klasör>/video.mp4` → 200.

## 9. Metricool'da planla (platform başına zirve saat)
Her platform **ayrı bir paylaşım** olarak, kendi zirve saatinde planlanır (Metricool en iyi saat verisi, Kasım 2026):

| Platform | Saat | providers | ağ verisi |
|---|---|---|---|
| Facebook | 12:00 | `[{"network":"facebook"}]` | `"facebookData": {"type": "REEL"}` |
| YouTube | 16:00 | `[{"network":"youtube"}]` | `"youtubeData": {"title": "<baslik.txt>", "type": "short", "privacy": "public", "madeForKids": false, "category": "EDUCATION", "tags": ["tarih", "osmanlı", ...]}` |
| TikTok | 18:00 | `[{"network":"tiktok"}]` | `"tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE", "title": "<aciklama.txt>"}` |
| Instagram | 20:00 | `[{"network":"instagram"}]` | `"instagramData": {"type": "REEL", "showReelOnFeed": true}` |

Takvim satırında saat yazıyorsa (EKSTRA) bölme yapma: dört platform tek paylaşımda o saatte gider. Video gün içinde hazırlanıyorsa saati geçmiş platformu bir sonraki günün aynı saatine değil, hemen sonraki en yakın uygun saate (en az 15 dk sonrası) koy ve raporda belirt.

Her paylaşım için `createScheduledPost` — blogId `7651740`, tarih `<YYYY-MM-DD>T<SAAT>:00+03:00`, info (yalnızca o platformun ağ verisini ekle):
```json
{"autoPublish": true, "draft": false, "text": "<aciklama.txt>",
 "media": ["https://raw.githubusercontent.com/medyagemreklamcilik-sudo/acaba/main/videolar/<klasör>/video.mp4"],
 "videoThumbnailUrl": "https://raw.githubusercontent.com/medyagemreklamcilik-sudo/acaba/main/videolar/<klasör>/kapak.jpg",
 "providers": [{"network":"<platform>"}],
 "publicationDate": {"dateTime": "<YYYY-MM-DD>T<SAAT>:00", "timezone": "Europe/Istanbul"},
 "<platform>Data": {...},
 "firstCommentText": "<ilk_yorum.txt>", "hasNotReadNotes": false, "shortener": false, "smartLinkData": {"ids": []}, "descendants": [], "mediaAltText": []}
```
İlk paylaşımın yanıtındaki `media`/`videoThumbnailUrl` (static.metricool.com) adreslerini sonraki üç paylaşımda kullanmak yeterlidir.
`VIDEO_THUMBNAIL_NOT_APPLICABLE` hatası gelirse `videoThumbnailUrl` olmadan bir kez daha dene (kapak zaten videonun ilk karesi). Başka hata verirse bir kez yeniden dene, yine olmazsa raporda mesajı olduğu gibi yaz ve takvimde durumu `hazır` bırak (Metricool planı 15 Kasım'da yükseltildi; aylık gönderi limiti artık sorun değil).
Dört paylaşım da başarılıysa takvimde durumu `planlandı` yap, commit + push.

## 10. Rapor
- `python3 tools/analiz.py <klasör>` ile kanca kontrolünü çalıştır; "Tarihle başlıyor" ya da "İlk 0.6 sn'de ekranda yazı yok" uyarısı varsa planlamadan önce düzelt.
Kullanıcıya kısa Türkçe özet: konu, süre, yayın tarihi ve platform saatleri, açıklama, tartışmalı/emin olunmayan noktalar, Metricool planner linki.
