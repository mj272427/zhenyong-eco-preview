# -*- coding: utf-8 -*-
# 振勇環保 新站 — 多頁式產生器（沉穩藍＋亮綠）
import os
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- SVG ----------
S = {
 'phone':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 'line':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 5.79 2 10.45c0 4.19 3.54 7.7 8.32 8.37.32.07.76.21.87.49.1.25.07.64.03.9l-.14.85c-.04.25-.2.98.86.53s5.7-3.36 7.78-5.75C21.36 14.66 22 12.68 22 10.45 22 5.79 17.52 2 12 2z"/></svg>',
 'logo':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 19a4 4 0 0 1-4-4c0-1.5.8-2.8 2-3.5"/><path d="M12 4a4 4 0 0 1 3.5 2l1 1.7"/><path d="m9 8 3-4 3 4"/><path d="M17.5 9.5 21 15a4 4 0 0 1-3.5 6H10"/><path d="m13 21 2-3-3.5-.5"/></svg>',
 'menu':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
 'check':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
 'star':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 2 2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.5-4.8 2.5.9-5.4-3.9-3.8 5.4-.8z"/></svg>',
 'shield':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 4 6v6c0 5 3.4 8.5 8 10 4.6-1.5 8-5 8-10V6z"/><path d="m9 12 2 2 4-4"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-5.2-7-11a7 7 0 0 1 14 0c0 5.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 'pin2':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 'mail':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 'gov':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M9 9h.01M15 9h.01M9 13h.01M15 13h.01M9 17h.01M15 17h.01"/></svg>',
 'bell':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>',
 'caret':'<svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="m6 9 6 6 6-6"/></svg>',
 'arrow':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" width="16" height="16"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}
def sv(paths):  # service icon wrapper
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+paths+'</svg>'

# ---------- 9 大服務 ----------
SERVICES = [
 (sv('<path d="M1 3h15v13H1z"/><path d="M16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>'),'廢棄物清運','一般無害性廢棄物依法清運，家庭、學校到商業空間皆可。',['國中小學廢棄教室清運','垃圾清運']),
 (sv('<path d="M14 2 3 13l3 3L17 5z"/><path d="m14 2 4 4"/><path d="M5 21h14"/><path d="M9 21v-3l4-4"/>'),'拆除清運','隔間、裝潢打除、店面復原到廠房拆除，拆完連廢料一併清走。',['居家拆除清運','電視台拆除清運','廠房拆除清運']),
 (sv('<path d="M3 21V9l6-4 6 4v12"/><path d="M15 21V13l6-4v12"/><path d="M3 21h18"/><path d="M7 13h.01M7 17h.01"/>'),'廠房拆除清運','工廠設備、機具與廠區整體拆除清運，一條龍處理到淨空。',['設備機具','廠區淨空']),
 (sv('<path d="M7 19a4 4 0 0 1-2-7.5"/><path d="m9 8 3-4 3 4"/><path d="M17 9.5 21 15a4 4 0 0 1-3.5 6H10"/><path d="m13 21 2-3-3.5-.5"/>'),'資源回收','紙類、金屬、廢五金、廢家電分類回收，讓資源循環再利用。',['紙類金屬','廢家電']),
 (sv('<path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v3"/><path d="M4 15h16"/><path d="M8 18v3M12 18v3M16 18v3"/>'),'文件銷毀','機密文件、帳冊安全銷毀，可配合政府與企業之保密需求。',['機密文件','可出證明']),
 (sv('<path d="M21 8 12 3 3 8l9 5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/>'),'過期品／食品報廢','過期食品、下架商品合法銷毀報廢，海關與食品業皆有實績。',['食品銷燬','海關報廢']),
 (sv('<path d="M12 2v4"/><path d="M8 6h8l1 4H7z"/><path d="M7 10v8a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-8"/><path d="M11 14h2"/>'),'環境消毒','清運後環境消毒，維護場域衛生與安全，讓空間安心使用。',['場域消毒','清運後處理']),
 (sv('<path d="M3 4h11v11H3z"/><path d="M14 8h4l3 3v4h-7z"/><circle cx="6.5" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/><path d="M6 7h5M6 10h5"/>'),'垃圾車清運','大型垃圾車機動調度，量大、急件也能快速到場處理。',['大型量體','機動調度']),
 (sv('<path d="M4 21V7l8-4 8 4v14"/><path d="M9 21v-6h6v6"/><path d="M9 3v4M15 3v4"/><circle cx="12" cy="11" r="1"/>'),'活動拆除作業','路跑、燈會、演唱會等大型活動的現場清運與拆除維護。',['路跑清運','燈會拆除','演唱會維護']),
]
def svc_card(item):
    ic,title,desc,tags = item
    lis=''.join('<li>%s</li>'%t for t in tags)
    return '<div class="svc"><span class="ic">%s</span><h3>%s</h3><p>%s</p><ul>%s</ul></div>'%(ic,title,desc,lis)

# ---------- 實績相簿（放一個資料夾＝一本相簿，資料夾名＝相簿名） ----------
import re, shutil
IMG_EXT={'.jpg','.jpeg','.png','.webp','.gif'}
ALBUMS_DIR=os.path.join(HERE,'albums')

def load_albums():
    out=[]
    if not os.path.isdir(ALBUMS_DIR): return out
    for name in sorted(os.listdir(ALBUMS_DIR), reverse=True):
        d=os.path.join(ALBUMS_DIR,name)
        if not os.path.isdir(d) or name.startswith('.'): continue
        photos=sorted(f for f in os.listdir(d) if os.path.splitext(f)[1].lower() in IMG_EXT)
        if not photos: continue
        m=re.match(r'^(\d{4})-(\d{2})[_\-](.+)$', name)
        date,title = ('%s.%s'%(m.group(1),m.group(2)), m.group(3)) if m else ('', name)
        out.append({'folder':name,'title':title,'date':date,'photos':photos})
    return out

def album_section(a):
    tiles=''.join('<a class="ph" href="albums/%s/%s" target="_blank" rel="noopener">'
                  '<img src="albums/%s/%s" alt="%s" loading="lazy"></a>'
                  %(a['folder'],p,a['folder'],p,a['title']) for p in a['photos'])
    date='<span class="al-date num">%s</span>'%a['date'] if a['date'] else ''
    return ('<section class="album"><div class="al-head"><h3>%s</h3>'
            '<span class="al-meta">%s<span class="al-cnt">%d 張</span></span></div>'
            '<div class="ph-grid">%s</div></section>')%(a['title'],date,len(a['photos']),tiles)

def albums_html():
    al=load_albums()
    if not al:
        return '<p style="text-align:center;color:var(--ink-faint)">相簿建置中。</p>'
    return ''.join(album_section(a) for a in al)

# ---------- 報價流程 ----------
def process():
    steps=[
     ('STEP 01', sv('<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>'),'拍照傳 LINE','把要清運或拆除的東西拍給我們，或直接來電說明狀況與地點。'),
     ('STEP 02', sv('<path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/><circle cx="12" cy="12" r="4"/>'),'免費回覆估價','依垃圾種類、材積車趟、樓層有無電梯評估，給你清楚的價格。'),
     ('STEP 03', sv('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><path d="m9 10 2 2 4-4"/>'),'約時間到場清運','談妥後約定時間，團隊準時到場，一次清乾淨、依法分類處理。'),
    ]
    inner=''.join('<div class="step"><div class="n">%s</div><div class="si">%s</div><h3>%s</h3><p>%s</p></div>'%s for s in steps)
    return ('<div class="sec-head"><span class="eyebrow">報價流程</span>'
            '<h2 class="title" style="color:#fff">三步驟，就知道要花多少</h2>'
            '<p class="lede">最怕被亂喊價？振勇報價公開透明——拍張照片傳過來，馬上給你估價。</p></div>'
            '<div class="steps">'+inner+'</div>'
            '<div class="process-cta"><a href="tel:0222910883" class="btn btn-call">%s現在就來電估價</a>'
            '<a href="contact.html" class="btn btn-line">%s用 LINE 傳照片</a></div>')%(S['phone'],S['line'])

# ---------- FAQ ----------
FAQS=[
 ('清一車大概多少錢？怎麼估價？','價格會依垃圾種類、數量材積（幾車趟）、樓層有無電梯、是否需要搬運而定。最快的方式是拍照傳 LINE 或直接來電，我們免費幫你估價，價格談妥、您確認後才進行。'),
 ('服務範圍到哪裡？','以五股為據點，服務新北與雙北一帶（五股、泰山、新莊、蘆洲、三重、林口等）。實際區域與距離歡迎來電確認。'),
 ('舊家具、家電、床墊可以一起清嗎？','可以。大型家具、家電、床墊、裝潢廢料都能一併處理，也能配合搬家、店面與辦公室整體淨空。'),
 ('你們是合法清運嗎？會不會亂倒？','是合法業者。本公司持乙級廢棄物處理技術員證照（新北市廢乙清字第 0093 號），並列入新北市環保局核定進廠之清除處理廠商，依法分類處理，絕不亂倒。'),
 ('拆除後的裝潢廢料你們會處理掉嗎？','會。拆除與清運一條龍，拆完的隔間、裝潢廢料會一併清走，還你一個乾淨可用的空間。'),
]
def faq():
    items=''
    for i,(q,a) in enumerate(FAQS):
        op=' open' if i==0 else ''
        items+='<details class="qa"%s><summary><span class="q">Q</span>%s%s</summary><div class="a">%s</div></details>'%(op,q,S['caret'],a)
    return '<div class="faq">'+items+'</div>'

# ---------- 導覽 ----------
NAV=[('index.html','首頁'),('about.html','關於我們'),('news.html','最新消息'),
     ('services.html','服務項目'),('works.html','實績介紹'),('location.html','交通位置'),('contact.html','聯絡我們')]
def header(active):
    links=''
    for href,label in NAV:
        cls=' class="active"' if href==active else ''
        links+='<a href="%s"%s>%s</a>'%(href,cls,label)
    return ('<div class="util"><div class="wrap"><span>合法清運 · 依法分類處理 · 絕不亂倒</span>'
            '<div class="util-r"><a href="tel:0222910883">%s(02)2291-0883</a>'
            '<a href="tel:0282956423">(02)8295-6423</a></div></div></div>'
            '<header class="nav"><div class="wrap">'
            '<a href="index.html" class="brand" aria-label="振勇環保有限公司"><span class="mark" aria-hidden="true">%s</span>'
            '<span>振勇環保<small>Zhen Yong Eco</small></span></a>'
            '<button class="burger" aria-label="開啟選單" aria-expanded="false" id="burger">%s</button>'
            '<nav class="menu" id="menu">%s'
            '<a href="contact.html" class="nav-cta">%s免費估價</a></nav></div></header>')%(S['phone'],S['logo'],S['menu'],links,S['phone'])

def footer():
    fnav=''.join('<a href="%s">%s</a>'%(h,l) for h,l in NAV[1:])
    return ('<footer><div class="wrap"><div class="cols">'
            '<div><h4>振勇環保有限公司</h4>'
            '<p>依法清運一般無害性廢棄物，以資源回收為核心。回收就是資源，不浪費、不丟棄，為地球盡一份心力。</p>'
            '<p style="margin-top:10px">乙級廢棄物處理技術員｜新北市廢乙清字第 0093 號<br>統一編號：54712081</p></div>'
            '<div><h4>網站導覽</h4><div class="fnav">%s</div></div>'
            '<div><h4>聯絡資訊</h4><p>新北市五股區民義路二段 23-9 號<br>'
            '<a href="tel:0222910883">(02)2291-0883</a>　<a href="tel:0282956423">(02)8295-6423</a><br>'
            '<a href="mailto:a0939516638@gmail.com">a0939516638@gmail.com</a><br>'
            '<a href="https://www.facebook.com/groups/635772690100613/" target="_blank" rel="noopener">Facebook 社團</a></p></div>'
            '</div><div class="legal"><span>© 2026 振勇環保有限公司　保留一切權利</span>'
            '<span>合法清運 · 依法分類處理 · 絕不亂倒</span></div></div></footer>')%fnav

def mobar():
    return ('<div class="mobar"><a href="tel:0222910883" class="m-call">%s撥打電話</a>'
            '<a href="contact.html" class="m-line">%s加 LINE 估價</a></div>')%(S['phone'],S['line'])

def page(active,title,desc,body):
    return ('<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s</title>\n<meta name="description" content="%s">\n'
            '<link rel="stylesheet" href="styles.css">\n</head>\n<body>\n'
            '%s\n%s\n%s\n%s\n<script src="main.js" defer></script>\n</body>\n</html>\n'
            )%(title,desc,header(active),body,footer(),mobar())

def page_hero(eyebrow,h1,p,crumb):
    return ('<section class="page-hero"><div class="wrap"><span class="eyebrow">%s</span>'
            '<h1>%s</h1><p>%s</p><div class="crumb"><a href="index.html">首頁</a> / %s</div></div></section>'
            )%(eyebrow,h1,p,crumb)

TITLE='振勇環保有限公司｜五股·雙北 廢棄物清運·拆除清運·資源回收'
DESC='振勇環保有限公司—五股在地合法清運業者。廢棄物清運、拆除清運、資源回收、文件銷毀、食品報廢、環境消毒。持乙級廢棄物處理技術員證照，新北市環保局核定清除處理廠商。'

# =================== 各頁內容 ===================
def home():
    hero=('<section class="hero"><div class="wrap"><div class="hero-main">'
          '<span class="eyebrow">五股 · 雙北　廢棄物清運 · 拆除清運 · 資源回收</span>'
          '<h1>一通電話，<br><span class="hl">垃圾變乾淨空間</span></h1>'
          '<p class="sub">振勇環保深耕五股在地，承接家庭、店面、廠房與活動現場的廢棄物清運、拆除與資源回收。合法業者、依法分類處理，服務範圍涵蓋雙北一帶，歡迎來電免費估價。</p>'
          '<div class="cta-row"><a href="tel:0222910883" class="btn btn-call">%s撥打電話</a>'
          '<a href="contact.html" class="btn btn-line">%s加 LINE 免費估價</a></div>'
          '<div class="chips"><span class="chip">%s乙級廢棄物處理技術員</span>'
          '<span class="chip">%s政府標案經驗</span><span class="chip">%s環保局核定清除廠商</span>'
          '<span class="chip">%s五股在地團隊</span></div></div>'
          '<aside class="hero-card"><h3>為什麼選振勇？</h3><div class="big">合法 · 準時 · 透明</div>'
          '<p>不亂喊價、不亂倒棄，一車清乾淨。</p><div class="stat-grid">'
          '<div class="stat"><b>免費</b><span>來電／到場估價</span></div>'
          '<div class="stat"><b>雙北</b><span>一帶皆可服務</span></div>'
          '<div class="stat"><b>9 大</b><span>清運拆除服務</span></div>'
          '<div class="stat"><b>依法</b><span>分類處理申報</span></div></div></aside></div></section>'
          )%(S['phone'],S['line'],S['check'],S['star'],S['shield'],S['pin'])
    svc_preview=('<section class="band band--tint"><div class="wrap"><div class="sec-head">'
          '<span class="eyebrow">服務項目</span><h2 class="title">從一件家具到整座廠房，我們都清得動</h2>'
          '<p class="lede">九大服務範圍，家庭、店面、辦公室、工廠到大型活動現場，一站處理。</p></div>'
          '<div class="svc-grid">'+''.join(svc_card(s) for s in SERVICES[:6])+'</div>'
          '<div style="margin-top:26px"><a href="services.html" class="btn btn-ghost">看全部 9 項服務 %s</a></div></div></section>'
          )%S['arrow']
    _pv=[(a['folder'],p,a['title']) for a in load_albums() for p in a['photos']]
    _tiles=''.join('<a class="ph" href="works.html"><img src="albums/%s/%s" alt="%s" loading="lazy"></a>'%(f,p,t) for f,p,t in _pv[:8])
    works_preview=('<section class="band band--tint" style="border-top:1px solid var(--line)"><div class="wrap"><div class="sec-head">'
          '<span class="eyebrow">實績介紹</span><h2 class="title">做過的案子，說明我們的能耐</h2>'
          '<p class="lede">從演唱會場館到海關食品銷毀、政府環境維護標案，實績會說話。</p></div>'
          '<div class="ph-grid" style="margin-top:24px">'+_tiles+'</div>'
          '<div style="margin-top:26px"><a href="works.html" class="btn btn-ghost">看更多實績 %s</a></div></div></section>'
          )%S['arrow']
    proc=('<section class="band band--dark"><div class="wrap">'+process()+'</div></section>')
    return page('index.html',TITLE,DESC,hero+svc_preview+works_preview+proc)

def about():
    body=page_hero('關於我們','回收就是資源，不浪費、不丟棄',
        '振勇環保深耕五股在地，秉持誠信經營、品質第一，依法為雙北一帶提供廢棄物清運與資源回收服務。','關於我們')
    body+=('<section class="band band--tint"><div class="wrap"><div class="about"><div>'
        '<p class="body">振勇環保有限公司，全力配合政府環保政策，依法清運一般無害性廢棄物。本公司以「垃圾經濟學」中「資源型回路」的角度出發，以再生的資源回收作為主要重點項目。</p>'
        '<p class="body">不論在收集或清運的過程中，皆秉持著小心、安全、衛生的理念來服務大眾。創業至今秉持「回收就是資源，不浪費、不丟棄」的原則，盡心為地球盡一份心力，以『誠信經營、品質第一』為經營守則，提升效率、追求卓越品質，使企業生命永續經營。</p>'
        '<div class="facts"><div class="fact"><b class="num">2014</b><span>公司設立</span></div>'
        '<div class="fact"><b class="num">9 大</b><span>清運拆除服務</span></div>'
        '<div class="fact"><b>雙北</b><span>服務範圍</span></div></div></div>'
        '<div class="about-right"><figure class="about-photo">'
        '<img src="img/customs.jpg" alt="振勇清運車依法進入垃圾焚化廠處理廢棄物" loading="lazy">'
        '<figcaption>清運車依法進廠處理，合法分類、絕不亂倒</figcaption></figure>'
        '<div class="cert-card">'
        '<div class="cert-row"><span class="ic">%s</span><div><b>乙級廢棄物處理技術員</b><span>證號：新北市廢乙清字第 0093 號</span></div></div>'
        '<div class="cert-row"><span class="ic">%s</span><div><b>政府標案指定廠商</b><span>承接公部門清運、活動與食品銷毀等標案</span></div></div>'
        '<div class="cert-row"><span class="ic">%s</span><div><b>環保局核定清除處理廠商</b><span>列入新北市環保局焚化廠核定進廠清除處理廠商名單</span></div></div>'
        '<div class="cert-row"><span class="ic">%s</span><div><b>統一編號 54712081</b><span>依法登記之環保清運公司</span></div></div>'
        '</div></div></div></div></section>')%(S['check'],S['gov'],S['shield'],S['pin2'])
    return page('about.html','關於我們｜'+TITLE,DESC,body)

def news():
    body=page_hero('最新消息','最新消息與公告','振勇的最新清運實績、服務公告與活動訊息，都會發布在這裡。','最新消息')
    body+=('<section class="band band--tint"><div class="wrap"><div class="empty">'
        '<div class="ic">%s</div><h3>消息陸續更新中</h3>'
        '<p>目前尚無最新公告。近期的清運實績可以先看「<a href="works.html" style="color:var(--green-600);font-weight:700">實績介紹</a>」，'
        '有任何需求也歡迎直接來電或加 LINE 詢問。</p>'
        '<div style="margin-top:22px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">'
        '<a href="tel:0222910883" class="btn btn-call">%s撥打電話</a>'
        '<a href="works.html" class="btn btn-ghost">看實績介紹 %s</a></div>'
        '</div></div></section>')%(S['bell'],S['phone'],S['arrow'])
    return page('news.html','最新消息｜'+TITLE,DESC,body)

def services():
    body=page_hero('服務項目','從一件家具到整座廠房，我們都清得動',
        '九大服務範圍，家庭、店面、辦公室、工廠到大型活動現場，一站處理。','服務項目')
    body+=('<section class="band band--tint"><div class="wrap"><div class="svc-grid">'
        +''.join(svc_card(s) for s in SERVICES)+'</div></div></section>')
    body+=('<section class="band band--dark"><div class="wrap">'+process()+'</div></section>')
    return page('services.html','服務項目｜'+TITLE,DESC,body)

def works():
    body=page_hero('實績介紹','做過的案子，說明我們的能耐',
        '每一個案子就是一本相簿——現場清運、拆除、銷毀的實況，實績會說話。','實績介紹')
    body+=('<section class="band band--tint"><div class="wrap">'+albums_html()+'</div></section>')
    return page('works.html','實績介紹｜'+TITLE,DESC,body)

def location():
    body=page_hero('交通位置','在五股，隨時為雙北出車','公司位於新北市五股區民義路二段，鄰近雙北，機動調度、快速到場。','交通位置')
    body+=('<section class="band band--tint"><div class="wrap"><div class="loc"><div class="info">'
        '<div class="info-row"><span class="ic">%s</span><div><b>公司地址</b><span>新北市五股區民義路二段 23-9 號</span></div></div>'
        '<div class="info-row"><span class="ic">%s</span><div><b>聯絡電話</b><a href="tel:0222910883">(02)2291-0883</a><a href="tel:0282956423">(02)8295-6423</a></div></div>'
        '<div class="info-row"><span class="ic">%s</span><div><b>電子信箱</b><a href="mailto:a0939516638@gmail.com">a0939516638@gmail.com</a></div></div>'
        '<div class="big-cta" style="margin-top:6px"><a href="tel:0222910883" class="btn btn-call">%s立即撥打電話</a></div>'
        '</div><div class="map"><iframe title="振勇環保有限公司地圖" loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
        'src="https://maps.google.com/maps?q=%%E6%%96%%B0%%E5%%8C%%97%%E5%%B8%%82%%E4%%BA%%94%%E8%%82%%A1%%E5%%8D%%80%%E6%%B0%%91%%E7%%BE%%A9%%E8%%B7%%AF%%E4%%BA%%8C%%E6%%AE%%B523-9%%E8%%99%%9F&z=16&output=embed"></iframe>'
        '</div></div></div></section>')%(S['pin2'],S['phone'],S['mail'],S['phone'])
    return page('location.html','交通位置｜'+TITLE,DESC,body)

def contact():
    body=page_hero('聯絡我們','留個訊息，我們盡速回覆','急件請直接來電或加 LINE；一般詢問也可以留言，我們會盡快與你聯繫。','聯絡我們')
    body+=('<section class="band band--tint"><div class="wrap"><div class="contact">'
        '<form class="lead" onsubmit="return false">'
        '<div><label for="c-name">姓名</label><input id="c-name" type="text" placeholder="您怎麼稱呼？" autocomplete="name"></div>'
        '<div><label for="c-phone">行動電話</label><input id="c-phone" type="tel" placeholder="方便聯絡的電話" autocomplete="tel"></div>'
        '<div><label for="c-msg">需求說明</label><textarea id="c-msg" placeholder="要清運／拆除的內容、地點、樓層，方便我們先估價"></textarea></div>'
        '<button type="submit" class="btn btn-green" style="width:100%%">送出詢問</button>'
        '<p style="font-size:.8rem;color:var(--ink-faint);text-align:center">送出後我們會盡速回電。急件建議直接來電或加 LINE 最快。</p></form>'
        '<aside class="contact-aside"><div class="hero-card"><h3 style="color:#fff">最快聯絡方式</h3>'
        '<div class="big-cta" style="margin-top:18px">'
        '<a href="tel:0222910883" class="btn btn-call">%s撥打 (02)2291-0883</a>'
        '<a href="contact.html" class="btn btn-line">%s加 LINE 傳照片估價</a></div>'
        '<p style="margin-top:16px">五股在地 · 雙北服務 · 免費估價 · 合法清運</p></div></aside>'
        '</div></div></section>')%(S['phone'],S['line'])
    body+=('<section class="band"><div class="wrap"><div class="sec-head center">'
        '<span class="eyebrow">常見問答</span><h2 class="title">打電話之前，先看這幾題</h2></div>'
        +faq()+'</div></section>')
    return page('contact.html','聯絡我們｜'+TITLE,DESC,body)

PAGES={'index.html':home,'about.html':about,'news.html':news,'services.html':services,
       'works.html':works,'location.html':location,'contact.html':contact}

if __name__=='__main__':
    out=os.path.join(HERE,'_site')
    os.makedirs(out,exist_ok=True)
    for fn,builder in PAGES.items():
        with open(os.path.join(out,fn),'w',encoding='utf-8') as f:
            f.write(builder())
        print('wrote',fn)
    for f in ['styles.css','main.js']:
        p=os.path.join(HERE,f)
        if os.path.exists(p): shutil.copy(p,os.path.join(out,f))
    for d in ['img','albums']:
        s=os.path.join(HERE,d)
        if os.path.isdir(s): shutil.copytree(s,os.path.join(out,d),dirs_exist_ok=True)
    open(os.path.join(out,'.nojekyll'),'w').close()
    print('site ->',out)
