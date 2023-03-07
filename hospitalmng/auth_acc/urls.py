from django.urls import path
from .views import *

urlpatterns=[
    path('login',LoginV.as_view(),name='logi'),
    path('regis',Registration.as_view(),name='regis'),
    path('logout',LogOut.as_view(),name='lgout'),
]