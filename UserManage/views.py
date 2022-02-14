import os.path

from django.http import HttpResponse
from django.shortcuts import render

from common import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.utils import timezone


def index_views(request):
    return HttpResponse('欢迎登录用户管理！')


def register_views(request):
    return render(request, 'users/register.html')


def adduser(request):
    corporate_name = request.POST.get("corporate_name", '')
    corporate_code = request.POST.get("corporate_code", '')
    password = make_password(request.POST.get("password", ''))
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
    Users = User.objects.get(username=corporate_code)

    # 如果能找到用户，并且密码正确
    if Users is not None:
        # return render(request, 'users/register.html')
        return HttpResponse('企业已存在！')
    else:
        record = User.objects.create(username=corporate_code,
                                     email=corporate_email,
                                     password=password,
                                     is_superuser=is_superuser,
                                     date_joined=date_joined)

        Companyrecord = models.Company.objects.create(userId=record.id,
                                                      email=corporate_email,
                                                      companyName=corporate_name,
                                                      code=corporate_code,
                                                      contacts=corporate_contacts,
                                                      phone=corporate_phone)

        print("新增用户："+Companyrecord.companyName+",统一信用代码："+Companyrecord.code)
        print("电子邮箱："+record.email)
        print("联系人："+Companyrecord.contacts)
        print("联系电话："+Companyrecord.phone)
        print("关联ID："+str(Companyrecord.userId))
        # return render(request, 'users/register.html')
        return HttpResponse('注册成功！')
