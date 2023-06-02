import numpy as np

m1 = np.array(
  [1, 2, 3]
)
nd1 = m1.ndim

m2 = np.array(
  [
    [1, 2, 3],
    [3, 4, 5],
  ]
)
nd2 = m2.ndim

m3 = np.array(
  [
    [
      [1, 2, 3],
      [4, 5, 6],
    ],
    [
      [0, 0, 0],
      [1, 1, 1],
    ],
    [
      [2, 2, 2],
      [3, 3, 3],
    ],
  ]
)
nd3 = m3.ndim

print("m1 =")
print(m1)
print()
print("ndim1 =", nd1)
print()

print("m2 =")
print(m2)
print()
print("ndim2 =", nd2)
print()

print("m3 =")
print(m3)
print()
print("ndim3 =", nd3)
print()

"""
$ python ndim_123.py
m1 =
[1 2 3]

ndim1 = 1

m2 =
[[1 2 3]
 [3 4 5]]

ndim2 = 2

m3 =
[[[1 2 3]
  [4 5 6]]

 [[0 0 0]
  [1 1 1]]

 [[2 2 2]
  [3 3 3]]]

ndim3 = 3

"""
