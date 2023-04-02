from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import View,TemplateView,CreateView,FormView,DeleteView
from store.models import Products
from django.contrib import messages
from .models import *





# Create your views here.
class CustHomeview(TemplateView):
    template_name="custhome.html"
    success_url=reverse_lazy("ch")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.all()
        return context
    
class profileView(TemplateView):
    template_name="profile.html"
    pk_url_kwargs="pk"
    
class ProductView(TemplateView):
    template_name='product.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('pk')
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.get(id=id)
        return context
def Addreview(request,*args,**kwargs):
      if request.method=="POST":
        id=kwargs.get('pid')
        product=Products.objects.get(id=id)
        user=request.user
        cmnt=request.POST.get("comment")
        Review.objects.create(product=product,user=user,comment=cmnt)
        return redirect('ch')
    
def addcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    Cartt.objects.create(mobile=mobile,user=user)
    messages.success(request,"Add Cart Successfully")

    return redirect('ch')
    
    

class MyCart(TemplateView):
    template_name='cart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Cartt.objects.filter(user=self.request.user)
        return context
    
    
class Deletecart(DeleteView):
    model=Cartt
    template_name='deletecart.html'
    success_url=reverse_lazy('ch')
    
class CheckOut(TemplateView):
    template_name="checkout.html"
    
    


    
