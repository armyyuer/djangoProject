# 菜鸟程序员：阿米
from django.urls import path
from group.views import index, groupadd, groupdel, grouppermissions, grouppermissionssave
urlpatterns = [
    path('index/', index, name='index'),
    path('groupadd/', groupadd, name='groupadd'),
    path('groupdel/', groupdel, name='groupdel'),
    path('grouppermissions/', grouppermissions, name='grouppermissions'),
    path('grouppermissionssave/', grouppermissionssave, name='grouppermissionssave'),

]
