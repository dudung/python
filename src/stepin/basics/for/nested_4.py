w = [1, 2]
x = ['a', 'b']
y = ['+', '-']
z = [True, False]

for i in w:
  for j in x:
    for k in y:
      for l in z:
        print(i, j, k, l)

"""
1 a + True
1 a + False
1 a - True
1 a - False
1 b + True
1 b + False
1 b - True
1 b - False
2 a + True
2 a + False
2 a - True
2 a - False
2 b + True
2 b + False
2 b - True
2 b - False
"""