x = [
  ['A', 'B', 'C'],
  [1],
  [True, False],
  [None],
  [1.253, -0.001, 9.3E-3, 100000.25]
]

print(x)
print()

for row in x:
  print(row)
print()

for row in x:
  for col in row:
    print(col, end=", ")
  print()


"""
$ python print.py
[['A', 'B', 'C'], [1], [True, False], [None], [1.253, -0.001, 0.0093, 100000.25]]

['A', 'B', 'C']
[1]
[True, False]
[None]
[1.253, -0.001, 0.0093, 100000.25]

A, B, C,
1,
True, False,
None,
1.253, -0.001, 0.0093, 100000.25,
"""
