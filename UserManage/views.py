import os.path
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from common import models
from common.models import Company
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


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

    return render(request, 'users/managelist.html', {'managelist': qs})


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
    isSame = check_password('nfc!@123', password)
    print("isSame：" + str(isSame))
    return render(request, 'users/managelist.html', {'manageid': uid})


def userReset(request):
    uid = request.GET.get('id')
    qs = User.objects.get(id=uid)
    password = make_password('nfc!@123')
    # password = make_password('nfc!@123', None, 'pbkdf2_sha256')
    qs.password = password
    qs.save()
    print(uid, password)
    isSame = check_password('nfc!@123', password)
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
    # return render(request, 'users/register.html')
    return render(request, 'users/manageadd.html')


def manageaddsave(request):
    username = request.POST.get("username", '')
    corporate_code = request.POST.get("corporate_code", '')
    password = make_password(request.POST.get("password", ''))
    is_superuser = request.POST.get("is_superuser", '')
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
        print("新增用户：" + record.username)
        # return render(request, 'users/register.html')
    return HttpResponseRedirect('/users/managelist/')
