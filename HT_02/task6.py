"""6. Write a script to check whether a value from user input is contained in 
a group of values."""

def check_val_in_list(list_, val):
	for i in list_:
		if val == str(i):
			return True
	return False


values_list = [1, 2, 'u', 'a', 4, True]
input_ = input('Enter value to check: ')

print(check_val_in_list(values_list, input_))
