import numpy as np

m = np.array(
  [
    [1, 2, 3],
    [9, 8, 7]
  ]
)

print(m)
print()

for row in m:
  for col in row:
    print(col, end='\t')
  print()


"""
$ for_loop.py
[[1 2 3]
 [9 8 7]]

1       2       3
9       8       7
"""
