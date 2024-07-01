from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'first_app/about.html')
def form(request):
   if request.method == 'POST':
        name= request.POST.get('username')
        email= request.POST.get('email')
        rating=request.POST.get('rating')
        # print(name, email, rating)
        # print(request.POST)
        return render(request, 'first_app/form.html', {'name': name, 'email': email, 'rating': rating})
   else:
       return render(request, 'first_app/form.html')
def index(request):
    return render(request, 'first_app/index.html')