import matrix as mtx

x = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]
print(x)

def f(x):
  return x**2 - 1

y = mtx.map(x, f)
print(y)


"""
$ python map_matrix.py
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[0, 3, 8], [15, 24, 35], [48, 63, 80]]
"""
