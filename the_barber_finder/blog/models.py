from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="person")
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    phone_num = models.CharField(max_length=15, blank=True)
    email_address = models.EmailField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # token = models.CharField(max_length=50, blank=True, null=True)
    avatar = models. ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Barber(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    validation_card_num = models.CharField(max_length=25, blank=True, unique=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    rate_number = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user.username


class Customer(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    # barber_list = models.ManyToManyField(Barber)
    wallet = models.DecimalField(default=0, max_digits=10, decimal_places=1)

    def __str__(self):
        return self.user.user.username


class BarberShop(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    address = models.CharField(max_length=200)
    owner = models.OneToOneField(Barber, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    name = models.CharField(max_length=50)
    barbers = models.ManyToManyField(Barber, related_name='barbers')
    desc = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    store = models.ForeignKey(BarberShop, on_delete=models.CASCADE)
    start_time = models.TimeField(default=0)
    end_time = models.TimeField(null=True)
    date = models.DateField(default=models.DateField(auto_now=True))

    def __str__(self):
        return self.barber.user.user.username


class Reserve(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(BarberShop, on_delete=models.CASCADE)
    # for x in store.barbers:
    #     st_brb.append(x.user.user_name)
    # print(st_brb)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    sub_time = models.IntegerField(null=True)






