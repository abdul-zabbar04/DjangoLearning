from typing import Any
from django.shortcuts import render
from cars.models import CarModel
from django.views.generic import ListView
from brands.models import BrandModel

def Home(request, brand_slug= None):
    data= CarModel.objects.all()
    brands= BrandModel.objects.all()
    if brand_slug is not None:
        brand= BrandModel.objects.get(slug= brand_slug) 
        data= CarModel.objects.filter(brand_name= brand)
    total= len(data)
    return render(request, 'home.html', {'data': data, 'brands': brands, 'total': total})

# class Home(ListView):
#     model= CarModel
#     template_name= 'home.html'

