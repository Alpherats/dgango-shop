from django.db import models


class FlipCoin(models.Model):
    is_eagle = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Eagle? Defenetly {self.is_eagle}, at time {self.created_at}'
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Full name - {self.surname} {self.name}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    viewed = models.IntegerField()
    published = models.BooleanField(default=False)