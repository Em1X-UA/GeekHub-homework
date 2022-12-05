"""
2. Написати програму, яка має складатися з трьох файлів/модулів.
- rozetka_api.py, де створти клас RozetkaAPI, який буде містити 1 метод
get_item_data, який на вхід отримує id товара з сайту розетки та повертає
словник з такими даними: item_id (він же і приймається на вхід), title,
old_price, current_price, href (лінка на цей товар на сайті), brand, category.
Всі інші методи, що потрібні для роботи мають бути приватні/захищені.

- data_operations.py з класами CsvOperations та DataBaseOperations.
CsvOperations містить метод для читання даних.
Метод для читання приймає аргументом шлях до csv файлу де в колонкі
ID записані як валідні, так і не валідні id товарів з сайту.
DataBaseOperations містить метод для запису даних в sqlite3 базу і відповідно
приймає дані для запису. Всі інші методи, що потрібні для роботи мають бути
приватні/захищені.

- task.py - головний модуль, який ініціалізує і запускає весь процес.
Суть процесу: читаємо ID товарів з csv файлу, отримуємо необхідні дані і
записуємо їх в базу. Якщо ID не валідний/немає даних - вивести відповідне
повідомлення і перейти до наступного.

Уточнення по другому завданню (бо не всі зрозуміли): воно має бути зроблене
лише за допомогою requests без використання BeautifulSoup по аналогії,
як було показано на лекції на прикладі сайту "Сільпо".
"""


from time import sleep
from random import randint

from modules.rozetka_api import RozetkaAPI
from modules.data_operations import CsvOperations, DataBaseOperations


def main():
    id_list = CsvOperations.read_csv('id_list.csv')
    db = DataBaseOperations()
    rztk = RozetkaAPI()

    for ind, item_id in enumerate(id_list):
        print(f'Getting {ind + 1} item data from id: {item_id}')
        if ind != 0:
            sleep(randint(3, 7))

        item = rztk.get_item_data(item_id)
        if not item:
            print(f'Id {item_id} is incorrect!')
            continue

        db.write_to_db(item)

    print('Parsing finished!')


if __name__ == '__main__':
    main()
