from django.urls import path
from .views import *

urlpatterns=[
    path('add/',AddView.as_view(),name='add')
]