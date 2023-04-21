import random
import math

def randomize(m):
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = 0.01 * random.randint(-100, 100)

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
  return max(0, x)
