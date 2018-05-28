from django.conf.urls import url

from . import views

app_name = 'orders'

urlpatterns = [
    #结算确认,展示用户要购买的商品,同时检查是否有收货地址
    url(r'^order_confirm/$', views.order_confirm, name='order_confirm'),
    #结算付款,展示对应的付款页面,进行金钱操作
    url(r'^order_pay/$', views.order_pay, name='order_pay'),
    #生成订单
    url(r'^order_done/$', views.order_done, name='order_done'),
    #查询订单
    url(r'^order_list/$', views.order_list, name='order_list'),
    #查询订单详情
    url(r'^(?P<order_id>\d+)/order_info/$', views.order_info, name='order_info'),
]