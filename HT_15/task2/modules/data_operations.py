"""
- data_operations.py з класами CsvOperations та DataBaseOperations.
CsvOperations містить метод для читання даних.
Метод для читання приймає аргументом шлях до csv файлу де в колонкі
ID записані як валідні, так і не валідні id товарів з сайту.
DataBaseOperations містить метод для запису даних в sqlite3 базу і відповідно
приймає дані для запису. Всі інші методи, що потрібні для роботи мають бути
приватні/захищені.
"""


import csv
import sqlite3


class CsvOperations:
    @staticmethod
    def read_csv(filename):
        """
        Return id_list from CSV file in ID column.
        """
        with open(filename, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [int(row['id']) for row in reader]


class DataBaseOperations:
    DB_FILE = 'database.db'

    def write_to_db(self, data: dict):
        """
        Creates table and appends parsed items.
        """
        with sqlite3.connect(self.DB_FILE) as db:
            cursor = db.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS items_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT, item_id VARCHAR, 
                title VARCHAR, old_price VARCHAR, current_price VARCHAR,
                href VARCHAR, brand VARCHAR, category VARCHAR)""")

            new_item = [v for _, v in data.items()]
            cursor.execute("INSERT INTO items_data(item_id, title, old_price, "
                           "current_price, href, brand, category) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?)", new_item)
