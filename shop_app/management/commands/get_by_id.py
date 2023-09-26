from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']

        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')


# class Command(BaseCommand):
#     help = "Get user by greater number."
#
#     def add_arguments(self, parser):
#         parser.add_argument('num', type=int, help='User number')
#
#     def handle(self, *args, **kwargs):
#         age = kwargs['age']
#
#         user = Client.objects.filter(number__gt=age)
#         self.stdout.write(f'{user}'
