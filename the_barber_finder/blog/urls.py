from django.urls import path, include
from .views import users_view, set_available_times, reserve_view

app_name = 'blog'

urlpatterns = [
    path('', users_view, name='Users'),
    path('auth/', include('authentincation.urls')),
    path('set_times/', set_available_times, name="set_av_time"),
    path('reserve_view/', reserve_view, name='reservation'),
]
