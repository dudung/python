# define matrix and print to console

def zero(rows, cols) {
  m = []
  for i in range(rows):
    r = []
    for j in range(cols):
      c = 0
      r.append(c)
    m.append(c)
  return m
}

m1 = zero(5, 10)
print(m1)
