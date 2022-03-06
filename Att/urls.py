# 菜鸟程序员：阿米
from django.urls import path
from Att.views import up_file_excel, upload, file_down

urlpatterns = [
    path('upfile/', up_file_excel, name='upfile'),
    path('upload/', upload, name='upload'),
    path('file_down/', file_down, name='file_down'),


]
