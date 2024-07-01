from django.urls import path
from . import views

urlpattern=[
    path('courses/', views.courses)
]