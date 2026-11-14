#!/bin/bash
# Sinematik "dosya" videosu üretim hattı (dikey 1080x1920, 30 fps).
# Kullanım:
#   bash sinematik/motor/uret.sh <klasör> stills [t1,t2,...]   → derle + kontrol kareleri (<klasör>/stills/)
#   bash sinematik/motor/uret.sh <klasör> final                → derle + parça render + ses + kapak ilk 2 kare → <klasör>/video.mp4
# Klasörde gerekenler: tts.txt, build/voice.mp3 + build/aligned.json (tools/viral.py voice), img/*.jpg, build/storyboard.py, kapak.json.
# Yarıda kalırsa aynı komutu yeniden çalıştır: bitmiş parçalar atlanır.
set -e
MOTOR=$(cd "$(dirname "$0")" && pwd)
D=$(cd "$1" && pwd); MODE=${2:-final}
export NODE_PATH=/home/user/acaba/vendor/claude-animation-skills/kit/node_modules CHROME=/opt/pw-browsers/chromium
REL=$(python3 -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$MOTOR" "$D")
cat > "$D/index.html" <<EOF
<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:"IBM Plex Mono";font-weight:500;src:url($REL/fonts/PlexMono.ttf)}
@font-face{font-family:"IBM Plex Mono";font-weight:600;src:url($REL/fonts/PlexMonoSemi.ttf)}
@font-face{font-family:"Special Elite";src:url($REL/fonts/SpecialElite.ttf)}
@font-face{font-family:"Cormorant Garamond";font-weight:300 700;src:url($REL/fonts/CormorantGaramond.ttf)}
@font-face{font-family:Oswald;font-weight:200 700;src:url($REL/fonts/Oswald.ttf)}
body{margin:0;background:#000}</style></head><body><canvas id="c"></canvas>
<script src="$REL/geo/dogu-akdeniz.js"></script><script src="sahne.js"></script><script src="$REL/dosya.js"></script>
</body></html>
EOF
[ -f "$D/format.json" ] || echo '{"w":1080,"h":1920,"fps":30}' > "$D/format.json"
python3 "$MOTOR/derle.py" "$D"
END=$(python3 -c "import re;print(re.search(r'dur: (\d+) / 30',open('$D/sahne.js').read()).group(1))")
if [ "$MODE" = "stills" ]; then
  TS=${3:-$(node -e "
const vm=require('vm'),fs=require('fs');const c={};vm.createContext(c);vm.runInContext(fs.readFileSync('$D/sahne.js','utf8')+';this.S=SPACES;',c);
const S=c.S,o=[0.05,1.0];for(let k=0;k<S.length;k++){const e=S[k+1]?S[k+1].t:$END/30-.5;for(const f of [.45,.9])o.push((S[k].t+(e-S[k].t)*f).toFixed(2))}console.log(o.join(','))")}
  rm -rf "$D/stills"; node "$MOTOR/render.js" "$D" stills "$TS" 2>&1 | grep -v '^\[page\]' || true
  python3 -I - "$D" <<'PY'
import sys, glob
from PIL import Image, ImageDraw
d = sys.argv[1]; fs = sorted(glob.glob(d + '/stills/s_*.jpg'), key=lambda f: float(f.split('s_')[-1][:-4]))
W, H = 216, 384; cols = 8; rows = (len(fs) + cols - 1) // cols
sh = Image.new('RGB', (W * cols, (H + 22) * rows), (20, 20, 20)); dr = ImageDraw.Draw(sh)
for i, f in enumerate(fs):
    x, y = (i % cols) * W, (i // cols) * (H + 22); sh.paste(Image.open(f).resize((W, H)), (x, y)); dr.text((x + 4, y + H + 4), f.split('s_')[-1][:-4], fill=(255, 255, 0))
sh.save(d + '/stills/_sayfa.jpg', quality=82); print('kontrol sayfası:', d + '/stills/_sayfa.jpg')
PY
  exit 0
fi
# parça render (270 kare, 4 işçi)
mkdir -p "$D/build/seg"; C=270; W=${W:-4}; export D END C MOTOR CRF=${CRF:-18}
job() { f0=$1; f1=$(( f0 + C < END ? f0 + C : END )); o=$D/build/seg/c$(printf %05d $f0).mp4
  [ -f $o ] && return 0; node $MOTOR/render.js $D range $f0 $f1 $o.tmp.mp4 > $D/build/c$f0.log 2>&1 && mv $o.tmp.mp4 $o; }
export -f job
seq 0 $C $((END-1)) | xargs -P $W -I{} bash -c 'job {}'
N=$(ls $D/build/seg/ | grep -c '^c[0-9]*\.mp4$' || true); NEED=$(( (END + C - 1) / C ))
[ "$N" = "$NEED" ] || { echo "eksik parça: $N/$NEED — komutu yeniden çalıştır"; exit 1; }
python3 "$MOTOR/ses.py" "$D"
[ -f "$D/kapak.jpg" ] || python3 "$MOTOR/kapak.py" "$D/kapak.json" "$D/kapak.jpg"
ls $D/build/seg/ | grep '^c[0-9]*\.mp4$' | sort | sed "s#^#file '$D/build/seg/#;s#\$#'#" > $D/build/list.txt
DUR=$(python3 -c "print($END/30)"); BR=$(python3 -c "d=$END/30;print(int(min(4500, 85*8*1000/d - 200)))")  # < ~90 MB (GitHub raw)
ffmpeg -v error -y -f concat -safe 0 -i $D/build/list.txt -i $D/build/mix.wav -i $D/kapak.jpg \
  -filter_complex "[2:v]scale=1080:1920,format=yuv420p[k];[0:v][k]overlay=0:0:enable='lt(n,2)'[v]" -map "[v]" -map 1:a \
  -c:v libx264 -preset medium -b:v ${BR}k -maxrate $((BR*3/2))k -bufsize $((BR*3))k -pix_fmt yuv420p -c:a aac -b:a 160k \
  -af loudnorm=I=-14:TP=-1.5:LRA=11 -movflags +faststart -shortest $D/video.mp4
ls -la $D/video.mp4 | awk '{printf "video.mp4: %.1f MB, ", $5/1048576}'; ffprobe -v error -show_entries format=duration -of csv=p=0 $D/video.mp4
rm -f $D/build/seg/c*.mp4   # yer aç (video.mp4 hazır)
