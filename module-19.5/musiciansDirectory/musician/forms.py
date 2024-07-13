from .models import MusicianModel
from django.forms import ModelForm

class MusicianForm(ModelForm):
    class Meta:
        model= MusicianModel
        fields= '__all__'