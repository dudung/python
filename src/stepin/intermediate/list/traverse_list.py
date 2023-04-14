x = ['A', 'B', 'C', 'D', 1, 2, 3, 4]

for i in x:
  print(i, end=", ")
print()
print()

for i in range(len(x)):
  print(x[i], end=", ")
print()
print()

i = 0
while i < len(x):
  if i != len(x) - 1:
    print(x[i], end=", ")
  else:
    print(x[i])
  i += 1
print()

[print(i, end=", ") for i in x]
print()
print()

for i, val in enumerate(x):
  print(val, end=", ")
print()
