from django.urls import path
from Customer.views import *

urlpatterns = [
    path('',CustHomeview.as_view(),name="ch"),
    path('profile/',profileView.as_view(),name="prof"),
    path('check/',CheckOut.as_view(),name="cout"),
    
    path('mycart/',MyCart.as_view(),name='mycart'),
    path('pro/<int:pk>',ProductView.as_view(),name='pro'),
    path('deletcart/<int:pk>/',Deletecart.as_view(),name='delc'),
    path('addcart/<int:pid>',addcart,name='addcart'),
    path('review/<int:pid>',Addreview,name='addr'),
    
    
]