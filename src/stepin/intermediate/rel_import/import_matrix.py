import sys
sys.path.append("../")

import matrix.matrix as mtx

a = [
  [2, 3, 4, 5, 6],
  [1, 1, 1, 1, 1]
]

rnum, cnum = mtx.getinfo(a)
print("rows =", rnum)
print("cols =", cnum)


"""
$ python import_matrix.py
rows = 2
cols = 5
"""
