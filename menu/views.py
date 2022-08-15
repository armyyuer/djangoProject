from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from common.models import Menu, MenuPermission
from login.ck import auth
from django.utils.safestring import mark_safe


@auth
def index(request):
    qs = Menu.objects.filter(parentID=0)
    return render(request, 'menu/index.html', {'MenuList': qs})


def menuadd(request):
    qs = Menu.objects.filter(parentID=0)
    return render(request, 'menu/add.html', {'MenuList': qs})


def menuaddsave(request):
    parentID = request.POST.get("parentID", '')
    menuName = request.POST.get("menuName", '')
    icon = request.POST.get("icon", '')
    od = request.POST.get("od", '')
    url = request.POST.get("url", '')
    code = request.POST.get("code", '')
    record = Menu.objects.create(menuName=menuName,
                                 parentID=parentID,
                                 icon=icon,
                                 od=od,
                                 url=url,
                                 code=code,
                                 img='')
    print("新增菜单：" + record.menuName)
    # return render(request, 'menu/add.html', {'MenuList': qs})
    return HttpResponseRedirect('/menu/index/')


def menuedit(request):
    list = Menu.objects.filter(parentID=0)
    menuID = request.GET.get("menuID", '')
    print(menuID)
    qs = Menu.objects.get(menuID=menuID)
    print(qs.menuName)
    permission = MenuPermission.objects.filter(menuID=menuID)
    return render(request, 'menu/edit.html', {'menuInfo': qs, 'list': list, 'permission': permission})


def menueditsave(request):
    menuID = request.POST.get("menuID", '')
    parentID = request.POST.get("parentID", '')
    menuName = request.POST.get("menuName", '')
    icon = request.POST.get("icon", '')
    od = request.POST.get("od", '')
    url = request.POST.get("url", '')
    code = request.POST.get("code", '')
    try:
        # 根据 id 从数据库中找到相应的户记录
        update = Menu.objects.get(menuID=menuID)
    except Menu.DoesNotExist:
        print("菜单不存在" + str(type))
    update.parentID = parentID
    update.menuName = menuName
    update.icon = icon
    update.od = od
    update.url = url
    update.code = code
    update.save()

    # return render(request, 'menu/add.html', {'MenuList': qs})
    return HttpResponseRedirect('/menu/index/')


def menudel(request):
    menuID = request.GET.get('menuID')
    # us = Menu.objects.get(menuID=menuID)
    print(menuID)
    try:
        pm = Menu.objects.get(parentID=menuID)
        pl = Menu.objects.get(parentID=menuID).delete()
        print("删除本菜单下子菜单")
        try:
            Permm = MenuPermission.objects.get(menuID=pm.menuID)
            Perml = MenuPermission.objects.get(menuID=pm.menuID).delete()
            print("删除本菜单下功能模块")
        except Menu.DoesNotExist:
            print("本菜单下无功能模块")
    except Menu.DoesNotExist:
        print("本菜单下无子菜单")
    il = Menu.objects.get(menuID=menuID).delete()
    print("删除本菜单")
    try:
        Permms = MenuPermission.objects.get(menuID=menuID)
        Permls = MenuPermission.objects.get(menuID=menuID).delete()
        print("删除本菜单下功能模块")
    except Menu.DoesNotExist:
        print("本菜单下无功能模块")
    return HttpResponseRedirect('/menu/index/')


def permissionadd(request):
    mID = request.POST.get("mID", '')
    codeName = request.POST.get("codeName", '')
    title = request.POST.get("title", '')
    record = MenuPermission.objects.create(menuID=mID,
                                           codeName=codeName,
                                           title=title)
    print("新增菜单功能：" + record.title)
    # return render(request, 'menu/add.html', {'MenuList': qs})
    return HttpResponseRedirect('/menu/menuedit/?menuID='+mID)


def permissiondel(request):
    permissionID = request.GET.get('permissionID')
    Permls = MenuPermission.objects.get(permissionID=permissionID)
    MenuPermission.objects.get(permissionID=permissionID).delete()
    return HttpResponseRedirect('/menu/menuedit/?menuID='+str(Permls.menuID))
