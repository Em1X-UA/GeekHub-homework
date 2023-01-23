from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


MAX_ADD_TO_CARTS_QTY = 10


class InCartProduct(forms.Form):
    internal_item_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(MAX_ADD_TO_CARTS_QTY),
    ])


class RemoveFromCart(forms.Form):
    int_id = forms.IntegerField(widget=forms.HiddenInput())
