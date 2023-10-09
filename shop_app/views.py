from django.shortcuts import render
from shop_app.models import Client, Order_shop
from django.utils import timezone
from datetime import timedelta


def hello_view(request):
    context = {
        "name": 'Tony'
    }
    return render(request, 'shop_app/index.html', context)


def show_items(request, id, days):
    client = Client.objects.filter(pk=id).first()

    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)

    orders = Order_shop.objects.filter(client=id, ordered_at__range=(start_date, end_date))
    print(f'start date = {start_date} , end date = {end_date}')
    orders_lst = []
    for order in orders:
        orders_lst.append(order)
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {'name': client.name,
               'orders': orders_lst,
               'days': days, }
    return render(request, 'shop_app/index.html', context)
