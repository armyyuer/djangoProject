# 菜鸟程序员：阿米
from django.urls import path
from UserManage.views import index_views, register_views, adduser, reg, listmanage, listcompany, manageedit_views, \
    manageReset, deletemanage, deleteuser, manageadd_views, manageaddsave, userReset, myinfo, ddbd, manageeditsave, manageup

urlpatterns = [
    path('', index_views, name='index'),
    path('index/', index_views, name='index'),
    path('register/', register_views, name='register'),
    path('reg/', reg, name='reg'),
    path('adduser/', adduser, name='adduser'),
    path('userlist/', listcompany, name='userlist'),
    path('managelist/', listmanage, name='managelist'),
    path('manageedit/', manageedit_views, name='manageedit_views'),
    path('manageadd/', manageadd_views, name='manageadd_views'),
    path('manageup/', manageup, name='manageup'),
    path('manageaddsave/', manageaddsave, name='manageaddsave'),
    path('manageeditsave/', manageeditsave, name='manageeditsave'),
    path('manageReset/', manageReset, name='manageReset'),
    path('userReset/', userReset, name='userReset'),
    path('deletemanage/', deletemanage, name='deletemanage'),
    path('deleteuser/', deleteuser, name='deleteuser'),
    path('myinfo/', myinfo, name='myinfo'),
    path('ddbd/', ddbd, name='ddbd'),
]
