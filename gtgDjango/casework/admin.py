from django.contrib import admin
from .models import Drink, Category, Order

# Register your models here.
admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(Order)