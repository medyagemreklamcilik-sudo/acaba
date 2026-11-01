---
name: analiz
description: acaba.nolurdu Shorts/Reels videolarında izleyicinin kaçıncı saniyede, neden bıraktığını bulur ve somut düzeltme önerir. Metricool'dan Instagram/TikTok/YouTube verisini çeker; YouTube Studio izleyici tutma CSV'si ya da ekran görüntüsü verilirse saniye saniye analiz yapar ve her düşüşü o anda söylenen cümle ve ekrandaki sahneyle eşleştirir. "/analiz", "/analiz <klasör>", "neden izlemeyi bıraktılar", "retention", "izleyici tutma" dendiğinde ya da bir retention grafiği/CSV'si paylaşıldığında kullan.
---

# /analiz: Shorts izleyici tutma analizi

Jake Schincariol'un `youtube-agent-skill` paketindeki `yt-retention` mantığının (MIT, `tools/LICENSE-yt-retention.txt`)
yalnızca kısa video için uyarlanmış hâli. Uzun video kısmı kullanılmaz.

Araç: `python3 tools/analiz.py <videolar/klasör> [--csv f.csv | --points "0:100,3:70,..."] [--avg SN --hold3 YÜZDE] [--platform p --views n] [--out]`

Araç videonun kendi zaman çizelgesini okur: `kelimeler.json` (ya da `build/aligned.json`) hangi saniyede ne söylendiğini,
`scenes.py` o saniyede ekranda hangi görselin ve yazının olduğunu verir. Her düşüş için muhtemel nedeni
(duraklama, yavaş anlatım, sayı yığını, durağan görüntü, yazı ağırlıklı kart, konu geçişi, kancanın erken cevaplanması,
kapanış) ve düzeltmeyi yazar.

## 1. Veriyi topla
Metricool brand `7651740`. `getAnalyticsDataByMetrics`, aralık: videonun yayın günü ile bugün arası.
- Instagram Reels: `IGRE02` (tarih), `IGRE03` (metin), `IGRE23` (izlenme), `IGRE24` (ortalama izleme sn), `IGRE28` (ilk 3 sn'yi geçenlerin %'si), `IGRE11` (erişim), `IGRE07` (yorum)
- TikTok: `TKPO02`, `TKPO05`, `TKPO06` (süre), `TKPO07` (izlenme), `TKPO13` (tamamını izleme %), `TKPO15` (ort. izleme), `TKPO09` (yorum). Boş gelebilir.
- YouTube: `YTVP02`, `YTVP17`, `YTVP06`, `YTVP08` (ort. izleme), `YTVP11`. Boş gelebilir.
Satırı videoya yayın tarihi ve açıklama metniyle eşleştir (`aciklama.txt`).

Saniye saniye eğri yalnızca YouTube Studio'da var: Studio → video → Analiz → Etkileşim → izleyici tutma grafiği →
indir. Kullanıcı CSV gönderirse `--csv`; ekran görüntüsü gönderirse grafikten 10-20 nokta oku (en az 0, 1, 2, 3, 5, 10 sn ve
her belirgin kırılma) ve `--points "sn:%,..."` ile ver. Shorts eğrisi sonda %100'ü aşabilir (döngü), bu iyidir.

## 2. Çalıştır
Her video için `--out` ile çalıştır (`<klasör>/analiz-<platform>.md` yazılır). Eşikler (Reels, ilk 3 sn'yi geçen):
60+ iyi, 45-60 orta, 45 altı zayıf. Eğride kanca kaybı (0-3 sn) 25 altı sağlıklı.

## 3. Kullanıcıya sun
Türkçe, kısa. Önce **tek en büyük sızıntı ve tek düzeltme**, sonra her bırakma anı için:
`X. saniye, %Y kayıp · söylenen cümle · ekrandaki sahne · neden · öneri`. Ortalama izleme süresinden yapılan
çıkarımın tahmin olduğunu, kesin saniye için Studio eğrisi gerektiğini söyle. Aracın neden etiketleri ipucudur;
cümleyi ve sahneyi kendin de değerlendir, mekanik nedeni yoksa içerik nedenini (konu dağıldı, vaat tutulmadı,
bilgi tekrar ediyor) yaz.

## 4. Öğrenimleri kaydet
Kanal geneline dair çıkan her kalıbı `ogrenimler.md`'ye ekle (tablo + madde). `/viral` metin yazmadan önce bu dosyayı okur;
yani analizden çıkan ders bir sonraki videoya otomatik yansır. Commit + push.
