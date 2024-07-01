from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='indexPage'),
    path('form/', views.form, name='formPage'),
    path('about/', views.about, name='aboutPage'),
]
