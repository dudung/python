import matrix as mtx

a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 8, 7, 6],
  [5, 4, 3, 2],
]
print("a =")
[print(i) for i in a]
print()

b = mtx.trace(a)
print("Tr(a) =", b)


"""
$ python trace_matrix.py
a =
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 8, 7, 6]
[5, 4, 3, 2]

Tr(a) = 16
"""
