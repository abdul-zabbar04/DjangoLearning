from django.urls import path
from . import views
# from first_app.views import home # alternative way

urlpatterns = [
    path('', views.home, name='homePage'),
]
