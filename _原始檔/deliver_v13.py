"""幹話曆落地頁 v13 交付：v12 的區塊圖＋新 03c（送禮範例動圖）＋03d（丁丁抱三盒）。"""
import os, shutil, base64, io, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
B = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/04_內容企劃/_多產品/落地頁改版設計_1122/"
V12 = B + '11.24_幹話日曆_落地頁改版_v12_受眾卡內頁縮小一點/'
V11 = B + '11.24_幹話日曆_落地頁改版_v11_拆解標籤移到內頁外_玄關笑著出門/'
NAME = '11.25_幹話日曆_落地頁改版_v13_加送禮範例_丁丁三色禮盒'; PRE = '11.25_幹話日曆_落地頁改版_v13'
O = B + NAME
SEC = ['03_誰適合幹話曆.jpg', '03b_聖誕節前到貨_金光_GIF.gif', '03c_送禮範例_三色禮盒_GIF.gif', '03d_送禮範例_交換禮物.jpg',
       '04_數字列.jpg', '05_365天內頁牆.jpg', '05a_撕下今天_GIF.gif', '06_一頁拆解_8天輪播_GIF.gif', '06a_貼到同事螢幕_GIF.gif',
       '07_貼成幹話牆_GIF.gif', '08_偷看明天_GIF.gif', '09_使用說明書.jpg', '10_三色底座.jpg', '11_規格.jpg', '12_轉折.jpg']
for sub in ['說明圖_1080寬', '動圖_MP4備用', '_原始檔']:
    os.makedirs(f'{O}/{sub}', exist_ok=True)
for n in SEC:
    dst = f'{O}/說明圖_1080寬/{n}'
    if n.startswith('03c'):
        shutil.copy(f'{D}/gif/enc/s03c.gif', dst); shutil.copy(f'{D}/gif/enc/s03c.mp4', f'{O}/動圖_MP4備用/{n[:-4]}.mp4')
    elif n.startswith('03d'):
        Image.open(f'{D}/sec/s03d.png').convert('RGB').save(dst, quality=90)
    else:
        shutil.copy(V12 + '說明圖_1080寬/' + n, dst)
        if n.endswith('.gif'): shutil.copy(V11 + '動圖_MP4備用/' + n[:-4] + '.mp4', f'{O}/動圖_MP4備用/{n[:-4]}.mp4')
head = ('<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>幹話曆落地頁 v13</title><style>body{margin:0;background:#888}main{max-width:432px;margin:0 auto;background:#fff}img,video{display:block;width:100%}</style><main>')
dyn = head + '\n'.join(f'<img src="說明圖_1080寬/{n}">' for n in SEC) + '</main>'
open(f'{O}/{PRE}_整頁預覽_動態.html', 'w').write(dyn)
parts, stills = [], []
for n in SEC:
    if n.endswith('.gif'):
        mp4 = f'{O}/動圖_MP4備用/{n[:-4]}.mp4'
        parts.append(f'<video autoplay muted loop playsinline src="data:video/mp4;base64,{base64.b64encode(open(mp4,"rb").read()).decode()}"></video>')
        fr = '00:00:01' if n.startswith('03b') else '00:00:00'
        b = subprocess.run(['ffmpeg', '-v', 'error', '-ss', fr, '-i', mp4, '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        stills.append(Image.open(io.BytesIO(b)).convert('RGB'))
    else:
        im = Image.open(f'{O}/說明圖_1080寬/{n}').convert('RGB'); stills.append(im)
        sm = im.resize((864, round(im.height * 864 / im.width)), Image.LANCZOS); bio = io.BytesIO(); sm.save(bio, 'JPEG', quality=86)
        parts.append(f'<img src="data:image/jpeg;base64,{base64.b64encode(bio.getvalue()).decode()}">')
open(f'{O}/{PRE}_整頁預覽_單檔整合.html', 'w').write(head + ''.join(parts) + '</main>')
stills = [s.resize((1080, round(s.height * 1080 / s.width))) for s in stills]
H = sum(s.height for s in stills); st = Image.new('RGB', (1080, H)); y = 0
for s in stills: st.paste(s, (0, y)); y += s.height
st.resize((540, H // 2), Image.LANCZOS).save(f'{O}/{PRE}_整頁預覽_靜態第一格.jpg', quality=82)
for f in ['build_page.py', 'page.html', 'LH.ttf', 'shot.py', 'shot_one.py', 'deliver_v13.py']:
    shutil.copy(f'{D}/{f}', f'{O}/_原始檔/{f}')
for f in ['clips_gh.py', 'clips_gbox.sh', 'render_gif.py', 'enc.sh', 'caps_g_days.json', 'caps_g_box.json']:
    shutil.copy(f'{D}/gif/{f}', f'{O}/_原始檔/{f}')
shutil.copytree(f'{D}/img', f'{O}/_原始檔/img', dirs_exist_ok=True)
print(O, H)
