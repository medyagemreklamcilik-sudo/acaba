import sys, json, urllib.request, urllib.parse, os, io, concurrent.futures as cf
from PIL import Image
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"}
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
jobs=json.load(open(sys.argv[2]))
idx={}
def search(q,rows):
    u="https://api.europeana.eu/record/v2/search.json?"+urllib.parse.urlencode({"wskey":"api2demo","query":q,"media":"true","rows":str(rows),"qf":"TYPE:IMAGE"})
    return json.load(urllib.request.urlopen(u,timeout=30)).get("items",[])
def grab(args):
    key,i,it=args
    for u in (it.get("edmIsShownBy") or [])+(it.get("edmPreview") or []):
        if "bildindex" in u: continue
        try:
            data=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read()
            im=Image.open(io.BytesIO(data)); im.load()
            if min(im.size)<300: continue
            fn=f"{key}_{i}.jpg"; im.convert("RGB").save(os.path.join(out,fn),quality=92)
            return fn,{"title":(it.get("title") or [""])[0],"provider":(it.get("dataProvider") or [""])[0],"url":u,"rights":(it.get("rights") or [""])[0],"size":im.size}
        except Exception as e:
            continue
    return None
tasks=[]
for key,q,n in jobs:
    try: items=search(q,n)
    except Exception as e: print("ERR",q,e); continue
    for i,it in enumerate(items): tasks.append((key,i,it))
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(grab,tasks):
        if r: idx[r[0]]=r[1]; print("OK",r[0],r[1]["size"],r[1]["title"][:60],flush=True)
mp=os.path.join(out,"_index.json")
old=json.load(open(mp)) if os.path.exists(mp) else {}
old.update(idx); json.dump(old,open(mp,"w"),ensure_ascii=False,indent=1)
