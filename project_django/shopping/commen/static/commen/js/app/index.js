/**
 * Created by Lisir on 2018/3/31.
 */
$(function () {
    $('.type2li').mouseover(function () {
        $(this).children('ul').css('display','block')
    })
    $('.type2li').mouseout(function () {
        $(this).children('ul').css('display','none')
    })
    $('.addcart').click(function () {
        //获取商品编号
        var $goods_id = $(this).attr('goodsid')
        console.log($goods_id)
        //发送ajax请求
        $.ajax({
            url: '/shopcart/'+$goods_id+ "/" + 1 + '/shopcart_add/',
            type: 'GET',
            success:function (response) {
                alert('商品成功添加到购物车')
            },
            error:function () {
                console.log('请求失败')
            }

        })
    })
})