from django.views.generic import ListView
from django.shortcuts import render
from album.models import AlbumModel


class home(ListView):
    model= AlbumModel
    context_object_name= 'data'
    template_name= 'home.html'