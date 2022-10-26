""" 4. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну
послідовність (рядок, список, кортеж) і повертає генератор, який буде
повертати значення з цієї послідовності, при цьому, якщо було повернено
останній елемент із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in my_generator([1, 2, 3]):
       print(elem)
   1    2    3    1    2    3    1"""


def get_value_from_iter(input_iter):
    while True:
        for item in input_iter:
            yield item


# iterable = 'hello'
iterable = range(5)
res = get_value_from_iter(iterable)
for n in range(10):
    print(next(res))
