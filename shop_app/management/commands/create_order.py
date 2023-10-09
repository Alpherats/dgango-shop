from django.core.management.base import BaseCommand
from shop_app.models import Order_shop, Client, Item


class Command(BaseCommand):
    help = 'create items'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        # client = Client.objects.filter(name='Client1')
        pk = kwargs['pk']

        client = Client.objects.filter(pk=pk).first()

        items = Item.objects.filter(pk=pk).first()

        order = Order_shop(client=client, items=items, total_price=15000)
        order.save()
