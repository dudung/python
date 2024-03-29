import math
def sigmoid(z):
  return 1 / (1 + math.exp(-z))

import sys
sys.path.append("../")

import datalibs as dl

import matrix.matrix as mtx

X1 = [
  [0, 0, 1, 1],
  [0, 1, 0, 1]
]

Y = [
  [0],
  [1],
  [0],
  [1]
]

W21 = [
  [1, 1],
  [1, 1],
  [1, 1]
]

W32 = [
  [1, 1, 1],
  [1, 1, 1]
]

W43 = [
  [1, 1]
]

dl.randomize(W21)
dl.randomize(W32)
dl.randomize(W43)

X2 = mtx.map(mtx.mul(W21, X1), sigmoid)
X3 = mtx.map(mtx.mul(W32, X2), sigmoid)
X4 = mtx.map(mtx.mul(W43, X3), sigmoid)

dl.roundmat(X2, 3)
dl.roundmat(X3, 3)
dl.roundmat(X4, 3)

print("X1")
[print(row) for row in X1]
print()

print("X2")
[print(row) for row in X2]
print()

print("X3")
[print(row) for row in X3]
print()

print("X4")
[print(row) for row in X4]
print()

print("Y")
[print(row) for row in mtx.tpose(Y)]


"""
$ python layers_2321_ff_rand_w.py
X1
[0, 0, 1, 1]
[0, 1, 0, 1]

X2
[0.5, 0.622, 0.512, 0.634]
[0.5, 0.622, 0.655, 0.758]
[0.5, 0.565, 0.713, 0.763]

X3
[0.369, 0.344, 0.35, 0.326]
[0.218, 0.176, 0.167, 0.137]

X4
[0.485, 0.488, 0.488, 0.49]

Y
[0, 1, 0, 1]
"""
