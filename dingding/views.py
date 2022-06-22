import json
from django.http import HttpResponse

import requests
from django.shortcuts import render

import api.ccgp
import dingtalk.api


# Create your views here.

def dingding_index(request):
    return render(request, 'dingding/index.html')


# 获得access_token
def access_token():
    request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    request.appkey = "ding2l1mdry4hwupi5wb"
    request.appsecret = "OZIPpjo8zvPult_YfntCFnbPTB5GTlsyhhtKoyt1Ha9-jxS6rhdlVv3AyZ_9Dezr"
    f = request.getResponse()
    # print(f['access_token'], "access_token")  # 获取access_token
    return f['access_token']


def get(request):
    response = HttpResponse()
    code = request.GET.get('code')
    print(code, "code")
    print(access_token(), "access_token")
    # 获取userId
    url1 = "https://oapi.dingtalk.com/user/getuserinfo?access_token={0}&code={1}".format(access_token(), code)
    resp1 = requests.get(url1)
    resp1 = resp1.json()
    resp = {}
    resp = resp1
    print(resp, "resp1")
    print(resp["is_sys"], "is_sys")
    print(resp["name"], "name")
    print(resp["userid"], "userid")
    # for re in resp.keys():
    # sys_level = re["sys_level"]
    # is_sys = re["is_sys"]
    # name = re["name"]
    # deviceId = re["deviceId"]
    # userid = re["userid"]
    # print(sys_level, "sys_level")
    # print(is_sys, "is_sys")
    # print(name, "name")
    # print(deviceId, "deviceId")
    # print(userid, "userid")

    # 获取userInfo
    # url2 = "https://oapi.dingtalk.com/user/get?access_token={0}&userid={1}".format(access_token(),
    #                                                                                resp1)  # resp1["userid"]
    url2 = "https://oapi.dingtalk.com/user/get?access_token={0}&userid={1}".format(access_token(), resp1["userid"])
    resp2 = requests.get(url2)
    resp2 = resp2.json()
    print(resp2, "resp2")

    # return HttpResponse(json.dumps(resp1))
    # return request.write(json.dumps({"status": "success", "userinfo": resp2}))
    response.write("<script language='javascript' type='text/javascript'>window.location.href='/ser/index/';</script>")
    return response


def DDbd(request):
    return s
