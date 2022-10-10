"""2. Write a script which accepts two sequences of comma-separated colors 
from user. Then print out a set containing all the colors from color_list_1 
which are not present in color_list_2."""

# input_ = 'white black red yellow, blue white red green'
input_ = input('Enter your colors: ')
colors1, colors2 = map(str, input_.split(','))

color_list_1 = set(colors1.split())
color_list_2 = set(colors2.split())

print(color_list_1.difference(color_list_2))
