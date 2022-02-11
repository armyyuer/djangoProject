import os.path

from django.http import HttpResponse
from django.shortcuts import render


def index_views(request):
    return HttpResponse('欢迎登录用户管理！')


def register_views(request):
    return render(request,'users/register.html')
