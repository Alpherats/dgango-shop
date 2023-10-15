from django.shortcuts import render, get_object_or_404
from shop_app.models import Client, Order_shop, Item, ItemImg
from django.utils import timezone
from datetime import timedelta
from .forms import EditProduct


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


def edit_item(request, pk):
    item = get_object_or_404(ItemImg, pk=pk)

    if request.method == 'POST':
        form = EditProduct(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'shop_app/item_form.html', {'form': form})

    else:
        form = EditProduct(instance=item)

    return render(request, 'shop_app/item_form.html', {'form': form})
