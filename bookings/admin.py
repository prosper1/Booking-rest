from django.contrib import admin
from .models import Item, Restaurant,Booking

# Register your models here.

admin.site.register(Item)
admin.site.register(Restaurant)
admin.site.register(Booking)
