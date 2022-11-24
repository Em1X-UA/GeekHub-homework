"""
   3. Реалізуйте класс Transaction.
   Його конструктор повинен приймати такі параметри:
- amount - суму на яку було здійснено транзакцію
- date - дату переказу
- currency - валюту в якій було зроблено переказ (за замовчуванням USD)
- usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
- description - опис транзакції (за дефолтом None)
Усі параметри повинні бути записані в захищені (_attr) однойменні атрибути.
Доступ до них повинен бути забезпечений лише на читання та за допомогою
механізму property. При чому якщо description дорівнює None,
то відповідне property має повертати рядок "No description provided".
Додатково реалізуйте властивість usd, що має повертати суму переказу у доларах
(сума * курс)
"""

from datetime import date as dt


class Transaction:
    def __init__(self, amount, date, currency='USD',
                 usd_conversion_rate=1.0, description=None):
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = 1 / usd_conversion_rate
        self._description = description

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def usd_conversion_rate(self):
        return self._usd_conversion_rate

    @property
    def description(self):
        if self._description is None:
            self._description = 'No description provided'
        return self._description

    @property
    def usd(self):  # only returned value, not creates parameter
        if self.currency.lower() == 'usd':
            return self.amount
        return self.amount * self._usd_conversion_rate


def main():
    trans1 = Transaction(1000, dt.today(), description='Some description')
    trans1_acts = [trans1.amount, trans1.date, trans1.currency,
                   trans1.usd_conversion_rate, trans1.description, trans1.usd]
    for el in trans1_acts:
        print(el)

    print('=================')

    trans2 = Transaction(10000, dt.today(), 'UAH', 37.5)
    trans2_acts = [trans2.amount, trans2.date, trans2.currency,
                   trans2.usd_conversion_rate, trans2.description, trans2.usd]
    for el in trans2_acts:
        print(el)

    print('=================')
    print(trans1.__dict__)
    print(trans2.__dict__)


if __name__ == '__main__':
    main()
