from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^address_add/$', views.address_add, name='address_add'),
    url(r'^address_list/$', views.address_list, name='address_list'),
]