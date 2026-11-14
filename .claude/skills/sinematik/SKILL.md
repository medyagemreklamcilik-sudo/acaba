---
name: sinematik
description: Verilen tarih konusundan, tamamen kodla çizilmiş sinematik "tek kesintisiz kamera" videosu üretir (yapay zekâ video üreticisi ve stok görüntü yok). Tek büyük dünya (eski harita, masa, pano) üzerinde kamera süzülür, detaylara dalar, geri çekilip yol alır; gerçek fotoğraf/belgeler dünyaya fiziksel baskı olarak düşer; her cümlenin tek bir kahramanı vardır; görsel vuruşlar söylenen kelimeye oturur. Seslendirme, satır zamanları, görseller, beat tablosu ve format konuya göre otomatik doldurulur. "/sinematik <konu>", "sinematik video", "tek plan kamera", "harita üstünde sinematik anlatım", "cinematic motion video" dendiğinde kullan.
---

# /sinematik — kodla çizilen tek plan sinematik video

Motor: `sinematik/motor/` (`core.js` kamera + dünya + efektler, `render.js` Playwright ile kare kare MP4, `geo/avrupa.js` Natural Earth kara/göl/nehir verisi, `fonts/` Cinzel, Playfair Display Italic, Caveat).
Örnek: `sinematik/ornekler/kanuni-viyana-demo/` (15 sn, 21:9, 3840x1646, 30 fps; kullanıcının beğendiği ilk video) — yeni videoya bu klasörü kopyalayarak başla, formatı dikeye çevir.

## Kullanıcının asıl isteği (aynen uygulanacak şablon)
Aşağıdaki şablondaki köşeli parantezli yerleri **kullanıcıya sormadan** konuya göre doldur (kullanıcı "bana hiçbir şey sorma" dedi):

- **Script / voiceover:** konuyu araştır (WebSearch, en az iki kaynak), metni yaz, seslendir. Türkçe ise Cavit Pancar (`tools/tts.py`, varsayılan ses), İngilizce (History with Berat) ise Peter (`voice.txt` = `ZthjuvLPty3kTMaNKVKb`, `lang.txt` = `en`). İstenen süreye göre kelime sayısı: Cavit ~2,4 kelime/sn, Peter ~2,6 kelime/sn. Süre birkaç saniye taşarsa `ffmpeg -af atempo=` ile en fazla %8 hızlandır.
- **Line timings:** `python3 tools/viral.py voice <klasör>` → `build/aligned.json` (faster-whisper + hizalama). Hızlandırdıysan zamanları aynı oranla böl (`build/words.json`).
- **Photos of the real people/places/objects:** `tools/ydl.py` (Yandex) ile gerçek tarihi görseller; filigransız, doğru kişi. Depoda o konunun görselleri varsa (`videolar/*/img/`) önce onları kullan.
- **Style references:** kullanıcı vermediyse varsayılan görünüm: koyu ceviz masa üstünde eski, yanık kenarlı parşömen harita; mürekkep kıyı çizgileri, mavi-gri deniz, nehirler; kırmızı mürekkep rota; Cinzel büyük etiketler, Playfair italik yıllar; beyaz kenarlı fiziksel baskılar; sıcak renk, yumuşak ışıma, vinyet, film greni.
- **Format:** kullanıcı ölçü belirtmediği sürece **her zaman 9:16, 1080x1920, 30 fps** (dikey). Yatay ancak açıkça istenirse (ör. 21:9, 3840x1646). Süre **seslendirme süresine tam eşit** (`dur` = ses süresi, kare = round(dur*fps)).
- **Dikey için:** örnek sahne 21:9'dur; dikeye geçerken `format.json` ve `FORMAT`'ı 1080x1920 yap, ekran dar olduğu için kamera `z` değerlerini yaklaşık 1/3'e indir (aynı alan görünsün), etiketleri büyüt (`size * z` ≥ 110 px) ve önemli şeyleri ekranın ortasında (y %30-%70) tut.

### THE STYLE
- Bütün video, tek büyük dünya üzerinde TEK kesintisiz kamera hareketi. Kesme yok, slayt değişimi yok. Kamera süzülür, detaya dalar, yol almak için geri çekilir, yeniden dalar.
- Hareket yumuşak ve çekilmiş gibi: her başlangıç/duruş yumuşak (motor zaman tabanlı Hermite eğrisi kullanır, C1 sürekli). Kamera asla ölü durmaz: beklemelerde bir sonraki yöne yavaşça kayar (iki anahtarı hafif kaydırarak koy). Hafif el kamerası, hızlı harekette hareket bulanıklığı, film greni, yumuşak ışıma, vinyet (motor otomatik yapar).
- Gerçek fotoğraf ve belgeler dünyaya fiziksel nesne olarak düşer (baskı, kâğıt, kupür), hikâyenin geçtiği yere.

### STORYTELLING AND READABILITY RULES (en önemli)
1. Her anlatım satırına tek fikir. Her satırın ekranda TEK kahramanı var (bir fotoğraf, bir kelime ya da bir belge); geri kalan her şey geri çekilir (`BEATS[].hero`, `mapDim`).
2. Her ifade ekranda bir kez görünür, asla tekrarlanmaz. Anlatıcı söylüyorsa ya gerçek belgede göster ya ekrana yaz, ikisini birden asla.
3. Dolgu yazı yok. Belgelerdeki gövde metni okunmaya çalışılacak kelimeler değil, kâğıt gibi okunan yumuşak gri çizgiler olsun.
4. Büyük, okunur tipografi: kahraman kelimeler çok büyük, etiketler asla küçük değil. Telefonda bir saniyede okunmuyorsa ya çok küçük ya çok fazla. (Pratik ölçü: kahraman kelime ekranda yüksekliğin en az %8'i; `size * z` ≥ 0,08 × H.)
5. Az, çoktur. Hikâyenin parçası olmayan süs (rastgele bant, damga, not, fazla etiket) yok.
6. Görsel anlar tam söylenen kelimeye oturur: kelime söylenirken daire çizilir, vuruşta damga iner (`t0` = kelimenin `s` zamanı).

### PROCESS
- İnşa etmeden önce **beat tablosu** yaz: zaman → anlatım → ekrandaki tek kahraman → ekrandaki yazı. Kullanıcıya göster. (Kullanıcı soru istemiyorsa tabloyu `README.md`'ye ve son rapora koy, beklemeden devam et.)
- Acele etme. Kalite hızdan önemli. Daha fazla şey eklemek yerine tasarım, akıcı hareket ve netlik.
- Son render'dan önce kendi işini kontrol et: her beat'ten still (`node sinematik/motor/render.js <klasör> stills 0.3,2.5,...`) ve kamera hareketlerinden ardışık kare dizileri çıkar; kalabalık, zor okunan, üst üste binen ya da sarsılan/aniden duran her şeyi düzelt.
- Son MP4'ü seslendirmeyle senkron, tam bu formatta teslim et.

## Görünüm: "dosya" stili (kullanıcının referansları, `sinematik/referans/dosya/01-16.png`)
Kullanıcı bu görünümü istedi; yeni videolarda varsayılan budur. Motor: `motor/dosya.js` (örnek: `ornekler/fahreddin-dosya/`, `index.html` bu motoru ve Plex Mono / Special Elite / Cormorant / Oswald fontlarını yükler). Eski parşömen görünümü `motor/core.js` ile yalnızca istenirse.
- Dünya: koyu camgöbeği belgesel haritası (taralı kara, ince ışıyan kıyı), üstünde mantar pano(lar) (`BOARDS`). Kamera koyu haritadan sıcak panoya, oradan tekrar haritaya süzülür.
- Nesneler: `halftone` (siyah üstünde nokta portre + kırmızı ışık), `polaroid` (gri tonlu baskı, siyah mono isim bandı, kırmızı raptiye, `brackets` odak köşeleri), `tag` (manila dosya etiketi: DOSYA + büyük yıl), `doc` (daktilo belge: başlık, gri satır, karartma, daktiloyla yazılan anahtar cümle + kırmızı daire, isteğe bağlı damga), `thread` (iki raptiye arası kırmızı ip), `glowdot` (turuncu ışıyan şehir + mono etiket + kesikli kare + nişangâh), `title` (ince büyük serif, yanlarda çizgi), `strike` (mono yazı, söylenince kırmızı çizgiyle üstü çizilir), `region`.
- Ekran katmanı: altta yıl çizgisi (`TIMELINE`), turuncu toz zerreleri, camgöbeği gölge / sıcak ışık renk, spot vinyet, gren.
- Kamera yavaş: ekran hızı ~400 px/sn'yi geçmesin (kullanıcı "kamera çok hızlı" dedi); nesneleri kameranın yolu üstünde sırala, uzak zıplama yok.

## Hızlı hat: storyboard derleyici (varsayılan, 15 Kasım)
Günlük videolar ve yeni sinematikler artık bununla üretilir (`/viral` adım 5-6'da tam örnek):
- `build/storyboard.py`: `SC(mekân, ifade, [nesneler])` sahneleri, nesneler kelimeye bağlı (`P` polaroid, `TI` başlık, `TG` etiket, `DC` belge, `BD` bant, `TH` ip, `HT` nokta portre, `CT` sayaç, `ST` üstü çizili, `RG` bölge yazısı, `GD`/`RT` harita noktası/rota).
- `python3 sinematik/motor/derle.py <klasör>` → yerleşim, kamera, BEATS, TIMELINE otomatik (`YATAY=1` ile 16:9 sürüm `<klasör>-yatay/`).
- `bash sinematik/motor/uret.sh <klasör> stills|final` → kontrol sayfası ya da kapaklı, sesli `video.mp4`; ses `motor/ses.py` (`SHOT=1` glitch anlarında silah sesi).

## Kapak (zorunlu, kullanıcı isteği)
TikTok kişisel hesapta `videoThumbnailUrl`'yi yok sayar ve kapağı videonun içinden seçer; Fahreddin videosunda ızgarada yalnızca "1918" etiketi göründü. Bu yüzden her sinematik videoda:
1. `kapak.json` yaz ve `python3 sinematik/motor/kapak.py <klasör>/kapak.json <klasör>/kapak.jpg` ile "dosya" stilinde kapak üret: mantar pano (`bg: cork`) ya da karanlık (`dark`), raptiyeli gri polaroid + siyah mono isim bandı, kırmızı ip ile bağlı manila yıl etiketi, kırmızı lastik damga ve **üstte iki satır kalın başlık** (siyah bant + kırmızı kenar; `title_red` ile bir satır kırmızı kutu). Örnek: `sinematik/ornekler/fahreddin-dosya/kapak.json`.
2. Başlık videonun kanca vaadi olsun, kısa ve şok/soru (ör. "PADİŞAHA BİLE / TESLİM OLMADI"); konu adı (ör. ÇÖL KAPLANI) damgaya gider. Satır başına ~14 karakter. Diğer kanal kapaklarıyla aynı okunurlukta olmalı: 3:4 ızgara kırpmasında (y 240-1680) ve 150 px genişlikte okunur. Yazı yüzün üstüne binmez, ip yüzün üstünden geçmez.
3. Kapağı videonun **ilk 2 karesine** göm (TikTok ilk kareyi alır):
   `ffmpeg -i video.mp4 -loop 1 -i kapak.jpg -filter_complex "[1:v]scale=1080:1920,format=yuv420p[k];[0:v][k]overlay=enable='lt(n\,2)':shortest=1[v]" -map "[v]" -map 0:a -c:v libx264 -preset slow -b:v 4300k -maxrate 6500k -bufsize 9000k -pix_fmt yuv420p -c:a copy -movflags +faststart video_k.mp4`
4. Metricool'da `videoThumbnailUrl` olarak da `kapak.jpg` ver. Dosya GitHub raw için 100 MB'ın altında olmalı (yukarıdaki bit hızı 2:24 için ~78 MB).

## Klasör ve dosyalar
```
sinematik/ornekler/<slug>/
  tts.txt          seslendirme (etiketli)      format.json  {"w","h","fps"}
  index.html       motor + sahne yükleyici      sahne.js     FORMAT, WORLD, IMAGES, OBJECTS, CAMERA, BEATS
  img/             gerçek görseller             audio.py     ses + sessiz sinematik alt katman → build/mix.wav
  README.md        beat tablosu, kaynaklar, görsel kaynakları
```
`sahne.js` öğeleri:
- `WORLD`: projeksiyon (`lon0`, `lat0`, `k` birim/derece, `latc`), harita dikdörtgeni `map {x,y,w,h}`, ızgara sınırları. Başka bölge gerekirse `motor/geo/` için Natural Earth'ten yeni `.js` üret (bkz. örnekteki Python kırpma adımı, `ne_50m_land`, `ne_50m_lakes`, `ne_50m_rivers_lake_centerlines`).
- `OBJECTS` tipleri: `city` (mürekkep nokta), `route` (çizilerek uzayan kırmızı rota, `dash` deniz yolu), `label` (mürekkeple soldan sağa yazılan büyük etiket + italik alt satır), `circle` (elle çizilen daire), `print` (düşen fiziksel baskı; `caption`, `tone`, `fx(ctx,t,x,y,w,h)` ile yağmur/kar gibi efekt).
- `CAMERA`: `{t, x, y, z}` anahtarları (dünya koordinatı, z = piksel/birim). Hızlı yolculuklarda geri çekil (z küçük), varışta dal (z büyük). Son anahtar = video sonu.
- `BEATS`: `{t, hero:[id...], mapDim}`; kahraman olmayanlar yumuşakça geri çekilir.

## Komutlar
```
cd /home/user/acaba
python3 tools/viral.py voice sinematik/ornekler/<slug>          # ses + kelime zamanları
export NODE_PATH=/home/user/acaba/vendor/claude-animation-skills/kit/node_modules CHROME=/opt/pw-browsers/chromium
cd sinematik && node motor/render.js ornekler/<slug> stills 0.5,3,6     # kontrol kareleri
bash ornekler/<slug>/build/render.sh                                  # 4 işçiyle paralel render → build/silent.mp4
cd ornekler/<slug> && python3 audio.py && ffmpeg -i build/silent.mp4 -i build/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5 -shortest video.mp4
```
Makinede GPU yok; 4K kare ~1-2 sn, 1080x1920 kare daha hızlı. 15 sn ≈ 450 kare, 4 işçiyle ~5-10 dk.

## Rapor
Kullanıcıya: beat tablosu, süre/format, kullanılan görseller ve kaynaklar, temkinli verilen noktalar; video dosyasını SendUserFile ile gönder.
