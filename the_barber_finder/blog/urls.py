from django.urls import path, include
from .views import users_view, set_available_times, reserve_view, choose_subtime, set_av_time, reserve_time

app_name = 'blog'

urlpatterns = [
    path('', users_view, name='Users'),
    path('auth/', include('authentincation.urls')),
    path('set_av_times/', set_available_times, name="set_av_time"),
    path('set_times/', set_av_time, name="set_time"),
    path('reserve_view/', reserve_view, name='reserve_barber'),
    path('subtime/', choose_subtime, name='subtime'),
    path('reservation/', reserve_time, name='reserve_time'),
]
