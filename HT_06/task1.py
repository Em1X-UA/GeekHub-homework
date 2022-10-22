"""1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти
користувачів (ім'я та пароль). Функція повинна приймати три аргументи:
два - обов'язкових (<username> та <password>) і третій - необов'язковий
параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException
                                (його також треба створити =))"""


def user_check(name, password, silent=False):
    class LoginException(Exception):
        pass

    users = [('MobyDick', 'Melville_18190801'), ('Zidane', 'Ballon_dor_1998'),
             ('Ronaldinho10', 'JogaBonita.1980'), ('Barry.Allen', 'F4stest.man_alive'),
             ('Elon_Mask', 'Gl0ry_to_Ukraine')]

    try:
        for user in users:
            if name == user[0] and password == user[1]:
                return True
        raise LoginException('Incorrectly entered login or password')
    except LoginException as err:
        if silent:
            return False
        print(err)
        # raise
    return


print(user_check('Elon_Mask', 'Gl0ry_to_Ukraine'))
print(user_check('user1', 'asdasd', True))
print(user_check('user1', 'asdasd'))
