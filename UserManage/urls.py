# 菜鸟程序员：阿米
from django.urls import path
from UserManage.views import index_views, register_views, adduser, reg, listmanage, listcompany, editmanage, \
    manageReset, deletemanage, deleteuser, manageadd_views, manageaddsave

urlpatterns = [
    path('', index_views, name='index'),
    path('index/', index_views, name='index'),
    path('register/', register_views, name='register'),
    path('reg/', reg, name='reg'),
    path('adduser/', adduser, name='adduser'),
    path('userlist/', listcompany, name='userlist'),
    path('managelist/', listmanage, name='managelist'),
    path('manageedit/', editmanage, name='manageedit'),
    path('manageadd/', manageadd_views, name='manageadd_views'),
    path('manageaddsave/', manageaddsave, name='manageaddsave'),
    path('manageReset/', manageReset, name='manageReset'),
    path('deletemanage/', deletemanage, name='deletemanage'),
    path('deleteuser/', deleteuser, name='deleteuser'),
]
