"""
1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість
color з початковим значенням white і метод для зміни кольору фігури, а його
підкласи «овал» (Oval) і «квадрат» (Square) містять методи _init_ для завдання
початкових розмірів об'єктів при їх створенні.
"""


from random import choice


class Figure:
    color = 'white'
    # def __init__(self):
    #     self.color = 'white'

    def change_color(self, color=None):
        if color is None:
            color = choice(['red', 'green', 'blue', 'purple', 'yellow'])
        self.color = color


class Oval(Figure):
    def __init__(self, diameter):
        self.diameter = diameter


class Square(Figure):
    def __init__(self, size):
        self.size = size


def main():
    print('Oval:')
    oval_1 = Oval(5)
    print(oval_1.color)

    oval_1.change_color('black')
    print(oval_1.color)

    print('\nSquare:')
    square_1 = Square(3)
    print(square_1.color)

    square_1.change_color()
    print(square_1.color)


if __name__ == '__main__':
    main()
