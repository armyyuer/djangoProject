import requests
import json
import urllib3
import datetime
from bs4 import BeautifulSoup


def deldw():
    username = "admin"
    password = "c69abe0532d40b02e4ae366197966e1a"
    homeurl = "https://10.80.104.103/login"
    topurl = "https://10.80.104.103/cus-api/api/bigScreen/monitor/risk/web/asset/top"
    scanurl = "https://10.80.104.103/assetApi/api/masscan/check/scan"
    passWordurl = "https://10.80.104.103/assetApi/api/sys/user/check/passWord?id=1"
    initLoginPageData = "https://10.80.104.103/assetApi/api/noAuth/initLoginPageData"
    infourl = "https://10.80.104.103/assetApi/api/sys/platform/info"
    imagesurl = "https://10.80.104.103/assetApi/api/noAuth/verify/images?date=1657428759736"
    guideurl = "https://10.80.104.103/assetApi/api/sys/user/check/guide"
    loginurl = "https://10.80.104.103/assetApi/api/authenticate"
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/100.0.4896.60 Safari/537.36 ',
        # 'cookie': 'acw_tc=2f624a5216515120695576519e78fd6cf0d08d9ff5f73384ee1a8dd3bd0271;path=/;HttpOnly;Max-Age=1800',
        # 'Referer': 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'

        'Host': 'www.ccgp-guangxi.gov.cn',
        'Content-Type': 'application/json',
    }
    data = {
        "password": password,
        "rememberMe": False,
        "verifyCode": "",
        "username": username
    }
    print(data, "data")
    # def getID():
    #     file0 = open("a.txt", "r", encoding="utf-8")

    # with open("a.txt",encoding='utf8') as f:
    # content = json.load(f)
    # print(type(content))  # <class 'str'>
    # # print(content)
    # file0.close()
    session = requests.session()
    urllib3.disable_warnings()
    # home = session.get(homeurl, headers=headers, verify=False)
    # print(home.text, "home")
    # top = session.get(topurl, headers=headers, verify=False)
    # print(top.text, "top")
    # scan = session.get(scanurl, headers=headers, verify=False)
    # print(scan.text, "scan")
    # pWurl = session.get(passWordurl, headers=headers, verify=False)
    # print(pWurl.text, "pWurl")
    # init = session.get(initLoginPageData, headers=headers, erify=False)
    # print(init.text, "init")
    # info = session.get(infourl, headers=headers, verify=False)
    # print(info.text, "info")
    # images = session.get(imagesurl, headers=headers, verify=False)
    # print(images.text, "images")
    # guide = session.get(guideurl, headers=headers, verify=False)
    # print(guide.text,"guide")
    resp = session.post(loginurl, headers=headers, data=json.dumps(data), verify=False)
    print(resp.text)
    datatxt = json.load(open("a.txt", "r", encoding='utf8'))
    # b_list = data.json()
    n_list = datatxt["data"]
    for i in n_list:
        id = i["id"]
        print(id)
        durl = "https://10.80.104.103/assetApi/api/sys/org/delete?id=" + str(id)
        did = session.delete(durl, headers=headers, verify=False)
        print(did.text)


def chcekurl():
    session = requests.session()
    # urllib3.disable_warnings()
    file0 = open("a.txt", "r", encoding="utf-8")
    # with open("a.txt",encoding='utf8') as f:
    # content = json.load(f)
    content = file0.read()
    # print(type(content))  # <class 'str'>
    # print(content)
    # file0.close()
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/100.0.4896.60 Safari/537.36 ',
        # 'cookie': 'acw_tc=2f624a5216515120695576519e78fd6cf0d08d9ff5f73384ee1a8dd3bd0271;path=/;HttpOnly;Max-Age=1800',
        # 'Referer': 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'

        'Host': 'www.ccgp-guangxi.gov.cn',
        'Content-Type': 'application/json',
    }
    w = ''
    txts = content.split("\n")

    for temp in txts:
        try:
            url = "http://" + temp+"/"
            rep = session.get(url, headers=headers, verify=False)

            print(rep.status_code)  # <class 'str'>
            if rep.status_code == 200:
                w += str(url) + "\n"
                print(f"{url}-{rep.status_code}--http访问正常")
            # else:
            #     print(f"{url}-{rep.status_code}--http无法访问")
            #     urls = "https://" + temp
            #     urllib3.disable_warnings()
            #     reps = session.get(urls, headers=headers, verify=False)
            #     if reps.status_code == 200:
            #         w += str(urls) + "\n"
            #         print(f"{urls}-{reps.status_code}--https访问正常")
            #     else:
            #         print(f"{urls}-{reps.status_code}--http及https无法访问")
        except:
            print(f"{url}--无响应")
            # urls = "https://" + temp
            # urllib3.disable_warnings()
            # reps = session.get(urls, headers=headers, verify=False)
            # if reps.status_code == 200:
            #     w += str(urls) + "\n"
            #     print(f"{urls}-{reps.status_code}--https访问正常")
            # else:
            #     print(f"{urls}-{reps.status_code}--http及https无法访问")
    file0.close()

    # print(w)
    with  open('url.txt', 'w')as f:
        f.write(w)
        f.close()


if __name__ == '__main__':
    chcekurl()
