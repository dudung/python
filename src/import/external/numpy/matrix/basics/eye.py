import numpy as np

m = np.eye(5)

print("m =")
print(m)

print()
print("ndim =", m.ndim)
print("shape =", m.shape)


"""
$ python eye.py
m =
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]

ndim = 2
shape = (5, 5)
"""
