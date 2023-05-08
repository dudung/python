def polynom(x, coefs):
  n = len(coefs)
  y = 0
  for i in range(n-1, -1, -1):
    c = coefs[i]
    y = y * x + c
  return y

def diff(x):
  n = len(x)
  m = range(n-1)
  y = [x[i+1] - x[i] for i in m]
  return y

def series(xbeg, xend, coefs):
  y = []
  for x in range(xbeg, xend+1):
    f = polynom(x, coefs)
    y.append(f)
  return y

y = series(0, 10, [1, 1, 1, 1])
dy = diff(y)
d2y = diff(dy)
d3y = diff(d2y)

n = len(y)
print("$i$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$")
print(":-: | :-: | :-: | :-: | :-:")
for i in range(n):
  print(i, end=" | ")
  print(y[i], end=" | ")
  if i < len(dy): print(dy[i], end=" | ")
  else:
    print(end=" | ")
  if i < len(d2y): print(d2y[i], end=" | ")
  else:
    print(end=" | ")
  if i < len(d3y): print(d3y[i], end=" | ")
  else:
    print(end=" | ")
  print()


"""
$ python polynom_terms_diffs.py
i       y       dy      d2y     d3y
0       1       3       8       6
1       4       11      14      6
2       15      25      20      6
3       40      45      26      6
4       85      71      32      6
5       156     103     38      6
6       259     141     44      6
7       400     185     50      6
8       585     235     56
9       820     291
10      1111
"""
