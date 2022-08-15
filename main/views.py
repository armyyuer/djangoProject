from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from django.utils.safestring import mark_safe

from login.ck import auth
from common import models
from common.models import Menu


@auth
def index(request):
    html = ""
    b_menus = Menu.objects.filter(parentID=0).order_by('od')
    for b in b_menus:
        html += "<li>"
        if menus_num(b.menuID) > 0:
            html += "<a href=\"" + b.url + "\"><i class=\"" + b.icon + "\"></i> <span class=\"nav-label\">" + b.menuName + " </span><span class=\"fa arrow\"></span></a>"
            html += "<ul class=\"nav nav-second-level\">"
            html += "<li><a class=\"J_menuItem\" href=\"mailbox.html\">收件箱</a>"
            html += "</li>"
            html += "<li><a class=\"J_menuItem\" href=\"mail_detail.html\">查看邮件</a>"
            html += "</li>"
            html += "<li><a class=\"J_menuItem\" href=\"mail_compose.html\">写信</a>"
            html += "</li>"
            html += "</ul>"
        else:
            html += "<a class=\"J_menuItem\" href=\"" + b.url + "\"><i class=\"" + b.icon + "\"></i> <span class=\"nav-label\">" + b.menuName + " </span></a>"
        html += "</li>"
        print(html)
    return render(request, 'main/index.html', {'html': mark_safe(html)})


@auth
def desktop_views(request):
    username = request.session['username']
    userid = request.session['userid']
    return render(request, 'main/desktop.html', {'username': username, 'userid': userid})


def menus_num(pid=0):
    qs = Menu.objects.filter(parentID=pid).count()
    return qs
