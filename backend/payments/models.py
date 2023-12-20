from django.db import models


class Item(models.Model):
    name = models.CharField('название', max_length=50, blank=False)
    description = models.CharField('описание', max_length=150, blank=False)
    price = models.PositiveIntegerField('цена', blank=False, default=0,)

    def __str__(self):
        return self.name
