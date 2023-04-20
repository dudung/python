from data import dataset1 as ds1
import datalibs as du

import sys
sys.path.append("../")

import matrix.matrix as mtx

x1 = [du.columnof(0, ds1)]
x2 = [du.columnof(1, ds1)]
y = du.columnof(2, ds1)

X1 = mtx.stackrows(x1, x2)
print(X1)
