from django.urls import path
from . import views

urlpatterns = [
    path('add_post', views.add_post, name='postPage')
]
