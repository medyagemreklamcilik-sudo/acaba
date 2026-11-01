// Mekânlar: makeStage() ile kurulan sahneyi giydirir. Hepsi { guncelle(t) } döner.
//   const scene = makeStage(); const m = sarayIc(scene, { gece: true }); ... m.guncelle(t)
import * as THREE from 'three';
import { glowSprite } from '../props.js';
import { kumas, mat, altin, tahta, parlak, mesh, kutu, kure, silindir, halka, kanvas } from './ortak.js';
import * as P from './proplar.js';

function gok(scene, [top, mid, hor, zemin], { env = 1, gunes = 2.3, gunesRenk = 0xfff3e6, hemi = [0xcfe4ff, 0x7f93ad, 0.75] } = {}) {
  const u = scene.userData.sky.material.uniforms; u.top.value.set(top); u.mid.value.set(mid); u.horizon.value.set(hor); u.floorC.value.set(zemin);
  scene.environmentIntensity = env; scene.userData.key.color.set(gunesRenk); scene.userData.key.intensity = gunes;
  scene.children.filter(c => c.isHemisphereLight).forEach(h => { h.color.set(hemi[0]); h.groundColor.set(hemi[1]); h.intensity = hemi[2]; });
}
const GECE = [0x05081a, 0x0b1233, 0x1b2350, 0x0b0d1c], GUNDUZ = [0x2b78d6, 0x5b9fea, 0x92c3f2, 0xa9cdf1], AKSAM = [0x1a2a5a, 0x8a5a7a, 0xf0a060, 0x3a2a2a];
const zemin = (scene, renk, y = 0.001) => scene.add(mesh(new THREE.PlaneGeometry(40, 40), mat(renk, { roughness: 0.95 }), [0, y, 0], [-Math.PI / 2, 0, 0]));
function guncelleyici(list) { return { guncelle: t => list.forEach((o, i) => o.guncelle && o.guncelle(t + i * 0.7)) }; }

export function sarayIc(scene, { gece = true } = {}) {
  gok(scene, gece ? GECE : GUNDUZ, gece ? { env: 0.35, gunes: 0.9, gunesRenk: 0x9db4ff, hemi: [0x5a6aa8, 0x2a1a22, 0.5] } : { env: 0.8, gunes: 1.6 });
  zemin(scene, 0x2a1520);
  scene.add(mesh(new THREE.PlaneGeometry(1.5, 14), kumas(0x8e1f2c), [0, 0.004, 3], [-Math.PI / 2, 0, 0]));
  for (const s of [-1, 1]) scene.add(mesh(new THREE.PlaneGeometry(0.06, 14), altin(), [s * 0.7, 0.006, 3], [-Math.PI / 2, 0, 0]));
  const cini = kanvas(256, 256, (x, w, h) => { x.fillStyle = '#16204a'; x.fillRect(0, 0, w, h); x.fillStyle = '#2a4a9a'; x.beginPath(); x.moveTo(w / 2, 10); x.lineTo(w - 10, h / 2); x.lineTo(w / 2, h - 10); x.lineTo(10, h / 2); x.fill(); x.fillStyle = '#c8d8f0'; x.beginPath(); x.arc(w / 2, h / 2, 28, 0, 7); x.fill(); x.fillStyle = '#b03030'; x.beginPath(); x.arc(w / 2, h / 2, 12, 0, 7); x.fill(); });
  cini.wrapS = cini.wrapT = THREE.RepeatWrapping; cini.repeat.set(30, 12);
  scene.add(mesh(new THREE.PlaneGeometry(30, 12), new THREE.MeshStandardMaterial({ map: cini, roughness: 0.6 }), [0, 6, -3.2]));
  const win = new THREE.MeshBasicMaterial({ color: gece ? 0x22306a : 0x9ac8f0 });
  for (const x of [-1.9, 1.9]) {
    scene.add(mesh(new THREE.PlaneGeometry(1.0, 2.0), win, [x, 2.4, -3.17]), mesh(new THREE.CircleGeometry(0.5, 32, 0, Math.PI), win, [x, 3.4, -3.17]));
    for (const s of [-1, 1]) scene.add(kutu(0.08, 2.1, 0.06, altin(), [x + s * 0.54, 2.4, -3.15]));
    scene.add(halka(0.54, 0.04, altin(), [x, 3.4, -3.15], [0, 0, 0], Math.PI));
  }
  if (gece) { scene.add(mesh(new THREE.CircleGeometry(0.22, 32), parlak(0xfff4c8), [1.95, 3.25, -3.12]), mesh(new THREE.CircleGeometry(0.19, 32), win, [2.06, 3.31, -3.11])); const g = glowSprite(0xfff0c0, 1.1); g.position.set(1.95, 3.25, -3.0); g.material.opacity = 0.35; scene.add(g); }
  const m1 = P.mesale(); m1.position.set(-1.25, 1.35, -3.0); const m2 = P.mesale(); m2.position.set(1.25, 1.35, -3.0); scene.add(m1, m2);
  return guncelleyici([m1, m2]);
}
export function divan(scene) { // Divan-ı Hümayun: sedirler, kubbe altı
  const m = sarayIc(scene, { gece: false });
  const s1 = P.sedir(3.2); s1.position.set(0, 0, -2.6); const s2 = P.sedir(2.4); s2.position.set(-2.2, 0, -1.0); s2.rotation.y = Math.PI / 2; const s3 = P.sedir(2.4); s3.position.set(2.2, 0, -1.0); s3.rotation.y = -Math.PI / 2;
  const k = P.kafes(); k.position.set(0, 1.9, -3.1); k.scale.setScalar(0.6); scene.add(s1, s2, s3, k);
  return m;
}
export function kahvehane(scene) {
  gok(scene, AKSAM, { env: 0.45, gunes: 0.8, gunesRenk: 0xffc890, hemi: [0xffd0a0, 0x3a2a1a, 0.55] });
  zemin(scene, 0x4a3420);
  const duvar = tahta(37, 0x8a6040);
  scene.add(kutu(12, 4, 0.1, duvar, [0, 2, -3]), kutu(0.1, 4, 8, duvar, [-3.2, 2, 0]), kutu(0.1, 4, 8, duvar, [3.2, 2, 0]));
  for (let i = -5; i <= 5; i++) scene.add(kutu(0.12, 0.12, 8, tahta(39, 0x5a3a20), [i * 0.6, 3.8, 0]));
  const p1 = P.sedir(3.0, 0x6a2a1a); p1.position.set(0, 0, -2.5); const p2 = P.sedir(3.0, 0x6a2a1a); p2.position.set(-2.8, 0, 0); p2.rotation.y = Math.PI / 2;
  const mg = P.mangal(); mg.position.set(1.8, 0, -1.6); const kd = P.kandil(); kd.position.set(0, 2.6, 0); const kd2 = P.kandil(); kd2.position.set(-1.5, 2.6, -1.5);
  const t1 = P.tabure(); t1.position.set(0.3, 0, -1.2); const tv = P.tavla(); tv.position.set(0.3, 0.37, -1.2);
  const tp = P.tepsi(); tp.position.set(-1.0, 0.47, -2.4); const f1 = P.fincan(); f1.position.set(-1.05, 0.5, -2.35); const cz = P.cezve(); cz.position.set(1.8, 0.33, -1.6);
  scene.add(p1, p2, mg, kd, kd2, t1, tv, tp, f1, cz);
  return guncelleyici([mg]);
}
export function sokak(scene, { gece = false } = {}) { // İstanbul sokağı: ahşap evler, minare
  gok(scene, gece ? GECE : GUNDUZ, gece ? { env: 0.3, gunes: 0.6, gunesRenk: 0x9db4ff } : {});
  zemin(scene, 0x7a7266);
  const ta = kanvas(256, 256, (x, w, h) => { x.fillStyle = '#7a7266'; x.fillRect(0, 0, w, h); x.strokeStyle = '#5a5248'; x.lineWidth = 4; for (let i = 0; i < 8; i++) for (let j = 0; j < 8; j++) { x.beginPath(); x.ellipse(i * 32 + (j % 2) * 16 + 16, j * 32 + 16, 14, 12, 0, 0, 7); x.stroke(); } });
  ta.wrapS = ta.wrapT = THREE.RepeatWrapping; ta.repeat.set(12, 40);
  scene.add(mesh(new THREE.PlaneGeometry(4, 40), new THREE.MeshStandardMaterial({ map: ta, roughness: 1 }), [0, 0.003, 0], [-Math.PI / 2, 0, 0]));
  const renk = [0xb0602a, 0x8a4a3a, 0xc8a070, 0x6a5a8a, 0x9a6a3a];
  for (let i = 0; i < 6; i++) for (const s of [-1, 1]) { const e = P.ahsapEv(renk[(i * 2 + (s > 0)) % 5]); e.position.set(s * 3.1, 0, -i * 2.4 + 2); e.rotation.y = -s * Math.PI / 2; scene.add(e); }
  const mn = P.minare(); mn.position.set(1.5, 0, -16); mn.scale.setScalar(2.2); scene.add(mn);
  return { guncelle() {} };
}
export function meclis(scene) { // 1920 Birinci Meclis: sıralar, kürsü, bayrak
  gok(scene, GUNDUZ, { env: 0.7, gunes: 1.4, hemi: [0xf0e8d8, 0x5a4a3a, 0.7] });
  zemin(scene, 0x6a4a30);
  scene.add(kutu(12, 5, 0.1, mat(0xe8dcc0), [0, 2.5, -3.2]), kutu(12, 0.8, 0.12, tahta(41, 0x5a3a20), [0, 0.4, -3.15]));
  const k = P.kursu(); k.position.set(0, 0, -2.2); scene.add(k);
  const b = P.bayrak({ direk: 3.6 }); b.position.set(-1.6, 0, -2.8); scene.add(b);
  const levha = mesh(new THREE.PlaneGeometry(2.4, 0.45), new THREE.MeshStandardMaterial({ map: kanvas(1024, 192, (x, w, h) => { x.fillStyle = '#1f4a2a'; x.fillRect(0, 0, w, h); x.fillStyle = '#e8c060'; x.font = 'bold 96px serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText('HÂKİMİYET MİLLETİNDİR', w / 2, h / 2); }) }), [0, 3.5, -3.14]); scene.add(levha);
  for (let r = 0; r < 4; r++) for (const s of [-1, 1]) { const sira = kutu(2.2, 0.08, 0.5, tahta(43, 0x5a3420), [s * 1.6, 0.75, r * 1.0 + 0.2]); const arka = kutu(2.2, 0.5, 0.05, tahta(43, 0x5a3420), [s * 1.6, 0.55, r * 1.0 + 0.45]); scene.add(sira, arka); }
  return guncelleyici([b]);
}
export function hamam(scene) {
  gok(scene, [0x3a4048, 0x5a6068, 0x7a8088, 0x3a3a3a], { env: 0.6, gunes: 0.5, hemi: [0xe8f0f8, 0x6a6a6a, 0.9] });
  const mermer = mat(0xe8e4dc, { roughness: 0.25 });
  zemin(scene, 0xd8d4cc);
  scene.add(silindir(1.6, 1.6, 0.5, mermer, [0, 0.25, -0.5], [0, 0, 0], 8)); // göbek taşı
  scene.add(kutu(12, 5, 0.1, mermer, [0, 2.5, -3.5]));
  for (let i = 0; i < 9; i++) { const yildiz = glowSprite(0xffffff, 0.4); yildiz.position.set(-2 + (i % 3) * 2, 4.2, -2.5 + Math.floor(i / 3) * 1.5); scene.add(yildiz); }
  const L = new THREE.PointLight(0xffffff, 6, 10, 1.2); L.position.set(0, 4, -1); scene.add(L);
  const buhar = P.duman(16, 0xffffff); buhar.position.set(0, 0.5, -0.5); scene.add(buhar);
  for (const s of [-1, 1]) { const kurna = silindir(0.25, 0.2, 0.3, mermer, [s * 2.2, 0.7, -3.2], [0, 0, 0], 24); scene.add(kurna); }
  return guncelleyici([buhar]);
}
export function mezarlik(scene, { aksam = true } = {}) {
  gok(scene, aksam ? AKSAM : GUNDUZ, aksam ? { env: 0.5, gunes: 1.0, gunesRenk: 0xffb070 } : {});
  zemin(scene, 0x4a5a34);
  for (let i = 0; i < 14; i++) { const t = P.mezarTasi({ bas: i % 3 ? 'kavuk' : 'fes' }); t.position.set((i % 5 - 2) * 1.0 + Math.sin(i) * 0.2, 0, -Math.floor(i / 5) * 1.3); t.rotation.set(Math.sin(i * 3) * 0.06, Math.sin(i * 7) * 0.2, Math.sin(i * 5) * 0.08); scene.add(t); }
  for (let i = 0; i < 6; i++) { const s = P.serviAgaci(); s.position.set((i % 2 ? 1 : -1) * (2.8 + i * 0.3), 0, -i * 1.2); s.scale.setScalar(1.3); scene.add(s); }
  return { guncelle() {} };
}
export function cephe(scene) { // Çanakkale / Kurtuluş Savaşı cephesi
  gok(scene, [0x5a6a7a, 0x8a8a8a, 0xb0a890, 0x6a5a40], { env: 0.6, gunes: 1.2, gunesRenk: 0xffe0b0 });
  zemin(scene, 0x7a6a4a);
  const s1 = P.siper(); s1.position.set(0, 0, 0.5); const s2 = P.siper(); s2.position.set(1.8, 0, -1.5);
  const d1 = P.duman(14); d1.position.set(-2, 0, -4); const d2 = P.duman(14, 0x6a6a6a); d2.position.set(2.5, 0, -6);
  const a1 = P.ates(); a1.position.set(-2, 0, -4);
  const b = P.bayrak({ direk: 2.4, en: 0.9, boy: 0.6 }); b.position.set(-0.6, 0, -0.3);
  scene.add(s1, s2, d1, d2, a1, b);
  return guncelleyici([d1, d2, a1, b]);
}
export function deniz(scene, { gece = false } = {}) { // kadırga/İngiliz gemisi için deniz
  gok(scene, gece ? GECE : GUNDUZ, gece ? { env: 0.3, gunes: 0.6, gunesRenk: 0x9db4ff } : {});
  const geo = new THREE.PlaneGeometry(60, 60, 80, 80); geo.rotateX(-Math.PI / 2); const base = geo.attributes.position.array.slice();
  const su = mesh(geo, mat(0x1a5a8a, { roughness: 0.25, metalness: 0.1 })); scene.add(su);
  return { guncelle(t) { const p = geo.attributes.position; for (let i = 0; i < p.count; i++) { const x = base[i * 3], z = base[i * 3 + 2]; p.setY(i, Math.sin(x * 0.8 + t * 1.5) * 0.08 + Math.sin(z * 1.1 + t * 1.2) * 0.06); } p.needsUpdate = true; geo.computeVertexNormals(); } };
}
export function acikAlan(scene, { renk = 0x6a7a4a } = {}) { gok(scene, GUNDUZ); zemin(scene, renk); return { guncelle() {} }; }
export const MEKANLAR = { sarayIc, divan, kahvehane, sokak, meclis, hamam, mezarlik, cephe, deniz, acikAlan };
