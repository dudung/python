# atan
$$\tag{0}
y = \tan x
$$

$$\tag{1}
x = \tan^{-1} y \equiv {\rm atan} \ y
$$


```shell
$ python atan.py
tan x   x(rad)  x(°)
0       0.000   0.0
0.25    0.245   14.0
0.5     0.464   26.6
0.75    0.644   36.9
1       0.785   45.0
1.333   0.927   53.1
```


```python
import math

x = [0, 0.25,  0.5, 0.75, 1, 1.333]

print("tan x\tx(rad)\tx(°)")
for s in x:
  rad = math.atan(s)
  deg = math.degrees(rad)
  print(f"{s}\t{rad:.3f}\t{deg:.1f}")
```
