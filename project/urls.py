# 菜鸟程序员：阿米
from django.urls import path
from project.views import index_views,projectadd

urlpatterns = [
    path('index/', index_views, name='index'),
    path('projectadd/', projectadd, name='projectadd'),
]
