# constant
$$\tag{1}
\lim_{x \to a} c = c, \ \ \ \ c \ne c(x)
$$


```shell
$ ../../../../../scripts/mdpy.sh constant.md
f(x) = c
a = 2
lim x --> 1     f(x) = 1
lim x --> 1.9   f(x) = 1
lim x --> 1.99  f(x) = 1
lim x --> 1.999 f(x) = 1
lim x --> 2.001 f(x) = 1
lim x --> 2.01  f(x) = 1
lim x --> 2.1   f(x) = 1
lim x --> 3     f(x) = 1

g(y) = c
b = b
lim y --> b g(y) = c
```


```python
# numerical method
def f(x):
  c = 1
  return c
print("f(x) = c")

a = 2
limit = [1, 1.9, 1.99, 1.999, 2.001, 2.01, 2.1, 3]
print("a =", a)

for x in limit:
  print("lim x -->", f"{x:<5}", "f(x) =", f(x))
print()

# symbolic method
from sympy import *
y, c, b = symbols("y c b")
g = Function('g')(y)
g = c
lim = limit(g, y, 0)

print("g(y) =", g)
print("b =", b)
print("lim y --> b g(y) =", lim)
```


## refs
+ Thomas Wallace Colthurst and Craig B. Watkins (eds), Joy Nicholson, Elizabeth Shapere, Carolyn Phillips, "Calculus Summary", World Web Math, Massachusetts Institute of Technology, 10 Jan 2020, url https://web.mit.edu/wwmath/calculus/summary.html [20230502].
+ Robert Sedgewick and Kevin Wayne, "Symbolic Methods", Programming in Java, Princeton University, 16 Jul 2017, url https://introcs.cs.princeton.edu/java/92symbolic/ [20230502].
+ SymPy Development Team, "Introduction: What is Symbolic Computation?", SymPy 1.11 documentation, SymPy, 22 Aug 2022, url https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html [20230502].
