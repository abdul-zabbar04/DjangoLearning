from django.urls import path
from .views import signup, home, user_login, profile, user_logout, pass_change, pass_change2, change_user_data
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', home, name='homePage'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('password_change/', pass_change, name='passchange'),
    path('password_change2/', pass_change2, name='passchange2'),
    path('user/', change_user_data, name='useredit')
]
