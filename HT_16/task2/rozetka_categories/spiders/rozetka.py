from urllib.parse import urljoin

import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from rozetka_categories.items import RozetkaCategoriesItem


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    HOME_URL = 'https://rozetka.com.ua/ua/'
    API_PATH = 'api/product-api/v4/goods/get-main'
    api_url = urljoin(HOME_URL, API_PATH)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) '
                      'Gecko/20100101 Firefox/108.0',
        'Accept': 'application/json, text/plain, */*'
    }
    
    def __init__(self, category):
        super(RozetkaSpider, self).__init__()
        self.category = category

    def start_requests(self):
        url = urljoin(self.HOME_URL, self.category)
        yield Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        all_id_css_path = "ul.catalog-grid li.catalog-grid__cell div.g-id::text"
        id_list = response.css(all_id_css_path).getall()
        for item_id in id_list:
            yield Request(url=self.api_url + f'?goodsId={item_id}',
                          headers=self.headers,
                          callback=self.get_item_data)

        next_page_css = 'a.button:nth-child(3)'
        next_page_url = response.css(next_page_css).attrib['href']
        yield response.follow(url=next_page_url,
                              headers=self.headers,
                              callback=self.parse)

    @staticmethod
    def get_item_data(response: HtmlResponse):
        data = response.json()['data']
        yield RozetkaCategoriesItem(
            item_id=data['id'],
            title=data['title'],
            old_price=float(data['old_price']),
            current_price=float(data['price']),
            href=data['href'],
            brand=data['brand'],
            category=data['last_category']['title'],
        )
