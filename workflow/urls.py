# 菜鸟程序员：阿米
from django.urls import path
from workflow.views import type_views, def_views, list, typeadd, typeedit, typeeditsave, typedel, wf, wfinfo, wfdel, wfadd, wfaddsave, wfinfosave
urlpatterns = [
    path('index/', type_views, name='type_views'),
    path('type/', type_views, name='type_views'),
    path('typeadd/', typeadd, name='typeadd'),
    path('typedel/', typedel, name='typedel'),
    path('typeedit/', typeedit, name='typeedit'),
    path('typeeditsave/', typeeditsave, name='typeeditsave'),
    path('def/', def_views, name='def_views'),
    path('wf/', wf, name='wf'),
    path('wfadd/', wfadd, name='wfadd'),
    path('wfaddsave/', wfaddsave, name='wfaddsave'),
    path('wfinfo/', wfinfo, name='wfinfo'),
    path('wfinfosave/', wfinfosave, name='wfinfosave'),
    path('wfdel/', wfdel, name='wfdel'),
    path('list/', list, name='list'),

]
