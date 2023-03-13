x = {9.11, 'a', '+', '|', 3.1415E-31, "Hello", True, False}
for i in x:
  print(i, end=' ')
print()

for i in {9, 8, 7, 'a', 'b', 'f', 'x', True, False, False, True}:
  print(i, end=' ')
print()


"""
False True 3.1415e-31 9.11 | Hello a +
False True 7 8 9 b f x a
"""

"""
+ True False 3.1415e-31 a Hello 9.11 |
False True f a 7 8 9 b x
"""

"""
False True 3.1415e-31 + 9.11 Hello a |
False True 7 8 9 f b a x
"""
