"""2. Write a script to remove empty elements from a list.
Test list: 
[(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]"""


my_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
# print(my_list)
# print(len(my_list))

my_list = [value for value in my_list if value]
# print(my_list)
# print(len(my_list))
