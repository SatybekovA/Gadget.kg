from django.contrib import admin
from .models import Customer, Employee, Order, Gender

# Register your models here.

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Gender)