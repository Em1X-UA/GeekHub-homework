from settings import atm_data
from modules.system_modules import clear, slp, get_user_choice, check_file
from modules.verification import login_user, register
from modules.admin_module import Admin
from modules.user_module import User


def greetings():
    """
    Start screen function
    """

    clear()
    print('Dear user!')
    print('Hello! I\'m console ATM program')
    print('Please use only digits for navigation in menu\n')
    input('Press any key and (or just) ENTER to proceed!')


def start_menu():
    """
    Start menu for login or register
    """

    print('Choose your option')
    print('1. Login')
    print('2. Register\n')
    print('0. Exit\n')
    user_choice = get_user_choice(2)
    user = ()
    match user_choice:
        case 1:
            user = (login_user())
        case 2:
            user = (register())
        case 0:
            print('Goodbye!')
            slp()
            clear()
            return start()
    clear()
    return user


def start():
    """
    Main working function to login and resend to user or admin module.
    """

    greetings()
    check_file(atm_data)
    user_login = start_menu()

    # check admin status
    if user_login[1]:
        user_class = Admin
    else:
        user_class = User
    user = user_class(user_login[0])
    user.user_menu()


if __name__ == '__main__':
    start()
