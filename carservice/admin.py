from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order, OrderList


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0 # išjungia papildomas tuščias eilutes įvedimui

class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date')
    inlines = [OrderInline]
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'service', 'quantity', 'price', )


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'display_cars')



class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model',  'plate_nr', 'vin_number')
    search_fields = ('plate_nr', 'vin_number', 'client')
    list_filter = ('client', 'car_model')

admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice, ServicePriceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderList, OrderListAdmin)
