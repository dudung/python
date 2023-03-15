def minlen(*args):
  n = len(args[0])
  for i in args:
    n = min(n, len(i))
  return n

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
  m = minlen(*args)
  n = len(args)
  s = []
  for i in range(m):
    ei = []
    for j in range(n):
      ei.append(args[j][i])
    p = prod(*ei)
    s.append(p)
  sp = sum(*s)
  return sp
  
x = [1, 2, 3, 4]
y = [2, 2, 2, 2]
z = [0, -1, 0, 1]

print("x  y   z")
for i in range(min(len(x), len(y), len(z))):
  print(f"{x[i]:1d}, {y[i]:1d}, {z[i]:2d}")

sp = sumprod(x, y, z)
print("summprod =", sp)
"""
x  y   z
1, 2,  0
2, 2, -1
3, 2,  0
4, 2,  1
summprod = 4
"""
