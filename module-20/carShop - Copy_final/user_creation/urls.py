from django.urls import path
from .views import signup, user_login, user_logout, profile, edit_profile, edit_password
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('signup/', signup.as_view(), name='signupPage'),
    path('login/', user_login.as_view(), name='loginPage'),
    path('logout/', user_logout.as_view(), name='logoutPage'),
    path('profile/', profile, name='profilePage'),
    path('profile/edit/', edit_profile, name='editProfilePage'),
    path('profile/password/change/', edit_password, name='passChangePage'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)