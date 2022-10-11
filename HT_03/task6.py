"""6. Write a script to get the maximum and minimum VALUE in a dictionary."""


my_dict = { 'a' : 3, 'c' : 4, 'd' : -3 }

max_val = max(my_dict.values())
min_val = min(my_dict.values())

print(f'{max_val=} {min_val=}')
