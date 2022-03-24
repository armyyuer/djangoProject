# 菜鸟程序员：阿米
from django.urls import path
from orders.views import index_views, show_views

urlpatterns = [
    path('index/', index_views, name='index'),
    path('show/', show_views, name='show'),
]
