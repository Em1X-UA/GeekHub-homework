from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=100, default='n/a')
    category_id = models.IntegerField(default=0)

    def __str__(self):
        return f'ID: {self.id} | Title: {self.category_title}'


class Product(models.Model):
    item_id = models.CharField(max_length=15, default='n/a')
    title = models.CharField(max_length=255, default='n/a')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    sell_status = models.BooleanField(default=False, blank=False, null=True)
    href = models.URLField(name='href')
    brand = models.CharField(max_length=50, default='n/a', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        try:
            category = self.category.category_title
        except AttributeError:
            category = 'CHOOSE CATEGORY'
        return f'ID: {self.id} | ' \
               f'Title: {self.title} | ' \
               f'Category: {category}'


class IdString(models.Model):
    input_string = models.CharField(max_length=10_000)
