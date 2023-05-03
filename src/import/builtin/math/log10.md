# log10
$$\tag{1}
y = ^{10}\log x \equiv \log x
$$


```shell
$ python log10.py
x       y=log10(x)
10000   4.0
1000    3.0
100     2.0
10      1.0
1       0.0
```


```python
import math

nums = [10000, 1000, 100, 10, 1]

print("x", "y=log10(x)", sep='\t')
for x in nums:
  y = math.log10(x)
  print(x, y, sep='\t')
```
