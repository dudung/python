# ceil
$$\tag{1}
y = \lceil x \rceil 
$$


```shell
$ python ceil.py
x       y
-3.2    -3
-2.7    -2
-1.5    -1
-0.5    0
0       0
0.7     1
1.2     2
2.5     3
```


```python
import math

nums = [-3.2, -2.7, -1.5, -0.5, 0, 0.7, 1.2, 2.5]

print("x", "y", sep='\t')
for x in nums:
  y = math.ceil(x)
  print(x, y, sep='\t')
```
