""" 5. Напишіть функцію, яка приймає на вхід рядок та повертає кількість окремих
регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж 1 раз.
Рядок буде складатися лише з цифр та букв (великих і малих).
Реалізуйте обчислення за допомогою генератора в один рядок
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі"""


def repeatable_chars_qty(string_to_check: str):
    return len(set(char for char in string_to_check.lower()
                   if string_to_check.lower().count(char) > 1))


my_string = 'Indivisibilities'
res = repeatable_chars_qty(my_string)
print(res)
