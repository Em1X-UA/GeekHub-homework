"""7. Написати функцію, яка приймає на вхід список (через кому), підраховує
кількість однакових елементів у ньому і виводить результат. Елементами
списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3,
    foo -> 2, [1, 2] -> 2, True -> 1" """


def count_same(*args):
    count_dict = {}
    for el in args:
        if str(el) not in count_dict.keys():
            count = 1
            count_dict.update({str(el): count})
        else:
            count = count_dict.get(str(el)) + 1
            count_dict.update({str(el): count})
    for k, v in count_dict.items():
        print(f'Value "{k}" passed in function {v} times.')


count_same(1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2])
