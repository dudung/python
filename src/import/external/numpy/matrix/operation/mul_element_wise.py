import numpy as np

a = np.array(
  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 29]
  ]
)

b = np.array(
  [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0]
  ]
)

c = a * b

print("a =")
print(a)
print()

print("b =")
print(b)
print()

print("c =")
print(c)


"""
$ python mul_element_wise.py
mul_element_wise.py
a =
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8 29]]

b =
[[1 0 0]
 [0 1 0]
 [0 1 0]]

c =
[[1 0 0]
 [0 5 0]
 [0 8 0]]
"""
