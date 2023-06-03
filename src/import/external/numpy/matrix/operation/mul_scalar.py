import numpy as np

a = np.array(
  [
    [1, 2],
    [3, 4]
  ]
)

b = 2

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
$ python mul_scalar.py
a =
[[1 2]
 [3 4]]

b =
2

c =
[[2 4]
 [6 8]]
"""
