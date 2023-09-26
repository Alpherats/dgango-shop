from django.core.management.base import BaseCommand
from shop_app.models import Item


class Command(BaseCommand):
    help = 'create items'

    def handle(self, *args, **kwargs):
        for i in range(1, 10 + 1):
            item = Item(item=f'item{i}', desc=f'my description{1}', price=10,
                        amount=1)
            item.save()
