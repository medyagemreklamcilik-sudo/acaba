// Ortak yardımcılar: malzeme, temel geometri, kanvas dokuları
import * as THREE from 'three';
import { fabricTexture, woodTexture, rng } from '../textures.js';

let _fab;
export const fab = () => (_fab = _fab || fabricTexture());
export const kumas = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.88, bumpMap: fab(), bumpScale: 1.1, ...o });
export const mat = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.6, ...o });
export const altin = () => mat(0xe3b23c, { metalness: 0.9, roughness: 0.3 });
export const gumus = () => mat(0xc9ccd2, { metalness: 1, roughness: 0.25 });
export const bronz = () => mat(0xb07a3a, { metalness: 0.9, roughness: 0.38 });
export const tahta = (seed = 7, color = 0xffffff) => new THREE.MeshStandardMaterial({ map: woodTexture(seed), color, roughness: 0.75 });
export const parlak = (color) => new THREE.MeshBasicMaterial({ color, toneMapped: false });

export function mesh(geo, m, p = [0, 0, 0], r = [0, 0, 0], s = null) {
  const o = new THREE.Mesh(geo, m); o.position.set(...p); o.rotation.set(...r);
  if (s) o.scale.set(...s);
  o.castShadow = true; o.receiveShadow = true; return o;
}
export const kutu = (w, h, d, m, p, r) => mesh(new THREE.BoxGeometry(w, h, d), m, p, r);
export const kure = (rad, m, p, s, seg = 32) => mesh(new THREE.SphereGeometry(rad, seg, Math.max(8, seg / 2)), m, p, [0, 0, 0], s);
export const silindir = (r0, r1, h, m, p, r, seg = 32, open = false) => mesh(new THREE.CylinderGeometry(r0, r1, h, seg, 1, open), m, p, r);
export const halka = (R, tube, m, p, r, arc = Math.PI * 2) => mesh(new THREE.TorusGeometry(R, tube, 12, 48, arc), m, p, r);
export function torna(profile, m, p, r, seg = 48, phiStart = 0, phiLen = Math.PI * 2) { // profile: [[r,y],...]
  return mesh(new THREE.LatheGeometry(profile.map(([x, y]) => new THREE.Vector2(x, y)), seg, phiStart, phiLen), m, p, r);
}
export function golgesiz(o) { o.traverse(c => { if (c.isMesh) c.castShadow = false; }); return o; }
export function grup(...ch) { const g = new THREE.Group(); ch.forEach(c => c && g.add(c)); return g; }

// ---- kanvas dokuları ----
export function kanvas(w, h, ciz) {
  const c = document.createElement('canvas'); c.width = w; c.height = h; const x = c.getContext('2d'); ciz(x, w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t;
}
// sahte hat yazısı satırları (ferman, kitap sayfası)
export function hatSatirlari(x, w, h, { ust = 0.12, alt = 0.92, satir = 11, renk = '#2a1a10', seed = 3, kenar = 0.1 } = {}) {
  const R = rng(seed); x.strokeStyle = renk; x.lineCap = 'round';
  for (let i = 0; i < satir; i++) {
    const y = h * (ust + (alt - ust) * i / Math.max(1, satir - 1));
    let px = w * (1 - kenar); x.lineWidth = w * 0.006;
    while (px > w * kenar) {
      const L = w * (0.03 + R() * 0.07);
      x.beginPath(); x.moveTo(px, y);
      x.bezierCurveTo(px - L * 0.3, y - h * 0.02 * R(), px - L * 0.6, y + h * 0.015, px - L, y - h * 0.01 * R());
      x.stroke();
      if (R() > 0.6) { x.beginPath(); x.arc(px - L * 0.5, y - h * 0.025, w * 0.004, 0, 7); x.fillStyle = renk; x.fill(); }
      if (R() > 0.75) { x.beginPath(); x.moveTo(px - L * 0.2, y); x.lineTo(px - L * 0.25, y - h * 0.05); x.stroke(); }
      px -= L + w * 0.015;
    }
  }
}
export function tugraCiz(x, cx, cy, s, renk = '#1b2a6b') { // stilize tuğra
  x.strokeStyle = renk; x.lineWidth = s * 0.035; x.lineCap = 'round';
  for (let i = 0; i < 3; i++) { x.beginPath(); x.moveTo(cx - s * 0.1 + i * s * 0.12, cy + s * 0.25); x.lineTo(cx - s * 0.1 + i * s * 0.12, cy - s * 0.55); x.stroke(); }
  x.beginPath(); x.ellipse(cx - s * 0.35, cy + s * 0.15, s * 0.42, s * 0.22, 0, 0, 7); x.stroke();
  x.beginPath(); x.ellipse(cx - s * 0.35, cy + s * 0.15, s * 0.28, s * 0.13, 0, 0, 7); x.stroke();
  x.beginPath(); x.moveTo(cx + s * 0.25, cy + s * 0.2); x.bezierCurveTo(cx + s * 0.6, cy + s * 0.1, cx + s * 0.7, cy - s * 0.1, cx + s * 0.9, cy - s * 0.05); x.stroke();
  x.beginPath(); x.moveTo(cx - s * 0.1, cy + s * 0.3); x.bezierCurveTo(cx, cy + s * 0.45, cx + s * 0.3, cy + s * 0.4, cx + s * 0.5, cy + s * 0.32); x.stroke();
}
export function bayrakDokusu() {
  return kanvas(768, 512, (x, w, h) => {
    x.fillStyle = '#e30a17'; x.fillRect(0, 0, w, h);
    const G = h, cx = 0.5 * G, cy = h / 2;
    x.fillStyle = '#fff'; x.beginPath(); x.arc(cx, cy, 0.25 * G, 0, 7); x.fill();
    x.fillStyle = '#e30a17'; x.beginPath(); x.arc(cx + 0.0625 * G, cy, 0.2 * G, 0, 7); x.fill();
    const sx = cx + 0.333 * G, r = 0.125 * G; x.fillStyle = '#fff'; x.beginPath();
    for (let i = 0; i < 10; i++) { const a = Math.PI + i * Math.PI / 5, rr = i % 2 ? r * 0.382 : r; x.lineTo(sx + Math.cos(a) * rr, cy + Math.sin(a) * rr); }
    x.closePath(); x.fill();
  });
}
