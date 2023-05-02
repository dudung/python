# constant
$$\tag{1}
\lim_{x \to a} c = c, \ \ \ \ c \ne c(x)
$$


```shell
$ ../../../../../scripts/mdpy.sh constant.md
f(x) = c
c = 1
a = 2
lim x --> 1     f(x) = 1
lim x --> 1.9   f(x) = 1
lim x --> 1.99  f(x) = 1
lim x --> 1.999 f(x) = 1
lim x --> 2.001 f(x) = 1
lim x --> 2.01  f(x) = 1
lim x --> 2.1   f(x) = 1
lim x --> 3     f(x) = 1

c = c
a = a
f(x) = c
lim x --> a f(x) = c
```


```python
# numerical method
def f(x):
  return c
print("f(x) = c")

c = 1
a = 2
limit = [1, 1.9, 1.99, 1.999, 2.001, 2.01, 2.1, 3]
print("c =", c)
print("a =", a)

for x in limit:
  print("lim x -->", f"{x:<5}", "f(x) =", f(x))
print()

# symbolic method
from sympy import *
x, c, a = symbols("x c a")
f = c
lim = limit(f, x, 0)

print("c =", c)
print("a =", a)
print("f(x) =", f)
print("lim x --> a f(x) =", lim)
```
