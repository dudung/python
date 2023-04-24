import mtxlib as mtx

a = [
  [1, 2, 3],
  [4, 5, 6]
]


b = [
  [1, 0.5, 3],
  [2, 1, 0.5]
]

c = mtx.hadamard(a, b)

print(a, '\n')
print(b, '\n')
print(c)


"""
$ python hadamard_product.py
[[1, 2, 3], [4, 5, 6]]

[[1, 0.5, 3], [2, 1, 0.5]]

[[1, 1.0, 9], [8, 5, 3.0]]
"""
