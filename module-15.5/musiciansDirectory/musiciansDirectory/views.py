from django.shortcuts import render
from albums.models import Albums
def home(request):
    data= Albums.objects.all()
    return render(request, 'home.html', {'data': data})