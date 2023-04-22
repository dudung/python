import copy
import random
import math

# create zero matrix with rnum rows and cnum columns
def zero(rnum, cnum):
  m = []
  for r in range(rnum):
    r = []
    for c in range(cnum):
      c = 0
      r.append(c)
    m.append(r)
  return m

# get string representation of matrix
def mat2str(m, fmt=".2e"):
  mstr = ""
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    rstr = ""
    for c in range(cnum):
      cstr = f"{m[r][c]:{fmt}}"
      rstr += cstr
      rstr += " "
    rstr += "\n"
    mstr += rstr
  return mstr

# stack rows of two matrices -- to-do unmacth dimension
def stackrows(x, y):
  z = x + y
  return z

# stack columns of two matrices -- to-do unmacth dimension
def stackcols(x, y):
  rnum = len(x)
  cnum = len(y[0])
  z = x.copy()
  for r in range(rnum):
    for c in range(cnum):
      z[r].append(y[r][c])
  return z

# addition of two matrices -- to-do unmacth dimension
def add(x, y):
  rnum = min(len(x), len(y))
  cnum = min(len(x[0]), len(y[0]))
  z = zero(rnum, cnum)
  for i in range(rnum):
    for j in range(cnum):
      z[i][j] = x[i][j] + y[i][j]
  return z

# substraction of two matrices -- to-do unmacth dimension
def sub(x, y):
  rnum = min(len(x), len(y))
  cnum = min(len(x[0]), len(y[0]))
  z = zero(rnum, cnum)
  for i in range(rnum):
    for j in range(cnum):
      z[i][j] = x[i][j] - y[i][j]
  return z

# multiplication of two matrices -- to-do unmacth dimension
def mul(x, y):
  rnum = len(x)
  mnum = min(len(x[0]), len(y))
  cnum = len(y[0])
  z = zero(rnum, cnum)
  for i in range(rnum):
    for j in range(cnum):
      s = 0
      for k in range(mnum):
        s += x[i][k] * y[k][j]
      z[i][j] = s
  return z

# map input matrix to output one via a function
def map(x, f):
  rnum = len(x)
  cnum = len(x[0])
  y = zero(rnum, cnum)
  for r in range(rnum):
    for c in range(cnum):
      y[r][c] = f(x[r][c])
  return y

# transpose a matrix
def tpose(x):
  rnum = len(x)
  cnum = len(x[0])
  y = zero(cnum, rnum)
  for r in range(rnum):
    for c in range(cnum):
      y[c][r] = x[r][c]
  return y

# trace of a square matrix
def trace(x):
  num = len(x)
  y = 0
  for i in range(num):
    y += x[i][i]
  return y

# get number of rows and colums of a matrix
def getinfo(m):
  rnum = len(m)
  cnum = len(m[0])
  return rnum, cnum

# randomize a matrix, initial matrix is changed
def randomize(m):
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = 0.01 * random.randint(-100, 100)

# randomize a matrix, return the result as new matrix
def randomized(n):
  m = copy.deepcopy(n)
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = 0.01 * random.randint(-100, 100)
  return m

# round matrix element to float with some digits
def roundmat(m, ndigits):
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    for c in range(cnum):
      m[r][c] = round(m[r][c], ndigits)

# obtain column c of a matrix
def columnof(c, m):
  value = []
  for r in m:
    value.append(r[c])
  return value

# obtain row r of a matrix
def rowof(r, m):
  value = m[r]
  return value

# square difference of two matrices
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

# gradient of value for change of matrix elements
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
