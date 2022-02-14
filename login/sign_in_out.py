from django.contrib.auth import authenticate, login, logout


# 登录处理
def signin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)
    x = ""
    return x


# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    x = ""
    return x
