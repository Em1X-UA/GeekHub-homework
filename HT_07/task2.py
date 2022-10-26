""" 2. Запишіть в один рядок генератор списку (числа в діапазоні
від 0 до 100 не включно), сума цифр кожного елемент якого буде дорівнювати 10.
   Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]"""


def list_generator(start, end):
    return [val for val in range(start, end)
            if sum(int(digit) for digit in str(val)) == 10]


result = list_generator(0, 100)
print(result)
