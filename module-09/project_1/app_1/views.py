from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is course page via app_1")
def about(request):
    return HttpResponse("This is about page via app_1")
def app_1(request):
    return HttpResponse("This is app_1 page")