from cars.models import CarModel, CommentModel
from django.forms import ModelForm

class CarForm(ModelForm):
    class Meta:
        model= CarModel
        fields='__all__'
    
class CommentForm(ModelForm):
    class Meta:
        model= CommentModel
        fields=['name', 'body']