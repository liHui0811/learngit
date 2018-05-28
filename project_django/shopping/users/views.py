from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# authenticate:身份认证[判断账号密码是否正确]login[记录登录状态]，logout[记录销毁登录状态]
from django.contrib.auth import authenticate, login, logout


from . import models


# Create your views here.

def user_register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {})
    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        userpass = request.POST['userpass']
        re_userpass = request.POST['re_userpass']
        nickname = request.POST['nickname']

        # 判断账号是否可用
        try:
            user = User.objects.get(username=username)
            return render(request, 'users/register.html', {'error_code': '-1', 'error_msg': '该账号已被注册，请用其他账号注册'})
        except:
            # 判断昵称是否可用
            try:
                nickname = User.userprofile.objects.get(nickname=nickname)
                return render(request, 'users/register.html', {'error_code': -2, 'error_msg': '该昵称已被占用，请使用其他昵称'})
            except:
                # 判断两次密码是否一致
                if userpass != re_userpass:
                    return render(request, 'users/register.html', {'error_code': -3, 'error_msg': '两次输入密码不一致'})

                    #
                    # 创建用户注册
            user = User.objects.create_user(username=username, password=userpass)
            # 创建用户资料
            userprofile = models.UserProfile(nickname=nickname, phone='待完善', gender='待完善', user=user)
            user.save()
            userprofile.save()
            return render(request, 'users/login.html', {'error_code': 1, 'error_msg': '账号注册成功，请使用新用户登录'})


def user_login(request):
    '''
    用户登录
    :param request:
    :return:
    '''
    if request.method == 'GET':
        #登录之后要跳转的下一个路径
        try:
            next_url = request.GET['next']
        except:
            next_url = '/'
        return render(request, 'users/login.html', {'next_url': next_url})

    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        userpass = request.POST['userpass']
        next_url = request.POST['next_url']#跳转的下一个页面路径

        # 判断账号密码是否正确

        user = authenticate(username=username, password=userpass)

        if user is not None:
            # 验证账号是否锁定
            if user.is_active:
                #记录登录状态
                login(request, user)
                print (next_url)
                # return render(request, 'users/login.html', {'error_code': 0, 'error_msg': '登录成功'})
                # return redirect(reverse('commen:index'))
                return redirect(next_url)
            else:
                return render(request, 'users/login.html', {'error_code': -2, 'error_msg': '账号被锁定，请联系管理员'})
        else:
            return render(request, 'users/login.html', {'error_code': -1, 'error_msg': '账号或密码不正确，请重新输入'})


def user_logout(request):
    '''
    用户退出
    :param request:
    :return:
    '''
    logout(request)
    return render(request, 'commen/index.html', {'error_code': 1, 'error_msg': '账号已成功退出'})

def address_add(request):
    '''
    添加地址
    :param requset:
    :return:
    '''
    if request.method == "GET":
        return render(request, 'users/address_add.html', {})

    elif request.method == "POST":
        #获取数据,添加地址
        recv = request.POST['recv']
        phone = request.POST['phone']
        nation = request.POST['nation']
        province = request.POST['province']
        city = request.POST['city']
        country = request.POST['country']
        street = request.POST['street']
        intro = request.POST['intro']
        try:
            set_default = request.POST['set_default']
            #修改原有的地址为非默认地址
            address_list = models.Address.objects.filter(user=request.user)
            for addr in address_list:
                addr.status = False
                addr.save()

            address = models.Address(nation=nation, province=province, city=city,\
                                     country=country, street=street, intro=intro,\
                                     recv=recv, phone=phone, status=True, user=request.user
                                     )
        except:
            address = models.Address(nation=nation, province=province, city=city, \
                                     country=country, street=street, intro=intro, \
                                     recv=recv, phone=phone, status=False, user=request.user
                                     )
        address.save()

        return redirect(reverse('users:address_list'))


def address_list(request):
    '''
    查看所有地址
    :param requset:
    :return:
    '''
    _address_list = models.Address.objects.filter(user=request.user)
    return render(request, 'users/address_list.html', {'address_list': _address_list})