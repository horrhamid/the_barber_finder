from django.urls import path
from .views import register_view, logout_view, login_view, main_view, registration, login_view2

app_name = 'authentication'

urlpatterns = [
    path('register_view/', register_view, name='register_view'),
    path('login/', login_view, name='login'),
    path('login2/', login_view2, name='login2'),
    path('logout/', logout_view, name='logout'),
    path('', main_view, name='main'),
    path('registration/', registration, name='registration'),
]
