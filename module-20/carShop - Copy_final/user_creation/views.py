from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView
from cars.models import CarModel
from user_creation.models import BroughtCars
from django.contrib.auth.decorators import login_required

# Create your views here.

# using class based view: 1
class signup(CreateView):
    form_class= UserForm
    template_name= 'user_creation.html'
    success_url= reverse_lazy('loginPage')
    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')    
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context['type']='Signup'
        return context

# using class based view: 2
class user_login(LoginView):
    form_class= AuthenticationForm
    template_name= 'user_creation.html'
    # success_url= reverse_lazy('homePage')
    def get_success_url(self):
        return reverse_lazy('homePage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Login Information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context['type']= 'Login'
        return context
    
# using class based view: 3
class user_logout(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logged out Successfully')
        return redirect('loginPage')
    
@login_required
def profile(request):
    user_cars= BroughtCars.objects.filter(owner= request.user)
    all_cars= []
    all_id=[]
    all_existed_car= CarModel.objects.all()
    for sin_car in all_existed_car:
        a= sin_car.id
        all_id.append(a)
    # print(all_id)
    for car in user_cars:
        if car.sold_car in all_id:
            x= CarModel.objects.get(id=car.sold_car)
            all_cars.append(x)
    return render(request, 'profile.html', {'data': all_cars})

@login_required
def edit_profile(request):
    if request.method=="POST":
        form= ProfileEditForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profilePage')
        else:
            messages.error(request, 'Failed to update')
    else:
        form= ProfileEditForm(instance= request.user)
    return render(request, 'user_creation.html', {'form': form, 'type': 'Update Profile'})

# class edit_profile(UpdateView):
#     form_class= ProfileEditForm
#     template_name= 'user_creation.html'
    

#     def form_valid(self, form):
#         messages.success(self.request, 'Profile Updated Successfully')
#         return super().form_valid(form)
#     def form_invalid(self, form):
#         messages.error(self.request, 'Failed to update')
#         return super().form_invalid(form)
#     def get_context_data(self, **kwargs):
#         context=  super().get_context_data(**kwargs)
#         context['type']= 'Update Profile'
#         return context

@login_required
def edit_password(request):
    if request.method== "POST":
        form= PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('profilePage')
        else:
            messages.warning(request, 'Password updated failed')
    else:
        form= PasswordChangeForm(request.user)
    return render(request, 'user_creation.html', {'form': form, 'type': 'Update Password'})
