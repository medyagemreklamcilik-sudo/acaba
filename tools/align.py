import json, re, difflib, sys
W=json.load(open(sys.argv[1])); S=open(sys.argv[2]).read().split()
def norm(t):
    t=t.lower().replace("i̇","i")
    t=t.translate(str.maketrans("âîûçğıöşü","aiucgiosu"))
    return re.sub(r"[^a-z0-9]","",t)
# character-level alignment: build char streams with token ids
def stream(tokens):
    cs=[];ids=[]
    for i,t in enumerate(tokens):
        for c in norm(t): cs.append(c); ids.append(i)
    return "".join(cs),ids
a,ai=stream([w["w"] for w in W]); b,bi=stream(S)
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
tok_times={}
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        wi=W[ai[blk.a+k]]; si=bi[blk.b+k]
        tok_times.setdefault(si,[]).append((wi["s"],wi["e"]))
out=[]
for i,t in enumerate(S):
    if i in tok_times:
        s=min(x[0] for x in tok_times[i]); e=max(x[1] for x in tok_times[i])
        out.append({"w":t,"s":s,"e":e})
    else: out.append({"w":t,"s":None,"e":None})
# fill gaps by interpolation
for i,o in enumerate(out):
    if o["s"] is None:
        p=out[i-1]["e"] if i>0 else 0
        n=next((x["s"] for x in out[i+1:] if x["s"] is not None),p+0.3)
        o["s"]=p; o["e"]=n; print("interp",o)
json.dump(out,open(sys.argv[3],"w"),ensure_ascii=False,indent=0)
print(len(out),"tokens")
