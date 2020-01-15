from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    short_description = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    size = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=10000)
    image = models.CharField(max_length=10000)

    def __str__(self):
        return self.name



