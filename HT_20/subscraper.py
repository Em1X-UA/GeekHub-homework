import django
django.setup()

from scraper.models import Product, IdString

from scraper.rozetka_api import RozetkaAPI


def parse_string():
    string_object = IdString.objects.first()
    response = string_object.input_string
    string_object.delete()

    if ';' in response:
        response.replace(';', '\n')
    if ',' in response:
        response.replace(',', '\n')
    if ' ' in response:
        response.replace(' ', '\n')
    if '\n\n' in response:
        response.replace('\n\n', '\n')
    response = response.split('\n')

    for id_obj in response:
        if id_obj != '':
            yield id_obj.strip()


def main():
    rztk = RozetkaAPI()
    for product_id in parse_string():
        product = rztk.get_item_data(item_id=product_id)
        Product.objects.update_or_create(
            item_id=product_id,
            defaults={
                'item_id': product['item_id'],
                'title': product['title'],
                'old_price': product['old_price'],
                'current_price': product['current_price'],
                'sell_status': product['sell_status'],
                'href': product['href'],
                'brand': product['brand'],
                'category': product['category']
            }
        )


if __name__ == '__main__':
    main()
