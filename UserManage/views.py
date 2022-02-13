import os.path

from django.http import HttpResponse
from django.shortcuts import render

import UserManage
from common import models


def index_views(request):
    return HttpResponse('欢迎登录用户管理！')


def register_views(request):
    return render(request, 'users/register.html')


def adduser(request):
    corporate_name = request.POST.get("corporate_name", '')
    corporate_code = request.POST.get("corporate_code", '')
    password = request.POST.get("password", '')
    corporate_contacts = request.POST.get("corporate_contacts", '')
    corporate_phone = request.POST.get("corporate_phone", '')
    print(corporate_name)
    print(corporate_code)
    # 从请求消息中 获取要添加的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    # record = models.AuthUser.objects.create(corporate_name=corporate_name,
    #                                         corporate_code=corporate_code,
    #                                         password=password,
    #                                         corporate_contacts=corporate_contacts,
    #                                         corporate_phone=corporate_phone)

    record = models.AuthUser.objects.create(username=corporate_name,
                                            email=corporate_code)
    return render(request, 'users/register.html')
