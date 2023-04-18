import matrix as mtx

a = [
  [1, 2, 3],
  [4, 5, 6],
]
print(a)

b = [
  [1, 1, 1],
  [2, 2, -6],
]
print(b)

c = mtx.add(a, b)
print(c)


"""
$ python add_matrix.py
[[1, 2, 3], [4, 5, 6]]
[[1, 1, 1], [2, 2, -6]]
[[2, 3, 4], [6, 7, 0]]
"""
