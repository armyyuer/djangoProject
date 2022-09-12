# 菜鸟程序员：阿米
from django.urls import path
from Ser.views import index_views, addflow, addflowsave

urlpatterns = [
    path('', index_views, name='index'),
    path('index/', index_views, name='index'),
    path('addflow/', addflow, name='addflow'),
    path('addflowsave/', addflowsave, name='addflowsave'),
]
