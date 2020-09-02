from django.contrib import admin
from .models import Order, RareMetalPrice, RareMetalSupplyAndDemand
# Register your models here.

admin.site.register(Order)
admin.site.register(RareMetalPrice)
admin.site.register(RareMetalSupplyAndDemand)