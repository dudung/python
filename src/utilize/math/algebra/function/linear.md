# linear
$$\tag{1}
f(x) = mx + b
$$

```shell
$ ../../../../../scripts/mdpy.sh linear.md
m = 2
b = 3
f(x) = 2x + 3
x       f(x)
0       3
1       5
2       7
3       9
4       11

f(x) = b + m*x
x       f(x)
0       b
1       b + m
2       b + 2*m
3       b + 3*m
4       b + 4*m
```


```python
# numerical method
def f(x):
  return m*x + b

m = 2
b = 3
print("m =", m)
print("b =", b)
print("f(x) = ", m, "x + ", b, sep='')

nums = [0, 1, 2, 3, 4]

print("x\tf(x)")
for x in nums:
  print(x, f(x), sep='\t')
print()

# symbolic method
from sympy import *
x, m, b = symbols("x m b")
f = m * x + b
print("f(x) =", f)

print("x\tf(x)")
for i in nums:
  print(i, f.subs(x, i), sep='\t')
```
