from django.contrib import admin
from .models import Property, Category, Reservation


admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Reservation)