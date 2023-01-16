import django
django.setup()

from scraper.models import IdObject, Product, IdString

from rozetka_api import RozetkaAPI


def parse_string():
    string_object = IdString.objects.all()[0]
    response = string_object.input_string
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
            IdObject.objects.create(item_id=id_obj.strip())
    string_object.delete()


def scrape():
    rztk = RozetkaAPI()
    for item in IdObject.objects.all():
        product = rztk.get_item_data(item_id=item.item_id)
        Product.objects.create(
            item_id=product['item_id'],
            title=product['title'],
            old_price=product['old_price'],
            current_price=product['current_price'],
            href=product['href'],
            brand=product['brand'],
            category=product['category']
            )
        item.delete()


if __name__ == '__main__':
    parse_string()
    scrape()
