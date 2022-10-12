"""9. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який
виведе всі високосні роки в цьому проміжку (границі включно).
P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо
він кратний 400."""


# start_year, last_year = 2990, 3022
start_year, last_year = map(int, input('Enter the start and last year '
                                       'separated by a space: ').split())

for year in range(start_year, last_year + 1):
    if (year % 4 == 0) and (year % 100 != 0):
        print(f'{year} is a leap year')
    elif (year % 400 == 0) and (year % 100 == 0):
        print(f'{year} is a leap year')
