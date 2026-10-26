"""Build historical regions from real administrative boundaries (Natural Earth
10m admin-1). Each region is a union of modern provinces approximating the
historical territory. Output: engine/geo/regions.json  {region: [ring, ...]} (lon/lat)."""
import json, os, sys
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))
GEO = os.path.join(ROOT, "..", "geo")

U = {
    "sogut": ["TR:Bilecik"],
    "osman": ["TR:Eskisehir"],
    "bursa": ["TR:Bursa"],
    "iznik": ["TR:Kocaeli", "TR:Sakarya", "TR:Yalova"],
    "karesi": ["TR:Balikesir", "TR:Çanakkale"],
    "gelibolu": ["TR:Çanakkale"],
    "edirne": ["TR:Edirne", "TR:Kirklareli", "TR:Tekirdag", "BG:Haskovo", "BG:Kardzhali", "BG:Yambol", "BG:Stara Zagora",
               "GR:Anatoliki Makedonia kai Thraki"],
    "filibe": ["BG:Plovdiv", "BG:Pazardzhik", "BG:Smolyan", "BG:Sofia", "BG:Grad Sofiya", "BG:Pernik", "BG:Kyustendil",
               "BG:Blagoevgrad"],
    "nis": ["RS:Nišavski", "RS:Pirotski", "RS:Toplicki", "RS:Jablanicki", "RS:Pcinjski"],
    "makedonya": ["MK:*", "XK:*"],
    "anadolu_bati": ["TR:Izmir", "TR:Manisa", "TR:Aydin", "TR:Mugla", "TR:Denizli", "TR:Usak", "TR:Kütahya",
                     "TR:Afyonkarahisar", "TR:Isparta", "TR:Burdur", "TR:Antalya"],
    "anadolu_kuzey": ["TR:Ankara", "TR:Bolu", "TR:Düzce", "TR:Zinguldak", "TR:Bartın", "TR:Karabük", "TR:Kastamonu",
                      "TR:Çankiri", "TR:Kinkkale", "TR:Çorum", "TR:Sinop", "TR:Samsun", "TR:Amasya", "TR:Tokat",
                      "TR:Yozgat", "TR:Kirsehir", "TR:Sivas"],
    "bulgaristan": ["BG:Vidin", "BG:Montana", "BG:Vratsa", "BG:Pleven", "BG:Lovech", "BG:Gabrovo", "BG:Veliko Tarnovo",
                    "BG:Ruse", "BG:Razgrad", "BG:Targovishte", "BG:Shumen", "BG:Silistra", "BG:Dobrich", "BG:Varna",
                    "BG:Burgas", "BG:Sliven"],
    "dobruca": ["RO:Constanta", "RO:Tulcea"],
    "tesalya": ["GR:Thessalia"],
    "selanik": ["GR:Kentriki Makedonia", "GR:Dytiki Makedonia", "GR:Ayion Oros"],
    "istanbul": ["TR:Istanbul"],
    "sirbistan": ["RS:Borski", "RS:Zajecarski", "RS:Raški", "RS:Pomoravski", "RS:Zlatiborski", "RS:Macvanski",
                  "RS:Branicevski", "RS:Podunavski", "RS:Šumadijski", "RS:Moravicki", "RS:Kolubarski"],
    "mora": ["GR:Peloponnisos"],
    "orta_yunan": ["GR:Stereá Elláda", "GR:Attiki", "GR:Dytiki Ellada"],
    "trabzon": ["TR:Ordu", "TR:Giresun", "TR:Trabzon", "TR:Rize", "TR:Gümüshane", "TR:Bayburt"],
    "bosna": ["BA:*"],
    "arnavutluk": ["AL:*", "GR:Ipeiros"],
    "karadag": ["ME:*"],
    "karaman": ["TR:Konya", "TR:Karaman", "TR:Aksaray", "TR:Nigde", "TR:Nevsehir", "TR:Mersin"],
    "kirim": ["RU:Crimea", "RU:Sevastopol"],
    "kili": ["UA:Odessa"],
    "dogu_anadolu": ["TR:Erzincan", "TR:Tunceli", "TR:Elazig", "TR:Malatya", "TR:Adiyaman", "TR:Diyarbakir", "TR:Batman",
                     "TR:Siirt", "TR:Bitlis", "TR:Mus", "TR:Bingöl", "TR:Erzurum", "TR:Iğdir", "TR:Agri", "TR:Van",
                     "TR:Hakkari", "TR:Sirnak", "TR:Mardin", "TR:K. Maras", "TR:Kayseri"],
    "kars": ["TR:Kars", "TR:Ardahan", "TR:Artvin", "GE:Ajaria"],
    "suriye": ["SY:*", "LB:*", "IL:*", "PS:*", "JO:*", "TR:Hatay", "TR:Gaziantep", "TR:Kilis", "TR:Adana", "TR:Osmaniye",
               "TR:Sanliurfa"],
    "suriye_kayip": ["SY:*", "LB:*", "IL:*", "PS:*", "JO:*"],
    "misir": ["EG:*"],
    "hicaz": ["SA:Makkah", "SA:Al Madinah", "SA:Tabuk", "SA:Al Bahah"],
    "belgrad": ["RS:Grad Beograd"],
    "onikiada": ["GR:Notio Aigaio"],
    "macaristan": ["HU:Pest", "HU:Budapest", "HU:Bács-Kiskun", "HU:Csongrád", "HU:Szeged", "HU:Baranya", "HU:Pécs",
                   "HU:Tolna", "HU:Somogy", "HU:Fejér", "HU:Jász-Nagykun-Szolnok", "HU:Szolnok", "HU:Békés", "HU:Heves",
                   "HU:Eger", "HU:Kecskemét", "HU:Hódmezôvásárhely", "HU:Dunaújváros", "HU:Székesfehérvár",
                   "HU:Szekszárd", "HU:Kaposvár", "HU:Békéscsaba", "HU:Érd", "HU:Nógrád", "HU:Salgótarján",
                   "HU:Veszprém", "RS:Severno-Backi", "RS:Zapadno-Backi", "RS:Severno-Banatski", "RS:Južno-Backi",
                   "RS:Srednje-Banatski", "RS:Južno-Banatski", "RS:Sremski", "HR:Osjecko-Baranjska",
                   "HR:Vukovarsko-Srijemska", "HR:Brodsko-Posavska", "HR:Viroviticko-Podravska", "RO:Timis", "RO:Arad",
                   "RO:Caras-Severin"],
    "irak": ["IQ:*"],
    "cezayir": ["DZ:El Tarf", "DZ:Tébessa", "DZ:Souk Ahras", "DZ:Tlemcen", "DZ:Annaba", "DZ:Skikda", "DZ:Jijel",
                "DZ:Béjaïa", "DZ:Tizi Ouzou", "DZ:Boumerdès", "DZ:Alger", "DZ:Tipaza", "DZ:Chlef", "DZ:Mostaganem",
                "DZ:Oran", "DZ:Aïn Témouchent", "DZ:Sétif", "DZ:Bordj Bou Arréridj", "DZ:Bouira", "DZ:Blida",
                "DZ:Tissemsilt", "DZ:Aïn Defla", "DZ:Relizane", "DZ:Saïda", "DZ:Sidi Bel Abbès", "DZ:Mascara",
                "DZ:Médéa", "DZ:Tiaret", "DZ:M'Sila", "DZ:Batna", "DZ:Khenchela", "DZ:Guelma", "DZ:Constantine",
                "DZ:Mila", "DZ:Oum el Bouaghi", "DZ:Biskra"],
    "tunus": ["TN:*"],
    "trablusgarp": ["LY:Ghadamis", "LY:An Nuqat al Khams", "LY:Al Butnan", "LY:Ajdabiya", "LY:Surt", "LY:Misratah",
                    "LY:Al Marqab", "LY:Tajura' wa an Nawahi al Arba", "LY:Az Zawiyah", "LY:Al Qubbah",
                    "LY:Al Jabal al Akhdar", "LY:Al Marj", "LY:Benghazi", "LY:Al Jifarah", "LY:Mizdah", "LY:Al Jufrah",
                    "LY:Ash Shati'", "LY:Sabha", "LY:Wadi al Hayaa", "LY:Murzuq", "LY:Ghat"],
    "kibris": ["CY:*", "@Northern Cyprus"],
    "kafkasya": ["GE:Abkhazia", "GE:Samegrelo-Zemo Svaneti", "GE:Shida Kartli", "GE:Racha-Lechkhumi-Kvemo Svaneti",
                 "GE:Mtskheta-Mtianeti", "GE:Kakheti", "GE:Samtskhe-Javakheti", "GE:Kvemo Kartli", "GE:Guria",
                 "GE:Tbilisi", "GE:Imereti", "AM:*", "AZ:*", "IR:West Azarbaijan", "IR:East Azarbaijan"],
    "girit": ["GR:Kriti"],
    "podolya": ["UA:Khmel'nyts'kyy", "UA:Vinnytsya", "UA:Ternopil'"],
    "eflak": ["RO:Mehedinti", "RO:Dolj", "RO:Olt", "RO:Teleorman", "RO:Giurgiu", "RO:Calarasi", "RO:Ialomita",
              "RO:Ilfov", "RO:Bucharest", "RO:Arges", "RO:Dâmbovita", "RO:Prahova", "RO:Buzau", "RO:Braila", "RO:Gorj",
              "RO:Vâlcea"],
    "bogdan": ["RO:Suceava", "RO:Botosani", "RO:Iasi", "RO:Neamt", "RO:Bacau", "RO:Vaslui", "RO:Vrancea",
               "RO:Galati"],
    "besarabya": ["MD:*"],
    "rumeli": ["BG:*", "MK:*", "XK:*", "AL:*", "ME:*", "GR:Kentriki Makedonia", "GR:Dytiki Makedonia",
               "GR:Anatoliki Makedonia kai Thraki", "GR:Ipeiros", "GR:Ayion Oros", "GR:Voreio Aigaio", "RS:Raški",
               "RS:Pcinjski", "RS:Jablanicki", "TR:Edirne", "TR:Kirklareli", "TR:Tekirdag"],
    "dogu_trakya": ["TR:Edirne", "TR:Kirklareli", "TR:Tekirdag"],
}

SEVR = {
    "YUNANİSTAN": ["TR:Izmir", "TR:Manisa", "TR:Edirne", "TR:Kirklareli", "TR:Tekirdag"],
    "İTALYA": ["TR:Antalya", "TR:Burdur", "TR:Isparta", "TR:Mugla", "TR:Denizli", "TR:Aydin", "TR:Konya", "TR:Karaman"],
    "FRANSA": ["TR:Adana", "TR:Mersin", "TR:Osmaniye", "TR:Hatay", "TR:Gaziantep", "TR:Kilis", "TR:Sanliurfa",
               "TR:Mardin", "TR:K. Maras", "TR:Adiyaman"],
    "ERMENİSTAN": ["TR:Erzurum", "TR:Trabzon", "TR:Rize", "TR:Bayburt", "TR:Gümüshane", "TR:Kars", "TR:Ardahan",
                   "TR:Artvin", "TR:Iğdir", "TR:Agri", "TR:Van", "TR:Bitlis", "TR:Mus"],
    "KÜRDİSTAN (ÖZERK)": ["TR:Diyarbakir", "TR:Batman", "TR:Siirt", "TR:Sirnak", "TR:Hakkari", "TR:Bingöl", "TR:Tunceli",
                          "TR:Elazig", "TR:Malatya"],
    "BOĞAZLAR": ["TR:Istanbul", "TR:Kocaeli", "TR:Yalova", "TR:Çanakkale"],
}


def rdp(pts, eps):
    if len(pts) < 4:
        return pts
    a, b = pts[0], pts[-1]
    ab = b - a
    n = np.hypot(*ab)
    if n == 0:
        d = np.hypot(*(pts - a).T)
    else:
        d = np.abs(ab[0] * (pts[:, 1] - a[1]) - ab[1] * (pts[:, 0] - a[0])) / n
    i = int(np.argmax(d))
    if d[i] > eps:
        l = rdp(pts[:i + 1], eps)
        r = rdp(pts[i:], eps)
        return np.vstack([l[:-1], r])
    return np.vstack([a, b])


def main():
    d = json.load(open(os.path.join(GEO, "ne_10m_admin_1.geojson")))
    feats = {}
    for f in d["features"]:
        p = f["properties"]
        iso, name, admin = p.get("iso_a2"), p.get("name"), p.get("admin")
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        rings = []
        for pp in polys:
            r = np.array(pp[0], np.float64)
            r = rdp(r, 0.012)
            if len(r) >= 3:
                rings.append(r.round(4).tolist())
        feats.setdefault((iso, name), []).extend(rings)
        feats.setdefault(("@", admin), []).extend(rings)

    def resolve(specs):
        out, missing = [], []
        for s in specs:
            if s.startswith("@"):
                k = ("@", s[1:])
                if k in feats:
                    out += feats[k]
                else:
                    missing.append(s)
                continue
            iso, name = s.split(":", 1)
            if name == "*":
                ks = [k for k in feats if k[0] == iso]
                if not ks:
                    missing.append(s)
                for k in ks:
                    out += feats[k]
            elif (iso, name) in feats:
                out += feats[(iso, name)]
            else:
                missing.append(s)
        return out, missing

    res, sev = {}, {}
    for k, v in U.items():
        res[k], miss = resolve(v)
        if miss:
            print("MISSING", k, miss)
    for k, v in SEVR.items():
        sev[k], miss = resolve(v)
        if miss:
            print("MISSING sevr", k, miss)
    json.dump({"regions": res, "sevr": sev}, open(os.path.join(GEO, "regions.json"), "w"))
    print("regions", len(res), "points", sum(len(r) for v in res.values() for r in v))


if __name__ == "__main__":
    main()
