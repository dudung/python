x = [8, 8 , 9, 1, 6]
print(x)

y = 1
x.append(y)
print(x)

z = [2, 3, 4]
x.extend(z)
print(x)


"""
$ python append_extend.py
[8, 8, 9, 1, 6]
[8, 8, 9, 1, 6, 1]
[8, 8, 9, 1, 6, 1, 2, 3, 4]
"""
