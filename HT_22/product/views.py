from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from product.forms import InCartProduct, EditProduct, RemoveForm
from product.models import Product, Category
from services import product as prod_service


@prod_service.superuser_only
def add_products(request):
    return render(request=request,
                  template_name='add_products.html')


@prod_service.superuser_only
def scraper(request):
    prod_service.start_scraping(request=request)
    return JsonResponse(data={'message': 'Scraping started!'}, status=200)


def my_products(request):
    categories = prod_service.get_available_categories_list()
    products_list = Product.objects.all().values('id', 'title', 'current_price')
    return render(request=request,
                  template_name='my_products.html',
                  context={
                      'products': products_list,
                      'categories': categories,
                  })


def product_data(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = InCartProduct(initial={
        'internal_item_id': product.id,
        'sell_status': product.sell_status,
        'quantity': 1,
    })
    return render(request=request,
                  template_name='product_data.html',
                  context={
                      'product': product,
                      'form': form,
                      'remove_form': RemoveForm(initial={'id': product.id}),
                  })


def category_products(request, pk):
    category_title = Category.objects.filter(id=pk).values_list('category_title', flat=True)[0]
    categories = prod_service.get_available_categories_list()
    products_list = Product.objects.filter(category_id=pk).values('id', 'title', 'current_price')
    return render(request=request,
                  template_name='category_products.html',
                  context={
                      'products': products_list,
                      'category': category_title,
                      'categories_list': categories,
                  })


@prod_service.superuser_only
def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = prod_service.edit_product_form(product=product)
    return render(request=request,
                  template_name='product_edit.html',
                  context={
                      'product': product,
                      'form': form,
                  })


@prod_service.superuser_only
@require_http_methods(['POST'])
def edit_confirm(request):
    form = EditProduct(request.POST)
    if not form.is_valid():
        return redirect(to='product:product_data', pk=form.id)
    data = form.cleaned_data
    prod_service.update_product(data=data)
    messages.success(request=request, message='Product edited!')
    return redirect(to='product:product_data', pk=data['id'])


@prod_service.superuser_only
@require_http_methods(['POST'])
def delete_product(request):
    form = RemoveForm(request.POST)
    if not form.is_valid():
        return redirect(to='product:product_data', pk=form.cleaned_data['id'])
    Product.objects.filter(id=form.cleaned_data['id']).delete()
    messages.success(request=request, message='Product deleted!')
    return redirect(to="product:my_products")
