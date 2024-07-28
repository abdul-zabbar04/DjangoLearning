from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import CarModel, CommentModel
from cars.forms import CarForm, CommentForm
from django.contrib import messages
from user_creation.forms import BroughtCarForm
# Create your views here.

# class HomeView(ListView):
#     data= CarModel.objects.all()
#     template_name= 'home.html'

# def Home(request):
#     data= CarModel.objects.all()
#     return render(request, 'home.html', {'data': data})

def add_car(request):
    if request.method=="POST":
        form= CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car Added')
            return redirect('homePage')
    else:
        form= CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

# class CarDetail(DetailView):
#     model= CarModel
#     pk_url_kwarg= 'id'
#     template_name= 'car_detail.html'
#     def post(self, request, *args, **kwargs):
#         comment_form= CommentForm(data= self.request.POST)
#         car= self.get_object()
#         if comment_form.is_valid():
#             new_comment= comment_form.save(commit=False)
#             new_comment.car= car
#             new_comment.save()
#         return self.get(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context=  super().get_context_data(**kwargs)
#         car= self.object
#         comments= car.comments.all()     
#         comment_form= CommentForm()
#         context['comments']= comments
#         context['comment_form']= comment_form
#         return context


def CarDetail(request, id):
    car= CarModel.objects.get(id= id)
    comments= CommentModel.objects.filter(car= car)
    if request.method== 'POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            new_comment= form.save(commit=False)
            new_comment.car=car
            new_comment.save()
            messages.success(request, 'Comment added')
            form= CommentForm()
            return render(request, 'cars/car_detail.html', {'car': car, 'form': form, 'comments': comments})
            
    else:
        form= CommentForm()
    return render(request, 'cars/car_detail.html', {'car': car, 'form': form, 'comments': comments})

def buy(request, id):
    form= BroughtCarForm()
    car= CarModel.objects.get(id= id)
    form.instance.owner= request.user
    form.instance.sold_car= id
    form.instance.save()
    car.quantity-=1
    car.save()
    return redirect('profilePage')

