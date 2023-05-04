import random as r

for i in range(20):
  x = r.randrange(0, 8, 2)
  print(x, end=' ')
print()

for i in range(20):
  x = r.randrange(7, 10)
  print(x, end=' ')
print()


"""
$ python randrange.py
2 0 2 2 6 0 0 0 4 0 4 0 0 2 6 2 2 6 4 0
9 9 9 8 8 9 7 7 8 8 9 7 8 7 8 8 8 7 7 9
"""
