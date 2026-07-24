# -*- coding: utf-8 -*-
# 產生 pCloud 公開資料夾的「內容指紋」寫入 .pcloud_fp
# 只讀 metadata（檔名+大小），不下載照片 → 極省。
# 有新增/刪除/改名/換檔時指紋才會變，偵測器據此判斷要不要觸發重建。
import os, sys, json, hashlib, urllib.request, urllib.parse

CODE = os.environ.get('PCLOUD_CODE', '').strip()
API  = os.environ.get('PCLOUD_API', 'https://eapi.pcloud.com')  # 歐洲節點
HERE = os.path.dirname(os.path.abspath(__file__))
FP   = os.path.join(HERE, '.pcloud_fp')

def call(method, **p):
    url = API + '/' + method + '?' + urllib.parse.urlencode(p)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

def walk(node, prefix, out):
    # 遞迴走訪（支援日後的分類多層資料夾），只收「路徑|大小」這種穩定欄位
    for c in node.get('contents', []) or []:
        path = prefix + '/' + c.get('name', '')
        if c.get('isfolder'):
            walk(c, path, out)
        else:
            out.append('%s|%s' % (path, c.get('size', '')))

def main():
    if not CODE:
        print('未設定 PCLOUD_CODE', file=sys.stderr); sys.exit(2)
    d = call('showpublink', code=CODE)
    if d.get('result') != 0:
        print('showpublink 失敗：%s' % d, file=sys.stderr); sys.exit(3)
    lines = []
    walk(d.get('metadata', {}), '', lines)
    lines.sort()
    fp = hashlib.sha256('\n'.join(lines).encode('utf-8')).hexdigest()
    with open(FP, 'w') as f:
        f.write(fp + '\n')
    print('指紋：%s（%d 檔）' % (fp, len(lines)))

if __name__ == '__main__':
    main()
