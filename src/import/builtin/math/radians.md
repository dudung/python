# radians
$$\tag{1}
y \ ({\rm rad}) = \left( \frac{\pi}{180} \right) \ x \ (^\circ)
$$


```shell
$ python radians.py
x(°)    y(rad)
0       0.0
30      0.5235987755982988
45      0.7853981633974483
60      1.0471975511965976
90      1.5707963267948966
120     2.0943951023931953
135     2.356194490192345
150     2.6179938779914944
180     3.141592653589793
```


```python
import math

x = [0, 30, 45, 60, 90, 120, 135, 150, 180]

print("x(°)\ty(rad)")
for degs in x:
  rads = math.radians(degs)
  print(degs, rads, sep='\t')
```
