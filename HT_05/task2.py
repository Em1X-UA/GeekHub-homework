"""2. Написати функцію <bank>, яка працює за наступною логікою: користувач
робить вклад у розмірі <a> одиниць строком на <years> років під <percents>
відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші
додаються до суми вкладу і в наступному році на них також нараховуються
відсотки). Параметр <percents> є необов'язковим і має значення по замовчуванню
<10> (10%). Функція повинна принтануть суму, яка буде на рахунку, а також її
повернути (але округлену до копійок). """


def bank(deposit, years, percents=10):
    for _ in range(1, years + 1):
        deposit *= 1 + percents / 100
    print(f'There is {round(deposit, 2)} "USD" on your account.')
    return round(deposit, 2)


print(bank(1000, 5, 15))
print(bank(1000, 3))
