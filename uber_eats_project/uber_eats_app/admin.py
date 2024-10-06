from django.contrib import admin
from .models import Customer, Restaurant, Dish, Order

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Order)

