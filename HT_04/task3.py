"""3. Користувач вводить змінні "x" та "y" з довільними цифровими значеннями.
Створіть просту умовну конструкцію (звісно вона повинна бути в тілі ф-ції),
під час виконання якої буде перевірятися рівність змінних "x" та "y" та у
випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z замінність на відповідні числа):
    x > y;       відповідь - "х більше ніж у на z"
    x < y;       відповідь - "у більше ніж х на z"
    x == y.      відповідь - "х дорівнює y" """


def compare_values(x, y):
    if x == y:
        return f'{x} equals {y}'
    max_val = max(x, y)
    min_val = min(x, y)
    return f'{max_val} is greater than {min_val} by {max_val - min_val}'


x, y = map(int, input('Enter (separated by a space) '
                      '2 INT numbers to compare : ').split())
print(compare_values(x, y))
