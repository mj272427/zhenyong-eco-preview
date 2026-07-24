# -*- coding: utf-8 -*-
# 從 pCloud 公開資料夾同步實績相簿 → albums/
# 「振勇實績」公開分享連結的 code 放在環境變數 PCLOUD_CODE（非密碼，只讀該公開資料夾）。
# 規則：公開資料夾底下「一個子資料夾＝一本相簿」，子資料夾名＝相簿名。
import json, os, re, sys, urllib.request, urllib.parse

CODE = os.environ.get('PCLOUD_CODE', '').strip()
API  = os.environ.get('PCLOUD_API', 'https://eapi.pcloud.com')  # 歐洲節點
HERE = os.path.dirname(os.path.abspath(__file__))
ALBUMS = os.path.join(HERE, 'albums')

def call(method, **p):
    url = API + '/' + method + '?' + urllib.parse.urlencode(p)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

def fetch(url, dest):
    req = urllib.request.Request(url, headers={'Referer': 'https://pcloud.com/'})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, 'wb') as f:
        f.write(r.read())

def link_for(fileid):
    # 只取「網頁尺寸縮圖」——原始高解析檔絕不放上網站（避免同業整包抓走可用大圖）
    for size in ('1024x1024', '800x800', '640x640'):
        th = call('getpubthumblink', code=CODE, fileid=fileid, size=size)
        if th.get('result') == 0 and th.get('hosts'):
            return 'https://' + th['hosts'][0] + th['path']
    return None  # 產不出縮圖就跳過這張，寧可少一張也不放原檔

def safe(name):
    return re.sub(r'[\\/:*?"<>|]+', '_', name).strip() or 'album'

def main():
    if not CODE:
        print('未設定 PCLOUD_CODE，略過 pCloud 同步（保留現有 albums/）。')
        return
    d = call('showpublink', code=CODE)
    if d.get('result') != 0:
        print('showpublink 失敗：', d)
        sys.exit(1)
    root = d.get('metadata', {})
    folders = [c for c in root.get('contents', []) if c.get('isfolder')]
    if not folders:
        print('pCloud「%s」目前沒有相簿子資料夾，略過同步（保留現有 albums/）。' % root.get('name', ''))
        return
    os.makedirs(ALBUMS, exist_ok=True)
    total = 0
    for fol in folders:
        name = safe(fol.get('name', 'album'))
        imgs = [f for f in fol.get('contents', [])
                if not f.get('isfolder') and str(f.get('contenttype', '')).startswith('image/')]
        if not imgs:
            print('  (跳過空相簿)', name)
            continue
        adir = os.path.join(ALBUMS, name)
        os.makedirs(adir, exist_ok=True)
        got = 0
        for i, f in enumerate(sorted(imgs, key=lambda x: x.get('name', '')), 1):
            url = link_for(f['fileid'])
            if not url:
                print('    ⚠ 產不出縮圖，跳過：', f.get('name'))
                continue
            dest = os.path.join(adir, '%03d.jpg' % i)
            fetch(url, dest)
            got += 1
            total += 1
        print('  相簿:', name, '->', got, '張')
    print('pCloud 同步完成：%d 本相簿、%d 張照片。' % (len(folders), total))

if __name__ == '__main__':
    main()
