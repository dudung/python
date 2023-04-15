l1 = 1
l2 = [1, 2]
l3 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

x = [9, 8, 7]
print(x)

x.append(l1)
print(x)

x.extend(l2)
print(x)

y = []
[y.extend(i) for i in l3]
x.extend(y)
print(x)

"""
nested_list_l1_extend.py
[9, 8, 7]
[9, 8, 7, 1]
[9, 8, 7, 1, 1, 2]
[9, 8, 7, 1, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
