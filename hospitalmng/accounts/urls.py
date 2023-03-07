from django.urls import path
from .views import *

urlpatterns=[
    path('log/',LogView.as_view(),name='log'),
    path('reg/',RegView.as_view(),name='reg'),
    path('staff/',StaffView.as_view(),name='vstaff'),
    path('delstaff/<int:sid>',StaffDeleteView.as_view(),name='delstaff'),
    path('editstaff/<int:sid>',StaffEdit.as_view(),name='editstaff'),
    path('home/',MainHome.as_view(),name='h'),
]