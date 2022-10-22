"""2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із
   відповідним текстом."""


def check_name_password(name, password):
    class NameLenException(Exception):
        pass

    class PasswordLenException(Exception):
        pass

    class PasswordSecurityException(Exception):
        pass

    class PasswordStrongSecurityException(Exception):
        pass

    def name_check():
        if len(name) not in range(3, 50 + 1):
            raise NameLenException('Name length must be >= 3 and <= 50')
        return

    def password_check():
        if len(password) < 8:
            raise PasswordLenException('Password should be >= 8 symbols')
        if not [x for x in password if x.isdigit()]:
            raise PasswordSecurityException('Password must have at list one digit')
        if ('.' not in password) and ('_' not in password):
            raise PasswordStrongSecurityException('Password must have "_" or "." symbol')
        return

    try:
        name_check()
    except NameLenException as err:
        print(err)

    password_status = 'Password status: '
    try:
        password_check()
    except PasswordLenException as err:
        password_status += f'\n{err}'
    except PasswordSecurityException as err:
        password_status += f'\n{err}'
    except PasswordStrongSecurityException as err:
        password_status += f'\n{err}'
    else:
        password_status += f'\nOK'
    finally:
        print(password_status)

    return
    # return (name, password),


check_name_password('user', 'as_a1sddas')
