import matrix as mtx

a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
]

b = mtx.tpose(a)

[print(i) for i in a]
print()
[print(i) for i in b]


"""
$ python tpose_matrix.py
[1, 2, 3, 4]
[5, 6, 7, 8]

[1, 5]
[2, 6]
[3, 7]
[4, 8]
"""
