from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    myDic= {
        'name': 'mac',
        'strList': ['python', 'JavaScript', 'Java'],
        'today': datetime.datetime.now(),
        'email': '',
        'fee': 6500,
        'about': 'hello I am Mac',
        'members': [
                    {'name': 'Josh', 'age': 19},
                    {'name': 'Dave', 'age': 22},
                    {'name': 'Mac', 'age': 31},
                ]
    }

    return render(request, 'firstapp/index.html', myDic)
