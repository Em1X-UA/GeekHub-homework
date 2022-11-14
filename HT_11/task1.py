""" 1. Створити клас Calc, який буде мати атрибут last_result та 4 методи.
Методи повинні виконувати математичні операції з 2-ма числами, а саме
додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атрибута last_result
він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен повернути результат
виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас (можете почитати цю статтю:
https://realpython.com/documenting-python-code/ ) """


class Calc:
    """
    Calculator class
    Have 4 methods to calculate 2 values
    """

    def __init__(self):
        self.last_result = None
        self.result = None

    def add(self, num1, num2):
        self.result = num1 + num2
        self.last_result = self.result
        return self.result

    def subtraction(self, num1, num2):
        self.result = num1 - num2
        self.last_result = self.result
        return self.result

    def multiplying(self, num1, num2):
        self.result = num1 * num2
        self.last_result = self.result
        return self.result

    def division(self, num1, num2):
        try:
            self.result = num1 / num2
        except ZeroDivisionError as err:
            self.result = err
        self.last_result = self.result
        return self.result


if __name__ == '__main__':
    print(Calc.__doc__)

    res = Calc()

    print(res.last_result)
    print(res.add(2, 2))
    print('==================')

    print(res.last_result)
    print(res.subtraction(5, 4))
    print('==================')

    print(res.last_result)
    print(res.multiplying(5, 5))
    print('==================')

    print(res.last_result)
    print(res.division(9, 3))
    print('==================')

    print(res.last_result)
    print(res.division(9, 0))
    print('==================')
