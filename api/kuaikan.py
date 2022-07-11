# 菜鸟程序员：阿米
import os

import requests
import urllib3
from lxml import etree
#整个文件夹装
dir = "./kuaikan/"

if not os.path.exists(dir):
    os.makedirs(dir)

def getimg():
    url = "https://www.kuaikanmanhua.com/web/comic/378762/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    session = requests.session()
    urllib3.disable_warnings()
    re = session.get(url, headers=headers, verify=False).text
    html = etree.HTML(re)
    print(re)
    r = html.xpath('/html/body/div/div/div/div/div/div/div/div/img/@src')
    i = 0
    for im in r:
        i += 1
        print(str(im))
        # j = requests.get(im)
        # with open(dir + '{}.jpg'.format(i), 'wb') as f:
        #     f.write(j.content)
    # print(r)


if __name__ == '__main__':
    getimg()
