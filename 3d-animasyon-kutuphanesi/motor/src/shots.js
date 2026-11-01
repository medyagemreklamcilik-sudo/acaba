// KATALOG: kütüphanedeki her öğe 1 saniyelik bir "çekim". node render.mjs stills 0.5,1.5,... katalog
// Yeni bir video için bu dosyayı kopyala ve kendi SHOTS listeni yaz (bkz. ../README.md).
import * as THREE from 'three';
import { cam, place } from './anim.js';
import { karakter, ROLLER } from './kutuphane/karakterler.js';
import { PROPLAR } from './kutuphane/proplar.js';
import { MEKANLAR } from './kutuphane/mekanlar.js';
import * as H from './kutuphane/hareketler.js';

function cerceve(obj, c, { yon = [0.45, 0.3, 1], pad = 1.2 } = {}) {
  obj.updateMatrixWorld(true);
  const b = new THREE.Box3().setFromObject(obj), ctr = b.getCenter(new THREE.Vector3()), sz = b.getSize(new THREE.Vector3());
  const tv = Math.tan(THREE.MathUtils.degToRad(c.fov / 2)), th = tv * 9 / 16;
  const d = Math.max(sz.y / 2 / tv, Math.max(sz.x, sz.z) / 2 / th) * pad + Math.max(sz.x, sz.z) / 2;
  const v = new THREE.Vector3(...yon).normalize().multiplyScalar(d);
  place(c, [ctr.x + v.x, ctr.y + v.y, ctr.z + v.z], [ctr.x, ctr.y - sz.y * 0.05, ctr.z]);
}
const studyo = (makeStage) => makeStage({ shadowSize: 4, sunDir: [-3, 6, 4] });

const ITEMS = [];
// --- karakterler ---
for (const r of ROLLER) ITEMS.push({ ad: 'karakter: ' + r, build(ms) { const s = studyo(ms); const h = karakter(r); h.setPose(H.DUR); s.add(h.root); const c = cam(30); cerceve(h.root, c, { pad: 1.15 }); return { scene: s, camera: c, update(t) { h.setPose(H.NEFES(t)); } }; } });
// --- pozlar ---
const POZLAR = { OTUR: 'OTUR', BAGDAS: 'BAGDAS', TEMENNA: 'TEMENNA', SECDE: 'SECDE', DUA: 'DUA', ASKER_SELAMI: 'ASKER_SELAMI', ISARET: 'ISARET', KOLLAR_BELDE: 'KOLLAR_BELDE', KOLLAR_KAVUSUK: 'KOLLAR_KAVUSUK', ELLER_HAVADA: 'ELLER_HAVADA', BOGAZ_TUT: 'BOGAZ_TUT', KITAP_OKU: 'KITAP_OKU', KURSU_KONUS: 'KURSU_KONUS' };
for (const p of Object.keys(POZLAR)) ITEMS.push({ ad: 'poz: ' + p, build(ms) { const s = studyo(ms); const h = karakter(p === 'ASKER_SELAMI' ? 'mehmetcik' : p === 'KURSU_KONUS' ? 'mebus' : 'halk_erkek'); h.setPose(H[p]); s.add(h.root); const c = cam(30); cerceve(h.root, c, { pad: 1.2 }); return { scene: s, camera: c, update() { h.setPose(H[p]); } }; } });
ITEMS.push({ ad: 'hareket: YURU', build(ms) { const s = studyo(ms); const h = karakter('yeniceri'); s.add(h.root); const c = cam(30); h.setPose(H.DUR); cerceve(h.root, c); return { scene: s, camera: c, update(t) { h.setPose(H.YURU(t + 0.15)); } }; } });
ITEMS.push({ ad: 'hareket: SEMA', build(ms) { const s = studyo(ms); const h = karakter('dervis'); s.add(h.root); const c = cam(30); h.setPose(H.SEMA(0)); cerceve(h.root, c); return { scene: s, camera: c, update(t) { h.setPose(H.SEMA(t)); h.root.rotation.y = t * 4; } }; } });
ITEMS.push({ ad: 'hareket: BOGUL_DUS', build(ms) { const s = studyo(ms); const h = karakter('sehzade'); s.add(h.root); const c = cam(32); h.setPose(H.DUR); cerceve(h.root, c, { yon: [1, 0.3, 0.6], pad: 1.4 }); return { scene: s, camera: c, update() { h.setPose(H.BOGUL_DUS(0.45)); H.dusur(h, 0.45); h.setMouth(1); } }; } });
// --- objeler ---
const PROP_ARG = { kitap: [], ferman: [] };
for (const [ad, f] of Object.entries(PROPLAR)) ITEMS.push({ ad: 'obje: ' + ad, build(ms) {
  const s = studyo(ms); const o = f(...(PROP_ARG[ad] || [])); s.add(o);
  if (ad === 'ferman') { o.position.y = 1.3; o.rotation.x = -0.2; }
  if (ad === 'kitap') o.guncelle(0.38);
  const c = cam(30); cerceve(o, c, { yon: ad === 'kitap' ? [0.2, 1.1, 0.8] : [0.6, 0.35, 1], pad: 1.25 });
  return { scene: s, camera: c, update(t) { if (o.guncelle && ad !== 'kitap') o.guncelle(ad === 'ferman' ? 0.75 : t); } };
} });
// --- mekanlar ---
const MK = { sarayIc: [[0, 1.7, 6], [0, 1.6, -2]], divan: [[0, 1.8, 5.5], [0, 1.2, -2]], kahvehane: [[0.5, 1.7, 3.5], [-0.3, 0.9, -2]], sokak: [[0, 1.7, 6], [0, 2, -6]], meclis: [[0.8, 1.8, 5.2], [0, 1.6, -2.5]], hamam: [[0, 1.6, 4.5], [0, 1.3, -1.5]], mezarlik: [[0, 1.6, 5], [0, 0.9, -1.5]], cephe: [[0, 1.6, 4.5], [0, 1.0, -2]], deniz: [[6, 3, 9], [0, 1.5, 0]], acikAlan: [[0, 1.7, 5], [0, 1, 0]] };
for (const [ad, f] of Object.entries(MEKANLAR)) ITEMS.push({ ad: 'mekan: ' + ad, build(ms) {
  const s = studyo(ms); const m = f(s); if (ad === 'deniz') { const k = (PROPLAR.kadirga)(); k.position.y = -0.1; s.add(k); m.ek = k; }
  const c = cam(40); place(c, ...MK[ad]); return { scene: s, camera: c, update(t) { m.guncelle(t); m.ek?.guncelle(t); } };
} });
// --- örnek sahneler (kütüphane birlikte nasıl kullanılır) ---
ITEMS.push({ ad: 'sahne: kardes katli', build(ms) {
  const s = studyo(ms); const m = MEKANLAR.sarayIc(s, { gece: true });
  const th = PROPLAR.taht(); th.position.z = -1.8; s.add(th);
  const p = karakter('padisah'); p.root.position.set(0, th.oturmaY, -1.85); p.setPose(H.OTUR_ISARET); s.add(p.root);
  const c1 = karakter('cellat'); c1.root.position.set(-1.0, 0, -0.6); c1.root.rotation.y = 0.5; c1.setPose(H.KOLLAR_KAVUSUK); s.add(c1.root);
  const c2 = karakter('dilsiz'); c2.root.position.set(1.0, 0, -0.6); c2.root.rotation.y = -0.5; c2.setPose(H.KOLLAR_KAVUSUK); s.add(c2.root);
  const sh = []; for (let i = 0; i < 5; i++) { const h = karakter(i % 2 ? 'sehzade' : 'sehzade_cocuk', { ust: [0x2f63c9, 0x3fa35b, 0xc9a12a, 0x8a3fb0, 0x2a8aa0][i] }); h.root.position.set((i - 2) * 0.55, 0, 0.9); h.root.rotation.y = Math.PI; s.add(h.root); sh.push(h); }
  const tb = PROPLAR.tabut(); tb.position.set(1.6, 0, 1.6); tb.rotation.y = 0.4; s.add(tb);
  const c = cam(40); place(c, [0.8, 2.6, 7.8], [0, 0.9, -0.6]);
  return { scene: s, camera: c, update(t) { m.guncelle(t); sh.forEach((h, i) => h.setPose(H.NEFES(t + i, H.DUR))); } };
} });
ITEMS.push({ ad: 'sahne: kahvehane', build(ms) {
  const s = studyo(ms); const m = MEKANLAR.kahvehane(s);
  const k = karakter('kahveci'); k.root.position.set(1.2, 0, -1.0); k.root.rotation.y = -0.6; k.setPose(H.DUR); s.add(k.root);
  const a = karakter('halk_erkek'); a.root.position.set(-0.4, 0.0, -2.35); a.setPose(H.OTUR); a.root.position.y = 0.0; s.add(a.root);
  const b = karakter('yeniceri'); b.root.position.set(0.6, 0, -2.35); b.setPose(H.OTUR); s.add(b.root);
  const c = cam(40); place(c, [0.5, 1.6, 3.2], [0, 0.9, -1.8]);
  return { scene: s, camera: c, update(t) { m.guncelle(t); H.konus(a, t); } };
} });
ITEMS.push({ ad: 'sahne: meclis 1920', build(ms) {
  const s = studyo(ms); const m = MEKANLAR.meclis(s);
  const k = karakter('mebus'); k.root.position.set(0, 0.2, -2.7); k.setPose(H.KURSU_KONUS); s.add(k.root);
  for (let i = 0; i < 6; i++) { const h = karakter(i % 3 === 0 ? 'subay_1920' : 'mebus'); h.root.position.set((i % 3 - 1) * 0.8 + (i < 3 ? -1.6 : 1.6) * 0.0 + (i < 3 ? -1.2 : 1.2), 0.3, 1.0 + Math.floor(i / 3) * 0.0); h.root.rotation.y = Math.PI; h.setPose(H.OTUR); s.add(h.root); }
  const c = cam(40); place(c, [1.0, 2.2, 5.0], [0, 1.4, -2.0]);
  return { scene: s, camera: c, update(t) { m.guncelle(t); H.konus(k, t, 0.6); } };
} });
ITEMS.push({ ad: 'sahne: cephe', build(ms) {
  const s = studyo(ms); const m = MEKANLAR.cephe(s);
  const sb = karakter('subay_1920'); sb.root.position.set(0.4, 0, 0.0); sb.setPose(H.ISARET); sb.root.rotation.y = -0.4; s.add(sb.root);
  for (let i = 0; i < 3; i++) { const h = karakter('mehmetcik'); h.root.position.set(-0.8 + i * 0.6, -0.25, 0.9); h.root.rotation.y = Math.PI * 0.9; h.setPose({ ...H.DUR, spine: [0.3, 0, 0] }); s.add(h.root); }
  const c = cam(40); place(c, [2.2, 1.9, 6.8], [0, 1.0, -0.6]);
  return { scene: s, camera: c, update(t) { m.guncelle(t); } };
} });
ITEMS.push({ ad: 'sahne: lozan', build(ms) {
  const s = studyo(ms); MEKANLAR.meclis(s);
  const ms_ = PROPLAR.lozanMasasi(); ms_.position.z = 0.6; s.add(ms_);
  const tr = karakter('cumhuriyet_beyi'); tr.root.position.set(-0.8, 0, 1.6); tr.root.rotation.y = Math.PI; tr.setPose(H.OTUR); s.add(tr.root);
  const en = karakter('ingiliz_subay'); en.root.position.set(0.8, 0, -0.4); en.setPose(H.OTUR); s.add(en.root);
  const c = cam(40); place(c, [4.2, 3.2, 5.6], [0, 0.8, 0.6]);
  return { scene: s, camera: c, update() {} };
} });
ITEMS.push({ ad: 'sahne: hoca ve esek', build(ms) {
  const s = studyo(ms); MEKANLAR.acikAlan(s, { renk: 0x9a8a5a });
  const e = PROPLAR.esek(); e.position.set(0.2, 0, 0); e.rotation.y = -0.3; s.add(e);
  const h = karakter('ulema', { ust: 0x6a5a3a }); h.root.position.set(-0.05, 0.64, 0.0); h.setPose({ ...H.OTUR, lHip: [-1.25, 0, 0.75], rHip: [-1.25, 0, -0.75], lKn: [1.2, 0, 0], rKn: [1.2, 0, 0] }); h.root.rotation.y = -Math.PI / 2; e.add(h.root); // eşeğe ters biner
  const c = cam(36); place(c, [1.6, 1.7, 4.4], [0.1, 1.1, 0]);
  return { scene: s, camera: c, update(t) { e.guncelle(t); } };
} });
ITEMS.push({ ad: 'sahne: kitap sayfa cevirme', build(ms) {
  const s = studyo(ms); MEKANLAR.sarayIc(s, { gece: true });
  const k = PROPLAR.kitap(); k.position.set(0, 0.8, 0); s.add(k); const sd = PROPLAR.samdan(); sd.position.set(0.35, 0.8, -0.15); s.add(sd);
  const ms_ = PROPLAR.masa({ en: 1.2, derin: 0.7, ortu: 0x5a1a24 }); ms_.position.y = 0.02; s.add(ms_);
  const c = cam(32); place(c, [0.15, 1.55, 0.75], [0, 0.82, 0]);
  return { scene: s, camera: c, update(t) { k.guncelle(0.3 + t * 0.4); } };
} });

export const DURATION = ITEMS.length;
export const CAPTIONS = ITEMS.map((it, i) => [i, it.ad, i + 0.99]);
export const FADES = [];
export const SHOTS = ITEMS.map((it, i) => ({ start: i, end: i + 1, build: ({ makeStage }) => it.build(makeStage) }));
export const KATALOG = ITEMS.map(i => i.ad);
