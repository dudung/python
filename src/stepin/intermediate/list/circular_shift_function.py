def shr1(z):
  y = z.pop()
  x.insert(0, y)
  
def shl1(z):
  y = z.pop(0)
  x.append(y)


x = [1, 2, 3, 4, 5]
print(x)

n = len(x)

for i in range(0, n):
  shr1(x)
  print(x)


"""
python circular_shift_function.py
"""
