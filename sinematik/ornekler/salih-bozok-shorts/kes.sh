#!/bin/bash
# Salih Bozok uzun videosundan Shorts: parçaları kes, eklerde kısa kararma, kapağı ilk 2 kareye göm.
set -e
SRC=../salih-bozok/video.mp4
cut() { # out start end fin fout
  ffmpeg -v error -y -ss $2 -i $SRC -t $(python3 -c "print(round($3-$2,3))") -vf "fade=t=in:st=0:d=$4,fade=t=out:st=$(python3 -c "print(round($3-$2-$5,3))"):d=$5" \
    -af "afade=t=in:st=0:d=$4,afade=t=out:st=$(python3 -c "print(round($3-$2-$5,3))"):d=$5" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -r 30 $1
}
make() { # n segs...
  n=$1; shift; i=0; : > build/l$n.txt; segs=("$@"); k=${#segs[@]}
  for s in "${segs[@]}"; do set -- $s; fi=0.25; fo=0.25; [ $i = 0 ] && fi=0.01; [ $i = $((k-1)) ] && fo=0.8
    cut build/s${n}_$i.mp4 $1 $2 $fi $fo; echo "file '$PWD/build/s${n}_$i.mp4'" >> build/l$n.txt; i=$((i+1)); done
  ffmpeg -v error -y -f concat -safe 0 -i build/l$n.txt -i kapak$n.jpg -filter_complex "[1:v]scale=1080:1920,format=yuv420p[k];[0:v][k]overlay=0:0:enable='lt(n,2)'[v]" \
    -map "[v]" -map 0:a -c:v libx264 -preset medium -b:v 5000k -maxrate 7000k -bufsize 14000k -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart short$n.mp4
}
mkdir -p build
make 1 "0.0 12.95" "492.35 547.75"
make 2 "277.5 303.0" "634.2 657.9"
make 3 "46.95 77.0" "591.6 601.7"
