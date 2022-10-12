"""7. Write a script which accepts a <number>(int) from user and generates 
dictionary in range <number> where key is <number> and value is 
<number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}"""


user_input = int(input('Enter dictionary range (only int): '))
# user_input = 3

my_dict = {}
for n in range(user_input + 1):
    my_dict.update({n: n * n})

print(my_dict)
