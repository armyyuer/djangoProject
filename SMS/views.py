from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('欢迎登录首页！')

def tologin_views(request):
    return HttpResponse('登录系统！')

def login_views(request):
    return HttpResponse('登录系统信息！')