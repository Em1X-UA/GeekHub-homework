"""6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів
в списку. Тобто функція приймає два аргументи: список і величину зсуву (якщо
ця величина додатна - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]"""


def shift_elements(lst: list, shift: int) -> list:
    if shift == 0:
        pass
    elif shift > 0:
        for i in range(shift):
            lst.insert(0, lst.pop(-1))
    else:
        for i in range(abs(shift)):
            lst.append(lst.pop(0))
    return lst


print(shift_elements([1, 2, 3, 4, 5], 1))
print(shift_elements([1, 2, 3, 4, 5], -2))
