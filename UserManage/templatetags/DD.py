# 菜鸟程序员：阿米
from django import template
register = template.Library()


@register.filter(name="managdd")
def managdd(uid: str):
    return uid