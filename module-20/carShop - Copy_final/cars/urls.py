from django.urls import path
from .views import add_car, CarDetail, buy

urlpatterns = [
    # path('add/', add_car, name='addCarPage' ),
    path('details/<int:id>/', CarDetail, name='carDetailsPage' ),
    path('buy/<int:id>/', buy, name='buyPage' ),
]
