from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
class Home(View):
    def get(self,req):
        return render(req,'home.html')

class LoginV(View):
    def get(self,req):
        f=LoginForm()
        user=req.user
        return render(req,'login.html',{'form':f,'user':user})
    def post(self,req,*args,**kwargs):
        form_data=LoginForm(data=req.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            user=authenticate(req,username=un,password=pw)
            if user:
                login(req,user)
                messages.success(req,"login completed")
                return redirect('h')
            else:
                messages.error(req,'login failed')
                return redirect('logi')
        else:
            return render(req,'login.html',{'form':form_data})
class Registration(View):
    def get(self,req):
        f=RegistrationForm()
        return render(req,'regis.html',{'form':f})
    def post(self,req,*args,**kwargs):
        form_data=RegistrationForm(data=req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('mh')
        else:
            return render(req,'regis.html',{'form':form_data})

class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect('logi')