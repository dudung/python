import numpy as np

"""
# generate matrices from solution
x1 = 4
x2 = 3
x3 = 1
x4 = 2
xx = [x1, x2, x3, x4]

a1 = [1, 2, 3, 4]
a2 = [2, 3, 1, 1]
a3 = [1, 3, 1, 3]
a4 = [1, 2, 2, 1]

b1 = np.dot(a1, xx)
b2 = np.dot(a2, xx)
b3 = np.dot(a3, xx)
b4 = np.dot(a4, xx)

a = np.vstack((a1, a2, a3, a4))
print("a =")
print(a)
print()

b = np.stack((b1, b2, b3, b4))
print("b =")
print(b)
print()
"""

a = np.array(
  [
    [1, 2, 3, 4],
    [2, 3, 1, 1],
    [1, 3, 1, 3],
    [1, 2, 2, 1]  
  ]
)
print("a =")
print(a)
print()

b = np.array([21, 20, 20, 14])
print("b =")
print(b)
print()

print("ax = b")
print()

inva = np.linalg.inv(a)
print("a^-1 =")
print(inva)
print()

x = inva @ b
print("x =")
print(x)


"""
$ python inverse_or_matrix.py
ax = b

a =
[[1 2 3 4]
 [2 3 1 1]
 [1 3 1 3]
 [1 2 2 1]]

b =
[21 20 20 14]

a^-1 =
[[ 0.61538462  1.15384615 -0.84615385 -1.07692308]
 [-0.53846154 -0.38461538  0.61538462  0.69230769]
 [ 0.07692308 -0.23076923 -0.23076923  0.61538462]
 [ 0.30769231  0.07692308  0.07692308 -0.53846154]]

x =
[4. 3. 1. 2.]
"""
