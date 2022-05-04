# 菜鸟程序员：阿米
from django.urls import path
from api.views import userinfo

urlpatterns = [
    path('userinfo/', userinfo, name='userinfo'),


]
