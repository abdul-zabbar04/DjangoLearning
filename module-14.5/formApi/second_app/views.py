from django.shortcuts import render
from .forms import demoModelForm

# Create your views here.
def model_form(request):
    form= demoModelForm()
    return render(request, 'second_app/model_form.html', {'form': form})