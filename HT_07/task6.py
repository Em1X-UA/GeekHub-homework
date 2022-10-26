""" 6. Напишіть функцію, яка приймає рядок з декількох слів і повертає довжину
найкоротшого слова. Реалізуйте обчислення за допомогою генератора в один рядок."""


def shortest_word_len(input_string: str):
    return min([len(word) for word in input_string.split()])


my_string = 'string check'
result = shortest_word_len(my_string)
print(result)
