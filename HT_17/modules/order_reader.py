from csv import DictReader
from os import remove

import requests


class OrderReader:
    temp_file_name = 'orders.csv'
    orders_list = []

    def __init__(self, csv_url: str):
        self.csv_url = csv_url

    def get_orders(self):
        self.download_file()
        self.read_file()
        remove(self.temp_file_name)
        return self.orders_list

    def download_file(self):
        response = requests.get(self.csv_url).content
        with open(self.temp_file_name, 'wb') as file:
            file.write(response)

    def read_file(self):
        with open(self.temp_file_name) as file:
            orders = DictReader(file)
            for row in orders:
                self.orders_list.append(row)
