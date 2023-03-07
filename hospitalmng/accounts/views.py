from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import*
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect('mh')
    return wrapper
# Create your views here.



@method_decorator(signin_required,name='dispatch')
class MainHome(View):
    def get(self,req,*args,**kwargs):
        user=req.user
        return render(req,'Main_home.html',{'name':user})
# class RegView(View):
#     def get(self,req,*args,**kwargs):
#         form=RegForm()
#         return render(req,'reg.html',{'form':form})
#     def post(self,req,*args,**kwargs):
#         form_data=RegForm(data=req.POST)
#         if form_data.is_valid():
#             first_name=form_data.cleaned_data.get('first_name')
#             lasr_name=form_data.cleaned_data.get('last_name')
#             username=form_data.cleaned_data.get('username')
#             email=form_data.cleaned_data.get('email')
#             experience=form_data.cleaned_data.get('experience')
#             password=form_data.cleaned_data.get('password')
#             messages.success(req,'registration successful')
#             return redirect('h')
            
        # else:
        #     messages.success(req,'registration failed')
        #     return render(req,'reg.html',{'form':form_data})
# class LogView(View):
#     def get(self,req,*args,**kwargs):
#         data=Logform()
#         return render(req,'reg.html',{'form':data})
#     def post(self,req,*args,**kwargs):
#         username=req.POST.get('username')
#         password=req.POST.get('password')
#         return HttpResponse("username:"+username+"<br>password:"+password)
@method_decorator(signin_required,name='dispatch')
class LogView(View):
    def get(self,req,*args,**kwargs):
        data=Logform()
        return render(req,'log.html',{'form':data})
    def post(self,req,*args,**kwargs):
        username=req.POST.get('username')
        password=req.POST.get('password')
        return HttpResponse("username:"+username+"<br>password:"+password)

@method_decorator(signin_required,name='dispatch')
class StaffView(View):
    def get(self,req,*args,**kwargs):
        # if req.user.is_authenticated:
        res=Staff.objects.all()
        return render(req,'staff.html',{"data":res})
        # else:
        #     return redirect('mh')
@method_decorator(signin_required,name='dispatch')
class RegView(View):
    def get(self,req,*args,**kwargs):
        f=RegModelForm()
        return render(req,'reg.html',{'form':f})
    def post(self,req,*args,**kwargs):
        form_data=RegModelForm(data=req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,'registration successful')
            return redirect('h')
            
        else:
            messages.success(req,'registration failed')
            return render(req,'reg.html',{'form':form_data})
@method_decorator(signin_required,name='dispatch')
class StaffDeleteView(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("sid")
        staff=Staff.objects.get(id=id)
        staff.delete()
        messages.success(req,"staff removed")
        return redirect('vstaff')
@method_decorator(signin_required,name='dispatch')
class StaffEdit(View):
    def get(self,req,*args,**kwargs):
        id= kwargs.get("sid")
        staff=Staff.objects.get(id=id)
        f=RegModelForm(instance=staff)
        return render(req,'edit_staff.html',{'form':f})
    def post(self,req,*args,**kwargs):
        id=kwargs.get("sid")
        staff=Staff.objects.get(id=id)
        form_data=RegModelForm(data=req.POST,instance=staff,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('vstaff')
        else:
            return render(req,'edit_staff.html',{'form':form_data})
