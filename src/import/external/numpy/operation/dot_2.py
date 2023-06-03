import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
c = a.dot(b)

print("a =", a)
print("b =", b)
print("c = a.dot(b) =", c)


"""
$ python dot_2.py
a = [1 2 3]
b = [3 2 1]
c = a.dot(b) = 10
"""
