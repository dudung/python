# asin
$$\tag{0}
y = \sin x
$$

$$\tag{1}
x = \sin^{-1} y \equiv {\rm asin} \ y
$$


```shell
$ python asin.py
sin x   x(rad)  x(°)
0       0.000   0.0
0.25    0.253   14.5
0.5     0.524   30.0
0.75    0.848   48.6
1       1.571   90.0
```


```python
import math

x = [0, 0.25,  0.5, 0.75, 1]

print("sin x\tx(rad)\tx(°)")
for s in x:
  rad = math.asin(s)
  deg = math.degrees(rad)
  print(f"{s}\t{rad:.3f}\t{deg:.1f}")
```
