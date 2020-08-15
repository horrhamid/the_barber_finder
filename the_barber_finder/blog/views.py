# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import BarberShop, Barber, Person, Customer, TimeTable
# Create your views here.


def users_view(request):
    name = None
    role = None
    name = request.user.username
    print("user name is :")
    print(name)
    if name:
        if check_barber(request.user):
            role = "Barber"
        else:
            role = "Customer"
    print("role :")

    print(role)
    barbershops = BarberShop.objects.all()
    return render(request, 'dashboard.html', context={'name': name,
                                                      'shops': barbershops,
                                                      'role': role})

def check_barber(user):
    person = Person.objects.filter(user=user)
    is_barber = Barber.objects.filter(user=person[0]).count()
    if is_barber != 0:
        return True
    else:
        return False

def set_av_time(request):
    return render(request, "time-managing_2.html")

def set_available_times(request):
    #
    username = None
    barber_shop_id = None
    if request.user.is_authenticated and check_barber(request.user):
        username = request.user
    else:
        return HttpResponse('barber Login needed!')
    if request.POST.get('date') and request.POST.get('time1') and request.POST.get('time2'):
        date = request.POST.get('date')
        start_time = request.POST.get('time1')
        end_time = request.POST.get('time2')
        person = Person.objects.filter(user=username)
        barber = Barber.objects.filter(user=person[0])
        start_time+=":00"
        end_time+=":00"
        print(date)
        print(start_time)
        print(end_time)
        print(person)
        print(barber)
        
        store = BarberShop.objects.filter(owner=barber[0])
        timeTable = TimeTable(barber=barber[0], store=store[0], start_time=start_time, end_time=end_time, date=date)
        timeTable.save()
    return HttpResponse("DONE !")


def reserve_view(request):
    shop = request.POST.get('custId')
    print(shop)
    barber = Barber.objects.filter()
    return render(request, "reservation-choose-tim.html", context={'Barber': barber})


def choose_subtime(request):
    return HttpResponse("IN RESERVE VIEW !!")
