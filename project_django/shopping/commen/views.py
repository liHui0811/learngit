from django.shortcuts import render
#require_GET装饰器，一般定义在视图函数上，指定视图函数的访问方式
from django.views.decorators.http import require_GET
#login_require装饰器，一般定义在视图函数上，只允许装饰函数的在用户登录之后才能访问
from django.contrib.auth.decorators import login_required

import goods, store

# Create your views here.
# @login_required
@require_GET
def index(request):
    '''
    只允许get方式访问
    :param request:
    :return:
    '''
    # if request.method == 'GET':
    #     return render(request, 'commen/index.html',{})
    #查询所有的商品类型，在首页中展示所有类型
    goodstype_1_list = goods.models.GoodsType.objects.filter(parent__isnull=True)
    #查询所有类型中指定的数据[切片]
    #(1)手机|数码
    goods_type_1 = goods.models.GoodsType.objects.get(pk=1)
    goods_type_1_list = goods.models.GoodsType.objects.filter(parent=goods_type_1)
    goods_list_1 = goods.models.Goods.objects.filter(goodstype__in=goods_type_1_list)[0:5]
    #(2)家居|家装
    goods_type_2 = goods.models.GoodsType.objects.get(pk=2)
    goods_type_2_list = goods.models.GoodsType.objects.filter(parent=goods_type_2)
    goods_list_2 = goods.models.Goods.objects.filter(goodstype__in=goods_type_2_list)[0:5]
    #(3)男装|女装
    goods_type_3 = goods.models.GoodsType.objects.get(pk=3)
    goods_type_3_list = goods.models.GoodsType.objects.filter(parent=goods_type_3)
    goods_list_3 = goods.models.Goods.objects.filter(goodstype__in=goods_type_3_list)[0:5]
    #热门店铺
    store_list = store.models.Store.objects.all()[0:5]
    return render(request, 'commen/index.html', {'goodstype_1_list': goodstype_1_list,\
                                                 'goods_list_1': goods_list_1,\
                                                 'goods_list_2': goods_list_2,\
                                                 'goods_list_3': goods_list_3,\
                                                 'store_list': store_list
                                                 })
