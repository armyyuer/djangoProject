# 菜鸟程序员：阿米
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# PC登陆验证
def auth(func):
    def inner(request, *args, **kwargs):
        response = HttpResponse()
        ck = request.session.get("username")
        '''如果没有登陆返回到login.html'''
        if not ck:
            response.write("<script>alert('请登录账号！');window.location.href='/login';</script>")
            return response
        return func(request, *args, **kwargs)

    return inner


# 钉钉手机端登陆验证
def authDD_m(func):
    def inner(request, *args, **kwargs):
        response = HttpResponse()
        ck = request.session.get("username")
        '''如果没有登陆返回到login.html'''
        if not ck:
            return HttpResponseRedirect("/dingding/")
        return func(request, *args, **kwargs)

    return inner


# 钉钉pc端登陆验证
def authDD_pc(func):
    def inner(request, *args, **kwargs):
        response = HttpResponse()
        ck = request.session.get("username")
        '''如果没有登陆返回到login.html'''
        if not ck:
            return HttpResponseRedirect("/dingding/pc/")
        return func(request, *args, **kwargs)

    return inner
