#conding=utf-8
from django.shortcuts import render, redirect
from hashlib import sha1
from django.http import JsonResponse

from df_user.models import UserInfo

def register(request):
    return render(request,'df_user/register.html')

#注册提交
def register_handle(request):
    #接收用户密码
    post = request.POST
    name = post.get('name')
    email = post.get('email')
    userName = post.get('userName')
    passWord = post.get('passWord')
    confirmPwd = post.get('confirmPwd')
    phoneNumber = post.get('phoneNumber')
    #判断两次密码
    if passWord != confirmPwd:
        return redirect('/user/register')
    #密码加密
    s1 = sha1()
    s1.update(str(passWord).encode('utf-8'))
    passwordSha1 = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.name = name
    user.email = email
    user.userName = userName
    user.passWord = passwordSha1
    user.phoneNumber = phoneNumber
    user.save()
    #注册成功，转到登录页面
    return redirect('/user/login/')

#根据用户名个数判断用户名是否存在
def register_exist(request):
    userName = request.GET.get('userName')
    count = UserInfo.objects.filter(userName=userName).count()
    return JsonResponse({'count':count})

#登录页面
def login(request):
    userNmae = request.COOKIES.get('userName')
    context = {'title':'用户登录','error_name': 0,'error_pwd': 0,'userName':userNmae}
    return render(request,'df_user/login.html',context)

#登录提交
def login_handle():
    #8:53
