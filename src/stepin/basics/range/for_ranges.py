r1 = range(1, 10)
r2 = range(101, 110)
for i in (r1, r2):
  for j in i:
    print(j, end=' ')
print()


"""
1 2 3 4 5 6 7 8 9 101 102 103 104 105 106 107 108 109
"""
