"""3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по
   правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
   перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення,
   наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)"""


class NameLenException(Exception):
    pass


class PasswordLenException(Exception):
    pass


class PasswordSecurityException(Exception):
    pass


class PasswordStrongSecurityException(Exception):
    pass


def check_name_password(name, password):
    check_status = 'Password status: '
    try:
        if not 3 <= len(name) <= 50:
            raise NameLenException('Name length must be >= 3 and <= 50')
        if len(password) < 8:
            raise PasswordLenException('Password should be >= 8 symbols')
        if not [x for x in password if x.isdigit()]:
            raise PasswordSecurityException('Password must have at list one digit')
        if ('.' not in password) and ('_' not in password):
            raise PasswordStrongSecurityException('Password must have "_" or "." symbol')
    except NameLenException as err:
        check_status = f'Name error: {err}'
    except PasswordLenException as err:
        check_status += str(err)
    except PasswordSecurityException as err:
        check_status += str(err)
    except PasswordStrongSecurityException as err:
        check_status += str(err)
    else:
        check_status += 'OK'

    return check_status


users = [('MD', 'Melville_18190801'), ('Zidane', 'Ballon'),
         ('Ronaldinho10', 'JogaBonita.1980'), ('Barry.Allen', 'F4stest.man_alive'),
         ('Elon_Mask', 'Glory_to_Ukraine'), ('Anonimous', 'fsdfds1f')]

for user in users:
    print('-----------------------------------')
    print(f'Name: {user[0]}')
    print(f'Password: {user[1]}')
    print(check_name_password(user[0], user[1]))
