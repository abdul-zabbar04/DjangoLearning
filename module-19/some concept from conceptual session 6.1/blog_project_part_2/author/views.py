from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.

def register(request):
    if request.method=='POST':
        register_form= forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    else:
        register_form= forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'} )

def user_login(request):
    if request.method=="POST":
        login_form= AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name= login_form.cleaned_data['username']
            user_pass= login_form.cleaned_data['password']
            user= authenticate(username= user_name, password= user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('homePage')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('register')
    else:
        login_form= AuthenticationForm()
    return render(request, 'register.html', {'form': login_form, 'type': 'Login'})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')

@login_required
def profile(request):
    data= Post.objects.filter(author= request.user)
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.method=="POST":
        form= forms.ChangeUserData(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form= forms.ChangeUserData(instance= request.user)
    return render(request, 'update_profile.html', {'form': form, 'type': 'Update'})

@login_required
def pass_change(request):
    if request.method=='POST':
        form= PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            messages.warning(request, 'Password updated failed')
    else:
        form= PasswordChangeForm(user=request.user)
    return render(request, 'changepass.html', {'form': form})