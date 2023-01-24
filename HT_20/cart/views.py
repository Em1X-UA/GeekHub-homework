from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods

from scraper.forms import InCartProduct, RemoveFromCart, MAX_ADD_TO_CARTS_QTY
from scraper.models import Product


def cart_page(request):
    cart = request.session.get('cart')
    try:
        items = list(Product.objects.filter(id__in=cart.keys()))
    except Exception:
        return render(request=request,
                      template_name='cart.html',
                      context={'items': [], 'sum_cost': 0,})
    sum_cost = 0

    available_items = []
    for item in items:
        quantity = cart[str(item.id)]
        # remove unavailable items if user added it (maybe earlier)
        if item.sell_status != 'available':
            del item
            continue

        available_items.append(item)
        sum_cost += item.current_price * quantity

        item.in_cart_form = InCartProduct(initial={
            'internal_item_id': item.id,
            'quantity': quantity,
        })
        item.form_remove = RemoveFromCart(initial={'int_id': item.id})

    return render(request=request,
                  template_name='cart.html',
                  context={
                      'items': available_items,
                      'sum_cost': sum_cost,
                  })


@require_http_methods(['POST'])
def add_to_cart(request):
    form = InCartProduct(request.POST)
    if not form.is_valid():
        return redirect(to=reverse(viewname='my_products'))
    data = form.cleaned_data

    cart = request.session.setdefault('cart', {})
    cart.setdefault(str(data['internal_item_id']), 0)
    cart[str(data['internal_item_id'])] += data['quantity']
    if cart[str(data['internal_item_id'])] > MAX_ADD_TO_CARTS_QTY:
        cart[str(data['internal_item_id'])] = MAX_ADD_TO_CARTS_QTY
    request.session.modified = True

    return redirect(to=reverse(viewname='product_data',
                               kwargs={'pk': data['internal_item_id']}))


@require_http_methods(['POST'])
def remove_from_cart(request):
    form = RemoveFromCart(request.POST)
    if not form.is_valid():
        return redirect(to=reverse(viewname='cart'))

    id_to_delete = str(form.cleaned_data['int_id'])
    cart = request.session.setdefault('cart', {})
    del cart[id_to_delete]
    request.session.modified = True

    return redirect(to=reverse(viewname='cart'))


@require_http_methods(['POST'])
def change_qty(request):
    form = InCartProduct(request.POST)
    if not form.is_valid():
        return redirect(to=reverse(viewname='cart'))
    data = form.cleaned_data

    cart = request.session.setdefault('cart', {})
    cart.setdefault(str(data['internal_item_id']), 0)
    cart[str(data['internal_item_id'])] = data['quantity']
    request.session.modified = True

    return redirect(to=reverse(viewname='cart'))


@require_http_methods(['POST'])
def clear_cart(request):
    request.session.get('cart').clear()
    request.session.modified = True
    return redirect(to=reverse(viewname='cart'))
