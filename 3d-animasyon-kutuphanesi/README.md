# 3D Animasyon Kütüphanesi (acaba.nolurdu)

Günlük videolar gerçek tarihi görsellerle devam ediyor; bu klasör **yedekte bekleyen** 3D stil içindir.
Bir gün 3D'ye (ya da sadece 3D kancaya) geçmek istersek karakterler, kostümler, objeler, mekânlar ve hareketler hazır.

Motor: `/zach-d-films` skill'inin three.js motoru (MIT, artemnovitckii/claude-animation-skills) + bizim kütüphanemiz.
Görseller: `katalog/` (her öğenin bir fotoğrafı + toplu sayfalar `katalog/00-*.jpg`).

## Klasör
```
3d-animasyon-kutuphanesi/
  README.md                ← bu dosya
  videolara-gore.md        ← önceki videolarımızda hangi sahne için hangi öğeler
  katalog/                 ← önizleme görselleri
  motor/
    index.html, render.mjs  (render.mjs: CHROME=/opt/pw-browsers/chromium GL=swiftshader)
    src/main.js, human.js, props.js, anim.js ...   (motorun kendisi)
    src/shots.js            ← şu an KATALOG; yeni video için kendi çekim listeni yaz
    src/kutuphane/
      ortak.js        malzemeler (kumaş, altın, bronz, ahşap), kanvas dokuları, bayrak, tuğra, hat satırları
      karakterler.js  karakter(rol), giydir(h, kostüm), BASLIK.*
      proplar.js      objeler (PROPLAR.*), hareketli olanlarda .guncelle(t)
      mekanlar.js     mekânlar (MEKANLAR.*), hepsi { guncelle(t) }
      hareketler.js   pozlar ve hareket döngüleri
```

## Karakterler (`karakter('rol', {renk değişikliği})`)
| Osmanlı | | Cumhuriyet / dönem dışı | |
|---|---|---|---|
| padisah | kavuk + sorguç, kürklü mor kaftan | subay_1920 | kalpak, haki palto, kemer |
| sehzade | genç, kaftan, fes | mehmetcik | kabalak (Çanakkale) |
| sehzade_cocuk | küçük şehzade | mebus | kalpak, siyah redingot |
| vezir, sadrazam | mücevveze sarık, kürklü kaftan, uzun sakal | cumhuriyet_beyi | fötr şapka, takım, kravat |
| seyhulislam, ulema | beyaz/koyu cübbe, geniş kol | cumhuriyet_hanimi | 1930'lar elbise, başı açık |
| yeniceri | börk, kısa kaftan, kırmızı çizme | ogretmen | takım, kravat |
| cellat, dilsiz | kırmızı külah / siyah | cocuk | kasket |
| hekim | koyu cübbe, sarık | ingiliz_subay | kep, haki üniforma |
| kahveci, kemanci | fes, cepken | | |
| halk_erkek, halk_kadin | sarık / yaşmak, ferace | | |
| valide_sultan, cariye | hotoz + duvak, kaftan/entari | | |
| dervis | Mevlevi sikkesi, beyaz tennure | | |
| tellak | peştamal | | |

Kendi kostümün: `giydir(makeHuman('archer'), { ust, alt, etek:'kaftan'|'cubbe'|'entari'|'ferace'|'palto', kurk, kusak, kemer, genisKol, yaka, dugme, kravat, bas:'kavuk'|'mucevveze'|'sarik'|'bork'|'fes'|'kalpak'|'sapka'|'hotoz'|'yasmak'|'sikke'|'takke'|'cellat'|'kasket'|'askeriKep'|'kabalak', sakal:'kisa'|'uzun'|'biyik'|'yok', kadin, ten, olcek })`

Gerçek kişiler (Atatürk, padişahlar) birebir modellenmedi; sahnede rolüyle (padişah, subay_1920) temsil edilir, isim alt yazıyla verilir.

## Objeler (`PROPLAR.ad()`)
- **Saray:** taht (`.oturmaY`), tabut (yeşil örtü + kavuk), kemend, yatagan, kilic, kafes, dolap (`.guncelle(t)` kapak açılır), sandik, minder, sedir
- **Belge:** ferman (`.guncelle(0..1)` rulo açılır, tuğralı), **kitap (`.guncelle(t)` sayfa çevrilir)**, muhur, tugraLevha, hokkaKalem
- **Saray entrikası:** zehirSisesi, serbetKadehi
- **Kahvehane:** fincan, cezve, tepsi, nargile, tabure, tavla, mangal
- **Işık:** mesale (titrer), samdan, kandil
- **Askeri:** top (bronz kuşatma topu), gulle, kadirga (kürekler hareketli), kalkan, tufek, siper, duman, ates
- **Cumhuriyet:** **bayrak (`.guncelle(t)` dalgalanır)**, kursu, masa, sandalye, haritaMasasi, lozanMasasi, radyo
- **Yapılar:** cami, minare, ahsapEv, kuyu, mezarTasi({bas:'kavuk'|'fes', yazi}), serviAgaci, sutun, kemer
- **Hayvan:** esek (kulak/kuyruk hareketli), at

## Mekânlar (`MEKANLAR.ad(scene, ayar)`)
sarayIc({gece}), divan, kahvehane, sokak({gece}), meclis (1920, "Hâkimiyet Milletindir"), hamam, mezarlik, cephe, deniz({gece}), acikAlan

## Pozlar / hareketler (`hareketler.js`)
DUR, OTUR, BAGDAS, ISARET, OTUR_ISARET, TEMENNA, SECDE, DUA, ASKER_SELAMI, KOLLAR_BELDE, KOLLAR_KAVUSUK, ELLER_HAVADA, BOGAZ_TUT, KITAP_OKU, KURSU_KONUS,
YURU(t), KOS(t), NEFES(t, poz), YAZ(t), SEMA(t), BOGUL_DUS(f, t) + dusur(h, f), konus(h, t) (ağız), lerpPose(a, b, k)

## Yeni bir 3D video/kanca yapmak
1. `cp -R motor <proje>` ve `ln -s /home/user/acaba/vendor/claude-animation-skills/kit/node_modules <proje>/node_modules` (paketler yoksa `vendor/claude-animation-skills/BU-DEPODA.md`).
2. `<proje>/src/shots.js`'i yaz: `CAPTIONS`, `DURATION`, `SHOTS = [{start, end, build({makeStage})}]`. Örnek çekimler katalogdaki "sahne:" öğelerinde (`motor/src/shots.js` sonu).
3. Ses: ElevenLabs Cavit Pancar (`tools/tts.py`), kelime zamanları `tools/transcribe.py`.
4. Önizleme: `CHROME=/opt/pw-browsers/chromium GL=swiftshader node render.mjs stills 1.2,3.4 stills`
5. Video: `node render.mjs video silent.mp4 30`, sonra ffmpeg ile ses + 1080x1920.
Hız (GPU'suz bulut makinesi): kare başı ~2-6 sn → 5 sn kanca ≈ 10 dk, 2,5 dk video ≈ 5 saat.

Kataloğu yeniden çekmek: `motor/` içinde `node render.mjs stills 0.5,1.5,...,N.5 stills` (N = öğe sayısı, `KATALOG` listesi).

## Low poly karakter (deneme)
`src/kutuphane/lowpoly.js`: `lowPolyAdam({ten, sac, ceket, gomlek, kravat, bas})` köşeli yüzeyli, düz gölgeli yakın çekim karakter (bıyıklı, takım elbiseli).
`a.ifade({ kizgin, saskin, gulumse, kirp, bak:[x,y] })` ifadeler, `lowPolyOda(scene)` sıcak ışıklı bulanık çalışma odası.
Örnek çekim listesi: `motor/src/ornek-lowpoly-shots.js` (4 sn: kararlı bakış + şaşkın yakın çekim). Görseller: `katalog/lowpoly/`.
Not: AI görsel üreticilerinin low poly kalitesine (detaylı eller, kumaş, kalabalık) kodla ulaşılamaz; bu, yakın çekim ve basit sahneler için.
