import math

nums = [-1.2, 2.3, -3.4, 4.5]
sign = [20.2, 100.9, -30.7, -59.2]

print("n\ts\tcopysign(n,s)")
for n, s in zip(nums, sign):
  cps = math.copysign(n, s)
  print(n, s, cps, sep='\t')

"""
$ python copysign.py
n       s       copysign(n,s)
-1.2    20.2    1.2
2.3     100.9   2.3
-3.4    -30.7   -3.4
4.5     -59.2   -4.5
"""
