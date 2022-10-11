"""1. Write a script that will run through a list of tuples and replace the 
last value for each tuple. The list of tuples can be hardcoded. 
The "replacement" value is entered by user. The number of elements in the 
tuples must be different."""


from random import randint

my_list = []
for _ in range(randint(2,7)):
	my_list.append(tuple(randint(0, 100) for __ in range(randint(3, 6))))

print(my_list)

#user_input = input('Enter replacement for last tuple elements: ')
user_input = 'my_value'

#print(my_list[0][0:-1])
for i in range(0, len(my_list)):
	
	#print(my_list[i][0:-1])
	my_list[i] = (f' for _ in my_list[i][0:-1], user_input)


print(my_list)


