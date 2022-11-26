import sqlite3
from random import randint, choice
from settings import input_attempts, atm_data
from modules.system_modules import clear, slp, get_user_choice, check_file
from modules.atm_module import Atm


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


def try_again_or_start(func):
    """
    Function mostly for input error cases before login
    """

    from main import start

    print('1. Try again')
    print('0. Back to start')
    user_choice = get_user_choice(1)
    if user_choice == 1:
        clear()
        return func()
    elif user_choice == 0:
        clear()
        return start()


def login_user():
    """
    Verification user and return tuple with user_type.
    True if collector.
    """

    clear()
    print('Please log in system')
    attempts_left = input_attempts
    for _ in range(input_attempts):
        input_login = input('1. Login: ')
        input_password = input('2. Password: ')

        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()

            cursor.execute("SELECT user FROM users_data "
                           "WHERE user = ?", [input_login])
            if cursor.fetchone() is None:
                attempts_left -= 1
                print(f'Incorrect login. {attempts_left} attempts left.')
            else:
                cursor.execute("SELECT password FROM users_data "
                               "WHERE user = ? AND password = ?",
                               [input_login, input_password])
                if cursor.fetchone() is None:
                    attempts_left -= 1
                    print(f'Incorrect password. '
                          f'{attempts_left} attempts left.')
                else:
                    cursor.execute("SELECT is_collector FROM users_data "
                                   "WHERE user = ?", [input_login])
                    if cursor.fetchone()[0] == '1':
                        user = (input_login, True)
                    else:
                        user = (input_login, False)
                    return user
    raise LoginFailedException('Error. All attempts failed. '
                               'Please contact the bank!')


def register():
    """
    Obviously this function can add new users and return user_name.
    """

    check_file(atm_data)

    user_login = input('Enter your login to register: ')

    # checking for same names in db
    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        cursor.execute("SELECT user FROM users_data "
                       "WHERE user = ?", [user_login])
        if cursor.fetchone() is not None:
            print(f'User with name "{user_login}" already exists.')
            print('Try to register again?')
            try_again_or_start(register)

    # checking name length
    name_status = f'Name "{user_login}" status is: '
    name_is_ok = True
    try:
        if not 4 <= len(user_login) <= 50:
            raise NameLenException('Name length must be >= 4 and <= 50')
    except NameLenException as err:
        name_status += str(err)
        name_is_ok = False
    else:
        name_status += 'OK'
    finally:
        clear()
        print(name_status)
        slp()
        if not name_is_ok:
            try_again_or_start(register)
        clear()

    user_password = input('Enter your password \n(must have >= 8 and <= 50 '
                          'symbols, at least 1 digit, and "_" or "." symbol): ')

    # password security checking
    password_status = 'Password status: '
    password_is_ok = True
    try:
        if not 8 <= len(user_password) <= 50:
            raise PasswordLenException('Password should be '
                                       '>= 8 and <= 50 symbols')
        if not [x for x in user_password if x.isdigit()]:
            raise PasswordSecurityException('Password must have '
                                            'at list one digit')
        if ('.' not in user_password) and ('_' not in user_password):
            raise PasswordStrongSecurityException('Password must have '
                                                  '"_" or "." symbol')
    except PasswordLenException as err:
        password_status += str(err)
        password_is_ok = False
    except PasswordSecurityException as err:
        password_status += str(err)
        password_is_ok = False
    except PasswordStrongSecurityException as err:
        password_status += str(err)
        password_is_ok = False
    else:
        password_status += 'OK'
    finally:
        clear()
        print(password_status)
        slp()
        if not password_is_ok:
            try_again_or_start(register)
        clear()

    # password confirmation
    attempts_left = input_attempts
    password_confirm = False
    for _ in range(input_attempts):
        input_confirm = input('Please confirm your password: ')
        if user_password == input_confirm:
            print('Password confirmed')
            password_confirm = True
            break
        attempts_left -= 1
        print(f'Incorrect password. {attempts_left} attempts left.')
    if not password_confirm:
        print('Error. You can try register again.')
        slp()
        clear()
        try_again_or_start(register)

    with sqlite3.connect(atm_data) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users_data(user, password, balance, "
                       "is_collector) VALUES (?, ?, ?, ?)",
                       (user_login, user_password, 0, False))
    clear()
    print(f'Registration completed! \n{user_login}, welcome to our bank!')
    slp()
    clear()
    random_bonus(user_login)
    return user_login, False


def random_bonus(user):
    """
    Calculate random registration bonus with chance = bonus_probability.
    If win - add money, else nothing.
    """

    bonus_probability = 10
    luck = randint(1, 100)
    if luck <= bonus_probability:
        bonus_variants = [100, 200, 500]
        bonus = choice(bonus_variants)
        print(f'Congratulations, {user}!')
        print(f'For registration, you have a bonus - {bonus} UAH!')
        Atm.change_user_balance(user, 'bonus', bonus)

        input('Press any key and (or just) ENTER to back main menu')
        clear()
