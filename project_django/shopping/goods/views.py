from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.serializers import serialize
from datetime import datetime
from . import models
import store


@login_required
def goods_upload(request, store_id):
    '''
    上传商品
    :param request:
    :param store_id:
    :return:
    '''
    if request.method == "GET":
        goods_1_type = models.GoodsType.objects.filter(parent__isnull=True)
        return render(request, 'goods/goods_upload.html', {'store_id': store_id, 'goods_1_type': goods_1_type})
    elif request.method == 'POST':  # 获取数据
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        intro = request.POST['intro']
        imgpath = request.FILES['imgpath']

        # 其他数据,获取商品类型及所属店铺
        type_id = request.POST['type2']
        goodstype = models.GoodsType.objects.get(pk=type_id)
        _store = store.models.Store.objects.get(pk=store_id)

        # 创建商品对象，完成上传操作
        goods = models.Goods(name=name, price=price, stock=stock, \
                             intro=intro, goodstype=goodstype, \
                             store=_store, sale=0)
        goods.save()
        # 创建商品图片对象，保存商品图片
        goods_image = models.GoodsImage(path=imgpath, goods=goods)
        goods_image.save()
    return redirect(reverse('goods:goods_info', kwargs={'goods_id': goods.id}))




def goods_info(request, goods_id):
    '''
    商品详情
    :param request:
    :param goods_id:
    :return:
    '''
    # 查询具体的商品
    goods = models.Goods.objects.get(pk=goods_id)
    return render(request, 'goods/goods_info.html', {'goods': goods})


def goodstype(request):
    # 获取类型编号并查询一级类型对象
    type_id = request.GET['type_id']
    goods_type = models.GoodsType.objects.get(pk=type_id)
    # 查询二级类型对象???
    good_type2_list = models.GoodsType.objects.filter(parent=goods_type)
    # 返回查询到的数据
    return HttpResponse(serialize('json', good_type2_list))


def goods_update(request, goods_id):
    '''
    修改商品信息
    :param request:
    :param goods_id:
    :return:
    '''
    goods = models.Goods.objects.get(pk=goods_id)
    if request.method == 'GET':
        goods_1_type = models.GoodsType.objects.filter(parent__isnull=True)

        return render(request, 'goods/goods_update.html',
                  {'goods_id': goods_id, 'goods': goods, 'goods_1_type': goods_1_type})
    elif request.method == 'POST':
        # 获取数据
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        intro = request.POST['intro']

        # 其他数据,获取商品类型及所属店铺
        # type_id = request.POST['type2']
        # goodstype = models.GoodsType.objects.get(pk=type_id)
        # _store = store.models.Store.objects.get(pk=store_id)

        # 创建商品对象，完成修改
        goods.name = name
        goods.price = price
        goods.stock = stock
        goods.intro = intro

        goods.save()
        # 创建商品图片对象，保存商品图片
        goods_image = models.GoodsImage.objects.get(pk=goods_id)

        path = request.FILES['imgpath']
        goods_image.path = path
        goods_image.save()


        return redirect(reverse('goods:goods_info', kwargs={'goods_id': goods.id}))
