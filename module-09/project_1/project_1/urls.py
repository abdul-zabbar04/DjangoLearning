from django.contrib import admin
from django.urls import path, include
# from views import contact
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path('', views.home),
    path('app_1/', include('app_1.urls'))
]
