from django.db import models


class Item(models.Model):
    """
        Django Модель Item с полями (name, description, price)
    """

    id = models.IntegerField(primary_key=True, serialize=True, unique=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = models.FloatField(default=1.00)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
