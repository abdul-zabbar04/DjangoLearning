from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import BroughtCars
class UserForm(UserCreationForm):
    first_name= forms.CharField(max_length=50, required=True)
    last_name= forms.CharField(max_length=50, required=True)
    email= forms.EmailField(required=True)
    class Meta:
        model= User
        fields=['username', 'first_name', 'last_name', 'email']

class ProfileEditForm(UserChangeForm):
    password= None
    class Meta:
        model= User
        fields=['username', 'first_name', 'last_name', 'email']
    
class BroughtCarForm(forms.ModelForm):
    class Meta:
        model= BroughtCars
        fields= '__all__'