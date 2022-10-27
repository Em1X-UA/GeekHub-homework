""" 3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію
цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1    3    5    7    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію
   по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо).
   Подивіться як веде себе стандартний range в таких випадках."""


def hand_made_range(*args):
    """This is hand made range function.
    You can use float values and values in string (in q-ty of args)
    (like input() func without handle conversion) as arguments"""

    def determine_value(num):
        try:
            num = float(num)
            return num if num % 1 != 0 else int(num)
        except ValueError:
            print(f'Argument "{num}" is not a number')
            raise ValueError

    args_list = [determine_value(item) for item in args]
    if len(args_list) == 1:
        start = 0
        stop = args_list[0]
        step = 1 if stop > start else -1
    elif len(args_list) == 2:
        start, stop = args_list
        step = 1 if stop > start else -1
    elif len(args_list) == 3:
        start, stop, step = args_list
    else:
        raise TypeError(f'Expected 1-3 arguments, got {len(args_list)}')

    try:
        if step == 0:
            raise ValueError('Step argument can\'t be 0!')
        elif start == stop:
            raise ValueError('Start and Stop arguments can\'t be equal')
        elif start > stop and step > 0:
            raise ValueError('If Start value bigger than Stop, Step should be negative')
        elif start < stop and step < 0:
            raise ValueError('You can\'t move from less value to bigger by subtracting')
    except ValueError as err:
        print(f'Error!!! {err}')
    else:
        value = start
        if start < stop:
            while value < stop:
                yield round(determine_value(value), 2)
                value += step
        else:
            while value > stop:
                yield round(determine_value(value), 2)
                value += step


my_gen_func = hand_made_range(1, '10', 2)
result_list = list(my_gen_func)
print(result_list)

type_list = [type(elem) for elem in result_list]
print(type_list)
