// Osmanlı ve Cumhuriyet dönemi karakterleri: makeHuman tabanı + kostüm + başlık
//   const v = karakter('vezir'); scene.add(v.root); v.setPose(DUR);
// Roller: padisah, sehzade, sehzade_cocuk, vezir, sadrazam, seyhulislam, ulema, yeniceri, cellat, dilsiz,
//         hekim, kahveci, halk_erkek, halk_kadin, valide_sultan, cariye, dervis, tellak, kopek_degil_esek_icin_proplar,
//         subay_1920, mehmetcik, mebus, cumhuriyet_beyi, cumhuriyet_hanimi, ogretmen, cocuk, ingiliz_subay, kemanci
import * as THREE from 'three';
import { makeHuman, torsoShell, torsoR, TORSO_SX, TORSO_SZ } from '../human.js';
import { materials } from '../materials.js';
import { kumas, mat, altin, mesh, kure, silindir, halka, torna, kutu } from './ortak.js';

const ICINDE = (root, node) => { let p = node; while (p) { if (p === root) return true; p = p.parent; } return false; };

// ---------- başlıklar (head grubuna takılır; kafatası merkezi y≈0.095, tepe ≈0.205) ----------
export const BASLIK = {
  kavuk(renk = 0xf7f3ea, ic = 0xb3202c) { // padişah kavuğu: soğan biçimli sarık + sorguç
    const g = new THREE.Group(), w = kumas(renk);
    g.add(kure(0.16, w, [0, 0.2, -0.01], [1, 0.95, 1]));
    for (let i = 0; i < 4; i++) g.add(halka(0.14 - i * 0.012, 0.024, w, [0, 0.14 + i * 0.045, -0.01], [Math.PI / 2 + 0.22, 0, 0]));
    g.add(kure(0.06, kumas(ic), [0, 0.36, -0.01], [1, 0.8, 1]));
    g.add(kure(0.026, mat(0xd8202a, { metalness: 0.3, roughness: 0.2, emissive: 0x300005 }), [0, 0.23, 0.15]));
    g.add(silindir(0.008, 0.013, 0.07, altin(), [0, 0.28, 0.14]));
    g.add(mesh(new THREE.ConeGeometry(0.025, 0.22, 12), mat(0x18151c, { roughness: 0.9 }), [0.02, 0.42, 0.11], [-0.3, 0, -0.18]));
    return g;
  },
  mucevveze(renk = 0xf7f3ea) { // vezir/şeyhülislam: büyük yuvarlak sarık, üstü kırmızı
    const g = new THREE.Group(), w = kumas(renk);
    g.add(kure(0.19, w, [0, 0.19, -0.01], [1.05, 0.72, 1.05]));
    for (let i = 0; i < 3; i++) g.add(halka(0.165 - i * 0.02, 0.028, w, [0, 0.14 + i * 0.05, -0.01], [Math.PI / 2 + 0.1, 0, 0]));
    g.add(silindir(0.05, 0.065, 0.12, kumas(0xa0222c), [0, 0.3, -0.01]));
    return g;
  },
  sarik(renk = 0xf2ede2, takke = 0x7a2a2a) { // halk/imam: takke üstüne sarık
    const g = new THREE.Group(), w = kumas(renk);
    g.add(kure(0.11, kumas(takke), [0, 0.15, -0.01], [1, 0.9, 1]));
    for (let i = 0; i < 3; i++) g.add(halka(0.118 - i * 0.008, 0.025, w, [0, 0.14 + i * 0.035, -0.01], [Math.PI / 2 + 0.15 + i * 0.1, i * 0.3, 0]));
    return g;
  },
  bork() { // yeniçeri börkü: arkaya düşen uzun beyaz keçe + kaşıklık
    const g = new THREE.Group(), w = kumas(0xf4f1ea);
    g.add(silindir(0.11, 0.12, 0.2, w, [0, 0.26, -0.01]));
    const yatma = mesh(new THREE.CylinderGeometry(0.075, 0.105, 0.42, 24), w, [0, 0.33, -0.2], [-1.05, 0, 0]); g.add(yatma);
    g.add(halka(0.12, 0.02, altin(), [0, 0.17, -0.01], [Math.PI / 2, 0, 0]));
    g.add(kutu(0.05, 0.12, 0.02, altin(), [0, 0.26, 0.12]));
    return g;
  },
  fes(renk = 0xb51f24) {
    const g = new THREE.Group();
    g.add(silindir(0.085, 0.105, 0.15, kumas(renk), [0, 0.23, -0.01], [-0.08, 0, 0]));
    const p = silindir(0.004, 0.004, 0.13, mat(0x111111), [0.05, 0.27, -0.06], [0.2, 0, 0.9]); g.add(p);
    return g;
  },
  kalpak(renk = 0x3a2a20) { // Kurtuluş Savaşı kalpağı
    const g = new THREE.Group(), k = kumas(renk, { bumpScale: 4 });
    g.add(silindir(0.11, 0.115, 0.17, k, [0, 0.235, -0.01], [-0.05, 0, 0]));
    g.add(kure(0.11, kumas(0x2a1d16), [0, 0.31, -0.01], [1, 0.25, 1]));
    return g;
  },
  sapka(renk = 0x3a3a3c) { // 1925 sonrası fötr şapka
    const g = new THREE.Group(), m = kumas(renk);
    g.add(silindir(0.2, 0.2, 0.012, m, [0, 0.175, -0.01]));
    g.add(silindir(0.1, 0.115, 0.13, m, [0, 0.24, -0.01]));
    g.add(silindir(0.116, 0.118, 0.03, mat(0x1a1a1a), [0, 0.195, -0.01]));
    return g;
  },
  hotoz(renk = 0xb3202c) { // kadın sultan başlığı + duvak
    const g = new THREE.Group();
    g.add(silindir(0.08, 0.11, 0.2, kumas(renk), [0, 0.25, -0.02]));
    g.add(halka(0.105, 0.015, altin(), [0, 0.17, -0.02], [Math.PI / 2, 0, 0]));
    for (let i = 0; i < 5; i++) g.add(kure(0.012, mat(0xffffff, { roughness: 0.2 }), [Math.sin(i - 2) * 0.09, 0.2, Math.cos(i - 2) * 0.09]));
    const duvak = torna([[0.12, 0.2], [0.17, 0.05], [0.2, -0.25]], kumas(0xf5ecef, { transparent: true, opacity: 0.85, side: THREE.DoubleSide }), [0, 0, -0.03], [0, 0, 0], 32, Math.PI * 0.6, Math.PI * 0.8);
    g.add(duvak);
    return g;
  },
  yasmak(renk = 0x2b2440) { // halk kadını: başörtü/yaşmak
    const g = new THREE.Group(), m = kumas(renk, { side: THREE.DoubleSide });
    g.add(torna([[0.0, 0.25], [0.12, 0.22], [0.15, 0.1], [0.14, -0.02], [0.17, -0.12]], m, [0, 0, -0.01], [0, 0, 0], 40, Math.PI * 0.22, Math.PI * 1.56));
    return g;
  },
  sikke() { // Mevlevi sikkesi
    const g = new THREE.Group();
    g.add(silindir(0.085, 0.11, 0.3, kumas(0xb89a6a), [0, 0.3, -0.01]));
    g.add(kure(0.085, kumas(0xb89a6a), [0, 0.45, -0.01], [1, 0.3, 1]));
    return g;
  },
  takke(renk = 0xf2ede2) { const g = new THREE.Group(); g.add(kure(0.108, kumas(renk), [0, 0.15, -0.01], [1, 0.75, 1])); return g; },
  cellat() { // kırmızı külah
    const g = new THREE.Group();
    g.add(mesh(new THREE.ConeGeometry(0.12, 0.3, 24), kumas(0x8e1414), [0, 0.3, -0.02], [-0.15, 0, 0]));
    g.add(halka(0.115, 0.022, kumas(0x2a1010), [0, 0.17, -0.01], [Math.PI / 2, 0, 0]));
    return g;
  },
  kasket(renk = 0x4a4038) { // Cumhuriyet halkı kasketi
    const g = new THREE.Group(), m = kumas(renk);
    g.add(kure(0.12, m, [0, 0.17, -0.02], [1.05, 0.6, 1.1]));
    g.add(silindir(0.09, 0.1, 0.012, m, [0, 0.155, 0.1], [0.25, 0, 0]));
    return g;
  },
  askeriKep(renk = 0x6b6a45) { // İngiliz/ecnebi subay kepi
    const g = new THREE.Group(), m = kumas(renk);
    g.add(silindir(0.125, 0.11, 0.09, m, [0, 0.21, -0.01]));
    g.add(silindir(0.11, 0.11, 0.01, mat(0x1a1a1a, { roughness: 0.3 }), [0, 0.17, 0.08], [0.35, 0, 0]));
    g.add(halka(0.112, 0.012, mat(0x5a2a1a), [0, 0.19, -0.01], [Math.PI / 2, 0, 0]));
    return g;
  },
  kabalak() { // Çanakkale kabalağı
    const g = new THREE.Group(), m = kumas(0x8a7a52);
    g.add(kure(0.118, m, [0, 0.17, -0.01], [1.05, 0.8, 1.05]));
    for (let i = 0; i < 3; i++) g.add(halka(0.115, 0.018, m, [0, 0.14 + i * 0.03, -0.01], [Math.PI / 2 + 0.2, 0, 0]));
    return g;
  },
};

// ---------- kostüm ----------
// spec: { ust, alt, cizme, etek: 'kaftan'|'cubbe'|'entari'|'ferace'|'palto'|null, etekBoy, kurk, kusak, genisKol, kemer, yaka, dugme, bas, basArgs, sakal: 'kisa'|'uzun'|'yok'|'biyik', kadin, ten, olcek, kravat }
export function giydir(h, s) {
  const M = materials();
  const ust = kumas(s.ust ?? 0x5b2a86), alt = kumas(s.alt ?? s.ust ?? 0x3a2a2a), cizme = mat(s.cizme ?? 0xc9a04a, { roughness: 0.5 });
  const ten = s.ten ? mat(s.ten, { roughness: 0.55 }) : null;
  const j = h.j;
  h.root.traverse(c => {
    if (!c.isMesh) return;
    const bacak = ICINDE(j.lHip, c) || ICINDE(j.rHip, c), ayak = ICINDE(j.lAn, c) || ICINDE(j.rAn, c);
    if (c.material === M.cloth || c.material === M.clothGrey || c.material === M.steel || c.material === M.leather) c.material = bacak ? alt : ust;
    if (ayak && c.material === M.skin) c.material = cizme;
    if (ayak && c.material === alt) c.material = cizme;
    if (ten && c.material === M.skin && !ayak) c.material = ten;
  });
  // sakal / kadın
  const sakallar = []; h.j.head.traverse(c => { if (c.isMesh && c.material.color && c.material.color.getHex() === M.beard.color.getHex()) sakallar.push(c); });
  if (s.kadin || s.sakal === 'yok') sakallar.forEach(c => (c.visible = false));
  if (s.sakal === 'biyik') sakallar.forEach(c => { if (c.parent === h.j.head) c.visible = true; else c.visible = false; });
  if (s.sakal === 'uzun' || s.sakal === 'kisa') {
    const L = s.sakal === 'uzun' ? 0.16 : 0.08, jaw = sakallar[0]?.parent;
    if (jaw) jaw.add(kure(0.075, mat(s.sakalRenk ?? 0x3a2a1c, { roughness: 1 }), [0, -0.05 - L * 0.35, 0.05], [1, 0.6 + L * 3, 0.7]));
  }
  if (s.kadin) {
    h.j.head.traverse(c => { if (c.isMesh && c.material === M.hair && c.geometry.parameters?.radius === 0.07) c.visible = false; });
    h.j.head.add(kure(0.12, mat(s.sacRenk ?? 0x2a1a12, { roughness: 0.8 }), [0, 0.06, -0.06], [0.95, 1.4, 0.8]));
  }
  if (s.bas && s.bas !== 'yok') {
    h.j.head.traverse(c => { if (c.isMesh && c.material === M.hair && c.geometry.parameters?.radius === 0.07) c.visible = false; });
    const b = BASLIK[s.bas](...(s.basArgs || [])); h.j.head.add(b); h.baslik = b;
  }
  // etek (kaftan/cübbe gövdenin altı)
  if (s.etek) {
    const boy = s.etekBoy ?? 0.82, gen = s.etek === 'cubbe' ? 0.36 : s.etek === 'ferace' ? 0.34 : s.etek === 'palto' ? 0.27 : 0.31;
    const acik = s.etek === 'kaftan' ? 0.5 : s.etek === 'entari' ? 0.25 : s.etek === 'palto' ? 0.15 : 0.0;
    const prof = []; for (let i = 0; i <= 12; i++) { const k = i / 12; prof.push([0.19 + (gen - 0.19) * Math.pow(k, 0.8), 0.12 - boy * k]); }
    const e = torna(prof, s.etek === 'entari' ? alt : ust, [0, 0, 0], [0, 0, 0], 56, acik / 2, Math.PI * 2 - acik);
    e.scale.set(1, 1, 0.82); e.material = e.material.clone(); e.material.side = THREE.DoubleSide; j.pelvis.add(e); h.etek = e;
    if (s.kurk) { // kürk şeritleri ön açıklıkta + etek ucu
      const km = kumas(s.kurk, { bumpScale: 5 });
      for (const sg of [-1, 1]) { const a = Math.max(acik / 2, 0.12);
        const st = kutu(0.05, boy, 0.04, km, [sg * Math.sin(a) * 0.25, 0.12 - boy / 2, Math.cos(a) * 0.82 * 0.25]); st.rotation.z = -sg * 0.1; st.rotation.y = sg * a; j.pelvis.add(st); }
    }
    if (s.etekUc) { const u = halka(gen * 0.985, 0.02, kumas(s.etekUc), [0, 0.12 - boy, 0], [Math.PI / 2, 0, 0]); u.scale.set(1, 0.82, 1); j.pelvis.add(u); }
  }
  // kuşak / kemer
  if (s.kusak) { const k = halka(torsoR(0.06) * TORSO_SX + 0.02, 0.035, kumas(s.kusak), [0, 0.06, 0], [Math.PI / 2, 0, 0]); k.scale.set(1, TORSO_SZ / TORSO_SX * 1.15, 1); j.spine.add(k); }
  if (s.kemer) { const k = halka(torsoR(0.04) * TORSO_SX + 0.012, 0.02, mat(s.kemer, { roughness: 0.4 }), [0, 0.04, 0], [Math.PI / 2, 0, 0]); k.scale.set(1, TORSO_SZ / TORSO_SX * 1.12, 1); j.spine.add(k); }
  // kürk yaka
  if (s.kurk) { const y = halka(0.12, 0.045, kumas(s.kurk, { bumpScale: 5 }), [0, 0.33, -0.01], [Math.PI / 2 + 0.25, 0, 0]); y.scale.set(1.35, 0.8, 1); j.chest.add(y); }
  if (s.yaka) j.chest.add(halka(0.075, 0.018, kumas(s.yaka), [0, 0.355, 0.0], [Math.PI / 2 + 0.2, 0, 0]));
  if (s.dugme) for (let i = 0; i < 5; i++) j.chest.add(kure(0.011, mat(s.dugme, { metalness: 0.8, roughness: 0.3 }), [0, 0.02 + i * 0.06, torsoR(0.2 + i * 0.06) * TORSO_SZ + 0.012], null, 12));
  if (s.kravat) j.chest.add(kutu(0.04, 0.2, 0.01, kumas(s.kravat), [0, 0.22, torsoR(0.38) * TORSO_SZ + 0.006], [-0.15, 0, 0]));
  if (s.genisKol) for (const k of ['lEl', 'rEl']) j[k].add(silindir(0.06, 0.12, 0.26, ust.clone ? ust : ust, [0, -0.13, 0], [0, 0, 0], 24, true));
  if (s.olcek) h.root.scale.setScalar(s.olcek);
  return h;
}

// ---------- hazır roller ----------
const ROL = {
  padisah: { ust: 0x5b2a86, alt: 0xe8d6a8, etek: 'kaftan', kurk: 0xd8c8a8, kusak: 0xd9a83a, bas: 'kavuk', sakal: 'kisa', etekUc: 0xe3b23c },
  sehzade: { ust: 0x2f63c9, alt: 0xe8dcc0, etek: 'kaftan', kusak: 0xd9a83a, bas: 'fes', basArgs: [0xb51f24], sakal: 'yok' }, // genç şehzade (fes yerine küçük kavuk istersen basArgs değiştir)
  sehzade_cocuk: { ust: 0x3fa35b, alt: 0xe8dcc0, etek: 'kaftan', kusak: 0xd9a83a, bas: 'sarik', basArgs: [0xf7f3ea, 0x3fa35b], sakal: 'yok', olcek: 0.62 },
  vezir: { ust: 0x2e7d4f, alt: 0xe8d6a8, etek: 'kaftan', kurk: 0xc9b48a, kusak: 0xb3202c, bas: 'mucevveze', sakal: 'uzun', sakalRenk: 0x777068 },
  sadrazam: { ust: 0xf2ede2, alt: 0xe8d6a8, etek: 'kaftan', kurk: 0xc9b48a, kusak: 0x2e7d4f, bas: 'mucevveze', sakal: 'uzun', sakalRenk: 0x9a948c },
  seyhulislam: { ust: 0xf4f1ea, alt: 0xf4f1ea, etek: 'cubbe', genisKol: true, kusak: 0x2e7d4f, bas: 'mucevveze', basArgs: [0xffffff], sakal: 'uzun', sakalRenk: 0xdcd8d0 },
  ulema: { ust: 0x2c3a5a, alt: 0xe8e2d0, etek: 'cubbe', genisKol: true, bas: 'sarik', sakal: 'uzun' },
  yeniceri: { ust: 0x2a5aa8, alt: 0xa82a2a, etek: 'kaftan', etekBoy: 0.6, kusak: 0xb3202c, bas: 'bork', sakal: 'biyik', cizme: 0xa8202a },
  cellat: { ust: 0x6a1212, alt: 0x2a1a14, etek: 'entari', etekBoy: 0.5, kusak: 0x1a1210, bas: 'cellat', sakal: 'kisa', sakalRenk: 0x1a1210, cizme: 0x2a1a14 },
  dilsiz: { ust: 0x1d1d22, alt: 0x1d1d22, etek: 'entari', etekBoy: 0.55, kusak: 0x6a1212, bas: 'takke', basArgs: [0x6a1212], sakal: 'yok', cizme: 0x1a1a1a },
  hekim: { ust: 0x2a2a3a, alt: 0xd8d0c0, etek: 'cubbe', genisKol: true, bas: 'sarik', basArgs: [0xe8e0d0, 0x2a2a3a], sakal: 'kisa' },
  kahveci: { ust: 0xa0522d, alt: 0x3a2a20, kusak: 0x2a5aa8, bas: 'fes', sakal: 'biyik', cizme: 0x3a2a20 },
  halk_erkek: { ust: 0x6a5a3a, alt: 0x3a3a48, etek: 'entari', etekBoy: 0.45, kusak: 0x8a2a2a, bas: 'sarik', basArgs: [0xe8e0d0, 0x6a2a2a], sakal: 'kisa', cizme: 0x3a2a20 },
  halk_kadin: { ust: 0x3a4a6a, alt: 0x3a4a6a, etek: 'ferace', etekBoy: 0.86, bas: 'yasmak', kadin: true, cizme: 0x2a2020 },
  valide_sultan: { ust: 0x7a1a3a, alt: 0xe8d0b0, etek: 'kaftan', etekBoy: 0.88, kurk: 0xe8dcc8, kusak: 0xd9a83a, bas: 'hotoz', kadin: true, cizme: 0xc9a04a },
  cariye: { ust: 0xd27a9a, alt: 0xf0e0d0, etek: 'entari', etekBoy: 0.86, bas: 'hotoz', basArgs: [0xd27a9a], kadin: true },
  dervis: { ust: 0xf4f1ea, alt: 0xf4f1ea, etek: 'cubbe', etekBoy: 0.86, bas: 'sikke', sakal: 'uzun', sakalRenk: 0x4a3a2a },
  tellak: { ust: 0xe8b090, alt: 0xb03030, ten: 0xe8b090, kemer: 0xb03030, bas: 'yok', sakal: 'yok' },
  subay_1920: { ust: 0x6b6a45, alt: 0x6b6a45, etek: 'palto', etekBoy: 0.7, kemer: 0x3a2a1a, dugme: 0xd9a83a, bas: 'kalpak', sakal: 'biyik', cizme: 0x1a1410 },
  mehmetcik: { ust: 0x8a7a52, alt: 0x8a7a52, kemer: 0x5a4028, bas: 'kabalak', sakal: 'biyik', cizme: 0x4a3a28 },
  mebus: { ust: 0x23232a, alt: 0x23232a, etek: 'palto', etekBoy: 0.55, yaka: 0xf2f2f2, dugme: 0x111111, bas: 'kalpak', sakal: 'biyik', cizme: 0x111111 },
  cumhuriyet_beyi: { ust: 0x3a3f4a, alt: 0x3a3f4a, yaka: 0xf2f2f2, kravat: 0x8a1a1a, dugme: 0x111111, bas: 'sapka', sakal: 'biyik', cizme: 0x1a1210 },
  cumhuriyet_hanimi: { ust: 0x2a5a7a, alt: 0x2a5a7a, etek: 'entari', etekBoy: 0.62, yaka: 0xf2f2f2, kadin: true, cizme: 0x1a1210 },
  ogretmen: { ust: 0x4a3a2a, alt: 0x3a3f4a, yaka: 0xf2f2f2, kravat: 0x1a3a6a, bas: 'yok', sakal: 'biyik', cizme: 0x1a1210 },
  cocuk: { ust: 0x8a2a2a, alt: 0x2a3a5a, bas: 'kasket', sakal: 'yok', olcek: 0.6 },
  ingiliz_subay: { ust: 0x7a6a45, alt: 0x7a6a45, kemer: 0x5a2a1a, dugme: 0xd9a83a, bas: 'askeriKep', sakal: 'biyik', sakalRenk: 0x8a6a3a, ten: 0xf0b8a0, cizme: 0x3a2214 },
  kemanci: { ust: 0x6a2a5a, alt: 0x2a2a3a, etek: 'entari', etekBoy: 0.45, kusak: 0xd9a83a, bas: 'fes', sakal: 'biyik' },
};
export const ROLLER = Object.keys(ROL);
export function karakter(rol, ekle = {}) {
  const base = ROL[rol]; if (!base) throw new Error('rol yok: ' + rol);
  const h = makeHuman('archer');
  // kukuleyi kaldır
  h.root.traverse(c => { if (c.isMesh && c.geometry.type === 'SphereGeometry' && c.geometry.parameters.radius === 0.135) c.visible = false; });
  giydir(h, { ...base, ...ekle });
  h.rol = rol;
  return h;
}
