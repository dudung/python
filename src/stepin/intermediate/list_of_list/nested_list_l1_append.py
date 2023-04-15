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

x.append(l2)
print(x)

x.append(l3)
print(x)


"""
$ append nested_list_l1_append.py
[9, 8, 7]
[9, 8, 7, 1]
[9, 8, 7, 1, [1, 2]]
[9, 8, 7, 1, [1, 2], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
"""
