d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d2.update(d1)

print(d2)
# {'c': 3, 'd': 4, 'a': 1, 'b': 2}


d1 = {'a': 1, 'b': 2}
d2 = {**d1, 'c': 3, 'd': 4}

print(d2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
