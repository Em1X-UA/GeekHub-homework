"""1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір
   автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду
   виводиться поточні кольори. Через декілька ітерацій - відбувається
   зміна кольорів - логіка така сама як і в звичайних світлофорах
   (пішоходам зелений тільки коли автомобілям червоний). """


from time import sleep


def light_colors():
    color_list = ['Red', 'Yellow', 'Green', 'Yellow']
    while True:
        for color_1 in color_list:
            color_2 = 'Green' if color_1 == 'Red' else 'Red'
            yield color_1, color_2


def main():
    colors = light_colors()
    while True:
        car_color, pedestrian_color = next(colors)
        seconds = 2 if car_color == 'Yellow' else 4
        for _ in range(seconds):
            print(f'{car_color} {pedestrian_color}')
            sleep(1)


if __name__ == '__main__':
    main()
