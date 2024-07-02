from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('',home, name='homePage'),
    path('second_app/', include('second_app.urls')),
]
