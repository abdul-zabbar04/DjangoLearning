from django.shortcuts import render
from .forms import FormApi
# Create your views here.
def form_api(request):
    form= FormApi()
    return render(request, 'first_app/form_api.html', {'form':form})