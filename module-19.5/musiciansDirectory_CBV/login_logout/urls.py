from django.urls import path
from .views import Signup, Login, log_out, profile, change_pass, change_pass2

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/change/password/', change_pass, name='pass_change'),
    path('profile/change/password/2', change_pass2, name='pass_change2'),
]
