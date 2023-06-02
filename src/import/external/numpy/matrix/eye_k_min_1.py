import numpy as np

m = np.eye(5, k=-1)

print("m =")
print(m)

print()
print("ndim =", m.ndim)
print("shape =", m.shape)


"""
$ python eye_k_min_1.py
m =
[[0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]]

ndim = 2
shape = (5, 5)
"""
