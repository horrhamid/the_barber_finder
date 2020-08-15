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
    if name:
        
        person = Person.objects.filter(user=request.user)
<<<<<<< HEAD
        is_barber = Barber.objects.filter(user=person)
        if is_barber != '':
=======
        # print(person[0])
        r = Barber.objects.filter(user=person)


        # st = print(len(r))
        st = 1
        role = ''
        if st:
>>>>>>> 9c48dadb3c1a5c8d13a8856d0e1bf694d38c6193
            role = "Barber"
        else:
            role = "Customer"
    print("user name is :")
    print(name)
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
    
    

