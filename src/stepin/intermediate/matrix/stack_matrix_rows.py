import matrix as mtx

m1 = mtx.zero(2, 3)
m1[0] = [1, 2, 3]
print(m1)

m2 = mtx.zero(1, 3)
m2[0] = [3, 2, 1]
print(m2)

m3 = mtx.stackrows(m1, m2)
print(m3)


"""
$ python stack_matrix_rows.py
[[1, 2, 3], [0, 0, 0]]
[[3, 2, 1]]
[[1, 2, 3], [0, 0, 0], [3, 2, 1]]
"""
