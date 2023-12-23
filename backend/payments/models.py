from django.db import models


class Item(models.Model):
    """Модель для товаров."""
    name = models.CharField('название', max_length=50, blank=False)
    description = models.CharField('описание', max_length=150, blank=False)
    price = models.PositiveIntegerField('цена', blank=False, default=0,)

    currency = models.CharField(
        'валюта',
        choices=[("usd", "USD"), ("eur", "EUR")],
        max_length=5,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Модель для корзины."""
    item = models.ManyToManyField(Item, related_name='orders')

    # метод для общей суммы товаров
    def total_price(self):
        total_price = 0
        for item in self.item.all():
            total_price += item.price
        return total_price
