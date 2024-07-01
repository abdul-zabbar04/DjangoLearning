from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    # return HttpResponse("Yes, i can do it")
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")