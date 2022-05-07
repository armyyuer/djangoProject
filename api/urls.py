# 菜鸟程序员：阿米
from django.urls import path
from api.views import userinfo, ccgpseed
from api.ccgp import seedtxt

urlpatterns = [
    path('userinfo/', userinfo, name='userinfo'),
    path('ccgpseed/', ccgpseed, name='ccgpseed'),
    path('ccgp/', seedtxt, name='seedtxt'),
]
