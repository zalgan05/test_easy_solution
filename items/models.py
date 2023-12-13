from django.db import models


MAX_LENGHT = 100


class Item(models.Model):
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название товара'
    )
    description = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name


class Price(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='item_prices',
        verbose_name='Товар'
    )
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Валюта'
    )
    stripe_price_id = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='ID цены товара'
    )

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def get_display_price(self):
        return f'{self.price} {self.currency}'


class OrderItem(models.Model):
    session_id = models.CharField(max_length=MAX_LENGHT)
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )


class Discount(models.Model):
    pass


class Tax(models.Model):
    pass
