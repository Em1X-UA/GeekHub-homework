from subprocess import Popen

from django.shortcuts import render, redirect, get_object_or_404

from scraper.forms import InCartProduct
from scraper.models import Product, IdString


def home(request):
    return render(request=request,
                  template_name='home.html')


def add_products(request):
    return render(request=request,
                  template_name='add_products.html')


def scraper(request):
    response = request.GET.get('id_string')
    IdString.objects.create(input_string=response)
    Popen(['python', 'subscraper.py'])
    return redirect(to=my_products)


def my_products(request):
    return render(request=request,
                  template_name='my_products.html',
                  context={'products': Product.objects.all()})


def product_data(request, pk):
    product = get_object_or_404(Product, id=pk)
    product_qty = 1 if product.sell_status == 'available' else 0
    form = InCartProduct(initial={'internal_item_id': product.id,
                                  'sell_status': product.sell_status,
                                  'quantity': product_qty})
    return render(request=request,
                  template_name='product_data.html',
                  context={'product': product, 'form': form})
