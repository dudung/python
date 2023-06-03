import numpy as np

a = np.array(
  [
    [1, 2],
    [3, 4]
  ]
)

b = 2

c = a / b

print("a =")
print(a)
print()

print("b =")
print(b)
print()

print("c =")
print(c)


"""
$ python div_scalar.py
a =
[[1 2]
 [3 4]]

b =
2

c =
[[0.5 1. ]
 [1.5 2. ]]
"""
