from django.db import models


class Product(models.Model):
    item_id = models.CharField(max_length=15, default='n/a')
    title = models.CharField(max_length=255, default='n/a')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    href = models.URLField(name='href')
    brand = models.CharField(max_length=50, default='n/a', null=True)
    category = models.CharField(max_length=100, default='n/a')


class IdObject(models.Model):
    item_id = models.CharField(max_length=15, default='')


class IdString(models.Model):
    input_string = models.CharField(max_length=10_000)
