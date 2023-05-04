from django.shortcuts import render, get_object_or_404
from .models import Car, CarModel, Order, OrderList, ServicePrice, Service
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    return render(request, 'index.html', {'cars': CarModel.objects.all(),'cars_count': CarModel.objects.all().count(), 'services': Service.objects.all(), 'services_count': Service.objects.all().count() })

def orders(request):
    return render(request, 'orders.html', {'orders': OrderList.objects.all()})

def specific_order(request, order_list_id):
    order_list = get_object_or_404(OrderList, pk=order_list_id)
    orders = Order.objects.filter(order_list_id__exact=order_list_id)
    return render(request, 'specific_order.html', {'order_list': order_list, "orders": orders})

def cars(request):
    paginator = Paginator(Car.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars
    }
    return render(request, 'cars.html', context)



def car(request, car_model_id):
    repaired_model = get_object_or_404(CarModel, pk=car_model_id)
    single_car = Car.objects.filter(car_model__exact=car_model_id)
    return render(request, 'car.html', {'car': single_car, 'repaired_model': repaired_model})


def car1(request, car_id):
    repaired_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car1.html', {'repaired_car': repaired_car})

def services(request):
    return render(request, 'services.html', {'services': Service.objects.all()})

def service(request, service_id):
    specific_service = ServicePrice.objects.filter(service__exact=service_id)
    return render(request, 'specific_service.html', {'specific_service': specific_service})


def search(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(car_model__brand__icontains=query) | Q(car_model__car_model__icontains=query) | Q(plate_nr__icontains=query)
                                        | Q(vin_number__icontains=query) | Q(client__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})