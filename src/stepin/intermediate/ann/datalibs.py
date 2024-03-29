import random
import math
import copy

def randomize(m):
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = 0.01 * random.randint(-100, 100)

def randomized(n):
  m = copy.deepcopy(n)
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = 0.01 * random.randint(-100, 100)
  return m

def roundmat(m, ndigits):
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = round(m[r][c], ndigits)

def columnof(c, m):
  value = []
  for r in m:
    value.append(r[c])
  return value

def rowof(r, m):
  value = m[r]
  return value

def sigmoid(z):
  return 1 / (1 + math.exp(-z))

def relu(z):
  return max(0, z)

def sqrdiff(x, y): # to-do mismatch dimension of x and y matrices
  rnum = min(len(x), len(y))
  cnum = min(len(x[0]), len(y[0]))
  m = []
  for i in range(rnum):
    row = []
    for j  in range(cnum):
      diff = x[i][j] - y[i][j]
      sqr = diff * diff
      row.append(sqr)
    m.append(row)
  return m

def mulscalar(z):
  eta = 0.001
  return -eta * z

def grad(dval, dm):
  rnum = len(dm)
  cnum = len(dm[0])
  g = []
  for i in range(rnum):
    row = []
    for j in range(cnum):
      row.append(dval / dm[i][j])
    g.append(row)
  return g
