from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views.generic import View

# Create your views here.

class AddView(View):
    def get(self,req,*args,**kwargs):
        form=Opform()
        return render(req,'add.html',{'form':form})