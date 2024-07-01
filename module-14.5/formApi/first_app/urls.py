from django.urls import path
from . import views
urlpatterns = [
    path('form_api/', views.form_api, name='formApiPage')
]
