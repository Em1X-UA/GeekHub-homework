"""7. Write a script to concatenate all elements in a list into a string and 
print it. List must include both strings and integers and must be hardcoded."""

my_list = [1, 2, 'u', 'a', 4, True]
my_string = ''

for el in my_list:
	my_string += str(el)

print(my_string)
