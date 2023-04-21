from data import dataset1 as ds1
import datalibs as dl

import sys
sys.path.append("../")

import matrix.matrix as mtx

x1 = [dl.columnof(0, ds1)]
x2 = [dl.columnof(1, ds1)]
X1 = mtx.stackrows(x1, x2)

y = dl.columnof(2, ds1)
Y = mtx.tpose([y])

W21 = mtx.zero(3, 2)
dl.randomize(W21)

W32 = mtx.zero(2, 3)
dl.randomize(W32)

W43 = mtx.zero(1, 2)
dl.randomize(W43)

X2 = mtx.map(mtx.mul(W21, X1), dl.sigmoid)
X3 = mtx.map(mtx.mul(W32, X2), dl.sigmoid)
X4 = mtx.map(mtx.mul(W43, X3), dl.sigmoid)

YC = mtx.tpose(X4)
dl.roundmat(YC, 3)

print(Y)
print(YC)

erri = dl.sqrdiff(Y, Y)
print(erri)


"""
$ python net2321_dataset1_ff_err.py
"""
