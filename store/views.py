from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,FormView
from .models import Products
from django.contrib import messages
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,logout




# Create your views here.
class StoreHome(TemplateView):
    template_name='storehome.html'
    form_class=ProductForm
    model=Products
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"Post uploaded")
        self.object=form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.all()
        return context
    
class AddProduct(CreateView):
    form_class=ProductForm
    model=Products
    template_name='add product.html'
    success_url=reverse_lazy('sh')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        return super().form_valid(form)
    
class MyProducts(TemplateView):
    template_name="my products.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.filter(user=self.request.user)
        return context
    
class UpdateProduct(UpdateView):
    form_class=ProductForm
    model=Products
    template_name='add product.html'
    success_url=reverse_lazy('sh')
    
class DeleteProduct(DeleteView):
    model=Products
    template_name='deleteproduct.html'
    success_url=reverse_lazy('myp')
    
class EditPassword(FormView):
    template_name="change passwod.html"
    form_class=PchangeForm
    def post(self,request,*args,**kwargs):
        form_data=PchangeForm(data=request.POST)  
        if form_data.is_valid():
           current=form_data.cleaned_data.get("old_password")
           new=form_data.cleaned_data.get("new_password")
           confirm=form_data.cleaned_data.get("confirm_password")
           print(current)
           user=authenticate(request,username=request.user.username,password=current)
           if user:  
              if new==confirm:
               user.set_password(new)
               user.save()
               messages.success(request,"password changed")
               logout(request)
               return redirect("log")
              else:
                messages.error(request,"password mismatches!!!")
                return redirect("cpswd")
           else:
                messages.success(request,"Incorrect Password")
                return redirect("cpswd")
        else:
                return render(request,"change password.html",{"form":form_data})
    
    

            

