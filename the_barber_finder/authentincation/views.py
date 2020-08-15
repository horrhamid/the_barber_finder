from django.shortcuts import render
from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Customer, Barber, Person

# Create your views here.


def main_view(request):
    return render(request, 'main2.html')


def register_view(request):
    return render(request, 'register.html')


# def logout_view(request):
#     pass


# def login_view(request):
#     pass
# global user_name33
# user_toke = ""
# user_name33 = "Anonymous"

def login_view(request):
    return render(request, 'login.html')


def login_view2(request):
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    print(username)
    print(pwd)
    user = authenticate(username=username, password=pwd)
    print(user)
    x = "invalid username or password"
    if user is None:
        return redirect("blog:Users")
    else:
        login(request, user)
        print("logged in")
        return redirect("blog:Users")


def logout_view(request):
    logout(request)
    return HttpResponse('Successfully Logged You Out Sir!')


def registration(request):
    first_name1 = request.POST.get('firstname')
    last_name1 = request.POST.get('lastname')
    user_name1 = request.POST.get('username')
    password1 = request.POST.get('password')
    email_add1 = request.POST.get('emaliadd')
    ph_num1 = request.POST.get('phonenum')
    role1 = request.POST.get('role')
    user, created = User.objects.get_or_create(username=user_name1)
    user.set_password(password1)
    user.save()
    print(user)
    if user:
        person = Person(user=user, first_name=first_name1, last_name=last_name1, email_address=email_add1, phone_num=ph_num1)
        person.save()
        if role1 == "Barber":
            b = Barber(user=person, rating=0, rate_number=0)
            b.save()
        else:
            c = Customer(user=person, wallet=0)
            c.save()
    else:
        redirect("blog:authentication:main")

    return redirect("blog:Users")
