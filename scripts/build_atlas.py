from pathlib import Path
import math, json

ROOT=Path(__file__).resolve().parents[1]/'references'
OUT=ROOT/'structure'
OUT.mkdir(exist_ok=True)
COLORS=['#4e747b','#638890','#78999d','#517980','#658b91','#88a7a9']

def feather(x,y,tx,ty,width=12,bend=0,i=0):
    dx,dy=tx-x,ty-y; length=math.hypot(dx,dy); nx,ny=-dy/length,dx/length
    def p(t,w=0):
        off=math.sin(t*math.pi)*bend+w
        return (x+dx*t+nx*off,y+dy*t+ny*off)
    # Filled asymmetric vane, staggered edge notches; no paired eye frames.
    pts=[p(0,-width*.5),p(.27,-width*.72),p(.53,-width*.48),p(.58,-width*.32),p(.65,-width*.4),p(.82,-width*.2),(tx,ty),p(.77,width*.34),p(.72,width*.22),p(.59,width*.52),p(.38,width*.76),p(0,width*.55)]
    poly=' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)
    a,b=p(.22),p(.65)
    return f'<polygon points="{poly}" fill="{COLORS[i%len(COLORS)]}"/><path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="#aec3c2" stroke-width=".65" opacity=".7"/>'

def ornament(x,y,small=False):
    s=.65 if small else 1
    return f'''<g transform="translate({x} {y}) scale({s})" fill="#b77757" stroke="#8b563d" stroke-width=".8"><path d="M0,-12 Q-14,-15 -13,-4 L-4,7 L0,12 L5,5 L13,-5 Q11,-15 0,-12Z"/><path d="M-7,-8 L6,6 M6,-8 L-6,5" fill="none" stroke="#f1d9b6" stroke-width="2"/></g>'''

def head(quarter=False):
    if not quarter:
        return '''<path d="M154 234 L151 273 L122 285 L236 285 L208 272 L204 234" fill="#e5d4c6"/>
<ellipse cx="180" cy="158" rx="72" ry="102" fill="#eee2d6" stroke="#c9b8aa"/>
<path d="M110 132 Q92 58 179 43 Q266 52 251 133 Q245 75 185 74 Q132 67 110 132" fill="#d9d4cd"/>
<path d="M179 160 L172 187 Q180 192 187 186 M164 212 Q181 220 196 211" fill="none" stroke="#bb9f8c" stroke-width="2"/>
<path d="M110 141 Q90 133 104 175 M250 141 Q269 133 255 175" fill="none" stroke="#c9b8aa" stroke-width="4"/>'''
    return '''<path d="M163 235 L155 274 L133 285 L239 285 L216 267 L215 228" fill="#e5d4c6"/>
<path d="M179 55 C232 45 265 87 256 151 C260 204 221 253 179 256 Q156 245 147 217 L143 197 L122 188 L143 171 Q126 111 151 74Z" fill="#eee2d6" stroke="#c9b8aa"/>
<path d="M147 129 Q132 76 163 55 Q221 31 251 90 L258 151 Q241 100 203 88 Q166 73 147 129" fill="#d9d4cd"/>
<path d="M224 146 Q252 131 241 176 L229 184" fill="#e5d4c6" stroke="#c9b8aa"/>
<path d="M147 217 Q159 221 174 213" fill="none" stroke="#bb9f8c" stroke-width="2"/>'''

def guides(quarter=False):
    x,w=(133,88) if quarter else (119,122)
    return f'<g class="guide"><rect x="{x}" y="132" width="{w}" height="30" rx="6" fill="none" stroke="#d76c61" stroke-dasharray="4 4"/><text x="180" y="315" text-anchor="middle" fill="#a7544d" font-size="11">虚线：需被覆盖的区域，非成品纹样</text></g>'

def coverage(quarter=False,side=False):
    s=''
    if side:
        for row in range(2):
            for i,x in enumerate([230,209,188,167] if quarter else [248,223,198,173]):
                s+=feather(x,140+row*14,x-(45 if quarter else 62),139+row*15,18,-2,i+row)
    elif quarter:
        for row in range(2):
            for i in range(3):
                s+=feather(154-i*5,140+row*14,130-i*4,137+row*15,18,-1,i+row)
                s+=feather(154+i*15,140+row*14,208+i*11,137+row*15,18,2,i+row)
    else:
        for row in range(2):
            for sign in [-1,1]:
                for i in range(3):s+=feather(180+sign*i*14,140+row*14,180+sign*(59+i*8),137+row*15,18,sign*2,i+row)
    return s

def wings(form,quarter=False):
    s=''
    if quarter:
        # Far wing foreshortened; near wing follows temple, not a mirrored front overlay.
        for i in range(4):
            ends={'closed':(104-i*3,139+i*5),'open':(102-i*2,110+i*12),'draped':(116-i*2,168+i*9),'wrap':(125-i*2,138+i*4)}
            tx,ty=ends[form];s+=feather(156,142+i*4,tx,ty,10,0,i)
        for i in range(5):
            ends={'closed':(284-i*9,137+i*6),'open':(278-i*6,88+i*19),'draped':(268-i*6,179+i*12),'wrap':(260-i*2,151+i*8)}
            tx,ty=ends[form];s+=feather(207+i*2,141+i*3,tx,ty,13,9 if form in ['wrap','draped'] else 0,i)
    else:
        for sign in [-1,1]:
            for i in range(5):
                ends={'closed':(112-i*9,-11+i*7),'open':(92+i*5,-58+i*18),'draped':(87+i*3,25+i*11),'wrap':(76+i*2,2+i*7)}
                ex,ey=ends[form]
                s+=feather(180+sign*(35+i*3),142+i*3,180+sign*ex,142+ey,13,(8 if form=='draped' else 0)*sign,i)
    return s

def side_extra(n,quarter):
    # Draw only the defining extra path; common coverage is separately layered above it.
    s='';start=(225,143) if quarter else (245,143)
    if n=='02':
        for i in range(4):s+=feather(start[0],171-i*5,123-i*5 if not quarter else 131-i*4,126-i*3,18,0,i)
    elif n=='05':
        for i in range(3):
            s+=feather(*start,103-i*7,113+i*5,15,0,i)
            s+=feather(*start,108-i*8,170+i*5,16,0,i+2)
    elif n=='08':
        for i in range(4):s+=feather(217+i*4,85+i*6,155-i*9,150,18,-10,i)
    elif n in ['06','09']:
        for i in range(4):s+=feather(*start,263-i*2,164+i*8,13,10,i)
    return s

def diagram(form,quarter=False,n=None):
    s=head(quarter)
    # Thin dotted support is instructional only; outside or behind the ornament.
    s+='<g class="guide"><path d="M112 129 Q180 115 248 130" fill="none" stroke="#a78e72" stroke-width="2" stroke-dasharray="3 5"/></g>'
    if n:
        # Side-source ends mostly on the far side; avoid two equal fan centers.
        for i in range(5):
            ex={'closed':91+i*8,'open':95+i*4,'draped':99+i*3,'wrap':115+i*2}[form]
            ey={'closed':137+i*5,'open':103+i*13,'draped':165+i*11,'wrap':146+i*5}[form]
            if quarter:ex+=16
            s+=feather(202,145+i*2,ex,ey,14, -7 if form=='draped' else 0,i)
        s+=side_extra(n,quarter)
    else:s+=wings(form,quarter)
    s+=coverage(quarter,side=bool(n))
    if n:
        ox,oy=((226,148) if quarter else (246,148))
        if n=='02':oy=174
        if n=='08':ox,oy=225,89
        if n=='09':ox,oy=(249,171) if quarter else (258,164)
        s+=ornament(ox,oy)
        if n=='07':s+=ornament(133 if quarter else 110,151,True)
    else:s+=ornament(155 if quarter else 180,140)
    s+=guides(quarter)
    return s

def topview():
    s='<ellipse cx="180" cy="173" rx="67" ry="83" fill="#eee2d6" stroke="#c9b8aa"/><path d="M170 94 L180 81 L190 94" fill="#eee2d6" stroke="#c9b8aa"/>'
    for sign in [-1,1]:
        for i in range(5):s+=feather(180+sign*(22+i*8),91+i*3,180+sign*(77-i*2),158+i*13,14,sign*-15,i)
        for i in range(3):s+=feather(180+sign*4,89,180+sign*(44+i*9),103+i*5,17,sign*-4,i)
    s+=ornament(180,88)
    s+='<text x="180" y="56" text-anchor="middle" font-size="12" fill="#7a7166">鼻尖／正面</text><text x="180" y="282" text-anchor="middle" font-size="12" fill="#7a7166">后脑方向</text>'
    return s

def detail():
    s='<text x="180" y="73" text-anchor="middle" font-size="13" fill="#657276">多枚羽面交错，中央饰品跨接</text>'
    for row in range(2):
        for sign in [-1,1]:
            for i in range(3):s+=feather(180+sign*i*17,140+row*20,180+sign*(66+i*14),133+row*22,24,sign*3,i+row)
    s+=ornament(180,145)
    s+='<g class="guide"><path d="M87 201 L270 201" stroke="#a78e72" stroke-dasharray="4 5"/><text x="180" y="226" text-anchor="middle" font-size="12" fill="#7a7166">隐藏承托与可见饰品分工不同</text></g>'
    return s

items=[('closed','中央连接 · 收束','横向顺叠，低张角；保留渐细外延。',None),('open','中央连接 · 开羽','外端增大张角，覆盖与中央饰品保持。',None),('draped','中央连接 · 垂羽','脸侧连续下弯，鼻尖与嘴唇露出。',None),('wrap','中央连接 · 环覆','沿太阳穴向后包覆；俯视用于解释弧向长度。',None)]
defs=[('01','closed','水平跨面，远端渐细'),('02','closed','低位起始，向对侧眉上斜行'),('03','draped','跨面后下弯：垂羽预设'),('04','open','跨面后上扬：开羽预设'),('05','open','上下分流，中间仍有羽面覆盖'),('06','wrap','主流跨面＋短辅流回折耳后'),('07','closed','主连接＋较小辅助固定'),('08','closed','冠侧下降进入眼区'),('09','wrap','耳后绕太阳穴向前覆盖')]
for n,f,d in defs: items.append((f,'旧布局 '+n,d,n))
records=[]
for f,title,desc,n in items:
    key='layout-'+n if n else 'centered-'+f
    last=topview() if f=='wrap' and not n else detail()
    if n:
        # Compact textual third panel avoids inventing a second geometry source.
        last=f'<text x="34" y="100" font-size="18" fill="#314b50">{title}</text><text x="34" y="135" font-size="13" fill="#657276">侧部起点 ≠ 中央连接饰品</text><text x="34" y="164" font-size="13" fill="#657276">仅在明确选择侧源时使用</text><text x="34" y="207" font-size="13" fill="#657276">编号是兼容预设，不是独立维度</text><text x="34" y="237" font-size="13" fill="#657276">形态兼容性请同时读取文字表</text>'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="470" viewBox="0 0 1080 470" role="img" aria-label="{title}结构示意"><style>text{{font-family:'Microsoft YaHei',sans-serif}}.hide-guides .guide{{display:none}}</style><rect width="1080" height="470" fill="#faf8f3"/><text x="30" y="38" font-size="24" fill="#243d42">{title}</text><text x="30" y="65" font-size="14" fill="#657276">{desc}</text><g transform="translate(0 86)">{diagram(f,False,n)}</g><g transform="translate(360 86)">{diagram(f,True,n)}</g><g transform="translate(720 86)">{last}</g><text x="180" y="429" text-anchor="middle" font-size="14" fill="#314b50">正面</text><text x="540" y="429" text-anchor="middle" font-size="14" fill="#314b50">斜侧示意 · 远侧缩短</text><text x="900" y="429" text-anchor="middle" font-size="14" fill="#314b50">{'俯视 · 环覆路径' if f=='wrap' and not n else '部件关系'}</text><text x="30" y="455" font-size="11" fill="#8b8073">结构草图 · 非已验证成图 · 配色、饰品款式、羽片数量仅为示意</text></svg>'''
    (OUT/(key+'.svg')).write_text(svg,encoding='utf-8')
    records.append(dict(key=key,title=title,desc=desc,kind='side' if n else 'base',svg=svg))

cards=''.join(f'<article data-kind="{r["kind"]}" id="{r["key"]}">{r["svg"]}<footer><a href="structure/{r["key"]}.svg" download>SVG 原图</a><a href="structure/{r["key"]}.png" download>PNG 副本</a></footer></article>' for r in records)
html='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>眼羽结构参考 · 中央连接与侧源扩展</title><style>
*{box-sizing:border-box}body{margin:0;background:#eeece6;color:#243d42;font-family:'Microsoft YaHei',sans-serif}main{max-width:1180px;margin:auto;padding:36px 24px}h1{font-size:30px;margin:0 0 12px}p{line-height:1.8;color:#59696b}.badge{font-size:12px;letter-spacing:2px;color:#866c50}nav{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0}button{font:inherit;border:1px solid #9aadae;border-radius:8px;background:#faf8f3;color:#314b50;padding:10px 16px;cursor:pointer}button[aria-pressed=true]{background:#314b50;color:white}button:focus-visible,a:focus-visible{outline:3px solid #b77757;outline-offset:3px}article{background:#faf8f3;border:1px solid #d4d9d4;border-radius:12px;overflow:hidden;margin:18px 0}article svg{width:100%;height:auto;display:block}footer{padding:12px 26px;display:flex;gap:24px;border-top:1px solid #e1e1d8}a{color:#476c76}aside{padding:20px;border-left:4px solid #b77757;background:#faf8f3;line-height:1.8}.hide-guides .guide{display:none}article[hidden]{display:none}small{color:#687878}@media(max-width:600px){main{padding:22px 10px}h1{font-size:23px}article{overflow-x:auto}article svg{min-width:760px}nav{gap:6px}button{padding:9px;font-size:13px}}@media print{nav,footer{display:none}article{break-inside:avoid}main{padding:0}}
</style><main><div class="badge">YUMAO / STRUCTURE STUDIES</div><h1>先看中央连接，再看侧源扩展</h1><p>低保真结构参考：比较同一头模上的羽流、连接与连续覆盖。图中颜色、饰品款式和数量不作为固定模板。<br>正面与斜侧为二维示意，环覆另给俯视；不代表实测三维模型或真实生图成功。</p><nav aria-label="参考分类"><button data-filter="base" aria-pressed="true">中央连接四形态</button><button data-filter="side" aria-pressed="false">侧源旧预设 01–09</button><button data-filter="all" aria-pressed="false">全部比较</button><button id="guides" aria-pressed="true">辅助标注：显示</button></nav><aside>蓝绿色：多枚羽片与连续覆盖；赭色：可见连接饰品；虚线：教学定位与隐藏承托。<br>默认中央饰品连接左右羽组；侧部装饰起点只属于明确选择的侧源方案。教学辅助线不属于最终作品。</aside>'''+cards+'''<aside id="legacy10"><strong>旧布局10已归回材料探索</strong><br>它没有独有的空间路径，不再绘制“第十种布局”误导使用者。天然羽、金属、织物、琉璃或元素均可用于中央连接及适配的侧源方案。旧10输入的兼容处理见文字表。</aside><p><a href="form-family.md">唯一构造定义</a> · <a href="side-origin-layouts.md">布局兼容表</a> · <a href="feather-form-reference.md">真实参考证据范围</a></p><small>本页不加载外部字体、脚本或网络资源。给生图工具使用时只选择目标项，排除辅助标注与无关预设。</small></main><script>
const buttons=[...document.querySelectorAll('[data-filter]')];function filter(kind){buttons.forEach(b=>b.setAttribute('aria-pressed',b.dataset.filter===kind));document.querySelectorAll('article').forEach(a=>a.hidden=kind!=='all'&&a.dataset.kind!==kind);document.getElementById('legacy10').hidden=kind==='base'}buttons.forEach(b=>b.onclick=()=>filter(b.dataset.filter));filter('base');document.getElementById('guides').onclick=function(){const hidden=document.body.classList.toggle('hide-guides');this.setAttribute('aria-pressed',!hidden);this.textContent='辅助标注：'+(hidden?'隐藏':'显示')};
</script></html>'''
(ROOT/'structure-atlas.html').write_text(html,encoding='utf-8')
(OUT/'index.json').write_text(json.dumps([{k:v for k,v in r.items() if k!='svg'} for r in records],ensure_ascii=False,indent=2),encoding='utf-8')
print('Built',len(records),'SVG diagrams and standalone HTML')
