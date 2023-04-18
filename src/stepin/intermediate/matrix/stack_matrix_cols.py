import matrix as mtx

m1 = mtx.zero(2, 3)
m1[0][0] = 1
m1[1][0] = 2
print(m1)

m2 = mtx.zero(2, 1)
m2[0][0] = 3
m2[1][0] = 4
print(m2)

m3 = mtx.stackcols(m1, m2)
print(m3)


"""
$ python stack_matrix_cols.py
[[1, 0, 0], [2, 0, 0]]
[[3], [4]]
[[1, 0, 0, 3], [2, 0, 0, 4]]
"""
