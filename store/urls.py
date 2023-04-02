from django.urls import path
from .views import *

urlpatterns = [
    path('',StoreHome.as_view(),name='sh'),
    path('addpro/',AddProduct.as_view(),name='adp'),
     path('mypro/',MyProducts.as_view(),name='myp'),
     path('cpswd/',EditPassword.as_view(),name="cpswd"),
    #  path('adtc/',AddtoCart.as_view(),name="adtc"),
     
    
     
      path('updatepro/<int:pk>/',UpdateProduct.as_view(),name='updatepro'),
      path('deletepro/<int:pk>/',DeleteProduct.as_view(),name='deletepro'),
    

]
