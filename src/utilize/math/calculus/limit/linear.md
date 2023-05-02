# constant
$$\tag{1}
\lim_{x \to a} mx + b = ma + b
$$


```shell
$ ../../../../../scripts/mdpy.sh linear.md
m = 2
b = 1
f(x) = 2x + 1
a = 2
lim x --> 1     f(x) = 3
lim x --> 1.9   f(x) = 4.8
lim x --> 1.99  f(x) = 4.98
lim x --> 1.999 f(x) = 4.998
lim x --> 2.001 f(x) = 5.002
lim x --> 2.01  f(x) = 5.02
lim x --> 2.1   f(x) = 5.2
lim x --> 3     f(x) = 7

m = m
b = b
a = a
f(x) = b + m*x
lim x --> a f(x) = a*m + b
```


```python
# numerical method
def f(x):
  return m*x + b

m = 2
b = 1
print("m =", m)
print("b =", b)
print("f(x) = ", m, "x + ", b, sep='')

a = 2
limit = [1, 1.9, 1.99, 1.999, 2.001, 2.01, 2.1, 3]
print("a =", a)

for x in limit:
  print("lim x -->", f"{x:<5}", "f(x) =", f(x))
print()

# symbolic method
from sympy import *
x, m, b, a = symbols("x m b a")
f = m*x + b
lim = limit(f, x, a)

print("m =", m)
print("b =", b)
print("a =", a)
print("f(x) =", f)
print("lim x --> a f(x) =", lim)
```
