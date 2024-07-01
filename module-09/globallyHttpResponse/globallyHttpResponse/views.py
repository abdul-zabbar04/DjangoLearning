from django.http import HttpResponse
def myName(request):
    return HttpResponse('My name is Abdul Zabbar')

def home(request):
    return HttpResponse('I am in home')