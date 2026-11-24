#!/usr/bin/env bash
# Maakt filmpje.mp4 van dia01.png..diaNN.png en audio/s01.mp3..sNN.mp3 in de map $1.
# Elke dia staat 0,6 s voor en 1,0 s na de gesproken tekst in beeld.
# Gebruik: bash maak-mp4.sh /pad/naar/werkmap 10
set -euo pipefail
W="$1"; N="$2"
mkdir -p "$W/seg"
: > "$W/lijst.txt"
for n in $(seq -w 1 "$N"); do
  i=$(printf "%02d" "$((10#$n))")
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$W/audio/s$i.mp3")
  T=$(python3 -c "print(round($d+1.6,2))")
  ffmpeg -v error -y -loop 1 -framerate 30 -i "$W/dia$i.png" -i "$W/audio/s$i.mp3" \
    -filter_complex "[1:a]adelay=600|600,apad=whole_dur=$T,aresample=44100[a];[0:v]format=yuv420p[v]" \
    -map "[v]" -map "[a]" -t "$T" -c:v libx264 -tune stillimage -preset medium -crf 20 -r 30 \
    -c:a aac -b:a 160k -ac 2 "$W/seg/$i.mp4"
  echo "file '$W/seg/$i.mp4'" >> "$W/lijst.txt"
done
ffmpeg -v error -y -f concat -safe 0 -i "$W/lijst.txt" -c copy -movflags +faststart "$W/filmpje.mp4"
ffprobe -v error -show_entries format=duration,size -of compact "$W/filmpje.mp4"
