import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
c = a @ b

print("a =", a)
print("b =", b)
print("c = a @ b =", c)


"""
$ python dot_1.py
a = [1 2 3]
b = [3 2 1]
c = a @ b = 10
"""
