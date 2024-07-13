from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.user_login.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', LogoutView.as_view(next_page='login', http_method_names = ['get', 'post', 'options']), name='logout'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/change/password', views.pass_change, name='changepass'),
]
