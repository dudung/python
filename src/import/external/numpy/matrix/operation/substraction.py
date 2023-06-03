import numpy as np

a = np.array(
  [
    [1, 2],
    [3, 4]
  ]
)

b = np.array(
  [
    [-1, 2],
    [-2, 5]
  ]
)

c = a - b

print("a =")
print(a)
print()

print("b =")
print(b)
print()

print("c =")
print(c)


"""
$ python substraction.py
a =
[[1 2]
 [3 4]]

b =
[[-1  2]
 [-2  5]]

c =
[[ 2  0]
 [ 5 -1]]
"""
