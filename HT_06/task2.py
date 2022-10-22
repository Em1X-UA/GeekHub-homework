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

    name_status = f'Name "{name}" status is: '
    password_status = 'Password status: '

    try:
        if len(name) not in range(3, 50 + 1):
            raise NameLenException('Name length must be >= 3 and <= 50')
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
        print(name_status)
        print(password_status)

    return


print(check_name_password('user', 'asas.s1sas'))
