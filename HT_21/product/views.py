from subprocess import Popen

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from product.forms import InCartProduct, EditProduct, RemoveForm
from product.models import Product, IdString, Category


def not_superuser_msg(request):
    msg_text = 'Only superusers allow this function!'
    return messages.error(request=request, message=msg_text)


def add_products(request):
    if not request.user.is_superuser:
        not_superuser_msg(request)
        return redirect(to=my_products)
    return render(request=request,
                  template_name='add_products.html')


def scraper(request):
    if not request.user.is_superuser:
        not_superuser_msg(request)
        return redirect(to=my_products)
    response = request.GET.get('id_string')
    IdString.objects.create(input_string=response)
    Popen(['python', 'subscraper.py'])
    messages.success(request=request, message='New products added!')
    return redirect(to=my_products)


def my_products(request):
    # delete empty categories
    # Category.objects.filter(product__isnull=True).delete()
    # categories = Category.objects.all()

    # don't show empty categories, but don't delete it
    categories = []
    for category in Category.objects.filter(product__isnull=False):
        if category not in categories:
            categories.append(category)

    return render(request=request,
                  template_name='my_products.html',
                  context={
                      'products': Product.objects.all(),
                      'categories': categories,
                  })


def product_data(request, pk):
    product = get_object_or_404(Product, id=pk)
    stock = True if product.sell_status == 'available' else False
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
                      'stock': stock,
                      'remove_form': RemoveForm(initial={'id': product.id}),
                  })


def category_products(request, pk):
    category_title = Category.objects.filter(id=pk)[0].category_title
    return render(request=request,
                  template_name='category_products.html',
                  context={
                      'products': Product.objects.filter(category_id=pk),
                      'category': category_title,
                  })


def edit_product(request, pk):
    if not request.user.is_superuser:
        not_superuser_msg(request)
        return redirect(to=my_products)

    product = get_object_or_404(Product, id=pk)
    form = EditProduct(initial={
        'id': product.id,
        'item_id': product.item_id,
        'title': product.title,
        'old_price': product.old_price,
        'current_price': product.current_price,
        'sell_status': product.sell_status,
        'href': product.href,
        'brand': product.brand,
        'category': product.category_id,
    })
    return render(request=request,
                  template_name='product_edit.html',
                  context={
                      'product': product,
                      'form': form,
                  })


@require_http_methods(['POST'])
def edit_confirm(request):
    if not request.user.is_superuser:
        not_superuser_msg(request)
        return redirect(to=my_products)

    form = EditProduct(request.POST)
    if not form.is_valid():
        return redirect(to=product_data, pk=form.id)
    data = form.cleaned_data
    category = Category.objects.filter(id=data['category'])[0]
    Product.objects.update_or_create(id=data['id'], defaults={
        'title': data['title'],
        'old_price': data['old_price'],
        'current_price': data['current_price'],
        'sell_status': data['sell_status'],
        'href': data['href'],
        'brand': data['brand'],
        'category': category,
    })
    messages.success(request=request, message='Product edited!')
    return redirect(to=product_data, pk=data['id'])


@require_http_methods(['POST'])
def delete_product(request):
    if not request.user.is_superuser:
        not_superuser_msg(request)
        return redirect(to=my_products)
    form = RemoveForm(request.POST)
    if not form.is_valid():
        return redirect(to=product_data, pk=form.cleaned_data['id'])
    Product.objects.filter(id=form.cleaned_data['id']).delete()
    messages.success(request=request, message=f'Product deleted!')
    return redirect(to=my_products)
