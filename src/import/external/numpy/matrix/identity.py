import numpy as np

m = np.identity(4)

print("m =")
print(m)

print()
print("ndim =", m.ndim)
print("shape =", m.shape)


"""
$ python identity.py
m =
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]

ndim = 2
shape = (4, 4)
"""
