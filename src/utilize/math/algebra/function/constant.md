# constant
$$\tag{1}
f(x) = c, \ \ \ \ \frac{dc}{dx} = 0
$$

```shell
$ ../../../../../scripts/mdpy.sh constant.md
c = 3
f(x) = 3
x       f(x)
0       3
1       3
2       3
3       3
4       3

f(x) = c
x       f(x)
0       c
1       c
2       c
3       c
4       c
```


```python
# numerical method
def f(x):
  return c

c = 3
print("c =", c)
print("f(x) =", c)

nums = [0, 1, 2, 3, 4]

print("x\tf(x)")
for x in nums:
  print(x, f(x), sep='\t')
print()

# symbolic method
from sympy import *
c = symbols("c")
f = Function('f')(x)
f = c
print("f(x) =", f)

print("x\tf(x)")
for x in nums:
  print(x, f.subs(x, x), sep='\t')
print()
```
