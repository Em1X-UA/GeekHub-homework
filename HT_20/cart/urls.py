from django.urls import path

from .views import cart_page, add_to_cart, remove_from_cart, change_qty, clear_cart


urlpatterns = [
    path('', cart_page, name='cart'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('remove_from_cart', remove_from_cart, name='remove_from_cart'),
    path('change_qty', change_qty, name='change_qty'),
    path('clear_cart', clear_cart, name='clear_cart')
]
