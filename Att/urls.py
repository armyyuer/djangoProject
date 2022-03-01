# 菜鸟程序员：阿米
from django.urls import path
from Att.views import up_file

urlpatterns = [
    path('upfile/', up_file, name='upfile'),
]
