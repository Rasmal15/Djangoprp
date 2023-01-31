from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse

from .forms import*
# Create your views here.
class MainHome(View):
    def get(self,req,*args,**kwargs):
        return render(req,'Main_home.html')
class RegView(View):
    def get(self,req,*args,**kwargs):
        form=RegForm()
        return render(req,'reg.html',{'form':form})
    def post(self,req,*args,**kwargs):
        form_data=RegForm(data=req.POST)
        if form_data.is_valid():
            first_name=form_data.cleaned_data.get('first_name')
            lasr_name=form_data.cleaned_data.get('last_name')
            username=form_data.cleaned_data.get('username')
            email=form_data.cleaned_data.get('email')
            experience=form_data.cleaned_data.get('experience')
            password=form_data.cleaned_data.get('password')
            return redirect('h')
        else:
            return render(req,'reg.html',{'form':form_data})
class LogView(View):
    def get(self,req,*args,**kwargs):
        data=Logform()
        return render(req,'reg.html',{'form':data})
    def post(self,req,*args,**kwargs):
        data=Logform()
        username=req.POST.get('username')
        password=req.POST.get('password')
        return HttpResponse("username:"+username+"<br>password:"+password)