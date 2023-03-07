from django.urls import path
from .views import *

urlpatterns=[
    path('add/',AddView.as_view(),name='add'),
    path('sub/',SubView.as_view(),name='sub'),
    path('mul/',MulView.as_view(),name='mul'),
]