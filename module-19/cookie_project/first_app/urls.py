from django.urls import path
from .views import home, get_cookie, del_cookie, set_session, get_session, del_session

urlpatterns = [
    # path('', home, name='home'), # cookie set urls call
    path('', set_session, name='home'), # session set url call
    path('get_cookie/', get_cookie),
    path('get_session/', get_session),
    path('del/', del_cookie),
    path('del_session/', del_session),
]
