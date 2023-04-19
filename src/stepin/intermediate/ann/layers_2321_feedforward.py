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
  [0.845, 0.845]
]

Z = mtx.mul(W, X)
Y = mtx.map(Z, sigmoid)

[print(row) for row in X]
print()

[print(row) for row in W]
print()

[print([f"{i:.1f}" for i in row]) for row in Y]


"""
$ python layers_21_matrix_and.py
[0, 0, 1, 1]
[0, 1, 0, 1]

[0.845, 0.845]

['0.5', '0.7', '0.7', '0.8']
"""
