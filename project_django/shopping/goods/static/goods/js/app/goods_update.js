/**
 * Created by Lisir on 2018/4/2.
 */
/**
 * Created by Lisir on 2018/4/1.
 */
$(function () {
    //当一级类型下拉列表发生改变是，出发改变事件
    $('#type3').change(function () {
        //清空二级类型下拉列表中的所有子元素
        $('#type4').empty()
        $.ajax({
            url: '/goods/goodstype/',
            type: 'GET',
            data: {
                'type_id': $('#type3').val()
            },
            success: function (response) {
                //将服务器中返回的json字符串，转换成json对象
                json_obj = JSON.parse(response)
                // console.log(json_obj)
                for (index in json_obj){
                    //列表取值name,id
                    console.log(json_obj[index].fields.name, json_obj[index].pk)
                    //dom操作将取出来的值显示到网页中二级列表中
                        //为type2创建optin
                    var $option = $('<option>')
                    $option.attr('value',json_obj[index].pk)
                    $option.text(json_obj[index].fields.name)
                    $('#type4').append($option)
                }
            },
            error: function () {
                console.log('请求发送失败')
            }

        })

    })
})