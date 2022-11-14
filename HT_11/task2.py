""" 2. Створити клас Person, в якому буде присутнім метод __init__ який буде
приймати якісь аргументи, які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атрибут
profession (його не має інсувати під час ініціалізації в самому класі)
та виведіть його на екран (прінтоніть) """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(self.age)
        # return self.age

    def print_name(self):
        print(self.name)
        # return self.name

    def show_all_information(self):
        print(self.__dict__)
        # return self.__dict__


if __name__ == '__main__':
    zizu = Person('Zinedine Zidane', 50)
    zizu.profession = 'Manager'
    zizu.show_age()
    print('====================')

    ramos = Person('Sergio Ramos', 36)
    ramos.profession = 'Player'
    ramos.print_name()
    print('====================')

    zizu.show_all_information()
    ramos.show_all_information()
