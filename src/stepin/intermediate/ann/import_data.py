from data import dataset1 as ds1
import datalibs as du

print("dataset1")
print(ds1)
print()

print("x1")
x1 = du.columnof(0, ds1)
print(x1)
print()

print("x2")
x2 = du.columnof(1, ds1)
print(x2)
print()

print("y")
y = du.columnof(2, ds1)
print(y)


"""
import_data_show.py
dataset1
[[0, 3, 0], [1, 3, 0], [2, 3, 1], [3, 3, 1], [0, 2, 0], [1, 2, 0], [2, 2, 1], [3, 2, 1], [0, 1, 0], [1, 1, 0], [2, 1, 1], [3, 1, 1], [0, 0, 0], [1, 0, 0], [2, 0, 1], [3, 0, 1]]

x1
[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

x2
[3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]

y
[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
"""
