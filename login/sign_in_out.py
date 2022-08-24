import hashlib

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from common.models import Company, UserGroups, MenuPermission, GroupPermissions


# 登录处理
def signin(request):
    response = HttpResponse()
    # 从 HTTP POST 请求中获取用户名、密码参数

    userName = request.POST.get('username')
    passWord2 = make_password(request.POST.get("password"))
    passWord = request.POST.get('password')
    # Encry = hashlib.md5()  # 实例化md5
    # Encry.update(passWord.encode())  # 字符串字节加密
    # password3 = Encry.hexdigest()  # 字符串加密
    print("username：" + userName)
    print("password：" + passWord)
    print("password2：" + passWord2)
    # print("password3：" + str(password3))

    pw = make_password('nfc!@123$%')
    # 使用 Django auth 库里面的 方法校验用户名、密码
    # user = authenticate(username=userName, password=password3)
    user = User.objects.get(username=userName)
    # if user:
    #     print("u：" + str(user))
        # uer = User.objects.filter(username=userName, password=passWord2)
        # uer = authenticate(username=userName, password=passWord)
        # print("uer：" + str(uer))

    if user:
        isSame = check_password(passWord, user.password)
        print("isSame：" + str(isSame))
        # print("user：" + str(user[0]))

        # 验证密码如果正确
        if isSame:
            print("userID：" + str(user.id))
            du = User.objects.get(username=userName)
            request.session['username'] = userName
            request.session['userid'] = du.id
            request.session['useremail'] = du.email
            um = UserGroups.objects.get(userID=user.id)
            request.session['usergroup'] = um.groupID
            gl = GroupPermissions.objects.filter(groupID=um.groupID)
            glist = []
            for g in gl:
                glist.append(g.permissionID)

            mp = MenuPermission.objects.filter(permissionID__in=glist)

            mlist = []
            for m in mp:
                mlist.append(m.codeName)
            print(mlist, 'mcodeName')
            request.session['permissions'] = mlist
            # dc = Company.objects.get(userId=du.id)
            # request.session['companyId'] = dc.companyId
            # request.session['companyName'] = dc.companyName
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    # 在session中存入用户类型
                    request.session['usertype'] = '1'

                    # return JsonResponse({'ret': 0})
                    response.write("<script>alert('" + str(userName) + "登陆成功！');window.location.href='/';</script>")
                    return HttpResponseRedirect('/')

                else:
                    login(request, user)
                    # 在session中存入用户类型
                    request.session['usertype'] = '0'
                    # return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
                    response.write("<script>alert('[" + str(
                        request.session['companyName']) + "]登陆成功！');window.location.href='/';</script>")
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
    response = HttpResponse()
    # 使用登出方法
    logout(request)
    response.write("<script>alert('登出成功！');window.location.href='/login';</script>")
    return response
