from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('delete/<int:roll>', views.delete_student, name='delete_student')
]
