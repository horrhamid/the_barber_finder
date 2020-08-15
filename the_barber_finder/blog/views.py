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
                                                      'shops': barbershops,
                                                      'role': role, })

