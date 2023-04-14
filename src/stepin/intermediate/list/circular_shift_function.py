def shr1(z):
  y = z.pop()
  x.insert(0, y)
  
def shl1(z):
  y = z.pop(0)
  x.append(y)


x = [1, 2, 3, 4, 5]
print(x)
print()

n = len(x)

for i in range(0, n):
  shr1(x)
  print(x)
print()

for i in range(0, n):
  shl1(x)
  print(x)


"""
python circular_shift_function.py
[1, 2, 3, 4, 5]

[5, 1, 2, 3, 4]
[4, 5, 1, 2, 3]
[3, 4, 5, 1, 2]
[2, 3, 4, 5, 1]
[1, 2, 3, 4, 5]

[2, 3, 4, 5, 1]
[3, 4, 5, 1, 2]
[4, 5, 1, 2, 3]
[5, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
"""
