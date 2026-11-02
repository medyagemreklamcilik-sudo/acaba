#!/usr/bin/env python3
"""Yavuz 1512 -> 1520 toprak büyümesi (HyperFrames sahnesi, 1080x1920, ~9 sn).
   python3 build.py            -> work/ klasörü + yavuz-harita.mp4
   python3 build.py --snap 1,4,8
Sınırlar YAKLAŞIKTIR: bugünkü ülke sınırlarından türetilir (Natural Earth 1:50m)."""
import json, math, shutil, subprocess, sys
from pathlib import Path
from shapely.geometry import shape, box, mapping
from shapely.ops import unary_union

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
KIT = ROOT / "vendor/claude-animation-skills/kit"
GEO = ROOT / "engine/geo"
LON0, LON1, LAT0, LAT1 = 8.0, 54.0, 14.0, 49.0
CLAT = math.cos(math.radians(36))
K = 1080 / ((LON1 - LON0) * CLAT)  # px / derece
def P(lon, lat): return ((lon - LON0) * CLAT * K, (LAT1 - lat) * K)

C = {f["properties"]["ADMIN"]: shape(f["geometry"]) for f in json.load(open(GEO / "ne_50m_admin_0_countries.geojson"))["features"]}
U = lambda *n: unary_union([C[x] for x in n])
tr = U("Turkey")
R = {
  "r1512": unary_union([U("Greece", "Bulgaria", "North Macedonia", "Albania", "Kosovo", "Montenegro", "Bosnia and Herzegovina"),
                        C["Republic of Serbia"].intersection(box(10, 30, 30, 44.6)), tr.intersection(box(20, 30, 39.0, 45))]),
  "r1514": tr.intersection(box(39.0, 30, 50, 45)),
  "r1516": U("Syria", "Lebanon", "Israel", "Palestine", "Jordan"),
  "r1517": C["Egypt"],
  "hicaz": C["Saudi Arabia"].intersection(box(34, 20.0, 40.6, 29.5)),
}
def alan(g):  # yaklaşık km²
    return sum(p.area * math.cos(math.radians(p.centroid.y)) * 111.3 ** 2 for p in (g.geoms if hasattr(g, "geoms") else [g]))
a12 = alan(R["r1512"]); a20 = alan(unary_union(list(R.values())))
print(f"1512 ≈ {a12/1e6:.2f} M km², 1520 ≈ {a20/1e6:.2f} M km², oran {a20/a12:.2f}")

def path(g, tol=0.04):
    g = g.simplify(tol, preserve_topology=True); out = []
    for poly in (g.geoms if hasattr(g, "geoms") else [g]):
        if poly.is_empty or poly.geom_type != "Polygon": continue
        for ring in [poly.exterior, *poly.interiors]:
            pts = [P(x, y) for x, y in ring.coords]
            out.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
    return "".join(out)
kara = [shape(f["geometry"]) for f in json.load(open(GEO / "ne_50m_land.geojson"))["features"]]
kara = unary_union([g for g in kara if g.intersects(box(LON0 - 5, LAT0 - 5, LON1 + 5, LAT1 + 5))]).intersection(box(LON0 - 5, LAT0 - 5, LON1 + 5, LAT1 + 5))
PINS = {"caldiran": (43.9, 39.15, "ÇALDIRAN"), "mercidabik": (37.27, 36.54, "MERCİDABIK"), "kahire": (31.25, 30.05, "RİDANİYE"), "mekke": (39.8, 21.42, "MEKKE"), "istanbul": (28.97, 41.01, "İSTANBUL")}
SIRA = ["r1512", "r1514", "r1516", "r1517", "hicaz"]
UNI = {f"u{i}": path(unary_union([R[k] for k in SIRA[:i + 1]]).buffer(0.05).buffer(-0.05), 0.05) for i in range(len(SIRA))}
spec = {**UNI, "kara": path(kara, 0.06), **{k: path(v) for k, v in R.items()}, "pins": {k: [*P(lo, la), ad] for k, (lo, la, ad) in PINS.items()},
        "oran": round(a20 / a12, 1), "H": (LAT1 - LAT0) * K}

work = HERE / "work"
if work.exists(): shutil.rmtree(work)
(work / "fonts").mkdir(parents=True); (work / "vendor").mkdir()
shutil.copy(ROOT / "engine/fonts/Anton-Regular.ttf", work / "fonts/Anton.ttf")
shutil.copy(ROOT / "engine/fonts/Montserrat[wght].ttf", work / "fonts/Montserrat.ttf")
shutil.copy(KIT / "vendor/gsap.min.js", work / "vendor/gsap.min.js")
html = (HERE / "template.html").read_text().replace("__SPEC__", json.dumps(spec, ensure_ascii=False))
(work / "index.html").write_text(html)
HF = ["npx", "--yes", "hyperframes@0.8.34"]
if "--snap" in sys.argv:
    t = sys.argv[sys.argv.index("--snap") + 1]
    r = subprocess.run(HF + ["snapshot", str(work), "--at", t], capture_output=True, text=True, cwd=KIT)
    print(r.stdout[-1500:], r.stderr[-1500:])
else:
    out = HERE / "yavuz-harita.mp4"
    r = subprocess.run(HF + ["render", str(work), "-o", str(out), "--fps", "30", "-q", "high"], capture_output=True, text=True, cwd=KIT)
    print(r.stdout[-1500:], r.stderr[-1500:])
