import numpy as np

m = np.array(
  [
    [1, 2, 3],
    [9, 8, 7]
  ]
)

print(m)
print()

m[0][1] = 100
print(m)


"""
$ python access_element.py
[[1 2 3]
 [9 8 7]]

[[  1 100   3]
 [  9   8   7]]
"""
