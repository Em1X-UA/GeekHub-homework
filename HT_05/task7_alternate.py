def count_same(*args):
    values = []
    count = []
    for el in args:
        if el not in [x for x in values if isinstance(x, type(el))]:
            values.append(el)
            count.append(1)
        else:
            count[values.index(el)] += 1
    return ', '.join([f'{values[i]} -> {count[i]}' for i in range(len(values))])
    # return '\n'.join([f'{values[i]} of type {type(values[i])} -> {count[i]}'
    #                   for i in range(len(values))])


print(count_same(1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2], '1'))
