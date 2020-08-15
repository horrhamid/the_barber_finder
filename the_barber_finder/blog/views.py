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
    r = Barber.objects.filter(user=person.first())
    print(len(r))
    st = 2
    try:
        # print(r)
        # print("in try")
        st = 0
    except:
        st = 1
        print("in exept")

    if st == 1 :
        role = "Customer"
    else:
        role = "Barber"

    print(role)
    # if r[0]:
    #     role = "Customer"
    # else:
    #     role = "Barber"
    barbershops = BarberShop.objects.all()

    return render(request, 'dashboard.html', context={'name': name,
                                                      'shops': barbershops,
                                                      'role':role,})
def create_time_table(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    barber = request.POST.get('barbername')
    shop = request.POST.get('shopname')
    date = request.POST.get('date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    

    
    

