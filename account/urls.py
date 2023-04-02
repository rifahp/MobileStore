from django.contrib import admin
from django.urls import path
from account.views import *
urlpatterns = [
    path('reg/',Regview.as_view(),name="reg"),
    path('login/',loginview.as_view(),name="log"),
    path('logout/',logout.as_view(),name='lgout'),
    
    
    
    
]