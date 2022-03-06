# 菜鸟程序员：阿米
from django.urls import path
from project.views import index_views, projectadd, projectaddsave, upfile

urlpatterns = [
    path('index/', index_views, name='index'),
    path('projectadd/', projectadd, name='projectadd'),
    path('projectaddsave/', projectaddsave, name='projectaddsave'),
    path('upfile/', upfile, name='upfile'),
]
