from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout



from .models import CustomerUser

# Create your views here.
class Home(TemplateView):
    template_name="Home.html"
    
class Regview(CreateView):
    form_class=RegForm
    template_name="registration.html"
    model=CustomerUser
    success_url=reverse_lazy('mh')

class loginview(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,req,*args,**kwargs):
        r=LogForm(data=req.POST)
        if r.is_valid():
            un=r.cleaned_data.get("username")
            pw=r.cleaned_data.get("password")
            user=authenticate(req,username=un,password=pw)
            if user:
                login(req,user)
                if req.user.usertype=="store":
                    return redirect('sh')
                else:
                    return redirect("ch")
            else:
                return render(req,'login.html',{"form":r})
        else:
            return render(req,'login.html',{"form":r})
        
class logout(View):
    def get(self,request):
        logout(request)
        return redirect("log")

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           