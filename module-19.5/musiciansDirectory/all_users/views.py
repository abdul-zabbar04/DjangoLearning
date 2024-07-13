from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect


class Signup(CreateView):
    form_class= UserForm
    template_name= 'signup.html'
    success_url= reverse_lazy('signup')

    def form_valid(self, form):
        messages.success(self.request, 'Created Account Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Created Account Failed')
        response = super().form_invalid(form)
        return response
    
class Login(LoginView):
    template_name= 'login.html'
    success_url= reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in Failed')
        response = super().form_invalid(form)
        return response

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')