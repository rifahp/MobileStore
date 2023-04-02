from django import forms
from .models import Bio
# from.models import Cart

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude={"user"}
    widgets={
         "phone":forms.NumberInput(attrs={"class":"form-control"}),
         "address":forms.CharField(max_length=200),
         "email":forms.EmailField(max_length=200)
    }
            
           
           
class Quantity(forms.Form):
    quantity=forms.IntegerField()
        