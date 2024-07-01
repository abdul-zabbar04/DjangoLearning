from django import forms
from .models import ModelForm

class Form(forms.ModelForm): 
    class Meta:
        model = ModelForm
        fields = ("__all__")
