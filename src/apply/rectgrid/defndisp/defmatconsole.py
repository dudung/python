# defmatconsole.py
# define matrix and print to console
# Sparisoma Viridi | https://github.com/dudung
# 20230801

def zero(rows, cols):
  m = []
  for i in range(rows):
    r = []
    for j in range(cols):
      c = 0
      r.append(c)
    m.append(r)
  return m

def mat2lines(m):
  s = ""
  for i in m:
    s += f"{i}" + "\n"
  return s

m1 = zero(5, 3)
print(mat2lines(m1))


"""
$ python defmatconsole.py
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
"""
