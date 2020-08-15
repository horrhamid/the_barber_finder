from django.contrib import admin
from .models import Customer, Person, Barber, BarberShop, TimeTable, Reserve
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'wallet',
    )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'user',
        'phone_num',
        'email_address',
        'create_date',
    )


class BarberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'validation_card_num',
        'rating',
    )


class BarberShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address',
        'owner',
        'name',
        'desc',
    )


class TimeTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'barber',
        'store',
        'start_time',
        'end_time',
        'date',
    )


class ReserveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'store',
        'barber',
        'sub_time',
        'date',
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Person, UserAdmin)
admin.site.register(Barber, BarberAdmin)
admin.site.register(BarberShop, BarberShopAdmin)
# admin.site.register(BarberShop)
admin.site.register(TimeTable, TimeTableAdmin)
# admin.site.register(TimeTable)
admin.site.register(Reserve, ReserveAdmin)

