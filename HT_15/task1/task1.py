"""
1. Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт
"https://www.expireddomains.net/domain-lists/"
(з ним будьте обережні :подмигивание::череп_и_кости:),
вибираєте будь-яку на ваш вибір доменну зону і парсите список доменів
з усіма відповідними колонками - доменів там буде десятки тисяч
(звичайно ураховуючи пагінацію).
Всі отримані значення зберегти в CSV файл.
"""


import re
import csv
from time import sleep
from random import choice
from urllib.parse import urljoin
from datetime import datetime, timedelta
from dataclasses import dataclass, fields, astuple

import requests
from bs4 import BeautifulSoup as Bs


@dataclass()
class Domain:
    domain: str  # Domain Name
    bl: int  # ?? link? | Majestic External Backlinks, Click on
    # the Number for Related Links
    domain_pop: int  # SEOkicks Domain Pop - Number of Backlinks
    # from different Domains
    a_birth: datetime.date  # The Birth Year of the Domain using the first
    # found Date from archive.org
    a_entries: int  # Archive.org Number of Crawl Results
    dmoz: str  # Status of the Domain in Dmoz.org
    status_com: str  # DNS Status .com of Domain Name
    status_net: str  # DNS Status .net of Domain Name
    status_org: str  # DNS Status .org of Domain Name
    status_de: str  # DNS Status .de of Domain Name
    status_tld_registered: int  # Number of TLDs the Domain Name is Registered
    related_cnobi: int  # Numberof Related Domains in .com/.net/.org/.biz/.info
    # (starts with + ends with)
    traffic: int  # Traffic supplied by the Provider (GoDaddy, Dynadot, Sedo...)
    valuation: int  # The GoDaddy Valuation Tool takes the Afternic sales
    # database into account and predicts the retail value based
    # on a proprietary algorithm.
    price: int  # Price information
    bids: int  # Number of Bids
    end_time: str  # Auction End Time


class ExpiredDomainsParser:
    BASE_URL = 'https://www.expireddomains.net/'
    URL = urljoin(BASE_URL, 'godaddy-traffic-domains/')
    PAGES_TO_PARSE = 10
    DOMAIN_FIELDS = [field.name for field in fields(Domain)]
    DOMAIN_CSV_FILE = 'domain.csv'
    session = requests.Session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;'
                         'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                         'application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'uk,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
               'Cache-Control': 'max-age=0',
               'Referer': URL,
               'sec-ch-ua': '"Chromium";v="106", "Not.A/Brand";v="24", "Opera GX";v="92"',
               'sec-ch-ua-mobile': '?0',
               'sec-ch-ua-platform': '"Windows"',
               'sec-fetch-dest': 'document',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests': '1',
               'accept - encoding': 'gzip, deflate, br',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0',
               }
    local_first_page = 'data/index0312.html'

    def get_result(self):
        """
        Returned all parsed domains list as objects.
        """
        first_page_url = self.URL + '?#listing'
        print('Getting data from 1 page.')
        domains_list = self.parse_single_page(first_page_url)

        if self.PAGES_TO_PARSE < 2:
            return domains_list

        for page_num in range(2, self.PAGES_TO_PARSE + 1):
            sleep(choice(list(range(7, 15))))
            print(f'Getting data from {page_num} page.')
            page_url_part = f'?start={page_num * 25}#listing'
            domains_list.extend(self.parse_single_page(
                urljoin(self.URL, page_url_part)))
        print('Finished')
        return domains_list

    def parse_single_page(self, url) -> list:
        """
        Getting page from url request, parsed it and returned Domains list.,
        """

        # Used to practice parsing without everytime requests.
        # with open(self.local_first_page, 'r') as file:
        #     page = file.read()

        domains = []
        page = self.session.get(url, headers=self.headers).content
        # data = Bs(page, 'lxml')
        data = Bs(page, 'html.parser')

        for element in data.select_one('tbody').find_all('tr'):
            domains.append(self.parse_single_domain(element))
        return domains

    def write_result_to_csv(self, domains: [Domain]):
        """
        Writing Domains to CSV result file.
        """
        with open(self.DOMAIN_CSV_FILE, 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.DOMAIN_FIELDS)
            writer.writerows([astuple(domain) for domain in domains])

    def get_first_page(self):
        """
        Saving first page to practice parsing without everytime requests.
        """
        with open(self.local_first_page, 'w') as file:
            res = self.session.get(self.URL).text
            file.write(res)

    def parse_single_domain(self, dom: Bs) -> Domain:
        """
        Parsing single domain and returning Domain class object.
        """
        return Domain(
            domain=dom.select_one('.field_domain').text,
            bl=int(dom.select_one('.field_bl').select_one('a')['title'][0]),
            domain_pop=int(dom.select_one('.field_domainpop').text),
            a_birth=self.pars_birth_date(dom.select_one('.field_abirth')),
            a_entries=int(dom.select_one('.field_aentries').text),
            dmoz=dom.select_one('.field_dmoz').text,
            status_com=dom.select_one('.field_statuscom').text,
            status_net=dom.select_one('.field_statusnet').text,
            status_org=dom.select_one('.field_statusorg').text,
            status_de=dom.select_one('.field_statusde').text,
            status_tld_registered=int(dom.select_one(
                '.field_statustld_registered').text),
            related_cnobi=int(self.get_related_cnobi(
                dom.select_one('.field_related_cnobi'))),
            traffic=int(re.sub('[^0-9]', '', dom.select_one(
                '.field_traffic').select_one('a')['title'])),
            valuation=int(re.sub('[^0-9]', '', dom.select_one(
                '.field_valuation').text)),
            price=int(re.sub('[^0-9]', '', dom.select_one('.field_price').text)),
            bids=int(dom.select_one('.field_bids').text),
            end_time=self.parse_end_time(dom.select_one('.field_endtime').text)
        )

    @staticmethod
    def pars_birth_date(a_birth_date: Bs):
        """
        Parse date and return it.
        """
        try:
            date_string = a_birth_date.select_one('a')['title']
            parsed_date = re.search('\d{4}-\d{2}-\d{2}', date_string)[0]
            return datetime.strptime(parsed_date, '%Y-%m-%d').date()
        except TypeError:
            return '-'

    @staticmethod
    def get_related_cnobi(bs_object: Bs):
        """
        Parse related_cnobi and return as int value.
        """
        try:
            return int(bs_object.text)
        except ValueError:
            return int(f"{re.sub('[^0-9]', '', bs_object.text)}00")

    @staticmethod
    def parse_end_time(end_time_string: str):
        """
        Parse end_time string and return datetime object with auction end-time
        """
        h, m, s = 0, 0, 0
        for el in end_time_string.split():
            if 'h' in el:
                h = int(el[:-1])
            elif 'm' in el:
                m = int(el[:-1])
            elif 's' in el:
                s = int(el[:-1])
        delta = timedelta(hours=h, minutes=m, seconds=s)
        return (datetime.now() + delta).isoformat(sep=' ', timespec='seconds')


def main():
    dom = ExpiredDomainsParser()

    # # dom.get_first_page()
    # a = dom.parse_single_page('')
    # for el in a:
    #     print(el)
    # dom.write_result_to_csv(a)

    domains = dom.get_result()
    dom.write_result_to_csv(domains)


if __name__ == '__main__':
    main()
