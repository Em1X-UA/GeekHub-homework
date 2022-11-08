""" Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях.
    Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали
    структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити нового користувача
    (при створенні нового користувача, перевіряється відповідність логіну і паролю
    мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор,
    який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб
    нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість).
    Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу
    що підтримує банкомат. В іншому випадку - повернути "здачу"
    (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість
    купюр банкомату, лише збільшується баланс користувача (моделюємо наявність двох незалежних
    касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною
    (невірний логін/пароль, недостатньо коштів на рахунку,
    неможливо видати суму наявними купюрами тощо.)
    - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій,
    що б ми могли його використати """



""""ЯКЩО ВИ ЦЕ БАЧИТЕ, ТО ЦЕ ЩЕ НЕ ПРАЦЮЄ ПОВНІСТЮ ЯК ТРЕБА. ЗАЙМАЮСЬ ВИПРАВЛЕННЯМ
ПРОХАННЯ ПЕРЕВІРИТИ ПІЗНІШЕ. НАДІСЛАВ ТАК ПОКИ НЕ ЗАКРИЛОСЬ, ЩОБ НЕ ЗАРАХУВАЛИ ЯК ПРОВТИК
ПРОШУ ВИБАЧЕННЯ ЗА ЗАТРИМКУ"""



import os
import sqlite3
from datetime import datetime
from time import sleep
from random import choice


atm_data = 'atm_database.db'
input_attempts = 3
banknotes_list = [10, 20, 50, 100, 200, 500, 1000]


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
            if not 8 <= len(password) <= 50:
                raise PasswordLenException('Password should be >= 8 and <= 50 symbols')
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
            sleep(1)
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

    check_file(atm_data)

    user_login = input('Enter your login to register: ')
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        cursor.execute("SELECT user FROM users_data WHERE user = ?", [user_login])
        if cursor.fetchone() is not None:
            print(f'User with name "{user_login}" already exists.')
            print('Try to register again?')
            try_again_or_start(register)

    user_password = input('Enter your password (password must have >= 8 and <= 50 symbols, '
                          'at least 1 digit, and "_" or "." symbol): ')
    check_name_password(user_login, user_password)
    confirm_password(user_password)

    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users_data(user, password, balance, "
                       "is_collector) VALUES (?, ?, ?, ?)",
                       (user_login, user_password, 0, False))
    clear()
    print(f'Congratulations, {user_login}! Welcome to our bank!')
    sleep(2)
    clear()
    user_menu(user_login)


def login_user():
    clear()
    print('Please log in system')
    attempts_left = input_attempts
    for _ in range(input_attempts):
        input_login = input('1. Login: ')
        input_password = input('2. Password: ')

        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()

            cursor.execute("SELECT user FROM users_data WHERE user = ?", [input_login])
            if cursor.fetchone() is None:
                attempts_left -= 1
                print(f'Incorrect login. {attempts_left} attempts left.')
            else:
                cursor.execute("SELECT password FROM users_data "
                               "WHERE user = ? AND password = ?",
                               [input_login, input_password])
                if cursor.fetchone() is None:
                    attempts_left -= 1
                    print(f'Incorrect password. {attempts_left} attempts left.')
                else:
                    clear()
                    print(f'Welcome, {input_login}!')
                    sleep(2)
                    clear()

                    collector_status = cursor.execute("SELECT is_collector "
                                                      "FROM main.users_data "
                                                      "WHERE user = ?", [input_login])
                    if collector_status:
                        return admin_menu(input_login)
                    else:
                        return input_login
    raise LoginFailedException('Error. All attempts failed. Please contact the bank!')


def check_file(file):
    """Check file exists, and possibility to create, if not."""
    clear()
    if not os.path.exists(file):
        print('Error! Database file  doesn\'t exists!')
        print('1. Create empty database file')
        print('2. Back to start')

        user_choice = input('Enter your choice: ')
        if user_choice == '1':
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
                    balance_changes VARCHAR)""")

                cursor.execute("""CREATE TABLE IF NOT EXISTS banknotes_qty(
                    nominal INTEGER, quantity INTEGER)""")
                for banknote in banknotes_list:
                    cursor.execute("INSERT INTO banknotes_qty(nominal, quantity)"
                                   " VALUES (?, ?)", (banknote, 0))

        elif user_choice == '2':
            return start()
        else:
            print('Wrong input!!! Try again.')
            return check_file(file)


def greetings():
    print('Dear user!')
    print('Hello! I\'m console ATM program')
    print('Please use only digits for navigation in menu\n')

    first_input = input('Press any key and (or just) ENTER to proceed, or type'
                        ' "register" (and press ENTER) if you\'re new user: ')
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
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        balance = cursor.execute("SELECT balance FROM users_data "
                                 "WHERE user = ?", [user]).fetchone()[0]
    print(f'You have {balance} UAH')
    input('Press any key and (or just) ENTER to back main menu')
    return user_menu(user)


def logger(user, operation, balance):
    data = (user, str(datetime.now()), operation, balance)
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO transaction_logs(""user, date, operation, "
                       "balance_changes"") VALUES (?, ?, ?, ?)", data)


def check_logs(user):
    clear()
    print(f'---{user} transactions history---')
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        for id_op, user_log, date, operation, balance_changes in \
                cursor.execute("SELECT * FROM transaction_logs"):
            if user == user_log:
                print(f'ID: {id_op}')
                print(f'Date: {date}')
                print(f'Operation: {operation}')
                print(f'Balance change: {balance_changes}')
                print('=======================')
        collector_status = cursor.execute("SELECT is_collector "
                                          "FROM users_data "
                                          "WHERE user = ?", [user])
    input('Press any key and (or just) ENTER to back main menu')
    clear()

    if collector_status:
        return admin_menu(user)
    else:
        user_menu(user)


def determine_value(num):
    num = float(num)
    return num if num % 1 != 0 else int(num)


def atm_balance():
    atm_cash = 0
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        for nominal, q_ty in cursor.execute("SELECT * FROM banknotes_qty"):
            atm_cash += nominal * q_ty
    return atm_cash


def withdraw_money(user):
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        balance = cursor.execute("SELECT balance FROM users_data "
                                 "WHERE user = ?", [user]).fetchone()[0]

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
            if user_input > balance:
                print('You don\'t gave enough money!')
                raise ValueError
            elif user_input % min_banknote != 0:
                print('Impossible to withdraw funds with existing banknotes: ')
                raise ValueError
            elif user_input > atm_balance():
                print('Sum is too much! ATM doesn\'t have enough money!')
                raise ValueError
            elif user_input <= 0:
                print('You can\'t withdraw negative (or zero) amount!')
                raise ValueError
            else:
                with sqlite3.connect(atm_data) as db:
                    cursor = db.cursor()
                    cursor.execute("UPDATE users_data SET balance = balance - ? "
                                   "WHERE user = ?", [user_input, user])

                logger(user, 'withdraw', f'-{user_input}')

                print(f'{user_input} UAH successfully withdrawn')
                input('Press any key and (or just) ENTER to back main menu')
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
    min_banknote = choice([5, 10, 20])
    clear()
    attempts = input_attempts
    for _ in range(input_attempts):
        print('Enter the amount by which you want to top up your account.')
        user_input = input(f'The minimum banknote for top-up is {min_banknote}!'
                           f'\nEnter: ')
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print('You can\'t add negative (or zero) amount to your balance!')
                raise ValueError
            else:
                if user_input % min_banknote != 0:
                    print(f'ATM accepts banknotes with a minimum denomination of {min_banknote}')
                    print(f'Take your {user_input % min_banknote} UAH back!')
                    user_input -= user_input % min_banknote
                with sqlite3.connect(atm_data) as db:
                    cursor = db.cursor()
                    cursor.execute("UPDATE users_data SET balance = balance + ? "
                                   "WHERE user = ?", [user_input, user])
                logger(user, 'Top up', f'+{user_input}')

                print(f'Your account has been topped up by {user_input} UAH.')
                input('Press any key and (or just) ENTER to back main menu')
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
                attempts -= 1
                print(f'Wrong input! Try again! {attempts} attempts left.')
                sleep(1)
                try_again_user(user_menu, user)


def check_banknotes(user):
    clear()
    print('Nominal | Quantity')
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        for nominal, q_ty in cursor.execute("SELECT * FROM banknotes_qty"):
            print(f'{nominal} UAH: {q_ty} pcs')
    input('Press any key and (or just) ENTER to back main menu')
    clear()
    admin_menu(user)


def check_atm_balance(user):
    clear()
    print(f'ATM has {atm_balance()} UAH')
    input('Press any key and (or just) ENTER to back main menu')
    clear()
    admin_menu(user)


def change_banknotes_balance_menu(user):
    def change_banknotes_qty(nominal_1, qty):
        with sqlite3.connect(atm_data) as db_1:
            cursor1 = db_1.cursor()
            cursor1.execute("UPDATE banknotes_qty SET quantity = ?"
                            "WHERE nominal = ?", [qty, nominal_1])
        print('ATM banknotes balance changed!')
        input('Press any key and (or just) ENTER to back main menu')
        clear()
        admin_menu(user)

    clear()
    print('Choose banknote nominal to change quantity')
    counter = 1
    nominals = banknotes_list
    # with sqlite3.connect(atm_data) as db:
    #     cursor = db.cursor()
    #     for nominal, _ in cursor.execute("SELECT * FROM banknotes_qty"):
    #         print(f'{counter}. UAH {nominal}')
    #         nominals.append(nominal)
    #         counter += 1
    for banknote in banknotes_list:
        print(f'{counter}. UAH {banknote}')
        counter += 1

    print('\n0. Back to main menu')
    attempt = input_attempts
    for _ in range(input_attempts):
        user_choice_1 = input('Enter your choice: ')
        user_choice_1 = determine_value(user_choice_1)
        if user_choice_1 in range(len(nominals)):
            attmp = input_attempts
            for _ in range(input_attempts):
                user_choice_2 = input(f'Enter {nominals[user_choice_1 - 1]} banknotes qty to set: ')
                user_choice_2 = determine_value(user_choice_2)
                if user_choice_2 < 0:
                    print('You can\'t set quantity less then zero!')
                    attmp -= 1
                    print(f'Try again! {attmp} attempts left.')
                    sleep(1)
                    continue
                else:
                    change_banknotes_qty(nominals[user_choice_1 - 1], user_choice_2)
        else:
            attempt -= 1
            print(f'Wrong input! Try again! {attempt} attempts left.')
            sleep(1)
    try_again_user(change_banknotes_balance_menu, user)


def admin_menu(user):
    print('What do you want to do?')
    print('1. Check ATM balance')
    print('2. Check banknotes balance')
    print('3. Change banknotes balance')
    print('4. Transactions history')
    print('0. Exit')

    attempts = input_attempts
    for _ in range(input_attempts):
        user_choice = input('Enter your choice: ')
        match user_choice:
            case '1':
                return check_atm_balance(user)
            case '2':
                return check_banknotes(user)
            case '3':
                return change_banknotes_balance_menu(user)
            case '4':
                return check_logs(user)
            case '0':
                print(f'Goodbye {user}!')
                sleep(2)
                clear()
                start()
            case _:
                print(f'Wrong input! Try again! {attempts} attempts left.')
                sleep(1)
                try_again_user(admin_menu, user)


def start():
    clear()
    greetings()
    check_file(atm_data)
    current_user = login_user()
    user_menu(current_user)


if __name__ == '__main__':
    start()
