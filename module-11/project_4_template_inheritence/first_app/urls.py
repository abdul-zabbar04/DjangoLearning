from django.urls import path
from . import views

urlpatterns=[
    path('index/', views.index, name='indexPage'),
    path('about/page/<int:id>/', views.about, name='aboutPage'),
    path('contact/', views.contact, name='contactPage'),
]