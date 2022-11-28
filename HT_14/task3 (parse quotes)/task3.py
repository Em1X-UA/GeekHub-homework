"""
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї
доступної інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""


import csv
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup as Bs


@dataclass
class Quote:
    quote: str
    author: str
    author_born_date: str
    author_born_place: str


class QuotesScraper:
    BASE_URL = 'http://quotes.toscrape.com'
    url = urljoin(BASE_URL, 'page/')
    pages_to_parse = 10
    RESULT_CSV = 'quotes.csv'
    QUOTE_FIELDS = [field.name for field in fields(Quote)]

    def get_all_quotes(self) -> [Quote]:
        """
        Get quotes from all pages in list, returned parsed result.
        """

        quotes_list = []
        for page_number in range(1, self.pages_to_parse + 1):
            page = requests.get(urljoin(self.url, str(page_number))).content
            soup = Bs(page, 'lxml')
            # soup = Bs(page, 'html.parser')
            quotes_list.extend(soup.select('.quote'))
        return [self.parse_single_quote(quote) for quote in quotes_list]

    def parse_single_quote(self, product: Bs) -> Quote:
        """
        Creating Quote class example by parsing input Bs object.
        """

        born_date, born_place = self.pars_author((product.select_one('a')['href']))
        return Quote(
            quote=product.select_one('.text').text[1:-1],
            author=product.select_one('.author').text,
            author_born_date=born_date,
            author_born_place=born_place
        )

    def pars_author(self, link):
        """
        Parsing and returns authors date and born place from input link.
        """

        soup = Bs(requests.get(urljoin(self.BASE_URL, link)).content, 'lxml')
        born_date = soup.select_one('.author-born-date').text
        born_place = soup.select_one('.author-born-location').text.replace('in ', '')
        return born_date, born_place

    def write_quotes_to_csv(self, quotes: [Quote]):
        """
        Writing all input Quotes to CSV file.
        """

        with open(self.RESULT_CSV, 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.QUOTE_FIELDS)
            writer.writerows([astuple(quote) for quote in quotes])
            # for quote in quotes:
            #     writer.writerow([v for _, v in quote.__dict__.items()])
            #     # writer.writerow((astuple(quote)))
        return


def main():
    q = QuotesScraper()
    all_quotes = q.get_all_quotes()
    q.write_quotes_to_csv(all_quotes)


if __name__ == '__main__':
    main()
