"""2. Створіть 3 різних функції (на ваш вибір). Кожна з цих функцій повинна
повертати якийсь результат (напр. інпут від юзера, результат математичної
операції тощо). Також створіть четверту ф-цію, яка всередині викликає 3
попередні, обробляє їх результат та також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцію, а вона в своєму
тілі - ще 3."""


def double(num):
    return num * 2


def exp_to_4(num):
    return num ** 4


def factorial(num):
    if num == 0:
        return 1
    f = 1
    i = 0
    while i < num:
        i += 1
        f *= i
    return f


def sum_all(num):
    return double(num) + exp_to_4(num) + factorial(num)


print(sum_all(5))
