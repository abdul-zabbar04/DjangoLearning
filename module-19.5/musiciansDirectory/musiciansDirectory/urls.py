from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('user/', include('all_users.urls')),
    # path('', home.as_view(), name='home')
    path('', home.as_view(), name='home')
]
