from django import forms
from django.forms import widgets
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model= AlbumModel
        fields= '__all__'
        widgets = {
            'album_release_date': widgets.DateInput(attrs={'type': 'date'})
        }