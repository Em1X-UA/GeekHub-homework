from django.shortcuts import render


MAX_ADD_TO_CARTS_QTY = 10


def cart_page(request):
    return render(request=request,
                  template_name='cart.html')
