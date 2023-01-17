from urllib.parse import urljoin

import requests


class RozetkaAPI:
    """
    Class for parsing Rozetka items by ID.
    """
    _HOME_URL = 'https://rozetka.com.ua/'
    _API_URL = 'api/product-api/v4/goods/get-main'
    _BASE_URL = urljoin(_HOME_URL, _API_URL)

    def get_item_data(self, item_id: int | str):
        """
        Parsing response json and return Product object.
        """
        response = requests.get(self._BASE_URL, params={"goodsId": item_id})
        data = response.json()['data']

        return dict(
            item_id=data['id'],
            title=data['title'],
            old_price=float(data['old_price']),
            current_price=float(data['price']),
            href=data['href'],
            brand=data['brand'],
            category=data['last_category']['title'],
        )
