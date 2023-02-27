from celery import shared_task

from product.models import IdString, Category, Product
from product.rozetka_api import RozetkaAPI


@shared_task(name='start_scraping_task', queue='celery')
def start_scraping_task():
    string_object = IdString.objects.first()
    id_list = string_object.input_string
    string_object.delete()
    if ';' in id_list:
        id_list = id_list.replace(';', '\n')
    if ',' in id_list:
        id_list = id_list.replace(',', '\n')
    if ' ' in id_list:
        id_list = id_list.replace(' ', '\n')
    if '\n\n' in id_list:
        id_list = id_list.replace('\n\n', '\n')
    id_list = id_list.split('\n')

    rztk = RozetkaAPI()
    for product_id in id_list:
        product = rztk.get_item_data(item_id=product_id)

        product_category = Category.objects.get_or_create(
            category_id=product['category_id'],
            defaults={
                'category_title': product['category_title'],
            }
        )[0]

        sell_status = True if product['sell_status'].lower() == 'available' else False
        Product.objects.update_or_create(
            item_id=product_id,
            defaults={
                'item_id': product['item_id'],
                'title': product['title'],
                'old_price': product['old_price'],
                'current_price': product['current_price'],
                'sell_status': sell_status,
                'href': product['href'],
                'brand': product['brand'],
                'category': product_category
            }
        )



