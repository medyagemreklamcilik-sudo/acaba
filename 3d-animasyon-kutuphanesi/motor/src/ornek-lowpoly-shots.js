import * as THREE from 'three';
import { cam, place, kf, smooth, easeOut, shake } from './anim.js';
import { lowPolyAdam, lowPolyOda } from './kutuphane/lowpoly.js';
// 4 sn deneme: 0-2.2 kararlı bakış (yavaş yaklaşma, göz kırpma, kaş çatma) | 2.2-4 şaşkın yakın çekim
export const DURATION = 4; export const CAPTIONS = []; export const FADES = [];
function sahne(makeStage) { const s = makeStage({ shadowSize: 6, sunDir: [10, 5, 1.5] }); lowPolyOda(s); const a = lowPolyAdam(); s.add(a.root); return { s, a }; }
export const SHOTS = [
  { start: 0, end: 2.2, build: ({ makeStage }) => { const { s, a } = sahne(makeStage); const c = cam(30); return { scene: s, camera: c, update(t) {
      const kirp = t > 1.0 && t < 1.16 ? Math.sin((t - 1.0) / 0.16 * Math.PI) : 0;
      a.ifade({ kizgin: kf(t, [[0, 0.2], [1.3, 0.9]]), gulumse: kf(t, [[1.2, 0], [1.8, 0.45]]), kirp, bak: [kf(t, [[0, 0.5], [0.8, 0]]), 0] });
      a.head.rotation.y = kf(t, [[0, 0.25], [0.9, 0.0]]); a.head.rotation.x = kf(t, [[0, 0], [1.4, 0.08]]);
      const sh = shake(t, 3, 2); const z = kf(t, [[0, 10.5], [2.2, 8.6]], x => x);
      place(c, [0.3 + sh[0] * 10, -0.4 + sh[1] * 10, z], [0, -0.55, 0]);
      return { dof: { focus: z, aperture: 0.012, maxblur: 0.02 }, bloom: 0.6, exposure: 1.1 }; } }; } },
  { start: 2.2, end: 5, build: ({ makeStage }) => { const { s, a } = sahne(makeStage); const c = cam(30); return { scene: s, camera: c, update(t) {
      a.ifade({ saskin: easeOut(Math.min(1, t / 0.25)), bak: [0, 0.1] }); a.head.rotation.x = -0.05; a.head.position.z = kf(t, [[0, 0], [0.3, 0.15]]);
      const sh = shake(t * 3, 6 * Math.max(0, 1 - t / 0.6), 5); const z = kf(t, [[0, 5.0], [1.8, 5.6]], x => x);
      place(c, [sh[0] * 10, 0.15 + sh[1] * 10, z], [0, 0.0, 0]);
      return { dof: { focus: z, aperture: 0.014, maxblur: 0.022 }, bloom: 0.6, exposure: 1.1 }; } }; } },
];
