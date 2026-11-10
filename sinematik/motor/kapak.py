"""Sinematik "dosya" stili kapak (1080x1920; yatay için "size": [1920, 1080], "photo_x", "title_cx", "stamp_cx"). Kullanım: python3 kapak.py <kapak.json> <çıktı.jpg>
JSON: {"bg": "cork"|"dark", "photo": "img/x.jpg", "crop": [x0,y0,x1,y1] (0-1), "name": "İSİM BANDI",
       "title": ["SATIR 1", "SATIR 2"], "title_red": 1 (kırmızı kutulu satır no, isteğe bağlı),
       "stamp": "KIRMIZI DAMGA", "tag_big": "1918", "tag_small": "DOSYA", "bottom": "alt mono satır"}
Yazılar TikTok/Instagram ızgarasının görünen bölgesinde (y 300-1600) tutulur."""
import json, sys, os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
F = os.path.join(os.path.dirname(__file__), 'fonts') + '/'
spec = json.load(open(sys.argv[1])); base = os.path.dirname(os.path.abspath(sys.argv[1]))
W, H = spec.get('size', [1080, 1920])  # yatay kapak için "size": [1920, 1080]
R = random.Random(7)

def cork():
    im = Image.new('RGB', (W, H), (140, 95, 55)); d = ImageDraw.Draw(im)
    cols = [(94, 60, 31), (168, 122, 74), (74, 47, 23), (195, 148, 99), (115, 75, 41)]
    for _ in range(90000):
        x, y, r = R.random() * W, R.random() * H, .6 + R.random() * 2.2
        d.ellipse((x - r, y - r, x + r, y + r), fill=cols[R.randrange(len(cols))])
    return im.filter(ImageFilter.GaussianBlur(.6))

def dark():
    im = Image.new('RGB', (W, H), (10, 14, 15)); d = ImageDraw.Draw(im)
    for x in range(0, W, 90): d.line((x, 0, x, H), fill=(18, 26, 28))
    for y in range(0, H, 90): d.line((0, y, W, y), fill=(18, 26, 28))
    return im

bg = cork() if spec.get('bg', 'cork') == 'cork' else dark()
# spot ışığı + vinyet
vg = Image.new('L', (W, H), 0); ImageDraw.Draw(vg).ellipse((-350, 150, W + 350, H - 150), fill=255); vg = vg.filter(ImageFilter.GaussianBlur(220))
bg = Image.composite(bg, Image.new('RGB', (W, H), (8, 6, 4)), vg)
d = ImageDraw.Draw(bg)

def pin(x, y, r=22):
    d.ellipse((x - r + 6, y - r + 9, x + r + 6, y + r + 9), fill=(20, 12, 8))
    for k in range(r, 0, -1):
        t = k / r; c = (int(110 + 120 * (1 - t) ** .5), int(10 + 40 * (1 - t)), int(8 + 30 * (1 - t)))
        d.ellipse((x - k, y - k, x + k, y + k), fill=c)
    d.ellipse((x - r * .45, y - r * .55, x - r * .05, y - r * .15), fill=(255, 150, 140))

def shadow_paste(img, x, y, blur=35, off=(22, 34), alpha=170):
    sh = Image.new('L', img.size, 0); ImageDraw.Draw(sh).rectangle((10, 10, img.size[0] - 10, img.size[1] - 10), fill=alpha)
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); bg.paste((0, 0, 0), (x + off[0], y + off[1]), sh); bg.paste(img, (x, y), img if img.mode == 'RGBA' else None)

# polaroid
ph = Image.open(os.path.join(base, spec['photo'])).convert('L')
c = spec.get('crop', [0, 0, 1, 1]); ph = ph.crop((int(c[0] * ph.width), int(c[1] * ph.height), int(c[2] * ph.width), int(c[3] * ph.height)))
ph = ImageEnhance.Contrast(ph).enhance(1.25)
if spec.get('censor'):
    a, b, c2, d2 = spec['censor']; fx = lambda v: (v - c[0]) / (c[2] - c[0]) * ph.width; fy = lambda v: (v - c[1]) / (c[3] - c[1]) * ph.height
    ImageDraw.Draw(ph).rectangle((fx(a), fy(b), fx(c2), fy(d2)), fill=5)
pw = spec.get('photo_w', 640); phh = int(ph.height * pw / ph.width); ph = ph.resize((pw, phh)); bw = 30
card = Image.new('RGB', (pw + 2 * bw, phh + bw + bw * 3), (236, 235, 230)); card.paste(Image.merge('RGB', [ph] * 3), (bw, bw))
cd = ImageDraw.Draw(card)
if spec.get('name'):
    f = ImageFont.truetype(F + 'PlexMonoSemi.ttf', 38); tw = cd.textlength(spec['name'], font=f)
    cd.rectangle((bw + 14, bw + phh - 34, bw + 14 + tw + 50, bw + phh + 34), fill=(22, 25, 27)); cd.text((bw + 39, bw + phh - 24), spec['name'], font=f, fill=(239, 239, 233))
card = card.convert('RGBA').rotate(spec.get('rot', 2.5), expand=True, resample=Image.BICUBIC)
py0 = spec.get('photo_y', 560); px0 = spec['photo_x'] if 'photo_x' in spec else (W - card.size[0]) // 2 + spec.get('photo_dx', -40)
shadow_paste(card, px0, py0)
pinA = (px0 + card.size[0] // 2, py0 + 40)
# manila etiket + ip
if spec.get('tag_big'):
    tw_, th_ = 400, 210; tag = Image.new('RGBA', (tw_, th_), (0, 0, 0, 0)); td = ImageDraw.Draw(tag)
    td.polygon([(60, 0), (tw_, 0), (tw_, th_), (60, th_), (0, th_ * .7), (0, th_ * .3)], fill=(216, 200, 160))
    td.ellipse((34, th_ / 2 - 20, 74, th_ / 2 + 20), fill=(239, 230, 204), outline=(140, 115, 70), width=4)
    td.text((128, 30), spec.get('tag_small', 'DOSYA'), font=ImageFont.truetype(F + 'PlexMono.ttf', 26), fill=(90, 78, 58))
    td.line((110, 66, tw_ - 26, 62), fill=(120, 105, 80), width=2)
    fb = ImageFont.truetype(F + 'Oswald.ttf', 118); fb.set_variation_by_axes([700]); td.text((104, 58), spec['tag_big'], font=fb, fill=(38, 34, 29))
    tag = tag.rotate(-7, expand=True, resample=Image.BICUBIC); tx, ty = W - tag.size[0] - 50, py0 + card.size[1] + spec.get('tag_dy', 40)
    shadow_paste(tag, tx, ty, blur=25, off=(16, 24), alpha=160); pinB = (tx + 62, ty + tag.size[1] // 2 + 6)
    # sarkan kırmızı ip
    pinC = (px0 + card.size[0] - 46, py0 + card.size[1] - 60)  # polaroidin sağ alt köşesindeki raptiye
    pts = [(pinC[0] + (pinB[0] - pinC[0]) * s / 30, pinC[1] + (pinB[1] - pinC[1]) * s / 30 + math.sin(math.pi * s / 30) * 50) for s in range(31)]
    d.line([(x + 4, y + 6) for x, y in pts], fill=(30, 10, 8), width=7); d.line(pts, fill=(184, 38, 31), width=6); pin(*pinB, 18); pin(*pinC, 18)
pin(*pinA)
# damga
if spec.get('stamp'):
    fs = ImageFont.truetype(F + 'Oswald.ttf', 104); fs.set_variation_by_axes([700]); st = Image.new('RGBA', (1000, 220), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    tw = sd.textlength(spec['stamp'], font=fs); x0 = (1000 - tw) / 2
    sd.rectangle((x0 - 34, 30, x0 + tw + 34, 190), outline=(205, 40, 34, 235), width=12); sd.text((x0, 38), spec['stamp'], font=fs, fill=(205, 40, 34, 235))
    noise = Image.effect_noise(st.size, 90).point(lambda v: 255 if v > 70 else 120); a = st.split()[3]; st.putalpha(Image.composite(a, Image.new('L', st.size, 0), noise))
    st = st.rotate(spec.get('stamp_rot', 7), expand=True, resample=Image.BICUBIC); bg.paste(st, (int(spec.get('stamp_cx', W / 2) - st.size[0] / 2), spec.get('stamp_y', py0 + card.size[1] - 150)), st)
# başlık: siyah bant + beyaz kalın yazı, isteğe bağlı kırmızı satır (kanaldaki kapaklarla aynı okunurluk)
ft = ImageFont.truetype(F + 'Oswald.ttf', spec.get('title_size', 128)); ft.set_variation_by_axes([700]); y = spec.get('title_y', 300)
for i, line in enumerate(spec['title']):
    CX = spec.get('title_cx', W / 2); tw = d.textlength(line, font=ft); bx0 = CX - tw / 2 - 34; red = spec.get('title_red') == i + 1
    d.rectangle((bx0 + 8, y + 10, bx0 + tw + 76, y + ft.size * 1.22 + 10), fill=(0, 0, 0))
    d.rectangle((bx0, y, bx0 + tw + 68, y + ft.size * 1.22), fill=(200, 40, 34) if red else (16, 18, 20))
    if not red: d.rectangle((bx0, y, bx0 + 12, y + ft.size * 1.22), fill=(200, 40, 34))
    d.text((CX - tw / 2 + 6, y + ft.size * .02), line, font=ft, fill=(255, 255, 255)); y += ft.size * 1.32
if spec.get('bottom'):
    fm = ImageFont.truetype(F + 'PlexMonoSemi.ttf', 44); tw = d.textlength(spec['bottom'], font=fm)
    d.rectangle(((W - tw) / 2 - 26, 1596, (W + tw) / 2 + 26, 1666), fill=(12, 14, 15)); d.text(((W - tw) / 2, 1604), spec['bottom'], font=fm, fill=(240, 117, 78))
# gren
g = Image.effect_noise((W, H), 30).convert('RGB'); bg = Image.blend(bg, ImageOps.autocontrast(g), .05)
bg.save(sys.argv[2], quality=93); print('kapak:', sys.argv[2])
