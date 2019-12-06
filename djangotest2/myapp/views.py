#coding=UTF-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def hello(request):
    #return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'  # 数据绑定
    return render(request, 'hello.html', context)  # 将绑定的数据传入前台

def test(request):
    #return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'  # 数据绑定
    return render(request, 'test123.html', context)  # 将绑定的数据传入前台

def index(request):
    #return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'  # 数据绑定
    return render(request, 'index.html', context)  # 将绑定的数据传入前台

def login_action(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username == 'admin' and password == 'admin':
            #登录成功就重定向
            #return  HttpResponseRedirect('/event_manage/')
            #登录成功，把user存到cookie里
            response=HttpResponseRedirect('/event_manage/')
            #1.存cookie
            #response.set_cookie("user",username,3600)
            #2.存session
            request.session['user']=username
            return response
        else:
            return  render(request,'index.html',{'error':'username or password is error'})

#重定向到登录成功的h5
def event_manage(request):
    #什么参数都不带
    #return render(request,"event_manage.html")
    #把username带出去1.cookies带出
    #username=request.COOKIES.get("user","")
    # 把username带出去2.session带出
    username=request.session.get("user","")
    return render(request,"event_manage.html",{"user":username})