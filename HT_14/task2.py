"""
2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату
(це може бути як один день так і інтервал - початкова і кінцева дати,
продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати
    (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
"""


from datetime import datetime, timedelta
from time import sleep
import os
import requests


class ExchangeRatesArchive:
    def work(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Hello! Here you can check currency rates archive to UAH.')

        dates_list = self.get_date_from_input()
        rate_list = self.create_rates_list(dates_list)
        self.print_rates(rate_list)

        user_inp = input('\nPress any key and (or just) "Enter" to exit, '
                         'or "yes"/"y" to use program again: ')
        if user_inp in ["yes", "y"]:
            self.work()
        exit()

    @staticmethod
    def get_rates_by_date(date: datetime) -> dict:
        """
        Get json file for rates by input date from API
        API: https://api.privatbank.ua/#p24/exchangeArchive
        """

        url = 'https://api.privatbank.ua/p24api/exchange_rates'
        return requests.get(url, {'date': date.strftime('%d.%m.%Y')}).json()

    def get_date_from_input(self) -> list:
        """
        Get dates from user, convert and return it as datetime objects.
        If fail all attempts - returned current date.
        """

        def wrong_input():
            """
            Input error notification
            """

            print(f'Wrong input! {input_attempts} attempts left.')
            sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

        input_attempts = 3
        while input_attempts > 0:
            if input_attempts < 3:
                print(f'{input_attempts} attempts left.')
            input_attempts -= 1

            print('Date should be in format "dd.mm.yyyy" or "yyyy.mm.dd" '
                  'and separate by a space, if you want check range\n'
                  'As separator in date you can use ".", "/" or "-"\n')

            user_input = input('Enter dates you want to check:')
            if user_input == '':
                wrong_input()
                continue

            user_input = user_input.replace('/', '.').replace('-', '.')
            user_input = user_input.split()

            if len(user_input) > 2:
                wrong_input()
                continue
            try:
                res_dates = []
                for el in user_input:
                    # Conversion string to datetime object
                    el = el.split('.')
                    if len(el[0]) > len(el[-1]):
                        el[0], el[-1] = el[-1], el[0]
                    res_dates.append(datetime.strptime('.'.join(el), '%d.%m.%Y'))
                res_dates.sort()
                self.check_valid_date(res_dates)
                os.system('cls' if os.name == 'nt' else 'clear')
                return res_dates

            except ValueError:
                wrong_input()
                continue
        print('All attempts failed! Returned today date')
        sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return [datetime.today()]

    @staticmethod
    def check_valid_date(date_list):
        """
        Checking dates list for availability in API.
        """

        api_years = 4
        first_available_in_api = datetime.today() - timedelta(days=api_years * 365)
        for date in date_list:
            if date > datetime.today():
                print('You can\'t watch in tomorrow '
                      '(If you\'re not Klychko, of course.')
                raise ValueError
            elif date < first_available_in_api:
                print(f'Used API saves value in a {api_years} years period.')
                print(f'First available date: {first_available_in_api}')
                raise ValueError

    def create_rates_list(self, dates: list) -> list:
        """
        Create and returned list with dicts, where key is date string,
        value is list with dicts for currencies which you can use in PB.
        """

        print('Receiving information from bank...')
        rates_list = []
        current_date = dates[0]
        while dates[-1] >= current_date:
            data = self.get_rates_by_date(current_date)
            new_el = {data['date']: []}

            rates_list.append(new_el)
            i = rates_list.index(new_el)

            for item in data["exchangeRate"]:
                if "saleRate" not in item.keys():
                    continue
                rates_list[i][data['date']].append({"currency": item["currency"],
                                                    "sale_rate": item["saleRate"],
                                                    "purchase_rate": item["purchaseRate"]})
            current_date += timedelta(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        return rates_list

    @staticmethod
    def print_rates(rate_list: list):
        """
        Printing rates information from input lists of dicts.
        """

        for day in rate_list:
            for date, rates in day.items():
                print(f'Date: {date}')
                print('Currency | Sale rate | Purchase rate')
                for curr in rates:
                    # sleep(0.2)
                    print(f"{curr['currency']} | "
                          f"{curr['sale_rate']} | "
                          f"{curr['purchase_rate']}")
            if day != rate_list[-1]:
                print('--------------------')


def main():
    test = ExchangeRatesArchive()
    test.work()


if __name__ == '__main__':
    main()
