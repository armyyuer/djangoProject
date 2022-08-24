from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from django.utils.safestring import mark_safe

from login.ck import auth
from common import models
from common.models import Menu, GroupPermissions, MenuPermission


@auth
def index(request):
    usergroup = request.session['usergroup']
    # print(usergroup)
    gp = GroupPermissions.objects.filter(groupID=usergroup)
    glist = []
    for g in gp:
        glist.append(g.permissionID)
        # print(str(g.permissionID))

    print(glist, 'glist')
    mp = MenuPermission.objects.filter(permissionID__in=glist)

    midlist = []
    for m in mp:
        midlist.append(m.menuID)
    mlist = []
    for m in mp:
        mlist.append(m.codeName)
    print(mlist, 'mp')
    # l = [1, 1, 3, 2, 2, 3, 4, 2, 5]
    new = []
    newid = []
    for i in mlist:
        if i not in new:
            new.append(i)
    print(new, 'new')
    for i in midlist:
        if i not in newid:
            newid.append(i)
    print(newid, 'newid')

    html = ""
    b_menus = Menu.objects.filter(parentID=0, menuID__in=newid).order_by('od')
    for b in b_menus:
        html += "<li>"
        if menus_num(b.menuID) > 0:
            html += "<a href=\"" + b.url + "\"><i class=\"" + b.icon + "\"></i> <span class=\"nav-label\">" + b.menuName + " </span><span class=\"fa arrow\"></span></a>"
            html += "<ul class=\"nav nav-second-level\">"
            s_menus = Menu.objects.filter(parentID=b.menuID, url__in=new)
            for s in s_menus:
                html += "<li><a class=\"J_menuItem\" href=\"" + s.url + "\">" + s.menuName + "</a>"
                html += "</li>"
            html += "</ul>"
        else:
            html += "<a class=\"J_menuItem\" href=\"" + b.url + "\"><i class=\"" + b.icon + "\"></i> <span class=\"nav-label\">" + b.menuName + " </span></a>"
        html += "</li>"
    return render(request, 'main/index.html', {'html': mark_safe(html)})


@auth
def desktop_views(request):
    username = request.session['username']
    userid = request.session['userid']
    return render(request, 'main/desktop.html', {'username': username, 'userid': userid})


def menus_num(pid=0):
    qs = Menu.objects.filter(parentID=pid).count()
    return qs
