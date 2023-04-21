from data import dataset1 as ds1
import datalibs as dl

import sys
sys.path.append("../")

import matrix.matrix as mtx

# get dataset
x1 = [dl.columnof(0, ds1)]
x2 = [dl.columnof(1, ds1)]
y = dl.columnof(2, ds1)

# prepare data in 2d-matrix
X1 = mtx.stackrows(x1, x2)
Y = mtx.tpose([y])

# define matrices for weights, zero matrices
W21 = mtx.zero(3, 2)
W32 = mtx.zero(2, 3)
W43 = mtx.zero(1, 2)

# initiate with random values [-1.00, 1.00]
dl.randomize(W21)
dl.randomize(W32)
dl.randomize(W43)

# perform feedforward
X2 = mtx.map(mtx.mul(W21, X1), dl.sigmoid)
X3 = mtx.map(mtx.mul(W32, X2), dl.sigmoid)
X4 = mtx.map(mtx.mul(W43, X3), dl.sigmoid)

print("X4")
print(mtx.getinfo(X4))
dl.roundmat(X4, 3)
print(mtx.tpose(X4))
print()

print("Y")
print(mtx.getinfo(Y))
print(Y)


"""
$ python net2321_dataset1_ff.py
X4
(1, 16)
[[0.559], [0.555], [0.552], [0.55], [0.562], [0.558], [0.554], [0.551], [0.567], [0.561], [0.556], [0.552], [0.573], [0.566], [0.56], [0.554]]

Y
(16, 1)
[[0], [0], [1], [1], [0], [0], [1], [1], [0], [0], [1], [1], [0], [0], [1], [1]]
"""
