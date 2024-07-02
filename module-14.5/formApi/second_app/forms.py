from django import forms
from .models import demoModel

class demoModelForm(forms.ModelForm):
    class Meta:
        model= demoModel
        fields= '__all__'