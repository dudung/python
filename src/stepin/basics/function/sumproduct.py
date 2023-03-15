def sum(*args):
  s = 0
  for i in args:
    s += i
  return s

def prod(*args):
  p = 1
  for i in args:
    p *= i
  return p

def sumprod(*args):
  sp = 0
  for i in args:
    pass

x = [1, 2, 3, 4]
y = [2, 2, 2, 2]
z = [1, -1, 1, -1]
sp = sumprod(x, y, z)

print("x  y   z")
for i in range(min(len(x), len(y), len(z))):
    print(f"{x[i]:1d}, {y[i]:1d}, {z[i]:2d}")

"""
"""
