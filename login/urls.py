# 菜鸟程序员：阿米
from django.urls import path
from login.views import tologin_views, login_views
from login import sign_in_out

urlpatterns = [
    path('', tologin_views, name='index'),
    path('index/', tologin_views, name='index'),
    path('tologin/', tologin_views, name='tologin'),
    path('signin/', sign_in_out.signin, name='signin'),
]
