"""
- rozetka_api.py, де створти клас RozetkaAPI, який буде містити 1 метод
get_item_data, який на вхід отримує id товара з сайту розетки та повертає
словник з такими даними: item_id (він же і приймається на вхід), title,
old_price, current_price, href (лінка на цей товар на сайті), brand, category.
Всі інші методи, що потрібні для роботи мають бути приватні/захищені.
"""


from urllib.parse import urljoin

import requests


class RozetkaAPI:
    """
    Class for parsing Rozetka items by ID.
    """
    _HOME_URL = 'https://rozetka.com.ua/'
    _API_URL = 'api/product-api/v4/goods/get-main'
    _BASE_URL = urljoin(_HOME_URL, _API_URL)

    def get_item_data(self, item_id):
        """
        Parsing response json and return dict with item parameters.
        """
        page = requests.get(self._BASE_URL, params={"goodsId": item_id}).json()
        if page['success'] is False:  # return False if item_id incorrect.
            return False
        data = page['data']

        # parsing saved json file
        # import json
        # with open('get-main.json') as file:
        #     data = json.load(file)['data']

        item_data = dict()
        item_data['item_id'] = data['id']
        item_data['title'] = data['title']
        item_data['old_price'] = float(data['old_price'])
        item_data['current_price'] = float(data['price'])
        item_data['href'] = data['href']
        item_data['brand'] = data['brand']
        item_data['category'] = data['last_category']['title']
        return item_data
