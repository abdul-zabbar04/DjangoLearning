from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def about(request):
    d= {
        'name': "Abdul Zabbar",
        'age' : 23,
        'today': datetime.datetime.now(), 
        'dept': ['EEE', 'CSE', 'ME', 'CE'],

        'courses': [
            {
                'id': 1,
                'course': 'python',
                'fee': 5000
            },
            {
                'id': 2,
                'course': 'django',
                'fee': 10000
            },
            {
                'id': 3,
                'course': 'c',
                'fee': 1000
            }
        ]
    }

    
    return render(request, 'about.html', d)

def contact(request):
    return render(request, 'contact.html')
