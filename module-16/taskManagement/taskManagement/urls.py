from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('tasks.urls')),
    path('category/', include('categories.urls')),
    path('', views.home, name='homePage'),
]
