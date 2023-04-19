import math
def sigmoid(z):
  return 1 / (1 + math.exp(-z))

import sys
sys.path.append("../")

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

X2 = mtx.map(mtx.mul(W21, X1), sigmoid)
X3 = mtx.map(mtx.mul(W32, X2), sigmoid)
X4 = mtx.map(mtx.mul(W43, X3), sigmoid)

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
$ python layers_2321_feedforward.py
X1
[0, 0, 1, 1]
[0, 1, 0, 1]

X2
[0.50, 0.73, 0.73, 0.88]
[0.50, 0.73, 0.73, 0.88]
[0.50, 0.73, 0.73, 0.88]

X3
[0.82, 0.90, 0.90, 0.93]
[0.82, 0.90, 0.90, 0.93]

X4
[0.84, 0.86, 0.86, 0.87]

Y
[0, 1, 0, 1]
"""
