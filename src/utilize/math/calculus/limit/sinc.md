# sinc
$$\tag{1}
\lim_{x \to a} \frac{\sin x}{x} = 1
$$


```shell
$ ../../../../../scripts/mdpy.sh sinc.md
f(x) = sin(x) / x
a = 0
lim x --> -1      f(x) = 0.841470985
lim x --> -0.1    f(x) = 0.998334166
lim x --> -0.01   f(x) = 0.999983333
lim x --> -0.001  f(x) = 0.999999833
lim x --> -0.0001 f(x) = 0.999999998
lim x --> +0.0001 f(x) = 0.999999998
lim x --> +0.001  f(x) = 0.999999833
lim x --> +0.01   f(x) = 0.999983333
lim x --> +0.1    f(x) = 0.998334166
lim x --> +1      f(x) = 0.841470985

a = 0
f(x) = sin(x)/x
lim x --> a f(x) = 1
```


```python
import math

# numerical method
def f(x):
  return math.sin(x) / x

print("f(x) = sin(x) / x")

a = 0
print("a =", a)
limit = [
  -1, -0.1, -0.01, -0.001, -0.0001,
  0.0001, 0.001, 0.01, 0.1, 1
]

for x in limit:
  print("lim x -->", f"{x:<+7}", "f(x) =", f"{f(x):0.9}")
print()

# symbolic method
from sympy import *
x = symbols("x")
a = 0
f = sin(x) / x
lim = limit(f, x, a)

print("a =", a)
print("f(x) =", f)
print("lim x --> a f(x) =", lim)
```
