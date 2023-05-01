# diff_xv
$$\tag{1}
v = \frac{dx}{dt}
$$

$$\tag{2}
a = \frac{dv}{dt}
$$

$$\tag{3}
\begin{array}{rcl}
x & = & x_0 + v_0 \cdot (t - t_0) \newline
& = & (x_0 - v_0 \ t_0) + v_0 \ t \newline
v & = & \displaystyle \frac{dx}{dt} \newline
& = & \displaystyle \frac{d}{dt} \left[ x_0 + v_0 \cdot (t - t_0) \right] \newline
& = & v_0 \newline
a & = & \displaystyle \frac{dv}{dt} \newline
& = & \displaystyle \frac{d}{dt} \left[ v_0 \right] \newline
& = & 0
\end{array}
$$


```shell
$  ../../../../../scripts/mdpy.sh diff_xv.md
x = v0*(t - t0) + x0
v = v0
a = 0
```


```python
from sympy import *
x, v, a, t, x0, v0, t0 = symbols("x v a t x0 v0 t0")

x = x0 + v0 * (t - t0)
print("x =", x)

v = diff(x, t)
print("v =", v)

a = diff(v, t)
print("a =", a)
```
