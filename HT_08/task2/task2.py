"""2. Написати функцію, яка приймає два параметри:
ім'я (шлях) файлу та кількість символів.
Файл також додайте в репозиторій. На екран має бути виведений список із
трьома блоками - символи з початку, із середини та з кінця файлу.
Кількість символів в блоках - та, яка введена в другому параметрі.
Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша,
ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному
символу, то що виводити на місці середнього блоку символів?).
Не забудьте додати перевірку чи файл існує."""


from os import path


def read_file(filename, chars: int) -> list:
    """Function accepts text file ('filename') and chars q-ty ('chars').
    It returned a list with 3 parts text (len == 'chars') from start, middle
    and end of text. Also if text can't be separated by 3 equal parts, with
    length == 'chars' it returned 1-2 text parts separated by 'chars' q-ty."""

    try:
        if not path.exists(filename):
            raise FileNotFoundError
        chars = abs(int(chars))
    except FileNotFoundError:
        print('File doesn\'t exists')
        raise
    except ValueError:
        print('Chars quantity is incorrect!')
        raise ValueError
    else:
        with open(filename) as file:
            content = file.read()
            mid_string = int(len(content) / 2)

            if chars > len(content):
                print(f'Attention! File {filename} length is less than '
                      f'input chars qty: {chars}! Returned listed file text')
                result = [content]
            elif chars >= mid_string:
                print(f'Attention! File {filename} doesn\'t have enough symbols to split '
                      f'for 3 parts with input chars q-ty: {chars}! Returned 2')
                result = [content[:chars], content[chars:]]
            elif chars * 3 >= len(content):
                print(f'Attention! File {filename} doesn\'t have enough '
                      f'symbols to split for 3 equal parts with input '
                      f'chars {chars} q-ty! Returned 3, but last is less')
                result = [content[:chars], content[chars:chars * 2],
                          content[chars * 2:chars * 3]]
            else:
                first = content[:chars]
                middle = content[int(mid_string - chars / 2):int(mid_string + chars / 2)]
                last = content[-chars::]
                result = [text for text in (first, middle, last)]
            return result


def main():
    test_file = 'testfile_task2.txt'
    for el in [50, 25, 14, 5]:
        print('--------------------------------')
        res = read_file(test_file, el)
        print(f'Chars input q-ty: {el}')
        print(res)


if __name__ == '__main__':
    main()
