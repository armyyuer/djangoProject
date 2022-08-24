import json

from django.contrib.auth import login
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import requests
from django.shortcuts import render
from django.contrib.auth.models import User

import UserManage
import api.ccgp
import dingtalk.api

# Create your views here.
from Att.views import upload
from common.models import DDuser, Att, UserGroups, GroupPermissions, MenuPermission
from login.ck import auth, authDD_m
from lxml import etree


def dingding_index(request):
    return render(request, 'dingding/index.html')


# 获得access_token
def access_token():
    request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    request.appkey = "dingws132rddwykvri4c"
    request.appsecret = "eMawCb2ej9ypr6UfiN93BgH_VYicTAX5OIdjuLE21_sfEnJBO_4IIlJHrD9aJd3u"
    f = request.getResponse()
    # print(f['access_token'], "access_token")  # 获取access_token
    return f['access_token']


# @auth
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

    try:
        # 根据 id 从数据库中找到相应的客户记录
        u = DDuser.objects.get(userid=resp["userid"])
        print("用户" + resp["name"] + "已绑定过,下一步验证用户数据" + str(type))
        cu = User.objects.get(id=u.uid)
        if cu.is_active:
            request.session['username'] = cu.username
            request.session['userid'] = cu.id
            request.session['useremail'] = cu.email
            um = UserGroups.objects.get(userID=cu.id)
            request.session['usergroup'] = um.groupID
            gl = GroupPermissions.objects.filter(groupID=um.groupID)
            glist = []
            for g in gl:
                glist.append(g.permissionID)

            mp = MenuPermission.objects.filter(permissionID__in=glist)

            mlist = []
            for m in mp:
                mlist.append(m.codeName)
            print(mlist, 'mcodeName')
            if cu.is_superuser:
                login(request, cu)
                request.session['usertype'] = '1'
                return HttpResponseRedirect('/dingding/main/')
            else:
                login(request, cu)
                request.session['usertype'] = '0'
                return HttpResponseRedirect('/dingding/main/')
        else:
            return HttpResponseRedirect("/dingding/DDbdend/?txt=账号已锁定，青联系管理员！")
    except DDuser.DoesNotExist:
        print("账号未绑定钉钉，青先绑定!" + str(type))
        return HttpResponseRedirect("/dingding/DDbdend/?txt=账号未绑定钉钉，青先绑定!")
    # url2 = "https://oapi.dingtalk.com/user/get?access_token={0}&userid={1}".format(access_token(), resp1["userid"])
    # resp2 = requests.get(url2)
    # resp2 = resp2.json()
    # print(resp2, "resp2")


def pcget(request):
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

    try:
        # 根据 id 从数据库中找到相应的客户记录
        u = DDuser.objects.get(userid=resp["userid"])
        print("用户" + resp["name"] + "已绑定过,下一步验证用户数据" + str(type))
        cu = User.objects.get(id=u.uid)
        if cu.is_active:
            request.session['username'] = cu.username
            request.session['userid'] = cu.id
            request.session['useremail'] = cu.email
            um = UserGroups.objects.get(userID=cu.id)
            request.session['usergroup'] = um.groupID
            gl = GroupPermissions.objects.filter(groupID=um.groupID)
            glist = []
            for g in gl:
                glist.append(g.permissionID)

            mp = MenuPermission.objects.filter(permissionID__in=glist)

            mlist = []
            for m in mp:
                mlist.append(m.codeName)
            print(mlist, 'mcodeName')
            request.session['permissions'] = mlist
            if cu.is_superuser:
                login(request, cu)
                request.session['usertype'] = '1'
                return HttpResponseRedirect('/main/')
            else:
                login(request, cu)
                request.session['usertype'] = '0'
                return HttpResponseRedirect('/main/')
        else:
            return HttpResponseRedirect("/login/err/?txt=账号已锁定，青联系管理员！")
    except DDuser.DoesNotExist:
        print("账号未绑定钉钉，青先绑定!" + str(type))
        return HttpResponseRedirect("/login/err/?txt=账号未绑定钉钉，青先绑定!")
    # url2 = "https://oapi.dingtalk.com/user/get?access_token={0}&userid={1}".format(access_token(), resp1["userid"])
    # resp2 = requests.get(url2)
    # resp2 = resp2.json()
    # print(resp2, "resp2")


def main(request):
    return render(request, 'dingding/main.html')


@authDD_m
def desktop(request):
    username = request.session['username']
    userid = request.session['userid']
    return render(request, 'dingding/desktop.html', {'username': username, 'userid': userid})


@authDD_m
def calendar(request):
    username = request.session['username']
    userid = request.session['userid']
    return render(request, 'dingding/calendar.html', {'username': username, 'userid': userid})


@authDD_m
def project(request):
    username = request.session['username']
    userid = request.session['userid']
    return render(request, 'dingding/project.html', {'username': username, 'userid': userid})


@authDD_m
def kangyi(request):
    username = request.session['username']
    userid = request.session['userid']
    att = Att.objects.filter(UserID=userid).order_by("-AttID")[:10]
    return render(request, 'dingding/kangyi.html', {'username': username, 'userid': userid, 'kangyilist': att})


@authDD_m
def uppic(request):
    type = request.GET.get("type")
    username = request.session['username']
    userid = request.session['userid']
    lx = ""
    if type == "1":
        lx = "健康码"
    if type == "2":
        lx = "行程码"
    if type == "3":
        lx = "核酸结果"
    return render(request, 'dingding/uppic.html', {'type': type, 'username': username, 'userid': userid, 'lx': lx})


@authDD_m
def uppicsave(request):
    type = request.POST.get("type")
    username = request.session['username']
    userid = request.session['userid']
    lx = ""
    if type == "1":
        lx = "健康码"
    if type == "2":
        lx = "行程码"
    if type == "3":
        lx = "核酸结果"
    if request.FILES.get("up_file"):
        furl = upload(request.FILES.get("up_file"), type, request)
        txt = "上传成功。"
        return HttpResponseRedirect("/dingding/kangyi/")
    else:
        txt = "*清选择要上传的图片!"
        print(txt)
        return render(request, 'dingding/uppic.html',
                      {'type': type, 'username': username, 'userid': userid, 'msg': txt, 'lx': lx})


def DDbd(request):
    return render(request, 'dingding/ddbd.html')


def DDbdu(request):
    response = HttpResponse()
    code = request.GET.get('code')
    uid = request.GET.get('uid')
    print(code, "code")
    print(uid, "uid")
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
    try:
        # 根据 id 从数据库中找到相应的客户记录
        u = DDuser.objects.get(uid=uid)
        print("用户" + resp["name"] + "已绑定过了，不用再次绑定！" + str(type))
        return HttpResponseRedirect("/dingding/DDbdend/?txt=用户" + resp["name"] + "已绑定过了，不用再次绑定！")
    except DDuser.DoesNotExist:
        print("用户开始绑定" + str(type))
        record = DDuser.objects.create(name=resp["name"],
                                       sys_level=0,
                                       is_sys=resp["is_sys"],
                                       deviceId=0,
                                       userid=resp["userid"],
                                       uid=uid)
        print("用户" + record.name + "绑定成功!")

    return HttpResponseRedirect("/dingding/DDbdend/?txt=用户" + record.name + "开始绑定成功!")


def DDbdend(request):
    txt = request.GET.get('txt')
    return render(request, 'dingding/DDbdend.html', {'txt': txt})


@authDD_m
def ser(request):
    username = request.session['username']
    userid = request.session['userid']
    return render(request, 'dingding/ser.html', {'username': username, 'userid': userid})


def pc(request):
    return render(request, 'dingding/pc.html')
