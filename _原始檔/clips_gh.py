"""幹話曆落地頁實拍動圖片段（2026-11-24）。iPhone HLG 轉 bt709；裁 4:5；彩度 1.45、對比 1.05。"""
import subprocess,os,shutil,sys
from concurrent.futures import ThreadPoolExecutor
M="/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/幹話日曆/毛片/"
FPS=15
C={
 'g_tear':  (M+'麻豆_影片_0812/C0004.mp4', 0.0, 4.15, 1.0, 0.36, False),
 'g_share': (M+'阿寧_演義/IMG_5359.MOV', 9.4, 14.4, 1.3, 0.45, True),
 'g_wall':  (M+'大C_B/影片檔_調色對齊麻豆/C3560.mp4', 2.2, 14.5, 2.0, 0.45, False),
 'g_flip':  (M+'大C_B/影片檔_調色對齊麻豆/C3528.mp4', 0.8, 8.2, 1.3, 0.62, False),
}
def run(item):
    n,(src,t0,t1,sp,cy,hdr)=item
    od=os.path.dirname(os.path.abspath(__file__))+f'/clips/{n}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
    pre='colorspace=all=bt709:iall=bt2020:itrc=bt709:format=yuv420p,' if hdr else ''
    vf=(f"{pre}setpts=PTS/{sp},fps={FPS},crop=iw:iw*1.25:0:(ih-iw*1.25)*{cy},"
        f"scale=1080:1350:flags=lanczos,eq=saturation=1.45:contrast=1.05")
    subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',src,'-vf',vf,'-q:v','2',f'{od}/%03d.jpg'],check=True,stdin=subprocess.DEVNULL)
    return n,len(os.listdir(od))
sel=sys.argv[1:] or list(C)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,[(k,C[k]) for k in sel]): print(r)
