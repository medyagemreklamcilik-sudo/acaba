# Salih Bozok: Başkomutan yaversiz gidemez (sinematik dosya, uzun video)

- Süre: 659.7 sn (≈11 dk), 1080x1920, 30 fps. Ses: ElevenLabs Cavit (eleven_v4), 6 parça birleştirildi (`build/parca`).
- Mekânlar: `board` (mantar pano, polaroid + ip), `dark` (karanlık stüdyo, nokta portre, başlık), `map` (Selanik → Manastır → İstanbul → Muş/Halep → Samsun…Ankara).
- Üretim: `build/storyboard.py` (sahneler, kelimeye bağlı nesneler) → `python3 build/derle.py` → `sahne.js` + `build/events.json`.
  Yerleşim, kamera (odak + pano sonu geri çekilme), BEATS ve TIMELINE (1880–1945) otomatik.
- Ses: `python3 audio.py` → `build/mix.wav` (re minör dron + seyrek piyano, kâğıt/raptiye/ip/daktilo efektleri, kanca ve 10 Kasım'da silah sesi, koridor saati).
- Render: `bash build/render2.sh` (270 karelik parçalar, yarıda kalırsa devam eder) → birleştir + ses + kapak ilk 2 kare.
- Kapak: `kapak.json` → `motor/kapak.py` → `kapak.jpg`.
- Metin: `tts.txt`. YouTube: `baslik.txt`, `aciklama.txt` (bölümler), `etiketler.txt`, `ilk_yorum.txt`.

Not: "Başkomutan yaversiz gidemez!" sözü anılarda aktarıldığı şekliyle, videoda "anlatılanlara göre" diye verilir. Ölüm döşeği fotoğrafları kullanılmadı.

## Sahne tablosu
| zaman | mekân | nesneler |
|---|---|---|
| 0:00.00 | dark | TETİĞİ ÇEKTİ |
| 0:04.28 | dark | 10 KASIM 1938 · DOLMABAHÇE, ATATÜRK, counter |
| 0:13.44 | board | tabanca, HEDEFİNİ BULMADI, SALİH BOZOK, 3 YIL |
| 0:20.80 | dark | NEDEN?, SELANİK |
| 0:30.10 | map | SELANİK · 1881 |
| 0:37.44 | board | SELANİK LİMANI, TÜRKÇE, RUMCA, LADİNO, BULGARCA |
| 0:46.84 | board | 1881, MUSTAFA, SALİH, UZAKTAN AKRABA, AYNI SOKAKLAR |
| 1:05.72 | board | NURİ, BİR YAŞ KÜÇÜK, 3, BİR İMPARATORLUK YIKILACAK, BİR CUMHURİYET DOĞACAK |
| 1:17.02 | board | ALİ RIZA EFENDİ †, ZÜBEYDE HANIM, doc |
| 1:39.12 | dark | MATEMATİK ÖĞRETMENİ, MUSTAFA, KEMAL, OLGUN · KUSURSUZ |
| 1:46.66 | board | RÜŞTİYE, MANASTIR ASKERİ İDADİSİ, AYNI YATAKHANE, AYNI TALİM |
| 1:58.94 | map | route, MANASTIR |
| 2:02.64 | dark | MANASTIR · İDADİ, ŞİİR, TARİH, HÜRRİYET, GECE · FISILTIYLA |
| 2:14.50 | map | route |
| 2:16.54 | board | İSTANBUL · HARBİYE, MEKTEB-İ HARBİYE, 1903, MUSTAFA KEMAL, 1905 |
| 2:28.94 | dark | subaylar, İKİ AYRI UÇ, AYRILMIYORLAR |
| 2:36.08 | board | JANDARMA, MAKEDONYA, EŞKIYA, BALKANLAR, KÖYLER BASILIYOR |
| 2:48.20 | board | doc, SALİH BEY |
| 2:55.24 | dark | hurriyet, HÜRRİYET · 1908, SELANİK · 1908 |
| 3:05.60 | board | 1909, HAREKET ORDUSU, hareket, KURMAY BAŞKANI: MUSTAFA KEMAL |
| 3:16.14 | dark | II. ABDÜLHAMİD, counter, TAHT |
| 3:22.06 | map | route, ALATİNİ KÖŞKÜ |
| 3:28.28 | board | ALATİNİ KÖŞKÜ, MUHAFIZ: SALİH |
| 3:32.30 | dark | DÜŞÜNSENE, ARKADAŞIN: TAHTI İNDİREN ORDUDA, SEN: KAPISINDA NÖBETTE |
| 3:40.50 | board | 1912, GERİ ÇEKİLİŞ, doc, SELANİK · 1912 |
| 3:53.54 | board | SELANİK, ARTIK BAŞKA BİR ÜLKE, GÖÇ YOLLARI, ZÜBEYDE HANIM, İSTANBUL’A SIĞINDI |
| 4:04.32 | map | SELANİK |
| 4:07.96 | dark | BİR DAHA HİÇ DÖNEMEDİ, SEN OLSAN?, NE HİSSEDERDİN? |
| 4:16.08 | board | 1914, ÇANAKKALE · 1915, ANAFARTALAR, CONKBAYIRI, DURDURULAMAZ DENİLEN ORDU DURDU |
| 4:28.60 | map | route, MUŞ, BİTLİS, route, 7. ORDU |
| 4:37.40 | dark | MUSTAFA KEMAL PAŞA, BAŞYAVER ARANIYOR, salih, SALİH |
| 4:41.60 | board | YAVER NE DEMEK?, KOMUTANIN GÖLGESİ, suriyeg, MEKTUP, KAPI |
| 4:56.00 | dark | yuruyus, ÖMRÜNÜN SONUNA KADAR |
| 5:03.26 | board | 1918, doc, İŞGAL ALTINDA İSTANBUL |
| 5:09.68 | map | route, SAMSUN, route, AMASYA, route |
| 5:17.54 | board | 23 NİSAN 1920 · ANKARA, BÜYÜK MİLLET MECLİSİ, YAVER |
| 5:26.26 | board | YOZGAT, ÇAPANOĞLU İSYANI, MECLİSE TEHDİT, SALİH BEY |
| 5:39.98 | board | SAKARYA · 1921, BÜYÜK TAARRUZ, İZMİR · 1922, 1923, cumhuriyet |
| 5:54.46 | board | doc, İSYANIN ŞEHRİNDEN, SONRA BİLECİK, counter, TÜRKİYE İŞ BANKASI · KURUCU |
| 6:09.00 | board | 1934, ATATÜRK, BOZOK, BOZOK = YOZGAT |
| 6:23.48 | board | SALİH BOZOK, NURİ, KIZ KARDEŞİ DÜRRİYE İLE EVLENDİ, ARTIK AKRABA, NURİ CONKER |
| 6:36.00 | board | ÇANKAYA SOFRASI, K. ATATÜRK · 1935, ÇANKAYA KÖŞKÜ, HEP AYNI YÜZ: SALİH |
| 6:50.22 | dark | SENİN DE BÖYLE BİR ARKADAŞIN VAR MI?, HİÇ GİTMEMİŞ BİRİ |
| 6:57.44 | board | 1937, NURİ CONKER †, ÜÇ ÇOCUKTAN BİRİ YOK, ikili, SARSILDI |
| 7:09.94 | board | ALARM, BURUN KANAMASI, KAŞINTI, doc, DİNLENMEYİ REDDETTİ |
| 7:29.76 | board | SALİH BEY, SAVARONA · YAZ 1938, DOLMABAHÇE · SONBAHAR, HER GÜN O KAPIDA |
| 7:41.04 | dark | ataturk, KİLO, SARARAN YÜZ, UZAYAN UYKULAR, FISILTI |
| 7:53.12 | dark | ELLİ YILLIK ARKADAŞIN, SEN NE YAPARDIN? |
| 7:57.58 | board | doc, UMUT, doc, BU SEFER UYANMADI |
| 8:12.30 | dark | DOLMABAHÇE, SESSİZLİK, SAAT |
| 8:20.06 | dark | 10 KASIM 1938 · SABAH, counter, KALBİ DURDU |
| 8:26.54 | dark | salih, SON KEZ |
| 8:33.80 | dark | KAPI, tabanca |
| 8:39.10 | board | doc, ANLATILANLARA GÖRE |
| 8:44.46 | dark | “BAŞKOMUTAN YAVERSİZ GİDEMEZ!” |
| 8:48.42 | board | SALİH BOZOK, HASTANE, KALBİ ÇOK AZ FARKLA ISKALADI |
| 8:55.32 | dark | YAŞIYOR, AMA BİR YARASI VAR, SADECE GÖĞSÜNDE DEĞİL |
| 9:02.94 | dark | BAZEN İNSAN, BİRİNİ KAYBEDİNCE KENDİNDEN DE BİR PARÇA KAYBEDER. |
| 9:07.46 | board | SON YOLCULUK, DOLMABAHÇE · KASIM 1938, TRENLE ANKARA’YA, MİLYONLAR |
| 9:16.74 | board | SALİH BOZOK, MECLİS, O ADAM ARTIK YOK |
| 9:26.06 | dark | counter, HAYATININ EN UZUN ÜÇ YILI |
| 9:32.30 | board | 1941, 60 YAŞINDA, doc, NURİ CONKER’İN MEZARI |
| 9:51.54 | board | İKİSİ YAN YANA, CEBECİ · ANKARA, ANITKABİR, ÜÇÜNCÜSÜ: ANITKABİR |
| 10:01.54 | board | CEMİL S. BOZOK, “HEP ATATÜRK’ÜN YANINDA”, CAN DÜNDAR, FİLM · 2010, VEDA |
| 10:24.40 | dark | SAVAŞLAR ANTLAŞMALAR DEVRİMLER, VE ARKALARINDA ADINI DUYMADIĞIMIZ İNSANLAR |
| 10:34.12 | dark | ORDU KURMADI, DEVLET KURMADI, salih, 50 YIL · TEK BİR KİŞİ |
| 10:43.02 | dark | yuruyus, YAVERSİZ GİTMESİNE RAZI OLMADI |
| 10:47.78 | dark | SADAKAT, HAYATINDAN VAZGEÇMEK Mİ?, YAŞAMAYA DEVAM ETMEK Mİ?, YORUMLARA YAZ |

## Görsel kaynakları
- `img/abdulhamid.jpg` ← https://images.ntv.com.tr/images/c0332952-d788-434e-87a6-0a52875e391c.jpg?format=webp&amp;width=1200&amp;height=630
- `img/alatini.jpg` ← https://cdn.kulturenvanteri.com/wp-content/uploads/2023/01/AHSEL063-scaled-e1710793738364.jpg
- `img/anitkabir.jpg` ← https://img-s1.onedio.com/id-53ff3b88f8b095ef0673bb8a/rev-0/w-1200/h-990/f-jpg/s-67a6e43de633b319af1c6e5b719114ebe575a230.jpg
- `img/ankara.jpg` ← https://iasbh.tmgrup.com.tr/b2d095/1200/675/17/0/744/409?u=https://isbh.tmgrup.com.tr/sbh/2025/04/22/milletin-meclisi-105-yasinda-1745352505300.jpeg
- `img/ataturk.jpg` ← https://media.licdn.com/dms/image/v2/D4E22AQHhG0UkpU8U5Q/feedshare-image-high-res/feedshare-image-high-res/0/1698574018194?e=2147483647&v=beta&t=09IZ30NWbcnye0YDpgTwp8jMqnluh3PzfUh_YB1Hop8
- `img/balkan.jpg` ← https://imgcdn.ensonhaber.com/old/content/2022/05/07/3d1dcde464d545860bb6701ba6e752e5.jpg
- `img/balkan2.jpg` ← https://i.pinimg.com/originals/4b/e3/bb/4be3bbc983237032edabf5908174df7e.jpg
- `img/balkan3.jpg` ← https://www.gunebakis.com.tr/sites/1262/uploads/2025/07/04/birinci-dunya-savasi-ve-trabzon-8.jpg
- `img/canakkale.jpg` ← https://i.pinimg.com/originals/10/bd/8f/10bd8f9bde9d11ec9177458055930ac3.jpg
- `img/canakkale2.jpg` ← https://i.pinimg.com/originals/50/34/ad/5034ad071245a390a98022c21e4e9c0b.jpg
- `img/cankaya.jpg` ← https://i.pinimg.com/originals/a5/9c/53/a59c533c14819c95dbcde9bab30bf30f.jpg
- `img/cebeci.jpg` ← https://cdn.kulturenvanteri.com/wp-content/uploads/2020/10/DSCF3651-scaled.jpg
- `img/cebeci2.jpg` ← https://cdn.kulturenvanteri.com/wp-content/uploads/2020/10/DSCF3647-scaled.jpg
- `img/cenaze.jpg` ← https://habereksprescomtr.teimg.com/haberekspres-com-tr/uploads/2024/11/ataturks-funeral-november-19-1938-16221077935.jpg
- `img/cenaze2.jpg` ← https://baskentgazetecomtr.teimg.com/baskentgazete-com-tr/imgs/101120211213509271511.jpg
- `img/cumhuriyet.jpg` ← https://www.konhaber.com/sahifeler/upload/2024/10/29/1730183601.jpg
- `img/cumhuriyet2.jpg` ← https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1692000/1693293.jpg
- `img/dolma.jpg` ← https://cdn.fotoatlas.net/wp-content/uploads/2023/12/gri_96_r_14_a25_036-scaled.jpg
- `img/dortlu.jpg` ← https://dergi.salom.com.tr/uploads/news/281020204H9csdtGJFHySdoIMztjzEbyh.jpg
- `img/galata.jpg` ← https://www.weltmuseumwien.at/pics/307490/VF_6974.jpg
- `img/harbiye.jpg` ← https://i.pinimg.com/originals/e0/04/65/e0046513de5ac9ee9e58cc5686a90786.jpg
- `img/hareket.jpg` ← https://i.pinimg.com/originals/c6/5d/81/c65d8121688e288c70f3da8b23745595.png
- `img/hareket2.jpg` ← https://www.isteataturk.com/gorseller/1507492664_ataturk.png
- `img/hurriyet.jpg` ← https://tarihvetoplumlar.com/wp-content/uploads/2020/05/Merzifon.jpg
- `img/hurriyet2.jpg` ← https://i.pinimg.com/originals/3c/31/2c/3c312c80a4d3aea6323eb4e048812746.png
- `img/hurriyet3.jpg` ← https://1.bp.blogspot.com/-jK3VmlcENDA/XmFBNTdo3PI/AAAAAAAA0AM/wy_ycIJyG8wddnE6CT0tFtJSZ_ea0UrSQCLcBGAsYHQ/s1600/II.MesrutiyetinIlaniAlmanBasininda.jpg
- `img/ikili.jpg` ← https://ilerigazetesicomtr.teimg.com/ilerigazetesi-com-tr/uploads/2025/05/2025/05-mayis/18-mayis/nuri-conker-kimdir-2.jpg
- `img/isbank.jpg` ← https://foto.sondakika.com/haber/2020/01/25/is-bankasi-deprem-kampanyasina-5-milyon-tl-bagis-12852186_8030_amp.jpg
- `img/isgal.jpg` ← https://i.pinimg.com/originals/2e/d8/3f/2ed83f1e83fe38aac26ece0c7ddf946b.jpg
- `img/isgal2.jpg` ← https://www.worldatlas.com/r/w1200-q80/upload/75/00/48/shutterstock-785842756-s3cdn.jpg
- `img/izmir.jpg` ← https://www.kocbayi.com.tr/getmedia/22c86aa8-53cc-4608-8cf4-969caeee4017/1200_sporakademisi-ata-binicilik1.jpg.aspx?width=1200&height=675&ext=.jpg
- `img/jandarma.jpg` ← https://i.pinimg.com/originals/80/91/40/8091405447270dae391499faa0a8e843.jpg
- `img/jandarma2.jpg` ← https://i.pinimg.com/originals/70/c2/67/70c267461ac677cc5a743d16c268dbc0.jpg
- `img/kapi.jpg` ← https://www.bizimyaka.com/sites/358/uploads/2022/11/09/172661-1755272868.jpg
- `img/kitapA.jpg` ← https://cdn.dsmcdn.com/ty851/product/media/images/20230428/1/333739332/58080223/1/1_org_zoom.jpg
- `img/kitapB.jpg` ← https://img.kitapyurdu.com/v1/getImage/fn:1130550/wh:84730144f/miw:200/mih:200
- `img/kitapC.jpg` ← https://img.kitapyurdu.com/v1/getImage/fn:11612332/wi:800/wh:44c84620f
- `img/kitapfoto.jpg` ← https://img.kitapyurdu.com/v1/getImage/fn:12136757/wi:800/wh:5ac886707
- `img/manastir.jpg` ← https://www.altinrota.org/assets/images/uploads/articles/global/2020-06-11-194234-manastir-askeri-idadisi-ogrenimi-ve-burada-kisiligini-etkileyen-olaylar-insanlar-6-1526904985.jpg
- `img/meclis.jpg` ← https://i.ytimg.com/vi/hqMucaRcFkw/maxresdefault.jpg
- `img/meclisic.jpg` ← https://img.yeniankara.com.tr/rcman/Cw1200h675q95gc/storage/files/images/2025/11/10/2025-11-10t134941-nk1u.jpg
- `img/mkgenc.jpg` ← https://media.licdn.com/dms/image/v2/C5622AQHVhEQL9tb94Q/feedshare-shrink_1280/feedshare-shrink_1280/0/1615658315628?e=2147483647&v=beta&t=y3h-uaTOtpOnfYBMUP-hRKeig8C5q5auoiLFpVAPK_Q
- `img/mkgenc2.jpg` ← https://atam.gov.tr/wp-content/uploads/2023/06/Ataturk-Portreleri-71-scaled.jpg
- `img/nuri.jpg` ← https://i.pinimg.com/originals/c3/f9/9a/c3f99ac1f743e0000edf9b488b2a0521.jpg
- `img/oda.jpg` ← https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1130000/1130914.jpg
- `img/sakarya.jpg` ← https://pbs.twimg.com/media/E9axWTaWUAk6ziY.jpg
- `img/sakarya2.jpg` ← https://sabirgazetesicom.teimg.com/crop/1280x720/sabirgazetesi-com/uploads/2026/08/polatli.jpg
- `img/salih.jpg` ← https://i.pinimg.com/736x/04/48/25/04482595078d17e5f2575fac356cf3c6.jpg
- `img/savarona.jpg` ← https://7deniznet.teimg.com/crop/1280x720/7deniz-net/uploads/2024/08/1976363.jpg
- `img/selanik.jpg` ← https://i.pinimg.com/originals/06/9f/ce/069fce32a15b0548045ee67af924a622.jpg
- `img/selanikev.jpg` ← https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2434000/2435381.jpg
- `img/sofra.jpg` ← https://isteataturk.com/gorseller/1511200529_ataturk.jpg
- `img/subaylar.jpg` ← https://i.ytimg.com/vi/t96OhnUiPj4/maxresdefault.jpg
- `img/suriye.jpg` ← https://mf.b37mrtl.ru/russian/images/2023.10/original/653a174d02e8bd4e830f7a6a.jpg
- `img/suriyeg.jpg` ← https://foto.haberler.com/haber/2023/10/12/salih-bozok-kimdir-kac-yasinda-nereli-ataturk-16423575_3005_amp.jpg
- `img/tabanca.jpg` ← https://d38vousazc6cao.cloudfront.net/Images/Shop/46/Product/31743/1500/384ac9a3f23d4b44bfc63fe8a33a0e3a.jpg
- `img/talim.jpg` ← https://anbmimarlik.com/wp-content/uploads/2022/03/Harbiye-11.jpg
- `img/teslim.jpg` ← https://www.ww2wrecks.com/wp-content/uploads/2024/11/Internationale_geschiedenis_Eerste_Balkanoorlog_SFA022816365-1024x786.jpg
- `img/teslim2.jpg` ← https://cdn.thecollector.com/wp-content/uploads/2024/01/suurender-thessaloniki-topsin-lithograph.jpg?width=1200&quality=100&dpr=2
- `img/veda.jpg` ← https://www.dreamogram.com/wp-content/uploads/2018/11/veda-ataturk-d05.jpg
- `img/yozgat.jpg` ← https://i.pinimg.com/736x/05/43/fa/0543fa19114086545e9be4bb5e94f46e.jpg
- `img/yozgat2.jpg` ← https://ilerigazetesicomtr.teimg.com/crop/1280x720/ilerigazetesi-com-tr/uploads/2024/07/2024/07-temmuz/112-temmuz/eski-yozgat1.jpg
- `img/yuruyus.jpg` ← https://i.pinimg.com/originals/66/79/12/66791214e655ba672dfc1882995bd10d.jpg
- `img/zubeyde.jpg` ← https://i.pinimg.com/736x/bd/8e/99/bd8e999ed09a23ed35548db79933f16d.jpg
