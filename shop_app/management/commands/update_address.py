from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Update user address by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('address', type=str, help="User's address")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        address = kwargs.get('address')
        client = Client.objects.filter(pk=pk).first()
        client.home_address = address
        client.save()
        self.stdout.write(f'{client}')
