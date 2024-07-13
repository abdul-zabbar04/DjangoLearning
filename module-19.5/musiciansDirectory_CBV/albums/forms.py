from django import forms
from django.forms import widgets
from .models import Albums

class AlbumForm(forms.ModelForm):
    class Meta:
        model= Albums
        fields= '__all__'
        widgets = {
            'album_release_date': widgets.DateInput(attrs={'type': 'date'})
        }