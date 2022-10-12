"""5. Write a script to remove values duplicates from dictionary. 
Feel free to hardcode your dictionary."""

my_dict = {'key1': 'hello', 'key2': 'Tom', 'key3': 'hello',
           'key4': 5, 'key5': 19.2, 'key6': 5}

temp_dict = {}
for k, v in my_dict.items():
    if v not in temp_dict.values():
        temp_dict.update({k: v})

my_dict = temp_dict.copy()
temp_dict.clear()

print(my_dict)
