from django.urls import path, include
from .views import users_view

app_name = 'blog'

urlpatterns = [
    path('', users_view, name='Users'),
    path('auth/', include('authentincation.urls'))
]
