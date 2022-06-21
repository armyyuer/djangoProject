# 菜鸟程序员：阿米
from django.urls import path
from orders.views import index_views
from ewm.views import generate_qrcode

urlpatterns = [
    # path('', index_views, name='index'),
    path('', generate_qrcode, name='ewm'),
]
