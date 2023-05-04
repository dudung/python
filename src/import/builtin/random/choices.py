import random as r

x = ["A", "B", "C", "D", "E"]

for i in range(1, 10):
  y = r.choices(x, weights=[1, 10, 1, 1, 1], k=i)
  print('-'.join(y))
print()


"""
$ python choices.py
B
B-E
B-B-B
B-B-A-B
A-B-C-C-E
B-B-E-B-A-B
B-E-B-B-B-B-B
B-B-C-B-B-B-C-B
B-B-B-B-B-B-B-C-B
"""
