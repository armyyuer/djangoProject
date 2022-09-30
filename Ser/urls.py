# 菜鸟程序员：阿米
from django.urls import path
from Ser.views import index_views, addflow, addflowsave, myorder, myorderinfo, myorderinfosave

urlpatterns = [
    path('', index_views, name='index'),
    path('index/', index_views, name='index'),
    path('addflow/', addflow, name='addflow'),
    path('addflowsave/', addflowsave, name='addflowsave'),
    path('myorder/', myorder, name='myorder'),
    path('myorderinfo/', myorderinfo, name='myorderinfo'),
    path('myorderinfosave/', myorderinfosave, name='myorderinfosave'),
]
