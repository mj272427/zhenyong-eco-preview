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
    # 先試原檔下載連結；不行再退大縮圖（1600px，網頁足夠且更快）
    dl = call('getpublinkdownload', code=CODE, fileid=fileid, forcedownload=1)
    if dl.get('result') == 0 and dl.get('hosts'):
        return 'https://' + dl['hosts'][0] + dl['path']
    th = call('getpubthumblink', code=CODE, fileid=fileid, size='1600x1600')
    if th.get('result') == 0 and th.get('hosts'):
        return 'https://' + th['hosts'][0] + th['path']
    raise RuntimeError('取不到下載連結 fileid=%s dl=%s' % (fileid, json.dumps(dl, ensure_ascii=False)))

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
        for i, f in enumerate(sorted(imgs, key=lambda x: x.get('name', '')), 1):
            ext = os.path.splitext(f.get('name', ''))[1].lower() or '.jpg'
            dest = os.path.join(adir, '%03d%s' % (i, ext))
            fetch(link_for(f['fileid']), dest)
            total += 1
        print('  相簿:', name, '->', len(imgs), '張')
    print('pCloud 同步完成：%d 本相簿、%d 張照片。' % (len(folders), total))

if __name__ == '__main__':
    main()
