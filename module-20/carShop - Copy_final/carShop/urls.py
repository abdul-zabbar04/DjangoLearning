from django.contrib import admin
from django.urls import path, include
from .views import Home
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='homePage'),
    path('brand/<slug:brand_slug>/', Home, name='brandWise'),
    path('user/', include('user_creation.urls')),
    path('cars/', include('cars.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
