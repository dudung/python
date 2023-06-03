import numpy as np

a = np.array(
  [
    [1, 2, 3],
    [0, 1, 2]
  ]
)

b = np.array(
  [
    [1, 0],
    [1, 1],
    [3, 2]
  ]
)

c = a @ b

print("a =")
print(a)
print()

print("b =")
print(b)
print()

print("c =")
print(c)


"""
$ python multiplication.py
a =
[[1 2 3]
 [0 1 2]]

b =
[[1 0]
 [1 1]
 [3 2]]

c =
[[12  8]
 [ 7  5]]
"""
