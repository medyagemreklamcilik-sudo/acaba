import sys, json, os, io, urllib.request, time, concurrent.futures as cf
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__)); import yandex
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"}
out=sys.argv[1]; jobs=json.load(open(sys.argv[2])); per=int(sys.argv[3]) if len(sys.argv)>3 else 8
os.makedirs(out,exist_ok=True); mp=os.path.join(out,"_index.json")
idx=json.load(open(mp)) if os.path.exists(mp) else {}
def grab(a):
    key,i,u=a
    if "wikimedia.org" in u: return None
    try:
        data=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read()
        im=Image.open(io.BytesIO(data)); im.load()
        if min(im.size)<500: return None
        fn=f"{key}_{i}.jpg"; im.convert("RGB").save(os.path.join(out,fn),quality=93)
        return fn,{"url":u,"size":im.size,"q":key}
    except Exception: return None
tasks=[]
for key,q in jobs:
    try: urls,c=yandex.search(q)
    except Exception as e: print("ERR",q,e); continue
    if c: print("CAPTCHA",q)
    for i,u in enumerate(urls[:per]): tasks.append((key,i,u))
    time.sleep(1.5)
with cf.ThreadPoolExecutor(10) as ex:
    for r in ex.map(grab,tasks):
        if r: idx[r[0]]=r[1]; print("OK",r[0],r[1]["size"],flush=True)
json.dump(idx,open(mp,"w"),indent=1)
