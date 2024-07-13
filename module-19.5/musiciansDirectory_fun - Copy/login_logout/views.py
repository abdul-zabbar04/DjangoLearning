from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('homePage')
    else:
        form= UserForm()
    return render(request, 'login_logout/authenticate.html', {'form': form, 'type': 'Submit', 'type2': 'Signup'})
    
def log_in(request):
    if request.method=='POST':
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name= form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            user= authenticate(username= user_name, password= user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('homePage')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('signup')
    else:
        form= AuthenticationForm()
    return render(request, 'login_logout/authenticate.html', {'form': form, 'type':'Login', 'type2': 'Login'})

@login_required           
def home(request):
    return render(request, 'login_logout/home.html')

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