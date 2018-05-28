from django.conf.urls import url

from . import views

app_name = 'shopcart'

urlpatterns = [
    url(r'(?P<goods_id>\d+)/(?P<count>\d+)/shopcart_add', views.shopcart_add, name='shopcart_add'),
    url(r'shopcart_info/', views.shopcart_info, name='shopcart_info'),

]