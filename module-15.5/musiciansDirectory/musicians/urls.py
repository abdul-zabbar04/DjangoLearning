from django.urls import path
from .import views

urlpatterns = [
    path('add_musician/', views.add_musician, name='addMusician'),
    path('edit_musician/<int:id>/', views.edit_musician, name='editMusician'),
]
