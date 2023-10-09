from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    number = models.CharField(max_length=15)
    home_address = models.TextField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client {self.name} with {self.mail} & {self.number}'


class Item(models.Model):
    item = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    amount = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Item {self.item} with price {self.price} & amount {self.amount}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ordered_at = models.DateTimeField(auto_now_add=True)


class Order_shop(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ordered_at = models.DateTimeField(auto_now_add=True)
