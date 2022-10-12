"""8. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити
умову, яка буде виводити поточне значення, якщо остача від ділення на 17
дорівнює 0."""


user_input = int(input('Enter INT value to count: '))
# user_input = int('93')

for i in range(1, user_input + 1):
    if i % 17 == 0:
        print(i)
