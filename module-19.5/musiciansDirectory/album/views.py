from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .models import AlbumModel
from .forms import AlbumForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class add_album(CreateView):
    model= AlbumModel
    form_class= AlbumForm
    template_name= 'add_album.html'
    success_url= reverse_lazy('addAlbum')
    def form_valid(self, form):
        messages.success(self.request, 'Album added successfully')
        return super().form_valid(form)