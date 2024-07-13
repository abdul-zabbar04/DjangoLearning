from django.shortcuts import render
from .forms import MusicianForm
from django.views.generic import CreateView, UpdateView
from .models import MusicianModel
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class add_musician(CreateView):
    model = MusicianModel
    form_class= MusicianForm
    template_name= 'add_musician.html'
    success_url= reverse_lazy('addMusician')
    def form_valid(self, form):
        return super().form_valid(form)
    
class Edit_musician(UpdateView):
    model= MusicianModel
    form_class= MusicianForm
    pk_url_kwarg= 'id'
    template_name= 'add_musician.html'
    success_url= reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Musician Edited Successfully')
        return super().form_valid(form)
    
