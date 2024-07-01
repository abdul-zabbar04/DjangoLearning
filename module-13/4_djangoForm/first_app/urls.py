from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='aboutPage'),
    path('form/', views.form, name='formPage'),
    path('index/', views.index, name='indexPage'),
    path('django_form/', views.djangoForm, name='djangoForm'),
    path('form_validation/', views.form_validation, name="formValidationPage"),
    path('passwordValidation/', views.password_validation, name= 'passwordValidationPage'),
]
