import django
django.setup()

from product.models import Product, IdString, Category

from product.rozetka_api import RozetkaAPI


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
                # 'sell_status': product['sell_status'],
                'sell_status': sell_status,
                'href': product['href'],
                'brand': product['brand'],
                'category': product_category
            }
        )


if __name__ == '__main__':
    main()
