"""
3. Створіть клас в якому буде атрибут який буде
рахувати кількість створених екземплярів класів.
"""


class Test:
    examples_count = 0

    def __init__(self, name):
        self.__class__.examples_count += 1
        self.name = name


def main():
    print('Start count: ', Test.examples_count)  # -> 0

    a = Test('a')
    print(a.name)  # -> a
    print(a.examples_count)  # -> 1

    b = Test('b')
    print(b.name)  # -> b
    print(b.examples_count)  # -> 2

    c = Test('c')
    print(c.name)  # -> c
    print(c.examples_count)  # -> c

    print(a.examples_count, b.examples_count, c.examples_count)  # -> 3 3 3


if __name__ == '__main__':
    main()
