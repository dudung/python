import matrix as mtx

a = [
  [1, 2, 3],
  [4, 5, 6],
]
print(a)

b = [
  [0, 2, 3],
  [3, 5, 5],
]
print(b)

c = mtx.sub(a, b)
print(c)


"""
$ python sub_matrix.py
[[1, 2, 3], [4, 5, 6]]
[[0, 2, 3], [3, 5, 5]]
[[1, 0, 0], [1, 0, 1]]
"""
