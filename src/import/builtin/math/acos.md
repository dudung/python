# acos
$$\tag{0}
y = \cos x
$$

$$\tag{1}
x = \cos^{-1} y \equiv {\rm acos} \ y
$$


```shell
$ python acos.py
cos x   x(rad)  x(°)
0       1.571   90.0
0.25    1.318   75.5
0.5     1.047   60.0
0.75    0.723   41.4
1       0.000   0.0
```


```python
import math

x = [0, 0.25,  0.5, 0.75, 1]

print("cos x\tx(rad)\tx(°)")
for s in x:
  rad = math.acos(s)
  deg = math.degrees(rad)
  print(f"{s}\t{rad:.3f}\t{deg:.1f}")
```
