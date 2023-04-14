x = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(x)

x.remove(5)
print(x)

y = x.pop(1)
print(y)
print(x)

del(x[1:5])
print(x)


"""
$ python del_rem_pop.py
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[9, 8, 7, 6, 4, 3, 2, 1, 0]
8
[9, 7, 6, 4, 3, 2, 1, 0]
[9, 2, 1, 0]
"""
