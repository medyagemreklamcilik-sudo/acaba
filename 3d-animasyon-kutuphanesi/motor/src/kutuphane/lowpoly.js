// Low-poly "craft" karakter (köşeli yüzeyler, düz gölgeleme). Birim: kafa yarıçapı = 1.
//   const a = lowPolyAdam({ ... }); scene.add(a.root); a.ifade({ kizgin: 1 }) ;  lowPolyOda(scene)
import * as THREE from 'three';
import { glowSprite } from '../props.js';

const F = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.78, metalness: 0, flatShading: true, ...o });
const M = (geo, mat, p = [0, 0, 0], r = [0, 0, 0], s = [1, 1, 1]) => { const m = new THREE.Mesh(geo, mat); m.position.set(...p); m.rotation.set(...r); m.scale.set(...s); m.castShadow = m.receiveShadow = true; return m; };
const sm = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
function ekstr(pts, depth, mat, bevel = 0) { const s = new THREE.Shape(); s.moveTo(...pts[0]); pts.slice(1).forEach(p => s.lineTo(...p)); s.closePath(); const g = new THREE.ExtrudeGeometry(s, { depth, bevelEnabled: bevel > 0, bevelSize: bevel, bevelThickness: bevel, bevelSegments: 1 }); g.translate(0, 0, -depth / 2); return new THREE.Mesh(g, mat); }
function titret(geo, amt, seed = 1) { // yüzeylere hafif düzensizlik: daha "el yapımı" kırık yüzler
  const p = geo.attributes.position, seen = new Map();
  for (let i = 0; i < p.count; i++) { const k = `${p.getX(i).toFixed(3)},${p.getY(i).toFixed(3)},${p.getZ(i).toFixed(3)}`; let d = seen.get(k); if (!d) { const h = Math.sin(i * 12.9898 + seed * 78.233) * 43758.5453; d = [(h % 1) * amt, ((h * 7) % 1) * amt, ((h * 13) % 1) * amt]; seen.set(k, d); } p.setXYZ(i, p.getX(i) + d[0], p.getY(i) + d[1], p.getZ(i) + d[2]); }
  geo.computeVertexNormals(); return geo;
}

export function lowPolyAdam({ ten = 0xe0915a, sac = 0x1c1510, ceket = 0x1d2230, gomlek = 0xf1ede4, kravat = 0x16161c, mendil = 0xf4f0e6, bas = null } = {}) {
  const root = new THREE.Group(), head = new THREE.Group(); root.add(head);
  const deri = F(ten), sacM = F(sac, { roughness: 0.85 }), koyu = F(0x2a1810);
  // ---- kafa: düşük çözünürlüklü küre + yüz biçimi ----
  const hg = new THREE.SphereGeometry(1, 14, 12), p = hg.attributes.position;
  for (let i = 0; i < p.count; i++) {
    let x = p.getX(i), y = p.getY(i), z = p.getZ(i);
    x *= 0.84; y *= 1.18; z *= 0.98;
    const alt = sm(-0.15, -1.1, y);                       // çene: aşağı doğru daralır, köşeli
    x *= 1 - 0.12 * alt - 0.22 * sm(-0.75, -1.2, y);   // köşeli çene
    if (z > 0) z *= 1 - 0.1 * alt;
    if (y < -0.9) y = -0.9 - (y + 0.9) * 0.35;            // düz çene altı
    if (z > 0.3 && y > 0.18 && y < 0.5) z += 0.07;        // kaş kemeri
    if (z > 0.3 && Math.abs(y) < 0.18 && Math.abs(x) > 0.55) x *= 1.04; // elmacık
    if (y > 0.75) y = 0.75 + (y - 0.75) * 0.7;            // düz tepe
    p.setXYZ(i, x, y, z);
  }
  titret(hg, 0.025, 3); head.add(M(hg, deri));
  // kulaklar
  for (const s of [-1, 1]) head.add(M(new THREE.IcosahedronGeometry(0.2, 0), deri, [s * 0.83, 0.02, -0.05], [0, s * 0.4, 0], [0.45, 1.25, 0.9]));
  // burun: dört yüzlü sırt + kanatlar
  head.add(M(new THREE.ConeGeometry(0.15, 0.62, 4), deri, [0, 0.0, 0.98], [-0.32, Math.PI / 4, 0], [1, 1, 1.25]));
  head.add(M(new THREE.IcosahedronGeometry(0.13, 0), deri, [0, -0.27, 1.02], [0, 0, 0], [1.5, 0.75, 0.9]));
  for (const s of [-1, 1]) head.add(M(new THREE.IcosahedronGeometry(0.08, 0), deri, [s * 0.14, -0.27, 0.95], [0, 0, 0], [1, 0.8, 0.8]));
  // gözler
  const goz = [], kapak = [], kas = [];
  for (const s of [-1, 1]) {
    const g = new THREE.Group(); g.position.set(s * 0.31, 0.12, 0.86); g.rotation.y = s * 0.26; g.scale.setScalar(1.2); head.add(g);
    const ak = M(new THREE.SphereGeometry(0.17, 10, 6), F(0xf6f2ea, { roughness: 0.3 }), [0, 0, 0], [0, 0, 0], [1.25, 0.72, 0.55]); g.add(ak);
    const iris = M(new THREE.CircleGeometry(0.088, 10), F(0x6a4320, { roughness: 0.3 }), [0, -0.005, 0.094]); g.add(iris);
    iris.add(M(new THREE.CircleGeometry(0.046, 8), F(0x0e0a08), [0, 0, 0.002]));
    iris.add(M(new THREE.CircleGeometry(0.018, 6), new THREE.MeshBasicMaterial({ color: 0xffffff }), [-0.03, 0.03, 0.004]));
    const kp = M(new THREE.SphereGeometry(0.185, 10, 5, 0, Math.PI * 2, 0, Math.PI / 2), deri, [0, 0, 0], [0, 0, 0], [1.27, 0.78, 0.62]); g.add(kp);
    const kp2 = M(new THREE.SphereGeometry(0.18, 10, 4, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), deri, [0, 0, 0], [0, 0, 0], [1.26, 0.74, 0.6]); g.add(kp2);
    // göz çizgisi (üst kapak kenarı)
    const cizgi = M(new THREE.TorusGeometry(0.2, 0.018, 4, 10, Math.PI), koyu, [0, 0.0, 0.02], [0, 0, 0], [1.08, 0.62, 0.6]); g.add(cizgi);
    // kalın köşeli kaş
    const k = ekstr([[-0.34, -0.03], [0.3, 0.04], [0.36, 0.17], [-0.3, 0.13]], 0.14, sacM); k.position.set(s * 0.35, 0.36, 0.93); k.rotation.y = s * 0.3; head.add(k);
    goz.push({ g, iris, s }); kapak.push({ kp, kp2, cizgi, s }); kas.push({ k, s });
  }
  // bıyık (iki parçalı, köşeli)
  const biyik = new THREE.Group(); biyik.position.set(0, -0.43, 0.98); biyik.scale.setScalar(1.15); head.add(biyik);
  for (const s of [-1, 1]) { const b = ekstr([[0.02, 0.1], [0.36, 0.06], [0.48, -0.12], [0.4, -0.2], [0.18, -0.06], [0.02, -0.04]], 0.16, sacM); b.scale.x = s; b.rotation.y = s * 0.35; biyik.add(b); }
  // ağız
  const agiz = new THREE.Group(); agiz.position.set(0, -0.66, 0.9); head.add(agiz);
  const dudak = M(new THREE.BoxGeometry(0.42, 0.05, 0.08), F(0x9a5a3a), [0, 0, 0]); agiz.add(dudak);
  const ic = M(new THREE.SphereGeometry(0.2, 8, 5), F(0x3a0e0e), [0, -0.02, 0.0], [0, 0, 0], [1.3, 0.1, 0.25]); agiz.add(ic);
  const dis = M(new THREE.BoxGeometry(0.4, 0.07, 0.06), F(0xf4f0e6, { roughness: 0.3 }), [0, 0.03, 0.02]); agiz.add(dis);
  // saç: büyük köşeli tutamlar
  { // saç: kafaya oturan kapak + önde kabarık perçem (vertex ile yükseltilir)
    const g = new THREE.SphereGeometry(1.07, 13, 7, 0, Math.PI * 2, 0, Math.PI * 0.37), q = g.attributes.position;
    for (let i = 0; i < q.count; i++) { let x = q.getX(i), y = q.getY(i), z = q.getZ(i);
      x *= 0.9; z *= 1.02; y *= 1.12;
      const on = sm(-0.1, 0.9, z), tep = sm(0.55, 1.0, y / 1.12);
      y += 0.3 * on * tep + 0.08 * on; z += 0.12 * on * tep;          // pompadour
      if (z < -0.2) y -= 0.05;
      q.setXYZ(i, x, y, z); }
    titret(g, 0.045, 7); head.add(M(g, sacM, [0, 0.0, -0.02]));
    const arka = new THREE.SphereGeometry(1.06, 11, 6, 0, Math.PI * 2, 0, Math.PI * 0.5); titret(arka, 0.04, 8);
    head.add(M(arka, sacM, [0, 0.05, -0.08], [-1.05, 0, 0], [0.9, 1.0, 1.0]));     // ense
  }
  for (const s of [-1, 1]) head.add(M(new THREE.BoxGeometry(0.1, 0.42, 0.22), sacM, [s * 0.82, 0.3, 0.12], [0, s * 0.2, 0])); // favori
  if (bas) head.add(bas);
  // ---- boyun, gövde ----
  root.add(M(new THREE.CylinderGeometry(0.46, 0.52, 0.6, 7), deri, [0, -1.05, -0.1]));
  const govde = new THREE.Group(); govde.position.y = 0.7; root.add(govde); const _root = root;
  const govdeProf = [[0.0, -1.6], [0.55, -1.62], [1.55, -1.95], [2.15, -2.45], [2.3, -3.3], [2.25, -6]].map(([x, y]) => new THREE.Vector2(x, y));
  const gv = M(titret(new THREE.LatheGeometry(govdeProf, 12), 0.02, 11), F(ceket, { roughness: 0.85 }), [0, 0, -0.2], [0, Math.PI / 12, 0], [1, 1, 0.62]); govde.add(gv);
  const on = 1.38; // ceketin ön yüzü z
  govde.add(Object.assign(ekstr([[-0.48, -1.55], [0.48, -1.55], [0.0, -3.7]], 0.05, F(gomlek, { roughness: 0.6 })), {}).translateZ(on - 0.05));
  for (const s of [-1, 1]) { const y = ekstr([[0, 0], [s * 0.55, 0.05], [s * 0.2, -0.55]], 0.08, F(gomlek, { roughness: 0.6 })); y.position.set(s * 0.05, -1.5, on + 0.04); y.rotation.x = -0.3; govde.add(y); }
  const kr = ekstr([[-0.13, 0], [0.13, 0], [0.09, -0.22], [0.2, -2.4], [0, -2.65], [-0.2, -2.4], [-0.09, -0.22]], 0.06, F(kravat, { roughness: 0.4 })); kr.position.set(0, -1.62, on + 0.03); kr.rotation.x = -0.12; govde.add(kr);
  for (const s of [-1, 1]) { const l = ekstr([[s * 0.5, -1.55], [s * 0.95, -1.75], [s * 0.7, -2.3], [s * 0.85, -2.45], [s * 0.15, -3.9], [s * 0.1, -3.7]], 0.08, F(ceket, { roughness: 0.6 })); l.position.z = on + 0.02; l.rotation.y = -s * 0.12; govde.add(l); }
  govde.add(Object.assign(ekstr([[0, 0], [0.42, 0.12], [0.36, -0.12]], 0.05, F(mendil, { roughness: 0.6 })), {}).translateX(-1.45).translateY(-2.75).translateZ(on - 0.15).rotateY(0.5));

  // ---- ifade: { kizgin, saskin, gulumse, kirp } 0..1 ----
  function ifade({ kizgin = 0, saskin = 0, gulumse = 0, kirp = 0, bak = [0, 0] } = {}) {
    for (const { k, s } of kas) { k.position.y = 0.36 + saskin * 0.16 - kizgin * 0.04; k.rotation.z = s * (kizgin * 0.42 - saskin * 0.12); }
    for (const { kp, kp2, cizgi, s } of kapak) {
      const ust = -0.8 + kizgin * 0.5 - saskin * 0.5 + kirp * 2.0;
      kp.rotation.x = ust; kp.rotation.z = s * kizgin * 0.3; kp2.rotation.x = 1.15 - gulumse * 0.35 - kirp * 1.1;
      cizgi.position.y = 0.06 - (ust + 0.8) * 0.07; cizgi.rotation.z = s * kizgin * 0.28;
    }
    for (const { iris, g } of goz) { iris.position.x = bak[0] * 0.06; iris.position.y = -0.005 + bak[1] * 0.04; iris.scale.setScalar(1 - saskin * 0.18); g.scale.y = 1 + saskin * 0.25; }
    const ac = saskin; ic.scale.set(1.3 - ac * 0.35, 0.1 + ac * 0.65, 0.25); ic.position.y = -0.02 - ac * 0.05; dis.visible = ac > 0.15; dis.position.y = 0.0 - ac * 0.02;
    dudak.scale.set(1 + gulumse * 0.25 - ac * 0.2, 1, 1); dudak.rotation.z = 0; agiz.position.y = -0.66 - ac * 0.06;
    biyik.rotation.x = -gulumse * 0.08; biyik.position.y = -0.43 + gulumse * 0.02;
  }
  ifade({ kizgin: 0.6, gulumse: 0.3 });
  return { root, head, ifade };
}

// Sıcak ışıklı çalışma odası: bulanık kitaplık, pencere, bokeh
export function lowPolyOda(scene, { pencere = 1 } = {}) {
  const u = scene.userData.sky.material.uniforms; u.top.value.set(0x3a2a1a); u.mid.value.set(0x5a4028); u.horizon.value.set(0x7a5a38); u.floorC.value.set(0x2a1a10);
  scene.environmentIntensity = 0.35;
  const key = scene.userData.key; key.color.set(0xffc58a); key.intensity = 3.2; key.position.set(10, 5, 1.5); key.shadow.camera.left = key.shadow.camera.bottom = -8; key.shadow.camera.right = key.shadow.camera.top = 8; key.shadow.camera.updateProjectionMatrix();
  scene.children.filter(c => c.isHemisphereLight).forEach(h => { h.color.set(0xffd8b0); h.groundColor.set(0x3a2418); h.intensity = 0.38; });
  const rim = new THREE.DirectionalLight(0x9ab8ff, 0.9); rim.position.set(-6, 4, -6); scene.add(rim);
  const duvar = F(0x5a3a24, { roughness: 0.95 }); scene.add(M(new THREE.PlaneGeometry(60, 40), duvar, [0, 0, -14]));
  // kitaplık
  const raf = F(0x3a2416);
  for (let r = 0; r < 5; r++) { scene.add(M(new THREE.BoxGeometry(9, 0.25, 1.4), raf, [-6, -6 + r * 3.2, -13])); for (let b = 0; b < 16; b++) { const h = 2.0 + ((b * 37 + r * 11) % 7) * 0.12, c = [0x6a2a1a, 0x2a3a5a, 0x5a4a2a, 0x1f3a2a, 0x7a5a3a, 0x3a2a3a][(b + r * 3) % 6]; scene.add(M(new THREE.BoxGeometry(0.45, h, 1.1), F(c), [-10 + b * 0.53, -6 + r * 3.2 + 0.12 + h / 2, -12.9], [0, 0, ((b * 7) % 5 === 0) ? 0.15 : 0])); } }
  // pencere (sağda, parlak)
  scene.add(M(new THREE.PlaneGeometry(7, 12), new THREE.MeshBasicMaterial({ color: new THREE.Color(1.6 * pencere, 1.3 * pencere, 0.9 * pencere), toneMapped: false }), [8, 1, -13.9]));
  for (let i = 0; i < 4; i++) scene.add(M(new THREE.BoxGeometry(0.3, 12, 0.3), raf, [4.5 + i * 2.3, 1, -13.7]));
  // bokeh ışıkları
  for (let i = 0; i < 14; i++) { const b = glowSprite(i % 3 ? 0xffc078 : 0xfff0d0, 0.8 + (i % 4) * 0.4); b.position.set(-12 + (i * 53) % 24, -4 + (i * 31) % 14, -12); b.material.opacity = 0.35; scene.add(b); }
  return { guncelle() {} };
}
