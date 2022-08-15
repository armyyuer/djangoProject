# 菜鸟程序员：阿米
from django.urls import path
from Ser.views import index_views

urlpatterns = [
    path('', index_views, name='index'),
    path('index/', index_views, name='index'),
]
