# 菜鸟程序员：阿米
from django.urls import path
from workflow.views import type_views, def_views, list
urlpatterns = [
    path('index/', type_views, name='type_views'),
    path('type/', type_views, name='type_views'),
    path('def/', def_views, name='def_views'),
    path('list/', list, name='list'),

]
