# 菜鸟程序员：阿米
from django import template

from common import models
from django.utils.html import format_html
from common.models import DDuser, Group, UserGroups
from django.utils.safestring import mark_safe

# 下面代码会直接使用register
register = template.Library()


@register.filter
def my_tag(value, value2=0):
    """
    value: 是必须的参数  是模板过滤器中|前面的值
    value2: 是模板过滤器中 : 后面的值
    """
    txt = ""

    try:
        users = DDuser.objects.get(uid=value2)
        print(str(users.name), 'users.name')
        txt = users.name + "[" + users.userid + "]"
    except DDuser.DoesNotExist:
        txt = "<a href=/users/ddbd/?userID=" + str(value2) + ">未绑定，点击绑定</a>"
        # txt = "未绑定，点击绑定"

    return mark_safe(value + txt)


@register.filter
def my_id(value, value2=0):
    return value + str(value2)


@register.filter
def my_group(value, value2=0):
    print(str(value2), 'userID')
    ot = ''
    try:
        qs = UserGroups.objects.get(userID=value2)
        group = Group.objects.get(groupID=qs.groupID)
        ot = group.groupName
    except UserGroups.DoesNotExist:
        ot = '用户组数据异常'
    return value + ot
