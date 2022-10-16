"""1. Написати функцію season, яка приймає один аргумент (номер місяця
від 1 до 12) та яка буде повертати пору року, до якої цей місяць належить
(зима, весна, літо або осінь). У випадку некоректного введеного
значення - виводити відповідне повідомлення."""


def get_month_name(num: int) -> str:
    month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
                  6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
                  11: 'November', 12: 'December'}
    season = ''
    if num in range(3, 5 + 1):
        season = 'Spring'
    elif num in range(6, 8 + 1):
        season = 'Summer'
    elif num in range(9, 11 + 1):
        season = 'Autumn'
    elif (num in range(1, 2 + 1)) or num == 12:
        season = 'Winter'
    else:
        return 'Incorrect number!'
    return f"It's {month_dict.get(num)}, and this is {season}!"


print(get_month_name(13))
