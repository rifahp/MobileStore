from django.db import models
from account.models import CustomerUser
from store.models import Products


# Create your models here.

class Bio(models.Model):
    phone=models.IntegerField(),
    address=models.CharField(max_length=200),
    email=models.EmailField(max_length=200),
    profile_pic=models.ImageField(upload_to="user_profile_pictures",null=True),
    user=models.OneToOneField(CustomerUser,on_delete=models.CASCADE,related_name="b_user")
    
class Cartt(models.Model):
    mobile=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='m_cart',null=True)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name='u_cart')
    
class Review(models.Model):
    comment=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name='commented_user')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='commented_product')
    


    

    
    
    
    
    