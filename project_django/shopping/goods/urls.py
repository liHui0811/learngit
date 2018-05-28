from django.conf.urls import url

from . import views

app_name = 'goods'

urlpatterns = [
    url(r'^(?P<store_id>\d+)/goods_upload/$', views.goods_upload, name='goods_upload'),
    url(r'^(?P<goods_id>\d+)/goods_info/$', views.goods_info, name='goods_info'),
    url(r'^(?P<goods_id>\d+)/goods_update/$', views.goods_update, name='goods_update'),
    url(r'^goodstype/$', views.goodstype, name='goodstype'),
]