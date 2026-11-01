// Objeler. Her fonksiyon THREE.Group döner; hareketli olanlarda g.guncelle(t) vardır.
import * as THREE from 'three';
import { glowSprite } from '../props.js';
import { kumas, mat, altin, gumus, bronz, tahta, parlak, mesh, kutu, kure, silindir, halka, torna, grup, kanvas, hatSatirlari, tugraCiz, bayrakDokusu } from './ortak.js';

const G = () => new THREE.Group();
const kirmizi = () => kumas(0xa61f2c), bordo = () => kumas(0x6e1824);

// ---------------- saray ----------------
export function taht() {
  const g = G(), a = altin(), r = kirmizi(), d = bordo();
  g.add(kutu(1.6, 0.12, 1.2, d, [0, 0.06, 0]), kutu(1.3, 0.12, 1.0, r, [0, 0.18, -0.05]), kutu(0.95, 0.22, 0.7, a, [0, 0.35, -0.12]), kutu(0.8, 0.07, 0.6, r, [0, 0.49, -0.1]));
  g.add(kutu(0.95, 1.25, 0.12, a, [0, 1.0, -0.48]), kutu(0.7, 0.9, 0.04, r, [0, 1.0, -0.41]));
  g.add(mesh(new THREE.CylinderGeometry(0.475, 0.475, 0.12, 40, 1, false, 0, Math.PI), a, [0, 1.62, -0.48], [Math.PI / 2, 0, Math.PI / 2]));
  g.add(kure(0.07, mat(0xfff0b0, { emissive: 0x806020, metalness: 0.5 }), [0, 1.98, -0.42]));
  for (const s of [-1, 1]) g.add(kutu(0.12, 0.42, 0.62, a, [s * 0.47, 0.62, -0.12]), kure(0.075, a, [s * 0.47, 0.86, 0.17]));
  g.oturmaY = 0.24; return g; // karakter.root.position.y = oturmaY, poz OTUR
}
export function tabut(orti = 0x1f5a32, kavuklu = true) { // yeşil örtülü tabut, baş ucunda kavuk
  const g = G();
  const sh = new THREE.Shape(); sh.moveTo(-0.95, 0); sh.lineTo(0.95, 0); sh.lineTo(0.95, 0.32); sh.quadraticCurveTo(0, 0.55, -0.95, 0.32); sh.closePath();
  const geo = new THREE.ExtrudeGeometry(sh, { depth: 0.5, bevelEnabled: true, bevelSize: 0.02, bevelThickness: 0.02 }); geo.translate(0, 0, -0.25);
  g.add(mesh(geo, tahta(11, 0x7a5a3a), [0, 0.42, 0]));
  const o = mesh(new THREE.ExtrudeGeometry(sh, { depth: 0.54, bevelEnabled: false }), kumas(orti, { side: THREE.DoubleSide }), [0, 0.44, 0], [0, 0, 0], [1.03, 1.05, 1]); o.geometry.translate(0, 0, -0.27); g.add(o);
  for (const x of [-0.75, 0.75]) for (const z of [-0.2, 0.2]) g.add(kutu(0.06, 0.42, 0.06, tahta(3), [x, 0.21, z]));
  for (const z of [-0.36, 0.36]) g.add(kutu(2.4, 0.05, 0.05, tahta(5), [0, 0.38, z]));
  if (kavuklu) { const k = grup(kure(0.11, kumas(0xf7f3ea), [0, 0, 0], [1, 0.8, 1]), halka(0.1, 0.02, kumas(0xf7f3ea), [0, -0.03, 0], [Math.PI / 2, 0, 0])); k.position.set(-0.85, 0.88, 0); g.add(k); }
  return g;
}
export function kemend() { // ipek yay kirişi
  const pts = []; for (let i = 0; i <= 40; i++) { const t = i / 40; pts.push(new THREE.Vector3(Math.sin(t * 9) * 0.05, -t * 0.7, Math.cos(t * 7) * 0.05 + t * 0.1)); }
  return grup(mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 80, 0.008, 8), kumas(0xd8c8a0)));
}
export function yatagan() {
  const g = G(), b = gumus();
  const sh = new THREE.Shape(); sh.moveTo(0, 0); sh.quadraticCurveTo(0.06, 0.35, -0.02, 0.62); sh.lineTo(-0.035, 0.6); sh.quadraticCurveTo(0.03, 0.35, -0.025, 0); sh.closePath();
  g.add(mesh(new THREE.ExtrudeGeometry(sh, { depth: 0.006, bevelEnabled: false }), b, [0, 0.12, 0]));
  g.add(silindir(0.014, 0.016, 0.12, mat(0xe8e0d0), [-0.01, 0.06, 0.003]), kure(0.022, mat(0xe8e0d0), [-0.01, -0.005, 0.003], [1.3, 0.8, 1]));
  return g;
}
export function kilic() {
  const g = G(); g.add(kutu(0.035, 0.85, 0.006, gumus(), [0, 0.5, 0]), kutu(0.2, 0.025, 0.04, altin(), [0, 0.07, 0]), silindir(0.016, 0.016, 0.14, kumas(0x3a1a10), [0, -0.01, 0]), kure(0.025, altin(), [0, -0.09, 0])); return g;
}
export function kafes() { // harem/şehzade kafesi: ahşap kafesli pencere
  const g = G(), w = tahta(9, 0x6a4a2a);
  const d = kanvas(512, 680, (x, W, H) => { x.clearRect(0, 0, W, H); x.strokeStyle = '#6a4424'; x.lineWidth = 14; for (let i = -H; i < W + H; i += 46) { x.beginPath(); x.moveTo(i, 0); x.lineTo(i + H, H); x.stroke(); x.beginPath(); x.moveTo(i, H); x.lineTo(i + H, 0); x.stroke(); } });
  g.add(kutu(1.2, 1.6, 0.04, mat(0x0d0a08), [0, 0.8, -0.05]));
  g.add(mesh(new THREE.PlaneGeometry(1.2, 1.6), new THREE.MeshStandardMaterial({ map: d, transparent: true, alphaTest: 0.5, side: THREE.DoubleSide, roughness: 0.8 }), [0, 0.8, 0]));
  for (const [x, y, ww, hh] of [[0, 1.62, 1.32, 0.08], [0, -0.02, 1.32, 0.08], [-0.62, 0.8, 0.08, 1.7], [0.62, 0.8, 0.08, 1.7]]) g.add(kutu(ww, hh, 0.08, w, [x, y, 0.02]));
  return g;
}
export function dolap(acik = 0.6) { // Kösem'in saklandığı dolap; g.guncelle(t) kapağı açar
  const g = G(), w = tahta(13, 0x8a5a3a);
  g.add(kutu(0.9, 1.9, 0.05, w, [0, 0.95, -0.3]), kutu(0.05, 1.9, 0.6, w, [-0.45, 0.95, 0]), kutu(0.05, 1.9, 0.6, w, [0.45, 0.95, 0]), kutu(0.9, 0.05, 0.6, w, [0, 1.9, 0]), kutu(0.9, 0.05, 0.6, w, [0, 0.025, 0]));
  const kap = G(); kap.position.set(-0.45, 0, 0.3); g.add(kap);
  kap.add(kutu(0.88, 1.85, 0.04, w, [0.44, 0.95, 0]), kure(0.025, altin(), [0.8, 0.95, 0.03]));
  for (let i = 0; i < 2; i++) kap.add(kutu(0.7, 0.75, 0.01, tahta(17, 0x6a4022), [0.44, 0.55 + i * 0.85, 0.025]));
  g.guncelle = t => { kap.rotation.y = -acik * t; }; g.guncelle(1); return g;
}
export function sandik() { const g = G(), w = tahta(19, 0x7a4a2a); g.add(kutu(0.8, 0.4, 0.45, w, [0, 0.2, 0]), mesh(new THREE.CylinderGeometry(0.225, 0.225, 0.8, 24, 1, false, 0, Math.PI), w, [0, 0.4, 0], [0, 0, Math.PI / 2]), kutu(0.82, 0.04, 0.47, altin(), [0, 0.12, 0]), kutu(0.08, 0.1, 0.02, altin(), [0, 0.38, 0.235])); return g; }
export function minder(renk = 0xa61f2c) { const g = G(); g.add(mesh(new THREE.BoxGeometry(0.6, 0.14, 0.6, 4, 2, 4), kumas(renk), [0, 0.07, 0])); g.add(...[-1, 1].flatMap(a => [-1, 1].map(b => kure(0.03, altin(), [a * 0.3, 0.07, b * 0.3])))); return g; }
export function sedir(boy = 2.4, renk = 0xa61f2c) { const g = G(); g.add(kutu(boy, 0.35, 0.7, tahta(21, 0x6a4a2a), [0, 0.175, 0]), kutu(boy, 0.12, 0.68, kumas(renk), [0, 0.41, 0.01]), kutu(boy, 0.5, 0.18, kumas(0x8a1a24), [0, 0.65, -0.27])); return g; }

// ---------- belge / yazı ----------
export function ferman() { // g.guncelle(t): 0 = rulo, 1 = tamamen açık
  const g = G();
  const doku = kanvas(512, 1400, (x, w, h) => { x.fillStyle = '#efe1bd'; x.fillRect(0, 0, w, h); x.fillStyle = 'rgba(120,80,30,.08)'; for (let i = 0; i < 60; i++) x.fillRect(Math.random() * w, Math.random() * h, 30, 2); tugraCiz(x, w * 0.5, h * 0.11, w * 0.32); hatSatirlari(x, w, h, { ust: 0.24, alt: 0.94, satir: 16, kenar: 0.12 }); });
  const L = 1.2, W = 0.45;
  const kag = mesh(new THREE.PlaneGeometry(W, L), new THREE.MeshStandardMaterial({ map: doku, roughness: 0.9, side: THREE.DoubleSide }));
  const ru = silindir(0.03, 0.03, W + 0.02, mat(0xe8d6a8, { roughness: 0.8 }), [0, 0, 0], [0, 0, Math.PI / 2]);
  const ust = silindir(0.03, 0.03, W + 0.02, mat(0xe8d6a8, { roughness: 0.8 }), [0, 0, 0], [0, 0, Math.PI / 2]);
  g.add(kag, ru, ust);
  g.guncelle = t => { const k = Math.max(0.02, Math.min(1, t)); kag.scale.y = k; kag.position.y = -L * k / 2; kag.material.map.repeat.set(1, k); kag.material.map.offset.set(0, 1 - k); ru.position.y = -L * k; ru.scale.setScalar(1 + (1 - k) * 0.8); ru.scale.x = ru.scale.z = 1 + (1 - k) * 0.8; ru.scale.y = 1; };
  g.guncelle(1); return g;
}
export function kitap({ renk = 0x6a1a1a, sayfa = 'hat' } = {}) { // g.guncelle(t): t 0→1 bir sayfa çevrilir; t 1→2 ikinci sayfa
  const g = G(), W = 0.32, H = 0.44;
  const sayfaDoku = (s) => kanvas(384, 512, (x, w, h) => { x.fillStyle = '#f1e4c4'; x.fillRect(0, 0, w, h); x.strokeStyle = '#b08a40'; x.lineWidth = 6; x.strokeRect(22, 22, w - 44, h - 44); x.lineWidth = 2; x.strokeRect(32, 32, w - 64, h - 64); hatSatirlari(x, w, h, { ust: 0.14, alt: 0.86, satir: 12, seed: s, kenar: 0.15 }); });
  const kapak = kumas(renk, { bumpScale: 2 });
  g.add(kutu(W, 0.012, H, kapak, [-W / 2, 0, 0]), kutu(W, 0.012, H, kapak, [W / 2, 0, 0]));
  g.add(mesh(new THREE.BoxGeometry(W - 0.015, 0.03, H - 0.02), [mat(0xe8dcc0), mat(0xe8dcc0), new THREE.MeshStandardMaterial({ map: sayfaDoku(1), roughness: 0.9 }), mat(0xe8dcc0), mat(0xe8dcc0), mat(0xe8dcc0)], [-W / 2 + 0.005, 0.021, 0]));
  g.add(mesh(new THREE.BoxGeometry(W - 0.015, 0.03, H - 0.02), [mat(0xe8dcc0), mat(0xe8dcc0), new THREE.MeshStandardMaterial({ map: sayfaDoku(2), roughness: 0.9 }), mat(0xe8dcc0), mat(0xe8dcc0), mat(0xe8dcc0)], [W / 2 - 0.005, 0.021, 0]));
  // çevrilen sayfa: segmentli düzlem, sırt (x=0) etrafında kıvrılır
  const geo = new THREE.PlaneGeometry(W - 0.015, H - 0.02, 24, 1); geo.rotateX(-Math.PI / 2); geo.translate((W - 0.015) / 2, 0, 0);
  const base = geo.attributes.position.array.slice();
  const on = sayfaDoku(3), arka = sayfaDoku(4);
  const pg = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: on, roughness: 0.9, side: THREE.DoubleSide })); pg.position.y = 0.038; pg.castShadow = true; g.add(pg);
  g.guncelle = t => {
    const ph = ((t % 1) + 1) % 1, a = Math.PI * (ph < 0.5 ? 2 * ph * ph : 1 - 2 * (1 - ph) * (1 - ph)); // easeInOut
    const curl = Math.sin(ph * Math.PI) * 1.6; const p = geo.attributes.position;
    for (let i = 0; i < p.count; i++) {
      const x0 = base[i * 3], z0 = base[i * 3 + 2], u = x0 / (W - 0.015);
      const ang = a + curl * u * u * 0.6; // uca doğru fazla kıvrılır
      p.setXYZ(i, Math.cos(ang) * x0, Math.sin(ang) * x0, z0);
    }
    p.needsUpdate = true; geo.computeVertexNormals();
    pg.material.map = (a > Math.PI / 2) ? arka : on;
  };
  g.guncelle(0); return g;
}
export function muhur() { const g = G(); g.add(silindir(0.04, 0.05, 0.08, mat(0x3a2a1a), [0, 0.12, 0]), kure(0.045, mat(0x3a2a1a), [0, 0.18, 0]), silindir(0.06, 0.06, 0.03, altin(), [0, 0.065, 0])); return g; }
export function tugraLevha() { const d = kanvas(768, 512, (x, w, h) => { x.fillStyle = '#123a2a'; x.fillRect(0, 0, w, h); x.strokeStyle = '#d9a83a'; x.lineWidth = 14; x.strokeRect(20, 20, w - 40, h - 40); tugraCiz(x, w * 0.48, h * 0.55, h * 0.55, '#e8c060'); }); const g = G(); g.add(kutu(1.2, 0.8, 0.05, tahta(5, 0x5a3a1a), [0, 0, -0.03]), mesh(new THREE.PlaneGeometry(1.1, 0.72), new THREE.MeshStandardMaterial({ map: d, roughness: 0.6 }), [0, 0, 0.001])); return g; }
export function hokkaKalem() { const g = G(); g.add(silindir(0.05, 0.06, 0.07, bronz(), [0, 0.035, 0]), kure(0.04, mat(0x111111), [0, 0.07, 0], [1, 0.3, 1]), silindir(0.005, 0.004, 0.28, tahta(2, 0xc8a070), [0.08, 0.06, 0], [0, 0, 1.2])); return g; }
export function zehirSisesi() { const g = G(); g.add(torna([[0, 0], [0.06, 0.01], [0.07, 0.08], [0.03, 0.15], [0.02, 0.22], [0.025, 0.24]], mat(0x2a6a3a, { transparent: true, opacity: 0.75, roughness: 0.1, metalness: 0.2 })), silindir(0.022, 0.018, 0.05, tahta(4), [0, 0.26, 0])); g.add(kure(0.05, parlak(0x3aff6a), [0, 0.05, 0], [1, 0.5, 1])); return g; }
export function serbetKadehi() { const g = G(); g.add(torna([[0.0, 0], [0.05, 0], [0.012, 0.02], [0.012, 0.09], [0.06, 0.12], [0.07, 0.2]], altin()), kure(0.06, mat(0x8a1a2a, { roughness: 0.1 }), [0, 0.17, 0], [1, 0.3, 1])); return g; }

// ---------- kahvehane ----------
export function fincan() { const g = G(); g.add(torna([[0, 0], [0.035, 0.002], [0.045, 0.05], [0.047, 0.055]], mat(0xf2ede4, { roughness: 0.2 })), kure(0.04, mat(0x2a1408, { roughness: 0.1 }), [0, 0.045, 0], [1, 0.08, 1]), torna([[0, -0.01], [0.04, -0.01], [0.05, 0.03]], altin(), [0, 0, 0])); return g; }
export function cezve() { const g = G(); g.add(torna([[0, 0], [0.06, 0], [0.065, 0.06], [0.05, 0.11], [0.058, 0.14]], mat(0xb5652a, { metalness: 0.9, roughness: 0.3 })), silindir(0.008, 0.008, 0.32, bronz(), [0.2, 0.12, 0], [0, 0, 1.3])); return g; }
export function tepsi() { const g = G(); g.add(silindir(0.3, 0.28, 0.03, bronz(), [0, 0.015, 0], [0, 0, 0], 48), halka(0.3, 0.012, bronz(), [0, 0.03, 0], [Math.PI / 2, 0, 0])); return g; }
export function nargile() { const g = G(); g.add(torna([[0, 0], [0.13, 0.02], [0.15, 0.12], [0.08, 0.25], [0.03, 0.3]], mat(0x3a6a9a, { transparent: true, opacity: 0.8, roughness: 0.1 })), silindir(0.018, 0.025, 0.4, bronz(), [0, 0.5, 0]), torna([[0.02, 0], [0.07, 0.04], [0.05, 0.09]], mat(0x8a3a1a), [0, 0.7, 0]), kure(0.04, parlak(0xff6a20), [0, 0.79, 0], [1, 0.3, 1])); const hp = []; for (let i = 0; i <= 20; i++) { const t = i / 20; hp.push(new THREE.Vector3(0.05 + t * 0.6, 0.35 - Math.sin(t * Math.PI) * 0.3 + t * 0.2, t * 0.2)); } g.add(mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(hp), 40, 0.012, 8), kumas(0x6a1a2a))); return g; }
export function tabure() { const g = G(), w = tahta(23, 0x8a6a4a); g.add(kutu(0.4, 0.04, 0.4, w, [0, 0.35, 0])); for (const a of [-1, 1]) for (const b of [-1, 1]) g.add(kutu(0.04, 0.35, 0.04, w, [a * 0.17, 0.175, b * 0.17])); return g; }
export function tavla() { const d = kanvas(512, 384, (x, w, h) => { x.fillStyle = '#6a3a1a'; x.fillRect(0, 0, w, h); for (let i = 0; i < 12; i++) { x.fillStyle = i % 2 ? '#e8d0a0' : '#8a1a1a'; const bx = 24 + (i % 6) * 38 + (i >= 6 ? 236 : 0); x.beginPath(); x.moveTo(bx, 20); x.lineTo(bx + 34, 20); x.lineTo(bx + 17, 170); x.fill(); x.beginPath(); x.moveTo(bx, h - 20); x.lineTo(bx + 34, h - 20); x.lineTo(bx + 17, h - 170); x.fill(); } }); const g = G(); g.add(kutu(0.6, 0.03, 0.45, tahta(8, 0x5a3010), [0, 0.015, 0]), mesh(new THREE.PlaneGeometry(0.56, 0.41), new THREE.MeshStandardMaterial({ map: d }), [0, 0.031, 0], [-Math.PI / 2, 0, 0])); for (let i = 0; i < 8; i++) g.add(silindir(0.022, 0.022, 0.012, mat(i % 2 ? 0xf0e8d8 : 0x1a1a1a), [-0.2 + (i % 4) * 0.04, 0.04, i < 4 ? -0.15 : 0.15])); return g; }
export function mangal() { const g = G(); g.add(torna([[0.05, 0], [0.25, 0.25], [0.28, 0.3]], bronz()), kure(0.2, mat(0x2a1a10, { emissive: 0x6a1a00, emissiveIntensity: 1 }), [0, 0.28, 0], [1, 0.2, 1])); for (let i = 0; i < 6; i++) g.add(kure(0.04, parlak(0xff5a10), [Math.cos(i) * 0.12, 0.3, Math.sin(i) * 0.12])); const gl = glowSprite(0xff7a30, 0.9); gl.position.y = 0.4; gl.material.opacity = 0.6; g.add(gl); return g; }

// ---------- ışık ----------
export function mesale() { const g = G(); g.add(silindir(0.025, 0.03, 0.55, tahta(4, 0x4a3020), [0, 0.27, 0]), silindir(0.05, 0.035, 0.1, bronz(), [0, 0.58, 0])); const fl = glowSprite(0xffa040, 0.45); fl.position.y = 0.7; const co = glowSprite(0xfff0b0, 0.15); co.position.y = 0.68; const L = new THREE.PointLight(0xff9a50, 3, 6, 1.6); L.position.y = 0.75; g.add(fl, co, L); g.guncelle = t => { const f = 1 + 0.15 * Math.sin(t * 19) + 0.08 * Math.sin(t * 31); fl.scale.setScalar(0.45 * f); L.intensity = 3 * f; }; return g; }
export function samdan() { const g = G(); g.add(torna([[0.09, 0], [0.1, 0.02], [0.03, 0.05], [0.02, 0.25], [0.05, 0.27]], altin()), silindir(0.022, 0.022, 0.16, mat(0xf2ead8), [0, 0.35, 0])); const fl = glowSprite(0xffc070, 0.18); fl.position.y = 0.46; const L = new THREE.PointLight(0xffb060, 1.2, 3, 2); L.position.y = 0.47; g.add(fl, L); return g; }
export function kandil() { const g = G(); g.add(torna([[0, 0], [0.1, 0.05], [0.08, 0.12], [0.03, 0.14]], mat(0x5a8a6a, { transparent: true, opacity: 0.7, roughness: 0.1 }))); for (let i = 0; i < 3; i++) { const a = i * 2.09; g.add(silindir(0.002, 0.002, 0.5, bronz(), [Math.cos(a) * 0.05, 0.38, Math.sin(a) * 0.05], [Math.sin(a) * 0.1, 0, -Math.cos(a) * 0.1])); } const fl = glowSprite(0xffd080, 0.25); fl.position.y = 0.1; const L = new THREE.PointLight(0xffc070, 1.5, 4, 2); L.position.y = 0.05; g.add(fl, L); return g; }

// ---------- askeri ----------
export function top() { // bronz kuşatma topu (Fatih'in topları)
  const g = G(), b = bronz();
  const n = torna([[0.0, -0.8], [0.2, -0.8], [0.24, -0.6], [0.2, -0.5], [0.17, 0.8], [0.2, 0.85], [0.2, 0.9], [0.1, 0.9], [0.1, 0.0]], b, [0, 0.5, 0], [-Math.PI / 2 + 0.08, 0, 0], 40); g.add(n);
  g.add(kutu(0.5, 0.25, 1.6, tahta(6, 0x6a4a2a), [0, 0.2, -0.1]));
  for (const s of [-1, 1]) for (const z of [-0.6, 0.45]) { g.add(silindir(0.2, 0.2, 0.08, tahta(6, 0x5a3a1a), [s * 0.3, 0.2, z], [0, 0, Math.PI / 2])); g.add(halka(0.2, 0.015, mat(0x2a2a2a, { metalness: 0.8 }), [s * 0.34, 0.2, z], [0, Math.PI / 2, 0])); }
  g.namlu = n; return g;
}
export function gulle() { return grup(kure(0.18, mat(0x5a5650, { roughness: 0.9 }), [0, 0.18, 0])); }
export function kadirga() { // g.guncelle(t) kürekler
  const g = G();
  const sh = new THREE.Shape(); sh.moveTo(-2.4, 0.2); sh.quadraticCurveTo(-1.5, -0.25, 0, -0.3); sh.quadraticCurveTo(1.6, -0.25, 2.6, 0.4); sh.lineTo(2.2, 0.45); sh.lineTo(-2.2, 0.45); sh.closePath();
  const geo = new THREE.ExtrudeGeometry(sh, { depth: 0.8, bevelEnabled: true, bevelSize: 0.08, bevelThickness: 0.1 }); geo.translate(0, 0, -0.4);
  g.add(mesh(geo, tahta(15, 0x7a4a2a), [0, 0.3, 0]));
  g.add(kutu(4.2, 0.04, 0.85, tahta(16, 0xa07a4a), [0, 0.76, 0]));
  g.add(silindir(0.05, 0.06, 3.2, tahta(4, 0x5a3a20), [0.2, 2.3, 0]));
  const yel = new THREE.Shape(); yel.moveTo(0, 0); yel.lineTo(1.6, 2.6); yel.lineTo(-1.4, 1.2); yel.closePath();
  g.add(mesh(new THREE.ShapeGeometry(yel), kumas(0xefe3c8, { side: THREE.DoubleSide }), [0.1, 1.2, 0.05]));
  const bf = mesh(new THREE.PlaneGeometry(0.5, 0.3), new THREE.MeshStandardMaterial({ map: bayrakDokusu(), side: THREE.DoubleSide }), [0.45, 3.75, 0]); g.add(bf);
  const kurekler = [];
  for (const s of [-1, 1]) for (let i = 0; i < 9; i++) { const k = G(); k.position.set(-1.6 + i * 0.4, 0.7, s * 0.48); k.add(silindir(0.015, 0.015, 1.6, tahta(2, 0xb08a5a), [0, -0.3, s * 0.65], [s * 1.05, 0, 0])); g.add(k); kurekler.push([k, s]); }
  g.guncelle = t => kurekler.forEach(([k, s]) => { k.rotation.z = Math.sin(t * 3) * 0.35; k.rotation.x = s * Math.cos(t * 3) * 0.12; });
  g.guncelle(0); return g;
}
export function kalkan() { const g = G(); g.add(mesh(new THREE.SphereGeometry(0.3, 32, 12, 0, Math.PI * 2, 0, 0.6), bronz(), [0, 0, 0], [Math.PI / 2, 0, 0]), kure(0.05, altin(), [0, 0, 0.1])); return g; }
export function tufek() { const g = G(); g.add(kutu(0.05, 0.05, 0.6, tahta(3, 0x6a4a2a), [0, 0, -0.1]), silindir(0.012, 0.012, 0.75, mat(0x3a3a3a, { metalness: 0.8 }), [0, 0.02, 0.45], [Math.PI / 2, 0, 0])); return g; }
export function siper() { const g = G(), k = mat(0x8a7a5a, { roughness: 1 }); for (let i = 0; i < 9; i++) g.add(kure(0.25, k, [-1 + i * 0.25, 0.15, 0], [1, 0.6, 0.8])); return g; }
export function duman(n = 14, renk = 0x9a9a9a) { // g.guncelle(t)
  const g = G(), m = []; for (let i = 0; i < n; i++) { const s = kure(0.3, mat(renk, { transparent: true, opacity: 0.35, roughness: 1, depthWrite: false })); s.castShadow = false; g.add(s); m.push(s); }
  g.guncelle = t => m.forEach((s, i) => { const k = ((t * 0.3 + i / n) % 1); s.position.set(Math.sin(i * 7) * 0.4 + k * 0.3, k * 2.2, Math.cos(i * 3) * 0.3); s.scale.setScalar(0.5 + k * 2); s.material.opacity = 0.4 * (1 - k); }); g.guncelle(0); return g;
}
export function ates() { const g = G(), fl = []; for (let i = 0; i < 6; i++) { const s = glowSprite(i % 2 ? 0xff5a10 : 0xffb030, 0.6); g.add(s); fl.push(s); } const L = new THREE.PointLight(0xff6a20, 5, 8, 1.5); L.position.y = 0.5; g.add(L); g.guncelle = t => { fl.forEach((s, i) => { const k = (t * 1.3 + i / 6) % 1; s.position.set(Math.sin(i * 5 + t * 3) * 0.2, k * 1.2, Math.cos(i * 4) * 0.2); s.scale.setScalar(0.8 * (1 - k) + 0.2); }); L.intensity = 5 + Math.sin(t * 20); }; g.guncelle(0); return g; }

// ---------- Cumhuriyet ----------
export function bayrak({ en = 1.5, boy = 1.0, direk = 3.2 } = {}) { // g.guncelle(t): dalgalanır
  const g = G();
  g.add(silindir(0.03, 0.035, direk, mat(0xd8d8d8, { metalness: 0.6, roughness: 0.3 }), [0, direk / 2, 0]), kure(0.05, altin(), [0, direk + 0.03, 0]));
  const geo = new THREE.PlaneGeometry(en, boy, 30, 12); geo.translate(en / 2, 0, 0); const base = geo.attributes.position.array.slice();
  const f = mesh(geo, new THREE.MeshStandardMaterial({ map: bayrakDokusu(), side: THREE.DoubleSide, roughness: 0.75 }), [0.03, direk - boy / 2 - 0.05, 0]); g.add(f);
  g.guncelle = t => { const p = geo.attributes.position; for (let i = 0; i < p.count; i++) { const x = base[i * 3], y = base[i * 3 + 1], u = x / en; p.setZ(i, Math.sin(x * 4 - t * 6 + y * 0.8) * 0.09 * u + Math.sin(x * 9 - t * 9) * 0.02 * u); p.setY(i, y - u * u * 0.06); } p.needsUpdate = true; geo.computeVertexNormals(); };
  g.guncelle(0); return g;
}
export function kursu() { const g = G(), w = tahta(25, 0x5a3a20); g.add(kutu(0.9, 1.1, 0.5, w, [0, 0.55, 0]), kutu(1.0, 0.06, 0.6, w, [0, 1.12, 0]), kutu(0.5, 0.04, 0.35, w, [0, 1.2, 0.05], [-0.3, 0, 0])); const b = bayrakDokusu(); g.add(mesh(new THREE.PlaneGeometry(0.6, 0.4), new THREE.MeshStandardMaterial({ map: b }), [0, 0.65, 0.251])); return g; }
export function masa({ en = 1.8, derin = 0.9, ortu = 0x2e5a3a } = {}) { const g = G(), w = tahta(27, 0x5a3a20); g.add(kutu(en, 0.05, derin, w, [0, 0.75, 0])); if (ortu) g.add(kutu(en + 0.04, 0.3, derin + 0.04, kumas(ortu), [0, 0.62, 0])); for (const a of [-1, 1]) for (const b of [-1, 1]) g.add(kutu(0.06, 0.73, 0.06, w, [a * (en / 2 - 0.08), 0.365, b * (derin / 2 - 0.08)])); return g; }
export function sandalye() { const g = G(), w = tahta(29, 0x5a3420); g.add(kutu(0.45, 0.05, 0.45, w, [0, 0.46, 0]), kutu(0.45, 0.5, 0.04, w, [0, 0.72, -0.21])); for (const a of [-1, 1]) for (const b of [-1, 1]) g.add(kutu(0.04, 0.46, 0.04, w, [a * 0.2, 0.23, b * 0.2])); return g; }
export function haritaMasasi() { const d = kanvas(1024, 640, (x, w, h) => { x.fillStyle = '#e8d8b0'; x.fillRect(0, 0, w, h); x.fillStyle = '#9ac0d8'; x.fillRect(0, 0, w, h * 0.22); x.fillRect(0, h * 0.85, w, h); x.fillStyle = '#d8c090'; x.beginPath(); x.moveTo(w * 0.12, h * 0.35); x.bezierCurveTo(w * 0.3, h * 0.25, w * 0.7, h * 0.28, w * 0.92, h * 0.35); x.lineTo(w * 0.9, h * 0.72); x.bezierCurveTo(w * 0.6, h * 0.8, w * 0.3, h * 0.78, w * 0.1, h * 0.7); x.fill(); x.strokeStyle = '#8a1a1a'; x.lineWidth = 6; x.setLineDash([16, 10]); x.beginPath(); x.moveTo(w * 0.2, h * 0.45); x.bezierCurveTo(w * 0.4, h * 0.6, w * 0.55, h * 0.4, w * 0.75, h * 0.55); x.stroke(); }); const g = masa({ en: 1.6, derin: 1.0, ortu: null }); g.add(mesh(new THREE.PlaneGeometry(1.4, 0.88), new THREE.MeshStandardMaterial({ map: d, roughness: 0.9 }), [0, 0.78, 0], [-Math.PI / 2, 0, 0])); return g; }
export function lozanMasasi() { const g = masa({ en: 4.0, derin: 1.2, ortu: 0x1f4a2a }); for (let i = 0; i < 5; i++) { g.add(mesh(new THREE.PlaneGeometry(0.22, 0.3), mat(0xf4efe0), [-1.6 + i * 0.8, 0.781, 0.2], [-Math.PI / 2, 0, (i - 2) * 0.2])); g.add(hokkaKalem().translateX(-1.4 + i * 0.8).translateY(0.775).translateZ(0.35)); } return g; }
export function radyo() { const g = G(); g.add(kutu(0.4, 0.3, 0.2, tahta(31, 0x6a3a1a), [0, 0.15, 0]), mesh(new THREE.CircleGeometry(0.09, 32), kumas(0xc8b090), [-0.06, 0.16, 0.101]), silindir(0.02, 0.02, 0.02, mat(0xd8c8a0), [0.12, 0.12, 0.11], [Math.PI / 2, 0, 0])); return g; }

// ---------- yapılar ----------
export function cami({ minare = 2 } = {}) {
  const g = G(), t = mat(0xe8e2d4, { roughness: 0.85 }), k = mat(0x6a7a8a, { metalness: 0.4, roughness: 0.5 });
  g.add(kutu(3, 1.6, 3, t, [0, 0.8, 0]), silindir(1.35, 1.45, 0.4, t, [0, 1.8, 0], [0, 0, 0], 48));
  g.add(mesh(new THREE.SphereGeometry(1.35, 48, 24, 0, Math.PI * 2, 0, Math.PI / 2), k, [0, 2.0, 0]), silindir(0.03, 0.03, 0.4, altin(), [0, 3.5, 0]));
  for (const s of [-1, 1]) g.add(mesh(new THREE.SphereGeometry(0.8, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2), k, [s * 1.5, 1.6, 0]));
  for (let i = 0; i < minare; i++) g.add(minareYap(i % 2 ? 1.9 : -1.9, i < 2 ? 1.9 : -1.9));
  for (let i = -2; i <= 2; i++) g.add(mesh(new THREE.PlaneGeometry(0.25, 0.5), mat(0x2a3a5a), [i * 0.55, 0.9, 1.51]));
  return g;
}
function minareYap(x, z) { const g = G(), t = mat(0xe8e2d4, { roughness: 0.85 }); g.position.set(x, 0, z); g.add(silindir(0.18, 0.2, 4.2, t, [0, 2.1, 0], [0, 0, 0], 16), silindir(0.3, 0.26, 0.12, t, [0, 3.4, 0], [0, 0, 0], 16), mesh(new THREE.ConeGeometry(0.2, 0.9, 16), mat(0x6a7a8a, { metalness: 0.4 }), [0, 4.65, 0])); return g; }
export function minare() { return minareYap(0, 0); }
export function ahsapEv(renk = 0xb0602a) { // İstanbul ahşap evi (cumbalı)
  const g = G(), w = tahta(33, renk), b = mat(0xe8dcc8);
  g.add(kutu(2.2, 2.4, 1.8, w, [0, 1.2, 0]), kutu(1.0, 1.2, 0.5, w, [0, 2.0, 1.1]));
  g.add(mesh(new THREE.ConeGeometry(1.75, 0.9, 4), mat(0x9a4a2a), [0, 2.85, 0], [0, Math.PI / 4, 0], [1.25, 1, 1]));
  for (const x of [-0.7, 0.7]) g.add(kutu(0.4, 0.6, 0.02, mat(0x2a2a3a), [x, 1.0, 0.91]), kutu(0.46, 0.66, 0.01, b, [x, 1.0, 0.905]));
  g.add(kutu(0.6, 0.6, 0.02, mat(0x2a2a3a), [0, 2.0, 1.36]), kutu(0.5, 1.0, 0.03, tahta(35, 0x5a3010), [0, 0.5, 0.91]));
  return g;
}
export function kuyu() { const g = G(), t = mat(0x9a948a, { roughness: 0.95 }); g.add(torna([[0.45, 0], [0.45, 0.6], [0.35, 0.6], [0.35, 0.05]], t, [0, 0, 0], [0, 0, 0], 32)); g.add(mesh(new THREE.CircleGeometry(0.35, 32), mat(0x050505), [0, 0.3, 0], [-Math.PI / 2, 0, 0])); for (const s of [-1, 1]) g.add(kutu(0.06, 1.0, 0.06, tahta(2), [s * 0.45, 1.0, 0])); g.add(silindir(0.04, 0.04, 1.0, tahta(3), [0, 1.35, 0], [0, 0, Math.PI / 2])); g.add(silindir(0.005, 0.005, 0.6, kumas(0xc8b090), [0, 1.05, 0])); return g; }
export function mezarTasi({ bas = 'kavuk', yazi = '' } = {}) { // Osmanlı mezar taşı, tepesi kavuk/fes
  const g = G(), t = mat(0xd8d2c4, { roughness: 0.95 });
  const d = kanvas(256, 640, (x, w, h) => { x.fillStyle = '#d8d2c4'; x.fillRect(0, 0, w, h); hatSatirlari(x, w, h, { ust: 0.12, alt: 0.8, satir: 9, renk: '#6a6458', kenar: 0.15 }); if (yazi) { x.fillStyle = '#4a4438'; x.font = 'bold 72px serif'; x.textAlign = 'center'; x.fillText(yazi, w / 2, h * 0.93); } });
  g.add(kutu(0.42, 1.1, 0.12, [t, t, t, t, new THREE.MeshStandardMaterial({ map: d, roughness: 0.95 }), t], [0, 0.55, 0]));
  g.add(silindir(0.08, 0.1, 0.12, t, [0, 1.16, 0]));
  if (bas === 'kavuk') g.add(kure(0.17, t, [0, 1.32, 0], [1, 0.75, 1]), halka(0.16, 0.035, t, [0, 1.25, 0], [Math.PI / 2, 0, 0]));
  else if (bas === 'fes') g.add(silindir(0.11, 0.13, 0.2, t, [0, 1.32, 0]));
  return g;
}
export function serviAgaci() { const g = G(); g.add(silindir(0.06, 0.08, 0.6, tahta(2, 0x4a3020), [0, 0.3, 0]), kure(0.4, mat(0x1f3a24, { roughness: 1 }), [0, 1.8, 0], [0.9, 3.2, 0.9])); return g; }
export function sutun(h = 3) { const g = G(), t = mat(0xe8e2d4, { roughness: 0.7 }); g.add(silindir(0.18, 0.2, h, t, [0, h / 2, 0], [0, 0, 0], 24), kutu(0.5, 0.15, 0.5, t, [0, 0.075, 0]), kutu(0.5, 0.15, 0.5, t, [0, h - 0.075, 0])); return g; }
export function kemer(gen = 2, h = 3) { const g = G(), t = mat(0xe8e2d4, { roughness: 0.75 }), a = mat(0xb03a2a); g.add(sutun(h).translateX(-gen / 2), sutun(h).translateX(gen / 2)); for (let i = 0; i < 12; i++) { const an = Math.PI * i / 11; g.add(kutu(0.28, 0.22, 0.4, i % 2 ? a : t, [Math.cos(an) * gen / 2, h + Math.sin(an) * gen / 2, 0], [0, 0, an + Math.PI / 2])); } return g; }

// ---------- hayvan ----------
export function esek() { // Nasreddin Hoca'nın eşeği; g.guncelle(t) kulak/kuyruk
  const g = G(), m = mat(0x8a8078, { roughness: 0.95 }), k = mat(0x3a3430);
  const cap = (r, l, p, rot) => mesh(new THREE.CapsuleGeometry(r, l, 6, 16), m, p, rot);
  g.add(cap(0.22, 0.6, [0, 0.85, 0], [0, 0, Math.PI / 2]));
  for (const x of [-0.32, 0.32]) for (const z of [-0.12, 0.12]) g.add(cap(0.055, 0.55, [x, 0.38, z]), kure(0.06, k, [x, 0.06, z], [1, 0.6, 1.2]));
  const boyun = cap(0.11, 0.35, [0.5, 1.12, 0], [0, 0, -0.8]); g.add(boyun);
  const bas = G(); bas.position.set(0.72, 1.3, 0); g.add(bas);
  bas.add(cap(0.1, 0.28, [0.12, -0.05, 0], [0, 0, Math.PI / 2 + 0.5]), kure(0.075, mat(0xc8c0b8), [0.3, -0.16, 0], [1, 0.8, 1.1]));
  for (const s of [-1, 1]) bas.add(kure(0.018, mat(0x111111, { roughness: 0.2 }), [0.12, 0.02, s * 0.085]));
  const kulak = [-1, 1].map(s => { const e = G(); e.position.set(-0.02, 0.08, s * 0.06); e.add(cap(0.035, 0.22, [0, 0.13, 0], [0, 0, 0])); bas.add(e); return [e, s]; });
  const kuyruk = G(); kuyruk.position.set(-0.52, 0.95, 0); kuyruk.add(cap(0.02, 0.35, [0, -0.2, 0], [0, 0, 0]), kure(0.04, k, [0, -0.42, 0])); g.add(kuyruk);
  g.add(kutu(0.5, 0.06, 0.5, kumas(0x8a1a24), [0, 1.08, 0]));
  g.guncelle = t => { kulak.forEach(([e, s]) => { e.rotation.x = s * (0.25 + Math.sin(t * 2 + s) * 0.15); }); kuyruk.rotation.z = Math.sin(t * 4) * 0.3; bas.rotation.z = Math.sin(t * 1.3) * 0.06; };
  g.guncelle(0); return g;
}
export function at(renk = 0x5a3a24) { // basit at (padişah alayı, savaş)
  const g = esek(); g.traverse(c => { if (c.isMesh && c.material.color?.getHex() === 0x8a8078) { c.material = mat(renk, { roughness: 0.6 }); } }); g.scale.set(1.25, 1.35, 1.2); return g;
}

// ---------- modern dönem (1900-1938) ----------
export function savasGemisi({ renk = 0x6a7078 } = {}) { // buharlı zırhlı (Mondros/işgal donanması, Vahdettin'in gemisi)
  const g = G(), c = mat(renk, { metalness: 0.5, roughness: 0.5 }), k = mat(0x2a2c30, { metalness: 0.4 });
  const sh = new THREE.Shape(); sh.moveTo(-3.2, 0.5); sh.lineTo(-3.0, 0); sh.lineTo(2.6, 0); sh.quadraticCurveTo(3.3, 0.1, 3.5, 0.6); sh.lineTo(-3.2, 0.6); sh.closePath();
  const geo = new THREE.ExtrudeGeometry(sh, { depth: 1.0, bevelEnabled: true, bevelSize: 0.05, bevelThickness: 0.05 }); geo.translate(0, 0, -0.5);
  g.add(mesh(geo, c, [0, -0.1, 0]), kutu(6.4, 0.04, 1.0, mat(0x9a8a6a), [0.1, 0.52, 0]));
  g.add(kutu(1.6, 0.6, 0.7, c, [0, 0.85, 0]), kutu(0.8, 0.4, 0.5, c, [0.2, 1.35, 0]));
  for (const x of [-0.4, 0.4]) g.add(silindir(0.16, 0.18, 1.1, k, [x, 1.6, 0]), halka(0.17, 0.02, mat(0xd8d8d8), [x, 1.95, 0], [Math.PI / 2, 0, 0]));
  for (const x of [-2.0, 2.2]) { const t = G(); t.position.set(x, 0.65, 0); t.add(silindir(0.32, 0.36, 0.25, c), silindir(0.05, 0.05, 1.0, k, [x > 0 ? 0.55 : -0.55, 0.05, 0.1], [0, 0, Math.PI / 2]), silindir(0.05, 0.05, 1.0, k, [x > 0 ? 0.55 : -0.55, 0.05, -0.1], [0, 0, Math.PI / 2])); g.add(t); }
  g.add(silindir(0.03, 0.04, 2.6, k, [-0.9, 2.0, 0]), silindir(0.03, 0.04, 2.0, k, [1.4, 1.6, 0]));
  return g;
}
export function tren() { // buharlı lokomotif + vagon (Hicaz/Bağdat demiryolu, Cumhuriyet demiryolları)
  const g = G(), s = mat(0x1e1e22, { metalness: 0.6, roughness: 0.4 }), r = mat(0x8a1a1a, { roughness: 0.5 }), a = altin();
  g.add(silindir(0.42, 0.42, 2.4, s, [0, 1.0, 0], [0, 0, Math.PI / 2], 32), kutu(1.0, 1.2, 1.1, s, [-1.5, 1.3, 0]), kutu(1.1, 0.12, 1.2, r, [-1.5, 1.95, 0]));
  g.add(silindir(0.14, 0.2, 0.7, s, [0.9, 1.7, 0]), kure(0.16, a, [0.2, 1.45, 0]), mesh(new THREE.ConeGeometry(0.45, 0.5, 4), s, [1.45, 0.45, 0], [0, 0, -Math.PI / 2], [1, 1, 1.4]));
  for (const x of [-1.6, -0.8, 0.0, 0.8]) for (const z of [-0.5, 0.5]) g.add(silindir(x < -1 ? 0.3 : 0.38, x < -1 ? 0.3 : 0.38, 0.08, r, [x, x < -1 ? 0.3 : 0.38, z], [Math.PI / 2, 0, 0]));
  g.add(kutu(3.6, 0.15, 1.1, s, [-0.4, 0.55, 0]));
  const v = G(); v.position.x = -4.2; g.add(v);
  v.add(kutu(3.0, 1.3, 1.2, mat(0x2a4a2a), [0, 1.25, 0]), mesh(new THREE.CylinderGeometry(0.7, 0.7, 3.1, 24, 1, false, 0, Math.PI), mat(0x3a3a3a), [0, 1.9, 0], [0, 0, Math.PI / 2], [1, 1, 0.9]));
  for (let i = 0; i < 5; i++) v.add(kutu(0.35, 0.4, 0.02, mat(0xe8d8a0, { emissive: 0x3a2a00 }), [-1.1 + i * 0.55, 1.45, 0.61]));
  for (const x of [-1.0, 1.0]) for (const z of [-0.5, 0.5]) v.add(silindir(0.3, 0.3, 0.08, s, [x, 0.3, z], [Math.PI / 2, 0, 0]));
  const d = P_duman(); d.position.set(0.9, 2.0, 0); g.add(d); g.guncelle = t => d.guncelle(t);
  return g;
}
function P_duman() { return duman(10, 0x5a5a5a); }
export function otomobil(renk = 0x1a1a1e) { // 1930'lar otomobili
  const g = G(), c = mat(renk, { metalness: 0.7, roughness: 0.25 }), k = mat(0x111111, { roughness: 0.6 }), kr = gumus();
  g.add(kutu(2.2, 0.35, 0.95, c, [0, 0.55, 0]), kutu(1.1, 0.5, 0.9, c, [-0.35, 0.95, 0]), kutu(0.9, 0.35, 0.7, c, [0.75, 0.75, 0]));
  for (const z of [-0.47, 0.47]) g.add(kutu(1.0, 0.3, 0.02, mat(0x8ab0c8, { roughness: 0.1, metalness: 0.3 }), [-0.35, 1.0, z]));
  for (const x of [-0.75, 0.75]) for (const z of [-0.5, 0.5]) { g.add(silindir(0.3, 0.3, 0.18, k, [x, 0.3, z], [Math.PI / 2, 0, 0])); g.add(silindir(0.15, 0.15, 0.19, kr, [x, 0.3, z], [Math.PI / 2, 0, 0])); g.add(mesh(new THREE.SphereGeometry(0.34, 20, 10, 0, Math.PI * 2, 0, Math.PI / 2), c, [x, 0.33, z], [0, 0, 0], [1.1, 0.7, 0.6])); }
  for (const z of [-0.3, 0.3]) g.add(kure(0.09, kr, [1.22, 0.75, z]), kure(0.06, parlak(0xfff6d0), [1.28, 0.75, z]));
  g.add(kutu(0.05, 0.35, 0.5, kr, [1.2, 0.6, 0]));
  return g;
}
export function ucak() { // çift kanatlı (1910-30'lar), g.guncelle(t) pervane
  const g = G(), c = mat(0x7a7a5a, { roughness: 0.6 }), w = kumas(0xd8ccaa);
  g.add(mesh(new THREE.CapsuleGeometry(0.22, 2.2, 8, 16), c, [0, 1.0, 0], [0, 0, Math.PI / 2]));
  for (const y of [0.8, 1.55]) g.add(kutu(0.6, 0.05, 4.0, w, [0.35, y, 0]));
  for (const z of [-1.4, 1.4]) for (const x of [0.15, 0.55]) g.add(silindir(0.015, 0.015, 0.75, mat(0x3a3a3a), [x, 1.18, z]));
  g.add(kutu(0.5, 0.04, 1.4, w, [-1.3, 1.05, 0]), kutu(0.45, 0.5, 0.04, w, [-1.35, 1.3, 0]));
  for (const z of [-0.45, 0.45]) g.add(silindir(0.18, 0.18, 0.06, mat(0x111111), [0.4, 0.2, z], [Math.PI / 2, 0, 0]), silindir(0.015, 0.015, 0.75, mat(0x3a3a3a), [0.4, 0.55, z * 0.6], [z > 0 ? 0.5 : -0.5, 0, 0]));
  const pv = G(); pv.position.set(1.38, 1.0, 0); pv.add(kutu(0.03, 1.1, 0.08, tahta(2, 0x6a4a2a)), kure(0.08, gumus())); g.add(pv);
  const tb = bayrakDokusu(); g.add(mesh(new THREE.PlaneGeometry(0.4, 0.27), new THREE.MeshStandardMaterial({ map: tb, side: THREE.DoubleSide }), [-1.35, 1.35, 0.025]));
  g.guncelle = t => { pv.rotation.x = t * 40; }; g.guncelle(0.3); return g;
}
export function mikrofon() { const g = G(), k = mat(0x2a2a2e, { metalness: 0.7, roughness: 0.3 }); g.add(silindir(0.15, 0.18, 0.04, k, [0, 0.02, 0]), silindir(0.012, 0.012, 1.4, gumus(), [0, 0.72, 0]), halka(0.1, 0.012, gumus(), [0, 1.48, 0]), kutu(0.1, 0.13, 0.05, k, [0, 1.48, 0])); return g; }
export function patlamisMisir() { // kâse dolusu patlamış mısır
  const g = G(); g.add(torna([[0, 0], [0.18, 0.01], [0.24, 0.16], [0.25, 0.17]], kumas(0xc42a2a, { side: THREE.DoubleSide })));
  const m = mat(0xfff4d0, { roughness: 0.9 }), y = mat(0xf0c050, { roughness: 0.7 });
  for (let i = 0; i < 70; i++) { const a = i * 2.39, r = 0.2 * Math.sqrt((i % 35) / 35), h = 0.1 + Math.floor(i / 35) * 0.05 + (i % 5) * 0.012; g.add(kure(0.03 + (i % 3) * 0.006, i % 9 ? m : y, [Math.cos(a) * r, h, Math.sin(a) * r], [1, 0.8, 1.1], 10)); }
  return g;
}
export const PROPLAR = { taht, tabut, kemend, yatagan, kilic, kafes, dolap, sandik, minder, sedir, ferman, kitap, muhur, tugraLevha, hokkaKalem, zehirSisesi, serbetKadehi, fincan, cezve, tepsi, nargile, tabure, tavla, mangal, mesale, samdan, kandil, top, gulle, kadirga, kalkan, tufek, siper, duman, ates, bayrak, kursu, masa, sandalye, haritaMasasi, lozanMasasi, radyo, cami, minare, ahsapEv, kuyu, mezarTasi, serviAgaci, sutun, kemer, esek, at, savasGemisi, tren, otomobil, ucak, mikrofon, patlamisMisir };
