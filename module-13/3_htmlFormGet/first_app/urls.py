from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='aboutPage'),
    path('form/', views.form, name='formPage'),
    path('index/', views.index, name='indexPage'),
]
