# pow
$$\tag{1}
z = x^y
$$


```shell
$ python pow.py
x       y       z=x^y
1       5       1.0
2       4       16.0
3       3       27.0
4       2       16.0
5       1       5.0
6       0       1.0
100     0.5     10.0
10      -1      0.1
4       2.5     32.0
```


```python
import math

x = [1, 2, 3, 4, 5, 6, 100, 10, 4]
y = [5, 4, 3, 2, 1, 0, 0.5, -1, 2.5]
n = min(len(x), len(y))

print("x\ty\tz=x^y")
for i in range(n):
  z = math.pow(x[i], y[i])
  print(x[i], y[i], z, sep='\t')
```
