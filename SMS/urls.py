from django.urls import path
from SMS.views import *

urlpatterns = [
    path('index/', index),
    path('tologin/', tologin_views),
    path('login/', login_views),
]
