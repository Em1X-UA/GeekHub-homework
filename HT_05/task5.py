"""5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить
всі числа Фібоначчі, що не перевищують його. """


def fibonacci(n):
    f1 = 0
    f2 = 1
    print(f1, end=' ')
    print(f2, end=' ')
    while True:
        f1, f2 = f2, f1 + f2
        if f2 <= n:
            print(f2, end=' ')
        else:
            break


fibonacci(400)
