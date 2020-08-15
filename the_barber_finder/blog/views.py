# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BarberShop, Barber, Person, Customer
# Create your views here.


def users_view(request):
    name = request.user.username
    print(name)
    person = Person.objects.filter(user=request.user)
    print(person)
    r = Barber.objects.filter(user=person)
    role = "x"
    if r[0]:
        role = "Customer"
    else:
        role = "Barber"
    barbershops = BarberShop.objects.all()

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
    

