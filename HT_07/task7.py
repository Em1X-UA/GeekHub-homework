""" 7. Напишіть функцію, яка приймає 2 списки. Результатом має бути новий
список, в якому знаходяться елементи першого списку, яких немає в другому.
Порядок елементів, що залишилися має відповідати порядку в першому (оригінальному)
списку. Реалізуйте обчислення за допомогою генератора в один рядок.
    Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 3, 4], [2]) --> [1, 3, 4]"""


def lists_difference(list1: list, list2: list):
    # return list(set(list1).difference(set(list2)))  # набагато швидше
    return [x for x in list1 if x not in list2]


my_list1 = [1, 2, 2, 2, 3, 4]
my_list2 = [2]
result = lists_difference(my_list1, my_list2)
print(result, type(result))
