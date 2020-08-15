# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BarberShop, Barber, Person, Customer
# Create your views here.


def users_view(request):
    name = None
    role = None
    name = request.user.username
    print("user name is :")
    print(name)
    if name:
        
        person = Person.objects.filter(user=request.user)
        is_barber = Barber.objects.filter(user=person[0]).count()
        if is_barber != 0:
            role = "Barber"
        else:
            role = "Customer"
    print("role :")
    print(role)
    barbershops = BarberShop.objects.all()

    return render(request, 'dashboard.html', context={'name': name,
                                                      'shops': barbershops,
                                                      'role': role})


def create_time_table(request):
    username = None
    barber_shop_id = None
    if request.user.is_authenticated():
        username = request.user.username
        barber_shop_id = request.session.get('shop_id', None)
    barber_name = request.POST.get('barbername')
    
    date = request.POST.get('date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    queryUser = User.objects.filter(user_name=username)
    print (queryUser)


def set_available_times(request):
    #
    return render(request, 'time-managing.html')
    
    

