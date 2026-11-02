# Osmanlı Sarayında Bir Cariye Olsaydın (uzun YouTube videosu)

- 16:9 · 1920x1080 · 24 fps · ~10:41 (seslendirme 10:29 + end screen kuyruğu)
- Ses: Cavit Pancar (ElevenLabs eleven_v4, ton etiketli `tts.txt`) · Müzik/SFX kodla üretildi (`audio.py`, D hicaz dron + ud-vari pluck, bölüm bölüm ruh hâli)
- Görsel: gerçek görseller (harem fotoğrafları, Melling/Allom gravürleri, Ayvazovski, Vanmour, Levnî) + çöp adam Gülnihal (canvas motoru, `web/`)
- Yükleme: **manuel** (Metricool'a planlanmadı). Başlık `baslik.txt`, açıklama `aciklama.txt`, etiketler `etiketler.txt`, sabit yorum `sabit-yorum.txt`, kapak `kapak.jpg`
- Video dosyası depoya girmez (GitHub 100 MB sınırı): `video.mp4` yerelde üretilir.

## Yapı
Kanca (≤10 sn) → başlık · Mariam'ın köyü · alınış (gösterilmez) · gemi/satış · hediye edilen insanlar · isim değişimi → ŞAFAK · SABAH · ÖĞLE · İKİNDİ · AKŞAM · GECE (sağ üstte YIL + saat rozeti) → dokuz yıl · üç kapı · çırağ çıkma · Dilruba'nın mektupları → Üsküdar · başörtüsü · bugün · 1909 · final sorusu.

## Temkinli verilen noktalar
- Gülnihal/Mariam/Dilruba kurgusal; videoda ve açıklamada "kurgusal hikâye" diye belirtildi.
- "Mendil atma" EFSANE damgasıyla verildi.
- Padişahın yüzü hiç gösterilmedi (yalnızca siluet); Safiye Sultan için güvenilir portre olmadığından yalnızca etiket.
- "Genellikle dokuz yıl" ifadesi kullanıldı; kesin süre değil.

## Yeniden üretim
```
cd uzun-videolar/2026-11-cariye
bash build/ses.sh                      # TTS + hizalama (build/ depoya girmez)
NODE_PATH=../../vendor/claude-animation-skills/kit/node_modules CHROME=/opt/pw-browsers/chromium node render.js stills 12,140
node render.js segments 0,1,2 ...      # build/workers.txt satırları paralel
python3 audio.py                       # audio/mix.wav
```
