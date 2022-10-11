"""7. Write a script which accepts a <number>(int) from user and generates 
dictionary in range <number> where key is <number> and value is 
<number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}"""


# user_imput = int(input('Enter dictionary range (only int): '))
user_imput = 3

my_dict = {}
for n in range(user_imput + 1):
    v = n ** 2
    my_dict.fromkeys(n, v)

print(my_dict)