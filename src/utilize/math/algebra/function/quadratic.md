# quadratic
$$\tag{1}
f(x) = ax^2 + bx + c
$$

```shell
$ ../../../../../scripts/mdpy.sh quadratic.md
a = 1
b = -4
c = 4
f(x) = 1x^2 + -4x + 4
x       f(x)
0       4
1       1
2       0
3       1
4       4

f(x) = a*x**2 + b*x + c
x       f(x)
0       c
1       a + b + c
2       4*a + 2*b + c
3       9*a + 3*b + c
4       16*a + 4*b + c
```


```python
# numerical method
def f(x):
  return a*x**2 + b*x + c

a = 1
b = -4
c = 4
print("a =", a)
print("b =", b)
print("c =", c)
print("f(x) = ", a, "x^2 + ", b, "x + ", c, sep='')

nums = [0, 1, 2, 3, 4]

print("x\tf(x)")
for x in nums:
  print(x, f(x), sep='\t')
print()

# symbolic method
from sympy import *
x, a, b, c = symbols("x a b c")
f = a*x**2 + b*x + c
print("f(x) =", f)

print("x\tf(x)")
for i in nums:
  print(i, f.subs(x, i), sep='\t')
```
