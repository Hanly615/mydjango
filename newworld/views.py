#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
       #return HttpResponse(u"Hello World! 大家好！")//此种方法网页信息需要写在括号里，比较麻烦
       return render(request,"index.html",)#此种方法调用index.html显示网页信息，比较简洁
