import json
from django.http import HttpResponse

import requests
from django.shortcuts import render

import api.ccgp


# Create your views here.

def dingding_index(request):
    return render(request, 'dingding/index.html')


def get(request):
    # info = request.arguments
    code = request.GET.get("code", None)
    print(code)
    # 获取access_token
    # AppKey = "ding4itesoimljq9ksmz"
    # AppSecret = "BW8XFsbesRJdOjmt_peYOQBTwVWUkQKONxZ2_2_fXhBQjmgq2Q6tRWrq867l84ht"
    # url = "https://oapi.dingtalk.com/gettoken?appkey={0}&appsecret={1}".format(AppKey, AppSecret)
    # resp = requests.get(url)
    # resp = resp.json()
    # access_token = resp["access_token"]
    # api.ccgp.access_token()
    # 获取userId
    url1 = "https://oapi.dingtalk.com/user/getuserinfo?access_token={0}&code={1}".format(api.ccgp.access_token(), code)
    resp1 = requests.get(url1)
    resp1 = resp1.json()
    print(resp1, 'resp1')

    # 获取userInfo
    url2 = "https://oapi.dingtalk.com/user/get?access_token={0}&userid={1}".format(api.ccgp.access_token(),
                                                                                   resp1)  # resp1["userid"]
    resp2 = requests.get(url2)
    resp2 = resp2.json()
    print(resp2, 'resp2')
    return HttpResponse(json.dumps({"status": "success", "userinfo": resp2}))
