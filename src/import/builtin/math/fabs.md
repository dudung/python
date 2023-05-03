# fabs
$$\tag{1}
y = |x|
$$


```shell
python fabs.py
x       y=|x|
-10     10.0
10.3    10.3
-2.5    2.5
4       4.0
0.12    0.12
-0.85   0.85
```


```python
import math

nums = [-10, 10.3, -2.5, 4, 0.12, -0.85]

print("x\ty=|x|")
for x in nums:
  y = math.fabs(x)
  print(x, y, sep='\t')
```
