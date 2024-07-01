from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def form(request):
    if request.method == 'POST':
        name= request.POST.get('username')
        email= request.POST.get('email')
        return render(request, 'first_app/form.html', {'name': name, 'email': email})
    return render(request, 'first_app/form.html')

def about(request):
    if request.method == 'POST':
        name= request.POST.get('username')
        email= request.POST.get('email')
        return render(request, 'first_app/about.html', {'name': name, 'email': email})
    return render(request, 'first_app/about.html')