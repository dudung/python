import math
def sigmoid(z):
  return 1 / (1 + math.exp(-z))

import sys
sys.path.append("../")

import matrix.matrix as mtx

X = [
  [0, 0, 1, 1],
  [0, 1, 0, 1]
]

W = [
  [100, 100]
]

Z = mtx.mul(W, X)
Y = mtx.map(Z, sigmoid)

[print(row) for row in X]
print()

[print(row) for row in W]
print()

[print(row) for row in Y]


"""
$ python layers_21_matrix_and.py

"""