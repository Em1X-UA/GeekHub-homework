"""
2. Створити клас Matrix, який буде мати наступний функціонал:
2.1. __init__ - вводиться кількість стовпців і кількість рядків
2.2. fill() - заповнить створений масив числами - по порядку.
Наприклад:
+────+────+
| 1  | 2  |
+────+────+
| 3  | 4  |
+────+────+
| 5  | 6  |
+────+────+
3. print_out() - виведе створений масив
(якщо він ще не заповнений даними - вивести нулі)
4. transpose() - перевертає створений масив.
Тобто, якщо взяти попередню таблицю, результат буде
+────+────+────+
| 1  | 3  | 5  |
+────+────+────+
| 2  | 4  | 6  |
+────+────+────+
P.S. Всякі там Пандас/Нампай не використовувати - тільки хардкор ;)
P.P.S. Вивід не обов’язково оформлювати у вигляді таблиці - головне,
щоб було видно, що це окремі стовпці / рядки
"""


class Matrix:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.array = [0 for _ in range(1, (self.columns * self.rows) + 1)]

    def fill(self):
        self.array = list(range(1, (self.columns * self.rows) + 1))

    def print_out(self):
        for i, c in enumerate(self.array):
            if (i + 1) % self.columns == 0:
                print(f'{c}')
            else:
                print(f'{c}|', end='')

    def transpose(self):
        self.columns, self.rows = self.rows, self.columns


def main():
    ex1 = Matrix(2, 3)
    ex1.fill()
    ex1.print_out()

    ex1.transpose()
    ex1.print_out()


if __name__ == '__main__':
    main()
