from django.urls import path, include
from .views import users_view, set_available_times

app_name = 'blog'

urlpatterns = [
    path('', users_view, name='Users'),
    path('auth/', include('authentincation.urls')),
    path('set_times/', set_available_times, name="set_av_time"),
]
