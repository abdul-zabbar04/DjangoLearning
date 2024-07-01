from django.shortcuts import render
from .form import contactForm, formValidation, passwordValidation
# Create your views here.
def about(request):
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        age= request.POST.get('age')
        check= request.POST.get('check')
        choice= request.POST.get('size')
        meals= request.POST.get('pizza')
        print(meals)
        return render(request, 'first_app/about.html', {'name': name, 'email': email, 'age':age, 'check': check, 'choice': choice, 'meals': meals})
    else:
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

def djangoForm(request):
    if request.method=="POST":
        form= contactForm(request.POST, request.FILES)
        if form.is_valid():
            file= form.cleaned_data['file']
            # print(file)
            with open('./first_app/upload/'+file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    # print(request.POST, request.FILES)
    return render(request, 'first_app/django_form.html', {'form': form})


    # name= request.POST.get('name')
    # email= request.POST.get('email')
    # meals= request.POST.get('pizza')
    # print(name, email, meals)
    # return render(request, 'first_app/django_form.html', {'form': form, 'name': name, 'email': email, 'meals': meals})

def form_validation(request):
    if request.method == "POST":
        form= formValidation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data) 
    else:
        form= formValidation()      
    return render(request, 'first_app/formValidation.html', {'form': form})

# password validation:
def password_validation(request):
    if request.method == "POST":
        form= passwordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data) 
    else:
        form= passwordValidation()      
    return render(request, 'first_app/passwordValidation.html', {'form': form})