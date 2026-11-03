---
name: sinematik
description: Verilen tarih konusundan, tamamen kodla çizilmiş sinematik "tek kesintisiz kamera" videosu üretir (yapay zekâ video üreticisi ve stok görüntü yok). Tek büyük dünya (eski harita, masa, pano) üzerinde kamera süzülür, detaylara dalar, geri çekilip yol alır; gerçek fotoğraf/belgeler dünyaya fiziksel baskı olarak düşer; her cümlenin tek bir kahramanı vardır; görsel vuruşlar söylenen kelimeye oturur. Seslendirme, satır zamanları, görseller, beat tablosu ve format konuya göre otomatik doldurulur. "/sinematik <konu>", "sinematik video", "tek plan kamera", "harita üstünde sinematik anlatım", "cinematic motion video" dendiğinde kullan.
---

# /sinematik — kodla çizilen tek plan sinematik video

Motor: `sinematik/motor/` — `core.js` (v2: düz dünya → WebGL lens → ekran katmanı), `render.js` (Playwright ile kare kare MP4), `geo/dunya.js` (Natural Earth kara/göl/nehir, lon -12…62 / lat 24…62), `geo/relief.jpg` (Natural Earth gölgeli kabartma), `fonts/` (Cinzel, Playfair Display Italic, Caveat, Amiri). `core_v1.js` eski düz (perspektifsiz) sürümdür.
**Varsayılan örnek: `sinematik/ornekler/viyana-seferi/` (belgesel modu, 9:16). Haritalı sade örnek: `sinematik/ornekler/kanuni-viyana-dikey/` (9:16, 1080x1920, 30 fps, 15 sn) — yeni videoya bu klasörü kopyalayarak başla.** (`kanuni-viyana-demo/` 21:9 v1 örneğidir.)

## Stil referansları (kullanıcının verdiği, `sinematik/referanslar/ref01-14.jpg`)
Kullanıcı ayrıca referans vermezse bu görünüm esas alınır; her videoda en az 4-5 tanesi bulunsun:
- **Sıcak sepya / kehribar ışık**, tek yönden (sol üst) gelen ışık havuzu, kenarlara doğru kararma, mum ışığı titremesi (`LOOK.light`, `lightPower`, `CANDLE = true`).
- **Haritaya eğik bakan kamera ve alan derinliği**: yakın ve uzak kısımlar yumuşak bulanık, odak ortada (`tilt` 20-40°, `LOOK.dof`, `focusY`). Detaya dalarken eğim azalır, geri çekilip yol alırken artar.
- **Kabartmalı arazi** (dağlar gölgeli), mavi-gri deniz, mürekkep kıyılar, nehirler (`relief`).
- **Parlayan çizgiler**: bölge sınırları turuncu/kırmızı parlar (`region`), rotalar ışık izi gibi akar (`route` + `glow`), önemli şehir adı altın parlar (`label` `style: 'glow'`).
- **Masa üstü fiziksel objeler**: büyüteç (altındaki haritayı gerçekten büyütür, `magnifier`), pirinç pusula (`compass`), haritaya dikilen kırmızı Osmanlı bayrakları / piyonlar (`flag`), parlayan iğneler (`pin`).
- **Gazete kupürü / dergi sayfası** (Tanin, Servet-i Fünun tarzı): gerçek başlık + gerçek fotoğraf, gövde metni yalnızca gri çizgiler (`newspaper`, `rtl: true` ile Osmanlıca başlık). Yalnızca gazetenin var olduğu dönemlerde (19.-20. yy) kullan; 16. yy için baskı/minyatür/belge kullan.
- **Fiziksel baskılar**: beyaz kenarlı fotoğraf/minyatür düşer, gölgesi oturur (`print`, `fx` ile yağmur, kar, ateş gibi efektler).
- Kaçınılacaklar (referanslarda olsa da kurallara aykırı): rastgele uyarı ikonları, okunmayan küçük etiket yığınları, süs için bant/damga.

## Belgesel modu (varsayılan; kullanıcı isteği: Netflix / yüksek bütçeli tarih belgeseli)
`index.html`'de `core.js`'ten sonra `motor/belgesel.js` yüklenir. Kanal tarih öğreten bir belgesel kanalıdır; her videoda:
- **Satranç taşı ordular** (`army`: `team` 'osm' kırmızı lake / 'hab' fildişi, `rows`, `cols`, `gap`, `S`, `path [[t,lon,lat]...]` söylenen kelimeye göre zamanlanır, `ring {t,lon,lat,r}` kuşatma halkası, `unring`, `king: true` önde kavuklu kral, `kingHide`), tek büyük taş (`king`: lider; yakın plan kahraman). Taşlar haritadan yükselir, yürürken hafif zıplar, gölgeleri ışığın tersine düşer, derinliğe göre bulanıklaşır.
- **Hareket eden gemiler** (`fleet`: `route` nehir/deniz rotası, `t0/t1`, `s0/s1` rota oranı, `n`, `spacing`, `S`): kürekler çalışır, dümen suyu bırakır, rotada yön çevirir.
- **Toplar** (`cannons`, `sink` ile çamura gömülme), **minyatür kale/şehir** (`citadel`: surlar, burçlar, iç şehir, kule), **duman + ateş** (`smoke`).
- **Slow motion**: `SLOMO = [[t0, t1, hız]]` — dramatik anda (yağmur, kar, çarpışma) animasyon ve parçacıklar yavaşlar, ses boğuklaşır (audio.py'de aynı aralıkta alçak geçiren filtre).
- **Hava ve ışık**: `WEATHER` (yağmur, kar; kar bokeh'li), `FLASHES` (şimşek), `RAYS(t)` (ışık huzmeleri + toz), `DARKEN(t)` (fırtınada karartma), `LOOK.teal` (teal-turuncu sinema tonu).
- **Ses**: dron + savaş davulu, ortam (su, yağmur, rüzgâr), vuruşlarda "braam"/top sesi; anlatımın altında otomatik kısılır.
Hikâye kuralları yine geçerli: her satırda tek kahraman (ordu, filo, toplar, kale, kral), gerisi söner; efekt kelimeye oturur.
Örnek: `sinematik/ornekler/viyana-seferi/` (18,9 sn). Yeni belgesel videoya bu klasörü kopyalayarak başla.

## Kullanıcının asıl isteği (aynen uygulanacak şablon)
Aşağıdaki şablondaki köşeli parantezli yerleri **kullanıcıya sormadan** konuya göre doldur (kullanıcı "bana hiçbir şey sorma" dedi):

- **Script / voiceover:** konuyu araştır (WebSearch, en az iki kaynak), metni yaz, seslendir. Türkçe ise Cavit Pancar (`tools/tts.py`, varsayılan ses), İngilizce (History with Berat) ise Peter (`voice.txt` = `ZthjuvLPty3kTMaNKVKb`, `lang.txt` = `en`). İstenen süreye göre kelime sayısı: Cavit ~2,4 kelime/sn, Peter ~2,6 kelime/sn. Süre birkaç saniye taşarsa `ffmpeg -af atempo=` ile en fazla %8 hızlandır.
- **Line timings:** `python3 tools/viral.py voice <klasör>` → `build/aligned.json` (faster-whisper + hizalama). Hızlandırdıysan zamanları aynı oranla böl (`build/words.json`).
- **Photos of the real people/places/objects:** `tools/ydl.py` (Yandex) ile gerçek tarihi görseller; filigransız, doğru kişi. Depoda o konunun görselleri varsa (`videolar/*/img/`) önce onları kullan.
- **Style references:** kullanıcı vermediyse varsayılan görünüm: koyu ceviz masa üstünde eski, yanık kenarlı parşömen harita; mürekkep kıyı çizgileri, mavi-gri deniz, nehirler; kırmızı mürekkep rota; Cinzel büyük etiketler, Playfair italik yıllar; beyaz kenarlı fiziksel baskılar; sıcak renk, yumuşak ışıma, vinyet, film greni.
- **Format:** kullanıcı ölçü belirtmediği sürece **her zaman 9:16, 1080x1920, 30 fps** (dikey). Yatay ancak açıkça istenirse (ör. 21:9, 3840x1646). Süre **seslendirme süresine tam eşit** (`dur` = ses süresi, kare = round(dur*fps)).
- **Dikey için okunurluk:** kahraman kelime ekranda en az ~110 px yükseklik (1080 genişlikte); harita etiketleri `size * z` ≥ 110. Önemli şeyleri ekranın ortasında (y %35-%70) tut; perspektif üst kısmı küçültür ve bulanıklaştırır.

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
- `LOOK` (isteğe bağlı): `tilt` (varsayılan 38°), `fov` (55), `dof` (1), `focusY` (.55), `light` ([.22,.16] ekran oranı), `lightPower`, `bloom`, `grain`, `vignette`, `warm`, `relief` (kabartma gücü, 0 = kapalı), `mblur`, `handheld`.
- `OBJECTS` tipleri (düz dünyada): `city`, `route` (`curve: true` yumuşak eğri, `dash` deniz yolu, `glow: '#ffae4a'` ışık izi), `region` (`pts` lon/lat poligon, parlayan sınır + hafif dolgu), `label` (mürekkep ya da `style: 'glow'`), `circle`, `print`, `newspaper` (`masthead`, `headline`, `img`, `rtl`), `compass`, `magnifier` (`path: [[t,x,y],...]`, `r`, `mag`).
  Ekran katmanında (dik duran / ekrana yazılan): `flag` (dikilen bayrak, `t0` = "düştü/aldı" kelimesi), `pin` (parlayan iğne), `title` (ekran yazısı: `text`, `y` 0-1, `size`, `t0`, `t1`; yalnızca söylenen ifade belgede gösterilmiyorsa).
- `CAMERA`: `{t, x, y, z, tilt, r}` anahtarları (dünya koordinatı, z = piksel/birim, tilt derece). Hızlı yolculuklarda geri çekil (z küçük, tilt büyük), varışta dal (z büyük, tilt küçük). Son anahtar = video sonu.
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
Makinede GPU yok (WebGL SwiftShader ile çalışır, `render.js` bayrakları ekler). 1080x1920 kare ~1 sn; 15 sn ≈ 450 kare, 4 işçiyle ~3-5 dk. Haritada üstte/altta masa görünmesin diye `WORLD.map` kameranın en uzak baktığı yeri de kapsasın (perspektif üst kenarı uzağa taşır).

## Rapor
Kullanıcıya: beat tablosu, süre/format, kullanılan görseller ve kaynaklar, temkinli verilen noktalar; video dosyasını SendUserFile ile gönder.
