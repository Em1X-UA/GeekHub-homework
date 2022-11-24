"""
4. Створіть клас, який буде повністю копіювати поведінку list,
за виключенням того, що індекси в ньому мають починатися з 1,
а індекс 0 має викидати помилку (такого ж типу, яку кидає list
якщо звернутися до неіснуючого індексу)
"""


class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError('Index start from 1!')
        index -= 1
        return super().__getitem__(index)


def main():
    a = MyList(range(1, 5))
    print(a)  # --> [1, 2, 3, 4]

    # print(f'{a[0]=}')  # --> IndexError
    print(f'{a[1]=}')  # --> 1
    print(f'{a[2]=}')  # --> 2

    a.append(5)
    print(a)  # --> [1, 2, 3, 4, 5]

    print(len(a))  # --> 5
    print(a.pop())  # --> 5
    print(a)  # --> [1, 2, 3, 4]


if __name__ == '__main__':
    main()
