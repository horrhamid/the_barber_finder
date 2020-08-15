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
def create_time_table(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    barber = request.POST['barber_name']
    shop = request.POST['shop_name']
    date = request.POST['date']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    

