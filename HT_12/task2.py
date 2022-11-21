"""
2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної
бібліотеки (включіть фантазію). Наприклад вона може містити
класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
Можна робити по прикладу банкомату з меню, базою даних і т.д.
"""


class Book:
    books = []
    taken_books = []

    def __init__(self, author, name, year):
        self.author = author
        self.name = name
        self.year = year
        Book.books.append((self.author, self.name, self.year,))

    def get_book_data(self):
        return self.author, self.name, self.year,


class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_books_list():
        print('Books in library:')
        for author, name, year in Book.books:
            print(f'Author: {author}, {year}, {name}')


class Student(Person):
    def take_book(self, book):
        book = Book.get_book_data(book)
        book_index = Book.books.index(book)
        taken_book = Book.books.pop(book_index)
        Book.taken_books.append((taken_book, f'taken by {self.name}'))
        print(f'Book is taken {taken_book}')

    def return_book(self, book):
        i = 0
        for el in Book.taken_books:
            if str(Book.get_book_data(book)) in str(el) and self.name in str(el):
                i = Book.taken_books.index(el)
                break
        returned_book = Book.taken_books.pop(i)
        Book.books.append(Book.get_book_data(book))
        print(f'Book returned {returned_book}')


class Teacher(Student):
    @staticmethod
    def get_taken_books():
        if len(Book.taken_books) < 1:
            print('Noo books taken')
            return

        print('Taken books')
        for book, taken_by in Book.taken_books:
            print(book[0], book[1], book[2], taken_by)


def main():
    kobzar = Book('Taras Shevchenko', '"Kobzar"', 1840)
    forest_song = Book('Lesya Ukrainka', '"The Forest Song"', 1912)
    shadow_forg_anc = Book('Mykhailo Kotsyubynsky',
                           '"Shadows of Forgotten Ancestors"', 1912)

    print('=============')
    print(kobzar.year)
    print(forest_song.name)
    print(shadow_forg_anc.author)
    print('=============')

    j_silver = Person('Johnny Silverhand')
    print(j_silver.name)
    j_silver.get_books_list()
    print('=============')

    barry_allen = Student('Barry Allen')
    print(barry_allen.name)
    barry_allen.take_book(kobzar)
    print('=============')
    teacher = Teacher('Teacher')
    print(teacher.name)
    teacher.get_taken_books()
    barry_allen.get_books_list()
    print('=============')
    barry_allen.return_book(kobzar)
    barry_allen.get_books_list()
    print('=============')


if __name__ == '__main__':
    main()
