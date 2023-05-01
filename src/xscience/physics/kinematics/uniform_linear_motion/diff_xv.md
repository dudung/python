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
v & = & \displaystyle \frac{dx}{dt} \newline
& = & \displaystyle \frac{d}{dt} \left[ x_0 + v_0 \cdot (t - t_0) \right] \newline
& = & v_0 \newline
a & = & \displaystyle \frac{dv}{dt} \newline
& = & \displaystyle \frac{d}{dt} \left[ v_0 \right] \newline
& = & 0
\end{array}
$$

$$\tag{4}
\begin{array}{rcl}
x & = & (x_0 - v_0 \ t_0) + v_0 \ t \newline
\end{array}
$$


```python
t0 = [1, 0, 2, 1, 0]
v0 = [2, 1, 3, 2, 2]
x0 = [4, 0, 8, 4, 1]

N = min(len(t0), len(v0), len(x0))

print("t\tx1\tx2\tx3\tx4\tx5")
for i in range(N):
tt = i

```
