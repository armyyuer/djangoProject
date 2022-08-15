# 菜鸟程序员：阿米
from django.urls import path
from menu.views import index, menuadd, menuaddsave, menuedit, menueditsave, menudel, permissionadd, permissiondel

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('menuadd/', menuadd, name='menuadd'),
    path('menuaddsave/', menuaddsave, name='menuaddsave'),
    path('menuedit/', menuedit, name='menuedit'),
    path('menueditsave/', menueditsave, name='menueditsave'),
    path('menudel/', menudel, name='menudel'),
    path('permissionadd/', permissionadd, name='permissionadd'),
    path('permissiondel/', permissiondel, name='permissiondel'),
]
