from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response= render(request, 'home.html')
    response.set_cookie('name', 'Mac')
    # response.set_cookie('name', 'Jac', max_age=10)
    response.set_cookie('name', 'Jac', expires=datetime.utcnow()+timedelta(days=7))
    return response

def set_session(request):
    data= {
        'name': 'Mac',
        'age': 23,
        'language': 'Bengali'
    }
    # delete date set
    print('this is expired date: ', request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html')


def get_cookie(request):
    name= request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})

def get_session(request):
    if 'name' in request.session:
        s_name= request.session.get('name', 'Guest')
        age= request.session.get('age')
        lan= request.session.get('language')
        request.session.modified= True
        return render(request, 'get_cookie.html', {'s_name': s_name, 'age': age, 'lan': lan})
    else:
        return HttpResponse('Your session has been expired. Login again')
def del_cookie(request):
    response= render(request, 'del.html')
    response.delete_cookie('name')
    return response

def del_session(request):
    # del request.session['name'] # for single property delete of dict.
    request.session.flush()
    return render(request, 'del.html')