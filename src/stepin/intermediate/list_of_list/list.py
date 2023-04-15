x = [
  [1, 2],
  [3, 4]
]

y = [
  [5, 6],
  [7, 8]
]

z = [1, 2, 3]

x[0].append(z)

for row in x:
  print(row)
print()



"""
x = [
  [1, 2, 3],
  [4, 5, 6]
]

for row in x:
  print(row)
print()

new_row = [3, 4, 5]

x.insert(0, new_row)
for row in x:
  print(row)
"""

"""
x = [1, 2, 3]
y = x.copy()
x.extend(y)
print(x)


x = [
  [1],
  ['A', 'B', 'C'],
  [True, False]
]

for row in x:
  for col in row:
    print(col, end=", ")
  print()

x.append("Hello")
print(x)

x.append([8, 7, 6, True, "Hello"])

for row in x:
  for col in row:
    print(col, end=", ")
  print()
  
print(x)
"""

"""
for row in x:
  for col in row:
    print(col)

for row in x:
  print(row)
"""