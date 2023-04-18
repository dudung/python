def createZeroMatrix(rnum, cnum):
  c = 0
  r = [c] * cnum
  m = [r] * rnum
  return m

def strMatrix(m, fmt=".2e"):
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

def appendRows(x, y):
  z = x + y
  return z

def appendColumns(x, y):
  z = x + y
  return z


m1 = createZeroMatrix(3, 2)
print(m1)

m2 = createZeroMatrix(1, 2)
print(m2)

m3 = appendRows(m1, m2)
print(m3)

n1 = createZeroMatrix(3, 2)
print(n1)

n2 = createZeroMatrix(3, 1)
print(n2)

n3 = appendColumns(n1, n2)
print(n3)
