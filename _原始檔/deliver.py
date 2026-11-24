"""把 sec/*.png 與 gif/enc 整理成交付資料夾（幹話曆 v9）。"""
import os, shutil, base64, io, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
B = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/04_內容企劃/_多產品/落地頁改版設計_1122/"
V = 'v11'; NAME = f'11.24_幹話日曆_落地頁改版_{V}_拆解標籤移到內頁外_玄關笑著出門'
O = B + NAME
SEC = [('s03', '03_誰適合幹話曆', 0), ('s03b', '03b_聖誕節前到貨_金光_GIF', 1), ('s04', '04_數字列', 0),
       ('s05', '05_365天內頁牆', 0), ('s05a', '05a_撕下今天_GIF', 1), ('s06', '06_一頁拆解_8天輪播_GIF', 1),
       ('s06a', '06a_貼到同事螢幕_GIF', 1), ('s07', '07_貼成幹話牆_GIF', 1), ('s08', '08_偷看明天_GIF', 1),
       ('s09', '09_使用說明書', 0), ('s10', '10_三色底座', 0), ('s11', '11_規格', 0), ('s12', '12_轉折', 0)]
for sub in ['說明圖_1080寬', '動圖_MP4備用', '_原始檔']:
    os.makedirs(f'{O}/{sub}', exist_ok=True)
names = []
for sid, nm, g in SEC:
    if g:
        shutil.copy(f'{D}/gif/enc/{sid}.gif', f'{O}/說明圖_1080寬/{nm}.gif')
        shutil.copy(f'{D}/gif/enc/{sid}.mp4', f'{O}/動圖_MP4備用/{nm}.mp4')
        names.append((sid, nm + '.gif', g))
    else:
        Image.open(f'{D}/sec/{sid}.png').convert('RGB').save(f'{O}/說明圖_1080寬/{nm}.jpg', quality=90)
        names.append((sid, nm + '.jpg', g))
title = f'幹話曆落地頁 {V}'
head = f'<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>body{{margin:0;background:#888}}main{{max-width:432px;margin:0 auto;background:#fff}}img,video{{display:block;width:100%}}</style><main>'
dyn = head + '\n'.join(f'<img src="說明圖_1080寬/{n}">' for _, n, _ in names) + '</main>'
open(f'{O}/{NAME.replace("_拆解標籤移到內頁外_玄關笑著出門","")}_整頁預覽_動態.html', 'w').write(dyn)
# single file
parts = []
for sid, n, g in names:
    if g:
        b = base64.b64encode(open(f'{D}/gif/enc/{sid}.mp4', 'rb').read()).decode()
        parts.append(f'<video autoplay muted loop playsinline src="data:video/mp4;base64,{b}"></video>')
    else:
        im = Image.open(f'{O}/說明圖_1080寬/{n}'); im = im.resize((864, round(im.height * 864 / im.width)), Image.LANCZOS)
        bio = io.BytesIO(); im.save(bio, 'JPEG', quality=86)
        parts.append(f'<img src="data:image/jpeg;base64,{base64.b64encode(bio.getvalue()).decode()}">')
open(f'{O}/{NAME.replace("_拆解標籤移到內頁外_玄關笑著出門","")}_整頁預覽_單檔整合.html', 'w').write(head + ''.join(parts) + '</main>')
# static preview: first frame of each gif (s06 frame 1, s03b frame 10)
ims = []
for sid, n, g in names:
    if g:
        fr = {'s03b': '010'}.get(sid, '001')
        ims.append(Image.open(f'{D}/gif/secframes/{sid}/{fr}.png').convert('RGB'))
    else:
        ims.append(Image.open(f'{O}/說明圖_1080寬/{n}').convert('RGB'))
H = sum(i.height for i in ims); st = Image.new('RGB', (1080, H)); y = 0
for i in ims: st.paste(i, (0, y)); y += i.height
st = st.resize((540, H // 2), Image.LANCZOS)
st.save(f'{O}/{NAME.replace("_拆解標籤移到內頁外_玄關笑著出門","")}_整頁預覽_靜態第一格.jpg', quality=82)
# sources
for f in ['build_page.py', 'page.html', 'LH.ttf', 'shot.py', 'deliver.py']:
    shutil.copy(f'{D}/{f}', f'{O}/_原始檔/{f}')
for f in ['clips_gh.py', 'render_gif.py', 'enc.sh', 'caps_g_days.json']:
    shutil.copy(f'{D}/gif/{f}', f'{O}/_原始檔/{f}')
shutil.copytree(f'{D}/img', f'{O}/_原始檔/img', dirs_exist_ok=True)
print(O); print(dyn[:200])
