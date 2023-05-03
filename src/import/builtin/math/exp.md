# exp
$$\tag{1}
y = e^x
$$


```shell
$ python exp.py
x       y=e^x
0       1.0
1       2.718281828459045
2       7.38905609893065
3       20.085536923187668
4       54.598150033144236
```


```python
import math

nums = [0, 1, 2, 3, 4]

print("x", "y=e^x", sep='\t')
for x in nums:
  y = math.exp(x)
  print(x, y, sep='\t')
```
