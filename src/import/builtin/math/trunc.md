# trunc
$$\tag{1}
y = \left\{
\begin{array}{cc}
\lceil x \rceil, & x < 0 \newline
0, & x = 0 \newline
\lfloor x \rfloor, & x > 0
\end{array}
\right.
$$

$$\tag{2}
y = [x] 
$$


```shell
$ python trunc.py
x       y
-3.2    -3
-2.7    -2
-1.5    -1
-0.5    0
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
  y = math.trunc(x)
  print(x, y, sep='\t')
```
