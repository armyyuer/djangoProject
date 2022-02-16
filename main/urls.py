# 菜鸟程序员：阿米
from django.urls import path
from main.views import index, desktop_views

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('desktop/', desktop_views, name='desktop'),
]
