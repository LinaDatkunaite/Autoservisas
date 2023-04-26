from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'service', 'quantity', 'order_date', )


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model',  'plate_nr', 'vin_number')
    search_fields = ('plate_nr', 'vin_number', 'client')
    list_filter = ('client', 'car_model')

admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(Order, OrderAdmin)
