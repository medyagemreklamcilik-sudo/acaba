#!/usr/bin/env python3
"""analiz.py - bir Shorts/Reels videosunda izleyicinin NEREDE ve NEDEN bıraktığını bulur.

    python3 tools/analiz.py <klasör> --csv retention.csv          # YouTube Studio izleyici tutma dışa aktarımı
    python3 tools/analiz.py <klasör> --points "0:100,3:72,10:55"  # ekran görüntüsünden okunan noktalar (sn:%)
    python3 tools/analiz.py <klasör> --avg 30.7 --hold3 38.4      # sadece Metricool ortalamaları (IG)
    ... --platform instagram --views 397   (rapora yazılır)   --out   (<klasör>/analiz.md'ye yazar)

Eğri analizi Jake Schincariol'un youtube-agent-skill/yt-retention aracından (MIT) Shorts'a uyarlandı:
  KANCA    ilk 3 sn'de kaybedilen (Shorts'ta kaydırma kararı burada verilir)
  ERKEN    3-10 sn arası kayıp (kancanın vaadi tutuldu mu)
  UÇURUM   tek bir anda dik düşüşler; her biri için o saniyede söylenen cümle + ekrandaki sahne/yazı
  KAYMA    ortadaki düzenli kanama (tempo)
  DÖNGÜ    sonda %100'ü aşan / yükselen eğri (tekrar izleme)
Her uçurum için videonun kendi zaman çizelgesinden (build/aligned.json + scenes.py) muhtemel neden ve öneri üretir.
"""
import csv, importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = ("peki", "ama", "gelelim", "sonra", "ya", "ancak", "fakat", "oysa", "üstelik", "şimdi")


# ---------------------------------------------------------------- veri
def load_words(d):
    for p in ("build/aligned.json", "build/words.json", "kelimeler.json"):
        f = os.path.join(d, p)
        if os.path.exists(f):
            return [(w["w"], float(w["s"]), float(w["e"])) for w in json.load(open(f))]
    return []


def load_scenes(d):
    f = os.path.join(d, "scenes.py")
    if not os.path.exists(f):
        return None
    spec = importlib.util.spec_from_file_location("scenes_" + os.path.basename(d.rstrip("/")).replace("-", "_"), f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def duration(d, S):
    if S is not None and hasattr(S, "DURATION"):
        return float(S.DURATION)
    import subprocess
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 os.path.join(d, "video.mp4")], capture_output=True, text=True).stdout or 0)


def load_curve(path=None, points=None, dur=None):
    rows = []
    if path:
        with open(path, newline="", encoding="utf-8-sig", errors="replace") as fh:
            for r in csv.reader(fh):
                nums = []
                for c in r:
                    c = c.strip().replace("%", "").replace(",", ".")
                    if ":" in c:  # 0:05 biçimi
                        try:
                            mm, ss = c.split(":")[-2:]
                            nums.append(int(mm) * 60 + float(ss)); continue
                        except ValueError:
                            pass
                    try:
                        nums.append(float(c))
                    except ValueError:
                        pass
                if len(nums) >= 2:
                    rows.append((nums[0], nums[1]))
    if points:
        for p in points.split(","):
            x, y = p.split(":")
            rows.append((float(x), float(y)))
    rows.sort()
    if not rows:
        return []
    # eksen yüzde ise (0..1 ya da 0..100) saniyeye çevir
    xs = [r[0] for r in rows]
    if dur and max(xs) <= 1.01:
        rows = [(x * dur, y) for x, y in rows]
    elif dur and max(xs) <= 100.5 and max(xs) > dur * 1.05:
        rows = [(x / 100 * dur, y) for x, y in rows]
    if max(r[1] for r in rows) <= 1.5:  # oran olarak geldiyse
        rows = [(x, y * 100) for x, y in rows]
    return rows


def interp(rows, t):
    if t <= rows[0][0]:
        return rows[0][1]
    for (x0, y0), (x1, y1) in zip(rows, rows[1:]):
        if x0 <= t <= x1:
            return y0 + (y1 - y0) * ((t - x0) / (x1 - x0 or 1))
    return rows[-1][1]


# ---------------------------------------------------------------- zaman çizelgesi
def said(words, t0, t1):
    return " ".join(w for w, s, e in words if e >= t0 and s <= t1)


def sentence_at(words, t):
    """t anındaki cümlenin tamamı (noktalama ile sınırlanır)."""
    if not words:
        return ""
    i = min(range(len(words)), key=lambda k: abs(words[k][1] - t))
    a = i
    while a > 0 and not re.search(r"[.!?…]$", words[a - 1][0]):
        a -= 1
    b = i
    while b < len(words) - 1 and not re.search(r"[.!?…]$", words[b][0]):
        b += 1
    return " ".join(w for w, _, _ in words[a:b + 1])


def scene_at(S, t):
    if S is None:
        return None, None
    sc = [s for s in S.SCENES if s["t"] <= t]
    if not sc:
        return None, None
    s = sc[-1]
    return s, s.get("_end", s["t"])


def overlays_at(S, t):
    if S is None:
        return []
    return [o for o in getattr(S, "OVERLAYS", []) if o.get("t0", 0) <= t <= o.get("t1", 0)]


def ov_text(o):
    if o.get("type") == "counter" and o.get("fmt"):
        return o["fmt"].format(o.get("to", ""))
    for k in ("text", "title"):
        if o.get(k):
            return str(o[k]).replace("\n", " ")
    if o.get("lines"):
        return " ".join(o["lines"])
    if o.get("tags"):
        return " / ".join(x[0] for x in o["tags"])
    return o.get("type", "")


def describe_screen(S, t):
    s, _ = scene_at(S, t)
    if s is None:
        return "-"
    what = s.get("img") or s.get("mode") or "?"
    if s.get("mode") and s.get("img"):
        what = f'{s["mode"]}:{s["img"]}'
    ovs = [f'{o["type"]} "{ov_text(o)[:40]}"' for o in overlays_at(S, t)]
    return what + ("  +  " + ", ".join(ovs) if ovs else "  (yazı yok)")


# ---------------------------------------------------------------- neden / öneri
def reasons(words, S, t, dur):
    out = []
    win = [(w, s, e) for w, s, e in words if t - 2.5 <= s <= t + 1.0]
    # duraklama
    gaps = [(b[1] - a[2], a[2]) for a, b in zip(win, win[1:])]
    if gaps:
        g, at = max(gaps)
        if g >= 0.7:
            out.append(("duraklama", f"{at:.1f}. sn'de {g:.1f} sn sessizlik",
                        "Sessizliği kes ya da araya SFX/kamera hareketi koy; Shorts'ta 0.5 sn'den uzun boşluk kaydırma demek."))
    # yavaş anlatım
    if win:
        span = (win[-1][2] - win[0][1]) or 1
        wps = len(win) / span
        if wps < 1.5:
            out.append(("yavaş", f"konuşma hızı {wps:.1f} kelime/sn",
                        "Bu cümleyi kısalt ya da sesi bu bölümde %5-8 hızlandır."))
    # tarih/sayı yığını
    nums = [w for w, _, _ in win if re.search(r"\d", w)]
    if len(nums) >= 2:
        out.append(("sayı", f"art arda sayı/tarih: {' '.join(nums)}",
                    "Tek bir sayı bırak; diğerini ekrana yazı olarak taşı ya da tamamen at."))
    # durağan görüntü
    s, _ = scene_at(S, t)
    if s is not None:
        held = t - s["t"]
        recent_ov = [o for o in getattr(S, "OVERLAYS", []) if t - 3.5 <= o.get("t0", -99) <= t]
        if held > 5 and not recent_ov:
            out.append(("durağan", f"aynı görsel {held:.0f} sn'dir ekranda, yeni yazı yok",
                        "Bu noktada yeni görsel, zoom vuruşu ya da kinetik yazı ekle (her 2-3 sn'de bir değişim)."))
        if s.get("mode") in ("plate", "card", "grid"):
            out.append(("yazı-ağır", f"ekranda {s['mode']} sahnesi (okuma gerektiriyor)",
                        "Yazıyı 3-4 kelimeye indir, belgeyi daha kısa tut ya da sesle aynı anda vurgula."))
    # konu geçişi
    first = [w for w, st, _ in words if t - 3 <= st <= t + 1.5]
    if any(w.lower().strip(",.!?\"'") in TRANS for w in first):
        out.append(("geçiş", "konu geçişi (Peki/Ama/Gelelim...)",
                    "Geçişi soru ya da vaatle yap: 'Ama asıl şok edici olan...' gibi yeni bir merak boşluğu aç."))
    # kanca cevabı verildi
    if words:
        hook = [w.lower().strip(",.!?\"'") for w, st, _ in words if st < 3.5 and len(w) > 4]
        here = [w.lower().strip(",.!?\"'") for w, _, _ in win]
        if t > 8 and hook and sum(1 for h in hook if h in here) >= 2:
            out.append(("cevap", "kancadaki soru/iddia burada cevaplanıyor",
                        "Cevabı videonun sonuna sakla; burada sadece ipucu ver."))
    if t >= dur - 9:
        out.append(("kapanış", "kapanış/soru bölümü",
                    "Normal düşüş. Son soruyu kısalt ve kancayla döngü kur (son cümle ilk cümleye bağlansın)."))
    return out


def hook_check(words, S):
    """İlk 3 saniyenin metinsel kontrolü (Shorts kanca kuralı)."""
    first = " ".join(w for w, s, _ in words if s < 3.0)
    notes = []
    if re.match(r"^\W*\d", first):
        notes.append("Tarihle başlıyor: kanca kuralına aykırı, en çarpıcı iddia ilk kelimelerde olmalı.")
    if first.count(" ") + 1 > 10:
        notes.append("İlk 3 saniyede 10'dan fazla kelime var; ilk cümle kısalmalı.")
    if not re.search(r"[?!]|\d", first):
        notes.append("İlk cümlede soru, sayı ya da ünlem yok; merak boşluğu zayıf.")
    ovs = [o for o in getattr(S, "OVERLAYS", []) if o.get("t0", 9) < 0.6] if S else []
    if not ovs:
        notes.append("İlk 0.6 sn'de ekranda yazı yok; sesi kapalı izleyen için kanca görünmüyor.")
    return first, notes


# ---------------------------------------------------------------- analiz
def analyse_curve(rows, words, S, dur):
    start = rows[0][1] or 100.0
    r3, r10 = interp(rows, 3.0), interp(rows, 10.0)
    end = rows[-1][1]
    # 1 sn'lik örnekleme, dik düşüşler
    grid = [(t, interp(rows, t)) for t in [x * 0.5 for x in range(int(dur * 2) + 1)]]
    drops = []
    for (t0, y0), (t1, y1) in zip(grid, grid[2:]):  # 1 sn pencere
        if t0 < 3.0:
            continue
        drops.append((y0 - y1, t0))
    drops.sort(reverse=True)
    cliffs, used = [], []
    for d, t in drops:
        if d < 1.5 or len(cliffs) >= 5:
            break
        if any(abs(t - u) < 3 for u in used):
            continue
        used.append(t)
        cliffs.append({"t": t, "lost": round(d, 1), "kalan": round(interp(rows, t + 1), 1)})
    mid = [(y0 - y1) for (t0, y0), (t1, y1) in zip(grid, grid[2:]) if 10 <= t0 <= dur - 10]
    slide = sum(mid) / len(mid) if mid else 0
    loop = max(y for t, y in grid if t >= dur * 0.85) > interp(rows, dur * 0.8) + 1
    return {"start": start, "kanca_kayip": round(start - r3, 1), "erken_kayip": round(r3 - r10, 1),
            "son": round(end, 1), "kayma_sn": round(slide, 2), "dongu": loop, "ucurumlar": cliffs}


def report(d, rows=None, avg=None, hold3=None, platform=None, views=None):
    d = d.rstrip("/")
    words, S = load_words(d), load_scenes(d)
    dur = duration(d, S)
    L = [f"# Analiz: {os.path.basename(d)}", "", f"Süre: {dur:.1f} sn" + (f" · Platform: {platform}" if platform else "")
         + (f" · İzlenme: {views}" if views else ""), ""]
    first, hnotes = hook_check(words, S)
    biggest = None

    if hold3 is not None:
        verdict = "iyi" if hold3 >= 60 else "orta" if hold3 >= 45 else "zayıf"
        L += [f"## Kanca (ilk 3 sn)", f"- İzleyenlerin **%{hold3:.1f}**'i ilk 3 saniyeyi geçti → **{verdict}** "
              "(Reels ölçütü: 60+ iyi, 45-60 orta, 45 altı zayıf)"]
        if hold3 < 45:
            biggest = ("kanca", f"izleyicinin %{100 - hold3:.0f}'i ilk 3 saniyede kaydırdı")
    else:
        L += ["## Kanca (ilk 3 sn)"]
    L += [f'- İlk 3 saniyede söylenen: "{first}"'] + [f"- {n}" for n in hnotes] + [""]

    if avg is not None and dur:
        pct = avg / dur * 100
        L += ["## Ortalama izleme", f"- Ortalama izleme süresi **{avg:.1f} sn** / {dur:.0f} sn → videonun **%{pct:.0f}**'i izleniyor."]
        L += [f'- Ortalama izleyici şu cümlede gitti ({avg:.0f}. sn): "{sentence_at(words, avg)}"',
              f"- Ekranda: {describe_screen(S, avg)}"]
        for tag, why, fix in reasons(words, S, avg, dur):
            L += [f"  - Olası neden: {why} → **Öneri:** {fix}"]
        L += ["- Not: bu bir ortalama; kesin bırakma saniyesi için YouTube Studio izleyici tutma eğrisi gerekir.", ""]
        if biggest is None and pct < 35:
            biggest = ("orta", f"izleyici ortalama {avg:.0f}. saniyede çıkıyor")

    if rows:
        A = analyse_curve(rows, words, S, dur)
        kv = "sağlıklı" if A["kanca_kayip"] < 25 else "sızdırıyor" if A["kanca_kayip"] < 40 else "ağır"
        L += ["## İzleyici tutma eğrisi",
              f"- Kanca kaybı (0-3 sn): **%{A['kanca_kayip']}** → {kv}",
              f"- Erken kayıp (3-10 sn): %{A['erken_kayip']}",
              f"- Orta bölüm kayması: saniyede %{A['kayma_sn']}",
              f"- Sonda kalan: %{A['son']}" + (" · **döngü var** (sonda tekrar izleme)" if A["dongu"] else ""), "",
              "### Bırakılan anlar"]
        for i, c in enumerate(A["ucurumlar"], 1):
            t = c["t"]
            L += [f"**{i}. {t:.0f}. saniye, %{c['lost']} kayıp** (sonra %{c['kalan']} kalıyor)",
                  f'- Söylenen: "{said(words, t - 1.5, t + 1.0)}"',
                  f'- Cümle: "{sentence_at(words, t)}"',
                  f"- Ekranda: {describe_screen(S, t)}"]
            rs = reasons(words, S, t, dur)
            for tag, why, fix in rs:
                L += [f"- Neden: {why} → **Öneri:** {fix}"]
            if not rs:
                L += ["- Belirgin teknik neden yok: içerik ilgiyi kaybettiriyor olabilir; bu cümleyi kes ya da daha çarpıcı bir bilgiyle değiştir."]
            L += [""]
        if not A["ucurumlar"]:
            L += ["- Tek bir anda dik düşüş yok; kayıp düzenli kayma şeklinde (tempo sorunu, ortayı kısalt).", ""]
        if A["kanca_kayip"] >= 25:
            biggest = ("kanca", f"ilk 3 saniyede %{A['kanca_kayip']} kayıp")
        elif A["ucurumlar"]:
            c = A["ucurumlar"][0]
            biggest = biggest or ("ucurum", f"{c['t']:.0f}. saniyede %{c['lost']} tek seferde kayıp")

    L += ["## Tek düzeltme"]
    if biggest:
        L += [f"En büyük sızıntı: **{biggest[1]}**. Önce bunu düzelt, gerisi sonra."]
    else:
        L += ["Kanca ve tempo sağlıklı görünüyor; sorun büyük ihtimalle kapak/başlık (paketleme). Kapağı ve ilk yazıyı değiştir."]
    return "\n".join(L) + "\n"


def main():
    a = sys.argv[1:]
    if not a or not os.path.isdir(a[0]):
        print(__doc__); sys.exit(1)

    def opt(k, cast=str):
        return cast(a[a.index(k) + 1]) if k in a else None
    d = a[0]
    S = load_scenes(d)
    dur = duration(d, S)
    rows = load_curve(opt("--csv"), opt("--points"), dur) if ("--csv" in a or "--points" in a) else None
    txt = report(d, rows, opt("--avg", float), opt("--hold3", float), opt("--platform"), opt("--views"))
    if "--out" in a:
        name = "analiz.md" if not opt("--platform") else f"analiz-{opt('--platform')}.md"
        open(os.path.join(d, name), "w").write(txt)
        print("yazıldı:", os.path.join(d, name))
    print(txt)


if __name__ == "__main__":
    main()
