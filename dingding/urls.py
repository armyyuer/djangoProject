# 菜鸟程序员：阿米
from django.urls import path
from dingding.views import dingding_index, get, DDbd
urlpatterns = [
    path('', dingding_index, name='dingding_index'),
    path('get/', get, name='get'),
    path('DDbd/', DDbd, name='DDbd'),

]
