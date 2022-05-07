import os
import sys
import re, requests
import json
import time
import dingtalk.api

userID = 27481131291224212
deptID = 646245618


# 获得access_token
def access_token():
    request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    request.appkey = "dingew1bs4souannu3md"
    request.appsecret = "t7TtbMeg-APC_37FKHRx2-2GSkwUeSWUoUSr687i9rOa6jUBF4OZcA7WHefPIGCJ"
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
    req.name = "IT部门"
    req.owner = "27481131291224212"
    req.useridlist = "27481131291224212"
    try:
        resp = req.getResponse(access_token())
        print(resp, "getChatid")
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
    access_token()
    get_department_list()
    get_user_list()
    today = time.strftime('%Y-%m-%d', time.localtime())
    print(today)
    host = "www.ccgp-guangxi.gov.cn"
    url = 'http://www.ccgp-guangxi.gov.cn/front/search/category'
    # url = 'http://www.ccgp-guangxi.gov.cn/reformColumn/index.html'
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/100.0.4896.60 Safari/537.36 ',
        # 'cookie': 'acw_tc=2f624a5216515120695576519e78fd6cf0d08d9ff5f73384ee1a8dd3bd0271;path=/;HttpOnly;Max-Age=1800',
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
    # print(n_list)
    # 遍历response
    for i in n_list:
        title = i["_source"]["title"]
        pathName = i["_source"]["pathName"]
        districtName = i["_source"]["districtName"]
        url_n = "http://"+host+i["_source"]["url"]
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

        chatid = getChatid()
        req = dingtalk.api.OapiChatSendRequest("https://oapi.dingtalk.com/chat/send")
        values = {
            "title": districtName+pathName,
            "messageUrl": url_n,
            "text": title+"\n发布时间:"+otherStyleTime
        }
        values = json.dumps(values)
        req.link = values
        try:
            resp = req.getResponse(access_token())
            print(resp,"seedtxt")
        except Exception as e:
            print(e,"seedtxt_err")
