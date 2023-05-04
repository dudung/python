import random as r

for i in range(10):
  x = r.uniform(10, 15)
  print(f"{x:.3f}", end=' ')
print()


for i in range(10):
  x = r.uniform(20, 23)
  print(f"{x:.3f}", end=' ')
print()

"""
$ python uniform.py
13.673 13.185 14.458 10.358 13.173 11.644 10.203 12.709 13.410 13.778
21.047 22.892 20.234 22.613 21.671 20.894 20.637 21.438 20.921 22.389
"""
