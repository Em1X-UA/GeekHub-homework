"""6. Write a script to get the maximum and minimum VALUE in a dictionary."""


my_dict = {'a': 3, 'b': 4, 'c': 'smth', 'd': -3}

values = [el for el in my_dict.values() if type(el) is not str]
max_val = max(values)
min_val = min(values)

print(f'{max_val=} {min_val=}')
