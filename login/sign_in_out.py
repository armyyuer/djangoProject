from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from common.models import Company


# 登录处理
def signin(request):
    response = HttpResponse()
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username', '')
    passWord2 = make_password(request.POST.get("password"))
    passWord = request.POST.get('password', '')
    print("username：" + userName)
    print("password：" + passWord)
    print("password2：" + passWord2)

    pw = make_password('nfc!@123')
    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)
    isSame = check_password(passWord, pw)
    print("isSame：" + str(isSame))

    # 如果能找到用户，并且密码正确
    if user is not None:

        du = User.objects.get(username=userName)
        request.session['username'] = userName
        request.session['userid'] = du.id
        request.session['useremail'] = du.email
        dc = Company.objects.get(userId=du.id)
        request.session['companyId'] = dc.companyId
        request.session['companyName'] = dc.companyName
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = '1'

                # return JsonResponse({'ret': 0})
                response.write("<script>alert('管理员"+str(request.session['username'])+"登陆成功！');window.location.href='/';</script>")
                return response
            else:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = '0'
                # return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
                response.write("<script>alert('["+str(request.session['companyName'])+"]登陆成功！');window.location.href='/';</script>")
                return response
        else:
            # return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})
            response.write("<script>alert('用户已经被禁用！');window.location.href='/login';</script>")
            return response

    # 否则就是用户名、密码有误
    else:
        # return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})
        # return HttpResponse('用户名或者密码错误！   [ <a href="javascript:history.go(-1)">返回</a> ]')
        response.write("<script>alert('用户名或者密码错误！');window.location.href='/login';</script>")
        return response


# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    x = ""
    return x
