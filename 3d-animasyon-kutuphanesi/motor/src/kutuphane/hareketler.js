// Pozlar ve hareketler. h.setPose(POZ) ile kullanılır; zamanla değişenler fonksiyondur: h.setPose(YURU(t))
import { lerpPose } from '../human.js';
export { lerpPose };

export const DUR = { lSh: [0.05, 0, 0.16], rSh: [0.05, 0, -0.16], lEl: [-0.25, 0, 0], rEl: [-0.25, 0, 0], lHip: [0, 0, 0.07], rHip: [0, 0, -0.07], lAn: [0, 0, -0.07], rAn: [0, 0, 0.07] };
export const OTUR = { lHip: [-1.5, 0, 0.12], rHip: [-1.5, 0, -0.12], lKn: [1.45, 0, 0], rKn: [1.45, 0, 0], lAn: [0.05, 0, 0], rAn: [0.05, 0, 0], lSh: [-0.45, 0, 0.32], rSh: [-0.45, 0, -0.32], lEl: [-0.95, 0, 0], rEl: [-0.95, 0, 0], drop: -0.47 };
export const BAGDAS = { lHip: [-1.4, 0.9, 0.5], rHip: [-1.4, -0.9, -0.5], lKn: [2.4, 0, 0], rKn: [2.4, 0, 0], lSh: [-0.3, 0, 0.2], rSh: [-0.3, 0, -0.2], lEl: [-1.1, 0, 0], rEl: [-1.1, 0, 0], drop: -0.82 };
export const ISARET = { ...DUR, rSh: [-1.45, 0.1, -0.05], rEl: [-0.1, 0, 0], chest: [0.05, -0.12, 0] };
export const OTUR_ISARET = { ...OTUR, rSh: [-1.45, 0.1, -0.05], rEl: [-0.1, 0, 0], chest: [0.08, -0.1, 0] };
export const TEMENNA = { ...DUR, spine: [0.35, 0, 0], chest: [0.2, 0, 0], head: [0.2, 0, 0], rSh: [-0.9, 0, -0.2], rEl: [-1.6, 0, 0], lSh: [0.2, 0, 0.1] }; // saygıyla eğilme
export const SECDE = { spine: [1.15, 0, 0], chest: [0.35, 0, 0], neck: [0.2, 0, 0], lHip: [-2.0, 0, 0.1], rHip: [-2.0, 0, -0.1], lKn: [2.55, 0, 0], rKn: [2.55, 0, 0], lAn: [0.9, 0, 0], rAn: [0.9, 0, 0], lSh: [-0.75, 0, 0.25], rSh: [-0.75, 0, -0.25], lEl: [-0.4, 0, 0], rEl: [-0.4, 0, 0], drop: -0.62 };
export const DUA = { ...DUR, lSh: [-0.9, 0, 0.35], rSh: [-0.9, 0, -0.35], lEl: [-1.3, 0, 0], rEl: [-1.3, 0, 0], head: [0.15, 0, 0] };
export const ASKER_SELAMI = { ...DUR, rSh: [-0.6, 0, -1.35], rEl: [-2.3, 0, 0], rWr: [0, 0, 0.3] };
export const KOLLAR_BELDE = { ...DUR, lSh: [0.1, 0, 0.55], rSh: [0.1, 0, -0.55], lEl: [-1.9, 0, 0], rEl: [-1.9, 0, 0] };
export const KOLLAR_KAVUSUK = { ...DUR, lSh: [-0.45, 0, 0.1], rSh: [-0.45, 0, -0.1], lEl: [-1.9, 0.6, 0], rEl: [-1.9, -0.6, 0] };
export const ELLER_HAVADA = { ...DUR, lSh: [-2.6, 0, 0.4], rSh: [-2.6, 0, -0.4], lEl: [-0.3, 0, 0], rEl: [-0.3, 0, 0], head: [-0.2, 0, 0] };
export const BOGAZ_TUT = { ...DUR, lSh: [-1.15, 0, -0.39], rSh: [-1.15, 0, 0.39], lEl: [-2.15, 0, 0], rEl: [-2.15, 0, 0], head: [-0.3, 0, 0] };
export const KITAP_OKU = { ...DUR, lSh: [-0.7, 0, 0.15], rSh: [-0.7, 0, -0.15], lEl: [-1.3, 0.4, 0], rEl: [-1.3, -0.4, 0], head: [0.35, 0, 0], neck: [0.15, 0, 0] };
export const KURSU_KONUS = { ...DUR, rSh: [-1.2, 0.3, -0.35], rEl: [-0.9, 0, 0], lSh: [-0.2, 0, 0.2], chest: [-0.05, 0, 0] };

const s = Math.sin;
// yürüyüş döngüsü (yerinde); root'u ayrıca ileri taşı: hız ≈ 0.9 m/sn
export function YURU(t, hiz = 1) {
  const p = t * 6.2 * hiz;
  return { lHip: [s(p) * 0.45, 0, 0.05], rHip: [-s(p) * 0.45, 0, -0.05], lKn: [Math.max(0, -s(p + 1.2)) * 0.9, 0, 0], rKn: [Math.max(0, s(p + 1.2)) * 0.9, 0, 0],
    lSh: [-s(p) * 0.4, 0, 0.12], rSh: [s(p) * 0.4, 0, -0.12], lEl: [-0.35, 0, 0], rEl: [-0.35, 0, 0], chest: [0.03, s(p) * 0.06, 0], drop: -Math.abs(s(p)) * 0.025 };
}
export function KOS(t) { const p = t * 10; return { ...YURU(t, 1.6), lSh: [-s(p) * 0.9, 0, 0.15], rSh: [s(p) * 0.9, 0, -0.15], lEl: [-1.4, 0, 0], rEl: [-1.4, 0, 0], spine: [0.15, 0, 0], drop: -0.05 - Math.abs(s(p)) * 0.04 }; }
// nefes / bekleme kıpırtısı
export function NEFES(t, poz = DUR, k = 1) { return { ...poz, chest: [(poz.chest?.[0] || 0) + s(t * 1.6) * 0.012 * k, poz.chest?.[1] || 0, 0], neck: [0.05, s(t * 0.7) * 0.08 * k, 0] }; }
// yazı yazma (masada otururken)
export function YAZ(t) { return { ...OTUR, rSh: [-0.9 + s(t * 7) * 0.05, 0, -0.15], rEl: [-1.1, 0, 0], rWr: [s(t * 9) * 0.2, 0, 0], head: [0.35, 0, 0], spine: [0.15, 0, 0] }; }
// boğulma → geriye düşme: f 0..1 (root.rotation.x = -f*1.48 ile birlikte kullan)
export function BOGUL_DUS(f, t = 0) { return { ...lerpPose(DUR, BOGAZ_TUT, Math.min(1, f * 3)), head: [-0.35 * f, s(t * 14) * 0.08 * (1 - f), 0], drop: -0.02 * f }; }
export function dusur(h, f) { h.root.rotation.x = -f * 1.48; }
// semazen dönüşü (derviş): root.rotation.y = t * hiz ile birlikte
export function SEMA(t) { return { ...DUR, rSh: [-0.2, 0, -1.6], lSh: [-0.2, 0, 1.4], rEl: [-0.3, 0, 0], lEl: [-0.2, 0, 0], head: [0, 0, 0.3], drop: s(t * 3) * 0.005 }; }
// konuşma: ağız hareketi
export function konus(h, t, siddet = 0.5) { h.setMouth(Math.max(0, s(t * 17) * 0.5 + s(t * 11) * 0.5) * siddet); }
