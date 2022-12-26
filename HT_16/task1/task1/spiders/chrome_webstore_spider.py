import scrapy
from scrapy import Request
from bs4 import BeautifulSoup as Bs

from ..items import ExtensionItem


class ChromeWebstoreSpider(scrapy.Spider):
    name = 'chrome_webstore_spider'
    allowed_domains = ['chrome.google.com']
    start_urls = ['https://chrome.google.com/webstore/sitemap']
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) '
                      'Gecko/20100101 Firefox/108.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/avif,image/webp,*/*;q=0.8'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        """Parse URLs from first page"""
        for link in Bs(response.body, 'xml').find_all('loc'):
            yield Request(url=link.text, headers=self.headers, callback=self.parse_links)

    def parse_links(self, response):
        """Parse URLs from first page"""
        for link in Bs(response.body, 'xml').find_all('loc'):
            yield Request(url=link.text, headers=self.headers, callback=self.parse_item)

    @staticmethod
    def parse_item(response):
        """Parse single extension item"""
        page = Bs(response.body, 'lxml')
        yield ExtensionItem(
            id=response.url.split('/')[-1].strip().split('?')[0],
            name=page.select_one('.e-f-w').text.strip(),
            description=page.select_one('.C-b-p-j-Pb').text.strip()
        )
