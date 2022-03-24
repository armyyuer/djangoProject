# 菜鸟程序员：阿米
from django.urls import path
from project.views import index_views, projectadd, projectaddsave, upfile, delete, edit_views, editsave, edititemsave,\
    deleteitem, projectItemadd, additemsave

urlpatterns = [
    path('index/', index_views, name='index'),
    path('projectadd/', projectadd, name='projectadd'),
    path('projectItemadd/', projectItemadd, name='projectItemadd'),
    path('projectaddsave/', projectaddsave, name='projectaddsave'),
    path('upfile/', upfile, name='upfile'),
    path('delete/', delete, name='delete'),
    path('edit/', edit_views, name='edit'),
    path('editsave/', editsave, name='editsave'),
    path('edititemsave/', edititemsave, name='edititemsave'),
    path('additemsave/', additemsave, name='additemsave'),
    path('deleteitem/', deleteitem, name='deleteitem'),
]
