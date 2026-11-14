# Sahne derleyicisi: storyboard (sahneler + kelimeye bağlı nesneler) -> sahne.js + build/events.json
# Zamanlar build/aligned.json'daki kelime başlangıçlarından; pano/karanlık sahnelerde yerleşim ve kamera otomatik.
import json, math, re, sys, os
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
A = json.load(open(f'{D}/aligned.json')); SZ = json.load(open(f'{D}/imgs.json'))['size']
TR = str.maketrans({'İ': 'i', 'I': 'ı'})
norm = lambda w: re.sub(r'[^0-9a-zçğıöşü]', '', w.translate(TR).lower())
TOK = [norm(x['w']) for x in A]
CUR = [0]
def T(ph):
    q = [norm(w) for w in ph.split()]; q = [w for w in q if w]
    for i in range(CUR[0], len(TOK) - len(q) + 1):
        if TOK[i:i + len(q)] == q: CUR[0] = i; return A[i]['s']
    sys.exit(f'bulunamadı: {ph!r} (imleç {CUR[0]}: {" ".join(TOK[CUR[0]:CUR[0]+8])})')
END = A[-1]['e'] + 2.3; FPS = 30; NF = round(END * FPS)

# ---------- nesne kurucuları ----------
def P(img, at, name=None, w=760, crop=None, **k): return dict(type='polaroid', img=img, at=at, name=name, w=w, crop=crop, **k)
def TG(at, small, big, sub=None, w=680, **k): return dict(type='tag', at=at, small=small, big=big, sub=sub, w=w, **k)
def BD(at, text, red=False, size=78, **k): return dict(type='band', at=at, text=text, red=red, size=size, **k)
def DC(at, head, key, keyAt=None, h=1150, **k): return dict(type='doc', at=at, head=head, key=key, keyAt=keyAt, w=1000, h=h, **k)
def TI(at, text, size=170, **k): return dict(type='title', at=at, text=text, size=size, **k)
def ST(at, text, strikeAt, size=130, **k): return dict(type='strike', at=at, text=text, strikeAt=strikeAt, size=size, **k)
def HT(img, at, crop=None, w=1150, **k): return dict(type='halftone', img=img, at=at, crop=crop, w=w, **k)
def RG(at, text, size=60, **k): return dict(type='region', at=at, text=text, size=size, **k)
def CT(at, frm, to, fmt, size=260, **k): return dict(type='counter', at=at, frm=frm, to=to, fmt=fmt, size=size, **k)
def TH(a, b, at=None): return dict(type='thread', a=a, b=b, at=at)
def GD(at, ll, label, **k): return dict(type='glowdot', at=at, ll=ll, label=label, **k)
def RT(at, pts, dur=1.2, **k): return dict(type='route', at=at, pts=pts, dur=dur, **k)

PL = {'selanik': (22.94, 40.64), 'manastir': (21.33, 41.03), 'istanbul': (28.97, 41.01), 'canakkale': (26.4, 40.15), 'mus': (41.5, 38.75), 'bitlis': (42.1, 38.4),
      'diyarbakir': (40.22, 37.91), 'halep': (37.16, 36.2), 'sam': (36.3, 33.51), 'samsun': (36.33, 41.29), 'amasya': (35.83, 40.65), 'erzurum': (41.27, 39.9), 'sivas': (37.02, 39.75),
      'ankara': (32.85, 39.93), 'yozgat': (34.8, 39.82), 'polatli': (32.15, 39.58), 'afyon': (30.54, 38.76), 'izmir': (27.14, 38.42), 'hatay': (36.16, 36.2), 'bilecik': (29.98, 40.14), 'adana': (35.32, 37.0)}
def proj(lo, la): return ((lo - 20) * 600 * math.cos(math.radians(30)), (46 - la) * 600)


YATAY = bool(os.environ.get('YATAY')); FW, FH = (1920, 1080) if YATAY else (1080, 1920)
def yerlestir_yatay(o, kind, h, w, L):
    """Yatay (16:9) yerleşim: pano soldan sağa akar, bantlar ebeveynin altına; karanlıkta yazılar görselin sağına."""
    o['_h'], o['_w'] = h, w; big = L['big']; ty = o['type']
    visual = ty in ('polaroid', 'tag', 'doc', 'halftone')
    if kind == 'board':
        if ty == 'band' and big is not None:
            px, py, ph_, pw = big['x'], big['y'], big['_h'], big['_w']
            o['y'] = py + ph_ / 2 + (o['size'] * .8 if big['type'] in ('tag', 'doc') else -40) + L['nb'] * (o['size'] * 1.9); L['nb'] += 1
            o['x'] = px + (90 if L['nb'] % 2 else -60); o['x'] = min(max(o['x'], px - pw / 2 + w / 2 - 60), px + pw / 2 - w / 2 + 60)
            o['rot'] = o.get('rot', [-.04, .03, -.02, .05][L['nb'] % 4]); o['_parent'] = big['id']; return
        o.pop('x', None); o.pop('y', None)
        o['x'] = L['cx'] + w / 2; o['y'] = L['side'] * (150 if visual else 60) - (h / 2 - 450 if h > 900 else 0) * 0
        if ty in ('title', 'strike'): o['_cy'] = o['y']; o['y'] = o['_cy'] - h / 2 + o['size'] * .74
        L['side'] = -L['side']; L['cx'] += w + 170; L['nb'] = 0
        if 'rot' not in o and visual: o['rot'] = [-.035, .03, -.02, .045, -.05, .02][(L['k'] + int(L['cx'])) % 6]
        if visual or ty == 'counter': L['big'] = o
        return
    # karanlık
    if 'x' in o and 'y' in o and not visual:  # elle verilmiş (yalnız tek sütun sahneler)
        if big is None:
            if ty in ('title', 'strike'): o['_cy'] = o['y'] + h / 2 - o['size'] * .74
            return
    if visual:
        x0 = max(L['cx'], L['sw'] + 220) if big is None and 'sw' in L else (L['cx'] if big is None else big['x'] + big['_w'] / 2 + 220 + (L.get('colw', 0)))
        o['x'] = x0 + w / 2; o['y'] = 0; L['big'] = o; L['col_y'] = None; L['colw'] = 0; L['cx'] = o['x'] + w / 2 + 220; return
    if big is None:  # yalnız yazı: ortada üst üste
        o['x'] = 0; top = L['cy']
        o['y'] = top + h / 2
        if ty in ('title', 'strike'): o['_cy'] = o['y']; o['y'] = top + o['size'] * .74
        L['cy'] = top + h + 110; L['sw'] = max(L.get('sw', 0), w / 2); return
    # görselin sağında sütun
    if L['col_y'] is None: L['col_y'] = -big['_h'] / 2 + 40
    top = L['col_y']; o['x'] = big['x'] + big['_w'] / 2 + 140 + w / 2; L['colw'] = max(L.get('colw', 0), w + 140)
    o['y'] = top + h / 2
    if ty in ('title', 'strike'): o['_cy'] = o['y']; o['y'] = top + o['size'] * .74
    L['col_y'] = top + h + 90; o['_colof'] = big['id']
SCENES = []
def SC(kind, ph, items=(), year=None, cam=None, glitch=None, boom=False, lead=.3):
    t = T(ph) - lead; CUR0 = CUR[0]
    SCENES.append(dict(kind=kind, t=t, items=list(items), year=year, cam=cam, glitch=glitch or [], boom=boom, cur=CUR0))

exec(open(f'{D}/storyboard.py').read())

# ---------- çözümleme ----------
OBJ, SPC, BEAT, GL, TLK, BOOMS = [], [], [], [], [], []
def ph_t(at, prev):
    if at is None: return prev + .4
    if isinstance(at, (int, float)): return prev + at
    return T(at) - .05
def height(o):
    if o['type'] == 'polaroid':
        W, H = SZ[o['img']]; c = o.get('crop') or [0, 0, 1, 1]; ph = o['w'] * (H * c[3]) / (W * c[2]); bw = o['w'] * .045
        return ph + bw + bw * (3.6 if o.get('name') else 1.2), o['w'] + 2 * bw
    if o['type'] == 'halftone':
        W, H = SZ[o['img']]; c = o.get('crop') or [0, 0, 1, 1]; return o['w'] * (H * c[3]) / (W * c[2]), o['w']
    if o['type'] == 'tag': return o['w'] * .52, o['w']
    if o['type'] == 'doc': return o['h'], o['w']
    if o['type'] == 'title':
        n = o['text'].count('\n') + 1; return o['size'] * o.get('lh', 1.05) * n, o['size'] * .78 * max(len(s) for s in o['text'].split('\n'))
    if o['type'] == 'strike': return o['size'] * 1.2, o['size'] * .66 * len(o['text'])
    if o['type'] == 'counter': return o['size'] * (1.5 if o.get('sub') else 1.1), o['size'] * 3
    if o['type'] == 'band': return o['size'] * 1.7, o['size'] * .66 * len(o['text']) + o['size'] * 1.2
    if o['type'] == 'region': return o['size'] * 1.2, o['size'] * .9 * len(o['text'])
    return 0, 0
nid = [0]
def newid(p): nid[0] += 1; return f'{p}{nid[0]}'

for si, sc in enumerate(SCENES):
    t_s = sc['t']; t_e = SCENES[si + 1]['t'] if si + 1 < len(SCENES) else END + 1
    CUR[0] = sc['cur']
    kind = sc['kind']; ox = 0 if kind == 'map' else 40000 * (si + 1)
    prev = t_s + .25; ev = []  # odak olayları
    side = -1; cy = 0; last_big = None; nb = 0; R_ = (si * 37) % 11
    L = dict(cx=0, side=-1, big=None, nb=0, col_y=None, cy=0, k=len(OBJ))
    for it in sc['items']:
        o = {k: v for k, v in it.items() if k not in ('at',)}
        if o['type'] == 'thread':
            o['t0'] = ph_t(it['at'], prev) if it['at'] is not None else None; OBJ.append(o); o['_sc'] = si; continue
        t0 = ph_t(it['at'], prev); prev = t0; t0 += o.pop('shift', 0); o['t0'] = round(t0, 3)
        o.setdefault('id', newid(o['type'][:2])); o['_sc'] = si
        if kind == 'map':
            OBJ.append(o); continue
        h, w = height(o)
        if YATAY:
            yerlestir_yatay(o, kind, h, w, L); OBJ.append(o); ev.append(o); continue
        if o['type'] in ('band',) and last_big is not None and 'x' not in o:
            px, py, ph_, pw = last_big['x'], last_big['y'], last_big['_h'], last_big['_w']
            o['x'] = px + (-1 if last_big.get('_side', 1) > 0 else 1) * min(250, pw * .25); o['y'] = py + ph_ / 2 + (o['size'] * .8 if last_big['type'] in ('tag', 'doc') else -40) + nb * (o['size'] * 1.9); nb += 1
            o['x'] = min(max(o['x'], px - pw / 2 + w / 2 - 60), px + pw / 2 - w / 2 + 60)
            o['rot'] = o.get('rot', [-.04, .03, -.02, .05][nb % 4]); cy = max(cy, o['y'] + o['size'] * 1.2 + 100)
            o['_h'], o['_w'] = h, w; o['_parent'] = last_big['id']
        else:
            if 'x' not in o:
                if kind == 'board' and o['type'] in ('polaroid', 'tag', 'doc'): o['x'] = side * (230 if o['type'] != 'doc' else 120); o['_side'] = side; side = -side
                else: o['x'] = 0
            if 'y' not in o:
                o['y'] = cy + h / 2
                if o['type'] in ('title', 'strike'): o['_cy'] = o['y']; o['y'] = cy + o['size'] * .74
            elif o['type'] in ('title', 'strike'): o['_cy'] = o['y'] + h / 2 - o['size'] * .74
            cy = max(cy, o.get('_cy', o['y']) + h / 2 + (150 if kind == 'board' else 110)); nb = 0
            if 'rot' not in o and kind == 'board' and o['type'] in ('polaroid', 'tag', 'doc'): o['rot'] = [-.035, .03, -.02, .045, -.05, .02][(R_ + len(OBJ)) % 6]
            o['_h'], o['_w'] = h, w
            if o['type'] in ('polaroid', 'tag', 'doc', 'halftone', 'counter'): last_big = o
        OBJ.append(o)
        ev.append(o)
    if YATAY and kind == 'dark':  # görsel yanındaki yazı sütununu görselin ortasına hizala
        for b in [q for q in OBJ if q.get('_sc') == si and q['id'] in {c.get('_colof') for c in OBJ if c.get('_sc') == si}]:
            col = [c for c in OBJ if c.get('_colof') == b['id']]; top = min(c.get('_cy', c['y']) - c['_h'] / 2 for c in col); bot = max(c.get('_cy', c['y']) + c['_h'] / 2 for c in col)
            dy = b['y'] - (top + bot) / 2
            for c in col:
                c['y'] += dy
                if '_cy' in c: c['_cy'] += dy
    # yerel -> dünya
    for o in OBJ:
        if o.get('_sc') == si and 'x' in o and kind != 'map': o['x'] += ox
        if o.get('_sc') == si: o['space'] = kind; o['_t1'] = t_e + .6
    for o in [o for o in OBJ if o.get('_sc') == si and o['type'] == 'thread']:
        def ref(r):
            mine = [x for x in OBJ if x.get('_sc') == si and x['type'] != 'thread']
            m = re.fullmatch(r'(tag|doc)(\d)', r)
            if m: return [x for x in mine if x['type'] == m.group(1)][int(m.group(2)) - 1]
            return next(x for x in mine if x.get('img') == r)
        a, b = ref(o['a']), ref(o['b'])
        o['from'], o['to'] = a['id'], b['id']; o['id'] = newid('th')
        if o['t0'] is None: o['t0'] = round(max(a['t0'], b['t0']) + .45, 3)
    # kamera
    def fit(objs, cap=.82):
        x0 = min(o['x'] - o['_w'] / 2 for o in objs); x1 = max(o['x'] + o['_w'] / 2 for o in objs)
        y0 = min(o.get('_cy', o['y']) - o['_h'] / 2 for o in objs); y1 = max(o.get('_cy', o['y']) + o['_h'] / 2 for o in objs)
        z = min(cap, .84 * FW / (x1 - x0 + 60), (.70 if YATAY else .68) * FH / (y1 - y0 + 60))
        return (x0 + x1) / 2, (y0 + y1) / 2 + 30 / z, z
    cam = []
    CUR[0] = sc['cur']
    if kind == 'map':
        for k in sc['cam']:
            tt = k[0] if isinstance(k[0], (int, float)) else T(k[0]); tt = t_s + tt if isinstance(k[0], (int, float)) else tt
            x, y = proj(*PL[k[1]]) if isinstance(k[1], str) else proj(*k[1]); cam.append([round(tt, 3), round(x + (k[3] if len(k) > 3 else 300 / k[2]), 1), round(y + (k[4] if len(k) > 4 else 0), 1), k[2]])
        BEAT.append(dict(t=round(t_s + .3, 3), hero=None, mapDim=.05))
    else:
        groups = []
        for o in ev:
            join = o.get('j', o['type'] in ('band',) or (kind == 'dark' and o['type'] in ('title', 'strike', 'counter') and groups and o['t0'] - groups[-1][-1]['t0'] < 9))
            if o.get('j') == 0: join = False
            if join and groups: groups[-1].append(o)
            else: groups.append([o])
        keys = []
        for gi, g in enumerate(groups):
            nxt = groups[gi + 1][0]['t0'] if gi + 1 < len(groups) else t_e
            # grup içindeki her yeni öğe kamerayı birleşik kutuya kaydırır
            for k, o in enumerate(g):
                x, y, z = fit(g[:k + 1], cap=g[0].get('zcap', .8))
                ta = o['t0'] + (.15 if k else 0.1)
                if gi == 0 and k == 0 and o['t0'] > t_s - .3: keys.append([round(t_s - .45, 3), x, y + 40 / z, z * .9])
                if k and o['t0'] - .7 > keys[-1][0] + .3: px_, py_, pz_ = keys[-1][1:]; keys.append([round(o['t0'] - .7, 3), px_, py_ + 12 / pz_, pz_ * 1.01])
                keys.append([round(ta, 3), x, y, z])
                hero = [q['id'] for q in g[:k + 1]] + [th['id'] for th in OBJ if th.get('_sc') == si and th['type'] == 'thread' and th['to'] in [q['id'] for q in g[:k + 1]]]
                hero += [p['id'] for p in OBJ if p.get('_sc') == si and p['type'] == 'region']
                BEAT.append(dict(t=round(o['t0'], 3), hero=hero, mapDim=.25 if kind == 'board' else .15))
            x, y, z = keys[-1][1:]
            gap = nxt - keys[-1][0]
            if gi + 1 < len(groups):
                if gap > 1.0: keys.append([round(nxt - min(1.1, gap * .45), 3), x, y + 18 / z, z * 1.02])
            else:
                if gap > 4.5 and kind == 'board' and len(ev) > 1:
                    keys.append([round(keys[-1][0] + 1.6, 3), x, y + 15 / z, z * 1.015])
                    X, Y, Z = fit(ev, cap=.6); keys.append([round(t_e + .4, 3), X, Y, max(Z, .2)])
                    BEAT.append(dict(t=round(keys[-2][0] + .3, 3), hero=None, mapDim=.1))
                else: keys.append([round(t_e + .4, 3), x, y + 50 / z, z * 1.05])
        # sıralı ve tekil zaman
        keys.sort(key=lambda k: k[0]); kk = []
        for k in keys:
            if kk and k[0] - kk[-1][0] < .12: kk[-1] = k
            else: kk.append(k)
        cam = [[k[0], round(k[1], 1), round(k[2], 1), round(k[3], 4)] for k in kk]
    SPC.append(dict(t=round(t_s, 3), s=kind, cam=[dict(t=k[0], x=k[1], y=k[2], z=k[3]) for k in cam]))
    if sc['year'] is not None: TLK.append(dict(t=round(t_s + .4, 3), v=sc['year'], dur=1.2))
    CUR[0] = sc['cur']
    for g in sc['glitch']:
        g0 = T(g[0]) - .05 if isinstance(g[0], str) else g[0]; GL.append([round(g0, 3), round(g0 + g[1], 3), g[2]])
    if sc['boom']: BOOMS.append(round(t_s + .3, 3))

# ---------- JS ----------
def js_obj(o):
    q = {}
    ty = o['type']
    for k, v in o.items():
        if k.startswith('_') or v is None or k in ('a', 'b', 'j', 'zcap', 'focus'): continue
        q[k] = v
    if ty == 'polaroid':
        if o.get('name'): q['nameT'] = round(o['t0'] + o.get('nameDelay', .45), 3)
    if ty == 'doc':
        c0 = CUR[0]; st_ = round(T(o['stamp']['t']) - .05, 3) if o.get('stamp') and isinstance(o['stamp']['t'], str) else None
        c1 = CUR[0]; CUR[0] = c0
        q['keyT'] = round(T(o['keyAt']) - .05 if isinstance(o.get('keyAt'), str) else o['t0'] + (o.get('keyAt') or .35), 3)
        q.setdefault('keyDur', round(min(1.3, .06 * len(o['key'])), 2)); q.setdefault('keySize', 70 if len(o['key']) < 16 else 58)
        q.setdefault('circleT', round(q['keyT'] + q['keyDur'] + .25, 3)); q.setdefault('rowsBefore', 3); q.setdefault('rowsAfter', 5); q.setdefault('seed', len(OBJ) % 40 + 1)
        q.pop('keyAt', None); CUR[0] = max(CUR[0], c1)
        if o.get('stamp'): s = dict(o['stamp']); s['t'] = st_ if st_ is not None else round(q['keyT'] + s['t'], 3); q['stamp'] = s
    if ty == 'strike': q['tStrike'] = round(T(o['strikeAt']) if isinstance(o['strikeAt'], str) else o['t0'] + o['strikeAt'], 3); q.pop('strikeAt')
    if ty == 'counter': q['from'] = q.pop('frm'); q['fmt'] = '__JS__' + o['fmt']; q.setdefault('dur', 1.2); q.setdefault('solid', '#f1efe8'); q.setdefault('glow', 'rgba(0,0,0,.6)')
    if o.get('crossT_at'): q['crossT'] = round(T(o['crossT_at']) - .05, 3); q.pop('crossT_at')
    if ty == 'glowdot': lo, la = PL[o['ll']] if isinstance(o['ll'], str) else o['ll']; q.pop('ll'); q['lon'], q['lat'] = lo, la; q.setdefault('size', 68)
    if ty == 'route': q['pts'] = [list(PL[p]) if isinstance(p, str) else p for p in o['pts']]; q['t1'] = round(o['t0'] + o.get('dur', 1.2), 3); q.pop('dur'); q['hide'] = round(o['_t1'], 3)
    if ty == 'title' and o.get('lineAt'): q['lineT'] = [round(T(x) - .05 if isinstance(x, str) else o['t0'] + x, 3) for x in o['lineAt']]; q.pop('lineAt')
    if ty in ('polaroid', 'tag', 'doc', 'band', 'title', 'strike', 'counter', 'halftone', 'glowdot', 'region', 'thread'):
        if 't1' not in q: q['t1'] = round(o['_t1'], 3)
    if ty == 'thread': q.setdefault('dur', .7); q.setdefault('sag', .11)
    for k in ('x', 'y', 'rot'):
        if k in q: q[k] = round(q[k], 3 if k == 'rot' else 1)
    s = json.dumps(q, ensure_ascii=False)
    return re.sub(r'"__JS__(.*?)"(?=[,}])', lambda m: m.group(1).replace('\\"', '"'), s)
# lineAt/keyAt/strikeAt zamanları için imleç: nesne sırasıyla (sahne imlecinden) yeniden ara
out = []
for si, sc in enumerate(SCENES):
    CUR[0] = sc['cur']
    for o in [o for o in OBJ if o.get('_sc') == si]: out.append(js_obj(o))
imgs = sorted(SZ.keys())
BEAT.sort(key=lambda b: b['t'])
TL = dict(t0=.6, t1=round(END - 1, 2), years=globals().get('TL_YEARS', [1880, 1945]), every=globals().get('TL_EVERY', 5 if YATAY else 10), tick=1, **({'bottom': 78} if YATAY else {}), keys=[dict(t=0, v=globals().get('TL_START', 1938.86))] + TLK)
IMGP = '../salih-bozok/' if YATAY else ''
js = f"""// {globals().get("BASLIK", "Sinematik dosya")} ({END:.1f} sn, 9:16).
// build/derle.py + build/storyboard.py ile üretildi; elle düzenleme yerine storyboard'u değiştirip yeniden derle.
const FORMAT = {{ w: {FW}, h: {FH}, fps: 30, dur: {NF} / 30 }};
const WORLD = {{ lon0: 20, lat0: 46, k: 600, latc: 30 }};
const IMAGES = {{}}; for (const k of {json.dumps(imgs)}) IMAGES[k] = `{IMGP}img/${{k}}.jpg`;
const SPACES = {json.dumps(SPC, ensure_ascii=False)};
const CAMERA = SPACES[0].cam;
const OBJECTS = [
{(','+chr(10)).join(out)}
];
const BEATS = {json.dumps(BEAT, ensure_ascii=False)};
const GLITCH = {json.dumps(GL)};
const TIMELINE = {json.dumps(TL)};
"""
OUT = R + '-yatay' if YATAY else R; os.makedirs(f'{OUT}/build', exist_ok=True); open(f'{OUT}/sahne.js', 'w').write(js)
json.dump(dict(s=[s['t'] for s in SPC], g=GL, b=BOOMS, kinds=[s['s'] for s in SPC], o=[json.loads(re.sub(r'"fmt": [^,}]*', '"fmt": 0', js_o)) for js_o in out], end=END), open(f'{OUT}/build/events.json', 'w'), ensure_ascii=False)
print('sahne', len(SPC), 'nesne', len(OBJ), 'kare', NF, 'süre', round(END, 2))
