from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('add/', views.add_musician.as_view(), name='addMusician'),
    path('edit/<int:id>', views.Edit_musician.as_view(), name='editMusician'),
]
