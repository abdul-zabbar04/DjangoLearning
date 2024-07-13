from django.urls import path
from .views import Signup, Login, user_logout

urlpatterns = [
    path('signup/', Signup.as_view(), name= 'signup'),
    path('login/', Login.as_view(), name= 'login'),
    path('logout/', user_logout, name= 'logout'),
]
