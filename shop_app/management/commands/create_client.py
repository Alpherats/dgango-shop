from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = 'create clients'

    def handle(self, *args, **kwargs):
        for i in range(1, 5 + 1):
            client = Client(name=f'Client{i}', mail=f'mail{i}@mail.ru', number=f'123456{i}',
                            home_address=f'address_{i}')
            client.save()
