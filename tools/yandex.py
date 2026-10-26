import sys, re, json, html, urllib.request, urllib.parse
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"}
def search(q):
    u="https://yandex.com/images/search?"+urllib.parse.urlencode({"text":q,"isize":"large"})
    h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read().decode("utf-8","ignore")
    h2=html.unescape(h)
    urls=re.findall(r'"origUrl":"(https?://[^"]+)"',h2) or re.findall(r'"img_href":"(https?://[^"]+)"',h2)
    if not urls: urls=re.findall(r'img_url=(https?%3A%2F%2F[^&"]+)',h); urls=[urllib.parse.unquote(x) for x in urls]
    seen=[];[seen.append(x) for x in urls if x not in seen]
    return seen, ("captcha" in h.lower() and "smartcaptcha" in h.lower())
if __name__=="__main__":
    for q in sys.argv[1:]:
        r,c=search(q); print("##",q,len(r),"CAPTCHA" if c else "")
        for x in r[:12]: print("  ",x[:160])
