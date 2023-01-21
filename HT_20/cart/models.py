from django.db import models


class UserCart(models.Model):
    # user = ''
    internal_item_id = models.IntegerField(max_length=6)
    item_qty = models.IntegerField(default=1)
