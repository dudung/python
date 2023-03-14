i = 0
N = 10
while i < N:
  print(i, end=' ')
  i += 1
  if i == 3:
    print()
    break
else:
  print("Not shown when it has break")


i = 0
N = 10
while i < N:
  print(i, end=' ')
  i += 1
  if i == 3:
    print()
    break

print("It will always be shown")


"""
0 1 2
0 1 2
It will always be shown
"""
