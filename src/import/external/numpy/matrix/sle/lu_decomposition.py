import numpy as np

print("ax = b")
print()

a = np.array(
  [
    [1, 2, 3, 4],
    [2, 3, 1, 1],
    [1, 3, 1, 3],
    [1, 2, 2, 1]  
  ]
)
print("a =")
print(a)
print()

b = np.array([21, 20, 20, 14])
print("b =")
print(b)
print()

x = np.linalg.solve(a, b)
print("x =")
print(x)


"""
$ python lu_decomposition.py
ax = b

a =
[[1 2 3 4]
 [2 3 1 1]
 [1 3 1 3]
 [1 2 2 1]]

b =
[21 20 20 14]

x =
[4. 3. 1. 2.]
"""
