"""4. Write a script which accepts a <number> from user and then <number> 
times asks user for string input. At the end script must print out result 
of concatenating all <number> strings."""

my_string = ''
strings_qty = int(input('Enter strings quantity: '))

for n in range(strings_qty):
	my_string += input(f'Enter {n + 1} string: ')

print(my_string)
