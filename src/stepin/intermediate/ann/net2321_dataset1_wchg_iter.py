from data import dataset1 as ds1
import datalibs as dl

import sys
sys.path.append("../")

import matrix.matrix as mtx
import random

def mulscalar(z):
  eta = 0.001
  return -eta * z

def grad(dval, dm):
  rnum = len(dm)
  cnum = len(dm[0])
  g = []
  for i in range(rnum):
    row = []
    for j in range(cnum):
      row.append(dval / dm[i][j])
    g.append(row)
  return g

x1 = [dl.columnof(0, ds1)]
x2 = [dl.columnof(1, ds1)]
X1 = mtx.stackrows(x1, x2)

y = dl.columnof(2, ds1)
Y = mtx.tpose([y])

W21 = mtx.zero(3, 2)
W32 = mtx.zero(2, 3)
W43 = mtx.zero(1, 2)

random.seed(446)
W21_1 = dl.randomized(W21)
W32_1 = dl.randomized(W32)
W43_1 = dl.randomized(W43)

random.seed(35)
W21_2 = dl.randomized(W21)
W32_2 = dl.randomized(W32)
W43_2 = dl.randomized(W43)

X2 = mtx.map(mtx.mul(W21_1, X1), dl.sigmoid)
X3 = mtx.map(mtx.mul(W32_1, X2), dl.sigmoid)
X4 = mtx.map(mtx.mul(W43_1, X3), dl.relu)
YC = mtx.tpose(X4)
erri = dl.sqrdiff(YC, Y)
err1 = sum(mtx.tpose(erri)[0])

X2 = mtx.map(mtx.mul(W21_2, X1), dl.sigmoid)
X3 = mtx.map(mtx.mul(W32_2, X2), dl.sigmoid)
X4 = mtx.map(mtx.mul(W43_2, X3), dl.relu)
YC = mtx.tpose(X4)
erri = dl.sqrdiff(YC, Y)
err2 = sum(mtx.tpose(erri)[0])

derr = err2 - err1

dW21 = mtx.sub(W21_2, W21_1)
dW32 = mtx.sub(W32_2, W32_1)
dW43 = mtx.sub(W43_2, W43_1)

gW21 = grad(derr, dW21)
gW32 = grad(derr, dW32)
gW43 = grad(derr, dW43)

DW21 = mtx.map(gW21, mulscalar)
DW32 = mtx.map(gW32, mulscalar)
DW43 = mtx.map(gW43, mulscalar)

W21_3 = mtx.add(W21_2, DW21)
W32_3 = mtx.add(W32_2, DW32)
W43_3 = mtx.add(W43_2, DW43)

X2 = mtx.map(mtx.mul(W21_3, X1), dl.sigmoid)
X3 = mtx.map(mtx.mul(W32_3, X2), dl.sigmoid)
X4 = mtx.map(mtx.mul(W43_3, X3), dl.relu)
YC = mtx.tpose(X4)
erri = dl.sqrdiff(YC, Y)
err3 = sum(mtx.tpose(erri)[0])

print(err1, err2, err3)


"""
$ python net2321_dataset1_ff_wchg.py
8 4.446905388295627 4.4461487743838335
"""
