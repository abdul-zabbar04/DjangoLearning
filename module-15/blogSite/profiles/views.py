from django.shortcuts import render

# Create your views here.
def add_profile(request):
    return render(request, 'add_profile.html')