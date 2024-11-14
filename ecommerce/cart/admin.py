from django.contrib import admin
from cart.models import Cart,Order_details,Payments
# Register your models here.
from django.http import HttpResponse


admin.site.register(Cart)
admin.site.register(Order_details)
admin.site.register(Payments)
