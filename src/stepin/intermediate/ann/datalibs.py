def columnof(c, m):
  value = []
  for r in m:
    value.append(r[c])
  return value

def rowof(r, m):
  value = m[r]
  return value
