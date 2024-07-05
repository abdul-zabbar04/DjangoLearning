from django.shortcuts import render, redirect
from .forms import Resister
from django.contrib import messages

#login form ar jonno package import
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm #for authentication form
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash # check authenticate, login and logout respectively

# user_data_edit korar jonno import:
from .forms import ChangeUserData
# Create your views here.
def home(request):
    return render(request, 'firstapp/home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            form= Resister(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfully!')
                # messages.info(request, 'Welcome')
                form.save()
                # print(form.cleaned_data)
                return redirect('login')

        else:
            form= Resister()
            return render(request, 'firstapp/signup.html', {'form': form})
    else:
        return redirect('profile')

def user_login(request):
    # akhane form direct korbo. forms.py teu kora jeto
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request=request, data= request.POST)
            if form.is_valid():
                username= form.cleaned_data['username']
                userpass= form.cleaned_data['password']
                # print(username, userpass)
                user= authenticate(username= username, password= userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')

        else:
            form= AuthenticationForm()
        return render(request, 'firstapp/login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form= ChangeUserData(request.POST, instance= request.user)
            if form.is_valid():
                messages.success(request,"Account updated successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form= ChangeUserData(instance= request.user)
        return render(request, 'firstapp/profile.html', {'form': form})
    else:
        return redirect('profile')
    
def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.method== "POST":
        form= PasswordChangeForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form= PasswordChangeForm(user=request.user)

    return render(request, 'firstapp/passchange.html', {'form': form})

def pass_change2(request):
    if request.method=="POST":
        form= SetPasswordForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form= SetPasswordForm(user=request.user)
    return render(request, 'firstapp/passchange.html', {'form': form})
            
def change_user_data(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form= ChangeUserData(request.POST, instance= request.user)
            if form.is_valid():
                messages.success(request,"Account updated successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form= ChangeUserData()
        return render(request, 'firstapp/profile.html', {'form': form})
    else:
        return redirect('profile')