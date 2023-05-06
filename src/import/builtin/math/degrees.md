# degrees
$$\tag{1}
y \ (^\circ) = \left( \frac{180}{\pi} \right) \ x \ ({\rm rad})
$$


```shell
$ python
degrees.py
x(rad)  y(°)
0.0000  0.0
0.5236  30.0
1.0472  60.0
1.5708  90.0
2.0944  120.0
2.6180  150.0
3.1416  180.0
```


```python
import math

pi = math.pi

nums = [0, pi/6, pi/3, pi/2, 2*pi/3, 5*pi/6, pi]

print("x(rad)\ty(°)")
for x in nums:
  y = math.degrees(x)
  print(f"{x:.4f}", f"{y:.1f}", sep='\t')
```
