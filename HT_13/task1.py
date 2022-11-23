"""
1. Створіть клас Car, який буде мати властивість year (рік випуску).
Додайте всі необхідні методи до класу, щоб можна було виконувати
порівняння car1 > car2, яке буде показувати, що car1 старша за car2.
Також, операція car1 - car2 повинна повернути різницю між роками випуску.
"""

from functools import total_ordering


class Car:
    def __init__(self, year):
        self.year = year

    @total_ordering
    def __ge__(self, other):
        return self.year <= other.year

    @total_ordering
    def __gt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __sub__(self, other):
        return self.year - other.year
        # return abs(self.year - other.year)


def main():
    car1 = Car(1995)
    car2 = Car(2020)

    print(car1 > car2)  # --> True (car1 is older)
    print(car1 - car2)  # --> -25


if __name__ == '__main__':
    main()
