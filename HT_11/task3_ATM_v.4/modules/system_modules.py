"""File contains often used functions"""


import os
import sqlite3
from time import sleep
from settings import input_attempts, sleep_time, banknotes_list, atm_data


def clear():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def slp():
    sleep(sleep_time)


def get_user_input():
    """determine int or float value"""

    attempts = input_attempts
    while attempts > 0:
        user_value = input('Enter your value: ')
        attempts -= 1
        try:
            user_value = float(user_value)
            if user_value < 0:
                print('You can\'t use values less then 0!')
                print(f'\n{attempts} attempts left!')
                continue
        except ValueError:
            print(f'"{user_value}" is not a number! '
                  f'\n{attempts} attempts left!')
            slp()
            continue
        else:
            clear()
            return user_value if user_value % 1 != 0 else int(user_value)
    print('All attempts failed! Chosen "0".')
    slp()
    clear()
    return 0


def get_user_choice(menu_range: int):
    """ Get input from user and check it for menu variants range.
    '0' is expected for exit"""

    attempts = input_attempts
    while attempts > 0:
        user_choice = input('Enter your choice: ')
        attempts -= 1

        try:
            user_choice = int(user_choice)
        except ValueError:
            print(f'"{user_choice}" is not integer number! '
                  f'\n{attempts} attempts left!')
            slp()
            continue
        else:
            if 0 <= user_choice <= menu_range:
                clear()
                return user_choice
            else:
                print(f'Input error. {attempts} attempts left!\n '
                      f'Try digit >= 0 and <= {menu_range}')
                continue
    print('All attempts failed! Chosen "0" option')
    slp()
    clear()
    return 0


def check_file(file):
    """Check file exists, and possibility to create, if not."""

    from main import start

    clear()
    if not os.path.exists(file):
        print('Error! Database file  doesn\'t exists!')
        print('1. Create empty database file')
        print('0. Back to start')

        user_choice = get_user_choice(1)
        if user_choice == 1:
            with sqlite3.connect(atm_data) as db:
                cursor = db.cursor()

                cursor.execute("""CREATE TABLE IF NOT EXISTS users_data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    user VARCHAR, 
                    password VARCHAR, 
                    balance VARCHAR,
                    is_collector VARCHAR)""")
                new_user = ('admin', 'admin', 0, True)
                cursor.execute("INSERT INTO users_data(user, password, balance, "
                               "is_collector) VALUES (?, ?, ?, ?)", new_user)

                cursor.execute("""CREATE TABLE IF NOT EXISTS transaction_logs(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user VARCHAR, 
                    date VARCHAR,
                    operation VARCHAR,
                    balance_changes VARCHAR,
                    remaining VARCHAR)""")

                cursor.execute("""CREATE TABLE IF NOT EXISTS banknotes_qty(
                    nominal INTEGER, quantity INTEGER)""")
                for banknote in banknotes_list:
                    cursor.execute("INSERT INTO banknotes_qty(nominal, quantity)"
                                   " VALUES (?, ?)", (banknote, 0))
        elif user_choice == 0:
            return start()


def determine_value(num):
    num = float(num)
    return num if num % 1 != 0 else int(num)
