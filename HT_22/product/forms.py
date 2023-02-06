from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Category


MAX_ADD_TO_CARTS_QTY = 10


class InCartProduct(forms.Form):
    internal_item_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(MAX_ADD_TO_CARTS_QTY),
    ])


class RemoveForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())


class EditProduct(forms.Form):
    category_choices = []
    for category in Category.objects.all():
        category_choices.append((category.id, category.category_title))
    category = forms.ChoiceField(choices=category_choices)

    id = forms.IntegerField(widget=forms.HiddenInput())
    item_id = forms.IntegerField(widget=forms.HiddenInput())
    title = forms.CharField(max_length=255)
    old_price = forms.DecimalField(max_digits=10, decimal_places=2)
    current_price = forms.DecimalField(max_digits=10, decimal_places=2)

    sell_choices = [(True, 'In stock'), (False, 'Not in stock')]
    sell_status = forms.ChoiceField(choices=sell_choices)

    href = forms.CharField(max_length=255)
    brand = forms.CharField(max_length=50, required=False)
