from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.

class Signup(CreateView):
    form_class= UserForm
    template_name= 'login_logout/authenticate.html'
    success_url= reverse_lazy('signup')

    def form_valid(self, form):
        messages.success(self.request, 'Created Account Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Created Account Failed')
        response = super().form_invalid(form)
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Submit'
        context["page"] = 'Signup'
        return context
    
class Login(LoginView):
    template_name= 'login_logout/authenticate.html'
    # success_url= reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('homePage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in Failed')
        response = super().form_invalid(form)
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        context["page"] = 'Login'
        return context

@login_required
def log_out(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'login_logout/profile.html')

@login_required
def change_pass(request):
    if request.method=='POST':
        form= PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('profile')
        else:
            messages.warning(request, 'Password Changed Failed')
    else:
        form= PasswordChangeForm(request.user)
    return render(request, 'login_logout/changepass.html', {'form': form})

@login_required
def change_pass2(request):
    if request.method=='POST':
        form= SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('profile')
        else:
            messages.warning(request, 'Password Changed Failed')
    else:
        form= SetPasswordForm(request.user)
    return render(request, 'login_logout/changepass.html', {'form': form})