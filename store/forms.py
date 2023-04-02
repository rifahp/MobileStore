from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        exclude=[
            'user'
        ]
        
class PchangeForm(forms.Form):
    old_password=forms.CharField(max_length=100,label="old password",widget=forms.PasswordInput)
    new_password=forms.CharField(max_length=100,label="new password",widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=100,label="confirm password",widget=forms.PasswordInput)
        
