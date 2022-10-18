"""3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число
від 0 до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні."""


def is_prime(num):
    if num == 1:
        return False
    elif num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


print(is_prime(1))
print(is_prime(3))
print(is_prime(4))
