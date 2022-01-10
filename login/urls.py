# 菜鸟程序员：阿米
from django.urls import path
from login.views import *

urlpatterns = [
    path('', tologin_views),
    path('index/', tologin_views),
    path('tologin/', tologin_views),
    path('login/', login_views),
]
