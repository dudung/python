import random as r

x = ["A", "B", "C", "D", "E"]

for i in range(20):
  y = r.choice(x)
  print(y, end='')
print()


"""
$ python choice.py
CEACCBCBCCECBCACEDAB
"""
