"""5. Ну і традиційно - калькулятор. Повинна бути 1 функція,
яка приймає 3 аргументи - один з яких операція, яку зробити! Аргументи брати
від юзера (можна по одному - окремо 2, окремо +, окремо 2; можна всі
разом - типу 2 + 2). Операції що мають бути
присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями
на предмет помилок!"""


def calculator(a, b, act):
    def determine_value(num):
        try:
            num = int(num)
            return num

        except ValueError:
            try:
                num = float(num)
                return num
            except ValueError:
                print(f'Input "{num}" is not a number')
                raise ValueError

    a = determine_value(a)
    b = determine_value(b)
    match act:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b if b != 0 else "Don't try to divide by zero"
        case '%':
            return a % b if b != 0 else "Oh, common.. divide by zero?"
        case '//':
            return a // b if b != 0 else "Don't play with me"
        case '**':
            return a ** b
        case _:
            return 'Incorrect action entered'


x, action, y = map(str, input('Enter (separated by a space) '
                              '2 INT numbers and action symbol (like "2 // 2"): ').split())

print(calculator(x, y, action))
