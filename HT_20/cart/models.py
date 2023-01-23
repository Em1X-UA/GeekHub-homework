from django.db import models


class UserCart(models.Model):
    internal_item_id = models.IntegerField()
    item_qty = models.IntegerField(default=1)
