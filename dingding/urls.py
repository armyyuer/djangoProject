# 菜鸟程序员：阿米
from django.urls import path
from dingding.views import dingding_index, get, DDbd, DDbdu, DDbdend, main, desktop, calendar, project, kangyi, uppic, uppicsave, ser, pc, pcget
urlpatterns = [
    path('', dingding_index, name='dingding_index'),
    path('get/', get, name='get'),
    path('DDbd/', DDbd, name='DDbd'),
    path('DDbdu/', DDbdu, name='DDbdu'),
    path('DDbdend/', DDbdend, name='DDbdend'),
    path('main/', main, name='main'),
    path('desktop/', desktop, name='desktop'),
    path('calendar/', calendar, name='calendar'),
    path('project/', project, name='project'),
    path('kangyi/', kangyi, name='kangyi'),
    path('uppic/', uppic, name='uppic'),
    path('uppicsave/', uppicsave, name='uppicsave'),
    path('ser/', ser, name='ser'),
    path('pc/', pc, name='pc'),
    path('pcget/', pcget, name='pcget'),

]
