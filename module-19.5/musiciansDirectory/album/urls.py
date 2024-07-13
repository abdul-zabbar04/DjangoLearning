from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_album.as_view(), name='addAlbum')
]
