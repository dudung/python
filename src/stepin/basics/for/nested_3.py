x = [1, 2, 3]
y = ['1a', '2b']
z = ['a1', 'b2']

for i in x:
  for j in y:
    for k in z:
      print(i, j, k)

"""
1 1a a1
1 1a b2
1 2b a1
1 2b b2
2 1a a1
2 1a b2
2 2b a1
2 2b b2
3 1a a1
3 1a b2
3 2b a1
3 2b b2
"""