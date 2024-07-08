from django.urls import path
from .views import sign_up, log_in, home, log_out, profile, change_pass, change_pass2

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/change/password/', change_pass, name='pass_change'),
    path('profile/change/password/2', change_pass2, name='pass_change2'),
    path('', home, name='home'),
]
