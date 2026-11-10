# Salih Bozok: yatay (16:9) sürüm

Dikey videonun (`../salih-bozok`) aynı ses, metin ve görsellerle 1920x1080 yeniden kurgusu. Başka motor ya da dış görüntü yok:
aynı `dosya.js` motoru, aynı storyboard; yalnız yerleşim ve kamera yatay kadraja göre yeniden hesaplandı.

- Üretim: `YATAY=1 python3 ../salih-bozok/build/derle.py` → `sahne.js` + `build/events.json`
  - Pano: polaroid/etiket/belge soldan sağa akar, bantlar ebeveynin altına iner; kadrajda komşu deliller de görünür.
  - Karanlık: yazılar görselin sağında, görsele ortalı sütun olarak durur.
  - Harita: aynı kamera anahtarları, daha geniş görüş.
  - Zaman şeridi 1880–1945, 5 yılda bir etiket, alttan 78 px.
- Görseller: `../salih-bozok/img/` (kopya yok). Ses: `../salih-bozok/build/mix.wav`.
- Render: `bash build/render2.sh` (CRF=20 parçalar) → birleştir + ses + kapak ilk 2 kare.
- Kapak: `kapak.json` (`"size": [1920, 1080]`) → `../../motor/kapak.py` → `kapak.jpg` (YouTube küçük resmi olarak da kullanılır).
