from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from common.models import Group, Menu, GroupPermissions
from django.http import HttpResponseRedirect


def index(request):
    qs = Group.objects.all().order_by("groupID")
    return render(request, 'group/index.html', {'GroupList': qs})


def groupadd(request):
    groupName = request.POST.get("groupName", '')
    record = Group.objects.create(groupName=groupName)
    print("新增用户组：" + record.groupName)
    return HttpResponseRedirect('/group/index/')


def groupdel(request):
    groupID = request.GET.get('groupID')
    il = Group.objects.get(groupID=groupID).delete()
    print("删除权限组")
    try:
        gp = GroupPermissions.objects.filter(groupID=groupID)
        Perml = GroupPermissions.objects.filter(groupID=groupID).delete()
        print("删除用户组下的权限数据")
    except Menu.DoesNotExist:
        print("本权限组下无权限数据")
    return HttpResponseRedirect('/group/index/')


def grouppermissions(request):
    groupID = request.GET.get("groupID", '')
    qs = Group.objects.get(groupID=groupID)
    groupName = qs.groupName
    MenuList = Menu.objects.filter(parentID=0)
    return render(request, 'group/grouppermissions.html',
                  {'groupName': groupName, 'groupID': groupID, 'menuList': MenuList})


def grouppermissionssave(request):
    groupID = request.POST.get('groupID')
    print(groupID)
    response = HttpResponse()
    if request.POST.getlist('permissions'):
        permissions = request.POST.getlist('permissions')
        print(permissions)
        gpl = GroupPermissions.objects.filter(groupID=groupID).delete()
        print("删除groupID=" + groupID)
        for p in permissions:
            print(p)
            record = GroupPermissions.objects.create(groupID=groupID,
                                                     permissionID=p)
            print(record.permissionID + "添加成功！")
        return HttpResponseRedirect('/group/index/')
    else:
        response.write(
            "<script>alert('清选择目录菜单功能！');window.location.href='/group/grouppermissions/?groupID=" + groupID + "';</script>")
        return response
