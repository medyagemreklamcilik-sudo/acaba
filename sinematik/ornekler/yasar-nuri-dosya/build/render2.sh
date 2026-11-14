cd /home/user/acaba/sinematik
export NODE_PATH=/home/user/acaba/vendor/claude-animation-skills/kit/node_modules CHROME=/opt/pw-browsers/chromium
D=ornekler/yasar-nuri-dosya; END=4045; C=270; W=${W:-4}
job() { f0=$1; f1=$(( f0 + C < END ? f0 + C : END )); o=$D/build/seg/c$(printf %05d $f0).mp4
  [ -f $o ] && return; node motor/render.js $D range $f0 $f1 $o.tmp.mp4 > $D/build/c$f0.log 2>&1 && mv $o.tmp.mp4 $o; }
export -f job; export D END C
seq 0 $C $((END-1)) | xargs -P $W -I{} bash -c 'job {}'
