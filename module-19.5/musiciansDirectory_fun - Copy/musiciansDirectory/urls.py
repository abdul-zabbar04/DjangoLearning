from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/', include('albums.urls')),
    path('musician/', include('musicians.urls')),
    path('', views.home, name= 'homePage'),
    path('musician/', include('login_logout.urls')),
]
