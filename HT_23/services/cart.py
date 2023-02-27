from django.contrib import messages
from django.http import JsonResponse

from product.forms import InCartProduct, RemoveForm, MAX_ADD_TO_CARTS_QTY
from product.models import Product


def authenticated_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            msg_text = 'Only authenticated users can use cart!'
            messages.error(request=request, message=msg_text)
            return JsonResponse({'message': msg_text}, status=300)
            # raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner


def get_product_title(pk):
    return Product.objects.get(pk=int(pk)).title


def get_cart_context(request):
    try:
        cart = request.session.get('cart')
        session_cart = request.session.setdefault('cart', {})
        items = Product.objects.filter(id__in=cart.keys()).values(
            'id', 'title', 'sell_status', 'current_price'
        )

        sum_cost = 0
        available_items = []
        removed_items = []
        for item in items:
            if not item['sell_status']:
                removed_items.append(item['title'])
                del session_cart[str(item['id'])]
                continue

            quantity = cart[str(item['id'])]
            sum_cost += item['current_price'] * quantity

            item['in_cart_form'] = InCartProduct(initial={
                'internal_item_id': item['id'],
                'quantity': quantity,
            })
            item['form_remove'] = RemoveForm(initial={'id': item['id']})

            available_items.append(item)
        if removed_items:
            message = f'Some products removed from your cart, due out of stock: ' \
                      f'{"; ".join(removed_items)}'
            messages.success(request=request, message=message)
            request.session.modified = True
        return {
            'items': available_items,
            'sum_cost': sum_cost
        }
    except Exception:
        return {'items': [], 'sum_cost': 0}


def add_product_to_cart(request):
    form = InCartProduct(request.POST)
    if not form.is_valid():
        return 'Form error: Wrong quantity!', 400
    data = form.cleaned_data
    cart = request.session.setdefault('cart', {})

    cart.setdefault(str(data['internal_item_id']), 0)
    cart[str(data['internal_item_id'])] += data['quantity']
    if cart[str(data['internal_item_id'])] > MAX_ADD_TO_CARTS_QTY:
        cart[str(data['internal_item_id'])] = MAX_ADD_TO_CARTS_QTY

    request.session.modified = True
    product_title = get_product_title(pk=data['internal_item_id'])
    return f'"{product_title}" added to your cart!', 200


def remove_product_from_cart(request):
    form = RemoveForm(request.POST)
    if not form.is_valid():
        return 'Unknown error!', 400
    cart = request.session.setdefault('cart', {})
    deleted_item_id = str(form.cleaned_data['id'])
    del cart[deleted_item_id]
    request.session.modified = True
    product_title = get_product_title(pk=deleted_item_id)
    return f'"{product_title}" removed from your cart!', 200


def change_product_quantity_in_cart(request):
    form = InCartProduct(request.POST)
    if not form.is_valid():
        return 'Wrong quantity!', 400
    data = form.cleaned_data

    cart = request.session.setdefault('cart', {})
    cart.setdefault(str(data['internal_item_id']), 0)
    cart[str(data['internal_item_id'])] = data['quantity']
    request.session.modified = True
    return 'Product quantity has been changed!', 200
