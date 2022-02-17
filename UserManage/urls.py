# 菜鸟程序员：阿米
from django.urls import path
from UserManage.views import index_views, register_views, adduser, reg, userlist,listcompany

urlpatterns = [
    path('', index_views, name='index'),
    path('index/', index_views, name='index'),
    path('register/', register_views, name='register'),
    path('reg/', reg, name='reg'),
    path('adduser/', adduser, name='adduser'),
    path('userlist/', userlist, name='adduser'),
    path('managelist/', listcompany, name='adduser'),
]
