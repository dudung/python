import numpy as np

m = np.array(
  [
    [1, 2],
    [3, 4],
    [5, 6],
  ]  
)

s = m.shape

print("m =")
print(m)
print()
print("(rows, cols) =", s)
print("rows =", s[0])
print("cosl =", s[1])

"""
$ python shape.py
m =
[[1 2]
 [3 4]
 [5 6]]

(rows, cols) = (3, 2)
rows = 3
cosl = 2
"""
