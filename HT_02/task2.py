"""2. Write a script which accepts two sequences of comma-separated colors 
from user. Then print out a set containing all the colors from color_list_1 
which are not present in color_list_2."""

# input_ = 'white black red yellow, blue white red green'
input_ = input('Enter your colors: ')
colors1, colors2 = map(str, input_.split(','))

color_list_1 = colors1.split()
color_list_2 = colors2.split()

my_set = {color for color in color_list_1 if color not in color_list_2}

print(my_set)
