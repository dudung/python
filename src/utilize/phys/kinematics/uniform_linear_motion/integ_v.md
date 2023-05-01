# integ_v
$$\tag{1}
x = \int v_0 \ dt
$$

$$\tag{2}
x - x_0 = \int_{t_0}^t v_0 \ dt
$$

$$\tag{3}
x = x(t), \ \ \ \ x_0 = x(t_0)
$$


```shell
$  ../../../../../scripts/mdpy.sh integ_v.md
v = v0
x = t*v0
x = t*v0 - t0*v0 + x0
```


```python
from sympy import *
x, v, t, x0, v0, t0 = symbols("x v t x0 v0 t0")

v = v0
print("v =", v)

x = integrate(v, t)
print("x =", x)

x = x0 + integrate(v, (t, t0, t))
print("x =", x)
```
