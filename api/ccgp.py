import os
import sys
import re, requests
import json
import time
import datetime
from bs4 import BeautifulSoup
from lxml import etree

from django.http import HttpResponse

import dingtalk.api

userID = ["userid1", "userid2"]  # 27481131291224212
deptID = 646245618


# 获得access_token
def access_token():
    request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    request.appkey = "dingws132rddwykvri4c"
    request.appsecret = "eMawCb2ej9ypr6UfiN93BgH_VYicTAX5OIdjuLE21_sfEnJBO_4IIlJHrD9aJd3u"
    # request.appkey = "dingew1bs4souannu3md"
    # request.appsecret = "t7TtbMeg-APC_37FKHRx2-2GSkwUeSWUoUSr687i9rOa6jUBF4OZcA7WHefPIGCJ"
    f = request.getResponse()
    print(f['access_token'], "access_token")  # 获取access_token
    return f['access_token']


# 默认情况下第一次创建群组 并获取群组id chatid并写入文件里
def getChatid():
    # file_name = "/tmp/.chatid"
    #
    # # 判断群组id文件是否存在
    #
    # if not os.path.exists(file_name):
    #     url = 'https://oapi.dingtalk.com/chat/create?access_token=%s' % access_token()
    #
    #     '''
    #     name : 群组名字
    #     owner: 群主userid
    #     useridlist: 群成员userId列表 也可以写群主userid
    #     '''
    #
    #     data = {
    #         "name": "IT部门",
    #         "owner": "27481131291224212",
    #         "useridlist": ["27481131291224212"]
    #     }
    #
    #     data = json.dumps(data)
    #     req = requests.post(url, data)
    #     chatid = json.loads(req.text)['chatid']
    #     with open(file_name, 'w') as fd:
    #         fd.write(chatid)
    # else:
    #     with open(file_name) as fd:
    #         chatid = fd.read()
    # print(chatid, "chatid")
    # return chatid
    req = dingtalk.api.OapiChatCreateRequest("https://oapi.dingtalk.com/chat/create")
    # req.name = "市场部"
    # req.owner = "274811312926324542"
    # req.useridlist = ["274811312926324542", "0506120309953694", "020215561323463831", "022460230820913350",
    #                   "144336582836424661", "16304563476535427", "01290214283733928788"]
    req.name = "IT部"
    req.owner = "27481131291224212"
    req.useridlist = ["27481131291224212"]
    try:
        resp = req.getResponse(access_token())
        print(resp.get("chatid"), "getChatid")
        return resp.get("chatid")
        # for i in resp
        #     return i["chatid"]
    except Exception as e:
        print(e, "getChatid_err")


# 获得部门列表
def get_department_list(dept_id=646245618):
    """
        查询部门列表
        :param dept_id: 部门id，默认为1（根部门），可输入任意部门id
        """
    post_url = "https://oapi.dingtalk.com/topapi/v2/department/listsub?access_token=%s" % (access_token())
    data = {
        "dept_id": dept_id,
    }
    response = requests.post(post_url, data)
    str_res = response.text
    result = (json.loads(str_res)).get('result')
    print(result, "get_department_list")
    return result


# access_token 访问令牌 chatid 群组id content 发送的内容
def tonews(access_token, chatid, content):
    '''
    chatid  : 群组id
    msgtype : 类型
    content : 内容
    '''
    url = "https://oapi.dingtalk.com/chat/send?access_token=%s" % access_token
    msgtype = 'text'
    values = {
        "chatid": chatid,
        "msgtype": msgtype,
        msgtype: {
            "content": content
        }
    }
    values = json.dumps(values)
    data = requests.post(url, values)
    errmsg = json.loads(data.text)['errmsg']
    if errmsg == 'ok':
        return "ok"

    return "fail: %s" % data.text


# 获得在职员工列表
def get_user_list():
    post_url = "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob?access_token=%s" % (access_token())
    # 初始化offset
    offset = 0
    while True:
        # 请求参数
        data = {
            "status_list": "2,3,5,-1",
            "offset": offset,
            "size": 50
        }
        # 发送post请求
        response = requests.post(post_url, data)
        str_res = response.text
        # json解析
        result = (json.loads(str_res)).get('result')

        # 返回当前页列表
        yield result["data_list"]
        print(result["data_list"], "get_user_list")
        try:
            # 下一页（下50条）
            offset = result["next_cursor"]
            continue
        # 退出条件
        except KeyError:
            break


# if __name__ == '__main__':
def seedtxt():
    getCcgp()
    getCcgp_gg()
    getCcgp_ygs()
    getHc()
    getyh()
    getTsg()
    # print(getCcgp() + getHc() + getyh() + getTsg())
    # return HttpResponse(getCcgp() + getHc() + getyh() + getTsg())


def getCcgp():
    access_token()
    get_department_list()
    get_user_list()
    today = time.strftime('%Y-%m-%d', time.localtime())
    print(today)
    host = "www.ccgp-guangxi.gov.cn"
    url = 'http://www.ccgp-guangxi.gov.cn/front/search/category'
    # url = 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36',
        'cookie': 'acw_tc=ac11000116607138483634388e013c9706945572bd6c4d52e9ce7245c0f1f6',
        # 'Referer': 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'

        'Host': 'www.ccgp-guangxi.gov.cn',
        'Content-Type': 'application/json',
    }
    data = {
        'categoryCode': 'ZcyAnnouncement1',
        'pageSize': '15',
        'pageNo': 1,
        'districtCode': ["450500"]
    }
    title = ""  # 标题
    pathName = ""  # 类型
    districtName = ""  # 区域
    url_n = ""  # 链接
    publishDate = ""  # 发布时间
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    b_list = response.json()
    n_list = b_list["hits"]["hits"]
    # print(n_list)
    # 遍历response
    txts = ""
    for i in n_list:
        title = i["_source"]["title"]
        pathName = i["_source"]["pathName"]
        districtName = i["_source"]["districtName"]
        url_n = "http://" + host + i["_source"]["url"]
        publishDate = i["_source"]["publishDate"]
        timeArray = time.localtime(int(publishDate / 1000))
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        print(title)
        print(publishDate)
        print(pathName)
        print(districtName)
        print("日期", otherStyleTime)
        print(url_n)
        print("-----------------------------------------------------")

        dqtime = datetime.datetime.now().strftime('%Y-%m-%d')
        if dqtime == otherStyleTime:

            print(dqtime, "dqtime")
            # chatid = getChatid()
            chatid = "chat979d2785fe780e114e3efdb71b909c1b"#市场部
            # chatid = "chatb735f7b0581925234db11ab3a125a54f"  # 测试
            req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
            values = {
                "title": districtName + pathName,
                "messageUrl": url_n,
                "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                "text": title + "\n发布时间:" + otherStyleTime
            }

            msg = {
                "link": {
                    "messageUrl": url_n,
                    "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                    "text": title + "\n发布时间:" + otherStyleTime,
                    "title": districtName + pathName
                },
                "msgtype": "link"
            }

            txts = txts + title + "<br>"
            values = json.dumps(values)
            req.link = values
            req.msgtype = "link"
            print(chatid, "chatidssssssssssssss")

            req.chatid = chatid
            req.link = values
            req.msgtype = "link"
            req.msg = msg

            try:
                resp = req.getResponse(access_token())
                # return HttpResponse(resp)
                print(resp, "seedtxt")
            except Exception as e:
                print(e, "seedtxt_err")
                # return HttpResponse(e)

    print(txts)
    # return txts


def getCcgp_gg():
    access_token()
    get_department_list()
    get_user_list()
    today = time.strftime('%Y-%m-%d', time.localtime())
    print(today)
    host = "www.ccgp-guangxi.gov.cn"
    url = 'http://www.ccgp-guangxi.gov.cn/front/search/category'
    # url = 'http://www.ccgp-guangxi.gov.cn/ZcyAnnouncement/ZcyAnnouncement1/index.html'
    # url = 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/86.0.4240.198 Safari/537.36',
        # 'cookie': 'acw_tc=ac11000116607138483634388e013c9706945572bd6c4d52e9ce7245c0f1f6',
        # 'Referer': 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'

        'Host': 'www.ccgp-guangxi.gov.cn',
        'Content-Type': 'application/json',
    }
    data = {
        'categoryCode': 'ZcyAnnouncement10016',
        'pageSize': '15',
        'pageNo': 1,
        'districtCode': ["450500"]
    }
    title = ""  # 标题
    pathName = ""  # 类型
    districtName = ""  # 区域
    url_n = ""  # 链接
    publishDate = ""  # 发布时间
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    b_list = response.json()
    n_list = b_list["hits"]["hits"]
    print(response.status_code)
    # 遍历response
    txts = ""
    for i in n_list:
        title = i["_source"]["title"]
        pathName = i["_source"]["pathName"]
        districtName = i["_source"]["districtName"]
        url_n = "http://" + host + i["_source"]["url"]
        publishDate = i["_source"]["publishDate"]
        timeArray = time.localtime(int(publishDate / 1000))
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        print(title)
        print(publishDate)
        print(pathName)
        print(districtName)
        print("日期", otherStyleTime)
        print(url_n)
        print("-----------------------------------------------------")

        dqtime = datetime.datetime.now().strftime('%Y-%m-%d')
        if dqtime == otherStyleTime:

            print(dqtime, "dqtime")
            # chatid = getChatid()
            chatid = "chat979d2785fe780e114e3efdb71b909c1b"#市场部
            # chatid = "chatb735f7b0581925234db11ab3a125a54f"  # 测试
            req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
            values = {
                "title": districtName + pathName,
                "messageUrl": url_n,
                "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                "text": title + "\n发布时间:" + otherStyleTime
            }

            msg = {
                "link": {
                    "messageUrl": url_n,
                    "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                    "text": title + "\n发布时间:" + otherStyleTime,
                    "title": districtName + pathName
                },
                "msgtype": "link"
            }

            txts = txts + title + "<br>"
            values = json.dumps(values)
            req.link = values
            req.msgtype = "link"
            print(chatid, "chatidssssssssssssss")

            req.chatid = chatid
            req.link = values
            req.msgtype = "link"
            req.msg = msg

            try:
                resp = req.getResponse(access_token())
                # return HttpResponse(resp)
                print(resp, "seedtxt")
            except Exception as e:
                print(e, "seedtxt_err")
                # return HttpResponse(e)

    print(txts)
    # return txts


def getCcgp_ygs():
    access_token()
    get_department_list()
    get_user_list()
    today = time.strftime('%Y-%m-%d', time.localtime())
    print(today)
    host = "www.ccgp-guangxi.gov.cn"
    url = 'http://www.ccgp-guangxi.gov.cn/front/search/category'
    # url = 'http://www.ccgp-guangxi.gov.cn/ZcyAnnouncement/ZcyAnnouncement1/index.html'
    # url = 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36',
        'cookie': 'acw_tc=ac11000116607138483634388e013c9706945572bd6c4d52e9ce7245c0f1f6',
        # 'Referer': 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'

        'Host': 'www.ccgp-guangxi.gov.cn',
        'Content-Type': 'application/json',
    }
    data = {
        'categoryCode': 'ZcyAnnouncement5',
        'pageSize': '15',
        'pageNo': 1,
        'districtCode': ["450500"]
    }
    title = ""  # 标题
    pathName = ""  # 类型
    districtName = ""  # 区域
    url_n = ""  # 链接
    publishDate = ""  # 发布时间
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    b_list = response.json()
    n_list = b_list["hits"]["hits"]
    print(response.status_code)
    # 遍历response
    txts = ""
    for i in n_list:
        title = i["_source"]["title"]
        pathName = i["_source"]["pathName"]
        districtName = i["_source"]["districtName"]
        url_n = "http://" + host + i["_source"]["url"]
        publishDate = i["_source"]["publishDate"]
        timeArray = time.localtime(int(publishDate / 1000))
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        print(title)
        print(publishDate)
        print(pathName)
        print(districtName)
        print("日期", otherStyleTime)
        print(url_n)
        print("-----------------------------------------------------")

        dqtime = datetime.datetime.now().strftime('%Y-%m-%d')
        if dqtime == otherStyleTime:

            print(dqtime, "dqtime")
            # chatid = getChatid()
            chatid = "chat979d2785fe780e114e3efdb71b909c1b"#市场部
            # chatid = "chatb735f7b0581925234db11ab3a125a54f"  # 测试
            req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
            values = {
                "title": districtName + pathName,
                "messageUrl": url_n,
                "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                "text": title + "\n发布时间:" + otherStyleTime
            }

            msg = {
                "link": {
                    "messageUrl": url_n,
                    "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                    "text": title + "\n发布时间:" + otherStyleTime,
                    "title": districtName + pathName
                },
                "msgtype": "link"
            }

            txts = txts + title + "<br>"
            values = json.dumps(values)
            req.link = values
            req.msgtype = "link"
            print(chatid, "chatidssssssssssssss")

            req.chatid = chatid
            req.link = values
            req.msgtype = "link"
            req.msg = msg

            try:
                resp = req.getResponse(access_token())
                # return HttpResponse(resp)
                print(resp, "seedtxt")
            except Exception as e:
                print(e, "seedtxt_err")
                # return HttpResponse(e)

    print(txts)
    # return txts


def getHc():
    access_token()
    get_department_list()
    get_user_list()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400',
    }
    # 海城区批复公告
    url = "http://www.bhhc.gov.cn/zwgk/fdzdgknr/zdxmpzhss/xmtzpzjgxx/"
    turl = ""
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    ss = soup.find_all("div", class_="right_list")
    # sss = ss[0].find("a").get("href")
    dqtime = datetime.datetime.now().strftime('%Y-%m-%d')
    txts = ""
    for i in ss:
        t = i.find_all("li")
        for j in t:
            # print(url+j.find("a").get("href"),j.find("a").get_text(),j.find("span").get_text())
            if dqtime == j.find("span").get_text():

                if j.find("a").get("href")[0] == ".":
                    turl = url + j.find("a").get("href")
                else:
                    turl = j.find("a").get("href")
                chatid = "chat979d2785fe780e114e3efdb71b909c1b"#市场部
                # chatid = "chatb735f7b0581925234db11ab3a125a54f"  # 测试
                req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
                values = {
                    "title": "海城区批复公告",
                    "messageUrl": turl,
                    "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                    "text": j.find("a").get_text() + "\n发布时间:" + j.find("span").get_text()
                }

                msg = {
                    "link": {
                        "messageUrl": turl,
                        "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                        "text": j.find("a").get_text() + "\n发布时间:" + j.find("span").get_text(),
                        "title": "海城区批复公告"
                    },
                    "msgtype": "link"
                }

                txts = txts + "[海城区批复公告]" + j.find("a").get_text() + "<br>"
                values = json.dumps(values)
                # req.link = values
                # req.msgtype = "link"
                # # print(chatid, "chatidssssssssssssss")

                req.chatid = chatid
                req.link = values
                req.msgtype = "link"
                req.msg = msg

                try:
                    resp = req.getResponse(access_token())
                    # return HttpResponse(resp)
                    print(resp, "seedtxt")
                except Exception as e:
                    print(e, "seedtxt_err")
                    # return HttpResponse(e)
        # print("-----------------------------------------------------")
    print("海城区批复公告爬取结束。")
    print(txts)
    # return txts


def getyh():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400',
    }
    # 银海区批复公告
    url = "http://www.yinhai.gov.cn/zwgk/fdzdgk/zdjsxm_1/xmtzpzjgxx/"
    turl = ""
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    ss = soup.find_all("ul", class_="list-cont")
    dqtime = datetime.datetime.now().strftime('(%Y-%m-%d)')
    # print(dqtime)
    txts = ""
    for i in ss:
        t = i.find_all("li")
        for j in t:
            # print(url+j.find("a").get("href"),j.find("a").get_text(),j.find("span").get_text())
            if dqtime == j.find("span").get_text():

                if j.find("a").get("href")[0] == ".":
                    turl = url + j.find("a").get("href")
                else:
                    turl = j.find("a").get("href")
                chatid = "chat979d2785fe780e114e3efdb71b909c1b"#市场部
                # chatid = "chatb735f7b0581925234db11ab3a125a54f"  # 测试
                req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
                values = {
                    "title": "银海区批复公告",
                    "messageUrl": turl,
                    "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                    "text": j.find("a").get_text() + "\n发布时间:" + j.find("span").get_text()
                }

                msg = {
                    "link": {
                        "messageUrl": turl,
                        "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                        "text": j.find("a").get_text() + "\n发布时间:" + j.find("span").get_text(),
                        "title": "银海区批复公告"
                    },
                    "msgtype": "link"
                }

                txts = txts + "[银海区批复公告]" + j.find("a").get_text() + "<br>"
                values = json.dumps(values)
                # req.link = values
                # req.msgtype = "link"
                # # print(chatid, "chatidssssssssssssss")

                req.chatid = chatid
                req.link = values
                req.msgtype = "link"
                req.msg = msg

                try:
                    resp = req.getResponse(access_token())
                    # return HttpResponse(resp)
                    print(resp, "seedtxt")
                except Exception as e:
                    print(e, "seedtxt_err")
                    # return HttpResponse(e)
        # print("-----------------------------------------------------")

    print("银海区批复公告爬取结束。")
    print(txts)
    # return txts


# if __name__ == '__main__':
def getTsg():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400',
    }
    # 铁山港区批复公告
    url = "http://www.bhtsg.gov.cn/zwgk/fdzdgk/zdjsxmpzhss/xmpzjg/"
    turl = ""
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find_all("div", class_="content-left")
    dqtime = datetime.datetime.now().strftime('%Y-%m-%d')
    txts = ""
    for ul in div:
        tul = ul.find_all("ul")
        for i in tul:
            t = i.find_all("li")
            for j in t:
                # h=j.find("a").get("href")[0]
                # print(url+j.find("a").get("href"),j.find("a").get_text(),j.find("span").get_text())
                # print(h)
                if dqtime == j.find("span").get_text():
                    if j.find("a").get("href")[0] == ".":
                        turl = url + j.find("a").get("href")
                    else:
                        turl = j.find("a").get("href")

                    chatid = "chat979d2785fe780e114e3efdb71b909c1b"#市场部
                    # chatid = "chatb735f7b0581925234db11ab3a125a54f"  # 测试

                    req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
                    values = {
                        "title": "铁山港区批复公告",
                        "messageUrl": turl,
                        "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                        "text": j.find("a").get_text() + "\n发布时间:" + j.find("span").get_text()
                    }

                    msg = {
                        "link": {
                            "messageUrl": turl,
                            "picUrl": "http://www.gxnfc.com/static/img/logo2.png",
                            "text": j.find("a").get_text() + "\n发布时间:" + j.find("span").get_text(),
                            "title": "铁山港区批复公告"
                        },
                        "msgtype": "link"
                    }

                    txts = txts + "[铁山港区批复公告]" + j.find("a").get_text() + "<br>"
                    values = json.dumps(values)
                    # req.link = values
                    # req.msgtype = "link"
                    # # print(chatid, "chatidssssssssssssss")

                    req.chatid = chatid
                    req.link = values
                    req.msgtype = "link"
                    req.msg = msg

                    try:
                        resp = req.getResponse(access_token())
                        # return HttpResponse(resp)
                        print(resp, "seedtxt")
                    except Exception as e:
                        print(e, "seedtxt_err")
                        # return HttpResponse(e)
    print("铁山港批复公告爬取结束。")
    print(txts)
    # return txts
