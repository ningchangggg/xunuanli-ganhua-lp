#!/bin/zsh
# 03c 三色禮盒推入動圖格（2026-11-25）
# 來源：丁丁 11/19「幹話日曆(版本1).mp4」的推盒段，本機取自 11.20丁丁④幹話_笑點開頭_v6.mp4 12.567–15.133 秒
# 天藍 0–0.566、薄荷 0.566–1.1 放慢 0.65 倍；卡其 1.1–2.566 原速；裁 1000x1250（從 y=560 往下，避開丁丁原片壓的「推出3款」字）
SRC=${1:-"../../../01_廣告投放/幹話日曆/成片/丁丁廣告_1120/11.20丁丁④幹話_笑點開頭_v6.mp4"}
cd "$(dirname $0)"; mkdir -p clips/g_box; rm -f clips/g_box/*
ffmpeg -v error -y -ss 12.567 -t 2.566 -i "$SRC" -filter_complex "[0:v]crop=1000:1250:0:560,split=3[a][b][c];[a]trim=0:0.566,setpts=(PTS-STARTPTS)/0.65[a1];[b]trim=0.566:1.1,setpts=(PTS-STARTPTS)/0.65[b1];[c]trim=1.1:2.566,setpts=PTS-STARTPTS[c1];[a1][b1][c1]concat=n=3:v=1,fps=15,eq=saturation=1.06" -q:v 2 clips/g_box/%03d.jpg
# 03d 丁丁抱三盒：同一支 v6 的 8.05 秒，裁 (0,340) 1080x1350 → img/gift.jpg
