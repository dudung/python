# find_v
Relation among velocity $v$ with position $x$ at time $t$ and initial position $x_0$ at initial time $t_0$ is as follow

$$\tag{1}
v = \frac{x - x_0}{t - t_0}
$$

or

$$\tag{2}
v = \frac{\Delta x}{\Delta t}
$$

since it has a constant value.

It is not necessary that $t_0 = 0$, but it is common to use that value.

Let choose $t = \{0, 1, 2, 3, 4\}$, $x = \{1, 3, 5, 7, 9\}$ and calculate $v$ for time $t$.


```shell
$ /mdpy.sh ulm_v.md
t       v
0       2.0
1       2.0
2       2.0
3       2.0
```


```python
def v(p1, p2):
  dx = p2[1] - p1[1]
  dt = p2[0] - p1[0]
  fv = dx / dt
  return fv

t = [0, 1, 2, 3, 4]
x = [1, 3, 5, 7, 9]
N = min(len(t), len(x))

print("t\tv")
for i in range(N - 1):
  t1 = t[i]
  x1 = x[i]
  t2 = t[i+1]
  x2 = x[i+1]
  vv = v((t1, x1), (t2, x2))
  tt = t1
  print(tt, vv, sep='\t')
```
