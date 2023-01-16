import django
django.setup()

from rozetka_api import RozetkaAPI
from scraper.models import IdObject, Product


def scrape():
    rztk = RozetkaAPI()
    for item in IdObject.objects.all():
        product = rztk.get_item_data(item_id=item.item_id)
        print(product)
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
    return Product.objects.all()


if __name__ == '__main__':
    scrape()
