from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse

from services import cart as cart_service


@cart_service.authenticated_only
def cart_page(request):
    context = cart_service.get_cart_context(request=request)
    return render(request=request,
                  template_name='cart.html',
                  context=context)


@cart_service.authenticated_only
@require_http_methods(['POST'])
def add_to_cart(request):
    response_message, status = cart_service.add_product_to_cart(request=request)
    return JsonResponse(data={'message': response_message}, status=status)


@require_http_methods(['POST'])
def remove_from_cart(request):
    response_message, status = cart_service.remove_product_from_cart(request=request)
    return JsonResponse(data={'message': response_message}, status=status)


@require_http_methods(['POST'])
def change_qty(request):
    response_message, status = cart_service.change_product_quantity_in_cart(request=request)
    return JsonResponse(data={'message': response_message}, status=status)


@require_http_methods(['POST'])
def clear_cart(request):
    request.session.get('cart').clear()
    request.session.modified = True
    return JsonResponse(data={'message': 'Cart cleared!'}, status=200)
