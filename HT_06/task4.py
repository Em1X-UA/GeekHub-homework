"""4. Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду
Морзе та виводить декодоване значення (латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive (на ваш розсуд - великими чи
                                            маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки
            тощо використовуватися не будуть. Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..-- -...   .. ...   .... . .-. .
    результат: GEEKHUB IS HERE"""


def morse_code(entered_string, default='decode'):
    decode = default == 'decode'
    encode_table = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
                    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
                    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
                    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
                    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
                    "Z": "--..", " ": "space", "SOS": "...---..."}

    if decode:
        decode_table = {v: k for k, v in encode_table.items()}
        symbols = entered_string.replace("   ", " space ").split(" ")
        return "".join(decode_table[x] for x in symbols)
    else:
        symbols = " ".join(encode_table[x] for x in entered_string.upper())
        return symbols.replace(" space ", "   ")


print(morse_code('--. . . -.- .... ..- -...   .. ...   .... . .-. .'))
print(morse_code('geekhub is here', 'encode'))
print(morse_code('...---...'))
print(morse_code('SOS', 'encode'))
