"""4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок
і кінець діапазона, і вертатиме список простих чисел всередині цього
діапазона. Не забудьте про перевірку на валідність введених даних та у
випадку невідповідності - виведіть повідомлення. """


def prime_list(a, b):
    def check_value(number):
        try:
            number = round(number)
            return number
        except ValueError:
            print(f'Input "{number}" is not a number')
            raise ValueError

    def is_prime(num):
        if num == 1:
            return False
        elif num % 2 == 0:
            return num == 2
        d = 3
        while d * d <= num and num % d != 0:
            d += 2
        return d * d > num

    a = check_value(a)
    b = check_value(b)
    return [x for x in range(a, b + 1) if is_prime(x)]


print(prime_list(2.7, 10))
