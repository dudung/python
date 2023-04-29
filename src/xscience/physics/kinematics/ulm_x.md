# ulm_x
Relation among position $x$ at time $t$ with velocity $v$ and initial position $x_0$ at initial time $t_0$ is as follow

$$\tag{1}
x \equiv x(t) = x_0 + v \cdot (t - t_0).
$$

If $t = t_0$ then

$$\tag{2}
x = x(t_0) = x_0.
$$

It is not necessary that $t_0 = 0$, but it is common to use that value.

Let choose $t_0 = 1$, $x_0 = 3$, $v = 2$, and calculate $x$ for time $t$ from $t_{\rm beg} = 0$ until $t_{\rm end} = 4$.


```shell
$ ./mdpy.sh ulm_x.md
t       x
0       1
1       3
2       5
3       7
4       9
```


```python
def x(t):
  fx = x_0 + v * (t - t_0)
  return fx

t_0 = 1
x_0 = 3
v = 2
t_beg = 0
t_end = 4

print("t\tx")
for t in range(t_beg, t_end + 1):
  print(t, x(t), sep='\t')

```