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
<<<<<<< HEAD
    print(name)
    person = Person.objects.filter(user=request.user)
    # print(person)
    if person:
        r = Barber.objects.filter(user=person)
    # st = print(len(r))
    st = 1
    role = ''
    if st:
        role = "Barber"
    else:
        role = "Customer"

    print(role)
    # if r[0]:
    #     role = "Customer"
    # else:
    #     role = "Barber"
=======
    if name:
        print(name)
        person = Person.objects.filter(user=request.user)
        print(person[0])
        r = Barber.objects.filter(user=person)


        # st = print(len(r))
        st = 1
        role = ''
        if st:
            role = "Barber"
        else:
            role = "Customer"

        print(role)
        # if r[0]:
        #     role = "Customer"
        # else:
        #     role = "Barber"
>>>>>>> c369bdd19660f73dc6f20becfb11daf444fac648
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



    
    

