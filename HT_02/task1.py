"""1. Write a script which accepts a sequence of comma-separated numbers from
user and generates a list and a tuple with those numbers."""

#user_input = '1, 3, 5, 7, 9, 150, 5.0, asd'
user_input = input('Enter numbers: ')

my_list = []

for el in user_input.split(','):
	el = el.strip()
	
	try:
		val = int(el)
		my_list.append(val)

	except ValueError:
		try:
			val = float(el)
			my_list.append(val)
		except ValueError:
			print(f'Input "{el}" is not a number')


my_tuple = tuple(my_list)

# print(my_list)
# print(my_tuple)
