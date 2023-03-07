from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views.generic import View


# Create your views here.

class AddView(View):
    def get(self,req,*args,**kwargs):
        form=Opform()
        return render(req,'add.html',{'form':form})
    def post(self,req,*args,**kwargs):
        form_data=Opform(data=req.POST)
        n1=req.POST.get("num1")
        n2=req.POST.get("num2")
        res=int(n1)+int(n2)
        if form_data.is_valid():
            n1=form_data.cleaned_data.get('num1')
            n2=form_data.cleaned_data.get('num2')
            return render (req,"add.html",{"res":res})
        else:
            return render(req,'add.html',{'form':form_data})
class SubView(View):
    def get(self,req,*args,**kwargs):
        form=Opform()
        return render(req,'sub.html',{'form':form})
    def post(self,req,*args,**kwargs):
        form_data=Opform(data=req.POST)
        n1=req.POST.get("num1")
        n2=req.POST.get("num2")
        res=int(n1)-int(n2)
        if form_data.is_valid():
            n1=form_data.cleaned_data.get('num1')
            n2=form_data.cleaned_data.get('num2')
            return render (req,"sub.html",{"res":res})
        else:
            return render(req,'sub.html',{'form':form_data})
class MulView(View):
    def get(self,req,*args,**kwargs):
        form=Opform()
        return render(req,'mul.html',{'form':form})
    def post(self,req,*args,**kwargs):
        form_data=Opform(data=req.POST)
        n1=req.POST.get("num1")
        n2=req.POST.get("num2")
        res=int(n1)*int(n2)
        if form_data.is_valid():
            n1=form_data.cleaned_data.get('num1')
            n2=form_data.cleaned_data.get('num2')
            return render (req,"mul.html",{"res":res})
        else:
            return render(req,'mul.html',{'form':form_data})