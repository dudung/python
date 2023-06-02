import numpy as np

m1 = np.array(
  [1, 2, 3]
)
s1 = m1.shape

m2 = np.array(
  [
    [1, 2, 3],
    [3, 4, 5],
  ]
)
s2 = m2.shape

m3 = np.array(
  [
    [
      [1, 2, 3, 0],
      [4, 5, 6, 0],
    ],
    [
      [0, 0, 0, 0],
      [1, 1, 1, 0],
    ],
    [
      [2, 2, 2, 0],
      [3, 3, 3, 0],
    ],
  ]
)
s3 = m3.shape

print("m1 =")
print(m1)
print()
print("shape1 =", s1)
print()

print("m2 =")
print(m2)
print()
print("shape2 =", s2)
print()

print("m3 =")
print(m3)
print()
print("shape3 =", s3)
print()

"""
$ python shape_123.py
m1 =
[1 2 3]

shape1 = (3,)

m2 =
[[1 2 3]
 [3 4 5]]

shape2 = (2, 3)

m3 =
[[[1 2 3 0]
  [4 5 6 0]]

 [[0 0 0 0]
  [1 1 1 0]]

 [[2 2 2 0]
  [3 3 3 0]]]

shape3 = (3, 2, 4)

"""
