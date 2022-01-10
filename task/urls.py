# 菜鸟程序员：阿米
from django.urls import path
from task.views import index_views

urlpatterns = [
    path('index/', index_views,name='index'),
]
