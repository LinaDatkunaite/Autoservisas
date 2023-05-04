from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_list_id>', views.specific_order, name='specific_order'),
    path('cars/', views.cars, name='cars'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>', views.service, name='service'),
    path('car/<int:car_model_id>', views.car, name='car'),
    path('car1/<int:car_id>', views.car1, name='car1'),
    path('search/', views.search, name='search'),
]