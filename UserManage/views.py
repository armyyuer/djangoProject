import os.path
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Att.views import wrdb, upload, userdb
from common import models
from common.models import Company, Group, UserGroups
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from login.ck import auth


def index_views(request):
    return HttpResponse('欢迎登录用户管理！')


def register_views(request):
    # return render(request, 'users/register.html')
    return render(request, 'users/reg.html')


def adduser(request):
    corporate_name = request.POST.get("corporate_name", '')
    corporate_code = request.POST.get("corporate_code", '')
    passWord = make_password(request.POST.get("password", ''))
    corporate_contacts = request.POST.get("corporate_contacts", '')
    corporate_phone = request.POST.get("corporate_phone", '')
    corporate_email = request.POST.get("corporate_email", '')
    is_superuser = 0
    is_staff = 0
    is_active = 0
    is_luck = 0
    d1 = timezone.now()
    # date_joined = d1.strftime("%Y-%m-%d")
    date_joined = d1
    # print(corporate_name)
    # print(corporate_code)
    # 从请求消息中 获取要添加的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    users = User.objects.filter(username=corporate_code)
    # 如果能找到用户
    if len(users) > 0:
        # return render(request, 'users/register.html')
        return HttpResponse('企业已存在！')
    else:
        record = User.objects.create(username=corporate_code,
                                     email=corporate_email,
                                     password=passWord,
                                     is_superuser=is_superuser,
                                     is_staff=is_staff,
                                     is_active=is_active,
                                     date_joined=date_joined)

        Companyrecord = models.Company.objects.create(userId=record.id,
                                                      email=corporate_email,
                                                      companyName=corporate_name,
                                                      code=corporate_code,
                                                      contacts=corporate_contacts,
                                                      is_luck=is_luck,
                                                      phone=corporate_phone)

        print("新增用户：" + Companyrecord.companyName + ",统一信用代码：" + Companyrecord.code)
        print("电子邮箱：" + record.email)
        print("联系人：" + Companyrecord.contacts)
        print("联系电话：" + Companyrecord.phone)
        print("关联ID：" + str(Companyrecord.userId))
        # return render(request, 'users/register.html')
        return HttpResponse('注册成功！')


def reg(request):
    # 如果是ajax请求返回true
    if request.is_ajax():
        username = request.GET.get('corporate_code')
        staff = User.objects.filter(username=username).first()
        if staff:
            return HttpResponse('用户名已存在')
        else:
            return HttpResponse('用户名可用')
    #
    # if request.method == 'GET':
    #     # 可判断用户的登录状态，已登录则返回true
    #     if request.user.is_authenticated():
    #         return redirect('/')
    #     return render(request, 'users/reg.html')

    if request.method == 'POST':
        corporate_name = request.POST.get("corporate_name", '')
        corporate_code = request.POST.get("corporate_code", '')
        # password = request.POST.get("password", '')
        password = make_password(request.POST.get("password", ''))
        cpassword = request.POST.get("cpassword", '')
        passworded = make_password(request.POST.get("password", ''))
        corporate_contacts = request.POST.get("corporate_contacts", '')
        corporate_phone = request.POST.get("corporate_phone", '')
        corporate_email = request.POST.get("corporate_email", '')
        is_superuser = 0
        d1 = timezone.now()
        # date_joined = d1.strftime("%Y-%m-%d")
        date_joined = d1
        # print(corporate_name)
        # print(corporate_code)
        # 从请求消息中 获取要添加的信息
        # 并且插入到数据库中
        # 返回值 就是对应插入记录的对象
        users = User.objects.filter(username=corporate_code)

        if request.POST.get('password') != request.POST.get('cpassword'):
            return render(request, 'users/register.html', {'message': '两次密码不一致'})
        if len(users) > 0:
            return render(request, 'users/register.html', {'message': '用户名已存在'})
        else:
            record = User.objects.create(username=corporate_code,
                                         email=corporate_email,
                                         password=password,
                                         is_superuser=is_superuser,
                                         date_joined=date_joined)

            companyrecord = models.Company.objects.create(userId=record.id,
                                                          email=corporate_email,
                                                          companyName=corporate_name,
                                                          code=corporate_code,
                                                          contacts=corporate_contacts,
                                                          phone=corporate_phone)

            print("新增用户：" + companyrecord.companyName + ",统一信用代码：" + companyrecord.code)
            print("电子邮箱：" + record.email)
            print("联系人：" + companyrecord.contacts)
            print("联系电话：" + companyrecord.phone)
            print("关联ID：" + str(companyrecord.userId))
            # # 将注册用户对象加入request中，对应键值为:user
            # auth.login(request, User)
            return redirect('/')


def listmanage(request):
    qs = User.objects.filter(is_superuser=1)
    print("ID：" + str(qs))
    return render(request, 'users/managelist.html', {'managelist': qs})


def managdd(uid):
    outStr = uid
    return outStr


def listcompany(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    # qs = Company.objects.values()
    qs = Company.objects.all()

    # # 检查url中是否有参数phonenumber
    # ph =  request.GET.get('is_luck',None)
    # # 如果有，添加过滤条件
    # if ph:
    #     qs = qs.filter(is_luck=ph)

    # 定义返回字符串
    # retStr = ''
    # for company in qs:
    #     for name, value in company.items():
    #         retStr += f'{name} : {value} | '
    #
    #     # <br> 表示换行
    #     retStr += '<br>'
    # print(qs)
    # return HttpResponse(retStr)
    return render(request, 'users/userlist.html', {'userlist': qs})


def editmanage(request):
    uid = request.GET.get('id')
    print(uid)
    qs = User.objects.get(id=uid)
    print(qs)
    return render(request, 'users/manageedit.html', {'manageinfo': qs})


def manageReset(request):
    uid = request.GET.get('id')
    qs = User.objects.get(id=uid)
    password = make_password('nfc!@123$%')
    # password = make_password('nfc!@123$%', None, 'pbkdf2_sha256')
    qs.password = password
    qs.save()
    print(uid, password)
    isSame = check_password('nfc!@123$%', password)
    print("isSame：" + str(isSame))
    return render(request, 'users/managelist.html', {'manageid': uid})


def userReset(request):
    uid = request.GET.get('id')
    qs = User.objects.get(id=uid)
    password = make_password('nfc!@123$%')
    # password = make_password('nfc!@123', None, 'pbkdf2_sha256')
    qs.password = password
    qs.save()
    print(uid, password)
    isSame = check_password('nfc!@123$%', password)
    print("isSame：" + str(isSame))
    return render(request, 'users/userlist.html', {'manageid': uid})


def deletemanage(request):
    uid = request.GET.get('id')
    qs = User.objects.get(id=uid).delete()
    print(qs)
    return render(request, 'users/managelist.html', {'manageid': uid})


@csrf_exempt
def deleteuser(request):
    uid = request.GET.get('id')
    us = Company.objects.get(companyId=uid)
    print(uid)
    du = User.objects.get(id=us.userId).delete()
    dc = Company.objects.get(companyId=uid).delete()
    return render(request, 'users/userlist.html', {'manageid': uid})
    #
    # qs = Company.objects.all()
    # return render(request, 'users/userlist.html', {'userlist': qs})


def manageadd_views(request):
    qs = Group.objects.all()
    return render(request, 'users/manageadd.html', {'groupList': qs})


def manageedit_views(request):
    uid = request.GET.get('id')
    print(uid)
    gs = Group.objects.all()
    print(gs)
    us = User.objects.get(id=uid)
    try:
        ug = UserGroups.objects.get(userID=uid)
    except Exception as e:
        ug = ""
    return render(request, 'users/manageedit.html', {'userinfo': us, 'groupList': gs, 'userGroups': ug})


def manageaddsave(request):
    username = request.POST.get("username", '')
    corporate_code = request.POST.get("corporate_code", '')
    password = make_password(request.POST.get("password", ''))
    is_superuser = request.POST.get("is_superuser", '')
    group_id = request.POST.get("group_id", '')
    is_staff = 1
    is_active = 0
    d1 = timezone.now()
    # date_joined = d1.strftime("%Y-%m-%d")
    date_joined = d1
    # print(corporate_name)
    # print(corporate_code)
    # 从请求消息中 获取要添加的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    users = User.objects.filter(username=username)
    # 如果能找到用户
    if len(users) > 0:
        print("用户[" + username + "]已存在，无法新增。")
        response = HttpResponse()
        response.write("<script>alert('账号已存在！');window.location.href='/users/manageadd/';</script>")
        return response
        # return HttpResponse('账号已存在！')
    else:
        record = User.objects.create(username=username,
                                     password=password,
                                     is_superuser=is_superuser,
                                     is_staff=is_staff,
                                     is_active=is_active,
                                     first_name='',
                                     last_name='',
                                     email='',
                                     date_joined=date_joined)
        recroup = UserGroups.objects.create(userID=record.id,
                                            groupID=group_id)
        print("新增用户：" + record.username + ",所在用户组：" + recroup.ID)
        # return render(request, 'users/register.html')
    return HttpResponseRedirect('/users/managelist/')


def manageeditsave(request):
    global update
    response = HttpResponse()
    username = request.POST.get("username")
    password = request.POST.get("password")

    userid = request.POST.get("userid")
    groupID = request.POST.get("groupID")  # 旧
    group_id = request.POST.get("group_id")  # 新
    try:
        # 根据 id 从数据库中找到相应的户记录
        update = User.objects.get(id=userid)
        update.username = username
        if request.POST.get("password"):
            update.password = password
        update.save()
        try:
            updateug = UserGroups.objects.get(userID=userid)
            updateug.groupID = group_id
            updateug.save()
            print("用户组存在，进行修改操作")
        except UserGroups.DoesNotExist:
            print("用户组不存在，进行新增操作")
            recroup = UserGroups.objects.create(userID=userid,
                                                groupID=group_id)
            print("用户组新增操作成功！")

    except User.DoesNotExist:
        print("用户不存在：" + str(username))
    return HttpResponseRedirect('/users/managelist/')


def manageup(request):
    response = HttpResponse()
    if request.FILES.get("up_file"):
        print("路径：" + str(request.FILES.get("up_file")))
        furl = upload(request.FILES.get("up_file"), 0, request)
        print("返回附件路径：" + str(furl))
        userdb(furl)  # 附件明细插入数据库
        return HttpResponseRedirect('/users/managelist/')
        # response.write("<script>alert('导入成功！');window.location.href='/users/managelist/';</script>")
    else:
        return HttpResponse('请选择需要导入的表格！   [ <a href="javascript:history.go(-1)">返回</a> ]')


def myinfo(request):
    username = request.session['username']
    userid = request.session['userid']
    print(userid)
    qs = User.objects.get(id=userid)
    print(qs)
    return render(request, 'users/myinfo.html', {'myinfo': qs})


def ddbd(request):
    userid = 0
    if request.GET.get('userID'):
        userid = request.GET.get('userID')
    else:
        userid = request.session['userid']
    return render(request, 'users/ddbd.html', {'userid': userid})


def DDbdu(request):
    userid = request.session['userid']
    return render(request, 'users/ddbd.html', {'userid': userid})
