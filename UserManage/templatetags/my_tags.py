# 菜鸟程序员：阿米
from django import template
from common import models
from django.utils.html import format_html
from common.models import DDuser
# 下面代码会直接使用register
register = template.Library()


@register.filter
def my_tag(value, value2=0):
    """
    value: 是必须的参数  是模板过滤器中|前面的值
    value2: 是模板过滤器中 : 后面的值
    """
    txt=""
    users = models.DDuser.objects.filter(uid=value2)
    ddid=""
    if len(users) > 0:
        # for u in users:
        #     ddid= u["userid"]
        txt="已绑定，钉钉id："+users["ddid"]
    else:
        text="现在绑定"
        txt = "未绑定钉钉账号,"+format_html('<a href="#">{}</a>',text)
    return value + txt


@register.filter
def my_id(value, value2=0):
    return value + str(value2)