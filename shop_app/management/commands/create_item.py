from django.core.management.base import BaseCommand
from shop_app.models import Item, ItemImg


class Command(BaseCommand):
    help = 'create items'

    # def handle(self, *args, **kwargs):
    #     for i in range(11, 20 + 1):
    #         item = Item(item=f'item{i}', desc=f'my description{1}', price=10,
    #                     amount=1, image='')
    #         item.save()
    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            item = ItemImg(item=f'item{i}', price=10, image='')
            item.save()
