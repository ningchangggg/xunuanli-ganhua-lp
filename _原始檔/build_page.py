"""幹話曆落地頁 v13（2026-11-25）：綜藝漫畫格版型＋03c 送禮範例（丁丁三色禮盒）。產出 page.html，432 寬。"""
import os, json, math, random
D = os.path.dirname(os.path.abspath(__file__))

P = [
    dict(n='01', who='厭世上班族', h='每天上班，都在等下班', img='p1', pg='d004',
         s='上班前撕一句<mark>幹話</mark>，先<mark>笑一下</mark>再去面對老闆。'),
    dict(n='02', who='心累需要笑一下', h='努力了一整天，<br>只想好好笑一下', img='p2', pg='d001',
         s='不灌雞湯，不說加油，一句幹話就讓你<mark>笑出來</mark>。'),
    dict(n='03', who='交換禮物', h='預算一千，<br>送一個全場笑翻的禮物', img='p3', pg='d003',
         s='拆開那一刻<mark>全場笑翻</mark>，抽到的人每天都想起你。'),
    dict(n='04', who='聖誕禮物', h='送給每天辛苦上班的他', img='p4', pg='d035',
         s='每天早上撕一句幹話，陪他<mark>笑著上班 365 天</mark>。'),
]
L = [
    dict(c=(230, 150), say='right:12px;top:22px', tail='right:40px', card='right:8px;bottom:10px;transform:rotate(6deg)', stk=('？', 'left:20px;top:110px;transform:rotate(-10deg)'), rot=-1),
    dict(c=(150, 150), say='right:12px;top:24px', tail='left:30px', card='right:6px;bottom:6px;transform:rotate(6deg)', stk=('哈', 'left:18px;bottom:40px;transform:rotate(-12deg)'), rot=1),
    dict(c=(160, 110), say='right:10px;top:14px', tail='left:26px', card='right:4px;bottom:8px;transform:rotate(7deg)', stk=('！', 'left:18px;bottom:30px;transform:rotate(-8deg)'), rot=-1),
    dict(c=(110, 120), say='right:12px;top:26px', tail='left:26px', card='right:14px;bottom:22px;transform:rotate(-6deg)', stk=('♡', 'right:30px;top:140px;transform:rotate(10deg)'), rot=1),
]

def speed_lines(cx, cy, n=64, r=(120, 160)):
    random.seed(int(cx * 7 + cy))
    ls = []
    for k in range(n):
        a = math.pi * 2 * k / n + random.uniform(-.03, .03)
        r0 = random.uniform(*r); w = random.uniform(1.2, 3.4)
        ls.append(f'<line x1="{cx+r0*math.cos(a):.0f}" y1="{cy+r0*math.sin(a):.0f}" x2="{cx+520*math.cos(a):.0f}" y2="{cy+520*math.sin(a):.0f}" stroke="#fff" stroke-width="{w:.1f}" stroke-linecap="round" opacity=".85"/>')
    m = f'-webkit-mask-image:radial-gradient(ellipse 62% 62% at {cx/4:.0f}% {cy/4:.0f}%,transparent 78%,#000 86%)'
    return f'<svg class="sl" style="{m}" viewBox="0 0 400 400" preserveAspectRatio="none">' + ''.join(ls) + '</svg>'

def burst(txt, w=160, h=124, fill='#F6D34A', rot=-6, fs=23):
    pts = []
    for k in range(28):
        r = 60 if k % 2 == 0 else 46
        a = math.pi * 2 * k / 28
        pts.append(f'{80+r*math.cos(a)*1.25:.1f},{62+r*math.sin(a)*.95:.1f}')
    return (f'<div class="burst" style="width:{w}px;height:{h}px"><svg viewBox="0 0 160 124" width="{w}" height="{h}"><polygon points="{" ".join(pts)}" fill="{fill}" stroke="#2B2622" stroke-width="3"/></svg>'
            f'<div class="bt lh" style="transform:rotate({rot}deg);font-size:{fs}px">{txt}</div></div>')

CSS = '''
@font-face{font-family:LH;src:url("LH.ttf")}
:root{--or:#C4562A;--ink:#2B2622;--yl:#F6D34A;--paper:#FFF6DF;--navy:#1C2633}
*{box-sizing:border-box;margin:0;padding:0}
body{width:432px;font-family:"Noto Sans CJK TC",sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;background:var(--paper)}
section{position:relative;background:var(--paper);background-image:radial-gradient(rgba(196,86,42,.16) 1.3px,transparent 1.6px);background-size:11px 11px;padding:36px 22px 40px}
.lh{font-family:LH;font-weight:400}
.en{font-family:Helvetica,Arial,sans-serif;font-weight:700;letter-spacing:.2em}
mark{color:inherit;background:linear-gradient(100deg,transparent 2%,rgba(246,211,74,.9) 4%,rgba(246,211,74,.75) 60%,rgba(246,211,74,.9) 96%,transparent 98%) no-repeat 0 78%/100% 48%;padding:0 2px}
.dk mark{background:none;color:var(--yl);font-weight:700;padding:0}
.eb{font-family:LH;font-size:17px;color:var(--or);letter-spacing:.08em;text-align:center}
h2{font-family:LH;font-weight:400;font-size:29px;line-height:1.38;text-align:center;margin-top:8px}
h2 .u{background:linear-gradient(transparent 62%,rgba(196,86,42,.28) 62%)}
.lead{font-size:14.5px;line-height:1.75;text-align:center;margin-top:12px;color:#4a423c}
.burst{position:relative;margin:0 auto}.burst svg{position:absolute;inset:0}
.bt{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;line-height:1.15;text-align:center}
/* panel */
.pn{position:relative;border:3px solid var(--ink);background:#fff;box-shadow:7px 7px 0 var(--ink)}
.pic{position:relative;background-size:cover;background-position:center;overflow:hidden}
.sl{position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:screen;pointer-events:none}
.tag{position:absolute;left:-10px;top:-16px;background:var(--yl);border:3px solid var(--ink);padding:3px 12px 5px;font-size:24px;transform:rotate(-4deg);box-shadow:3px 3px 0 var(--ink);z-index:3}
.tag small{font-family:Helvetica,Arial;font-weight:700;font-size:12px;letter-spacing:.1em;margin-right:6px;vertical-align:3px}
.say{position:absolute;background:#fff;border:3px solid var(--ink);border-radius:22px;padding:9px 14px;font-size:19px;line-height:1.35;max-width:230px;z-index:3}
.say:after{content:"";position:absolute;width:18px;height:18px;background:#fff;border-right:3px solid var(--ink);border-bottom:3px solid var(--ink);bottom:-11px;transform:rotate(45deg)}
.card{position:absolute;width:204px;border:5px solid #fff;box-shadow:0 6px 14px rgba(0,0,0,.28);z-index:2}
.card:before{content:"";position:absolute;width:80px;height:20px;background:rgba(196,86,42,.72);top:-14px;left:62px;transform:rotate(-5deg)}
.stk{position:absolute;width:58px;height:58px;border-radius:50%;background:var(--or);border:3px solid var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-family:LH;z-index:3}
.nar{background:var(--ink);color:#fff;padding:12px 16px 13px;font-size:15px;line-height:1.6}
.nar mark{background:none;color:var(--yl);font-weight:700;padding:0}
/* s03 */
#s03 .burst{margin-top:18px}
#s03 .pn{margin-top:34px}
#s03 .pic{height:388px}
/* s03b */
#s03b{padding:6px 22px 34px}
.xm{position:relative;overflow:hidden;background:#C4402F;border:3px solid var(--ink);box-shadow:7px 7px 0 var(--ink);padding:20px 12px 22px;text-align:center;color:#fff;outline:2px solid #E2BE6E;outline-offset:-9px;transform:rotate(-1deg)}
.xm .sm{font-size:10px;letter-spacing:.32em;color:#F3D99B}
.xm .big{font-family:LH;font-size:36px;letter-spacing:.1em;margin-top:4px;background:linear-gradient(180deg,#FFF6DA 10%,#F1CF7E 55%,#D9A94A 90%);-webkit-background-clip:text;color:transparent}
.xm .sh{position:absolute;top:-30%;bottom:-30%;width:90px;left:-40%;transform:skewX(-22deg);background:linear-gradient(90deg,transparent,rgba(255,236,180,.6),transparent);animation:sweep 2.5s linear infinite}
.xm .sp{position:absolute;width:14px;height:14px;margin:-7px;opacity:0;background:radial-gradient(circle,#FFF4C8 0 18%,transparent 20%),linear-gradient(0deg,transparent 45%,#FFE7A0 45% 55%,transparent 55%),linear-gradient(90deg,transparent 45%,#FFE7A0 45% 55%,transparent 55%);animation:tw 2.5s linear infinite}
@keyframes sweep{0%{left:-40%}55%{left:120%}100%{left:120%}}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}12%{opacity:1;transform:scale(1.15) rotate(20deg)}26%{opacity:0;transform:scale(.4)}}
/* s03c gift */
#s03c{padding:30px 22px 22px}
#s03c .pn{margin-top:30px}
#s03d{padding:22px 22px 44px}
#s03c .gb{height:477px}
#s03d .gf{height:477px;background-position:center top}
#s03c .chips{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid var(--ink);background:#fff}
#s03c .chips div{text-align:center;padding:9px 0 10px;font-family:LH;font-size:17px;border-left:3px solid var(--ink);color:#b3aaa2;transition:none}
#s03c .chips div:first-child{border-left:none}
#s03c .chips div.on{background:var(--yl);color:var(--ink)}
#s03c .chips i{display:block;width:30px;height:12px;margin:0 auto 5px;border:2px solid var(--ink);border-radius:3px;opacity:.45}
#s03c .chips div.on i{opacity:1}
#s03c .gbst{position:absolute;right:-12px;top:388px;z-index:4}
/* s04 */
#s04{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:8px 22px 40px}
#s04>div{background:#fff;border:3px solid var(--ink);box-shadow:4px 4px 0 var(--ink);text-align:center;padding:14px 4px 12px}
#s04>div:nth-child(2){background:var(--yl);transform:rotate(1.5deg)}
#s04>div:nth-child(1){transform:rotate(-1.5deg)}
#s04 .n{font-family:LH;font-size:40px;line-height:1;color:var(--or)}
#s04 .n small{font-size:20px}
#s04 .c{font-size:13px;margin-top:6px}
/* s05 wall */
#s05 .pn{margin-top:26px;background:var(--navy);height:470px;overflow:hidden}
.wall img{position:absolute;width:96px;box-shadow:0 3px 8px rgba(0,0,0,.4);border:2px solid #fff}
#s05 .stk{right:-8px;top:-18px;width:auto;height:auto;border-radius:12px;padding:6px 12px;font-size:20px;transform:rotate(6deg)}
/* how */
.how .hd{text-align:center}
.how .no{display:inline-block;background:var(--yl);border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);padding:4px 12px;font-size:12px;transform:rotate(-2deg)}
.how h3{font-family:LH;font-weight:400;font-size:27px;line-height:1.38;margin-top:14px}
.how p.d{font-size:14.5px;line-height:1.75;color:#4a423c;margin-top:10px}
.how .pn{margin-top:22px}
.how .ph{height:477px;background-size:cover;background-position:center}
.how .bar{display:flex;align-items:center;gap:10px;background:var(--ink);color:#fff;padding:11px 14px}
.how .bar .st{color:var(--yl);font-size:12px}
.how .bar .cn{font-size:16px;flex:1}
.how .bar .ee{font-size:10px;color:#bdb3aa}
.how .sfx{position:absolute;z-index:3}
/* s06 */
#s06 .pn{margin-top:22px;padding:58px 0 0}
#s06 .cap small{font-family:Helvetica,Arial;font-size:11px;letter-spacing:.14em;color:var(--or)}
#s06 .cap{position:absolute;top:0;left:0;right:0;background:var(--yl);border-bottom:3px solid var(--ink);padding:8px 10px;font-size:14px;line-height:1.45;text-align:center;font-weight:700;height:58px;flex-direction:column;display:flex;align-items:center;justify-content:center}
#s06 .pg{position:relative;height:216px;background-size:252px auto;background-repeat:no-repeat;background-position:center 16px}
#s06 .ln{position:absolute;border-top:2px dashed var(--ink);height:0}
#s06 .pgc{position:absolute;left:64px;top:15px;width:254px;height:186px;border:1.5px solid #cfc6b8;box-shadow:0 4px 12px rgba(30,27,25,.16);border-radius:2px}
#s06 .lb{position:absolute;width:62px;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:11.5px;font-weight:700;line-height:1.25;text-align:center;letter-spacing:-.02em}
#s06 .lb b{width:22px;height:22px;border:2px solid var(--ink);border-radius:50%;background:var(--or);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px}
/* s09 */
#s09 .pn{margin-top:22px;padding:18px 18px 10px}
#s09 .tt{display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px solid var(--ink);padding-bottom:10px}
#s09 .tt .a{font-family:LH;font-size:24px}#s09 .tt .b{font-size:11px;color:#7a716a}
#s09 dl{display:grid;grid-template-columns:76px 1fr}
#s09 dt,#s09 dd{padding:11px 0;border-bottom:2px dashed #d9d0c3;font-size:14px;line-height:1.55}
#s09 dt{color:var(--or);font-weight:700}
#s09 dl>*:nth-last-child(-n+2){border-bottom:none}
#s09 .seal{position:absolute;right:-14px;bottom:-24px}
/* s10 */
#s10 .pn{margin-top:22px}
#s10 .pic{height:213px}
#s10 .chips{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid var(--ink)}
#s10 .chips div{text-align:center;padding:10px 0 11px;font-family:LH;font-size:18px;border-left:3px solid var(--ink)}
#s10 .chips div:first-child{border-left:none}
#s10 .chips i{display:block;width:30px;height:12px;margin:0 auto 6px;border:2px solid var(--ink);border-radius:3px}
/* s11 */
#s11 .pn{margin-top:22px}
#s11 .pic{height:300px}
#s11 table{width:100%;border-collapse:collapse}
#s11 td{padding:11px 14px;border-top:2px dashed #d9d0c3;font-size:14px;line-height:1.5}
#s11 td:first-child{width:76px;color:var(--or);font-weight:700}
#s11 tr:first-child td{border-top:3px solid var(--ink)}
/* s12 */
#s12 .pn{transform:rotate(-1deg)}
#s12 .pic{height:420px}
#s12 .say{left:16px;top:18px;font-size:22px;max-width:300px}
#s12 .end{position:absolute;right:14px;bottom:14px;z-index:3;background:var(--yl);border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);padding:5px 12px 7px;font-size:16px;transform:rotate(4deg)}
#s12 .end .en{font-size:11px;letter-spacing:.2em;display:block}
'''

def s03():
    h = '''<section id="s03"><div class="eb">誰適合幹話曆？</div>
<h2>聖誕禮物 x 交換禮物<br><span class="u">送一個讓人笑出來的禮物</span></h2>''' + burst('笑一下<br>再出門')
    for x, l in zip(P, L):
        h += f'''<div class="pn" style="transform:rotate({l['rot']}deg)">
<div class="tag lh"><small>NO.{x['n']}</small>{x['who']}</div>
<div class="pic" style="background-image:url(img/{x['img']}.jpg)">{speed_lines(*l['c'])}
<div class="say lh" style="{l['say']}" data-t="{l['tail']}">{x['h']}</div>
<img class="card" src="img/{x['pg']}.jpg" style="{l['card']}">
<div class="stk" style="{l['stk'][1]}">{l['stk'][0]}</div></div>
<div class="nar">{x['s']}</div></div>'''
    return h + '</section>'

def s03b():
    sp = ''.join(f'<i class="sp" style="left:{x}%;top:{y}%;animation-delay:{d}s"></i>' for x, y, d in
                 [(8, 18, 0), (90, 22, .5), (93, 74, 1.0), (6, 78, 1.5), (50, 8, 2.0)])
    return f'<section id="s03b"><div class="xm"><div class="sh"></div>{sp}<div class="en sm">CHRISTMAS DELIVERY</div><div class="big">聖誕節前到貨</div></div></section>'

GIFT_CHIPS = json.load(open(f'{D}/gif/caps_g_box.json'))[0] if os.path.exists(f'{D}/gif/caps_g_box.json') else ''

def s03c():
    return f'''<section id="s03c"><div class="eb">送禮範例</div>
<h2>還沒拆開，<br><span class="u">外盒就先讓人笑了</span></h2>
<div class="lead">三款外盒，三種小白表情，<br>盒子就很精美，送禮直接加分。</div>
<div class="pn" style="transform:rotate(-1deg)">
<div class="tag lh"><small>GIFT BOX</small>三色禮盒</div>
<div class="pic gb" data-clip="g_box" style="background-image:url(gif/clips/g_box/001.jpg)"></div>
<div class="gbst">{burst('超可愛！', 112, 86, '#F6D34A', 6, 21)}</div>
<div class="chips" data-caps="g_box">{GIFT_CHIPS}</div>
<div class="nar">外盒跟底座同色，<mark>挑一個顏色就能送</mark>。</div></div></section>
<section id="s03d"><div class="pn" style="transform:rotate(1deg)">
<div class="tag lh"><small>EXAMPLE</small>交換禮物</div>
<div class="pic gf" style="background-image:url(img/gift.jpg)">{speed_lines(235, 235, 56, (170, 210))}
<div class="say lh" style="right:10px;top:26px" data-t="left:22px">交換禮物，<br>我就帶這盒！</div>
<div class="stk" style="left:14px;bottom:150px;transform:rotate(-10deg)">♡</div></div>
<div class="nar">拆開前先笑一次，翻開幹話<mark>再笑一次</mark>。</div></div></section>'''

def s04():
    return '''<section id="s04"><div><div class="n">365</div><div class="c">句厭世幹話</div></div>
<div><div class="n">365</div><div class="c">隻手繪小白</div></div>
<div><div class="n">3<small>色</small></div><div class="c">三角摺立底座</div></div></section>'''

def s05():
    random.seed(5)
    imgs = ''
    k = 1
    for r in range(7):
        for c in range(4):
            if k > 44: break
            x = c * 100 - 8 + (r % 2) * 22 + random.uniform(-6, 6)
            y = r * 68 - 14 + random.uniform(-5, 5)
            imgs += f'<img src="img/wall/{k:03d}.jpg" style="left:{x:.0f}px;top:{y:.0f}px;transform:rotate({random.uniform(-7,7):.1f}deg)">'
            k += 1
    return f'''<section id="s05"><div class="eb">從元旦到跨年</div>
<h2>365 天，<br><span class="u">天天都有一句幹話</span></h2>
<div class="lead">每一頁都是新的厭世金句，<br>再配一隻手繪小白陪你演。</div>
<div style="position:relative"><div class="pn"><div class="wall">{imgs}</div></div><div class="stk lh">不重複！</div></div></section>'''

def how(n, sid, h, d, clip, cn, ee, sfx, sfx_pos):
    return f'''<section id="{sid}" class="how"><div class="hd"><span class="no en">HOW TO USE {n:02d}</span>
<h3>{h}</h3><p class="d">{d}</p></div>
<div class="pn"><div class="ph" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div>
<div class="sfx" style="{sfx_pos}">{sfx}</div>
<div class="bar"><span class="st en">STEP {n:02d}</span><span class="cn lh">{cn}</span><span class="ee en">{ee}</span></div></div></section>'''

def s06():
    caps = json.load(open(f'{D}/gif/caps_g_days.json'))
    return f'''<section id="s06"><div class="eb">一頁有什麼？</div>
<h2>一頁一句，<br><span class="u">每天換一種厭世</span></h2>
<div class="pn"><div class="cap" data-caps="g_days">{caps[0]}</div>
<div class="pg" data-clip="g_days" style="background-image:url(gif/clips/g_days/001.jpg)">
<span class="lb" style="left:0;top:22px"><b>1</b>日期</span><i class="ln" style="left:56px;width:24px;top:42px"></i>
<span class="lb" style="right:0;top:18px"><b>2</b>農曆與節氣</span><i class="ln" style="right:56px;width:22px;top:38px"></i>
<span class="lb" style="left:0;top:76px"><b>3</b>手繪小白</span><i class="ln" style="left:56px;width:40px;top:96px"></i><i class="pgc"></i></div></div></section>'''

def s09():
    rows = [('成分', '365 句幹話、365 隻手繪小白、農曆節氣'),
            ('適應症', '週一症候群、開會前焦慮、選禮物困難'),
            ('用法用量', '每日一次，早上撕一頁；必要時傳給同事'),
            ('副作用', '上班笑出聲、被隔壁同事借走不還'),
            ('注意事項', '請勿放在老闆看得到的地方'),
            ('保存方式', '辦公桌上，伸手撕得到的地方')]
    dl = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in rows)
    return f'''<section id="s09"><div class="eb">本品為日曆，不是藥</div>
<h2>上班前，<br><span class="u">請先服用一頁</span></h2>
<div class="pn" style="transform:rotate(-.6deg)"><div class="tt"><span class="a">幹話日曆 2027</span><span class="b">使用說明書｜請詳閱後再上班</span></div>
<dl>{dl}</dl><div class="seal">{burst('每日<br>一頁', 110, 86, '#F6D34A', 8, 19)}</div></div></section>'''

def s10():
    return f'''<section id="s10"><div class="eb">底座款式</div>
<h2>三種顏色，<br><span class="u">三種上班心情</span></h2>
<div class="pn"><div class="pic" style="background-image:url(img/s10.jpg)">{speed_lines(200, 230, 48, (170, 200))}</div>
<div class="chips"><div><i style="background:#A9CBE6"></i>放空天藍</div><div><i style="background:#9C918A"></i>看開卡其</div><div><i style="background:#9DD8D2"></i>摸魚薄荷</div></div></div></section>'''

def s11():
    rows = [('尺寸', '14 × 10 公分，橫式手撕'), ('內容', '365 頁，每頁一句幹話＋手繪小白＋農曆'),
            ('底座', '三角摺立，不用另外買架子'), ('重量', '623 g（含外盒 918 g）')]
    tr = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows)
    return f'''<section id="s11"><div class="eb">規格</div>
<h2>小小一本，<br><span class="u">桌上剛剛好</span></h2>
<div class="pn" style="transform:rotate(.6deg)"><div class="pic" style="background-image:url(img/s11.jpg)"></div><table>{tr}</table></div></section>'''

def s12():
    return '''<section id="s12" style="padding-bottom:48px"><div class="pn"><div class="pic" style="background-image:url(img/s12.jpg)">
<div class="say lh" data-t="left:30px">日子不一定會變好，<br>但每天可以先笑一下。</div>
<div class="end lh"><span class="en">TO BE CONTINUED</span>明天還有一句</div></div></div></section>'''

def build():
    body = (s03() + s03b() + s03c() + s04() + s05()
        + how(1, 's05a', '早上撕一頁，<br>先笑完再上班', '撕下今天這頁，一句幹話配一隻小白，<br>比咖啡還提神。', 'g_tear', '撕下今天', 'TEAR', burst('嘶～', 96, 74, '#fff', -8, 22), 'right:-10px;top:-26px')
        + s06()
        + how(2, 's06a', '好笑的那句，<br>貼到同事的螢幕上', '好笑不要獨享，<br>讓整個辦公室一起笑。', 'g_share', '分享同事', 'SHARE', burst('貼！', 96, 74, '#F6D34A', 6, 24), 'left:-12px;top:-26px')
        + how(3, 's07', '撕下來的每一頁，<br>貼成你的幹話牆', '一天一張，貼滿一整面，<br>這一年有多厭世，一看就知道。', 'g_wall', '貼成幹話牆', 'COLLECT', burst('啪！', 96, 74, '#fff', -6, 24), 'right:-10px;top:-26px')
        + how(4, 's08', '放在玄關，<br>每天都笑著出門！', '365 句不重複，<br>每天都在期待下一句。', 'g_flip', '笑到黑姑', 'LOL', burst('哈哈哈', 104, 80, '#F6D34A', 6, 19), 'left:-12px;top:-26px')
        + s09() + s10() + s11() + s12())
    js = '''<script>document.querySelectorAll('.say[data-t]').forEach((e,i)=>{const c='t'+i;e.classList.add(c);const s=document.createElement('style');s.textContent=`.${c}:after{${e.dataset.t}}`;document.head.appendChild(s)})</script>'''
    html = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=432"><title>幹話曆落地頁 v13</title><style>{CSS}</style></head><body>{body}{js}</body></html>'
    open(f'{D}/page.html', 'w').write(html)
    print('ok')

if __name__ == '__main__':
    build()
