# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BarberShop
# Create your views here.


def users_view(request):
    name = request.user.username
    barbershops = BarberShop.objects.all()
    for x in barbershops:
        print(x.name)
    return render(request, 'dashboard.html', context={'name': name,
                                                      'shops': barbershops })
