from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'navigationApp/about.html')

def contact(request):
    return render(request, 'navigationApp/contact.html')