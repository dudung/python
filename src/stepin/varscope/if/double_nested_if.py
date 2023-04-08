x = 3
y = 4
z = 5
print(x, y, z)

if x > 4:
  y = 2
  if z < 10:
    x = 300
  else:
    x = -100
else:
  y = 100

print(x, y, z)


"""
$ python double_nested_if.py
3 4 5
3 100 5
"""
