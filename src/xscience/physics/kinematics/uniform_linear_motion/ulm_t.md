# ulm_t
Relation among time $t$ with position $x$, initial position $x_0$ at time $t_0$ and velocity is as follow

$$\tag{1}
t = t_0 + \frac{x - x_0}{v}
$$

or

$$\tag{2}
t = \frac{x - x_0}{v}
$$

if it is chosen that $t_0 = 0$. It is not necessary that $t_0 = 0$, but it is common to use that value.

Let choose $x = \{1, 3, 5, 7, 9\}$, $v = 2$, $x_0 = 3$, $t_0 = 1$ and calculate $t$ for every position.


```shell
$ /mdpy.sh ulm_t.md
x       t
1       0.0
3       1.0
5       2.0
7       3.0
9       4.0
```


```python
def t(x):
  ft = t_0 + (x - x_0) / v
  return ft

v = 2
t_0 = 1
x_0 = 3
x = [1, 3, 5, 7, 9]
N = len(x)

print("x\tt")
for i in x:
  xx = i
  tt = t(xx)
  print(xx, tt, sep='\t')
```
