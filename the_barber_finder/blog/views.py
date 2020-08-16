# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
import datetime
import time
from .models import BarberShop, Barber, Person, Customer, TimeTable, Reserve
# Create your views here.


def users_view(request):
    name = None
    role = None
    name = request.user.username
    reserved = None
    times = None
    show_times = []
    print("user name is :")
    print(name)
    if name == "admin":
        return HttpResponse("LOGOUT needed!")
    if name:
        if check_barber(request.user):
            role = "Barber"
            person = Person.objects.filter(user=request.user)
            barber = Barber.objects.filter(user=person[0])
            reserved = Reserve.objects.filter(barber=barber[0])
            times = Reserve.objects.values_list('sub_time').filter(customer=customer[0])
        else:
            role = "Customer"
            person = Person.objects.filter(user=request.user)
            customer = Customer.objects.filter(user=person[0])
            reserved = Reserve.objects.filter(customer=customer[0])
            times = Reserve.objects.values_list('sub_time').filter(customer=customer[0])
    print("role :")

    print(role)
    # if role == "Barber":
    #     reserved = Reserve.objects.filter(barber=)

    for x in times:
        show_times.append(time.strftime('%H:%M:%S', time.gmtime(int(x))))
    barbershops = BarberShop.objects.all()
    return render(request, 'dashboard.html', context={'name': name,
                                                      'shops': barbershops,
                                                      'role': role,
                                                      'reserved': reserved,
                                                      'show_times': show_times})


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
    names = []
    shop = request.POST.get('shop_id')
    #print(shop)
    barberlist_ids = BarberShop.objects.values_list('barbers').filter(id=shop)
    for x in barberlist_ids:
        print (x[0])
        barber = Barber.objects.filter(id=x[0])
        print(barber[0])
        #person = Person.objects.filter(user=barber[0])
        names.append(barber[0])
    print(names)
    return render(request, "reservation-choose-tim.html", context={'Barber': names})


def choose_subtime(request):
    print("we are in choose_subtime")
    shave_date = request.POST.get("date")
    barber_name = request.POST.get("barber_name")
    print("barber name:")
    print(barber_name)
    print("shave_date:")
    print(shave_date)
    return render(request, "subtime_reserve.html", context={'shave_date': shave_date,
                                                            'barber_name': barber_name})


def reserve_time(request):
    #add reservation into the table
    reserved = False
    username = None
    if request.user.is_authenticated:
        username = request.user
    else:
        return HttpResponse("NOOO ! login needed")
    print("we are in reserve_time")
    shave_date = request.POST.get("shave_date")
    barber_name = request.POST.get("barber_name")
    selected_time = request.POST.get("time")
    selected_time+=":00"
    print("barber name:")
    print(barber_name)
    print("shave_date:")
    print(shave_date)
    print("selected time:")
    print(selected_time)
    queryUser = User.objects.filter(username=barber_name)
    queryPerson = Person.objects.filter(user=queryUser[0])
    queryBarber = Barber.objects.filter(user=queryPerson[0])
    print (str(queryBarber))
    queryset = TimeTable.objects.filter(barber=queryBarber[0],date= shave_date ).order_by('start_time')
    print (str(queryset))
    respons = queryset
    subtime_start = datetime.time(int(0), int(0), int(1))
    time_sec = calc_sec(subtime_start)
    #print (time_sec)
    for i in range(1, 74):
        for res in respons:
            #move on times in this spec day and calculate subtimes
            if (calc_sec(res.start_time) <=  calc_sec(selected_time)) and (calc_sec(selected_time) <= calc_sec(res.end_time)-1200):
                reserved = True
    #check this subtime is not in reserved table
    if reserved:
        person = Person.objects.filter(user=username)
        user_barber = User.objects.filter(username=barber_name)
        person_barber = Person.objects.filter(user=user_barber[0])
        customer = Customer.objects.filter(user=person[0])
        barber = Barber.objects.filter(user=person_barber[0])
        store = BarberShop.objects.filter(owner=barber[0])
        stored_time = calc_sec(selected_time)/1200
        queryReserve = Reserve.objects.filter(customer__in=customer, store__in=store, barber__in=barber, date=shave_date, sub_time=stored_time).count()
        print (queryReserve)
        if queryReserve == 0:
            reserve = Reserve(customer=customer[0], store=store[0], barber=barber[0], date=shave_date, sub_time=stored_time)
            reserve.save()
            return HttpResponse("DONE !")
        else:
            return HttpResponse("NOOO ! time is reserved")
    else:
        return HttpResponse("NOOO ! there is no available time")


def calc_sec(in_time):
    x = time.strptime(str(in_time).split(',')[0],'%H:%M:%S')
    time_sec = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return time_sec