# sqrt
$$\tag{1}
y = \sqrt{x}
$$


```shell
$ ../../../../scripts/mdpy.sh sqrt.md
x       y
0       0.0
1       1.0
2       1.4142135623730951
3       1.7320508075688772
4       2.0
5       2.23606797749979
6       2.449489742783178
7       2.6457513110645907
8       2.8284271247461903
9       3.0
```


```python
import math

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("x", "y", sep='\t')
for x in nums:
  y = math.sqrt(x)
  print(x, y, sep='\t')
```
