from data import dataset1 as ds1
import datalibs as dl

import sys
sys.path.append("../")

import matrix.matrix as mtx

x1 = [dl.columnof(0, ds1)]
x2 = [dl.columnof(1, ds1)]
y = dl.columnof(2, ds1)

X1 = mtx.stackrows(x1, x2)
Y = mtx.tpose([y])

print(X1)
print(Y)


"""
$ python prepare_data.py
[[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]]
[[0], [0], [1], [1], [0], [0], [1], [1], [0], [0], [1], [1], [0], [0], [1], [1]]
"""
