# -*- coding: utf-8 -*-
# 從 pCloud 公開資料夾同步實績相簿 → albums/<分類>/<相簿>/
# 結構：振勇實績 / <分類> / <相簿> / 照片…（分類直屬照片則自成一本以分類命名的相簿）
# 只取網頁尺寸縮圖，原始高解析檔絕不上站。
import json, os, re, sys, shutil, urllib.request, urllib.parse

CODE = os.environ.get('PCLOUD_CODE', '').strip()
API  = os.environ.get('PCLOUD_API', 'https://eapi.pcloud.com')  # 歐洲節點
HERE = os.path.dirname(os.path.abspath(__file__))
ALBUMS = os.path.join(HERE, 'albums')
IMG = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.heic', '.heif')

def call(method, **p):
    url = API + '/' + method + '?' + urllib.parse.urlencode(p)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

def fetch(url, dest):
    req = urllib.request.Request(url, headers={'Referer': 'https://pcloud.com/'})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, 'wb') as f:
        f.write(r.read())

def link_for(fileid):
    # 只取網頁尺寸縮圖（原檔永不上站）
    for size in ('1024x1024', '800x800', '640x640'):
        th = call('getpubthumblink', code=CODE, fileid=fileid, size=size)
        if th.get('result') == 0 and th.get('hosts'):
            return 'https://' + th['hosts'][0] + th['path']
    return None

def is_img(x):
    return not x.get('isfolder') and os.path.splitext(x.get('name', ''))[1].lower() in IMG

def safe(name):
    return re.sub(r'[\\/:*?"<>|]+', '_', name).strip() or '_'

def main():
    if not CODE:
        print('未設定 PCLOUD_CODE，略過 pCloud 同步（保留現有 albums/）。')
        return
    d = call('showpublink', code=CODE)
    if d.get('result') != 0:
        print('showpublink 失敗：', d); sys.exit(1)
    root = d.get('metadata', {})

    # 收集 (分類, 相簿名, 圖片清單)
    jobs = []
    for cat in [c for c in root.get('contents', []) if c.get('isfolder')]:
        cat_name = cat.get('name', '')
        subfolders = [x for x in cat.get('contents', []) if x.get('isfolder')]
        direct = [x for x in cat.get('contents', []) if is_img(x)]
        for sf in subfolders:
            imgs = [x for x in sf.get('contents', []) if is_img(x)]
            if imgs:
                jobs.append((cat_name, sf.get('name', ''), imgs))
        if direct:  # 分類底下直接放照片 → 自成一本
            jobs.append((cat_name, cat_name, direct))
    # 相容：根目錄直接放的相簿（無分類）→ 歸到「其他」
    for alb in [c for c in root.get('contents', []) if c.get('isfolder')]:
        imgs = [x for x in alb.get('contents', []) if is_img(x)]
        subs = [x for x in alb.get('contents', []) if x.get('isfolder')]
        if imgs and not subs:
            jobs.append(('其他', alb.get('name', ''), imgs))

    if not jobs:
        print('pCloud「%s」目前沒有含照片的相簿，略過同步（保留現有 albums/）。' % root.get('name', ''))
        return

    # 有內容才重建 albums/（反映刪除、改名、搬分類）
    if os.path.isdir(ALBUMS):
        shutil.rmtree(ALBUMS)
    os.makedirs(ALBUMS)

    total = 0
    for cat_name, alb_name, imgs in jobs:
        adir = os.path.join(ALBUMS, safe(cat_name), safe(alb_name))
        os.makedirs(adir, exist_ok=True)
        got = 0
        for i, f in enumerate(sorted(imgs, key=lambda x: x.get('name', '')), 1):
            url = link_for(f['fileid'])
            if not url:
                print('    ⚠ 產不出縮圖，跳過：', f.get('name')); continue
            fetch(url, os.path.join(adir, '%03d.jpg' % i))
            got += 1; total += 1
        print('  %s / %s -> %d 張' % (cat_name, alb_name, got))
    cats = sorted(set(j[0] for j in jobs))
    print('pCloud 同步完成：%d 個分類、%d 本相簿、%d 張照片。' % (len(cats), len(jobs), total))

if __name__ == '__main__':
    main()
