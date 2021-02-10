from django.contrib import admin

# Register your models here.
from .models import CartItem, Order, OrderItem


admin.site.register([CartItem, Order, OrderItem])
