import sys, json, urllib.request, urllib.parse
for q in sys.argv[1:]:
    u="https://api.europeana.eu/record/v2/search.json?"+urllib.parse.urlencode({"wskey":"api2demo","query":q,"media":"true","rows":"12","qf":"TYPE:IMAGE"})
    d=json.load(urllib.request.urlopen(u,timeout=30))
    print("##",q,d.get("totalResults"))
    for it in d.get("items",[]):
        t=(it.get("title") or [""])[0][:70]; print("  ",t,"|",(it.get("dataProvider") or [""])[0][:30],"|",(it.get("edmIsShownBy") or [""])[0])
