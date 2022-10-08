"""1. Write a script which accepts a sequence of comma-separated numbers from
user and generates a list and a tuple with those numbers."""

# user_input = '1, 3, 5, 7, 9, 150, 5.0'
user_input = input('Enter numbers: ')

my_list = []

for el in user_input.split(','):
	try:
		if int(el) / float(el) == 1.0:
			my_list.append(int(el))
	except:
		my_list.append(float(el))

my_tuple = tuple(my_list)


# print(my_list)
# print(my_tuple)
