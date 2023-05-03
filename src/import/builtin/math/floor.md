# ceil
$$\tag{1}
y = \lfloor x \rfloor 
$$


```shell
$ python floor.py
x       y
-3.2    -4
-2.7    -3
-1.5    -2
-0.5    -1
0       0
0.7     0
1.2     1
2.5     2
```


```python
import math

nums = [-3.2, -2.7, -1.5, -0.5, 0, 0.7, 1.2, 2.5]

print("x", "y", sep='\t')
for x in nums:
  y = math.floor(x)
  print(x, y, sep='\t')
```
