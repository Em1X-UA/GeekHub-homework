""" 3. Програма-банкомат.
   Використовуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та
        історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених
        даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу
        (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка
        додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете
        реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
        Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
        (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Подивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання
        має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій """


import os
import csv
import json
from datetime import datetime
from time import sleep
from random import choice


users_data = 'users.csv'
input_attempts = 3


class NameLenException(Exception):
    pass


class PasswordLenException(Exception):
    pass


class PasswordSecurityException(Exception):
    pass


class PasswordStrongSecurityException(Exception):
    pass


class LoginFailedException(Exception):
    pass


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def try_again_or_start(func):
    """Function mostly for input error cases before login"""
    print('1. Try again')
    print('2. Back to start')
    attempts = input_attempts
    for _ in range(input_attempts):
        user_choice = input('Enter your choice: ')
        if user_choice == '1':
            clear()
            return func()
        elif user_choice == '2':
            clear()
            return start()
        else:
            attempts -= 1
            print(f'Wrong input!!! Try again. {attempts} left')
    print('All attempts failed. Backing to start')
    sleep(3)
    clear()
    start()


def register():
    """Obviously this function can add new users"""

    def check_name_password(name, password):
        """Checking name length and password security for new users"""

        name_status = f'Name "{name}" status is: '
        password_status = 'Password status: '

        try:
            if not 4 <= len(name) <= 50:
                raise NameLenException('Name length must be >= 4 and <= 50')
            if len(password) < 8:
                raise PasswordLenException('Password should be >= 8 symbols')
            if not [x for x in password if x.isdigit()]:
                raise PasswordSecurityException('Password must have at list one digit')
            if ('.' not in password) and ('_' not in password):
                raise PasswordStrongSecurityException('Password must have "_" or "." symbol')
        except NameLenException as err:
            name_status += str(err)
            password_status += 'Please fix NAME first!'
        except PasswordLenException as err:
            password_status += str(err)
        except PasswordSecurityException as err:
            password_status += str(err)
        except PasswordStrongSecurityException as err:
            password_status += str(err)
        else:
            name_status += 'OK'
            password_status += 'OK'
            return {name: password}
        finally:
            clear()
            print(name_status)
            print(password_status)
            sleep(5)
            clear()
        try_again_or_start(register)

    def confirm_password(some_password):
        attempts_left = input_attempts
        for _ in range(input_attempts):
            input_confirm = input('Please confirm your password: ')
            if some_password == input_confirm:
                print('Password confirmed')
                return True
            attempts_left -= 1
            print(f'Incorrect password. {attempts_left} attempts left.')
        print('Error. But you can try register again.')
        try_again_or_start(register)

    check_file(users_data)
    with open(users_data, 'r', newline='') as file:
        user_login = input('Enter your login to register: ')
        read = csv.DictReader(file, fieldnames=['Login', 'Password'])
        for row in read:
            if row['Login'] == user_login:
                print(f'User with name "{user_login}" already exists.')
                print('Try to register again?')
                try_again_or_start(register)

    user_password = input('Enter your password (password must have >= 8 symbols, '
                          'at least 1 digit, and "_" or "." symbol): ')
    check_name_password(user_login, user_password)
    confirm_password(user_password)

    with open(users_data, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Login', 'Password'])
        writer.writerows([{'Login': user_login, 'Password': user_password}])

    with open(fr'users_info\{user_login}_balance.txt', 'w') as balance_file:
        balance_file.write('0')

    with open(fr'users_info\{user_login}_transactions.json', 'w') as trans_file:
        data = {str(datetime.now()): [{"Operation": 'Registration'}, {"Balance change": 0}]}
        json.dump(data, trans_file, indent=2)

    clear()
    print(f'Congratulations, {user_login}! Welcome to our bank!')
    sleep(3)
    clear()
    start()


def login_user():
    clear()
    print('Please log in system')
    attempts_left = input_attempts
    for _ in range(input_attempts):
        input_login = input('1. Login: ')
        input_password = input('2. Password: ')
        with open(users_data, 'r', newline='') as file:
            reader = csv.DictReader(file, fieldnames=['Login', 'Password'])
            for row in reader:
                if row['Login'] == input_login and row['Password'] == input_password:
                    clear()
                    print(f'Welcome, {input_login}!')
                    sleep(2)
                    clear()
                    return input_login
        attempts_left -= 1
        print(f'Incorrect login or password. {attempts_left} attempts left.')
    raise LoginFailedException('Error. All attempts failed. Please contact the bank!')


def check_file(file):
    """Check file exists, and possibility to create, if not."""
    clear()
    if not os.path.exists(file):
        print(f'Error! File {file} doesn\'t exists!')
        print('We recommend contacting the bank to resolve this '
              'misunderstanding. \nIf you have an urgent need, we \n'
              'can create a new empty file, \nuntil the problem with '
              'the support service is resolved.')
        print(f'1. Create empty file "{file}"')
        print('2. Back to start')
        user_choice = input('Enter your choice: ')
        if user_choice == '1':
            match file[-4::]:
                case '.csv':
                    with open(file, 'w') as new_file:
                        writer = csv.DictWriter(new_file, fieldnames=['Login', 'Password'])
                        writer.writeheader()
                        clear()
                        start()
                case 'json':
                    with open(file, 'w') as trans_file:
                        data = {str(datetime.now()): [{"Operation": 'Registration'}, {"Balance change": 0}]}
                        json.dump(data, trans_file, indent=2)
                case '.txt':
                    with open(file, 'w') as balance_file:
                        balance_file.write('0')
                case _:
                    print('Unknown Error! Restart program')
                    sleep(5)
                    start()
        elif user_choice == '2':
            return start()
        else:
            print('Wrong input!!! Try again.')
            return check_file(file)


def greetings():
    print('Dear user!')
    print('Hello! I\'m console ATM program')
    print('Please use only digits for navigation in menu\n')

    first_input = input('Press ENTER to proceed, or type '
                        '"register" if you\'re new user: ')
    if first_input.lower() == 'register':
        register()


def try_again_user(func, user):
    """Function mostly for input error cases after login"""
    print('1. Try again')
    print('2. Back to main menu')
    print('0. Exit')
    attempts = input_attempts
    for _ in range(input_attempts):
        user_choice = input('Enter your choice: ')
        if user_choice == '1':
            clear()
            return func(user)
        elif user_choice == '2':
            clear()
            user_menu(user)
        elif user_choice == '0':
            clear()
            return start()
        else:
            attempts -= 1
            print(f'Wrong input!!! Try again. {attempts} left')
    print('All attempts failed. Exit.')
    sleep(3)
    clear()
    start()


def check_balance(user):
    clear()
    with open(fr'users_info\{user}_balance.txt') as bal_file:
        balance = bal_file.read()
    balance = round(determine_value(balance), 2)
    print(f'You have {balance} UAH')
    input('Press ENTER to back main menu')
    return user_menu(user)


def logger(user, operation, balance):
    data = {str(datetime.now()): [{"Operation": operation}, {"Balance change": balance}]}
    with open(fr"users_info\{user}_transactions.json", "r+") as file:
        file_data = json.load(file)
        file_data.update(data)

    with open(fr"users_info\{user}_transactions.json", "w") as file:
        json.dump(file_data, file, indent=2)


def check_logs(user):
    clear()
    with open(fr'users_info\{user}_transactions.json', 'r') as file:
        transactions = json.load(file)
        for date, op_bal_list in transactions.items():
            print(date)
            for el in op_bal_list:
                for key, value in el.items():
                    print(f'{key}: {value}')
            print('=======================')
    input('Press ENTER to back main menu')
    clear()
    user_menu(user)


def determine_value(num):
    num = float(num)
    return num if num % 1 != 0 else int(num)


def withdraw_money(user):
    with open(fr'users_info\{user}_balance.txt') as bal_file:
        balance = bal_file.read()

    min_banknote = choice([50, 100, 200])
    clear()

    attempts = input_attempts
    for _ in range(input_attempts):
        print('Enter the amount, you want to withdraw! (or 0 to back main menu)')
        user_input = input(f'The amount must be a multiple '
                           f'of {min_banknote}!\nEnter: ')

        try:
            user_input = int(user_input)
            balance = determine_value(balance)
            if user_input > balance or user_input % min_banknote != 0:
                raise ValueError
            else:
                balance -= user_input

                with open(fr'users_info\{user}_balance.txt', 'w') as bal_file:
                    bal_file.write(str(balance))
                logger(user, 'withdraw', f'-{user_input}')

                print(f'{user_input} UAH successfully withdrawn')
                input('Press ENTER to back main menu')
                clear()
                user_menu(user)
        except ValueError:
            attempts -= 1
            print(f'Incorrect amount entered. Try again! {attempts} attempts left.')
            sleep(2)
            clear()
            continue
    try_again_user(withdraw_money, user)


def top_up_balance(user):
    with open(fr'users_info\{user}_balance.txt') as bal_file:
        balance = bal_file.read()
    min_banknote = choice([5, 10, 20])
    clear()
    attempts = input_attempts
    for _ in range(input_attempts):
        print('Enter the amount by which you want to top up your account.')
        user_input = input(f'The minimum banknote for top-up is {min_banknote}!'
                           f'\nEnter: ')
        try:
            user_input = int(user_input)
            balance = determine_value(balance)
            if user_input % min_banknote != 0:
                raise ValueError
            else:
                balance += user_input

                with open(fr'users_info\{user}_balance.txt', 'w') as bal_file:
                    bal_file.write(str(balance))
                logger(user, 'Top up', f'+{user_input}')

                print(f'Your account has been topped up by {user_input} UAH.')
                input('Press ENTER to back main menu')
                clear()
                user_menu(user)
        except ValueError:
            attempts -= 1
            print(f'Incorrect amount entered. Try again! {attempts} attempts left.')
            sleep(2)
            clear()
            continue
    try_again_user(top_up_balance, user)


def user_menu(user):
    """Main menu"""
    print('What do you want to do?')
    print('1. Check balance')
    print('2. Withdraw money')
    print('3. Top up the balance')
    print('4. Transactions history')
    print('0. Exit')

    attempts = input_attempts
    for _ in range(input_attempts):
        user_choice = input('Enter your choice: ')
        match user_choice:
            case '1':
                return check_balance(user)
            case '2':
                return withdraw_money(user)
            case '3':
                return top_up_balance(user)
            case '4':
                return check_logs(user)
            case '0':
                print(f'Goodbye {user}!')
                sleep(3)
                clear()
                start()
            case _:
                print(f'Wrong input! Try again! {attempts} attempts left.')
                sleep(3)
                try_again_user(user_menu, user)


def start():
    clear()
    greetings()
    check_file(users_data)
    current_user = login_user()
    check_file(fr'users_info\{current_user}_balance.txt')
    check_file(fr'users_info\{current_user}_transactions.json')
    user_menu(current_user)


if __name__ == '__main__':
    start()
