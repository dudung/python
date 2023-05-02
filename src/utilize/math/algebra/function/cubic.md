# cubic
$$\tag{1}
f(x) = ax^3 + bx^2 + cx + d
$$

```shell
$ ../../../../../scripts/mdpy.sh cubic.md
a = 1
b = 1
c = 1
f(x) = 1x^3 + 1x^2 + 1x + 1
x       f(x)
0       1
1       4
2       15
3       40
4       85

f(x) = a*x**3 + b*x**2 + c*x + d
x       f(x)
0       d
1       a + b + c + d
2       8*a + 4*b + 2*c + d
3       27*a + 9*b + 3*c + d
4       64*a + 16*b + 4*c + d
```


```python
# numerical method
def f(x):
  return a*x**3 + b*x**2 + c*x + d

a = 1
b = 1
c = 1
d = 1
print("a =", a)
print("b =", b)
print("c =", c)
print("f(x) = ", a, "x^3 + ", b, "x^2 + ", c, "x + ", d, sep='')

nums = [0, 1, 2, 3, 4]

print("x\tf(x)")
for x in nums:
  print(x, f(x), sep='\t')
print()

# symbolic method
from sympy import *
x, a, b, c, d = symbols("x a b c d")
f = a*x**3 + b*x**2 + c*x + d
print("f(x) =", f)

print("x\tf(x)")
for i in nums:
  print(i, f.subs(x, i), sep='\t')
```
