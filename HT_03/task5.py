"""5. Write a script to remove values duplicates from dictionary. 
Feel free to hardcode your dictionary."""


my_dict = {'key1': 'hello', 'key2': 'Tom', 'key3': 'hello', 
			'key4': 5, 'key5': 19.2, 'key6': 5}

values = my_dict.values()
print(values)

count_dict = {}
for element in values:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

for k, v in count_dict:
	if v > 1:

print(duplicates)
print(my_dict)
