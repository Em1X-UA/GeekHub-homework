from subprocess import Popen

from django.contrib import messages
from django.shortcuts import redirect

from product.models import Product, IdString, Category
from product.forms import EditProduct


def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            msg_text = 'Only superusers allow this function!'
            messages.error(request=request, message=msg_text)
            return redirect(to='product:my_products')
            # raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner


def get_available_categories_list():
    # delete empty categories
    # Category.objects.filter(product__isnull=True).delete()
    # categories = Category.objects.all().values('id', 'category_title')

    # don't show empty categories, but don't delete it
    categories = []
    for category in Category.objects.filter(product__isnull=False).values('id', 'category_title'):
        if category not in categories:
            categories.append(category)
    return categories


def start_scraping(request):
    response = request.GET.get('id_string')
    IdString.objects.create(input_string=response)
    Popen(['python', 'subscraper.py'])


def edit_product_form(product: Product):
    return EditProduct(initial={
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


def update_product(data):
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
