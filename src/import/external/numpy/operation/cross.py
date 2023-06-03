import numpy as np

a = np.array([1, 1, 0])
b = np.array([-1, 1, 0])
c = np.cross(a, b)

print("a =", a)
print("b =", b)
print("c = np.ross(a, b) =", c)

"""
$ python cross.py
a = [1 1 0]
b = [-1  1  0]
c = np.ross(a, b) = [0 0 2]
"""
