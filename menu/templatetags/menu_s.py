# 菜鸟程序员：阿米
from django import template

from common import models
from django.utils.html import format_html
from common.models import Menu, MenuPermission, GroupPermissions
from django.utils.safestring import mark_safe

# 下面代码会直接使用register
register = template.Library()


@register.filter
def menus(value, pid=0):
    qs = Menu.objects.filter(parentID=pid)
    txt = ""
    for m in qs:

        txt += "<p>├- &nbsp;<a href=/menu/menuedit/?menuID=" + str(m.menuID) + ">" + m.menuName + "</a>&nbsp;&nbsp;[ <a href=/menu/menudel/?menuID=" + str(m.menuID) + ">删除</a> ]</p>"
    # return render(request, 'menu/index.html', {'MenuList': qs})
    # return value+txt
    return mark_safe(txt)


@register.filter
def permissions(groupID, menuID=0):
    qs = MenuPermission.objects.filter(menuID=menuID)
    txt = ""
    gs = GroupPermissions.objects.filter(groupID=groupID)
    for m in qs:
        checked = ""
        txt += "<label class=\"checkbox-inline\"><input type=\"checkbox\" name=\"permissions\" value=\"" + str(m.permissionID) + "\" id=\"inlineCheckbox1\""
        for g in gs:
            # print(str(g.permissionID)+","+str(m.permissionID))
            if str(g.permissionID) == str(m.permissionID):
                txt += "checked = \"\""
            else:
                txt += ""
        txt += ">" + m.title +"</label>"
        # txt += "<p>├- &nbsp;<a href=/menu/menuedit/?menuID=" + str(m.menuID) + ">" + m.menuName + "</a>&nbsp;&nbsp;[ <a href=/menu/menudel/?menuID=" + str(m.menuID) + ">删除</a> ]</p>"
    return mark_safe(txt)


@register.filter
def menus_num(value, pid=0):
    qs = Menu.objects.filter(parentID=pid).count()
    return mark_safe(str(qs))


@register.filter
def menus_b(value, pid=0):
    qs = Menu.objects.filter(parentID=pid).count()
    return mark_safe(str(qs))