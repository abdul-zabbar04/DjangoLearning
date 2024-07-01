from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(request):
    student= models.Student.objects.all()
    print(student)
    return render(request, 'first_app/home.html', {'data': student})

def delete_student(request, roll):
    print("Request:", request, "roll:",roll)
    student= models.Student.objects.all()
    std = models.Student.objects.get(pk =roll).delete()
    return redirect("homePage")