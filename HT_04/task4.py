""" 4. Наприклад маємо рядок --> "f98neroі4nr0c3n30іrn03іen3c0rfe kdno400we(nw,
kowe%00koі!jn35pіjnp4 6іj7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв
по клаві =)
   Створіть ф-цію, яка буде отримувати довільні рядки на зразок цього та яка
   обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прінтує довжину рядка,
кількість букв та цифр
-  якщо довжина менше 30 -> прінтує суму всіх чисел та окремо рядок без цифр
та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =) """


def check_string(string):
    len_str = len(string)

    def alpha_list():
        return [i for i in string if i.isalpha()]

    def digit_list():
        return [int(i) for i in string if i.isdigit()]

    if len_str in range(30, 50 + 1):
        print(f'String length is: {len_str}. '
              f'String has: {len(alpha_list())} letters, '
              f'and {len(digit_list())} digits')
    elif len_str < 30:
        print(f'String contains numbers whose sum is: {sum(digit_list())} '
              f'and "{"".join(alpha_list())}" letters')
    else:
        print(f'String has {len_str - len(alpha_list()) - len(digit_list())} '
              f'symbols that do not belong to letters or digits.')
    return


my_str = 'f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 ' \
         '6ij7k5j78p3kj546p4 65jnpoj35po6j345'

check_string(my_str)
