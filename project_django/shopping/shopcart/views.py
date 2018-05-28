from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
#Q 条件对象
#F 原始值对象
from django.db.models import Q, F

from .import models
import goods
# Create your views here.


def shopcart_add(request, goods_id, count):
    '''
    添加商品goods,购买count数量到购物车
    :param request:
    :param goods_id:
    :param count:
    :return:
    '''
    #得到用户够买的商品
    _goods = goods.models.Goods.objects.get(pk=goods_id)
    try:
        #查询当前用户购物车中是否包含该商品
        shopcart = models.Shopcart.objects.get(Q(user=request.user) & Q(goods=_goods))
        shopcart.count += int(count)
        shopcart.subtoal = shopcart.count * _goods.price
        shopcart.save()

    except Exception as e:
        print ('------->', e)
        #如果不包含创建购物对象,添加到购物车中
        shopcart = models.Shopcart(goods=_goods, count=count, user=request.user)
        shopcart.subtoal = float(count) * _goods.price
        shopcart.save()
    return HttpResponse('商品添加成功')
    # return redirect(reverse('shopcart:shopcart_info'))



def shopcart_info(request):
    '''
    查看购物车
    :param request:
    :return:
    '''
    shopcart_list = models.Shopcart.objects.filter(user=request.user).order_by('-add_time')
    return render(request, 'shopcart/shopcart_info.html', {'shopcart_list': shopcart_list})























