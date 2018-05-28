from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

import shopcart,users
from . import models
# Create your views here.
def order_confirm(request):
    '''
    结算确认
    :param request:
    :return:
    '''
    #获取数据
    shopcart_id_list = request.POST.getlist('buy_goods_id')
    print(shopcart_id_list)
    shopcart_list = shopcart.models.Shopcart.objects.filter(pk__in=shopcart_id_list)
    print(shopcart_list)
    return render(request, 'orders/order_confirm.html', {'shopcart_list': shopcart_list})



def order_pay(request):
    '''
    结算付款
    :param request:
    :return:
    '''

    pass


def order_done(request):
    '''
    生成订单
    :param request:
    :return:
    '''
    #获取购买的商品
    shopcart_list = request.POST.getlist('sc')
    #获取收货地址
    addr_id = request.POST['addr_id']
    address = users.models.Address.objects.get(pk=addr_id)
    #拼接地址
    addr = address.recv + ";" + address.phone + ";" + address.nation + ";" + address.province \
           + ";" + address.city + ";" + address.country + ";" + address.street + ";" + address.intro
    total = 0
    #生成订单
    myorder = models.MyOrder(user=request.user, address=addr, total=total)
    myorder.save()
    #创建订单对象
    for sc_id in shopcart_list:
        #查询购物对象
        _shopcart = shopcart.models.Shopcart.objects.get(pk=sc_id)
        #创建订单对象
        order_item = models.MyOrderItem(goods_img=_shopcart.goods.goodsimage_set.first().path,\
                                        goods_name=_shopcart.goods.name,\
                                        goods_price=_shopcart.goods.price,\
                                        goods_count=_shopcart.count,\
                                        goods_subtotal=_shopcart.subtoal,\
                                        myorder=myorder
                                        )
        order_item.save()
        #计算总金额
        total += _shopcart.subtoal
    #更新总金额
    myorder.total =total
    myorder.save()
    #保存跳转到订单详情页面
    return redirect(reverse('orders:order_info', kwargs={'order_id': myorder.id}))


def order_list(request):
    '''
    查询所有订单
    :param request:
    :return:
    '''

    order_list = models.MyOrder.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'order_list': order_list})

def order_info(request,order_id):
    '''
    订单详情
    :param request:
    :return:
    '''
    #查询订单
    _order = models.MyOrder.objects.get(pk=order_id)
    return render(request, 'orders/order_info.html', {'order': _order})

