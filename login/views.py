import os.path

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('欢迎登录首页！')


def tologin_views(request):
    # return HttpResponse('登录系统！')
    return render(request, 'login/index.html')


def login_views(request):
    return HttpResponse('登录系统信息！')


def login_err(request):
    txt = request.GET.get('txt')
    return render(request, 'login/err.html', {'txt': txt})